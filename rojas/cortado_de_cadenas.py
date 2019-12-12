#5. CORTADO DE CADENAS++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#                   1         2         3         4         5         6         7         8         9         0         1
#         01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901324567890123456789012
beskjed=("La mayoría de los hombres son como hojas que caen y revolotean indecisas mientras que otras son como los astros: " \
#                2         3         4         5         6         7         8         9         0         1       
#         34567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890   
         "siguen una ruta fija,ningún viento los alcanza y llevan en su interior su propia ley y trayectoria")
print(len(beskjed))

# 1.Del mensaje anterior imprimir: "hojas"
print(beskjed[35:40])

# 2.Del mensaje anterior imprimir: "interior"
print(beskjed[175:183])

# 3.Del mensaje anterior imprimir: "viento"
print(beskjed[141:147])

# 4.Del mensaje anterior imprimir: "trayectoria"
print(beskjed[200:211])

# 5.Del mensaje anterior imprimir: "astros"
print(beskjed[105:111])

# 6.Del mensaje anterior imprimir: "hombres"
print(beskjed[18:25])

# 7.Del mensaje anterior imprimir: "ruta"
print(beskjed[124:128])

# 8.Del mensaje anterior imprimir: "ningún viento los alcanza"
print(beskjed[134:159])

# 9.Del mensaje anterior imprimir: "los hombres son como hojas"
print(beskjed[14:40])

# 10.Del mensaje anterior imprimir: "en su interior su propia ley "
print(beskjed[169:197])

# 11.Del mensaje anterior imprimir: "siguen una ruta fija"
print(beskjed[113:133])

# 12.Del mensaje anterior imprimir: "son como los astros"
print(beskjed[92:111])

# 13.Del mensaje anterior imprimir: "la hoja cae"
print(beskjed[0:2]+beskjed[34:39]+beskjed[44:48])

# 14.Del mensaje anterior imprimir: "un hombre lleva su ley fija"
print(beskjed[120:122]+beskjed[17:24]+beskjed[161:167]+beskjed[183:186]+beskjed[193:197]+beskjed[128:133])

# 15.Del mensaje anterior imprimir: "p e r ú"
print(beskjed[187:188]+beskjed[12:13]+beskjed[52:53]+beskjed[138:139])
