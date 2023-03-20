
package holamundo;

import java.util.Scanner;

public class Holamundo {

    public static void main(String[] args) {
        
        Scanner in = new Scanner(System.in);
        int edad = 0;
        System.out.println("ingrese su edad: ");
        edad = in.nextInt();
        
        System.out.println("Su edad es: "+ edad);
    }
    
}
