         [bits 32]

;        esp -> [ret]  ; ret - adres powrotu do asmloader

liczba   equ -10

         mov eax, liczba  ; eax = liczba
         mov ecx, eax     ; ecx = eax

         test eax, eax
         jns nieujemna  ; jump if sign not ser  ; SF = 0

         neg ecx  ; ecx = -ecx

nieujemna:
          
         push ecx  ; ecx -> stack
         push eax  ; eax -> stack
         
;        esp -> [eax][ecx][ret]

         call getaddr  ; push on the stack the run-time address of format and jump to getaddr
format:
         db "liczba = %d", 0xA
         db "modul = %d", 0xA, 0
getaddr:

;        esp -> [format][eax][ecx][ret]

         call [ebx+3*4]  ; printf(format, eax, ecx);
         add esp, 3*4    ; esp = esp + 12

;        esp -> [ret]

         push 0          ; esp -> [00 00 00 00][ret]
         call [ebx+0*4]  ; exit(0);

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

Tablica API

ebx    -> [ ][ ][ ][ ] -> exit
ebx+4  -> [ ][ ][ ][ ] -> putchar
ebx+8  -> [ ][ ][ ][ ] -> getchar
ebx+12 -> [ ][ ][ ][ ] -> printf
ebx+16 -> [ ][ ][ ][ ] -> scanf

%endif
