import requests
import json

company = 'saturn'
model = 'LS'
year = 2000
url = f'https://webapi.nhtsa.gov/api/Recalls/vehicle/modelyear/{year}/make/{company}/model/{model}?format=json'
req = requests.get(url)

if int(req.status_code) == 200:
    apiDict = json.loads(req.text)
    print(apiDict.keys())

    results = apiDict['Results'][0]['Notes']
    print(apiDict['Results'][0]['Notes'])

