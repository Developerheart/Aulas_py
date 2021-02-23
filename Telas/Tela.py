if __name__ == '__main__':
    print('Você está tentando rodar esse programa diretamente')
else:
    from PySimpleGUI import *
    from time import sleep

    # Layout


    class Screen:

        @staticmethod
        def boasvindas():
            theme(new_theme='Reddit')
            layout = [
                [Text('Bem vindo', text_color='green', font='Courir 25')],
                [Button('Continuar', focus=1, font='Courir 12')]
            ]

            janela = Window('Tela de boas vindas', size=(300, 300), font='Courir 14').Layout(layout)
            event = janela.read()

            janela.Close()
            return event

        @staticmethod
        def iniciar():
            theme(new_theme='Reddit')
            layout = [
                [Text('Deseja cadastrar: ', font='Courir 12', text_color='green')],
                [Checkbox('Sim', key="Sim", font='Courir 12', text_color='green'), Checkbox('Não', key='Não',
                                                                                            font='Courir 12',
                                                                                            text_color='red')],
                [Checkbox('Pesquisar', key="Pesquisar", font='Courir 12', text_color='blue')],
                [Button("Confirmar", font='Courir 12', focus=1), Button("Sair", font='Courir 12', focus=1)]
            ]
            # janela
            janela = Window("Tela de confirmação", size=(300, 300)).layout(layout)
            # Extrair dados
            button, values = janela.read()

            janela.Close()

            return button, values

        @staticmethod
        def cadastrar():
            layout2 = [
                [Text("Informe seus cadastros")],
                [Text("Nome", size=(8, 0)), Input(size=(100, 0), key='nome')],
                [Text("Idade", size=(8, 0)), Input(size=(100, 0), key='idade')],
                [Text("Sexo", size=(8, 0)), Input(size=(100, 0), key='sexo')],
                [Text("Historico medico", size=(8, 0)), Input(size=(100, 3), key='HISMED')],
                [Button("Enviar Dados")]

            ]
            # janela
            screen = Window("tela de cadastro", size=(300, 300), font='Courir 14').layout(layout2)
            # Dados
            button, values = screen.read()
            print(values)
            screen.Close()
            return values

        @staticmethod
        def cadastrarsintomas():
            layout3 = [
                [Text("Sintomas", font='Courir 12')],
                [Text("Descrição dos sintomas", size=(14, 0)), Input(size=(100, 0), key='Descricao')],
                [Text("Data de inicio dos sintomas", size=(14, 0)), Input(size=(100, 0), key='DataSin')],
                [Text("Data da consulta", size=(14, 0)), Input(size=(100, 3), key='DataCon')],
                [Text("Medicamentos receitados", size=(14, 0)), Input(size=(100, 3), key='Medicamentos')],
                [Button("Enviar Dados")]
            ]

            screen2 = Window("Sintomas", size=(400, 300)).layout(layout3)

            button, values = screen2.read()
            screen2.Close()
            return values

        @staticmethod
        def pesquisarid():
            layout = [
                [Text('Pesquisando id', size=(14, 0)), Input(size=(100, 0), key='ID')],
                [Button("Pesquisar")]
            ]
            janela = Window('Tela de pesquisa', size=(300, 300), font='Courir 12').Layout(layout)
            buton, values = janela.read()

            janela.close()

            return buton, values
        @staticmethod
        def exibirdados(*dados):
            layout = [
                [Text('Dados do requisitados')],
                [Text(f'Nome: {dados[0]}')],
                [Button('Continuar', focus=1, font='Courir 12')]

            ]
            janela = Window(f'Dados {id}', size=(600, 600), font='Courir 13').Layout(layout)
            button, values = janela.read()
            janela.close()
