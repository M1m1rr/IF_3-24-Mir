Program RepUnt;
uses crt;
var X :Integer;

Begin
clrscr;
 Writeln('                              Mirza Aryasatya Akmal');
 Writeln('                                     X MIPA 5      ');
 Writeln('                                        17         ');

 X:=1;
  Repeat
   Begin
    Write(X);
    Write(', ');
    X:=X+2;
   End;
    Until X>=100;
 readln;
End.