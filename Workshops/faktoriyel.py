# -*- coding: utf-8 -*-

sayi = int(input("Bir sayi giriniz: "))

faktoriyel = 1

if sayi<0:
    print("Negatif Sayı Olmaz")
elif sayi == 0:
    print("Sonuc: 1")
else:
    for i in range(1,sayi + 1):
        faktoriyel = faktoriyel * i
    print("Sonuç : " , faktoriyel)