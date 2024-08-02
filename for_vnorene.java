public class for_vnorene {
    public static void main(String[] args) {
        for (int a = 1; a <= 10; a++) {
            for (int b = 1; b <= 10; b++) {
                System.out.printf("%4d", a * b); // Vypíše hodnotu zarovnanú do šírky 4 znakov
            }
            System.out.println(); // Nový riadok po každom riadku násobilky
        }
    }
}
