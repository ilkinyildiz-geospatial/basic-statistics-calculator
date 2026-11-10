import math

veri = [3, 5, 6, 5, 7, 8, 9, 23, 56, 78, 98, 43, 55]

def ortalama_hesapla(liste):
    
    return sum(liste) / len(liste)

def varyans_hesapla(liste):
  
    mu = ortalama_hesapla(liste)
    n = len(liste)
    
    kareler_toplami = sum((x - mu) ** 2 for x in liste)
   
    return kareler_toplami / n


def standart_sapma_hesapla(liste):
   
    var = varyans_hesapla(liste)
    return math.sqrt(var)


mu = ortalama_hesapla(veri)
varyans = varyans_hesapla(veri)
standart_sapma = standart_sapma_hesapla(veri)


print(f"Veri Sayısı : {len(veri)}")
print(f"Ortalama : {mu:.4f}")
print(f"Varyans : {varyans:.4f}")
print(f"Standart Sapma : {standart_sapma:.4f}")