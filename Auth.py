import re
import ast

class validation:

    @staticmethod
    def name(x):
        while True:
            name = input(f"please enter your {x} name : ")
            if name and name.isalpha():
                return name
            else:
                print("wrong name format")
    @staticmethod
    def password():
         while True :
            password = input("please enter your password : ")
            confirm_password = input("please confirm your password : ")
            if password and password == confirm_password:

                return password
            else :
                print("passwords dosen't match")

    @staticmethod
    def email():
        while True :
            email = input("please enter your email : ")
            if re.fullmatch(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',email):
                return email
            else :
                print("email is not valid")

    @staticmethod
    def phone():
        while True :
            phone = input("please enter your phone : ")
            if re.fullmatch(r'^01[0125][0-9]{8}$',phone):
                return phone
            else :
                print("Not a valid Phone Number")

class user:
    def __init__(self, first_name, last_name, password, email, phone): 
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.email = email
        self.phone = phone


    @classmethod
    def from_input(cls):
        return cls(
            validation.name("first"),
            validation.name("last"),
            validation.password(),
            validation.email(),
            validation.phone(),
           
        )
    def obj(self):
        return {
            "first_name":self.first_name,
            "last_name":self.last_name,
            "password":self.password,
            "email":self.email,
            "phone":self.phone

        }


def register():
    new_user = user.from_input()

    f = open("users","a+")
    f.seek(0)
    data = f.read(100)
    if len(data) > 0:
        f.write("\n")
    f.write(str(new_user.obj()))
    f.close()
    with open(f"users_projects/{new_user.email}.txt", 'w') as fp:
        pass
    fp.close()
    return True


def login():
    while True:
        email = input("Enter your email address :")
        password = input("Enter your password : ")
        f = open("users","r")
        for line in f :
            user = ast.literal_eval(line)
            if(user["email"] == email and user["password"] == password):
                return user["email"]
        else:
            print("No such user")    