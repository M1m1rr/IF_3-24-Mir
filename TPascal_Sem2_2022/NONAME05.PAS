Program Remedial;
uses crt;
var NS : String;
var Nilai : Integer;

Begin
 clrscr;
writeln('Mirza Aryasatya Akmal');
writeln('X MIPA 5');
writeln('17');
 writeln('------------------------------');
 write('   Nama Siswa  : ');readln(NS);
 write('   Nilai Siswa : ');readln(Nilai);
 writeln('------------------------------');
if (Nilai>=75) then
 begin
  writeln('             LULUS             ')
 end
else if (Nilai>=65) and (Nilai<75) then
 begin
  writeln('            REMEDIAL           ')
 end
else if (Nilai<65) then
 begin
  writeln('             GAGAL             ')
 end;
 readln;
End.