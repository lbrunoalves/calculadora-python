from tkinter import *

def  limparDisplay() -> None:
    display.delete(0, END)

def inserir(valor: str) -> None:
    display.insert(END, valor)

def calcularResultado() -> None:
    textoDisplay = display.get()
    resultado = eval(textoDisplay)
    limparDisplay()
    inserir(resultado)

janela = Tk()
janela.title("Calculadora")
display = Entry(janela, bg="black", font="Tahoma 24", width=20, fg="white")
display.pack()

frame = Frame(janela)
frame.pack()

gray = "#333333"
orange = "#ff9500"

btn0 = Button(frame, text="0", bg=gray, fg="white", font="Tahoma 16 bold",
              height=3, width=6, command=lambda: inserir("0"))
btn1 = Button(frame, text="1", bg=gray, fg="white", font="Tahoma 16 bold",
              height=3, width=6, command=lambda: inserir("1"))
btn2 = Button(frame, text="2", bg=gray, fg="white", font="Tahoma 16 bold",
              height=3, width=6, command=lambda: inserir("2"))
btn3 = Button(frame, text="3", bg=gray, fg="white", font="Tahoma 16 bold",
              height=3, width=6, command=lambda: inserir("3"))
btn4 = Button(frame, text="4", bg=gray, fg="white", font="Tahoma 16 bold",
              height=3, width=6, command=lambda: inserir("4"))
btn5 = Button(frame, text="5", bg=gray, fg="white", font="Tahoma 16 bold",
              height=3, width=6, command=lambda: inserir("5"))
btn6 = Button(frame, text="6", bg=gray, fg="white", font="Tahoma 16 bold",
              height=3, width=6, command=lambda: inserir("6"))
btn7 = Button(frame, text="7", bg=gray, fg="white", font="Tahoma 16 bold",
              height=3, width=6, command=lambda: inserir("7"))
btn8 = Button(frame, text="8", bg=gray, fg="white", font="Tahoma 16 bold",
              height=3, width=6, command=lambda: inserir("8"))
btn9 = Button(frame, text="9", bg=gray, fg="white", font="Tahoma 16 bold",
              height=3, width=6, command=lambda: inserir("9"))
btnSomar = Button(frame, text="+", bg=orange, fg="white", font="Tahoma 16 bold",
              height=3, width=6, command=lambda: inserir("+"))
btnSubtrair = Button(frame, text="-", bg=orange, fg="white", font="Tahoma 16 bold",
              height=3, width=6, command=lambda: inserir("-"))
btnMultiplicar = Button(frame, text="*", bg=orange, fg="white", font="Tahoma 16 bold",
              height=3, width=6, command=lambda: inserir("*"))
btn0Dividir = Button(frame, text="/", bg=orange, fg="white", font="Tahoma 16 bold",
              height=3, width=6, command=lambda: inserir("/"))
btnLimpar = Button(frame, text="C", bg=orange, fg="white", font="Tahoma 16 bold",
              height=3, width=6, command=limparDisplay)
btnPonto = Button(frame, text=".", bg=orange, fg="white", font="Tahoma 16 bold",
              height=3, width=6)
btnIgual = Button(frame, text="=", bg=orange, fg="white", font="Tahoma 16 bold",
              height=3, width=6, command=calcularResultado)

btn7.grid(row=0, column=0)
btn8.grid(row=0, column=1)
btn9.grid(row=0, column=2)
btnSomar.grid(row=0, column=3)

btn4.grid(row=1, column=0)
btn5.grid(row=1, column=1)
btn6.grid(row=1, column=2)
btnSubtrair.grid(row=1, column=3)

btn1.grid(row=2, column=0)
btn2.grid(row=2, column=1)
btn3.grid(row=2, column=2)
btnMultiplicar.grid(row=2, column=3)

btnIgual.grid(row=3, column=0)
btn0.grid(row=3, column=1)
btnLimpar.grid(row=3, column=2)
btn0Dividir.grid(row=3, column=3)



janela.mainloop()