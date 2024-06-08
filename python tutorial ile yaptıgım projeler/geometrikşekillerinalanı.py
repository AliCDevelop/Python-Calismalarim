print("GEOMETRİK ŞEKİLLERİN  ALANINI HESAPLAYAN PROGRAM")

print("1-KARE", "\n2-DİKDÖRTGEN", "\n3-ÜÇGEN")

secim=input("Alanını öğrenmek istediğiniz geometrik şekli seçiniz:")

if secim=="1":
    kare=int(input("Karenin bir kenarını giriniz:"))
    print("Karenin alanı", kare**2,"'dir.")


if secim=="2":
    u=int(input("Dikdörtgenin uzun kenarını giriniz:"))
    k=int(input("Dikdörtgenin kısa kenarını giriniz:"))
    print("Dikdörtgenin alanı", u*k,"'dir.")


if secim=="3":
    a=int(input("Üçgenin bir kenarını giriniz:"))
    b=int(input("Üçgenin diğer kenarını giriniz:"))
    print("Üçgenin alanı", a*b/2,"'dir.")
