#include <stdio.h>
#include <stdlib.h>

/*
r0  r1  r2
|---|---|       .
0   1   2   3   4   5   6    indeksy
1   1   2   3   5   8   13   wartości
    |---|---|
    r0  r1  r2

Przesunięcie ramki w prawo:

r0 = r1
r1 = r2
r2 = r1 + r0
*/

int fibo1(int n) {
int r0 = 1;
int r1 = 1;
int r2 = 2;

if (n == 0) return r0;
if (n == 1) return r1;
if (n == 2) return r2;

int i;
for (i = 1; i <= n-2; i++) {
r0 = r1;
r1 = r2;
r2 = r0 + r1;
}

return r2;
}

/*
- dokonaj analizy wywołanai fibo1(4)

* fibo(4) =
  r0 = 1
  r1 = 1
  r2 = 2
  
  4 == 0  false 
  4 == 1  false
  4 == 2  false
  
  i
  i = 1
  1 <= 2   r0 = 1
     r1 = 2
   r2 = 1 + 2 = 3   i = 2
   
  2 <= 2   r0 = 2
     r1 = 3
   r2 = 2 + 3 = 5   i = 3
   
  3 <= 2   false
  
  return r2 = 5 
  
- narysuj graf obliczeń dla fibo1(4)  

f(0)  f(1)    f(2)
         \   /  |
          f(3)  |
             \  |
              f(4)
*/

int main() {
    printf("fibo.c\n\n");
    
    int n = 4;
    
    printf("fibo1(%d) = %d\n", n, fibo1(n));
    
    return 0;
}