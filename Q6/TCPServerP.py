from socket import *

# Inicia o servidor
serverPort = 12006
serverSocket = socket(AF_INET,SOCK_STREAM) 
serverSocket.bind(('', serverPort)) 
serverSocket.listen(1)

print('Servidor no ar!')
while True:
    connectionSocket, addr = serverSocket.accept()
    print(f"Conectado com: {addr}")
    
    # Espera receber a primeira mensagem do usuário
    connectionSocket.recv(1024)

    # Da as boas vindas
    welcome = "Olá! Qual o seu nome?"
    connectionSocket.send(welcome.encode())

    # Espera receber o nome do usuário
    name = connectionSocket.recv(1024).decode()
    
    # Oferece serviços para o usuário
    services = f"""
    Certo, {name}! Como posso te ajudar?
    Digite o número que corresponde à opção desejada:

    1 - Agendar um horário de monitoria
    2 - Listar as próximas atividades da disciplina
    3 - E-mail do professor
    """
    connectionSocket.send(services.encode())

    # Espera número do serviço
    number = connectionSocket.recv(1024).decode()
    # Responde de acordo com o serviço escolhido
    message = ""
    if number == "1":
        message = "Para agendar uma monitoria, basta enviar um email para cainafigueiredo@poli.ufrj.br"
    elif number == "2":
        message = """
        Fique atento para as datas das próximas atividades. Confira o que vem por aí!

        P1: 26 de Maio de 2022
        Lista 3: 29 de Maio de 2022
        """
    elif number == "3":
        message = """
        Quer falar com o professor?
        O email dele é sadoc@ic.ufrj.br
        """

    # Despede-se do usuario
    goodbye = "\nObrigado por utilizar nossos serviços! Até logo!"
    message = message + goodbye
    connectionSocket.send(message.encode())
    
    # Termina a conexão
    connectionSocket.close()