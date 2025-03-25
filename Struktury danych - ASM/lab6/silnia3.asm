         [bits 32]

;        esp -> [ret]  ; ret - adres powrotu do asmloader

n        equ 5

         mov ecx, n  ; ecx = n
         mov eax, 1  ; eax = 1

         test ecx, ecx  ; ecx & ecx  ; OF=0 SF ZF PF CF=0 affected

         je done  ; jump if equal ; ZF = 1

         cmp ecx, 1  ; ecx & 1  ; OF=0 SF ZF PF CF=0 affected

         je done  ; jump if equal ; ZF = 1


petla    mul ecx  ; edx:eax = eax*ecx

;        mul arg  ; edx:eax = eax*arg

         cmp ecx, 1  ; ecx & 1  ; OF=0 SF ZF PF CF=0 affected

         je done  ; jump if not equal  ; ZF = 0

         dec ecx  ; ecx--

         loop petla

done     push eax
         
;        esp -> [eax][ret]

         call getaddr  ; push on the stak the run-time address of format and jump to get address
format:
         db "silnia = %u", 0xA, 0
getaddr:

;        esp -> [format][eax][ret]

         call [ebx+3*4]  ; printf(format, eax);
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

ebx    -> [ ][ ][ ][ ] -> exit
ebx+4  -> [ ][ ][ ][ ] -> putchar
ebx+8  -> [ ][ ][ ][ ] -> getchar
ebx+12 -> [ ][ ][ ][ ] -> printf
ebx+16 -> [ ][ ][ ][ ] -> scanf

%endif
