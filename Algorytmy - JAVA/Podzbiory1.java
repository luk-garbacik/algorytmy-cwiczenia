package Algorytmy;

public class Podzbiory1 {
    public static void main(String[] args) {
        int a,b,c,d;
        int suma=0;
        for (a=0;a<=1;a++)
            for (b=0;b<=1;b++)
                for (c=0;c<=1;c++)
                    for (d=0;d<=1;d++)
                    {
                        suma++;
                        System.out.print("{");
                        if (a==1){System.out.print("1");}
                        if (b==1){System.out.print("2");}
                        if (c==1){System.out.print("3");}
                        if (d==1){System.out.print("4");}
                        System.out.print("}");
                        System.out.println("");
                    }
        System.out.println("Liczba zbiorow: "+suma);
    }
}
//i 0 1 2 3 4 5
//Vi 6 2 3 2 3 1
//Wi 6 4 5 7 10 2
//44 Problem doboru załogi statku kosmicznego