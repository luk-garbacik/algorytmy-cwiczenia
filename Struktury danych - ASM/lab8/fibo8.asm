         [bits 32]

;        esp -> [ret]  ; ret - adres powrotu do asmloader

%ifdef COMMENT
 
a   b      a+2b
|---|   |---|
1   1   2   3   5   8   13   wartosci
    |---|   |---|
    b  a+b    2a+3b

Przesuniecie ramki:

xadd (b, a) = (a+b, b) // wynik w rejestrze b

Schemat oblicze�:

                xadd        xadd           xadd
(a, b) -> (b, a) => (a+b, b) => (a+2b, a+b) => (2a+3b, a+2b) => ...

%endif

n        equ 5
 
         mov ebp, ebx  ; ebp = ebx
 
         mov ecx, n  ; ecx = n

         mov eax, 1  ; eax = 1
         mov ebx, 1  ; ebx = 1

         cmp ecx, 1  ; ecx - 0  ; ZF affected
         ja next2

         jmp done

next2    sub ecx, 1  ; ecx = ecx - 1

shift    xadd ebx, eax

         loop shift

done:    push ebx

;        esp -> [ebx][ret]

         call getaddr  ; push on the stack the run-time address of format and jump to getaddr
format:
         db "fibo = %i", 0xA, 0
getaddr:

;        esp -> [format][ebx][ret]

         call [ebp+3*4]  ; pritnf(format, ebx)
         add esp, 2*4    ; esp = esp + 8

;        esp -> [format]

         push 0          ; esp -> [00 00 00 00][ret]
         call [ebp+0*4]  ; exit(0);

; asmloader API
;
; ESP wskazuje na prawidlowy stos
; argumenty funkcji wrzucamy na stos
; EBX zawiera pointer na tablice API
;
; call [ebx + NR_FUNKCJI*4] ; wywolanie funkcji API
;
; NR_FUNKCJI:
;
; 0 - exit
; 1 - putchar
; 2 - getchar
; 3 - printf
; 4 - scanf
;
; To co funkcja zwr�ci jest w EAX.
; Po wywolaniu funkcji sciagamy argumenty ze stosu.
;
; https://gynvael.coldwind.pl/?id=387
 
%ifdef COMMENT
 
ebx    -> [ ][ ][ ][ ] -> exit
ebx+4  -> [ ][ ][ ][ ] -> putchar
ebx+8  -> [ ][ ][ ][ ] -> getchar
ebx+12 -> [ ][ ][ ][ ] -> printf
ebx+16 -> [ ][ ][ ][ ] -> scanf
 
%endif