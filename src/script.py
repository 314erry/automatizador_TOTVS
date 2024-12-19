from time import sleep
from unidecode import unidecode
import pyautogui
import os
import keyboard
import threading

interromper = False

def verificar_esc():
    global interromper
    while True:
        if keyboard.is_pressed("esc"):
            interromper = True
            print("\nProcesso interrompido pelo usuário.")
            break
        sleep(0.1)

def stringLinha():
    print('-' * 40)

def enderacamento():
    global interromper
    interromper = False
    threading.Thread(target=verificar_esc, daemon=True).start()
    salvarNumSeries()
    stringLinha()
    input("Pressione Enter para iniciar o endereçamento. Certifique-se de que a célula inicial está selecionada.")
    sleep(5)
    caminho_arquivo = os.path.join(os.environ['USERPROFILE'], "Downloads", "automatizador_TOTVS-main", "src", "numeros_series.txt")
    try:
        with open(caminho_arquivo, "r") as arquivo:
            series = arquivo.readlines()
            for serie in series:
                if interromper:
                    return
                pyautogui.press('enter')
                pyautogui.write(serie.strip())
                pyautogui.press('enter')
                sleep(0.7)
                pyautogui.write("1")
                sleep(0.7)
                pyautogui.press('down', presses=2)
                sleep(0.7)
                pyautogui.press('right', presses=3)
                sleep(0.7)
    except Exception as e:
        print("Erro:", e)
    
    print("Números de série endereçados com sucesso!")

def obter_configuracoes():
    configuracoes = []
    while True:
        codigo = input(f'{stringLinha()}\nDigite o código da ONU que deseja transferir (ou "sair" para finalizar):\n>>> ')
        if codigo.lower() == 'sair':
            break
        try:
            quantidade = int(input(f"Digite a quantidade para o código {codigo}:\n>>> "))
            armazem_origem = input("Digite o armazém ORIGEM:\n>>> ")
            armazem_destino = input("Digite o armazém DESTINO:\n>>> ")
            configuracoes.append({
                'codigo': codigo,
                'quantidade': quantidade,
                'armazem_origem': armazem_origem,
                'armazem_destino': armazem_destino
            })
        except ValueError:
            print("Quantidade inválida. Tente novamente.")
    return configuracoes

def ler_series(caminho_arquivo, quantidade, offset):
    try:
        with open(caminho_arquivo, "r") as arquivo:
            series = [linha.strip() for linha in arquivo if linha.strip()]
        if not series:
            raise ValueError("O arquivo de números de série está vazio.")
        return series[offset:offset + quantidade]
    except Exception as e:
        print(f"Erro ao ler números de série: {e}")
        return []

def processar_transferencia(series, codigo, armazem_origem, armazem_destino):
    for serie in series:
        if interromper:
            print("Transferência interrompida.")
            return
        try:
            pyautogui.write(codigo)
            pyautogui.press('down')
            sleep(0.7)
            pyautogui.press('right', presses=2)
            pyautogui.write(armazem_origem)
            sleep(0.7)
            pyautogui.press('right', presses=4)
            pyautogui.write(armazem_destino)
            sleep(0.7)
            pyautogui.press('right')
            pyautogui.press('enter')
            pyautogui.write(serie)
            pyautogui.press('enter')
            sleep(0.7)
            pyautogui.press('right', presses=4)
            pyautogui.write("1")
            sleep(0.7)
            pyautogui.press('down', presses=2)
            sleep(0.7)
        except Exception as e:
            print(f"Erro durante o processamento da série {serie}: {e}")

def transferenciaMultipla():
    global interromper
    interromper = False
    threading.Thread(target=verificar_esc, daemon=True).start()

    caminho_arquivo = os.path.join(os.environ['USERPROFILE'], "Downloads", "automatizador_TOTVS-main", "src", "numeros_series.txt")

    stringLinha()
    escolha = input("Digite '1' para transferência única ou '2' para transferência múltipla:\n>>> ")

    if escolha == '1':
        stringLinha()
        codigo = input('Digite o código da ONU que deseja transferir:\n>>> ')
        armazem_origem = input("Digite o armazém ORIGEM:\n>>> ")
        armazem_destino = input("Digite o armazém DESTINO:\n>>> ")
        try:
            input("Pressione Enter para iniciar a transferência automática. Certifique-se de minimizar essa aba e selecionar a célula inicial.")
            sleep(5)
            series = ler_series(caminho_arquivo, quantidade=9999, offset=0)
            processar_transferencia(series, codigo, armazem_origem, armazem_destino)
        except Exception as e:
            print(f"Erro na transferência única: {e}")
    elif escolha == '2':
        configuracoes = obter_configuracoes()
        offset = 0
        try:
            input("Pressione Enter para iniciar a transferência automática. Certifique-se de minimizar essa aba e selecionar a célula inicial.")
            sleep(5)
            for config in configuracoes:
                series = ler_series(caminho_arquivo, config['quantidade'], offset)
                if not series:
                    print(f"Séries insuficientes para o código {config['codigo']}.")
                    continue
                processar_transferencia(series, config['codigo'], config['armazem_origem'], config['armazem_destino'])
                offset += config['quantidade']
        except Exception as e:
            print(f"Erro na transferência múltipla: {e}")
    else:
        print("Opção inválida. Saindo.")

    print("Processo de transferência concluído!")

def solicitar():
    global interromper
    interromper = False
    threading.Thread(target=verificar_esc, daemon=True).start()
    
    stringLinha()
    codigo = input('Digite o código que deseja realizar a solicitação: ')
    numArmazem = input(f"Digite o armazém onde está localizado o código {codigo}: ")
    descSolicit = input('Digite a descrição da sua solicitação: ')
    try:
        quantidade = int(input("Digite a quantidade de solicitações que deseja realizar: "))
        if quantidade <= 0:
            print("Quantidade inválida. Tente novamente.")
            return
    except ValueError:
        print("Entrada inválida. Digite um número inteiro para a quantidade.")
        return

    stringLinha()
    input("Pressione Enter para iniciar o processo de solicitação automática.")
    sleep(5)
    i = 0
    while i < quantidade:
        if interromper:
            return
        try:
            pyautogui.press('right')
            pyautogui.press('enter')
            pyautogui.write(str(codigo))
            pyautogui.press('enter')
            sleep(0.7)
            pyautogui.press('right')
            pyautogui.write(str(numArmazem))
            sleep(0.7)
            pyautogui.press('right')
            pyautogui.write('1')
            pyautogui.press('down')
            sleep(0.7)
            pyautogui.press('right', presses=3)
            pyautogui.write('0101004')
            sleep(0.7)
            pyautogui.press('down')
            pyautogui.press('enter')
            pyautogui.write(unidecode(descSolicit.strip().upper()))
            sleep(0.7)
            pyautogui.press('enter')
            pyautogui.press('down')
            sleep(0.7)
        except Exception as e:
            print("Erro:", e)
        i += 1
            
    print(f"{quantidade} solicitações realizadas com sucesso!")
    
def baixar():
    global interromper
    interromper = False
    threading.Thread(target=verificar_esc, daemon=True).start()
    
    salvarNumSeries()
    stringLinha()
    input("Pressione Enter para iniciar a baixa. Certifique-se de minimizar essa aba e selecionar a primeira célula.")
    sleep(5)
    caminho_arquivo = os.path.join(os.environ['USERPROFILE'], "Downloads", "automatizador_TOTVS-main", "src", "numeros_series.txt")
    try:
        with open(caminho_arquivo, "r") as arquivo:
            series = arquivo.readlines()
            for serie in series:
                if interromper:
                    return
                pyautogui.press('enter')
                pyautogui.write(serie.strip())
                pyautogui.press('enter')
                sleep(0.7)
                pyautogui.press('down')
                pyautogui.press('left')
                sleep(0.7)
    except Exception as e:
        print("Erro:", e)
        
    print("Baixas realizadas com sucesso!")

def salvarNumSeries():
    stringLinha()
    print("Digite os novos números de série para salvar:")
    print("(Apenas 1 nº de série por linha e pressione Enter duas vezes para finalizar):")

    try:
        linhas = []
        while True:
            linha = input()
            if linha == "":
                break
            linhas.append(linha)

        if not linhas:
            print("Digite os Nº de Série para salvar. Tente Novamente.")
            return

        caminho_arquivo = os.path.join(os.environ['USERPROFILE'], "Downloads", "automatizador_TOTVS-main", "src", "numeros_series.txt")
        with open(caminho_arquivo, "w") as arquivo:
            arquivo.write("\n".join(linhas))
    except Exception as e:
        print("Erro:", e)
        
    print("Números de série salvos com sucesso!")

def listarNumSerie():
    stringLinha()
    caminho_arquivo = os.path.join(os.environ['USERPROFILE'], "Downloads", "automatizador_TOTVS-main", "src", "numeros_series.txt")
    try:
        with open(caminho_arquivo, "r") as arquivo:
            series = [linha.strip() for linha in arquivo if linha.strip()]
            if not series:
                print("Não há nenhum Nº de Série salvo.")
            else:
                print("\nNúmeros de Série no arquivo:")
                for serie in series:
                    print(serie.strip())
    except Exception as e:
        print("Erro ao listar números de série:", e)

def menu():
    while True:    
        stringLinha()
        print()
        print("  ██╗      ██████╗  ██████╗  █████╗ ")
        print("  ██║     ██╔═══██╗██╔════╝ ██╔══██╗")
        print("  ██║     ██║   ██║██║  ███╗███████║")
        print("  ██║     ██║   ██║██║   ██║██╔══██║")
        print("  ███████╗╚██████╔╝╚██████╔╝██║  ██║")
        print("  ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝")
        print("      Automatizador TOTVS v1.6.4        ")
        print("         © 2024 Pierry Jonny    ")
        print()
        print("Menu:")
        print("1. Endereçamento")
        print("2. Transferência Múltipla")
        print("3. Solicitar")
        print("4. Baixar Pré-Requisitos")
        print("5. Salvar Nº Série")
        print("6. Listar Nº Série")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            enderacamento()
        elif opcao == "2":
            transferenciaMultipla()
        elif opcao == "3":
            solicitar()
        elif opcao == "4":
            baixar()
        elif opcao == "5":
            salvarNumSeries()
        elif opcao == "6":
            listarNumSerie()
        elif opcao == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")
            
menu()
