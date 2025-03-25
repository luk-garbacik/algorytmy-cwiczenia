package Algorytmy;

public class BrutalnaSiła {
    final static int N = 6; // liczba przedmiotów
    final static int MAX_V = 10; // objetość plecaka
    final static int[] V = {6,2,3,2,3,1}; // objetości przedmiotów
    final static int[] W = {6,4,5,7,10,2}; // wartości przedmiotów

    static int P(int n,int maxV){
        if (n==0 && maxV<V[0]){
            return 0;
        }
        if (n==0 && maxV>=V[0]){
            return W[0];
        }
        int w1=P(n-1,maxV);
        if (V[n]>maxV && n>0){
            return w1;
        }
        int w2=P(n-1,maxV-V[n])+W[n];
        if (w1<w2){
            return w2;
        }
        else {
            return w1;
        }
    }


    public static void main(String[] args) {
        System.out.println("Najwyzsza wartosc przedmiotow: "+P(N-1,MAX_V));
    }
}





















