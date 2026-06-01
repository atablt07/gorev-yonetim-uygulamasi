import os

# --- AYARLAR ---
DOSYA_ADI = "gorevler.txt"


def dosya_kontrol_ve_yukle():
    """
    Program başladığında görevleri dosyadan okur.
    Eğer dosya yoksa boş bir liste döndürür.
    Dosya kodlaması utf-8 olarak ayarlanmıştır.
    """
    gorevler = []

    if os.path.exists(DOSYA_ADI):
        try:
            with open(DOSYA_ADI, "r", encoding="utf-8") as dosya:
                for satir in dosya:
                    if satir.strip():
                        gorevler.append(satir.strip())
        except Exception as e:
            print(f"Hata: Dosya okunurken bir sorun oluştu! ({e})")

    return gorevler


def gorevleri_kaydet(gorevler):
    """
    Herhangi bir değişiklik yapıldığında listeyi dosyaya kaydeder.
    """
    try:
        with open(DOSYA_ADI, "w", encoding="utf-8") as dosya:
            for gorev in gorevler:
                dosya.write(gorev + "\n")
    except Exception as e:
        print(f"Hata: Dosya kaydedilirken bir sorun oluştu! ({e})")


def gorevleri_listele(gorevler):
    """
    Mevcut görevleri numaralandırarak ekrana basar.
    Liste boşsa kullanıcıyı bilgilendirir.
    """
    print("\n--- GÖREV LİSTESİ ---")

    if not gorevler:
        print("Listeniz şu anda boş.")
    else:
        for index, gorev in enumerate(gorevler, start=1):
            print(f"{index}. {gorev}")

    print("-" * 20)


def yeni_gorev_ekle(gorevler):
    """
    Kullanıcıdan yeni görev alır ve listeye ekler.
    Boş giriş yapılmasını engeller.
    """
    print("\n--- YENİ GÖREV EKLE ---")
    giris = input("Yapılacak görevi giriniz: ").strip()

    if giris:
        gorevler.append(giris)
        gorevleri_kaydet(gorevler)
        print("Görev başarıyla eklendi.")
    else:
        print("Uyarı: Boş bir görev ekleyemezsiniz!")


def gorev_duzenle(gorevler):
    """
    Mevcut bir görevi günceller.
    Geçersiz sıra numarası girilirse hata mesajı verir.
    """
    gorevleri_listele(gorevler)

    if not gorevler:
        return

    print("\n--- GÖREV DÜZENLE ---")

    try:
        sira = int(input("Düzenlemek istediğiniz görevin numarasını girin: "))

        if 1 <= sira <= len(gorevler):
            yeni_metin = input(f"'{gorevler[sira - 1]}' yerine ne yazılsın?: ").strip()

            if yeni_metin:
                gorevler[sira - 1] = yeni_metin
                gorevleri_kaydet(gorevler)
                print("Görev başarıyla güncellendi.")
            else:
                print("Uyarı: Görev metni boş olamaz. İşlem iptal edildi.")
        else:
            print("Hata: Geçersiz görev numarası!")

    except ValueError:
        print("Hata: Lütfen sayısal bir değer giriniz.")


def gorev_sil(gorevler):
    """
    Seçilen görevi listeden siler.
    Hatalı girişleri kontrol eder.
    """
    gorevleri_listele(gorevler)

    if not gorevler:
        return

    print("\n--- GÖREV SİL ---")

    try:
        sira = int(input("Silmek istediğiniz görevin numarasını girin: "))

        if 1 <= sira <= len(gorevler):
            silinen = gorevler.pop(sira - 1)
            gorevleri_kaydet(gorevler)
            print(f"'{silinen}' listeden silindi.")
        else:
            print("Hata: Geçersiz görev numarası!")

    except ValueError:
        print("Hata: Lütfen sayısal bir değer giriniz.")


def ana_menu():
    """
    Programın ana döngüsüdür.
    Kullanıcı çıkış yapana kadar menüyü gösterir.
    """
    gorevler = dosya_kontrol_ve_yukle()

    while True:
        print("\n=== GÖREV YÖNETİM UYGULAMASI ===")
        print("1. Görevleri Listele")
        print("2. Yeni Görev Ekle")
        print("3. Görev Düzenle")
        print("4. Görev Sil")
        print("5. Çıkış")

        secim = input("Seçiminiz (1-5): ").strip()

        if secim == "1":
            gorevleri_listele(gorevler)
        elif secim == "2":
            yeni_gorev_ekle(gorevler)
        elif secim == "3":
            gorev_duzenle(gorevler)
        elif secim == "4":
            gorev_sil(gorevler)
        elif secim == "5":
            print("Programdan çıkılıyor. İyi günler!")
            break
        else:
            print("Hata: Lütfen 1 ile 5 arasında geçerli bir seçim yapınız.")


if __name__ == "__main__":
    ana_menu()
