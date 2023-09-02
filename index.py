market_isim = 'Crew Bilişim'

def urun_sec():
    print('Laptop : 1', '\n', 'Tablet : 2')
    cevap = input("Lütfen bir ürün seçiniz (1-5): ")
    return cevap

def urun_detayi(urun_id):
    urunler = {
        '1': {'isim': 'Ürün 1', 'fiyat': 35000},
        '2': {'isim': 'Ürün 2', 'fiyat': 15000},
        '3': {'isim': 'Ürün 3', 'fiyat': 25000},
        '4': {'isim': 'Ürün 4', 'fiyat': 13000},
        '5': {'isim': 'Ürün 5', 'fiyat': 22000}
    }
    
    return urunler.get(urun_id)

def main():
    while True:
        print(market_isim + ' Hoşgeldiniz.')
        bütce = int(input('Lütfen bir bütçe belirtiniz: '))
        print('Bütçeniz {}₺ olarak düzenlendi.'.format(bütce))
        print()
        
        urun_id = urun_sec()
        urun = urun_detayi(urun_id)
        
        if urun:
            urun_fiyat = urun['fiyat']
            if bütce >= urun_fiyat:
                toplam = bütce - urun_fiyat
                print('Başarıyla {} satın aldınız. Yeni bakiyeniz {}₺'.format(urun['isim'], toplam))
            else:
                print('Üzgünüz, yeterli bütçeniz yok.')
        else:
            print('Geçersiz ürün seçimi.')

        print('----------------------------------')

if __name__ == "__main__":
    main()
