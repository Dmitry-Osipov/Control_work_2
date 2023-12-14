import java.util.ArrayList;
import java.util.List;
import java.util.Random;


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
            if (randomValue <= currentWeight) return toy;
        }

        return null;
    }
}