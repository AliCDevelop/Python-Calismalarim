print("VÜCUT KİTLE İNDEKSİNİ HESAPLAYAN PROGRAM")

kilo=int(input("KİLONUZU GİRİNİZ:"))
boy=float(input("BOYUNUZU GİRİNİZ:"))

sonuc=kilo/(boy**2)

if sonuc<20:
    print(sonuc,"ÇOK ZAYIFSINIZ")

elif sonuc<25 and sonuc>18:
    print(sonuc,"NORMALSİNİZ")


else:
    print(sonuc,"KİLONUZA DİKKAT EDİN")
