
def validar(msg, validos):
    valor = str(input(msg)).upper()
    while not valor in validos:
        print("Digitou errado")
        valor = str(input(msg)).upper()
        
    return valor
        
def buscarMaiorElevador(opcoes):
    itens = [0,0,0];
    for resposta in respostas:
        for opcao in opcoes:
            itens[opcoes.index(opcao)] += 1;

    return opcoes[itens.index(max(itens))]

elevadores = ["A", "B", "C"]
turnos = ["M", "V", "N"]
respostas = []


while (True):
    elevador = validar("Informe o elevador mais utilizado: (A, B, C)", elevadores)
    turno = validar("Informe o turno mais utilizado: (M, V, N)", turnos)

    respostas.append([elevador, turno])   
    
    if input("Deseja continuar? (S/N)").upper() != "S":
        break
    
print("------------") 
print(buscarMaiorElevador(elevadores));    
print("------------")   

elevadoresUtilizados = [0,0,0];
for resposta in respostas:
    
    if resposta[0] == "A":
        elevadoresUtilizados[0] += 1;
    if resposta[0] == "B":
        elevadoresUtilizados[1] += 1;
    if resposta[0] == "C":
        elevadoresUtilizados[2] += 1;
        
maiorIndice = elevadoresUtilizados.index(max(elevadoresUtilizados))
print("O elevador mais utilizado foi o elevador ", elevadores[maiorIndice])

turnosUtilizados = [0,0,0]
for resposta in respostas:    
    if resposta[0] == elevadores[maiorIndice]:
        if resposta[1] == "M":
            turnosUtilizados[0] += 1;
        if resposta[1] == "V":
            turnosUtilizados[1] += 1;
        if resposta[1] == "N":
            turnosUtilizados[2] += 1;

indiceTurno = turnosUtilizados.index(max(turnosUtilizados))
print("O elevador ", elevadores[maiorIndice], " foi mais utilizado no turno ", turnos[indiceTurno])





