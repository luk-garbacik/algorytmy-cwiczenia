package Algorytmy;

public class ProgramowanieDynamiczne {
    final static int MAX_V = 10; // objętość plecaka
    final static int[] V = {6, 2, 3, 2, 3, 1}; // objętości przedmiotów
    final static int[] W = {6, 4, 5, 7, 10, 2}; // wartości przedmiotów
    final static int N = V.length; // liczba przedmiotów
    final static int liczebnoscKrolikow=1000;
    private static int P() {
        int[] poprzeni=new int[MAX_V+1];
        int[] aktulany=new int[MAX_V+1];

        for (int i=0;i<=N;i++){
            for (int j=0;j<=MAX_V;j++){
                if (i==0 || j==0){
                    aktulany[j]=0;
                }
                else if (V[i-1]<=j){
                    int opcja2=W[i - 1] + poprzeni[j-V[i-1]];
                    aktulany[j]=Math.max(opcja2, aktulany[j]);
                }
                else {
                    aktulany[j]=poprzeni[j];
                }
            }
            int[] temp = poprzeni;
            poprzeni = aktulany;
            aktulany = temp;
        }
        return aktulany[MAX_V];
    }
    static int Krole(int max){
        int miesiace=1;
        int aktualnaLiczbaPar=0;
        int poprzedniaLiczbaPar=1;
        while (aktualnaLiczbaPar<=max){
            int temp=aktualnaLiczbaPar;
            aktualnaLiczbaPar=poprzedniaLiczbaPar+aktualnaLiczbaPar;
            poprzedniaLiczbaPar=temp;
            //System.out.println("aktualna liczba: "+aktualnaLiczbaPar+" miesiace:"+miesiace);
            miesiace++;
        }
        return miesiace-1;
    }
    public static void main(String[] args) {
        int maxVaue=P();
        System.out.println("Maksymalna wartosc:"+maxVaue);
        System.out.println("Kroliki osiagna liczebnosc "+liczebnoscKrolikow+" w "+Krole(liczebnoscKrolikow)+"miesiecy");

    }
}
