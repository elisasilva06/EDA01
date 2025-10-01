import matplotlib.pyplot as plt
import networkx as nx

# === pede o arquivo ao usuário ===
nome_arquivo = input("Digite o nome do arquivo .txt: ").strip()

# === lê o arquivo ===
with open(nome_arquivo, "r") as f:
    linhas = f.readlines()

print("\n=== Conteúdo do arquivo escolhido ===")
for linha in linhas:
    print(linha.strip())
print("=====================================")

# === cria a lista de adjacência ===
adj = {}
for linha in linhas[1:]:  # pula a primeira linha (ND)
    v1, v2 = linha.strip().split()
    if v1 not in adj:
        adj[v1] = []
    if v2 not in adj:
        adj[v2] = []
    adj[v1].append(v2)
    adj[v2].append(v1)

# === mostra lista de adjacência ===
print("\nLista de Adjacência:")
for v in adj:
    print(v, "->", adj[v])

# === lista arestas (sem duplicar) ===
arestas = []
for v in adj:
    for u in adj[v]:
        if (u, v) not in arestas:
            arestas.append((v, u))

print("\nArestas do grafo:", arestas)

# === graus dos vértices ===
print("\nGraus dos vértices:")
for v in adj:
    print(v, "-> grau =", len(adj[v]))

# === verifica bipartição ===
cor = {}
bipartido = True
for vertice in adj:
    if vertice not in cor:
        cor[vertice] = 0
        fila = [vertice]

        while len(fila) > 0:
            atual = fila.pop(0)
            for vizinho in adj[atual]:
                if vizinho not in cor:
                    cor[vizinho] = 1 - cor[atual]
                    fila.append(vizinho)
                elif cor[vizinho] == cor[atual]:
                    bipartido = False

grupo1 = []
grupo2 = []
if bipartido:
    for v in cor:
        if cor[v] == 0:
            grupo1.append(v)
        else:
            grupo2.append(v)

# === mostra resultado da bipartição ===
if bipartido:
    print("\nO grafo É bipartido!")
    print("Bloco 1:", grupo1)
    print("Bloco 2:", grupo2)
else:
    print("\nO grafo NÃO é bipartido.")

# === visualização com networkx ===
G = nx.Graph()
for v in adj:
    for u in adj[v]:
        G.add_edge(v, u)

cores = []
for no in G.nodes():
    if bipartido and no in grupo1:
        cores.append("lightblue")
    elif bipartido and no in grupo2:
        cores.append("lightcoral")
    else:
        cores.append("lightgray")

nx.draw(G, with_labels=True, node_color=cores)
plt.title("Visualização do Grafo")
plt.show()
