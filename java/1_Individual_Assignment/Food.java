public class Food extends Entity {
    private String type;
    
    public Food(String code, String name, String type) {
        super(code, name);
        this.type = type;
    }

    public String getType() { return type; }
    public void setType(String type) { this.type = type; }

    @Override
    public String toString() {
        return super.toString().replace("}", ", type='" + type + "'}");
    }
}
