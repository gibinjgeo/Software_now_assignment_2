import cv2
import numpy as np
import time

img_path = r'C:\Users\JAMES\Documents\JAPA\CDU\HIT137\Assignment 2\chapter1.jpg'
image = cv2.imread(img_path)


current_time = int(time.time())
generated_number = (current_time % 100) + 50

if generated_number % 2 == 0:
    generated_number += 10
    print("Generated Even Number Is :", generated_number)
else:
    print("Generated Odd Number Is :",generated_number)


modified_img = cv2.add(image, (generated_number, generated_number, generated_number, 0))


output_path = r'C:\Users\JAMES\Documents\JAPA\CDU\HIT137\Assignment 2\chapter1out.png'
cv2.imwrite(output_path, modified_img)

print("The New Modified image is now saved at:", output_path)


red_channel = modified_img[:, :, 2]
red_sum = np.sum(red_channel)

print("The sum of all red pixel values in the modified image is:", red_sum)
