import numpy as np
import cv2
import struct
import matplotlib.pyplot as plt
import os
import pylab
# cv2读取图片是BGR，但是plt颜色接口为RGB
def readBMP(file_dir,show=False):
    
    f = open(file_dir,'rb')
    print(f'图片{file_dir}，正在读取')
    #读取位图文件头 14 Byte
    Type = f.read(2)  #类型
    Size = f.read(4) #文件大小
    f.seek(f.tell() + 4)  # 跳过保留字
    bfOffBits = f.read(4) #从文件头开始到到实际数据之间字节的偏移量

    #读取位图信息头 40 Byte
    biSize = f.read(4)  # 信息块的大小
    biWidth = f.read(4)
    biHeight = f.read(4)
    biPlanes = f.read(2)  # 1,位图的位面数
    biBitCount = f.read(4) # 说明比特数，通常为1/4/8/16/24/32
    f.seek(f.tell()+22) #剩下的信息帮助不大，所以直接跳过

    Pic_size, = struct.unpack('i',Size)
    Width, = struct.unpack('i',biWidth)
    Height, = struct.unpack('i',biHeight)
    Bit, = struct.unpack('i',biBitCount)
    print(f'文件大小为{Pic_size} Byte, 图片宽度{Width}, 图片高度{Height}, 每个像素所占位数{Bit}')

    #读取颜色表
    color_table = np.zeros(shape=[256,4],dtype=int)
    f.seek(54)  #直接跳到颜色表,颜色表的排列是 B G R 需要注意
    for i in range(0,256):
        b, = struct.unpack('B',f.read(1))
        g, = struct.unpack('B',f.read(1))
        r, = struct.unpack('B',f.read(1))
        alpha, = struct.unpack('B',f.read(1))

        color_table[i][0] = r
        color_table[i][1] = g
        color_table[i][2] = b
        color_table[i][3] = alpha

    offset, = struct.unpack('i',bfOffBits)
    #读取图像，读图像的时候是从下到上，从左到右
    f.seek(offset)

    img = np.zeros(shape=[Height,Width,3],dtype=int)
    if Bit!=24:
        for y in range(0,Height):
            for x in range(0,Width):
                index, = struct.unpack('B',f.read(1))
                img[Height-y-1,x] = color_table[index][0:3] #不能将alpha分量放进去
    else:
        for y in range(0,Height):
            for x in range(0,Width):
                r, = struct.unpack('B',f.read(1))
                g, = struct.unpack('B',f.read(1))
                b, = struct.unpack('B',f.read(1))
                img[Height-y-1,x] = [r,g,b] #不能将alpha分量放进去
    if show:
        plt.imshow(img)
        plt.show()
    f.close()

    
    return img,Bit

def pic_conv_grey(pic,bit,pic_name='out',show = False):
    pp = pic.copy()
    if(bit==8):
        img_grey = pp[:,:,0]   #灰色
    if(bit==24):
        img_grey = 0.299*pp[:,:,0] + 0.587*pp[:,:,1] + 0.114*pp[:,:,2]
    img_grey= np.rint(img_grey) # 四舍五入取整 
    img_grey = img_grey.astype(np.uint8)
    pic = pic.astype(np.uint8)
    r = np.zeros(256)
    width,height,layer  = pic.shape

    for i in range(width):
        for j in range(height):
            r[pic[i][j]]+=1

    r = r/(width*height)
    s = np.zeros(256)   #累计概率
    for i in range(256):
        for j in range(i+1):
            s[i]+=r[j]     

    s = np.rint(s*255)    #四舍五入

    img_res = np.zeros(shape=(width,height))

    for x in range(width):
        for y in range(height):
            img_res[x][y] = s[img_grey[x][y]]

    img_res = combine(img_res)
    img_res = img_res.astype(np.uint8)
    img_bgr = cv2.cvtColor(img_res,cv2.COLOR_RGB2BGR)
    cv2.imwrite(f'./pic_out/{pic_name}.jpg',img_bgr)
    
    if show:
        plt.imshow(img_res,'gray')
        plt.show()
    return img_res

def combine(pic):
    n,m = pic.shape
    res = np.zeros((n,m,3))
    res[:,:,0] = pic
    res[:,:,1] = pic
    res[:,:,2] = pic
    return res

def pic_conv_rgb(pic,pic_name='out',show=False):
    n,m,layer = pic.shape

    pic_R = pic[:,:,0]
    pic_G = pic[:,:,1]
    pic_B = pic[:,:,2]

    R = combine(pic_R)
    G = combine(pic_G)
    B = combine(pic_B)

    

    conv_R = pic_conv_grey(R,8,f'{pic_name}_red')[:,:,0]
    conv_G = pic_conv_grey(G,8,f'{pic_name}_green')[:,:,0]
    conv_B = pic_conv_grey(B,8,f'{pic_name}_blue')[:,:,0]

    img_res = np.zeros((n,m,3))

    img_res[:,:,0] = conv_R
    img_res[:,:,1] = conv_G
    img_res[:,:,2] = conv_B
    img_res = img_res.astype(np.uint8)
    img_bgr = cv2.cvtColor(img_res,cv2.COLOR_RGB2BGR)
    cv2.imwrite(f'./pic_out/{pic_name}.jpg',img_bgr)
    if show:
        plt.imshow(img_res)
        plt.show()
    return img_res

def pixel_collect(pic,x,y,kernel):
    n,m = pic.shape
    
    lst = []
    kernel = (int)((kernel-1)/2)
    left = x-kernel if x-kernel>=0 else 0
    right = x+kernel if x+kernel<m else m-1
    top = y-kernel if y-kernel>=0 else 0
    bottom = y+kernel if y+kernel<n else n-1
    for i in range(left,right+1):
        for j in range(top,bottom+1):
            pixel = pic[i][j]
            lst.append(pixel)
            
    return np.array(lst)

def Media_filter(pic,kernel=3,pic_name='out',show=False):
    n,m,layer = pic.shape
    img_res = np.zeros((n,m,3))
    pp = pic.copy() #深copy
    img_r,img_g,img_b = pp[:,:,0],pp[:,:,1],pp[:,:,2]

    imgs = [img_r,img_g,img_b]

    for img in imgs:
        width,height = img.shape
        for i in range(width):
            for j in range(height):
                lst = pixel_collect(img,i,j,kernel)
                ans = np.median(lst)
                img[i][j]=ans
                
    img_res[:,:,0],img_res[:,:,1],img_res[:,:,2] = img_r,img_g,img_b
    img_res = img_res.astype(np.uint8)
    img_bgr = cv2.cvtColor(img_res,cv2.COLOR_RGB2BGR)
    cv2.imwrite(f'./pic_out/{pic_name}.jpg',img_bgr)
    if show:
        plt.imshow(img_res)
        plt.show()

    return img_res

def Mean_filter(pic,kernel=3,pic_name='out',show=False):
    n,m,layer = pic.shape
    img_res = np.zeros((n,m,3))
    pp = pic.copy() #深copy
    img_r,img_g,img_b = pp[:,:,0],pp[:,:,1],pp[:,:,2]

    imgs = [img_r,img_g,img_b]

    for img in imgs:
        width,height = img.shape
        for i in range(width):
            for j in range(height):
                lst = pixel_collect(img,i,j,kernel)
                ans = np.mean(lst)
                img[i][j]=ans
                
    img_res[:,:,0],img_res[:,:,1],img_res[:,:,2] = img_r,img_g,img_b
    img_res = img_res.astype(np.uint8)
    img_bgr = cv2.cvtColor(img_res,cv2.COLOR_RGB2BGR)
    cv2.imwrite(f'./pic_out/{pic_name}.jpg',img_bgr)
    if show:
        plt.imshow(img_res)
        plt.show()
    return img_res

if __name__ == '__main__':
    # 测试用例
    a = cv2.imread('./irelia.jpg',0)
    
    hist = cv2.calcHist([a],[0],None,[256],[0,256])
    plt.hist(a.ravel(),256)
    plt.show()
    #img,bit = readBMP('./pic_test/Panda(jiaoyan).bmp')
    #Mean_filter(img,show=True)

    
    

