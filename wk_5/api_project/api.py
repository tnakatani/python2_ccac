import requests
import json
import csv

# artist = 'nirvana'
# url = f'https://api.discogs.com/database/search?q={artist}&key={key}&secret={secret}&page=1&per_page=100'
# req = requests.get(url)
# 
# if int(req.status_code) == 200:
#     apiDict = json.loads(req.text)
#     print(apiDict['results'][0].keys())
#     results = apiDict['results']
# 
#     for r in results:
#         print(r['title'])

req = requests.get(url_user)

def response_is_200():
    int(req.status_code) == 200

with open('seller_listings.csv','w') as f, open('sample_listing.json','w') as j:
    key = 'kHMaTxVJxeCDNOuOJdqK'
    secret = 'ykrkhBryxPLbtCtVPcMKzovBOdHNPwkz'
    username = 'kittertea'
    status = 'for sale'
    sort = 'price'
    sort_order = 'desc'
    url_user = f'https://api.discogs.com/users/{username}/inventory?status={status}&sort={sort}&sort_order={sort_order}&page=1&per_page=100&key={key}&secret={secret}'
    headers = ['listings',
               'title',
               'price',
               'currency',
               'url']
    writer = csv.writer(f)
    writer.writerow(headers)

    try:
        requests.get(url_user)
        apidict = json.loads(req.text)

        json.dump(apidict['listings'][0]['release'], j, indent=4, ensure_ascii=False)

        for item in apidict['listings']:
            artist = item['release']['artist']
            title = item['release']['title']
            price = item['price']['value']
            currency = item['price']['currency']
            url = item['uri']
            writer.writerow([artist,title,price,currency,url])
    except requests.exceptions.RequestException as e:
        print(e)
        sys.exit(1)



