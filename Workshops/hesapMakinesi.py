# -*- coding: utf-8 -*-

def topla(sayi1,sayi2):
    return sayi1 + sayi2

def cikar(sayi1,sayi2):
    return sayi1 - sayi2

def carp(sayi1,sayi2):
    return sayi1 * sayi2

def bol(sayi1,sayi2):
    return sayi1 / sayi2

print("Operasyon:")
print("1 : Topla")
print("2 : Çıkar")
print("3 : Çarp")
print("4 : Böl")

secenek = input("Operasyon Seçiminiz? ")

sayi1 = int(input("Birinci Sayı? "))
sayi2 = int(input("İkinci Sayı? "))



if secenek == '1':
    print("Toplam : " + str(topla(sayi1,sayi2)))
    

elif secenek == '2':
    print("Çıkarma : " + str(cikar(sayi1,sayi2)))
    

elif secenek == '3':
    print("Çarpma : " + str(carp(sayi1,sayi2)))
    

elif secenek == '4':
    print("Bölme : " + str(bol(sayi1,sayi2)))
    
else:
    print("Geçersiz Seçenek")
    
    