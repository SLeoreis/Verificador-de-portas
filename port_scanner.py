import socket # importando a biblioteca
from datetime import datetime

ip = input("Digite o IP: ") # entrada para IP, 
t1 = datetime.now()


for porta in range(1,65535):
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET (representa o tipo de endereço), SOCK_STREAM (indica que socket é do tipo TCP)
    cliente.settimeout(2) # limite de tempo suportado
    conexao = cliente.connect_ex((ip, porta)) 
    
  # condição (se conexão for igual a 0 porta aberta se não porta fechada)
    with open("teste.txt", 'a') as f: # inserir caminho onde será salvo o arquivo
        if conexao == 0:
            f.write(str(porta) + " ," + " >> porta aberta")
            f.writelines('\n') # pula a linha
            print(str(porta) +  " >> porta aberta") 

t2 = datetime.now() #tempo quando a varredura acabou
total = t2-t1
print("tempo total de varredura: ",total)
            