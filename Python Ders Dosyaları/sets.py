# -*- coding: utf-8 -*-

studentsSet = {"Mustafa","Nurdan","Berrak"}
print(studentsSet)

for student in studentsSet:
    print(student)
    
print("Berrak" in studentsSet)

if "Berrak" in studentsSet:
    print("Listede var")
    
studentsSet.add("Ali")
print(studentsSet)

studentsSet.update(["Doruk","Mert","Elif"])
print(studentsSet)

print(len(studentsSet))
studentsSet.remove("Elif")
print(len(studentsSet))

studentsSet.discard("Elif") #silerken bulamazsan hata verme.
print(len(studentsSet))

x = studentsSet.clear()
print(len(studentsSet))
del studentsSet


#setUnion Konusu
setA = {1,2,3,4,5}
setB = {1,3,4,6,7,8}

print(setA | setB)
print(setA.union(setB))
print(setB.union(setA))

#setIntersection Konusu

setA = {1,2,3,4,5}
setB = {1,3,4,6,7,8}

print(setA & setB)
print(setA.intersection(setB))
print(setB.intersection(setA))