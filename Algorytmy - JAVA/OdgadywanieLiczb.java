package Algorytmy;

import java.util.Random;

public class OdgadywanieLiczb {
    public static void main(String[] args) {
        Random rand = new Random();
        int losowaLiczba = rand.nextInt(101); // Generuje liczbę od 0 do 100
        int m=50;

        System.out.println("Twoja liczba to: "+zgadywanie(losowaLiczba,m));
    }
    static double zgadywanie(int losowaLiczba,int m){
        int dolnyPrzedzial=1;
        int gornyPrzedzial=100;
        do {
            if (m>losowaLiczba){
                System.out.println(m+" jest za duze");
                gornyPrzedzial=m-1;
            }
            if (m<losowaLiczba){
                System.out.println(m+" jest za male");
                dolnyPrzedzial=m+1;
            }
            m=((dolnyPrzedzial+gornyPrzedzial)/2);
        }while (!(m==losowaLiczba));

        return m;
    }}

