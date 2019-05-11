# -*- coding: utf-8 -*-
#%% Classlara Giriş
class Matematik:
    def topla(self,sayi1,sayi2):
        return sayi1 + sayi2
    
    def cikar(self,sayi1,sayi2):
        return sayi1 - sayi2
    
    def carp(self,sayi1,sayi2):
        return sayi1 * sayi2
    
    def bol(self,sayi1,sayi2):
        return sayi1 / sayi2
    
matematik = Matematik()
print("Toplam = " + str(matematik.topla(2,78)))

#%% __init__ fonksiyonu ve self tam konu
class Matematik:
    def __init__(self,sayi1,sayi2):
        self.sayi1 = sayi1
        self.sayi2 = sayi2
    def topla(self):
        return self.sayi1 + self.sayi2
    def cikar(self):
        return self.sayi1 - self.sayi2
    def carp(self):
        return self.sayi1 * self.sayi2
    def bol(self):
        return self.sayi1 / self.sayi2
    
matematik = Matematik(2,78)

print("Toplam = " + str(matematik.topla()))
#%% Property

class Person:
    def __init__(self,firstName,lastName,age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        
person1 = Person("Mustafa","Topalbekiroğlu",23)
print(person1.firstName)

class Worker(Person):
    def __init__(self,salary):
        self.salary = salary
        
class Customer(Person):
    def __init__(self,creditCardNumber):
        self.creditCardNumber = creditCardNumber

ahmet = Worker()

mehmet = Customer()

