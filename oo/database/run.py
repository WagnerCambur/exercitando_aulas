from postgres import PostgresDB
#orientado a objetos principio aberto/fechado
from repositorio import Repositorio

#teste database
db_conn = PostgresDB()
repo = Repositorio()

repo.insert(db_conn)
repo.select(db_conn)