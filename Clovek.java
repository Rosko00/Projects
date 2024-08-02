public class Clovek {
    private String jmeno; // súkromný atribút
    private int vek; // súkromný atribút

    // Konstruktor
    public Clovek(String jmeno, int vek) {
        this.jmeno = jmeno;
        this.setVek(vek); // Použitie setteru pre validáciu veku
    }

    // Getter pre jmeno
    public String getJmeno() {
        return jmeno;
    }

    // Getter pre vek
    public int getVek() {
        return vek;
    }

    // Setter pre vek
    public void setVek(int novyVek) {
        if (novyVek > 0) {
            this.vek = novyVek;
        } else {
            throw new IllegalArgumentException("Vek musí byť kladné číslo");
        }
    }

    public static void main(String[] args) {
        // Vytvorenie inštancie
        Clovek clovek = new Clovek("Jozef", 30);

        // Prístup k jmenu (iba čítanie)
        System.out.println(clovek.getJmeno());  // Výpis: Jozef

        // Prístup k veku (čítanie a zápis)
        System.out.println(clovek.getVek());  // Výpis: 30

        // Nastavenie nového veku
        clovek.setVek(35);
        System.out.println(clovek.getVek());  // Výpis: 35

        // Pokus o nastavenie neplatného veku (záporné číslo)
        try {
            clovek.setVek(-5);
        } catch (IllegalArgumentException e) {
            System.out.println(e.getMessage());  // Výpis: Vek musí byť kladné číslo
        }
    }
}
