import requests
import json

key = 'kHMaTxVJxeCDNOuOJdqK'
secret = 'ykrkhBryxPLbtCtVPcMKzovBOdHNPwkz'

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

username = 'kittertea'
status = 'for sale'
sort = 'price'
sort_order = 'descend'
url_user = f'https://api.discogs.com/users/{username}/inventory?status={status}&sort={sort}&page=1&per_page=100&key={key}&secret={secret}'
req = requests.get(url_user)

if int(req.status_code) == 200:
    apiDict = json.loads(req.text)
    print(apiDict.keys())
    print(apiDict['listings'][0]['price']['currency'])



