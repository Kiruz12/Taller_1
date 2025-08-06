import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;
public class Main {
    public static void main(String[] args) {
Scanner lea = new Scanner(System.in);
List<Object>Ventas= new ArrayList<>();
int op = 0;
boolean n = true;
int id = 0;
while (n == true){
    System.out.println("Menú.");
    System.out.println("1. Crear nueva venta.");
    System.out.println("2. Listar ventas.");
    System.out.println("3. Buscar por ID.");
    System.out.println("4. Modificar.");
    System.out.println("5. Eliminar.");
    System.out.println("6. Calcular totales (ingreso total).");
    System.out.println("7. Salir.");
    op = lea.nextInt();
    while(op <= 0 || op > 7){
        System.out.println("Ingrese un número válido");
        op = lea.nextInt();
    }
        switch (op) {
            case 1:
            int[] ventas = new int[5];
            id = id + 1;
            ventas[1] = id;
            System.out.println("Ingrese el número de el producto:");
            ventas[2] = lea.nextInt();
            System.out.println("Ingrese la cantidad de producto:");
            ventas[3] = lea.nextInt();
            System.out.println("Ingrese el precio unitari0 de el producto:");
            ventas[4] = lea.nextInt();
            System.out.println("El id asignado para el producto es 00"+id);
            Ventas.add(ventas);
            System.out.println(Ventas);
             break;
            case 2:
        
             break;
            case 3:
        
             break;
            case 4:
        
             break;
            case 5:
        
             break;
            case 6:
        
             break;
            case 7:
        
             break;
        }
}
}
}