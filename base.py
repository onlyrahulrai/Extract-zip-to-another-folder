import zipfile
import os
import shutil

zip = f'{os.getcwd()}/code.zip'

code_folder_path = os.path.join(os.getcwd(),'templates')

code_static_path = os.path.join(os.getcwd(),'static')

temp_folder_path = os.path.join(code_folder_path, 'temp_folder.zip')

with zipfile.ZipFile(zip,'r') as zip_ref:
    zip_ref.extractall(code_folder_path)

    extracted_zip_path = os.path.join(code_folder_path,os.path.basename(zip).split('.')[0])

    code_folders = os.listdir(extracted_zip_path)

    for item in code_folders:
        if item in ["css","js"]:
            path = os.path.join(extracted_zip_path,item)

            shutil.copytree(path,os.path.join(code_static_path,item))

            shutil.rmtree(path)




