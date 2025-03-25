package Algorytmy;

import java.util.Random;

public class MonteCarlo {
    static int liczbaProbek = 100000;
    static int N=6;
    final static int[][] czas= { {0, 7, 20, 21, 12, 23},
                                        {27, 0, 13, 16, 46, 5},
                                        {53, 15, 0, 25, 27, 6},
                                        {16, 2, 35, 0, 47, 10},
                                        {31, 29, 5, 18, 0, 4},
                                        {28, 24, 1, 17, 5, 0}};
    static int[] najlepszaKombinacja;
    static int najlepszyCzas=Integer.MAX_VALUE;
    private static int PoleFigury(int proby) {
        Random random=new Random();
        int i=0;
        int licz=0;
        do {
            double x = random.nextDouble(liczbaProbek + 1) / liczbaProbek;
            double y = random.nextDouble(liczbaProbek + 1) / liczbaProbek;
            double funcja=Math.sin(x);
            if (y<=funcja) {
                licz++;
            }
            i++;

        }while (i<liczbaProbek);
        return licz;
    }

    private static int[] generujKombinacje(){
        //ustawianie kombinacji
        int[] kombinacja=new int[N];
        for (int i=0;i<N;i++){
            kombinacja[i]=i;
        }
        Random random=new Random();
        for (int i=N-1;i>0;i--){
            int j= random.nextInt(i+1);
            int temp=kombinacja[i];
            kombinacja[i]=kombinacja[j];
            kombinacja[j]=temp;
        }
        return kombinacja;
    }

    private static int czasPrzestrojenia(int[] kominacja){
        int czasPrzestrojenia=0;
        for (int i=0;i<N-1;i++){
            czasPrzestrojenia += czas[kominacja[i]][kominacja[i + 1]];
        }
        czasPrzestrojenia += czas[kominacja[N - 1]][kominacja[0]];
        return czasPrzestrojenia;
    }
    private static void LodyWszystkichSmakow(int proby){
        for (int i=0;i<liczbaProbek;i++){
            int[] losowaKombinacja=generujKombinacje();
            int czasPrzestrojenia=czasPrzestrojenia(losowaKombinacja);
            if (czasPrzestrojenia<najlepszyCzas){
                najlepszyCzas=czasPrzestrojenia;
                najlepszaKombinacja=losowaKombinacja;
            }
        }
        System.out.println("Lody wszytsich smakow");
        System.out.println("Najlepzszy czas:"+najlepszyCzas+" Najlepsza kombinacja:"+najlepszaKombinacja);
    }



    public static void main(String[] args) {

        System.out.println("Pole figury:"+PoleFigury(liczbaProbek));
        LodyWszystkichSmakow(liczbaProbek);
    }
}
