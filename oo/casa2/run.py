from casa import Casa
from pessoa import Pessoa
#orientado a objetos associação bilateral
#teste casa2

casa_da_ana = Casa()
ana = Pessoa('Ana')
ana.set_local(casa_da_ana)
casa_da_ana.set_proprietario(ana)

proprietario = casa_da_ana.get_proprietario()
proprietario.se_apresentar()
ana.apresentar_local()