"""
Discogs API Query Tool: Connect to Discogs API and pull merchant listing data
"""

import sys
import json
import csv
import argparse
import logging
import requests


############################################################
# API
############################################################


def verify_seller_exists(api_content):
    """ Check API response to see if seller exists.
        Aborts script if seller is not found.
    """
    if 'message' in api_content:
        logging.error('Could not find username. Aborting script')
        sys.exit()


def get_seller_data(seller, api_key, api_secret):
    """Makes an API call to Discogs, verifies the user exists, and returns
    the seller's listing data.

    Args:
        seller: Username of the seller
        api_key: API key to access Discogs API
        api_secret: API secret to access Discogs API

    Returns:
        content: Python
    """
    status, sort, sort_order = 'for sale', 'price', 'desc'
    api_query = f'https://api.discogs.com/users/{seller}' \
        + f'/inventory?status={status}&sort={sort}' \
        + f'&sort_order={sort_order}&page=1&per_page=100' \
        + f'&key={api_key}&secret={api_secret}'
    try:
        req = requests.get(api_query)
        content = json.loads(req.text)
        return content
    except requests.exceptions.RequestException as error_msg:
        print(error_msg)
        sys.exit(1)


def dump_top_listing(seller, seller_data):
    """Dump most expensive record in seller's inventory into JSON file

    Args:
        seller: Username of the seller
        seller_data: Dictionary of seller's listings
    """
    output_path = f'./output/{seller}_top_listing.json'
    with open(output_path, 'w') as output:
        json.dump(seller_data['listings'][0], output, indent=4,
                  ensure_ascii=False)


def write_header(csv_writer):
    """Write the header for the CSV output for the seller's listings

    Args:
        csv_writer: csv.writer() object
    """
    csv_headers = ['listings', 'title', 'price', 'currency', 'url']
    csv_writer.writerow(csv_headers)


def dump_inventory_listings_to_csv(seller, seller_data):
    """Dump seller's inventory into CSV file

    Args:
        seller: Username of the seller
        seller_data: Dictionary of seller's listings
    """
    output_path = f'./output/{seller}_listings.csv'
    with open(output_path, 'w') as output:
        writer = csv.writer(output)
        write_header(writer)
        for item in seller_data['listings']:
            artist = item['release']['artist']
            title = item['release']['title']
            price = item['price']['value']
            currency = item['price']['currency']
            url = item['uri']
            writer.writerow([artist, title, price, currency, url])


def main(seller, api_key, api_secret):
    """Query Discogs API to get seller inventory data

    Args:
        specification: Path to JSON file with query specifications
    """

    print(f'Calling Discogs API to get user {seller}\'s inventory...')
    seller_data = get_seller_data(seller, api_key, api_secret)
    verify_seller_exists(seller_data)

    print(f'API call successful, dumping seller data')
    dump_top_listing(seller, seller_data)
    dump_inventory_listings_to_csv(seller, seller_data)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Look up Discogs seller\'s \
            most expensive records')
    parser.add_argument('--seller', help='Discogs seller username to query')
    parser.add_argument('--key', help='Discogs API key')
    parser.add_argument('--secret', help='Discogs API secret')
    args = parser.parse_args()

    main(args.seller, args.key, args.secret)
