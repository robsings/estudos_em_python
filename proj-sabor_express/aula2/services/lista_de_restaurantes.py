import os
from data.dados import restaurantes 
from utils.voltar_ao_menu_principal import voltar_ao_menu_principal

def listar_restaurantes():
    os.system('cls')
    print("""\n\n\033[40;32mℝ𝕖𝕤𝕥𝕒𝕦𝕣𝕒𝕟𝕥𝕖𝕤 𝕝𝕚𝕤𝕥𝕒𝕕𝕠𝕤\n\n\033[0m""")

    for restaurante in restaurantes:
        nome_do_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = "Ainda está ativo." if restaurante['ativo'] else "Já não está mais ativo."
        print(f"""
              • Restaurante {nome_do_restaurante}
              \tCategoria: {categoria}
              \tAtivo: {ativo}\n\n
        """)
    input ('\nTecle \"Enter\" para voltar ao menu principal.')

    voltar_ao_menu_principal()