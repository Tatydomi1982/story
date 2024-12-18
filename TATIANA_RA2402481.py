import numpy as np
import matplotlib.pyplot as plt

# Função para criar e salvar o gráfico
def gerar_grafico(nome, ra, filename):
    # Dados
    X = np.linspace(0.2, 8, 170)  # Intervalo de X de 0.2 a 8 com 170 pontos
    Y1 = 5.6 + np.cos(X)  # Função Y1
    Y2 = 2.8 + np.cos(2.8 + X / 0.5) / 2  # Função Y2
    Y3 = np.random.uniform(Y1, Y2, len(X))  # Função aleatória entre Y1 e Y2

    # Gráfico
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(X, Y1, label=f'Limite Superior+{ra}', color='blue', linestyle='-', linewidth=2)
    ax.plot(X, Y2, label=f'Limite Inferior+{ra}', color='red', linestyle='--', linewidth=2)
    ax.plot(X, Y3, label='Função Aleatória', color='green', linestyle='-.', marker='s', markersize=4)

    # Círculo e etiqueta
    ax.scatter(2.0, 2.0, color='black', s=100, label=f'Ponto RA ({ra})')
    ax.text(2.05, 2.0, ra, fontsize=10, verticalalignment='center', color='black')

    # Configuração dos eixos
    ax.set_xlim(0, 6)
    ax.set_ylim(0, 6)
    ax.set_xticks(np.arange(0, 6.2, 0.2))
    ax.set_yticks(np.arange(0, 6.2, 0.2))
    ax.set_xlabel("X", fontsize=12)
    ax.set_ylabel("Y", fontsize=12)
    ax.set_title(f"{nome} - RA{ra}", fontsize=14)

    # Grid e legenda
    ax.grid(True, which='both', linestyle='--', linewidth=0.5)
    ax.minorticks_on()
    ax.legend()

    # Salvar o arquivo
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

gerar_grafico("Tatiana Araújo Domingos", "2402481", "grafico_RA2402481.png")

print("Gráficos gerados e salvos individualmente.")