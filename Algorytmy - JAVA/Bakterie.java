package Algorytmy;

import java.util.Scanner;

public class Bakterie {
    public static void main(String[] args) {
        Scanner scanner=new Scanner(System.in);
        System.out.println("Podaj pocztkowa liczbe bakterii");
        int poczatkowaLiczbaBakterii= scanner.nextInt();
        System.out.println("Podaj liczbe generacji");
        int generacje = scanner.nextInt();
        int[] liczbaBakterii=new int[generacje+1];
        liczbaBakterii[0]=poczatkowaLiczbaBakterii;
        for (int i=1;i<=generacje;i++)
        {
            liczbaBakterii[i]=liczbaBakterii[i-1]*2;
        }
        int populacja=liczbaBakterii[generacje];
        System.out.println("Po "+generacje+" generacjach liczba bakterii wynosi "+populacja+" zajelo to "+generacje*2+" minut");
    }
}
