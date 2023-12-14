import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class Writer {
    private final String fileName;

    public Writer(String fileName) { this.fileName = "store_app/src/" + fileName + ".txt"; }

    public void write() {
        try (FileWriter writer = new FileWriter(fileName);
             Scanner scanner = new Scanner(System.in)) {
            ToyRandomizer toyRandomizer = new ToyRandomizer();

            for (int i = 0; i < 3; i++) {
                System.out.println("Введите id: ");
                int id = scanner.nextInt();
                System.out.println("Введите вес выпадения игрушки: ");
                double frequency = scanner.nextDouble();
                System.out.println("Введите название игрушки: ");
                String name = scanner.next();
                toyRandomizer.addToy(id, frequency, name);
            }

            String result;
            for (int i = 0; i < 10; i++) {
                Toy randomToy = toyRandomizer.getRandomToy();
                if (randomToy != null) result = "Вы выиграли " + randomToy.getName() + "!\n";
                else result = "Игрушка не разыграна.\n";

                writer.write(result);
            }
        } catch (IOException e) {
            System.out.println("Произошла непредвиденная ошибка.");
        }
    }
}