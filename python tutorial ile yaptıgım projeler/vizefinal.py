vize=int (input("Vize notunuzu giriniz:"))
final=int (input("Final notunuzu giriniz:"))

puan= (vize*0.3) + (final*0.7)

print("Puanınız",puan,"dır")

if puan<45:
    print("KALDI")

elif puan>45 and puan<70:
    print("GEÇTİ")

else:
    print("ÇOK BAŞARILI")
