from requests import post
from json import dumps

class CreateGist:
    BASE_URL = "https://api.github.com/gists"

    def __init__(self, headers:dict):
        self.headers = headers

    def create_new_gist(self,files: dict, description: str = "A gist", public: bool = False) -> bool:
        header = self.headers

        payload = {
            "public": public, "description": description, "files": files
        }
        resp = post(self.BASE_URL, headers=header, data=dumps(payload))

        resp_code = resp.status_code
        print(resp.content)
        return resp_code == 201
    

