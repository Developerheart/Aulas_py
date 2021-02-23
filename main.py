if __name__ == '__main__':

    from APS3.classes import ClassePessoa, ClasseSintomas
    from APS3.Telas import Tela
    from APS3.DB.banco_de_dados import cria_bd_app
    import os

    if os.path.exists('ControleCovid.bd'):
        print('Banco já criado')
    else:
        cria_bd_app()

    while True:
        a = Tela.Screen.boasvindas()

        t, c = Tela.Screen.iniciar()

        if t == 'Sair':
            break

        if c['Não']:
            break
        elif c['Pesquisar']:
            a = Tela.Screen.pesquisarid()[1]
            a = int(a['ID'])
            print(a)
            dados = ClassePessoa.Pessoa.pesquisar(a)
            print(dados)
            Tela.Screen.exibirdados(dados)

        else:
            a = Tela.Screen.cadastrar()
            t3 = ClassePessoa.Pessoa(nome=a['nome'], idade=a['idade'], sexo=a['sexo'], historicomedico=a['HISMED'])

            b = Tela.Screen.cadastrarsintomas()
            t1 = ClasseSintomas.Sintoma(descsintomas=b['Descricao'], datainisintomas=b['DataSin'],
                                        dataentconsulta=b['DataCon'],
                                        medicreceitados=b['Medicamentos'])
            print(b)
            print(a)
            id = t1.salvar()[0]
            id = int(id[0])
            print('id', id)
            t3.Salvar(id)
else:
    print('está tentando importar o arquivo main do aplitavio. Executeo diretamente')