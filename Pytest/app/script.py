import requests

def sample1(url):
    return sample2(url)

def sample2(url):
    try:
        response = requests.get(url)
        return response.status_code
    except Exception:
        return 0


class SampleClass:
    def __init__(self):
        self._req = requests
    
    def get(self, url):
        try:
            response = self._req.get(url)
            return response
        except Exception:
            return 0
