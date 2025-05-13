public class Client extends Entity {
    private String email;

    public Client(String code, String name, String email) {
        super(code, name);
        this.email = email;
    }

    public String getEmail() { return email; }
    public void setEmail(String email) { this.email = email; }

    @Override
    public String toString() {
        return super.toString().replace("}", ", email='" + email + "'}");
    }
}
