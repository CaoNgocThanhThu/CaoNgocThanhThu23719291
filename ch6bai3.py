# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 19:49:52 2024

@author: Cao Ngọc Thanh Thư 23719291
"""
N = int(input("Nhập số nguyên dương có 2 chữ số: "))
if 10 <= N <= 99:
    print("Tổng các chữ số của {N} là: ", ( N % 10 ) + ( N // 10 ))
else:
    print("Số đã nhập không phải số nguyên dương có 2 chữ số")