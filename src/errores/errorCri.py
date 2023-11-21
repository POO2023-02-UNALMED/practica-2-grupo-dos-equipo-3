from tkinter import *
from errorApli import ErrorAplicacion

class ErrorCritico(ErrorAplicacion):
    def __init__(self, err=""):
        super().__init__("Detectado Error Critico: " + err)
    def display(self):
        print(self.args[0])
        
