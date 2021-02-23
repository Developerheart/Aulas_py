if __name__ == '__main__':
    print('o modulo a seguir não deve ser executado diretamente, por favor, ultilize-o atraves do arquivo main!')
else:
    class Pessoa:
        def __init__(self, nome='Steve', idade=18, sexo='Não declarado', historicomedico='Sem histórico medico'):
            self.__nome = nome
            self.__idade = idade
            self.__sexo = sexo
            self.__historicomedico = historicomedico

        @property
        def nome(self):
            return self.__nome

        @property
        def idade(self):
            return self.__idade

        @property
        def sexo(self):
            return self.__sexo

        @property
        def historicomedico(self):
            return self.__historicomedico


        def Salvar(self, id):
            """ Insere os dados no bd"""
            import sqlite3

            conexao = sqlite3.connect('ControleCovid.bd')
            cursor = conexao.cursor()
            cursor.execute('''
            insert into Paciente (nome, idade, sexo, historicomedico, id_sintomas) values (?, ?, ?, ?, ?)
            ''', (self.__nome, self.__idade, self.__sexo, self.__historicomedico, id))
            conexao.commit()
            cursor.close()

        @staticmethod
        def pesquisar(id):
            import sqlite3
            conexao = sqlite3.connect('ControleCovid.bd')
            cursor = conexao.cursor()
            cursor.execute('''
            select * from Paciente where id_sintomas = ?
            ''', [id])
            dados = list(cursor.fetchall())

            cursor.close()
            return dados

