import java.io.Serializable;
import java.util.ArrayList;
import java.util.List;

public class Poi extends Entity implements Serializable {
    private String category;
    private String rating;
    private String location;
    private List<String> comments;

    public Poi(String code, String name, String category, String rating, String location, List<String> comments) {
        super(code, name);
        this.category = category;
        this.rating = rating;
        this.location = location;
        this.comments = comments != null ? comments : new ArrayList<>();
    }

    public String getCategory() { return category; }
    public void setCategory(String category) { this.category = category; }

    public String getRating() { return rating; }
    public void setRating(String rating) { this.rating = rating; }

    public String getLocation() { return location; }
    public void setLocation(String location) { this.location = location; }

    public List<String> getComments() { return comments; }
    public void setComments(List<String> comments) { this.comments = comments; }

    @Override
    public String toString() {
        return super.toString().replace("}",
               ", category='" + category + "', rating='" + rating +
               "', location='" + location + "', comments=" + comments + "}");
    }
}