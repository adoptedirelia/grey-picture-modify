import cv2
import numpy as np

pic1 = cv2.imread('./pic_out/irelia_after0.jpg')
pic2 = cv2.imread('./pic_out/irelia_after1.jpg')
pic3 = cv2.imread('./pic_out/irelia_after2.jpg')
pic1 = pic1.sum(axis=2)//3
pic2 = pic2.sum(axis=2)//3
pic3 = pic3.sum(axis=2)//3
n,m = pic1.shape
out = np.zeros(shape=(n,m,3))
out[:,:,0]=pic1
out[:,:,1]=pic2
out[:,:,2]=pic3
cv2.imwrite('test.jpg',out)
