# -*- coding: utf-8 -*-

matris1 =  [[1,3,5],[2,4,1],[1,5,7]]
matris2 =  [[3,3,4],[2,4,1],[3,5,4]]
sonuc = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(matris1)):
    for j in range(len(matris2)):
        sonuc [i][j] = matris1 [i][j] + matris2 [i][j]
print(sonuc)