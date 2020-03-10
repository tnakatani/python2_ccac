import json
import requests

# Set up the variables
company = 'saturn'
model = 'LS'
year = 2000

# Set up the API call URL
url = f'https://webapi.nhtsa.gov/api/Recalls/vehicle/modelyear/{year}/make/{company}/model/{model}?format=json'

# Make the request
def get_request(url):
    # Save API request object to a variable
    api_response = requests.get(url)
    # If API response is 200, return the API response data as a dictionary
    if int(api_response.status_code) == 200:
        return json.loads(api_response.text)


def get_count(api_response):
    return api_response["Count"]


def dump_data_to_json(api_response):
    output_path = f'{company}_{model}_{year}_recalls.json'
    print(f'Dumping API data to {output_path}')
    with open(output_path, 'w') as out_file:
        json.dump(api_response, out_file)


def main():
    """Run the functions"""
    api_data = get_request(url)
    print(get_count(api_data))
    dump_data(api_data)


if __name__ == '__main__':
    main()
