#orientado a objetos principio aberto/fechado
# from repositorio import Repositorio
# from database import PostgresDB

# #teste database
# db_conn = PostgresDB()
# repo = Repositorio()

# repo.insert(db_conn)
# repo.select(db_conn)


#orientado a objetos associação bilateral
#teste casa2
from casa2 import Casa, Pessoa

casa_da_ana = Casa()
ana = Pessoa('Ana')
ana.set_local(casa_da_ana)
casa_da_ana.set_proprietario(ana)

proprietario = casa_da_ana.get_proprietario()
proprietario.se_apresentar()

ana.apresentar_local()
