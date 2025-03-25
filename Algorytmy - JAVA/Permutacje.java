package Algorytmy;

public class Permutacje {

    final static int N = 6; // permutacje n-elementowe
    private static int[] l = new int[N];
    private static int[] lmin = new int[N];
    public static int[][] switchTimesI = {
            {0, 7, 20, 21, 12, 23},
            {27, 0, 13, 16, 46, 5},
            {53, 15, 0, 25, 27, 6},
            {16, 2, 35, 0, 47, 10},
            {31, 29, 5, 18, 0, 4},
            {28, 24, 1, 17, 5, 0}
    };
    public static int[][] switchTimesJ = {
            {0, 27, 53, 16, 31, 28},
            {7, 0, 15, 2, 29, 24},
            {20, 13, 0, 35, 5, 1},
            {21, 16, 25, 0, 18, 17},
            {12, 46, 27, 47, 0, 5},
            {23, 5, 6, 10, 4, 0}
    };
    public static void main(String[] args) {
        permutacje(0);
        System.out.println("Minimalny całkowity czas przestrojenia maszyny wynosi " + czasMin + ". ");
        System.out.print("Oto przykładowa kolejność produkcji lodów, dla której całkowity czas przestrojenia maszyny jest minimalny: ");
        for (int j = 0; j < N; j++) {
            System.out.print(lmin[j] + " ");
        }
        System.out.println("");
    }
    public static int czas = 0;
    public static int czasMin = 99999999;
    static void permutacje(int i) {
        if (i == N) {
            czas = 0;
            int prevsmak = l[0];
            for (int j = 0; j < N; j++) {
                System.out.print(l[j] + " ");
                int smak = l[j];
                if (j == 2 || j == 4) {
                    czas += switchTimesJ[prevsmak-1][smak-1];
                } else if(j == 0) {
                    continue;
                } else {
                    czas += switchTimesI[prevsmak-1][smak-1];
                    if(j == 5){
                        prevsmak = smak;
                        smak = l[0];
                        czas += switchTimesJ[prevsmak-1][smak-1];
                    }
                }
                prevsmak = smak;
            }
            System.out.println("Czas " + czas);
            if(czasMin > czas){
                czasMin = czas;
                for(int j = 0; j < N; j++){
                    lmin[j]=l[j];
                }
            }
        } else {
            for (int j = 1; j <= N; j++) {
                int k;
                for (k = 0; k < i; k++) {
                    if (l[k] == j) {
                        break;
                    }
                }
                if (k == i) {
                    l[k] = j;
                    permutacje(i + 1);
                }
            }
        }
    }
}
