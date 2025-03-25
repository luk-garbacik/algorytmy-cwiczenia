package Algorytmy;

import java.util.Scanner;

public class SymbolNewtona {
    public static void main(String[] args){
        Scanner scanner=new Scanner(System.in);
        int n=scanner.nextInt();
        int k=scanner.nextInt();

        System.out.println(newton(n,k));
    }
    static int newton(int n,int k) {
        if (n == k || k == 0) {
            return 1;
        } else if (k > 0 && n > k) {
            int resultN = 1;
            int resultK = 1;
            int resultNK = 1;
            for (int i = 1; i <= n; i++) {
                resultN = resultN * i;
            }
            for (int i = 1; i <= k; i++) {
                resultK = resultK * i;
            }
            for (int i = 1; i <= (n - k); i++) {
                resultNK = resultNK * i;
            }

            System.out.println(resultN + "/" + resultK + "*" + resultNK);
            return (resultN / (resultK * resultNK));
        }
        else {
            System.out.println("Jest problem");
            return 0;
        }
    }
}
