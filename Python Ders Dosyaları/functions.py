# -*- coding: utf-8 -*-
#%%
sehir = "Ankara"

print(sehir.upper())

print(sehir.endswith("a"))

#%%
def selamVer(isim = "Ziyaretçi"):
    print("Merhaba " + isim)
    
selamVer("Mustafa")
selamVer("Ökkeş")
selamVer()

#%%
def selamVer2(isim = "Ziyaretçi ", soyIsim = "Arkadaş"):
    print("Merhaba " + isim + soyIsim)
selamVer2()
selamVer2("Mustafa ", "Topalbekiroglu")

#%%
def dikUcgenAlaniHesaplama(a,b):
    return a*b/2

alan = dikUcgenAlaniHesaplama(4,7)

print(alan)

#%%
dikUcgenAlaniHesaplama2 = lambda a,b : a*b/2

print(dikUcgenAlaniHesaplama2(2,6))

x = dikUcgenAlaniHesaplama2
print(x(4,7))