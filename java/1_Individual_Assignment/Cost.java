public class Cost extends Entity {
    private double amount;

    public Cost(String code, String name, double amount) {
        super(code, name);
        this.amount = amount;
    }

    public double getAmount() { return amount; }
    public void setAmount(double amount) { this.amount = amount; }

    @Override
    public String toString() {
        return super.toString().replace("}", ", amount=" + amount + "}");
    }
}
