from conta import Conta


conta = Conta(123, "Wagner", 55.5, 1000.0)
conta.deposita(1000)
conta.extrato()
conta.saca(200.0)
conta.extrato()

