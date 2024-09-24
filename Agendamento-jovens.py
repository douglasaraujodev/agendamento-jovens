# agendamento.py

import json
from datetime import datetime

# Função para carregar agendamentos de um arquivo
def carregar_agendamentos():
    try:
        with open('agendamentos.json', 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

# Função para salvar agendamentos em um arquivo
def salvar_agendamentos(agendamentos):
    with open('agendamentos.json', 'w') as arquivo:
        json.dump(agendamentos, arquivo)

# Função para exibir agendamentos
def exibir_agendamentos(agendamentos):
    if agendamentos:
        print("\nAgendamentos:")
        for agendamento in agendamentos:
            print(f"{agendamento['nome']} - {agendamento['idade']} anos - {agendamento['data_exame']}")
    else:
        print("\nNenhum agendamento encontrado.")

# Função principal
def main():
    agendamentos = carregar_agendamentos()

    while True:
        print("\n--- Sistema de Agendamento de Exames de Vista ---")
        print("1. Agendar exame")
        print("2. Ver agendamentos")
        print("3. Sair")
        
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            nome = input("Digite seu nome: ")
            idade = input("Digite sua idade: ")
            data_exame = input("Digite a data do exame (YYYY-MM-DD): ")

            # Validação simples da data
            try:
                datetime.strptime(data_exame, "%Y-%m-%d")
                agendamentos.append({
                    'nome': nome,
                    'idade': idade,
                    'data_exame': data_exame
                })
                salvar_agendamentos(agendamentos)
                print("Exame agendado com sucesso!")
            except ValueError:
                print("Data inválida. Por favor, use o formato YYYY-MM-DD.")

        elif escolha == '2':
            exibir_agendamentos(agendamentos)

        elif escolha == '3':
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
