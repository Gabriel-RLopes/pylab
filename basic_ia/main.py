from utils.logger import setup_logger
from model.trainer import Trainer
from model.predictor import Predictor

def menu():
    print('1- treinar ia')
    print('2- testar ia')
    print('0- sair')

def main():
    setup_logger()

    while True:
        menu()
        opcao = input('escolha:')
        if opcao == '1':
            Trainer.train()
        elif opcao =='2':
            texto=input('digite uma frase: ')
            predictor = Predictor()
            resultado = predictor.predict(texto)
            print(resultado)
        elif opcao == 0:
            break
        else:
            print('opcao invalida')


if __name__ == '__main__':
    main()
