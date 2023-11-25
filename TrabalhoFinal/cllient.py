import tkinter

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'  # Endereco IP do Servidor
port = 44765  # Porta que o Servidor esta
ADD = (host, port)
client.connect(ADD)
client.settimeout(0.01)
mensagem = ''


def send():
    destinatario = entrada1.get().encode('utf-8')
    client.send(destinatario)

    assunto = entrada2.get().encode('utf-8')
    if (entrada2.get() == ''):
        assunto = 'Sem Assunto'.encode('utf-8')
    client.send(assunto)

    mensagem = entrada3.get().encode('utf-8')
    client.send(mensagem)


def receive():
    global mensagem
    try:
        mensagem += client.recv(1024).decode("utf-8", "ignore") + "\n"
        caixaDeEntrada2['text'] = mensagem
    except:
        pass
    caixaDeEntrada2.after(1000, receive)


def clear():
    global mensagem
    mensagem = ''
    caixaDeEntrada2['text'] = ''


interface = tkinter.Tk()
interface.configure()
interface.title()
interface.geometry()

lable1 = tkinter.Label(interface, text="Destinatario", height=1, width=10, font="arial 12")
lable2 = tkinter.Label(interface, text="Assunto", height=1, width=10, font="arial 12")
lable3 = tkinter.Label(interface, text='Mensagem', height=1, width=10, font='arial 12')
espacoBut = tkinter.Label(interface, text='', height=1, width=1)
caixaDeEntrada = tkinter.Label(interface, text='Caixa De Entrada:', height=2, width=20, font='arial 12')
espacoBut2 = tkinter.Label(interface, text='', height=1, width=1)
espacoBut3 = tkinter.Label(interface, text='', height=1, width=1)
caixaDeEntrada2 = tkinter.Label(interface, text='', height=15, width=50, font='arial 12', bg="gray")
caixaDeEntrada2.after(1000, receive)

lable1.grid(row=1, column=1)
lable2.grid(row=3, column=1)
lable3.grid(row=5, column=1)
espacoBut.grid(row=8, column=1)
espacoBut2.grid(row=10, column=1)
espacoBut3.grid(row=12, column=1)
caixaDeEntrada.grid(row=13, column=1)
caixaDeEntrada2.grid(row=14, column=1)

entrada1 = tkinter.Entry(interface, font='arial 16')
entrada2 = tkinter.Entry(interface, font='arial 16')
entrada3 = tkinter.Entry(interface, font='arial 16')

entrada1.grid(row=2, column=1)
entrada2.grid(row=4, column=1)
entrada3.grid(row=6, column=1)

botao1 = tkinter.Button(interface, text='Send', height=1, width=5, font='arial 16', command=send)
botao1.grid(row=9, column=1)
botaoClear = tkinter.Button(interface, text='Clear', height=1, width=5, font='arial 16', command=clear)
botaoClear.grid(row=11, column=1)

interface.mainloop()