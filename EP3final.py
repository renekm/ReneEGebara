import tkinter as tk
import numpy as np 
 
class Jogo:

    jogadas = 0
    while jogadas < 10:
        jogadas += 1
        
        def __init__(self,jogadas):
            self.M = np.array([[1,2,3], [4,5,6], [7,8,9]])
            self.jogadas = jogadas
        
        def recebe_jogada (self, linha, coluna):
            if self.jogadas %2 == 0:
                self.M[linha][coluna] == "O"
            else:
                self.M[linha][coluna] == "X"
            self.jogadas = 1
        
        def verifica_ganhador(self):
            if self.jogadas > 4:
                if self.M[0][0] == "X" and self.M[0][1] == "X" and self.M[0][2] == "X":
                    return 1 
                elif self.M[1][0] == "X" and self.M[1][1] == "X" and self.M[1][2] == "X":
                    return 1
                elif self.M[2][0] == "X" and self.M[2][1] == "X" and self.M[2][2] == "X":
                    return 1
                elif self.M[0][0] == "X" and self.M[1][1] == "X" and self.M[2][2] == "X":
                    return 1
                elif self.M[0][2] == "X" and self.M[1][1] == "X" and self.M[2][0] == "X":
                    return 1
                elif self.M[0][0] == "O" and self.M[0][1] == "O" and self.M[0][2] == "O":
                    return 2
                elif self.M[1][0] == "O" and self.M[1][1] == "O" and self.M[1][2] == "O":
                    return 2
                elif self.M[2][0] == "O" and self.M[2][1] == "O" and self.M[2][2] == "O":
                    return 2
                elif self.M[0][0] == "O" and self.M[1][1] == "O" and self.M[2][2] == "O":
                    return 2
                elif self.M[0][2] == "O" and self.M[1][1] == "O" and self.M[2][0] == "O":
                    return 2
            if self.jogadas == 9:
                return 0
                
            else:
                return -1
    
        def limpa_jogadas(verifica_ganhador):
            a = verifica_ganhador()
            if a == 1 or a == 2 or a == 0:
                return Jogo
                

class Tabuleiro: 

    def __init__(self):
        self.window=tk.Tk()
        self.window.title("Jogo da Velha")
        self.window.configure(width=400, height=400)

        botao1=tk.Button(self.window)
        botao1.configure(height=15,width=30)
        botao1.grid(row=0, column=0)
		
        botao2=tk.Button(self.window)
        botao2.configure(height=15,width=30)
        botao2.grid(row=0, column=1)

        botao3=tk.Button(self.window)
        botao3.configure(height=15,width=30)
        botao3.grid(row=0, column=2)

        botao4=tk.Button(self.window)
        botao4.configure(height=15,width=30)
        botao4.grid(row=1, column=0)

        botao5=tk.Button(self.window)
        botao5.configure(height=15,width=30)
        botao5.grid(row=1, column=1)

        botao6=tk.Button(self.window)
        botao6.configure(height=15,width=30)
        botao6.grid(row=1, column=2) 

        botao7=tk.Button(self.window)
        botao7.configure(height=15,width=30)
        botao7.grid(row=2, column=0)

        botao8=tk.Button(self.window)
        botao8.configure(height=15,width=30)
        botao8.grid(row=2, column=1)

        botao9=tk.Button(self.window)
        botao9.configure(height=15,width=30)
        botao9.grid(row=2, column=2)


        prox_jogada=tk.Label(self.window, text="Próxima jogada: ")
        prox_jogada.grid(row=3,column=0)

    def iniciar(self):  
        self.window.mainloop()

    def prox_jogada(self):
        if self.jogadas %2 == 0:
             prox_jogada == "O"
        else:
            prox_jogada == "X"
        




            
            
        
        



tabuleiro=Tabuleiro()
tabuleiro.iniciar()
jogo = Jogo()
jogo.iniciar()

