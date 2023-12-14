public class Main {
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
