def converter_para_booleano(valor):
    valor = valor.lower()
    if valor in ['sim', 's', 'yes', 'y']:
        return True
    elif valor in ['nao', 'não', 'n', 'no']:
        return False
    else:
        raise ValueError('Valor inválido')