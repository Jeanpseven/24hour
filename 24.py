import time
import getpass
import json
from cryptography.fernet import Fernet

# Função para criptografar a senha
def criptografar_senha(senha, chave):
    f = Fernet(chave)
    senha_criptografada = f.encrypt(senha.encode())
    return senha_criptografada

# Função para descriptografar a senha
def descriptografar_senha(senha_criptografada, chave):
    f = Fernet(chave)
    senha = f.decrypt(senha_criptografada).decode()
    return senha

# Função para executar o código fornecido pelo usuário
def executar_codigo(codigo):
    # Executar o código fornecido pelo usuário
    print("Executando o código fornecido pelo usuário...")
    try:
        exec(codigo)
        print("Código executado com sucesso!")
    except Exception as e:
        print(f"Erro ao executar o código: {str(e)}")

# Função para reiniciar o timer de 24 horas com uma confirmação de senha
def reiniciar_timer(senha_correta):
    senha = getpass.getpass("Digite a senha para reiniciar o timer: ")
    confirmacao_senha = getpass.getpass("Confirme a senha: ")

    if senha == confirmacao_senha and senha == senha_correta:
        print("Timer reiniciado com sucesso.")
        return True
    else:
        print("Senha incorreta ou as senhas não correspondem. Timer não reiniciado.")
        return False

# Obter a senha correta
senha_correta = getpass.getpass("Digite a senha correta: ")

# Gerar uma chave de criptografia
chave = Fernet.generate_key()

# Criptografar a senha correta
senha_criptografada = criptografar_senha(senha_correta, chave)

# Salvar a senha criptografada e a chave em um arquivo JSON
dados = {
    'senha_criptografada': senha_criptografada.decode(),
    'chave': chave.decode()
}
with open('senha.json', 'w') as file:
    json.dump(dados, file)

print("Senha criptografada e chave salvas com sucesso!")

# Loop principal do programa
while True:
    print("----- Timer de Execução de Código -----")
    print("Tempo restante até a próxima execução: 24 horas")
    print("1. Executar código digitado")
    print("2. Executar código de um arquivo")
    print("3. Reiniciar timer")
    print("0. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        codigo = input("Digite o código que deseja executar:\n")
        executar_codigo(codigo)

    elif escolha == "2":
        arquivo = input("Digite o caminho do arquivo que contém o código:\n")
        try:
            with open(arquivo, "r") as file:
                codigo = file.read()
                executar_codigo(codigo)
        except Exception as e:
            print(f"Erro ao ler o arquivo: {str(e)}")

    elif escolha == "3":
        reiniciado = reiniciar_timer(senha_correta)
        if reiniciado:
            continue

    elif escolha == "0":
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")

    # Aguardar 24 horas antes da próxima execução
    print("Aguardando 24 horas até a próxima execução...")
    time.sleep(24 * 60 * 60)

print("Encerrando o programa...")
