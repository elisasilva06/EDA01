- Projeto – Teoria dos Grafos
- Alunas : Ana Elisa Oliveira Silva e Samyra de Araujo Lobo Silva
- Tema C: Agendador de Processos Concorrentes
- Estrutura de Dados: Lista de Adjacência
- Linguagem: Python (Google Colab)

🎯 Objetivo

O projeto tem como objetivo verificar se é possível agendar processos concorrentes em dois blocos de tempo diferentes, garantindo que processos incompatíveis não rodem juntos.
Para isso, foi utilizada a 2-coloração de grafos, que identifica se o grafo é bipartido.

* Estrutura do Projeto

main.py → código principal do programa

processos_simples.txt → exemplo de grafo com agendamento possível

processos_medio.txt → exemplo intermediário

processos_impossivel.txt → exemplo onde o agendamento é impossível


* Como Compilar e Executar o Projeto 
- Execução no Google Colab (recomendado)

O Google Colab já possui o Python e as bibliotecas necessárias instaladas, então não é preciso configurar nada.
Siga os passos abaixo:

- Acesse o site: https://colab.research.google.com
 
Crie um novo notebook.

- Faça upload dos seguintes arquivos no painel lateral do Colab:

main.py

processos_simples.txt

processos_medio.txt

processos_impossivel.txt

- Em uma célula, digite:

!python main.py


Quando o programa pedir, digite o nome de um dos arquivos de entrada (por exemplo processos_simples.txt).

O programa mostrará o resultado no console e exibirá o gráfico colorido do grafo


- Execução com Arquivo Executável (Windows 10/11)

Também é possível executar o projeto por meio de um arquivo executável, sem precisar instalar o Python ou bibliotecas adicionais.

O executável foi criado a partir do código principal, porém:

o arquivo de entrada já está definido dentro do código (não é necessário digitar o nome durante a execução);

e a parte do desenho do grafo foi removida, pois a biblioteca gráfica não foi compatível com a compilação.