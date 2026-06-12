import os
from data.dados import restaurantes 
from utils.voltar_ao_menu_principal import voltar_ao_menu_principal
from utils.converter_para_booleano import converter_para_booleano
"""
No python você pode criar listas ou tuplas para armazenar
dados. A primeira diferença enre elas é a sintaxe.
Enquanto listas são definidas com colchetes `[]`
as tuplas são definidas com parênteses `()`.
A segunda diferença entre elas é a mutabilidade.
Listas são mutáveis e possuem até mesmo funções 
próprias para isso, como `append()`, `extend()`, 
`insert()`, `remove()`, entre outras. Já as tuplas
não são mutáveis, muito menos possuem funções próprias
para isso.
Devido a imutabilidade, as tuplas são mais rápidas
do que as listas, porém as listas são mais flexíveis,
pois permitem operações com os dados.
Podemos resumir dizendo que as tuplas são mais apropriadas
para armazenar constantes, enquanto as listas
são mais adequadas para armazenar variáveis.
"""

def cadastrar_novo_restaurante():    
    os.system('cls')
    print("""\n\n\033[40;32mℂ𝕒𝕕𝕒𝕤𝕥𝕣𝕠 𝕕𝕖 𝕟𝕠𝕧𝕠𝕤 𝕣𝕖𝕤𝕥𝕒𝕦𝕣𝕒𝕟𝕥𝕖𝕤\n\n\033[0m""")
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar:\n')
    categoria_do_restaurante = input('\nEsse restaurante oferece qual tipo de comida?\n')
    esse_restaurante_esta_ativo = converter_para_booleano(input('\nEsse restaurante está ativo atualmente?\n'))
    restaurantes.append({
        'nome': nome_do_restaurante,
        'categoria': categoria_do_restaurante,
        'ativo': esse_restaurante_esta_ativo})
    
    print(f'\n\n\033[40;32mO restaurante {nome_do_restaurante} foi cadastrado com sucesso!\033[0m\n\n')
    
    input ('\nTecle \"Enter\" para voltar ao menu principal.')

    voltar_ao_menu_principal()



    

    

    

