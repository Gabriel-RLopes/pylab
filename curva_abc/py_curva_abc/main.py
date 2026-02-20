from dataclasses import dataclass
from typing import List


@dataclass
class Produto:
    nome: str
    faturamento: float
    rentabilidade: float
    percentual: float = 0.0
    acumulado: float = 0.0
    classe: str = ''


def calcular_curva_abc(produtos: List[Produto]) -> List[Produto]:
    positivos = [p for p in produtos if p.faturamento > 0]
    negativos = [p for p in produtos if p.faturamento <= 0]

    total = sum(p.faturamento for p in positivos)

    positivos.sort(key=lambda x: x.faturamento, reverse=True)

    acumulado = 0

    for p in positivos:
        p.percentual = p.faturamento / total
        acumulado += p.percentual
        p.acumulado = acumulado

        if p.rentabilidade <= 0.80:
            p.classe = 'A'
        elif p.rentabilidade <= 0.95:
            p.classe = 'B'
        elif p.rentabilidade <= 1:
            p.classe = 'C'
        else:
            p.classe = 'D'

    for p in negativos:
        p.classe = 'D'

    return positivos + negativos


if __name__ == '__main__':
    produtos = [
        Produto('p1', 150000, 20000),
        Produto('p3', 100000, 10000),
        Produto('p4', 70000, 8000),
        Produto('p2', -150000, -5000),
    ]

    resultado = calcular_curva_abc(produtos=produtos)

    for p in resultado:
        print(f'{p}')