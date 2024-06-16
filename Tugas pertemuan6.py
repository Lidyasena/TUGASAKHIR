
#  balok.py
def volume_balok(panjang, lebar, tinggi):
    return panjang * lebar * tinggi

def luas_permukaan_balok(panjang, lebar, tinggi):
    return 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)


# kubus.py
def volume_kubus(sisi):
    return sisi ** 3

def luas_permukaan_kubus(sisi):
    return 6 * (sisi ** 2)


# limas segiempat.py
def volume_limas(panjang, lebar, tinggi):
    return (panjang * lebar * tinggi) / 3

def luas_permukaan_limas(panjang, lebar, tinggi_sisi_miring):
    luas_alas = panjang * lebar
    luas_sisi_miring = (panjang + lebar) * tinggi_sisi_miring / 2
    return luas_alas + luas_sisi_miring

# bola.py
import math

def volume_bola(jari_jari):
    return (4/3) * math.pi * (jari_jari ** 3)

def luas_permukaan_bola(jari_jari):
    return 4 * math.pi * (jari_jari ** 2)

