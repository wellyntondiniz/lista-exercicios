
def validar(msg, validos):
    valor = str(input(msg)).upper()
    while not valor in validos:
        print("Digitou errado")
        valor = str(input(msg)).upper()
        
    return valor
        
def buscarMaiorQuantidade(opcoes, respostas):
    itens = [];
    for opcao in opcoes:
        itens.append(0)
        
    for resposta in respostas:
        for opcao in opcoes:
            if (opcao in resposta):
                itens[opcoes.index(opcao)] += 1;


    return opcoes[itens.index(max(itens))]


def buscarMaior(itens):
    return max(itens, key=itens.get);

def buscarMenor(itens):
    return min(itens, key=itens.get);
    

elevadores = {"A":0, "B":0, "C":0}
turnos = {"M":0, "V":0, "N":0}
andares = {"1":0, "2":0, "3":0, "4":0}


while (True):
    elevador = validar("Informe o elevador mais utilizado: (A, B, C)", elevadores.keys())
    elevadores[elevador] += 1;
    
    turno = validar("Informe o turno mais utilizado: (M, V, N)", turnos.keys())
    turnos[turno] += 1;
    
    andar = validar("Informe o andar: (1, 2, 3, 4)", andares.keys())
    andares[andar] += 1;
    
    if input("Deseja continuar? (S/N)").upper() != "S":
        break

print("O elevador mais utilizado foi o elevador: ", buscarMaior(elevadores));
print("O turno mais utilizado foi o turno: ", buscarMaior(turnos)); 
print("O andar com mais respondentes: ", buscarMaior(andares)); 

maiorTurno = turnos[buscarMaior(turnos)]
menorTurno = turnos[buscarMenor(turnos)]


diferenca = (menorTurno / maiorTurno) * 100;
print(diferenca)

