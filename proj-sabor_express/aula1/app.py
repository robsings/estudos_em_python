
from utils.input_usuario import obter_entrada_menu
# use fsymbols para decorar o título do app
titulo_app = "\n𝕊𝕒𝕓𝕠𝕣 𝔼𝕩𝕡𝕣𝕖𝕤𝕤"

menu = f"""
1. Cadastrar restaurante
2. Listar restaurante
3. Ativar restaurante
4. Sair
"""
print(f"{titulo_app}\n{menu}")

opcao = obter_entrada_menu()
print(f"\n\nOpção escolhida:{opcao}\n")

print('A', 'L','U','R','A', sep ='\n')
