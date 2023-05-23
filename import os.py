import os
import shutil
from_dir = "C:/Users/gtbca_xams4nw/Downloads"
to_dir = 'C:/Users/gtbca_xams4nw/c112'
list_of_files = os.listdir(from_dir)
#print(list_of_files)
for file_name in list_of_files:
    name,extention = os.path.splitext(file_name)
    #print(name)
    #print(extention)
    if extention == "":
        continue
    if extention in [".gif",".png",".jpg",".jpeg",".jfif",".tiff",".svg"]:
        path1 = from_dir + "/" + file_name
        path2 = to_dir + "/" + "arquivos_de_imagem"
        path3 = to_dir + "/" + "arquivos_de_imagem" + "/" + file_name
        #print(path1)
        #print(path3)
        if os.path.exists(path2):
            print("movendo" + file_name)
            shutil.copy(path1,path3)
        else: 
            os.makedirs(path2)
            print("movendo" + file_name)
            shutil.copy(path1,path3)
    if extention in [".doc",".docx",".txt",".html",".htm",".nfo",".rtf",".wri",".odt",".pdf",".dic",".notebook",".log",".epub"]:
        path1 = from_dir + "/" + file_name
        path2 = to_dir + "/" + "arquivos_de_texto"
        path3 = to_dir + "/" + "arquivos_de_texto" + "/" + file_name
        #print(path1)
        #print(path3)
        if os.path.exists(path2):
            print("movendo" + file_name)
            shutil.copy(path1,path3)
        else: 
            os.makedirs(path2)
            print("movendo" + file_name)
            shutil.copy(path1,path3)
    if extention in [".avi",".wmv",".mov",".qt",".mkv",".mp4",".avchd",".swf",".flv"]:
        path1 = from_dir + "/" + file_name
        path2 = to_dir + "/" + "arquivos_de_vídeo"
        path3 = to_dir + "/" + "arquivos_de_vídeo" + "/" + file_name
        #print(path1)
        #print(path3)
        if os.path.exists(path2):
            print("movendo" + file_name)
            shutil.copy(path1,path3)
        else: 
            os.makedirs(path2)
            print("movendo" + file_name)
            shutil.copy(path1,path3)