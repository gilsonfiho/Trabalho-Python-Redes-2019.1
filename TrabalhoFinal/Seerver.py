import socketserver

X=0
clientes=[]
conexoes=[]

class lidaCliente(socketserver.BaseRequestHandler):

    def handle(self):

        print("Conectado a :", self.client_address)

        while True:

            global X

            if not self.request in conexoes:
                clientes.append(((self.client_address),"Usuario{0}".format(X)))
                conexoes.append(self.request)
                X+=1

            endEmissor = self.client_address
            endDestinatario = None
            emissor = ''

            destinatario = self.request.recv(1024)
            assunto = self.request.recv(1024)
            corpo = self.request.recv(1024)

            for i in range(X):
                if(endEmissor==clientes[i][0]):
                    emissor = clientes[i][1]
                    break

            for i in range(X):
                if(destinatario.decode("utf-8","ignore")==clientes[i][1]):
                    endDestinatario=clientes[i][0]
                    break

            mensagem = "Emissor: "+emissor+"\n"+"Assunto: "+assunto.decode("utf-8","ignore")+"\n"+"Mensagem: "+corpo.decode("utf-8","ignore") #Formatação da mensagem a ser enviada
            mensagem = bytes(mensagem, 'utf-8')
            for sock in conexoes:
                if (endDestinatario==sock.getpeername()):
                    sock.send(mensagem)


#Configuração do servidor
host = '127.0.0.1'
port = 44765
End = (host, port)
server = socketserver.ThreadingTCPServer(End,lidaCliente)
server.serve_forever()