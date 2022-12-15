import os
import shutil
print(dir(os))


source="C:/Users/Security/Downloads"

destination="C:/Users/Security/Desktop/tanzy"

list=os.listdir(source)
for i in list:
    name,extention=os.path.splitext(i)
    print("name",name)

    print("extention",extention)
    if extention =="":
        continue
    if extention in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        path1 = source + '/' + i
        path2 = destination + '/' + "Image_Files"
        path3 = destination + '/' + "Image_Files" + '/' + i


        if os.path.exists(path2):
            shutil.move(path1,path3)
            print("moving")
        else:
            os.makedirs(path2)
            shutil.move(path1,path3)
            print("moving")


    

