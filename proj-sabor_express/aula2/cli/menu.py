
from utils.fechar_aplicacao import finalizar_app
from services.novo_restaurante import cadastrar_novo_restaurante
from services.lista_de_restaurantes import listar_restaurantes
from services.alternar_estado_restaurante import alternar_estado_restaurante

class Menu:
    def __init__(self, n_func):
        self.n_func = n_func


    def acionar_funcionalidade(self, opcao):
       # region condicional if
       """ Condicionl com if, elif e else
        if opcao == 1:
            print('Cadastrar restaurante\n')
        elif opcao == 2:
            print('Listar restaurante\n')
        elif opcao == 3:
            print('Ativar restaurante\n')
        else:
            finalizar_app()
        """   
       # endregion 
       # region condicional match case
       match opcao:
            case 1:
               cadastrar_novo_restaurante()
            case 2:
               listar_restaurantes()
            case 3:
                alternar_estado_restaurante()
            case 4:
                finalizar_app()
            case _:
                if opcao is None:
                    print('Digite apenas números\n') 
                else: 
                    print('Opção inválida\n')
       # endregion  
    
