import os
import shutil
from tqdm import tqdm

sourceDir = './data/cctv'
targetDir = './data/processed_file'

for root, dirs, files in os.walk(sourceDir):
    for file in tqdm(files, desc="waiting..."):
        shutil.copy(os.path.join(root, file), targetDir)
