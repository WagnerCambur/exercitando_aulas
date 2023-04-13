from conta import Conta


conta = Conta(123, "Wagner", 55.5, 1000.0)
conta.__deposita(300.0)
conta.__extrato()
conta.__saca(100.0)
conta.__extrato()

