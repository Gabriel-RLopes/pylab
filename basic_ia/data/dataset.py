def load_dataset():
    texts = [
        "eu amo programar",
        "python é maravilhoso",
        "odeio bugs no sistema",
        "esse erro me deixa irritado",
        "o sistema ficou excelente",
        "que código horrível"
    ]

    labels = [
        "positivo",
        "positivo",
        "negativo",
        "negativo",
        "positivo",
        "negativo"
    ]

    return texts, labels
