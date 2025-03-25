package Algorytmy;

public class plecakVW {
    public static void main(String[] args) {
        int N = 6;
        float[] tabVi = {6, 2, 3, 2, 3, 1};
        float[] tabWi = {6, 4, 5, 7, 10, 2};
        float maxPojemnoscPlecaka = 10;
        float V=0;
        float[] tabVW=new float[N];
        int s = (int) Math.pow(2, N);
        int[] najlepszaKombinacja = new int[N];
        float wartosc=0;
        float gen=0;
        for (int i=0;i<N;i++){
            tabVW[i]=tabWi[i]/tabVi[i];
        }
        for (int l=1;l<N;l++){
        for (int i=1;i<N;i++) {
            if (tabVW[i-1]<tabVW[i])
            {
                gen=tabVW[i];
                tabVW[i]=tabVW[i-1];
                tabVW[i-1]=gen;
                gen=tabVi[i];
                tabVi[i]=tabVi[i-1];
                tabVi[i-1]=gen;
                gen=tabWi[i];
                tabWi[i]=tabWi[i-1];
                tabWi[i-1]=gen;
            }
        }}
        for (int i=0;i<6;i++){
            if (V+tabVi[i]<=maxPojemnoscPlecaka){
                wartosc=wartosc+tabWi[i];
                V=V+tabVi[i];
            }
        }
        for (int i=0;i<N;i++) {
            System.out.println(tabVi[i]+" "+tabWi[i]+" "+tabVW[i]);
        }
        System.out.println(wartosc);
    }
}
