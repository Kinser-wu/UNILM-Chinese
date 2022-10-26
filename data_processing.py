import os
from pathlib import Path
from tqdm import tqdm
import time

def main():
    file_list = []
    for root, dirs, files in os.walk('./data/processed_file'):
        for file in files:
            file_list.append(Path(os.path.join(root, file)))

    for file in file_list:
        with open(file, 'r', encoding='utf8') as fp:
            data = fp.readlines()
        print(data)
        src_text = data[-1]
        tgt_text = data[0]
        data1 = {'src_text':src_text.strip(),'tgt_text':tgt_text.strip()}
        with open('data/cctv_process/cctv_data.json', 'a', encoding='utf8') as fp:
            fp.write(f'{str(data1)}\n')


if __name__ == '__main__':
    main()