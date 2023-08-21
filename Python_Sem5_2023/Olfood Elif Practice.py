print('===========')
print('Online Food')
print('===========')

food = ['1. Ayam Geprek', '2. Ayam Goreng', '3. Ayam Geprek + Nasi', '4. Ayam Goreng + Nasi', '5. Ayam Paket Spesial']
drink = ['1. Air Putih', '2. Teh Manis(Panas/Dingin)', '3. Soda', '4. Kopi']

i_name = str(input('Nama Pemesan = '))
print('Masukkan angka untuk melihat menu : ')
print('1. Makanan')
print('2. Minuman')
i_menu0 = int(input('Pilih Menu = '))

if i_menu0 == 1:
    for foodlist in food :
        print(foodlist) 
    i_food0 = int(input('Pilih Pesanan = '))
    if i_food0 == 1:
        o_price0 = 7000
        print('Harga = 7000')
        i_foodqty = int(input('Jumlah Pesanan = '))
    elif i_food0 == 2:
        o_price0 = 7500
        print('Harga = 7500')
        i_foodqty = int(input('Jumlah Pesanan = '))
    elif i_food0 == 3:
        o_price0 = 12000
        print('Harga = 12000')
        i_foodqty = int(input('Jumlah Pesanan = '))
    elif i_food0 == 4:
        o_price0 = 12500
        print('Harga = 12500')
        i_foodqty = int(input('Jumlah Pesanan = '))
    elif i_food0 == 5:
        o_price0 = 15000
        print('Harga = 15000')
        i_foodqty = int(input('Jumlah Pesanan = '))
    else :
        print('Invalid')
    
    o_foodtotal = int(i_foodqty)*int(o_price0)
    print('Harga Pesanan = ', o_foodtotal)
    print('')
    i_extra = int(input('Tambah minum (1 = Ya , 2 = Tidak) = '))
    if i_extra == 1:
        for drinklist in drink :
            print(drinklist)
        i_drink = int(input('Pilih Minuman = '))
        if i_drink == 1:
            o_price1 = 3000
            print('Harga = 3000')
            i_drinkqty = int(input('Jumlah Minuman = '))
        elif i_drink == 2:
            o_price1 = 4000
            print('Harga = 4000')
            i_drinkqty = int(input('Jumlah Minuman = '))
        elif i_drink == 3:
            o_price1 = 4500
            print('Harga = 4500')
            i_drinkqty = int(input('Jumlah Minuman = '))
        elif i_drink == 4:
            o_price1 = 5000
            print('Harga = 5000')
            i_drinkqty = int(input('Jumlah Minuman = '))
        else : 
            print('Invalid')
            
        o_drinktotal = int(i_drinkqty)*int(o_price1)
        print('Harga Minuman Total = ', o_drinktotal)
        print('')
        o_ordertotal = int(o_drinktotal)+int(o_foodtotal)
        print('Total Order = ', o_ordertotal)
        print('')
        
        i_uangbayar = int(input('Masukkan Jumlah Saldo = '))
        if i_uangbayar < o_ordertotal :
            print('Saldo Tidak Cukup')
        elif i_uangbayar == int(o_ordertotal) :
            print('Saldo Pas')
        elif i_uangbayar >= o_ordertotal :
            o_kembali = int(i_uangbayar)-int(o_ordertotal)
            print('Kembalian = ', o_kembali)
        else :
            print('Invalid')
    elif i_extra == 2:
        o_ordertotal = o_foodtotal
        print('Total Order = ', o_foodtotal)
        i_uangbayar = int(input('Masukkan Jumlah Saldo = '))
        if i_uangbayar < o_ordertotal :
            print('Saldo Tidak Cukup')
        elif i_uangbayar == int(o_ordertotal) :
            print('Saldo Pas')
        elif i_uangbayar >= o_ordertotal :
            o_kembali = int(i_uangbayar)-int(o_ordertotal)
            print('Kembalian = ', o_kembali)
        
    else :
        print('Invalid')
        
elif i_menu0 == 2:
    for drinklist in drink :
        print(drinklist)
    i_drink = int(input('Pilih Minuman = '))
    if i_drink == 1:
        o_price1 = 3000
        print('Harga = 3000')
        i_drinkqty = int(input('Jumlah Minuman = '))
    elif i_drink == 2:
        o_price1 = 4000
        print('Harga = 4000')
        i_drinkqty = int(input('Jumlah Minuman = '))
    elif i_drink == 3:
        o_price1 = 4500
        print('Harga = 4500')
        i_drinkqty = int(input('Jumlah Minuman = '))
    elif i_drink == 4:
        o_price1 = 5000
        print('Harga = 5000')
        i_drinkqty = int(input('Jumlah Minuman = '))
    else : 
      print('Invalid')
            
    o_drinktotal = int(i_drinkqty)*int(o_price1)
    o_ordertotal = o_drinktotal
    print('Harga Minuman Total = ', o_drinktotal)
    print('')
    print('Total Order = ', o_ordertotal)
    print('')
    
    i_uangbayar = int(input('Masukkan Jumlah Saldo = '))
    if i_uangbayar < o_ordertotal :
        print('Saldo Tidak Cukup')
    elif i_uangbayar == int(o_ordertotal) :
        print('Saldo Pas')
    elif i_uangbayar >= o_ordertotal :
        o_kembali = int(i_uangbayar)-int(o_ordertotal)
        print('Kembalian = ', o_kembali)
    else :
        print('Invalid')
    
else : 
    print('Invalid')