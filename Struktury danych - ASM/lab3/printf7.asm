         [bits 32]

;        esp -> [ret]  ; ret - adres powrotu do asmloader

a        equ 4

         call getaddr
addr_a:
         dd a  ; [ ][ ][ ][ ]  ; define double word
getaddr:

;        esp -> [addr_a][ret]

         mov eax, [esp]  ; eax = *(int*)esp = addr_a
         push dword [eax]  ; *(int*)eax = *(int*)addr_a = a -> stack

;        esp -> [a][addr_a][ret]

         call getaddr2  ; push on the stack the run-time address of format and jump to getaddr
format:
         db "a = %d", 0xA, 0
getaddr2:

;        esp -> [format][a][addr_a][ret]

         call [ebx+3*4]  ; printf(format, a);
         pop ebx         ; Remove addr_a from the stack
         pop ebx         ; Remove a from the stack
         pop ebx         ; Remove format from the stack

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
