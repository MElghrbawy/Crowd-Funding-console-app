import selectMenu
import Auth
import crud




option = selectMenu.select.auth_select()

login = False;
if option == 1:
    register = Auth.register()
    if register:
        print("***************************************")
        print("Please login")
        login = Auth.login()
else:
    login = Auth.login()
    
    
if login:
    project_crud = crud.projectCrud(login)
    while True:
        option = selectMenu.select.main_select()
        if option == 1:
            project_crud.create_project()
        elif option == 2:
            project_crud.view_projects()
        elif option == 3:
            project_crud.edit_project()
        elif option == 4:
            project_crud.delete_project()
        else:
            break


