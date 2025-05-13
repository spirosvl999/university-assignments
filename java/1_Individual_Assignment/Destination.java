public class Destination extends Entity {
    private String region;

    public Destination(String code, String name, String region) {
        super(code, name);
        this.region = region;
    }

    public String getRegion() { return region; }
    public void setRegion(String region) { this.region = region; }

    @Override
    public String toString() {
        return super.toString().replace("}", ", region='" + region + "'}");
    }
}
