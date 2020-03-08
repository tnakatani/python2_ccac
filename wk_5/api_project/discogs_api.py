"""
Discogs API Query Tool: Connect to Discogs API and pull merchant listing data
"""

import sys
import json
import csv
import argparse
import logging
import requests


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

    def get_seller_data(self):
        """Makes an API call to Discogs, verifies the user exists, and returns
        the seller's listing data.

        Returns:
            content: JSON data as a Python dictionary
        """
        try:
            req = requests.get(self.api_query)
            self.api_response = json.loads(req.text)
            return self.api_response
        except requests.exceptions.RequestException as error_msg:
            logging.error(error_msg)
            sys.exit(1)

    def get_top_listing(self):
        """Get most expensive listing from API response"""
        self.top_listing = self.api_response['listings'][0]

    def verify_seller_exists(self):
        """ Check API response to see if seller exists.
            Aborts script if seller is not found.
        """
        if 'message' in self.api_response:
            logging.error('Could not find seller. Aborting script')
            sys.exit()

    def show_top_listing(self):
        """ Show most expensive record in seller's inventory"""
        self.get_top_listing()
        print(self.top_listing)

    def dump_top_listing(self):
        """Dump most expensive record in seller's inventory into JSON file

        Args:
            seller: Username of the seller
            seller_data: Dictionary of seller's listings
        """
        output_path = f'./output/{self.seller}_top_listing.json'
        with open(output_path, 'w') as output:
            json.dump(self.top_listing, output, indent=4, ensure_ascii=False)

    @staticmethod
    def write_header(csv_writer):
        """Write the header for the CSV output for the seller's listings

        Args:
            csv_writer: csv.writer() object
        """
        csv_headers = ['listings', 'title', 'price', 'currency', 'url']
        csv_writer.writerow(csv_headers)

    def dump_inventory_listings_to_csv(self):
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


def parse_args():
    """Parse arguments from the CLI"""
    parser = argparse.ArgumentParser(description='Look up Discogs seller\'s \
            most expensive records')
    parser.add_argument('--seller',
                        help='Discogs seller username to query',
                        default='kittertea')
    parser.add_argument('--key',
                        help='Discogs API key',
                        default='kHMaTxVJxeCDNOuOJdqK')
    parser.add_argument('--secret',
                        help='Discogs API secret',
                        default='ykrkhBryxPLbtCtVPcMKzovBOdHNPwkz')
    return parser.parse_args()


def main():
    """Run the module"""
    args = parse_args()
    api = APICaller(args.seller, args.key, args.secret)
    api.create_api_query()
    api.get_seller_data()
    api.verify_seller_exists()
    api.dump_top_listing()
    api.dump_inventory_listings_to_csv()


if __name__ == '__main__':
    main()
