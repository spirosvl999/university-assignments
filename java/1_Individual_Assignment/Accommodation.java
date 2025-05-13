public class Accommodation extends Entity {
    private String type; // π.χ. "Hotel", "B&B"
    private double pricePerNight;

    public Accommodation(String code, String name, String type, double pricePerNight) {
        super(code, name);
        this.type = type;
        this.pricePerNight = pricePerNight;
    }

    // getters/setters...

    @Override
    public String toString() {
        return super.toString().replace("}", 
               ", type='" + type + "'" +
               ", pricePerNight=" + pricePerNight + "}");
    }
}
