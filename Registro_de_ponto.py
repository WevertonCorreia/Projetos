import sqlite3
import datetime

def criar_tabela():
    conn = sqlite3.connect("registros.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Registros (
                        id INTEGER PRIMARY KEY,
                        tipo TEXT NOT NULL,
                        hora TEXT NOT NULL
                    )''')
    conn.commit()
    conn.close()

def registrar_horario(tipo):
    agora = datetime.datetime.now()
    hora_formatada = agora.strftime("%H:%M")
    
    conn = sqlite3.connect("registros.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Registros (tipo, hora) VALUES (?, ?)", (tipo, hora_formatada))
    conn.commit()
    conn.close()
    print(f"Horário de {tipo} registrado com sucesso às {hora_formatada}.")

def main():
    criar_tabela()
    
    print("1. Registrar entrada na empresa")
    print("2. Registrar hora do almoço")
    print("3. Registrar retorno do almoço")
    print("4. Registrar saída da empresa")
    opcao = input("Selecione uma opção (1/2/3/4): ")
    
    if opcao == "1":
        registrar_horario("entrada")
    elif opcao == "2":
        registrar_horario("almoço")
    elif opcao == "3":
        registrar_horario("retorno do almoço")
    elif opcao == "4":
        registrar_horario("saída")
    else:
        print("Opção inválida.")

if __name__ == "__main__":
    main()
