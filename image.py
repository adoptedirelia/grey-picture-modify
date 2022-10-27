import torch
import cv2
import numpy as np
import os
out_path = './pic_out'
input_path ='irelia.jpg'
img_name='irelia'
def pic_conv(pic_path,pic,layer=0,grey=True):
    img_grey = 0.299*pic[:,:,0] + 0.587*pic[:,:,1] + 0.114*pic[:,:,2]
    img = pic
    img_grey= np.rint(img_grey) # 四舍五入取整 
    r = np.zeros(256)
    width,height,  = pic.shape
    for i in range(n):
        for j in range(m):
            r[pic[i][j]]+=1

    r = r/(width*height)
    s = np.zeros(256)   #累计概率
    for i in range(256):
        for j in range(i+1):
            s[i]+=r[j]     

    s = round(s*255)    #四舍五入

    img_res = img_grey

    for x in range(width):
        for y in range(height):
            img_res = s[img_res[x][y]]


    pic = cv2.imread(pic_path)


    if grey:
        pic = pic.sum(axis=2)//3
    else:
        pic = pic[:,:,layer]
    pic_name = pic_path.split('.')[0]
    if not os.path.exists(f'{out_path}'):
        os.makedirs(f'{out_path}')
        print('make dir ~')
    outpath1 = f'{out_path}/{pic_name}_before{layer}.jpg'
    outpath2 = f'{out_path}/{pic_name}_after{layer}.jpg'
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

def pic_mix(img_name):
    pic1 = cv2.imread(f'{out_path}/{img_name}_after0.jpg')
    pic2 = cv2.imread(f'{out_path}/{img_name}_after1.jpg')
    pic3 = cv2.imread(f'{out_path}/{img_name}_after2.jpg')
    pic1 = pic1.sum(axis=2)//3
    pic2 = pic2.sum(axis=2)//3
    pic3 = pic3.sum(axis=2)//3
    n,m = pic1.shape
    out = np.zeros(shape=(n,m,3))
    out[:,:,0]=pic1
    out[:,:,1]=pic2
    out[:,:,2]=pic3
    cv2.imwrite(f'{out_path}/{input_path}_colorful.jpg',out)

if __name__ == '__main__':
    for i in range(1):
        print(i)

