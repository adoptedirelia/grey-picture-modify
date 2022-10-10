import torch
import cv2
import numpy as np
import os
def pic_conv(pic_path):
    pic = cv2.imread(pic_path)
    pic = pic.sum(axis=2)//3
    pic_name = pic_path.split('.')[0]
    if not os.path.exists('./pic_out'):
        os.makedirs('./pic_out')
        print('make dir pic_out')
    outpath1 = f'./pic_out/{pic_name}_before.jpg'
    outpath2 = f'./pic_out/{pic_name}_after.jpg'
    cv2.imwrite(outpath1,pic)
    print(pic.shape)
    r = np.zeros(256)
    n,m = pic.shape
    for i in range(n):
        for j in range(m):
            r[pic[i][j]]+=1

    s = np.zeros(256)
    r=r/(n*m)
    for i in range(256):
        for j in range(i):
            s[i]+=r[j] 
    s=s*255
    out = pic
    for i in range(n):
        for j in range(m):
            out[i][j]=s[pic[i][j]]

    cv2.imwrite(outpath2,out)

if __name__ == '__main__':
    pic_conv('irelia.jpg')

