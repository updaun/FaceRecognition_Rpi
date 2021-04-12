import os
import shutil


def remove():
    dir_path = '/home/pi/Face_Recognition/dataset/'
    print('-'*70)
    file_list = os.listdir(dir_path)
    print(*file_list)
    for file in file_list:
        file_path = os.path.join(dir_path, file)
        if os.path.isdir(file_path):
            dir_path2 = file_path
            print(dir_path2)
            shutil.rmtree(dir_path2)
    print('='*70)
    file_list = os.listdir(dir_path)
    print(*file_list)

    print('Remove Success!!!')

    print('='*70)

# os.rmdir('/home/pi/Face_Recognition/dataset/daun')
