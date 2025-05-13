import java.util.*;

public class Main {
    private static Scanner scanner = new Scanner(System.in);
    private static List<Poi> pois = new ArrayList<>();

    public static void main(String[] args) {
        pois = DataManager.loadList("pois.ser");

        while (true) {
            System.out.println("\n--- ΜΕΝΟΥ ---");
            System.out.println("1. Προβολή όλων των διαθέσιμων POIs");
            System.out.println("2. Προσθήκη νέου POI");
            System.out.println("3. Αναζήτηση POI βάσει ονόματος");
            System.out.println("4. Διαγραφή POI");
            System.out.println("5. Προβολή κριτικών POIs");
            System.out.println("6. Έξοδος από την εφαρμογή");
            System.out.print("Επιλογή: ");
            String input = scanner.nextLine();

            switch (input) {
                case "1": viewAllPois(); break;
                case "2": addPoi(); break;
                case "3": searchPoiByName(); break;
                case "4": deletePoi(); break;
                case "5": viewPoiComments(); break;
                case "6":
                    DataManager.saveList(pois, "pois.ser");
                    System.out.println("Έξοδος από την εφαρμογή. Τα δεδομένα αποθηκεύτηκαν.");
                    return;
                default: System.out.println("Μη έγκυρη επιλογή.");
            }
        }
    }

    private static void viewAllPois() {
        if (pois.isEmpty()) {
            System.out.println("Δεν υπάρχουν διαθέσιμα POIs.");
            return;
        }
        for (Poi poi : pois) {
            System.out.println(poi);
        }
    }

    private static void addPoi() {
        System.out.print("Κωδικός: ");
        String code = scanner.nextLine();
        System.out.print("Τίτλος: ");
        String name = scanner.nextLine();
        System.out.print("Κατηγορία: ");
        String category = scanner.nextLine();
        System.out.print("Rating: ");
        String rating = scanner.nextLine();
        System.out.print("Γεωγραφική τοποθεσία: ");
        String location = scanner.nextLine();
        System.out.print("Σχόλιο: ");
        String comment = scanner.nextLine();

        Poi poi = new Poi(code, name, category, rating, location, Arrays.asList(comment));
        pois.add(poi);
        System.out.println("Το POI προστέθηκε επιτυχώς.");
    }

    private static void searchPoiByName() {
        System.out.print("Εισάγετε τίτλο προς αναζήτηση: ");
        String name = scanner.nextLine().toLowerCase();
        boolean found = false;
        for (Poi poi : pois) {
            if (poi.getName().toLowerCase().contains(name)) {
                System.out.println(poi);
                found = true;
            }
        }
        if (!found) {
            System.out.println("Δεν βρέθηκε POI με αυτό το όνομα.");
        }
    }

    private static void deletePoi() {
        System.out.print("Εισάγετε τον τίτλο του POI προς διαγραφή: ");
        String name = scanner.nextLine().toLowerCase();
        Iterator<Poi> iterator = pois.iterator();
        boolean deleted = false;
        while (iterator.hasNext()) {
            Poi poi = iterator.next();
            if (poi.getName().toLowerCase().equals(name)) {
                iterator.remove();
                System.out.println("Το POI διαγράφηκε επιτυχώς.");
                deleted = true;
                break;
            }
        }
        if (!deleted) {
            System.out.println("Δεν βρέθηκε POI με αυτόν τον τίτλο.");
        }
    }

    private static void viewPoiComments() {
        if (pois.isEmpty()) {
            System.out.println("Δεν υπάρχουν POIs.");
            return;
        }
        for (Poi poi : pois) {
            System.out.println(poi.getName() + " - Σχόλια: " + poi.getComments());
        }
    }
}