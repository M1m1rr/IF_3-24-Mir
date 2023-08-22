#Quiz==Quiz==Quiz==Quiz==Quiz==Quiz==Quiz==Quiz==Quiz==Quiz==Quiz==Quiz==Quiz==Quiz==Quiz==Quiz==Quiz==

print('======================')
print('KURSUS MENJAHIT YANI-6')
print('======================')

keahlian = ['A. Menjahit Kebaya', 'B. Menjahit Celana Bahan Kain', 'C. Menjahit Celana Bahan Denim', 'D. Menjahit Tas']
print('KEAHLIAN : ')
for listkeahlian in keahlian :
    print(listkeahlian)
print('======================')
nama = input('Nama Calon Siswa : ')
input_keahlian = str(input('Pilih Kursus [A - D] : '))

if input_keahlian == 'A':
    print('Keahlian Kursus : Menjahit Kebaya')
    harga_kursus = 150000
    waktu = int(input('Lama Waktu Kursus (Minggu) = '))
    total = int(harga_kursus)*int(waktu)
    print('Total Biaya Kursus Yang Harus Dibayar = ', total)
elif input_keahlian == 'B':
    print('Keahlian Kursus : Menjahit Celana Bahan Kain')
    harga_kursus = 200000
    waktu = int(input('Lama Waktu Kursus (Minggu) = '))
    total = int(harga_kursus)*int(waktu)
    print('Total Biaya Kursus Yang Harus Dibayar = ', total)
elif input_keahlian == 'C':
    print('Keahlian Kursus : Menjahit Celana Bahan Denim')
    harga_kursus = 250000
    waktu = int(input('Lama Waktu Kursus (Minggu) = '))
    total = int(harga_kursus)*int(waktu)
    print('Total Biaya Kursus Yang Harus Dibayar = ', total)
elif input_keahlian == 'D':
    print('Keahlian Kursus : Menjahit Jas')
    harga_kursus = 300000
    waktu = int(input('Lama Waktu Kursus (Minggu) = '))
    total = int(harga_kursus)*int(waktu)
    print('Total Biaya Kursus Yang Harus Dibayar = ', total)
else :
    print('Invalid') 
    quit()

saldo = int(input('Uang Pembayaran Anda = Rp '))
if saldo == total:
    print('Saldo Pas')
    print('Terimakasih,', nama, 'Telah Memilih Kursus di YANI-6')
elif saldo < total :
    print('Saldo Tidak Mencukupi')
elif saldo > total :
    kembalian = int(saldo)-int(total)
    print('Uang Kembalian Anda = Rp', kembalian)
    print('Terimakasih,', nama, 'Telah Memilih Kursus di YANI-6')
