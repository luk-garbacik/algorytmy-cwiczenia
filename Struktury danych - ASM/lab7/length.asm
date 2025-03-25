         [bits 32]

;        esp -> [ret]  ; ret - adres powrotu do asmloader

%ifdef COMMENT

123 / 10 = 12
12 / 10 = 1
1 / 10 = 0
0

%endif

n        equ 831

         mov ecx, 0  ; ecx = 0
         
         mov ebp, 10  ; ebp = 10

;        edx:eax = 0:n

         mov eax, n  ; eax = n
petla    mov edx, 0  ; edx = 0

         div ebp     ; eax = edx:eax / ebp  ; iloraz
                     ; edx = edx:eax % ebp  ; reszta

         inc ecx  ; ecx++
         
         cmp eax, 0  ; eax - 0           ; OF SF ZF AF PF CF affected
         jnz petla   ; jump if not zero  ; ZF = 0

         push ecx  ; ecx -> stack
         
;        esp -> [ecx][ret]

         call getaddr  ; push on the stack the run-time address of format and jump to getaddr
format:
         db "length = %u", 0xA, 0
getaddr:

;        esp -> [format][ecx][ret]

         call [ebx+3*4]  ; printf(format, ecx);
         add esp, 2*4    ; esp = esp + 8

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
