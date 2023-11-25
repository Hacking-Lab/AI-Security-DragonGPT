import requests

headers = {'Content-Type': 'application/json'}


class OpenAIHandler:
    def __init__(self, output_file, proxy):
        self.output_file = output_file
        self.proxy = proxy

    def do_threat_modeling(self, sentence):
        data = {
            'systemContent': ["Generate Threats and their Preventive Measures"],
            'promptText': [sentence]
        }
        try:
            response = requests.post(self.proxy, headers=headers, json=data)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            print("Can't use configured proxy")
            exit()
        result = response.text
        print(result)
        if self.output_file:
            with open(self.output_file, "w") as f:
                f.write(result)
