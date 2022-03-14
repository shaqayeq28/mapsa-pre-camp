import re
regex = '^.\B([a-zA-Z0-9]){1,64}[\._]?[a-zA-Z0-9]+[@]\w+[.][a-zA-Z]{2,3}$'
def check(email):
    if (re.search(regex, email)):
        print("Valid Email")
    else:
        print("Invalid Email")

email = "va.sh@gmail.com"
check(email)
