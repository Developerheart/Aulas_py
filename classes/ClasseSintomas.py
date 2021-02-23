if __name__ == '__main__':
    print('Está tentando executar uma modulo diretamente, por favor, executeo pelo arquivo main!!')
else:
    class Sintoma:
        def __init__(self, descsintomas='Não descrito', datainisintomas='Não informado', dataentconsulta='data_De_HOJE',
                     medicreceitados='Nenhum'):
            self.__DescSintomas = descsintomas
            self.__DataIniSintomas = datainisintomas
            self.__DataEntConsulta = dataentconsulta
            self.__MedicReceitados = medicreceitados

        def salvar(self):
            import sqlite3
            conexao = sqlite3.connect('ControleCovid.bd')
            cursor = conexao.cursor()
            cursor.execute('''
            insert into Sintomas (descsintomas, datainisintomas, dataentconsulta, medicreceitados) VALUES (?,?,?,?)
            ''', [self.__DescSintomas, self.__DataIniSintomas, self.__DataEntConsulta, self.__MedicReceitados])
            conexao.commit()
            cursor.execute(''' 
            select MAX(id_sintoma) from main.Sintomas 
            ''')
            id = cursor.fetchall()
            cursor.close()
            return id
