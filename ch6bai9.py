# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 13:51:49 2024

@author: Cao Ngọc Thanh Thư 23719291
"""
import math
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
if a < 0 or b < 0:
    print("Lỗi")
else:
    phuong_trinh_1 = (math.sqrt(a) - math.sqrt(b))/(a**(1/4) - b**(1/4)) 
    phuong_trinh_2 = (math.sqrt(a) + (a*b)**(1/4))/(a**(1/4) + b**(1/4))
    print("Kết quả: ", phuong_trinh_1 - phuong_trinh_2)