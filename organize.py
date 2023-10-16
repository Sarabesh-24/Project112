import os
import shutil

from_dir="C:\\Users\\Envy\\Desktop\\Images111"
to_dir="C:\\Users\\Envy\\Desktop\\test"
list_oft_file=os.listdir(from_dir)
print(list_oft_file)
for file_name in list_oft_file:
    name,extention=os.path.splitext(file_name)
    print(name)
    print(extention)
    if extention==" ":
        continue
    if extention in [".gif",".png",".jpg",".jfif","jpeg"]:
        path1=from_dir+"\\"+file_name
        path2=to_dir+"\\"+file_name
        shutil.move(path1,path2)