
from utils.obter_entrada import obter_entrada_menu
from cli.menu import Menu
import os
# use fsymbols para decorar o título do app
# https://stackoverflow.com/questions/4842424/list-of-ansi-color-escape-sequences

#os.system('cls')
titulo_app = "\n\033[40;32m𝕊𝕒𝕓𝕠𝕣 𝔼𝕩𝕡𝕣𝕖𝕤𝕤\033[0m"

menu_lista = f"""\033[40m
1. Cadastrar restaurante
2. Listar restaurante
3. Mudar o status de um restaurante
4. Sair
\033[0m"""

def main():
    while True:
        print(f"{titulo_app}\n{menu_lista}")

        opcao_escolhida = obter_entrada_menu()
        menu = Menu(opcao_escolhida)
        print(f"\n\n\033[40;32mOpção escolhida: {opcao_escolhida}\033[0m\n")
        menu.acionar_funcionalidade(opcao_escolhida)
        #print('A', 'L','U','R','A', sep ='\n')

if __name__ == "__main__":
    main()

