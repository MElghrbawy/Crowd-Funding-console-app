from datetime import datetime
import ast
import selectMenu
import re


class helper:
    def name():
        while True:
            title = input(f"please enter your title : ")
            if title and title.isalpha():
                return title
            else:
                print("Enter a valid title")

    def target():
        while True:
            total = input("Enter your total target : ")

            if total and total.isnumeric():
                return total
            else:
                print("Wrong Value")

    def time(x):
        format = "%d-%m-%Y"

        while True:

            date = input(
                f"Enter a {x} date in this format (day-month-year) : ")

            try:
                bool(datetime.strptime(date, format))
                return date
            except ValueError:
                print("Incorrect date format")

    def whitespace_only(file):
        content = open(file, 'r').read()
        if re.search(r'^\s*$', content):
            return True


class project:
    def __init__(self, title, description, total_target, start_date, end_date):
        self.title = title
        self.description = description
        self.total_target = total_target
        self.start_date = start_date
        self.end_date = end_date

    @classmethod
    def from_input(cls):
        return cls(
            helper.name(),
            input("Enter project description : "),
            helper.target(),
            helper.time("start"),
            helper.time("end"),
        )

    def obj(self):
        return {
            "title": self.title,
            "description": self.description,
            "total_target": self.total_target,
            "start_date": self.start_date,
            "end_date": self.end_date
        }


class projectCrud:

    def __init__(self, email):
        self.email = email

    def create_project(self):

        new_project = project.from_input()

        f = open(f"users_projects/{self.email}.txt", "a")
        f.write(str(new_project.obj())+"\n")
        f.close()

    def view_projects(self):
        if helper.whitespace_only(f"users_projects/{self.email}.txt"):
            print("file is empty")
        else:
            h = open(f"users_projects/{self.email}.txt", "r")
            print("***************************************")
            for line in h:
                project = ast.literal_eval(line)
                if(project):
                    for key in project:
                        print(f"{key} : {project[key]}")
                else:
                    print("Error : No project found")
                print("***************************************")

    def delete_project(self):
        title = helper.name()
        found = False
        try:
            with open(f"users_projects/{self.email}.txt", 'r') as fr:
                lines = fr.readlines()

            with open(f"users_projects/{self.email}.txt", 'w') as fw:
                for line in lines:

                    if line.find(title) == -1:
                        fw.write(line)
                    else:
                        found = True
                        print("Project Deleted Successfully")
            if not found:
                print("No project with such title")
        except:
            print("error")

    def edit_project(self):
        title = helper.name()
        new_user = {}
        user_index = 0
        lines = []

        # finding user
        f = open(f"users_projects/{self.email}.txt", "r")
        for index, line in enumerate(f):
            user = ast.literal_eval(line)
            if(user["title"] == title):
                new_user = user
                user_index = index
        f.close()

        print(new_user, user_index)
        # editing
        if new_user:
            while True:
                option = selectMenu.select.edit_select()
                if option == 1:
                    title = helper.name()
                    new_user["title"] = title
                elif option == 2:
                    description = input("Enter new description")
                    new_user["description"] = description
                elif option == 3:
                    total_target = helper.target()
                    new_user["total_target"] = total_target
                elif option == 4:
                    start_date = helper.time("start")
                    new_user["start_date"] = start_date
                elif option == 5:
                    end_date = helper.time("end")
                    new_user["end_date"] = end_date
                else:
                    break
        else:
            print("No project with this title")
            return

        w = open(f"users_projects/{self.email}.txt", "r+")
        lines = w.readlines()
        w.seek(0)
        w.truncate()
        for index, line in enumerate(lines):
            if index != user_index:
                w.write(line)
            else:
                w.write(str(new_user)+"\n")
