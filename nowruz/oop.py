import hashlib
import re
regex_u=re.compile(r'^[a-zA-Z]+[_]{1}[A-Za-z]+$')
regex_p=re.compile(r'[a-zA-Z0-9]{1}[a-zA-Z0-9]{5,}')
regex_ph=re.compile(r'^(0|98)[0-9]{10}$')
regex_e=re.compile(r'^[a-zA-Z0-9]+[-|_]{0,1}[@]{1}[a-zA-Z0-9]+[-|_]{0,1}[.]{1}[A-Za-z]{2,5}$')


class Account:

    def __init__(self,username,password,phone_number,email):
        if re.fullmatch(regex_u,username):
            self.username=username
        else:
            raise Exception('invalid username')
        if re.fullmatch(regex_p,password):
            self.password=password
            password=hashlib.sha256(password.encode('utf_8')).hexdigest()
        else:
            raise Exception('invalid password')
        if re.fullmatch(regex_ph,phone_number):
            self.phone_number=phone_number
        else:
            raise  Exception('invalid phone number')
        if re.fullmatch(regex_e,email):
            self.email=email
        else:
            raise  Exception('invalid email')


class Site:
    def __init__(self,url,active_users=[],register_users=[]):
        self.url=url
        self.active_users=active_users
        self.register_users=register_users
    def register(self,user):
        username=user.username
        for i in range(len(self.register_users)):
            if username in self.register_users[i][0]:
                raise Exception('user already registered')
            else:
                (self.register_users).append(username)
                print('register successful')





    # def login
    #
    #
    #
    # def logout(self,username):
    #     if
    #
    #
    #





user1=Account('sh_vl','Aa123123','09121111221','sh@vl.com')
user2=Site('fjklkjkkjk')
user3=Site.register(user2,user1)
user2.register(user1)

print(user1.username)