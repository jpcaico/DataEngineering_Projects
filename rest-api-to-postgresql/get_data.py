import requests
import jsonschema

class Data:

    def get(self, url):
        return requests.get(url, verify=False).json()

    def return_treated_data(self, data):
       
        self.data = data

        launch, rocket, mission = [], [], []

        for result in data['results']:
            row = {}
            row['launch_id'] = result['id']
            row['launch_name'] = result['name']
            row['launch_status'] = result['status']['name']
            row['launch_status_description'] = result['status']['description']
            row['launch_window_start'] = result['window_start']
            row['launch_window_end'] = result['window_end']
            row['launch_provider_name'] = result['launch_service_provider']['name']
            launch.append(row)
        
        for result in data['results']:
            row = {}
            row['mission_id'] = result['mission']['id']
            row['launch_id'] = result['id']
            row['mission_name'] = result['mission']['name']
            row['mission_description'] = result['mission']['description']
            row['mission_type'] = result['mission']['type']
            mission.append(row)

        for result in data['results']:
            row = {}
            row['rocket_id'] = result['rocket']['id']
            row['launch_id'] = result['id']
            row['rocket_fullname'] = result['rocket']['configuration']['full_name']
            row['rocket_family'] = result['rocket']['configuration']['family']
            row['rocket_variant'] = result['rocket']['configuration']['variant']
            rocket.append(row)

        return [launch, mission, rocket]


    def validate_schema(self, my_data, my_schema):
        self.my_schema = my_schema
        try:
            jsonschema.validate(instance=my_data, schema=my_schema)
        except jsonschema.exceptions.ValidationError as err:
            print(err)
            print("JSON Not Valid")
            return False
        print("JSON Valid")
        return True

