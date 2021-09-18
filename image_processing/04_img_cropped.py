import cv2		# เรียกใช้ library OpenCV
import numpy as np		# เรียกใช้ library Numpy

# อ่านไฟล์รูปจาก path แล้วเก็บในตัวแปร img
img = cv2.imread('./images/test_img.png')
# เก็บค่าความสูง, ความกว้าง, channel ไว้ในตัวแปร row, col, ch ตามลำดับ
row, col, ch = img.shape

start_row, end_row = 100, row-100  # กำหนดตำแหน่งความสูงที่ต้องการ crop
start_col, end_col = 100, col-100		# กำหนดตำแหน่งความกว้างที่ต้องการ crop

# crop ภาพในตัวแปร img ตามตำแหน่งที่กำหนด
cropped = img[start_row:end_row, start_col:end_col]

cv2.imshow('original', img)		# แสดงภาพในตัวแปร img บนหน้าต่าง original
cv2.imshow('cropped', cropped)  # แสดงภาพในตัวแปร cropped บนหน้าต่าง cropped

# ทำการดีเลย์หน้าต่างที่เปิดเป็นหน่วยมิลลิวินาที (โดย 0 หมายถึงดีเลย์จนกว่าจะมี input)
cv2.waitKey(0)
cv2.destroyAllWindows()		# ปิดหน้าต่างทั้งหมดที่เปิดโดยโปรแกรม
