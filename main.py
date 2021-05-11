import os

folder_mama = r'C:\Users\Victor\Desktop\Tiktok' + '\\'

for folder, dir, files in os.walk(folder_mama):
    #print(folder.split())
    arr_folder = folder.split()
    arr_folder.pop(0)
    separator = ''
    nume_grafica = separator.join(arr_folder)
    #print(nume_grafica)
    for file in os.listdir(folder):
        #print(file)
        os.chdir(folder)
        #print(os.getcwd())
        nume_fisier_intreg = file.split('.')
        nume_fisier = nume_fisier_intreg[0]
        #print(nume_fisier)
        new_name = '{} {}.jpg'.format(nume_fisier, nume_grafica)
        print(new_name)
        #os.rename(file, new_name)

