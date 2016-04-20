
import tkinter as tk

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


		    
		



	def iniciar(self):
		self.window.mainloop()





tabuleiro=Tabuleiro()
tabuleiro.iniciar()





