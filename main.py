import matplotlib.pyplot as plt
import networkx as nx

def ler_arquivo():
    nome = input("Digite o nome do arquivo .txt: ").strip()
    with open(nome, "r") as arquivo:
        conteudo = arquivo.readlines()
    return conteudo

def criar_lista_adjacencia(linhas):
    lista = {}
    for linha in linhas[1:]:
        a, b = linha.strip().split()
        if a not in lista:
            lista[a] = []
        if b not in lista:
            lista[b] = []
        lista[a].append(b)
        lista[b].append(a)
    return lista

def mostrar_vizinhos(lista_adj):
    print("\nVizinhos de cada vértice:")
    for vertice in lista_adj:
        print(f"{vertice}: {', '.join(lista_adj[vertice])}")

def mostrar_graus(lista_adj):
    print("\nGraus dos vértices:")
    for vertice in lista_adj:
        grau = len(lista_adj[vertice])
        print(f"{vertice}: grau = {grau}")

def listar_arestas(lista_adj):
    arestas = []
    for v in lista_adj:
        for u in lista_adj[v]:
            if (u, v) not in arestas:
                arestas.append((v, u))
    return arestas

def verificar_bipartido(lista_adj):
    cor = {}
    fila = []
    eh_bipartido = True

    for vertice in lista_adj:
        if vertice not in cor:
            cor[vertice] = 0
            fila.append(vertice)

            while fila:
                atual = fila.pop(0)
                for vizinho in lista_adj[atual]:
                    if vizinho not in cor:
                        cor[vizinho] = 1 - cor[atual]
                        fila.append(vizinho)
                    elif cor[vizinho] == cor[atual]:
                        eh_bipartido = False

    grupo1 = [v for v in cor if cor[v] == 0]
    grupo2 = [v for v in cor if cor[v] == 1]

    return eh_bipartido, grupo1, grupo2

def desenhar_grafo(lista_adj, bipartido, grupo1, grupo2):
    grafo = nx.Graph()

    for v in lista_adj:
        for u in lista_adj[v]:
            grafo.add_edge(v, u)

    cores = []
    for no in grafo.nodes():
        if bipartido and no in grupo1:
            cores.append("lightblue")
        elif bipartido and no in grupo2:
            cores.append("lightcoral")
        else:
            cores.append("lightgray")

    nx.draw(grafo, with_labels=True, node_color=cores)
    plt.title("Visualização do Grafo")
    plt.show()

linhas = ler_arquivo()

print("\n=== Conteúdo do arquivo ===")
for linha in linhas:
    print(linha.strip())
print("============================")

adjacencia = criar_lista_adjacencia(linhas)

print("\nLista de Adjacência:")
for v in adjacencia:
    print(f"{v} -> {adjacencia[v]}")

mostrar_vizinhos(adjacencia)

arestas = listar_arestas(adjacencia)
print("\nArestas do grafo:")
print(arestas)

mostrar_graus(adjacencia)

bipartido, grupo1, grupo2 = verificar_bipartido(adjacencia)

if bipartido:
    print("\nO grafo É bipartido!")
    print("Bloco 1:", grupo1)
    print("Bloco 2:", grupo2)
else:
    print("\nO grafo NÃO é bipartido.")

desenhar_grafo(adjacencia, bipartido, grupo1, grupo2)
