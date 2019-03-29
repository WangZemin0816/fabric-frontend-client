
from service.http_request import http
class LoginService():
    def __init__(self):
        self.login_url = "/"
        pass

    def login(self,username,password,remember_me):
        login_form={
            "username":username,
            "password":password,
            "rememberMe": remember_me
        }
        return http.post(self.login_url,login_form)


login = LoginService()
del LoginService