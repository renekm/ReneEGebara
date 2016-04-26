
import tkinter as tk
import ep3 

class Tabuleiro: 

    def __init__(self):
            
        self.jogo=ep3.Jogo()

        self.proximoJogador = "O"

        self.window=tk.Tk()
        self.window.title("Jogo da Velha")
        self.window.configure(width=400, height=400)

        botao1=tk.Button(self.window)
        botao1.configure(height=15,width=30, command=self.muda_tabuleiro1)
        botao1.grid(row=0, column=0)
        
		
        botao2=tk.Button(self.window)
        botao2.configure(height=15,width=30, command=self.muda_tabuleiro2)
        botao2.grid(row=0, column=1)
        

        botao3=tk.Button(self.window)
        botao3.configure(height=15,width=30, command=self.muda_tabuleiro3)
        botao3.grid(row=0, column=2)
        

        botao4=tk.Button(self.window)
        botao4.configure(height=15,width=30, command=self.muda_tabuleiro4)
        botao4.grid(row=1, column=0)
        

        botao5=tk.Button(self.window)
        botao5.configure(height=15,width=30, command=self.muda_tabuleiro5)
        botao5.grid(row=1, column=1)
        

        botao6=tk.Button(self.window)
        botao6.configure(height=15,width=30, command=self.muda_tabuleiro6)
        botao6.grid(row=1, column=2)
         

        botao7=tk.Button(self.window)
        botao7.configure(height=15,width=30, command=self.muda_tabuleiro7)
        botao7.grid(row=2, column=0)
        

        botao8=tk.Button(self.window)
        botao8.configure(height=15,width=30, command=self.muda_tabuleiro8)
        botao8.grid(row=2, column=1)
        

        botao9=tk.Button(self.window)
        botao9.configure(height=15,width=30, command=self.muda_tabuleiro9)
        botao9.grid(row=2, column=2)
        


        prox_jogada=tk.Label(self.window, text="Próxima jogada: ")
        prox_jogada.grid(row=3,column=0)

    def iniciar(self):
        self.window.mainloop()

           
    def muda_tabuleiro1(self):
        if self.proximoJogador == "X":
            self.botao1.configure(text="X")
            self.proximoJogador = "O"
        else:
            self.botao1.configure(text="O")
            self.proximoJogador = "X"

        self.jogo.recebe_jogada(0,0)

    def muda_tabuleiro2(self):
        if self.proximoJogador == "X":
            self.botao2.configure(text="X")
            self.proximoJogador = "O"
        else:
            self.botao2.configure(text="O")
            self.proximoJogador = "X"

        self.jogo.recebe_jogada(0,1)
        
    def muda_tabuleiro3(self):
        if self.proximoJogador == "X":
            self.botao3.configure(text="X")
            self.proximoJogador = "O"
        else:
            self.botao3.configure(text="O")
            self.proximoJogador = "X"

        self.jogo.recebe_jogada(0,2)
        
    def muda_tabuleiro4(self):
        if self.proximoJogador == "X":
            self.botao4.configure(text="X")
            self.proximoJogador = "O"
        else:
            self.botao4.configure(text="O")
            self.proximoJogador = "X"

        self.jogo.recebe_jogada(1,0)
        
    def muda_tabuleiro5(self):
        if self.proximoJogador == "X":
            self.botao5.configure(text="X")
            self.proximoJogador = "O"
        else:
            self.botao5.configure(text="O")
            self.proximoJogador = "X"

        self.jogo.recebe_jogada(1,1)
        

    def muda_tabuleiro6(self):
        if self.proximoJogador == "X":
            self.botao6.configure(text="X")
            self.proximoJogador = "O"
        else:
            self.botao6.configure(text="O")
            self.proximoJogador = "X"

        self.jogo.recebe_jogada(1,2)


    def muda_tabuleiro7(self):
        if self.proximoJogador == "X":
            self.botao7.configure(text="X")
            self.proximoJogador = "O"
        else:
            self.botao7.configure(text="O")
            self.proximoJogador = "X"

        self.jogo.recebe_jogada(2,0)
        
    def muda_tabuleiro8(self):
        if self.proximoJogador == "X":
            self.botao8.configure(text="X")
            self.proximoJogador = "O"
        else:
            self.botao8.configure(text="O")
            self.proximoJogador = "X"

        self.jogo.recebe_jogada(2,1)

    def muda_tabuleiro9(self):
        if self.proximoJogador == "X":
            self.botao9.configure(text="X")
            self.proximoJogador = "O"
        else:
            self.botao9.configure(text="O")
            self.proximoJogador = "X"

        self.jogo.recebe_jogada(2,2)    
                





        


tabuleiro=Tabuleiro()
tabuleiro.iniciar()





