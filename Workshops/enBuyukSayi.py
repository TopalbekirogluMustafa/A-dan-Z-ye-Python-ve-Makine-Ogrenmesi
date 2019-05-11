# -*- coding: utf-8 -*-

a = int (input ("Bir Sayı Giriniz: "))
b = int (input ("Bir Sayı Giriniz: "))
c = int (input ("Bir Sayı Giriniz: "))

if (a >= b) and (a >= c):
    enBuyuk = a

elif (b >= a) and (b >= c):
    enBuyuk = b

elif (c >= a) and (c >= b):
    enBuyuk = c
    
print("En Büyük Sayı :  ", enBuyuk)