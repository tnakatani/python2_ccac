"""
Discogs API Query Tool: Connect to Discogs API and pull merchant listing data
"""

import sys
import json
import csv
import argparse
import logging
import requests


class MissingAPIKeyOrSecret(Exception):
    """Error logging for no input value"""
    def __init__(self, error_field):
        super(MissingAPIKeyOrSecret, self).__init__()
        self.msg = f'Missing API {error_field}. Aborting script.'


class InvalidAPIKeyOrSecret(Exception):
    """Error logging for no input value"""
    def __init__(self):
        super(InvalidAPIKeyOrSecret, self).__init__()
        self.msg = f'Invalid API key/secret. Aborting script.'


class SellerDoesNotExistError(Exception):
    """Error logging when Discogs seller does not exist"""
    def __init__(self, seller):
        super(SellerDoesNotExistError, self).__init__()
        self.seller = seller
        self.msg = f'Could not find seller "{seller}". Aborting script.'


class APICaller:
    """Class to make API calls"""
    def __init__(self, seller, key, secret):
        """Initialize API call config

        Args:
            seller (str): Username of the seller
            key (str): API key to access API
            secret (str): API secret to access API
        """
        self.seller = seller
        self.key = key
        self.secret = secret
        self.api_response_status_code = None
        self.api_response = None
        self.api_query = None
        self.top_listing = None

    def create_api_query(self):
        """Create API request URL"""
        status, sort, sort_order = 'for sale', 'price', 'desc'
        api_query = f'https://api.discogs.com/users/{self.seller}' \
            + f'/inventory?status={status}&sort={sort}' \
            + f'&sort_order={sort_order}&page=1&per_page=100' \
            + f'&key={self.key}&secret={self.secret}'
        self.api_query = api_query

    def validate_request(self):
        """Check if provided API key and secret is valid"""
        logging.info('Verifying API key and secret')
        if self.key is None:
            raise MissingAPIKeyOrSecret('key')
        if self.secret is None:
            raise MissingAPIKeyOrSecret('secret')
        if self.api_response_status_code == 401:
            raise InvalidAPIKeyOrSecret()

    def validate_seller(self):
        """ Check API response to see if seller exists.
            Aborts script if seller is not found.
        """
        logging.info('Verifying seller')
        # print(self.api_response_status_code)
        # print(self.api_response)
        if self.api_response_status_code == 404:
            raise SellerDoesNotExistError(self.seller)

    def get_seller_listings(self):
        """Makes an API call to Discogs, validates API key/secret and
        seller, and then sets the seller's listing data and top listing record
        as class attributes.
        """
        try:
            req = requests.get(self.api_query)
            self.api_response_status_code = req.status_code
            self.api_response = json.loads(req.text)
            self.validate_request()
            self.validate_seller()
        except requests.exceptions.RequestException as error:
            logging.error(error)
            sys.exit()
        except MissingAPIKeyOrSecret as err:
            logging.error(err.msg, exc_info=True)
            sys.exit()
        except InvalidAPIKeyOrSecret as err:
            logging.error(err.msg, exc_info=True)
            sys.exit()
        except SellerDoesNotExistError as err:
            logging.error(err.msg, exc_info=True)
            sys.exit()

    def get_top_listing(self):
        """Get most expensive listing from API response"""
        self.validate_seller()
        self.top_listing = self.api_response['listings'][0]

    def dump_top_listing(self):
        """Dump most expensive record in seller's inventory into JSON file

        Args:
            seller: Username of the seller
            seller_data: Dictionary of seller's listings
        """
        output_path = f'./output/{self.seller}_top_listing.json'
        self.get_top_listing()
        with open(output_path, 'w') as output:
            json.dump(self.top_listing,
                      output,
                      indent=4,
                      ensure_ascii=False)
        print(f'Top listing exported to {output_path}')

    def dump_listings_to_csv(self):
        """Dump seller's inventory into CSV file

        Args:
            seller: Username of the seller
            seller_data: Dictionary of seller's listings
        """
        output_path = f'./output/{self.seller}_listings.csv'
        with open(output_path, 'w') as output:
            writer = csv.writer(output)
            self.write_header(writer)
            for item in self.api_response['listings']:
                artist = item['release']['artist']
                title = item['release']['title']
                price = item['price']['value']
                currency = item['price']['currency']
                url = item['uri']
                writer.writerow([artist, title, price, currency, url])
        print(f'Listings exported to {output_path}')

    @staticmethod
    def write_header(csv_writer):
        """Write the header for the CSV output for the seller's listings

        Args:
            csv_writer: csv.writer() object
        """
        csv_headers = ['listings', 'title', 'price', 'currency', 'url']
        csv_writer.writerow(csv_headers)


def parse_args():
    """Parse arguments from the CLI"""
    parser = argparse.ArgumentParser(description='Look up Discogs seller\'s \
            most expensive records')
    parser.add_argument('--seller',
                        help='Discogs seller username to query',
                        default='black_snake_moan')
    parser.add_argument('--key',
                        help='Discogs API key (required)')
    parser.add_argument('--secret',
                        help='Discogs API secret (required)')
    return parser.parse_args()


def main():
    """Run the module"""
    args = parse_args()
    api = APICaller(args.seller, args.key, args.secret)
    api.create_api_query()
    api.get_seller_listings()
    api.dump_top_listing()
    api.dump_listings_to_csv()


if __name__ == '__main__':
    main()
