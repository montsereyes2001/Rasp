import requests 
from requests.structures import CaseInsensitiveDict

class Api:
    def metodoGet(self,data,path):
        path=self.endpoint+path
        data = {}
        headers = CaseInsensitiveDict()
        headers["Accept"] = "application/json"
        headers["Authorization"] = "Bearer %s" % self.token
        resp = requests.get(path,data=data, headers=headers)
        return resp.json()