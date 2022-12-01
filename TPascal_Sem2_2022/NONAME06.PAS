Program UH2;
uses crt;
var NP,KT : String;
var HT,JT,TB : Longint;

Begin
 clrscr;
  writeln('---------------------------------------------------');
  writeln('   Kode Tiket : V = VIP, B = Bisnis, E = Ekonomi');
  writeln('---------------------------------------------------');
    write('   NIK Pelanggan   : ');readln(NP);
    write('   Kode Tiket      : ');readln(KT);
  writeln('---------------------------------------------------');
       If KT=('V') Then
 Begin
  HT:=15000;
  writeln('   Kode Tiket      : VIP');
  writeln('   Harga Tiket     : 15000');
  writeln('   Nama Kereta     : Argo Bromo');
  writeln('   Tujuan          : Jakarta - Surabaya');
 End
  Else if KT=('B') Then
 Begin
  HT:=12500;
  writeln('   Kode Tiket      : Bisnis');
  writeln('   Harga Tiket     : 12500');
  writeln('   Nama Kereta     : Argo Lawu');
  writeln('   Tujuan          : Jakarta - Bandung');
 End
  Else if KT=('E') Then
 Begin
  HT:=12500;
  writeln('   Kode Tiket      : Ekonomi');
  writeln('   Harga Tiket     : 12500');
  writeln('   Nama Kereta     : Mutiara Selatan');
  writeln('   Tujuan          : Jakarta - Banjar');
 End
  Else
  Begin
  writeln('   Inputan Tidak Benar ')
  End;

    write('   Jumlah Tiket    : ');readln(JT);
  TB:=(HT*JT);
  writeln('---------------------------------------------------');
  writeln('   Harga Total (Rp): ',TB);
  writeln('---------------------------------------------------');
  writeln('   Selamat Jalan!');
 readln;
End.