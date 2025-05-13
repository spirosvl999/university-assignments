import java.util.List;

public class Route extends Entity {
    private List<String> stops;

    public Route(String code, String name, List<String> stops) {
        super(code, name);
        this.stops = stops;
    }

    public List<String> getStops() { return stops; }
    public void setStops(List<String> stops) { this.stops = stops; }

    @Override
    public String toString() {
        return super.toString().replace("}", ", stops=" + stops + "}");
    }
}
