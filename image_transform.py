# bmp-jpg
import math
import os

import cv2 as cv

path = input("请输入图像文件夹路径，按回车结束。\neg. D:\image\n\n<dir> ")
targetquality = input("\n请输入图像压缩质量(0-100)\n")
extern = [".jpg", ".png", ".bmp", ".tiff", ".gif"]
tempfiles = os.listdir(path)
imagefiles = []
imagenames = []
for file in tempfiles:
    ext = os.path.splitext(file)[-1]
    if ext in extern:
        imagefiles.append(file)
        imagenames.append(os.path.splitext(file)[0])

folder = os.path.exists("output")
if not folder:
    os.makedirs("output")
cnt = 0
for image in imagefiles:
    src = cv.imread(
        path + "\\" + image, cv.IMREAD_COLOR)
    buff = []
    param = [cv.IMWRITE_JPEG_QUALITY, int(targetquality)]
    retval, buff = cv.imencode(".jpg", src, param)
    dst = cv.imdecode(buff, cv.IMREAD_COLOR)
    cv.imwrite("output\\" + imagenames[cnt] + ".jpg", dst)
    cnt += 1
ans = input("转换完成，输入‘y/Y’打开输出文件夹。\n")
if ans == "y" or ans == "Y":
    os.startfile("output")
