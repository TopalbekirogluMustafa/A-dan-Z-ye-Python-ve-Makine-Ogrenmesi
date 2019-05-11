# -*- coding: utf-8 -*-

sehirler = ["Ankara", "İstanbul", "İzmir"]
#print(sehirler = [0])
#print(sehirler = [1])
#print(sehirler = [2])


#%% For intro
for sehir  in sehirler:
    
    if sehir != "Ankara":
        print(sehir + " için kod = " +sehir[0:3])
        print("*********")
#    if sehir == "Ankara":
#        print(sehir + " için kod = " +sehir[0:3])
        
#%% For range (sağ tık "Run Cell" komutu ile çalıştır!)
        
for x in range(2,10,2):
    print(x)