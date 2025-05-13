public class TourDate extends Entity {
    private String date; 
    
    public TourDate(String code, String name, String date) {
        super(code, name);
        this.date = date;
    }

    public String getDate() { return date; }
    public void setDate(String date) { this.date = date; }

    @Override
    public String toString() {
        return super.toString().replace("}", ", date='" + date + "'}");
    }
}
