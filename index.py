market_isim = 'Crew Bilişim'

while(True):
    print(market_isim + ' Hoşgeldiniz.')
    bütce = int(input('Lütfen bir bütce belirtiniz: '))
    print('Bütceniz {}₺ olarak düzenlendi.'.format(bütce))
    print('                 ')
    print('\n', 'Laptop : 1', '\n', 'Tablet : 2') 
    print('                 ')
    cevap = input( )
    if (cevap == '1'):
        print('          ')
        print('▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬', '\n', '1.', 'Ürün 1 :', '35000₺', '\n', '2.', 'Ürün 2 :', '15000₺', '\n', '3.', 'Ürün 3 :', '25000₺', '\n', '4.', 'Ürün 4 :', '13000₺', '\n', '5.', 'Ürün 5 :', '22000₺')
        print('▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬')
        print("Lütfen bir ürün ıd'si belirtiniz.")
        ürün = input( )
        if (ürün == '1'):
            ürün_fiyat = 35000
            toplam = bütce - ürün_fiyat
            print('Başarıyla {} nolu ürünü satın aldınız. Yeni bakiyeniz {}₺'.format(ürün, toplam))
            print('▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬')
        if (ürün == '2'):
            ürün_fiyat = 15000
            toplam = bütce - ürün_fiyat
            print('Başarıyla {} nolu ürünü satın aldınız. Yeni bakiyeniz {}₺'.format(ürün, toplam))
            print('▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬')
        if (ürün == '3'):
            ürün_fiyat = 25000
            toplam = bütce - ürün_fiyat
            print('Başarıyla {} nolu ürünü satın aldınız. Yeni bakiyeniz {}₺'.format(ürün, toplam))
            print('▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬')
        if (ürün == '4'):
            ürün_fiyat = 13000
            toplam = bütce - ürün_fiyat
            print('Başarıyla {} nolu ürünü satın aldınız. Yeni bakiyeniz {}₺'.format(ürün, toplam))
            print('▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬')
        if (ürün == '5'):
            ürün_fiyat = 25000
            toplam = bütce - ürün_fiyat
            print('Başarıyla {} nolu ürünü satın aldınız. Yeni bakiyeniz {}₺'.format(ürün, toplam))
            print('▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬')
