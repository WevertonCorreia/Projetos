import sqlite3
import csv

def verificar_registros_e_gerar_csv():
    conn = sqlite3.connect("registros.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Registros")
    registros = cursor.fetchall()
    conn.close()
    
    if registros:
        print("Registros:")
        for registro in registros:
            print("ID:", registro[0], "- Tipo:", registro[1], "- Hora:", registro[2])

        registros_dia_30 = [registro for registro in registros if registro[2].startswith('30')]
        registros_dia_31 = [registro for registro in registros if registro[2].startswith('31')]
        
        if registros_dia_30:
            with open('registros_dia_30.csv', 'w', newline='') as arquivo_csv:
                escritor_csv = csv.writer(arquivo_csv)
                escritor_csv.writerow(['ID', 'Tipo', 'Hora'])
                escritor_csv.writerows(registros_dia_30)
            print("Arquivo CSV para o dia 30 gerado com sucesso!")
        
        if registros_dia_31:
            with open('registros_dia_31.csv', 'w', newline='') as arquivo_csv:
                escritor_csv = csv.writer(arquivo_csv)
                escritor_csv.writerow(['ID', 'Tipo', 'Hora'])
                escritor_csv.writerows(registros_dia_31)
            print("Arquivo CSV para o dia 31 gerado com sucesso!")
        
        if not registros_dia_30 and not registros_dia_31:
            print("Não há registros para os dias 30 ou 31.")
    else:
        print("Não há registros disponíveis.")

if __name__ == "__main__":
    verificar_registros_e_gerar_csv()