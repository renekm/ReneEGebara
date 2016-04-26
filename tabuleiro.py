
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 15:02:09 2016

@author: Rene Martinez
"""

import tkinter as tk
import ep3 

import tkinter.messagebox

class Tabuleiro: 

    def __init__(self):
            
        self.jogo=ep3.Jogo()

        self.proximoJogador = "O"

        self.window=tk.Tk()
        self.window.title("Jogo da Velha")
        self.window.configure(width=400, height=400)

        self.botao1=tk.Button(self.window)
        self.botao1.configure(height=15,width=30, command=self.muda_tabuleiro1)
        self.botao1.grid(row=0, column=0)
        
		
        self.botao2=tk.Button(self.window)
        self.botao2.configure(height=15,width=30, command=self.muda_tabuleiro2)
        self.botao2.grid(row=0, column=1)
        

        self.botao3=tk.Button(self.window)
        self.botao3.configure(height=15,width=30, command=self.muda_tabuleiro3)
        self.botao3.grid(row=0, column=2)
        

        self.botao4=tk.Button(self.window)
        self.botao4.configure(height=15,width=30, command=self.muda_tabuleiro4)
        self.botao4.grid(row=1, column=0)
        

        self.botao5=tk.Button(self.window)
        self.botao5.configure(height=15,width=30, command=self.muda_tabuleiro5)
        self.botao5.grid(row=1, column=1)
        

        self.botao6=tk.Button(self.window)
        self.botao6.configure(height=15,width=30, command=self.muda_tabuleiro6)
        self.botao6.grid(row=1, column=2)
         

        self.botao7=tk.Button(self.window)
        self.botao7.configure(height=15,width=30, command=self.muda_tabuleiro7)
        self.botao7.grid(row=2, column=0)
        

        self.botao8=tk.Button(self.window)
        self.botao8.configure(height=15,width=30, command=self.muda_tabuleiro8)
        self.botao8.grid(row=2, column=1)
        

        self.botao9=tk.Button(self.window)
        self.botao9.configure(height=15,width=30, command=self.muda_tabuleiro9)
        self.botao9.grid(row=2, column=2)
        


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
        
        a = self.jogo.verifica_ganhador()
        if a == 0:
            tkinter.messagebox.showinfo("Jogadores", "Deu velha!")
        elif a == 1:
            tkinter.messagebox.showinfo("Jogador X", "Parabéns, você é o ganhador")
        elif a == 2:
            tkinter.messagebox.showinfo("Jogador O" , "Parabéns, você é o ganhador")
        if a == 1 or a == 2 or a == 0:
            self.jogo.limpa_jogadas()

    def muda_tabuleiro2(self):
        if self.proximoJogador == "X":
            self.botao2.configure(text="X")
            self.proximoJogador = "O"
        else:
            self.botao2.configure(text="O")
            self.proximoJogador = "X"

        self.jogo.recebe_jogada(0,1)
        
        a = self.jogo.verifica_ganhador()
        if a == 0:
            tkinter.messagebox.showinfo("Jogadores", "Deu velha!")
        elif a == 1:
            tkinter.messagebox.showinfo("Jogador X", "Parabéns, você é o ganhador")
        elif a == 2:
            tkinter.messagebox.showinfo("Jogador O" , "Parabéns, você é o ganhador")
        if a == 1 or a == 2 or a == 0:
            self.jogo.limpa_jogadas()
        
    def muda_tabuleiro3(self):
        if self.proximoJogador == "X":
            self.botao3.configure(text="X")
            self.proximoJogador = "O"
        else:
            self.botao3.configure(text="O")
            self.proximoJogador = "X"

        self.jogo.recebe_jogada(0,2)
        
        a = self.jogo.verifica_ganhador()
        if a == 0:
            tkinter.messagebox.showinfo("Jogadores", "Deu velha!")
        elif a == 1:
            tkinter.messagebox.showinfo("Jogador X", "Parabéns, você é o ganhador")
        elif a == 2:
            tkinter.messagebox.showinfo("Jogador O" , "Parabéns, você é o ganhador")
        if a == 1 or a == 2 or a == 0:
            self.jogo.limpa_jogadas()
        
    def muda_tabuleiro4(self):
        if self.proximoJogador == "X":
            self.botao4.configure(text="X")
            self.proximoJogador = "O"
        else:
            self.botao4.configure(text="O")
            self.proximoJogador = "X"

        self.jogo.recebe_jogada(1,0)
        
        a = self.jogo.verifica_ganhador()
        if a == 0:
            tkinter.messagebox.showinfo("Jogadores", "Deu velha!")
        elif a == 1:
            tkinter.messagebox.showinfo("Jogador X", "Parabéns, você é o ganhador")
        elif a == 2:
            tkinter.messagebox.showinfo("Jogador O" , "Parabéns, você é o ganhador")
        if a == 1 or a == 2 or a == 0:
            self.jogo.limpa_jogadas()
        
    def muda_tabuleiro5(self):
        if self.proximoJogador == "X":
            self.botao5.configure(text="X")
            self.proximoJogador = "O"
        else:
            self.botao5.configure(text="O")
            self.proximoJogador = "X"

        self.jogo.recebe_jogada(1,1)
        
        a = self.jogo.verifica_ganhador()
        if a == 0:
            tkinter.messagebox.showinfo("Jogadores", "Deu velha!")
        elif a == 1:
            tkinter.messagebox.showinfo("Jogador X", "Parabéns, você é o ganhador")
        elif a == 2:
            tkinter.messagebox.showinfo("Jogador O" , "Parabéns, você é o ganhador")
        if a == 1 or a == 2 or a == 0:
            self.jogo.limpa_jogadas()
        

    def muda_tabuleiro6(self):
        if self.proximoJogador == "X":
            self.botao6.configure(text="X")
            self.proximoJogador = "O"
        else:
            self.botao6.configure(text="O")
            self.proximoJogador = "X"

        self.jogo.recebe_jogada(1,2)
        
        a = self.jogo.verifica_ganhador()
        if a == 0:
            tkinter.messagebox.showinfo("Jogadores", "Deu velha!")
        elif a == 1:
            tkinter.messagebox.showinfo("Jogador X", "Parabéns, você é o ganhador")
        elif a == 2:
            tkinter.messagebox.showinfo("Jogador O" , "Parabéns, você é o ganhador")
        if a == 1 or a == 2 or a == 0:
            self.jogo.limpa_jogadas()


    def muda_tabuleiro7(self):
        if self.proximoJogador == "X":
            self.botao7.configure(text="X")
            self.proximoJogador = "O"
        else:
            self.botao7.configure(text="O")
            self.proximoJogador = "X"

        self.jogo.recebe_jogada(2,0)
        
        a = self.jogo.verifica_ganhador()
        if a == 0:
            tkinter.messagebox.showinfo("Jogadores", "Deu velha!")
        elif a == 1:
            tkinter.messagebox.showinfo("Jogador X", "Parabéns, você é o ganhador")
        elif a == 2:
            tkinter.messagebox.showinfo("Jogador O" , "Parabéns, você é o ganhador")
        if a == 1 or a == 2 or a == 0:
            self.jogo.limpa_jogadas()
        
    def muda_tabuleiro8(self):
        if self.proximoJogador == "X":
            self.botao8.configure(text="X")
            self.proximoJogador = "O"
        else:
            self.botao8.configure(text="O")
            self.proximoJogador = "X"

        self.jogo.recebe_jogada(2,1)
        
        a = self.jogo.verifica_ganhador()
        if a == 0:
            tkinter.messagebox.showinfo("Jogadores", "Deu velha!")
        elif a == 1:
            tkinter.messagebox.showinfo("Jogador X", "Parabéns, você é o ganhador")
        elif a == 2:
            tkinter.messagebox.showinfo("Jogador O" , "Parabéns, você é o ganhador")
        if a == 1 or a == 2 or a == 0:
            self.jogo.limpa_jogadas()

    def muda_tabuleiro9(self):
        if self.proximoJogador == "X":
            self.botao9.configure(text="X")
            self.proximoJogador = "O"
        else:
            self.botao9.configure(text="O")
            self.proximoJogador = "X"

        self.jogo.recebe_jogada(2,2)    
        
        a = self.jogo.verifica_ganhador()
        if a == 0:
            tkinter.messagebox.showinfo("Jogadores", "Deu velha!")
        elif a == 1:
            tkinter.messagebox.showinfo("Jogador X", "Parabéns, você é o ganhador")
        elif a == 2:
            tkinter.messagebox.showinfo("Jogador O" , "Parabéns, você é o ganhador")
        if a == 1 or a == 2 or a == 0:
            
            self.jogo.limpa_jogadas()

    
