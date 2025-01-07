import os

odoo_structure = {
    "my_project" : {
        "env" : {}, #setup virtual enviroment
        "src" : {}, #contains the clone of Odoo itself, as well as various third-party add-on projects
        "local" : {}, #used to save your instance-specific add-ons
        "filestore" : {}, #used as a file store
        "bin" : {}, # includes various helper executable shell scripts
        "logs" : {}, #used to store the server log files
    }
}

def odoo_repos(path_proj,structure):
    for folder, subfolders in structure.items():
        folder_path = os.path.join(path_proj,folder) #e.g. if path_proj = "/home/" and folder = "my_project" than folder_path = "/home/my_project"
        os.makedirs(folder_path)
        if isinstance(subfolders, dict): # checks if subfolders is a dictionary (aka checks if there's the need of creating another directory)
            odoo_repos(folder_path, subfolders)    


if __name__ == "__main__":
    path = "."
    if not os.path.exists(path):
        print("Invalid path")
    else:
        odoo_repos(path,odoo_structure)
        print("Repos created correctly")    