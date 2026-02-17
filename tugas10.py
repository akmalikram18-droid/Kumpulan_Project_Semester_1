##writefile modul_bangun_ruang.py
import math

def kubus(sisi):
    hasil = math.pow(sisi, 3)
    return hasil

def balok(p, l, t):
    hasil = p*l*t
    return hasil

def prisma(a,ts, tp):
    la = a*ts/2
    hasil = la*tp
    return hasil

def tabung(r, t):
    return math.pi*r*r*t

def kerucut(r, t):
    return (1/3)*math.pi*r*r*t