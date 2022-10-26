import os

path = './data/processed_file'

def get_filelist(dir):
    Filelist = []
    for home, dirs, files in os.walk(path):
        for file in files:
            Filelist.append(os.path.join(home, file))
    return Filelist

if __name__ == "__main__":
    Filelist = get_filelist(dir)
    print(Filelist)
    print(len(Filelist))

    f = open('result.txt', 'w')
