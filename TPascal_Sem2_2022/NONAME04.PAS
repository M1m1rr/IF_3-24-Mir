Program Nilai;
uses crt;
var NH1,NH2,NT,NPAS : Integer;
var NS : String;
var NA : Real;

Begin
 clrscr;
 writeln('<---------------------------->');
 write('  <b>Nama Siswa = ');readln(NS);
 write('   Nilai Harian 1 = ');readln(NH1);
 write('   Nilai Harian 2 = ');readln(NH2);
 write('   Nilai Tugas    = ');readln(NT);
 write('   Nilai PAS      = ');readln(NPAS);
 writeln('<---------------------------->');

 NA:=((NH1+NH2+NT)/3)*0.75+(NPAS*0.25);

End.