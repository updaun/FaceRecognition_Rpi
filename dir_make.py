import os


def make():
    def createFolder(directory):
        try:
            if not os.path.exists(directory):
                os.makedirs(directory)
        except OSError:
            print('Error: Creating directory. ' + directory)

    createFolder('/home/pi/Face_Recognition/dataset/daun')

    print('Make Directory Success!!!')
    print('-'*70)
