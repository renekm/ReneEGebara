3# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 08:58:03 2016

@author: Rene Martinez
"""
import numpy as np 


class Jogo:
    
        
    def __init__(self):
        self.M = [[1,2,3], [4,5,6], [7,8,9]]
        self.jogadas=0
    
   
        
    def recebe_jogada (self, linha, coluna):
        print("wweee")
        if self.jogadas %2 == 0:
            self.M[linha][coluna] == "O"
            self.jogadas += 1
        else:
            self.M[linha][coluna] == "X"
            self.jogadas += 1

        
    def verifica_ganhador(self):
        if self.jogadas >= 4:
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
        elif self.jogadas == 9:
            return 0
                
        else:
            return -1
    
    def limpa_jogadas(verifica_ganhador):
        a = verifica_ganhador()
        if a == 1 or a == 2 or a == 0:
            return Jogo



                
                
            
            
        
        
        