print('Toko Online')
print('===========')
print('Selamat Datang!')
print('Silakan isi input pemesanan anda di bawah : ')

nama = input('Nama pemesan : ')
print(nama)

print('Pilihan Merchandise')
print('')
print('Masukkan angka untuk memilih merchandise : ')
print('1. Sepatu')
print('2. Baju')
print('3. Celana')
print('4. Tas')

nomerch = int(input('Masukkan nomor merchandise : '))

if (nomerch == 1):
    harga = 150000
    print('Anda memesan : Sepatu')
    print('Harga per unit : 150000')
    print('Pilih size : ')
    print('1. 37')
    print('2. 38')
    print('3. 39')
    print('4. 40')
    size = int(input('Masukkan Size : '))
    
    if size == 1:
        harga = harga*1
        print('Harga ukuran : ', harga)
    elif size == 2:
        harga = harga + 2000
        print('Harga ukuran : ', harga)
    elif size == 3:
        harga = harga + 3000
        print('Harga ukuran : ', harga)
    elif size == 4:
        harga = harga + 4000
        print('Harga ukuran : ', harga)
    else :
        print('Invalid')
    
    qty = input('Jumlah barang : ')
    total = int(qty)*int(harga)
    print('Total bayar : ', total) 
    
    
elif (nomerch == 2):
    harga = 65000
    print('Anda memesan : Baju')
    print('Harga per unit : 65000')
    print('Pilih size : ')
    print('1. S')
    print('2. M')
    print('3. L')
    print('4. XL')
    size = int(input('Masukkan Size : '))
    if size == 1:
        harga = harga*1
        print('Harga ukuran : ', harga)
    elif size == 2:
        harga = harga + 2000
        print('Harga ukuran : ', harga)
    elif size == 3:
        harga = harga + 3000
        print('Harga ukuran : ', harga)
    elif size == 4:
        harga = harga + 4000
        print('Harga ukuran : ', harga)
    else :
        print('Invalid')
    
    qty = input('Jumlah barang : ')
    total = int(qty)*int(harga)
    print('Total bayar : ', total) 
    
elif (nomerch == 3):
    harga = 45000
    print('Anda memesan : Celana')
    print('Harga per unit : 45000')
    print('Pilih size : ')
    print('1. S')
    print('2. M')
    print('3. L')
    print('4. XL')
    size = int(input('Masukkan Size : '))
    if size == 1:
        harga = harga*1
        print('Harga ukuran : ', harga)
    elif size == 2:
        harga = harga + 2000
        print('Harga ukuran : ', harga)
    elif size == 3:
        harga = harga + 3000
        print('Harga ukuran : ', harga)
    elif size == 4:
        harga = harga + 4000
        print('Harga ukuran : ', harga)
    else :
        print('Invalid')
    
    qty = input('Jumlah barang : ')
    total = int(qty)*int(harga)
    print('Total bayar : ', total) 
    
elif (nomerch == 4):
    harga = 50000
    print('Anda memesan : Tas')
    print('Harga per unit : 50000')
    print('Invalid')
    
    qty = input('Jumlah barang : ')
    total = int(qty)*int(harga)
    print('Total bayar : ', total) 
     
if total >= 225000:
    diskon = (int(total)/100)*5
    print('Anda mendapat diskon 5% sebesar : ', diskon)
    total = int(total)-int(diskon)
    print('Total harga : ', total)
    
elif total >= 500000:
    diskon = (int(total)/100)*20
    print('Anda mendapat diskon 20% sebesar : ', diskon)
    total = int(total)-int(diskon)
else :
    print('Anda tidak mendapatkan diskon')
    
uangmu = int(input('Uangmu berapa : '))
kembalian = int(uangmu)-int(total)

if uangmu < total:
    print('Uang Tidak Cukup')

elif uangmu > total:
 print('Kembalianmu : ', int(kembalian))
 
elif uangmu == total:
 print('Uang Pas, Terimakasih sudah berbelanja!')
    
    
    