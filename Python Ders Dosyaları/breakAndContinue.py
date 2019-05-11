# -*- coding: utf-8 -*-


sehirler = ["Ankara", "İstanbul", "İzmir"]
#print(sehirler = [0])
#print(sehirler = [1])
#print(sehirler = [2])

for sehir  in sehirler:
    
    if sehir == "Ankara":
        continue
    print(sehir + " için kod = " +sehir[0:3])
    print("*********")
    if sehir == "İstanbul":
        break
    print(sehir + " için kod = " +sehir[0:3])
    print("*********")