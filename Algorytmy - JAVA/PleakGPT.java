package Algorytmy;

public class PleakGPT {
    public static void main(String[] args) {
        int N = 6;
        int[] tabVi = {6, 2, 3, 2, 3, 1};
        int[] tabWi = {6, 4, 5, 7, 10, 2};
        int maxPojemnoscPlecaka = 10;

        int s = (int) Math.pow(2, N);

        int[] najlepszaKombinacja = new int[N];
        int maxWartosc = 0;

        for (int l = 0; l < s; l++) {
            int V = 0;
            int W = 0;
            int[] kombinacja = new int[N];

            for (int i = 0; i < N; i++) {
                if (((l >> i) & 1) == 1) {
                    if (V + tabVi[i] <= maxPojemnoscPlecaka) {
                        V += tabVi[i];
                        W += tabWi[i];
                        kombinacja[i] = 1;
                    }
                }
            }

            if (W > maxWartosc) {
                maxWartosc = W;
                najlepszaKombinacja = kombinacja.clone();
            }
        }

        System.out.println("Maksymalna wartość plecaka: " + maxWartosc);
        System.out.print("Najlepsza kombinacja przedmiotów: ");
        for (int i = 0; i < N; i++) {
            if (najlepszaKombinacja[i] == 1) {
                System.out.print("[" + tabVi[i] + ", " + tabWi[i] + "] ");
            }
        }
    }

}

