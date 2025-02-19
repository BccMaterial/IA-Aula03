from classes import FilaPrioridade, Tabuleiro, Visitados

def dijkstra(problema):
    no = problema.iniciar()
    fila = FilaPrioridade()
    fila.push(0, no)
    visitados = Visitados()
    visitados.adicionar(no)

    while not fila.esta_vazio():
        no = fila.pop()
        visitados.adicionar(no)

        # faz o teste objetivo. Se chegou no resultado final
        # retorna o No correspondente
        resultado = problema.testar_objetivo(no)
        if (resultado):
            return (visitados.tamanho(), no)

        # função sucessores define os Nós sucessores
        nos_sucessores = problema.gerar_sucessores(no)

        # para cada sucessor, se armazena se ainda não visitado
        for no_sucessor in nos_sucessores:
            # pula estado_filho se já foi expandido
            if not visitados.foi_visitado(no_sucessor):
                fila.push(no_sucessor.custo, no_sucessor)

    return (visitados.tamanho(), None)


def a_estrela(problema):
    no = problema.iniciar()

    fila = FilaPrioridade()
    fila.push(0, no)

    visitados = Visitados()
    visitados.adicionar(no)

    while not fila.esta_vazio():
        no = fila.pop()
        visitados.adicionar(no)

        # faz o teste objetivo. Se chegou no resultado final
        # retorna o No correspondente
        resultado = problema.testar_objetivo(no)
        if (resultado):
            return (visitados.tamanho(), no)

        # função sucessores define os Nós sucessores
        nos_sucessores = problema.gerar_sucessores(no)

        # para cada sucessor, se armazena se ainda não visitado
        for no_sucessor in nos_sucessores:
            # pula estado_filho se já foi expandido
            if not visitados.foi_visitado(no_sucessor):
                no_sucessor.custo = no.custo + problema.custo(no, no_sucessor)
                no_sucessor.heuristica = problema.heuristica(no_sucessor)
                a_estrela_n = (no_sucessor.custo + no_sucessor.heuristica)

                fila.push(a_estrela_n, no_sucessor)

    return (visitados.tamanho(), None)

def no_caminho(no):
  caminho = []
  while no.no_pai is not None:
    caminho.append(no.estado)
    no = no.no_pai
  caminho.reverse()  # Inverte a ordem para que ela retorne uma lista do primeiro nó do Array até o ultimo
  return caminho

problema= Tabuleiro()
print("Solução com Dijkstra:")
total, sol = dijkstra(problema)
if sol:
  print(no_caminho(sol))
print("Quantidade de estados visitados: ", total)

print("\n")
total, sol = a_estrela(problema)
if sol:
  print("Solução com A estrela: ", no_caminho(sol))
print("Quantidade de estados visitados: ", total)

