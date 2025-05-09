         [bits 32]

;        esp -> [ret]  ; ret - adres powrotu do asmloader

a        equ 4
b        equ 5
c        equ 6

;          0:eax
;        + 0:esi
;        -------
;        edi:esi

         mov eax, b  ; eax = b
         mov esi, c  ; esi = c

         mul esi  ; edx:eax = eax*esi

;        mul arg  ; edx:eax = eax*arg

         mov esi, a  ; esi = a

         mov edi, 0  ; edi = 0
         add eax, esi  ; eax = eax + esi

         push edi  ; edi -> stack
         push eax  ; eax -> stack

;        esp -> [eax][edi][ret]

         call getaddr  ; push on the stack the runtime address of format and jump to getaddr
format:
         db 'a + b*c = %llu', 0xA, 0
getaddr:

;        esp -> [format][eax][edi][ret]

         call [ebx+3*4]  ; printf(format, edi:eax);
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

ebx    -> [ ][ ][ ][ ] -> exit
ebx+4  -> [ ][ ][ ][ ] -> putchar
ebx+8  -> [ ][ ][ ][ ] -> getchar
ebx+12 -> [ ][ ][ ][ ] -> printf
ebx+16 -> [ ][ ][ ][ ] -> scanf

%endif