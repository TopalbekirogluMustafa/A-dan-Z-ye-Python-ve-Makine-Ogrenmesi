# -*- coding: utf-8 -*-

# substring
mesaj = "Merhaba Dünya"
print(mesaj[2:5])
yeniMesaj = mesaj[12:13]
print(yeniMesaj)


# len fonksiyonu
print(len(mesaj))
yeniMesaj2 = mesaj[len(mesaj)-1:len(mesaj)]
print(yeniMesaj2)

# lower upper
print(mesaj.upper())
print(mesaj.lower())

# replace
print(mesaj.replace("ü","u"))
print(mesaj)
#mesaj=mesaj.replace("ü","u")
print(mesaj.replace("a","e"))

# split ve strip
#boşlukların hepsini yoksayarak işlem yapmak
#istiyorsak .strip ifadesini kullanırız.
bilgi = "  Mustafa;Topalbekiroğlu;23;Gaziantep  "
print(bilgi.split())
print("Adı = " + bilgi.split(";")[0])

# input
ad = input("Adınız? ")
sayi1 = input("Sayı 1 =? ")
sayi2 = input("Sayı 2 =? ")
print(int(sayi1) +int(sayi2))

