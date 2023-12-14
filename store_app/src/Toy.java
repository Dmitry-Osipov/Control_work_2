public class Toy {
    private final String name;
    private final double winPercentage;
    private final int id;

    public Toy(int id, double winPercentage, String name) {
        this.id = id;
        this.winPercentage = winPercentage;
        this.name = name;
    }

    public String getName() { return name; }

    public double getWinPercentage() { return winPercentage; }

    public int getId() { return id; }
}
