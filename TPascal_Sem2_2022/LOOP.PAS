Program Repetition;
uses crt;                                                                 S
var X,NA : Integer;

Begin
 clrscr;
   Write(' Repetition Amount : ');Readln(NA);
  For X := NA Downto 0 Do
   If X Mod 2 = 1 Then
 Begin
   Write(X, ' ');
 End;
 readln;
End.