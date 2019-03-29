import requests


class HttpRequest(object):

    def __init__(self):
        self.session = requests.session()
        self.base_url = "http://localhost:8081"

    def print(self):
        print("31423423423")

    def post(self, rela_url, data):
        abs_url = self.getAbsUrl(rela_url)
        return self.session.post(abs_url, data=data)

    def upload(self, rela_url, data, files):
        abs_url = self.getAbsUrl(rela_url)
        return self.session.post(abs_url, data=data, files=files)

    def getAbsUrl(self, rela_url):
        return self.base_url + rela_url


http = HttpRequest()

del HttpRequest
