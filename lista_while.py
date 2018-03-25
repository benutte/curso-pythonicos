var = []
while True:
    msg = raw_input("Digite um valor ou nada para sair: ")
    if msg:
        var.append(msg)
    else:
        break
for valor in var:
    print valor
