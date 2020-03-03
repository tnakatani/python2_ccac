# API Design Project

## Program Objective

Use data from an API service to answer one or more compelling inquiry questions of your design

### Program Requirement 1

Engineer a python script that uses the requests library to make calls to an API of your choosing. Assemble data that is returned from that API to answer the question or set of questions you designed for this project.

### Program Requirement 2

Once you have data assembled that speaks to your research question, format the results of your API inquiry in a format that is understandable by a non-pythonista and can be posted on our course website and on the walls of our classroom 1136! Graphs, charts, figures, tables, images--all of these are welcome and invited.

## Submission: Discogs API Search - What are the merchant's most valuable records?

### Scripts 1: ```discogs_api.py``` 
`discogs_api.py` connects to the Discogs API to extract the most valuable records currently listed by a merchant.

Below is an example of how to run the script:

```bash
python discogs_api.py --seller <SELLER_NAME> --key <DISCOGS_API_KEY> --secret <DISCOGS_API_SECRET>
```

| Argument  | Description  | 
|---|---|
```--seller``` | Discogs merchant's username to query
```--key```    | Discogs API key 
```--secret``` | Discogs API secret

The script outputs two files prefixed by the ```--seller``` argument passed when running the script:

1. <discogs_merchant>_listings.csv - CSV file listing top 100 most expensive records by the merchant.
2. <discogs_merchant>_top_listing.csv - JSON file containing metadata of the most expensive record listed by the merchant. 


_Note that a Discogs API is required to run this script.  Users can get a Discogs API key + secret by following the instructions on the Discogs page:_

_[Discogs API Doc: Discogs auth flow](https://www.discogs.com/developers#page:authentication,header:authentication-discogs-auth-flow)_

---

### Script 2: ```merge_and_sort_listings.py```

`merge_and_sort_listings.py` compiles all of the query data in the `output` directory and sorts them by the top 10 most expensive records grouped by currency.

Results are stored in [`top_records.csv`](output/top_records.csv).

