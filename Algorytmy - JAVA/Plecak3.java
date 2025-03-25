package Algorytmy;


public class Plecak3 {
    public static void main(String[] args) {
        int N=6;
        int maxPojemnosc=10;
        int maxWartosc=0;

        int[] tabVi = {6 ,2 ,3 ,2 ,3 ,1};
        int[] tabWi = {6, 4, 5, 7, 10, 2};
        int s=(int)Math.pow(2,N);
        for (int l=0;l<s;l++)
        {
            int V=0;
            int W=0;
            for (int i =0;i<=N;i++){
                if (((l >> i) & 1) == 1) {
                    if (V + tabVi[i] <= maxPojemnosc) {
                        V = V + tabVi[i];
                        W = W + tabWi[i];
                    }
                }
            }
            if (W>maxWartosc){
                maxWartosc=W;
            }
        }
        System.out.println("Maksymalna: "+maxWartosc);
    }
}
