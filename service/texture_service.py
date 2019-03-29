
from service.http_request import http

class TextureService():
    upload_url="/texture/upload"
    def __init__(self):
        pass

    def upload(self,imgInfo,originImg,divisionImg):
        files = {
            'origin': originImg,
            'division': divisionImg,
        }
        efile = {
            'efile': imgInfo
        }
        return http.upload(self.upload_url,data=efile,files=files)


texture = TextureService()
del TextureService