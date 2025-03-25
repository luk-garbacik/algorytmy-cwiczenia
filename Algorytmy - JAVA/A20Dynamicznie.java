package Algorytmy;

public class A20Dynamicznie {
    static int iloscPar=100;
    public static int P(){
        if (iloscPar<=1){
            return iloscPar;
        }

        int miesiace=0;
        int aktulanaLiczbaPar=0;
        int poprzedniaLiczbaPar=1;

        while (aktulanaLiczbaPar<=iloscPar){
            int temp=aktulanaLiczbaPar;
            aktulanaLiczbaPar=poprzedniaLiczbaPar+aktulanaLiczbaPar;
            poprzedniaLiczbaPar=temp;
            miesiace++;
            System.out.println("Populacja krolikow  "+aktulanaLiczbaPar+" w "+miesiace+"miesiacu");
        }
        return miesiace;
    }

    public static void main(String[] args) {
        int p=P();
        System.out.println("Populacja krolikow przekroczy "+iloscPar+" w "+p+"miesiecy");
    }
}
