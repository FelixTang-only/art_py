import os
import shutil
import glob

mkdir_path = r'/Users/apple/Downloads/test1'

goal_dir = r'/Users/apple/Downloads/test'

if not os.path.exists(mkdir_path):
    os.mkdir(mkdir_path)

file_num = 0
dir_num = 0

for file in glob.glob(f'{goal_dir}/**/*', recursive=True):
    if os.path.isfile(file):
        filename = os.path.basename(file)
        if '.' in filename:
            suffix = filename.split('.')[-1]
        else:
            suffix = 'others'
        if not os.path.exists(f'{mkdir_path}/{suffix}'):
            os.mkdir(f'{mkdir_path}/{suffix}')
            dir_num += 1
        shutil.copy(file, f'{mkdir_path}/{suffix}')
        file_num += 1

print(f'done, have{file_num} file into {dir_num} floder')