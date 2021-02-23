if __name__ == '__main__':
    print('Está tentando executar esse arquivo diretamente')
else:
    import sqlite3


    def cria_bd_app():
        conexao = sqlite3.connect('ControleCovid.bd')
        cursor = conexao.cursor()
        cursor.execute('''
            create table Sintomas (
            id_sintoma integer not null primary key autoincrement,
            descsintomas varchar not null,
            datainisintomas varchar not null,
            dataentconsulta varchar not null,
            medicreceitados varchar not null
            );
        ''')

        cursor.execute(''' 
            create table Paciente (
            id_paciente integer not null primary key autoincrement,
            nome varchar not null,
            idade integer not null,
            sexo varchar not null,
            historicomedico varchar not null, 
            id_sintomas integer,
            foreign key(id_sintomas) references Sintomas(id_sintoma)
            );
        ''')

        conexao.close()
        print('log: Banco de dados criado com sucesso')

