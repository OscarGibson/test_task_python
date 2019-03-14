import requests
import json
from django.conf import settings

class FlickerAPI:

    def __init__(self):
        self.FLICKER_URL = settings.FLICKER_URL
        self.FLICKER_API_KEY = settings.FLICKER_API_KEY
        self.FLICKER_SORT_TYPES = settings.FLICKER_SORT_TYPES

    def find(self, text, sort_type, page=1):
        url = self.FLICKER_URL % (
            self.FLICKER_API_KEY,
            text,
            sort_type,
            page
        )

        response = requests.get(url)
        
        if response.status_code == 200:
            print(dir(response))
            print(response.text[14:len(response.text) - 1])
            return json.loads(response.text[14:len(response.text) - 1])
        else:
            raise Exception("ERROR")
