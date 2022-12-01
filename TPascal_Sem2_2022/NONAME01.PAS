Program KKM;
uses crt;
var NS : String;
var UH1,UH2,NT : Integer;

Begin
clrscr;
write('Nama Siswa = ');readln(NS);
write('Nilai UH 1 = ');readln(UH1);
write('Nilai UH 2 = ');readln(UH2);
NT:=UH1 + UH2;
writeln('Rata Rata Nilai = ',NT);

if NT >= 120 then
  writeln('SISWA LULUS' )
else if NT < 120 then
  writeln('SISWA TIDAK LULUS' );
readln;
End.
