print('--------------------------')
print('--------Toko Buah---------')
print('--------------------------')
nama = input('Nama Pembeli : ')
buah = input('Buah apa : ')


if (buah == 'apel'):
 harga = 6500
if (buah == 'semangka'):
 harga = 7500
if (buah == 'alpukat'):
 harga = 4500
if (buah == 'jambu'):
 harga = 5500
if (buah == 'melon'):
 harga = 10500
if (buah == 'pisang'):
 harga = 5000

print('Harga per kg : ', harga)

jml = input('Berapa kg : ')

total = int(jml)*int(harga)
print('Totalnya : ', int(total))
    
if total <= 47500:
    print('Anda tidak mendapatkan diskon')
    
if total >= 50000:
    diskon = (int(total)/100)*5
    print('Anda mendapat diskon 5% sebesar : ', diskon)
    total1 = int(total)-int(diskon)
    print('Total harga : ', total1)
    
if total >= 100000:
    diskon = (int(total)/100)*20
    print('Anda mendapat diskon 20% sebesar : ', diskon)
    total1 = int(total)-int(diskon)
    print('Total harga : ', total1)
    
uangmu = int(input('Uangmu berapa : '))
kembalian = int(uangmu)-int(total1)

if uangmu < total1:
    print('Uang Tidak Cukup')

elif uangmu > total1:
 print('Kembalianmu : ', int(kembalian))
 
elif uangmu == total1:
 print('Uang Pas, Terimakasih sudah berbelanja!')
