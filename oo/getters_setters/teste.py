from alarme import Alarme
#acessando atributos privados
al = Alarme(False)
#al.__estado #não será possivel acessar atributo diretamente
al.get_estado()
#al.set_estado(True) #acessando atributo e alterando para True