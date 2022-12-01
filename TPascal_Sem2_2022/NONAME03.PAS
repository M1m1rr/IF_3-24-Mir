Program Buku;
uses crt;
var NP,NB : String;
var LP : Integer;

Begin
clrscr;
write('Nama Peminjam = ');readln(NP);
write('Nama Buku = ');readln(NB);
write('Lama Pinjam (Hari) = ');readln(LP);

if LP >= 7 then
  writeln('Tidak Terkena Denda' )
else if LP < 7 then
  writeln('Terkena Denda' );
readln;
End.