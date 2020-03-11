import json
import requests


class APICall:
    def __init__(self, company, model, year):
        self.company = company
        self.model = model
        self.year = year

    @property
    def url(self):
        return f'https://webapi.nhtsa.gov/api/Recalls/vehicle/modelyear/' \
               + f'{self.year}/make/{self.company}/model/' \
               + f'{self.model}?format=json'

    def get_request(self):
        # Save API request object to a variable
        api_response = requests.get(self.url)
        # If API response is 200, return the API response data as a dictionary
        if int(api_response.status_code) == 200:
            return json.loads(api_response.text)

    def get_count(self, api_response):
        return api_response["Count"]

    def dump_data_to_json(self, api_response):
        output_path = f'{self.company}_{self.model}_{self.year}_recalls.json'
        print(f'Dumping API data to {output_path}')
        with open(output_path, 'w') as out_file:
            json.dump(api_response, out_file, indent=4)


if __name__ == '__main__':
    # Instantiate an APICall object
    saturn = APICall('saturn', 'LS', 2000)
    # Save API request to a variable
    api_data = saturn.get_request()
    # Get recall count
    saturn.get_count(api_data)
    # Dump recall data to JSON file
    saturn.dump_data_to_json(api_data)
