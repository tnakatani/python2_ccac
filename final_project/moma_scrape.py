"""Scrape data from the Museum of Modern Art's online collection.

"""

import urllib.request
import logging
import csv
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd


class ArtworkSoup(BeautifulSoup):
    def __init__(self):
        self.url_ids = []
        self.htmls = []
        self.artwork_data = []

    @staticmethod
    def build_url(url_id):
        """Build a url to query MoMA website"""
        url = (f'https://www.moma.org/collection/works/{url_id}')
        return url

    @staticmethod
    def get_response(url):
        """Get HTML response from url"""
        req = urllib.request.Request(url)
        try:
            response = urllib.request.urlopen(req)
        except urllib.error.HTTPError as e:
            logging.info(e.code)
        else:
            return response.read()

    def scrape(self, url_ids):
        """Create a BeautifulSoup class from multiple URLs"""
        for url_id in url_ids:
            url = self.build_url(url_id)
            response = self.get_response(url)
            if response:
                logging.debug('Scraping URL ID: %s', url_id)
                html = BeautifulSoup(response, "html.parser")
                data = self.get_artwork_data(html)
                data_dict = self.make_artwork_dict(url_id, data)
                self.artwork_data.append(data_dict)

    def get_artwork_data(self, html):
        """Extract artwork data from HTMLs and aggregate into dictionaries

        """
        main = html.find('h1')
        artist = main.select('span')[0].get_text(strip=True)
        title = main.select('span')[1].get_text(strip=True)
        date = main.select('span')[2].get_text(strip=True)
        desc_key = map(self.clean_html,
                       html.find_all(
                           'span',
                           'work__caption__term__text'))
        desc_value = map(self.clean_html,
                         html.find_all(
                             'span',
                             'work__caption__description__text'))
        return (artist, title, date, desc_key, desc_value)

    @staticmethod
    def make_artwork_dict(art_id, data):
        """Build a dictionary from scraped data"""
        artwork_dict = {}
        artwork_dict['id'] = art_id
        artwork_dict['artist'] = data[0]
        artwork_dict['title'] = data[1]
        artwork_dict['date'] = data[2]
        artwork_dict.update(dict(zip(data[3], data[4])))
        return artwork_dict

    @staticmethod
    def clean_html(html):
        """Strip tag and newline characters"""
        # Some descriptions have <em> tags within the <span> tag.
        return html.get_text(strip=True).lower()

def write_to_csv(data_dict, out_path='artwork_data.csv'):
    try:
        with open(out_path, 'w') as f:
            header = list(data_dict[-1].keys())
            writer = csv.DictWriter(f, fieldnames=header)
            writer.writeheader()
            for data in data_dict:
                writer.writerow(data)
    except IOError:
        logging.error('I/O Error')

def dict_to_df(data):
    return pd.DataFrame.from_dict(data)


def main():
    # Log scraping status
    logging.basicConfig(filename='scrape.log', level=logging.DEBUG)

    scraper = ArtworkSoup()
    artwork_ids = np.random.randint(30000, size=30000)
    scraper.scrape(artwork_ids)
    df = dict_to_df(scraper.artwork_data)
    df.to_csv('artwork_data.csv')


if __name__ == '__main__':
    main()
