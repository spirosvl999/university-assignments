import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class DataManager {
    @SuppressWarnings("unchecked")
    public static <T> List<T> loadList(String filename) {
        File f = new File(filename);
        if (!f.exists()) return new ArrayList<>();
        try (ObjectInputStream in = new ObjectInputStream(new FileInputStream(f))) {
            return (List<T>) in.readObject();
        } catch (Exception e) {
            System.err.println("Load " + filename + " failed: " + e.getMessage());
            return new ArrayList<>();
        }
    }

    public static <T> void saveList(List<T> list, String filename) {
        try (ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream(filename))) {
            out.writeObject(list);
        } catch (IOException e) {
            System.err.println("Save " + filename + " failed: " + e.getMessage());
        }
    }
}