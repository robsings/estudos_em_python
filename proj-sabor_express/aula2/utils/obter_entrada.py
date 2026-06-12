def obter_entrada_menu():
    try:
        entrada = int(input("\n\tEscolha uma das opções exibidas: "))
        return entrada
    except ValueError as e:
        entrada = str(e).split("'")[1]
        return entrada
    
    # region outra forma de tratar erro onde o usuário digita uma string
    """except ValueError:
        return None """
    #endregion
    
