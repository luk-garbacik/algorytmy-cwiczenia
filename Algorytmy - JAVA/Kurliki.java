package Algorytmy;

import java.util.Scanner;

public class Kurliki {
    public static void main(String[] args) {
        Scanner scanner=new Scanner(System.in);
        System.out.println("Podaj liczbe miesiecy");
        int miesiace= scanner.nextInt();
        int[] populacjaKrolikow=new int[miesiace+1];

        populacjaKrolikow[0]=1;
        populacjaKrolikow[1]=1;

        for (int i=2;i<=miesiace;i++)
        {
         populacjaKrolikow[i]=populacjaKrolikow[i-1]+populacjaKrolikow[i-2];
        }
        int populacjaKurlikow=populacjaKrolikow[miesiace];
        System.out.println("Po "+miesiace+" miesiacach byłoby "+populacjaKurlikow+" par kurlikow");
    }
}
