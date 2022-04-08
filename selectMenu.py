class select:
    @staticmethod
    def auth_select():

        print("""
        Select Action
        1-Register
        2-Login
        """)
        bol = True
        while bol:
           option = input("Select an Option : ")
           if (option == "1" or option == "2"):
              bol=False

        return int(option)
    @staticmethod
    def main_select():
        print("""
        Select Action
        1-Create Project
        2-View all Projects
        3-Edit Project
        4-Delete project
        5-exit
         """)
        bol = True
        while bol:
          option = input("Select an Option : ")
          if (int(option) in range(1,6)):
              bol=False

        return int(option)


    @staticmethod
    def edit_select():
        print("""
        Select what do you want to edit
        1-title
        2-description
        3-total target
        4-start date
        5-end date
        6-back to main menu
         """)
        bol = True
        while bol:
          option = input("Select an Option : ")
          if (int(option) in range(1,7)):
              bol=False

        return int(option)


