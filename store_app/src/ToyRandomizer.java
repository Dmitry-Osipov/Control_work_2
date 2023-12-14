import java.util.ArrayList;
import java.util.List;
import java.util.Random;

class Toy {
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

public class ToyRandomizer {
    private List<Toy> toys;
    private Random random;

    public ToyRandomizer() {
        toys = new ArrayList<>();
        random = new Random();
    }

    public void addToy(int id, double winPercentage, String name) {
        Toy toy = new Toy(id, winPercentage, name);
        toys.add(toy);
    }

    public Toy getRandomToy() {
        double totalWeight = toys.stream().mapToDouble(t -> t.getWinPercentage()).sum();
        double randomValue = random.nextDouble() * totalWeight;

        double currentWeight = 0;
        for (Toy toy : toys) {
            currentWeight += toy.getWinPercentage();
            if (randomValue <= currentWeight) {
                return toy;
            }
        }

        return null;
    }

    public static void main(String[] args) {
        ToyRandomizer toyRandomizer = new ToyRandomizer();
        toyRandomizer.addToy(1, 2, "Robot");
        toyRandomizer.addToy(2, 2, "Car");
        toyRandomizer.addToy(3, 6, "Doll");

        for (int i = 0; i < 10; i++) {
            Toy randomToy = toyRandomizer.getRandomToy();
            if (randomToy != null) System.out.println("Вы выиграли " + randomToy.getName() + "!");
            else System.out.println("Вы ничего не выиграли. Что-то пошло не так.");
        }
    }
}