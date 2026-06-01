# Görev Yönetim Uygulaması

Bu proje, Python ile geliştirilmiş basit bir komut satırı görev yönetim uygulamasıdır. Kullanıcı görev ekleyebilir, görevleri listeleyebilir, düzenleyebilir ve silebilir.

## Özellikler

- Görev ekleme
- Görevleri listeleme
- Görev düzenleme
- Görev silme
- Görevleri `gorevler.txt` dosyasında saklama
- Hatalı girişler için kullanıcı uyarıları

## Kullanılan Teknolojiler

- Python 3
- Dosya işlemleri
- Liste veri yapısı
- Fonksiyonel programlama mantığı

## Kurulum

Projeyi bilgisayarınıza indirdikten sonra klasörün içine girin:

```bash
cd gorev-yonetim-uygulamasi
```

Programı çalıştırın:

```bash
python main.py
```

Bazı sistemlerde komut şu şekilde olabilir:

```bash
python3 main.py
```

## Kullanım

Program çalıştırıldığında kullanıcıya aşağıdaki menü gösterilir:

```text
=== GÖREV YÖNETİM UYGULAMASI ===
1. Görevleri Listele
2. Yeni Görev Ekle
3. Görev Düzenle
4. Görev Sil
5. Çıkış
```

Kullanıcı menüden yapmak istediği işlemi seçerek görev listesini yönetebilir.

## Örnek Çıktı

```text
--- GÖREV LİSTESİ ---
Listeniz şu anda boş.
--------------------
```

Görev eklendikten sonra:

```text
--- GÖREV LİSTESİ ---
1. Python çalış
--------------------
```

## Dosya Yapısı

```text
gorev-yonetim-uygulamasi/
├── main.py
├── README.md
├── .gitignore
└── LICENSE
```

## Not

`gorevler.txt` dosyası program çalışırken otomatik oluşur. Bu dosya kişisel görevleri tuttuğu için GitHub'a yüklenmemesi adına `.gitignore` içine eklenmiştir.

## Lisans

Bu proje MIT lisansı ile paylaşılmıştır.
