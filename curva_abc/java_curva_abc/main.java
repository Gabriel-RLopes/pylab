import java.util.*;
import java.util.stream.Collectors;

class Produto {
    String nome;
    double faturamento;
    double rentabilidade;
    double percentual;
    double acumulado;
    String classe;

    public Produto(String nome, double faturamento, double rentabilidade) {
        this.nome = nome;
        this.faturamento = faturamento;
        this.rentabilidade = rentabilidade;
    }

    @Override
    public String toString() {
        return nome + " | Classe: " + classe + 
               " | %: " + percentual + 
               " | Acum: " + acumulado;
    }
}

public class CurvaABC {

    public static List<Produto> calcular(List<Produto> produtos) {

        List<Produto> positivos = produtos.stream()
                .filter(p -> p.faturamento > 0)
                .sorted((a, b) -> Double.compare(b.faturamento, a.faturamento))
                .collect(Collectors.toList());

        List<Produto> negativos = produtos.stream()
                .filter(p -> p.faturamento <= 0)
                .collect(Collectors.toList());

        double total = positivos.stream()
                .mapToDouble(p -> p.faturamento)
                .sum();

        double acumulado = 0;

        for (Produto p : positivos) {
            p.percentual = p.faturamento / total;
            acumulado += p.percentual;
            p.acumulado = acumulado;

            if (p.rentabilidade < 0) {
                p.classe = "D";
            } else if (acumulado <= 0.80) {
                p.classe = "A";
            } else if (acumulado <= 0.95) {
                p.classe = "B";
            } else {
                p.classe = "C";
            }
        }

        for (Produto p : negativos) {
            p.classe = "E";
        }

        positivos.addAll(negativos);
        return positivos;
    }

    public static void main(String[] args) {

        List<Produto> produtos = Arrays.asList(
                new Produto("P1", 150000, 20000),
                new Produto("P3", 100000, 10000),
                new Produto("P4", 70000, 8000),
                new Produto("P2", -150000, -5000)
        );

        List<Produto> resultado = calcular(produtos);

        resultado.forEach(System.out::println);
    }
}