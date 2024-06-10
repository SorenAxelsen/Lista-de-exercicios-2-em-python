import java.util.ArrayList;
import java.util.List;

// Classe abstrata Veiculo
abstract class Veiculo {
    // Método abstrato mover
    public abstract void mover();
}

// Subclasse Carro que herda de Veiculo
class Carro extends Veiculo {
    @Override
    public void mover() {
        System.out.println("Carro se moveu na estrada.");
    }
}

// Subclasse Moto que herda de Veiculo
class Moto extends Veiculo {
    @Override
    public void mover() {
        System.out.println("Moto se moveu na rodovia.");
    }
}

public class Main {
    public static void main(String[] args) {
        // Criando uma lista de objetos do tipo Veiculo
        List<Veiculo> veiculos = new ArrayList<>();

        // Adicionando objetos Carro e Moto na lista
        veiculos.add(new Carro());
        veiculos.add(new Moto());

        // Iterando sobre a lista e chamando o método mover para cada veículo
        for (Veiculo veiculo : veiculos) {
            veiculo.mover();
        }
    }
}

