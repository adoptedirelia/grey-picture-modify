import numpy as np
import cv2
import struct
import matplotlib.pyplot as plt
import os


def readBMP(file_dir,show=False):
    
    f = open(file_dir,'rb')
    print(f'图片名字{file_dir}，正在读取')
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
    color_table = np.empty(shape=[256,4],dtype=int)
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

    img = np.empty(shape=[Height,Width,3],dtype=int)
    if Bit==8:
        for y in range(0,Height):
            for x in range(0,Width):
                index, = struct.unpack('B',f.read(1))
                img[Height-y-1,x] = color_table[index][0:3] #不能将alpha分量放进去
    if Bit==24:
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
    return img



if __name__ == '__main__':
    
    for i in os.listdir('./pic_test'):
        str = i[len(i)-3:len(i)]
        if str == 'bmp':
            i = './pic_test/' + i
            img = readBMP(i)
    

