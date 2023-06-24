
// nama = maulana hafizh aiputra
// nim = 064002200034
import java.util.Scanner;

interface Animal {
    void sound(); 
}

class Cat implements Animal {
    @Override
    public void sound() {
        System.out.println("Meoww");
    }
}

class Dog implements Animal {
    @Override
    public void sound() {
        System.out.println("Wooff");
    }
}

class Opet implements Animal {
    @Override
    public void sound(){
        System.out.println("pasisipapasipasipaga");
    }
}

public class SuaraAnimal {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Pilih suara hewan (dog/cat/opet):");
        String choice = scanner.nextLine();

        Animal animal;
        if (choice.equalsIgnoreCase("dog")) {
            animal = new Dog(); 
        } else if (choice.equalsIgnoreCase("cat")) {
            animal = new Cat(); 
        } else if (choice.equalsIgnoreCase("opet")){
            animal = new Opet();
        } else {
            System.out.println("Pilihan tidak valid.");
            return;
        }

        animal.sound(); 
    }
}
