from utils.voltar_ao_menu_principal import voltar_ao_menu_principal
from data.dados import restaurantes

def alternar_estado_restaurante():
    print("""\n\n\033[40;32m𝔸𝕝𝕥𝕖𝕣𝕒𝕣 𝕠 𝕖𝕤𝕥𝕒𝕕𝕠 𝕕𝕠 𝕣𝕖𝕤𝕥𝕒𝕦𝕣𝕒𝕟𝕥𝕖\n\n\033[0m""")
    nome_do_restaurante = input('\nDigite o nome do restaurante que deseja alterar o estado:\n')
    restaurante_encontrado = False

    for restaurante in restaurantes: 
        if nome_do_restaurante.lower() == restaurante['nome'].lower():
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            print(f"O restaurante {restaurante['nome']} está ativo" if restaurante['ativo'] else f"O restaurante {restaurante['nome']} já não está mais em funcionamento.")
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado.')


    input ('\nTecle \"Enter\" para voltar ao menu principal.')
    voltar_ao_menu_principal()