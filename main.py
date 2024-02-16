class Kutuphane():

    def __init__(self, f="books.txt", mode="a+", abc="utf-8"):
        self.f = f
        self.mode = mode
        self.abc = abc
        self.dosya = open(self.f,self.mode,encoding=self.abc)


    def __del__(self):
        self.dosya.close()


    def kitaplari_listele(self):

      with open("books.txt","r",encoding="utf-8") as f:
        satirlar = f.read().splitlines()
        self.dosya.seek(0)
        for i in satirlar:
            bilgi = i.split(",")
            print(f"Adı:{bilgi[0]} | Yazarı:{bilgi[1]} | Yılı:{bilgi[2]} | Sayfa:{bilgi[3]}")

    def kitap_ekle(self):
        kitap = input("Lütfen kitap adını giriniz: ")
        yazar = input("Lütfen yazar adını giriniz: ")
        yil = input("Lütfen kitbın basım yılını giriniz: ")
        sayfa = input("Lütfen kitabın sayfa saysını giriniz: ")

        with open("books.txt","a+",encoding="utf-8") as f:
        #self.dosya.write(f"{kitap},{yazar},{yil},{sayfa}\n")
            f.write(f"{kitap},{yazar},{yil},{sayfa}\n")
            f.seek(0)

    def kitap_sil(self):
        kitap = input("Lütfen silinecek kitabın adını giriniz: ")
        with open("books.txt","r",encoding="utf-8") as f:
            satirlar = f.read().splitlines()
        indeks = None
        for i,satir in enumerate(satirlar):
            bilgi = satir.split(",")
            if bilgi[0] == kitap:
                indeks = i
                break
        if indeks is not None:
            del satirlar[indeks]
        with open("books.txt","w",encoding="utf-8") as f:
            for satir in satirlar:
                f.write(f"{satir}\n")

    def bilgi_degistir(self):
        degistirilecek_kitap_bilgisi = input("Lütfen değiştirilecek kitabı giriniz.")

        #with open("books.txt","r",encoding="utf-8") as f:
        satirlar = self.dosya.read().splitlines()
        indeks = None
        for i,satir in enumerate(satirlar):
            bilgi = satir.split(",")
            if bilgi[0] == degistirilecek_kitap_bilgisi:
                indeks = i
                break

        if indeks is not None:
            print("""
            1)Yazar (1)
            2)Basım Yılı (2)
            3)Sayfa Sayısı (3)
            """)
            kitabin_hangi_bilgisi = input("Kitabın hangi bilgisi değiştirilecek.")
            if kitabin_hangi_bilgisi == "1":
                yeni_bilgi = input("Yazarın yeni adı: ")
                bilgi = satirlar[indeks].split(",")
                bilgi[1] = yeni_bilgi
                satirlar[indeks] = ",".join(bilgi)
            elif kitabin_hangi_bilgisi == "2":
                yeni_bilgi = input("Kitabın yeni basım yılı: ")
                bilgi = satirlar[indeks].split(",")
                bilgi[2] = yeni_bilgi
                satirlar[indeks] = ",".join(bilgi)
            elif kitabin_hangi_bilgisi == "3":
                yeni_bilgi = input("Kitabın yeni sayfa sayısı: ")
                bilgi = satirlar[indeks].split(",")
                bilgi[3] = yeni_bilgi
                satirlar[indeks] = ",".join(bilgi)
            else:
                print("Lütfen geçerli değer giriniz")

            with open("books.txt","w", encoding="utf-8") as f:
                for satir in satirlar:
                    f.write(f"{satir}\n")
        else:
            print("Kitap bulunamadı.")


lib = Kutuphane()

while True:
    print("""
    *** MENÜ ***
    1)Listelemek (1)
    2)Eklemek (2)
    3)Silmek (3)
    4)Kapat (q)
    5)Güncelle (4)
    """)
    islem = input("Lütfen yapacağınız işlemi seçiniz.")
    if islem == "1":
        lib.kitaplari_listele()
    elif islem == "2":
        lib.kitap_ekle()
    elif islem == "3":
        lib.kitap_sil()
    elif islem == "q":
        break
    elif islem == "4":
        lib.bilgi_degistir()
    else:
        print("Lütfen geçerli bir değer giriniz.")

