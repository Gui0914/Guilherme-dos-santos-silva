from tkinter import messagebox
import tkinter as tk

def exibir_vencedor(jogador):
    messagebox.showinfo("Fim de jogo", f"O jogador {jogador} venceu!")

def exibir_empate():
    messagebox.showinfo("Fim de jogo", "O jogo terminou em empate!")

def verificar_vitoria(jogador):
    for linha in range(3):
        if (tabuleiro[linha][0] == tabuleiro[linha][1] == tabuleiro[linha][2] == jogador) or \
           (tabuleiro[0][linha] == tabuleiro[1][linha] == tabuleiro[2][linha] == jogador):
            return True

    if (tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador) or \
       (tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador):
        return True

    return False

def clicar_celula(linha, coluna):
    global jogador_atual

    if tabuleiro[linha][coluna] == " ":
        tabuleiro[linha][coluna] = jogador_atual
        celulas[linha][coluna].config(text=jogador_atual)
        
        if verificar_vitoria(jogador_atual):
            exibir_vencedor(jogador_atual)
            janela.quit()
        elif numero_jogadas == 8:
            exibir_empate()
            janela.quit()
        
        jogador_atual = "O" if jogador_atual == "X" else "X"

janela = tk.Tk()
janela.title("Jogo da Velha")

tabuleiro = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

celulas = []

for linha in range(3):
    celula_linha = []
    for coluna in range(3):
        celula = tk.Button(janela, text=" ", font=("Arial", 20), width=6, height=3,
                           command=lambda linha=linha, coluna=coluna: clicar_celula(linha, coluna))
        celula.grid(row=linha, column=coluna)
        celula_linha.append(celula)
    celulas.append(celula_linha)

jogador_atual = "X"
numero_jogadas = 0

janela.mainloop()
