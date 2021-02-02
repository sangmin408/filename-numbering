import os
import glob

# 해당 폴더안에 jpg 확장자 모두 불러오기
fpath = "C:\\japanesegirl\\12\\*.png"
for fpath in glob.glob(fpath):
    fpath_r = fpath.replace('34 (', '(')  # selfie (27).jpg => (27).jpg로 변경
    os.rename(fpath, fpath_r)
fpath = "C:\\japanesegirl\\12\\*.png"  # 해당 폴더안에 jpg 확장자 모두 불러오기
for fpath in glob.glob(fpath):
    fpath_r = fpath.replace('(', '')  # (27).jpg => 27).jpg로 변경
    os.rename(fpath, fpath_r)

fpath = "C:\\japanesegirl\\12\\*.png"  # 해당 폴더안에 jpg 확장자 모두 불러오기
for fpath in glob.glob(fpath):
    fpath_r = fpath.replace(')', '')  # 27).jpg => 27.jpg로 변경
    os.rename(fpath, fpath_r)
