from time import sleep
import pyautogui

def stringLinha():
    print('-'*40)

def enderacamento():
    stringLinha()
    print("Digite os novos números de série para endereçar:")
    print("(Apenas 1 nº de série por linha e pressione Enter duas vezes para finalizar):")

    try:
        linhas = []
        while True:
            linha = input()
            if linha == "":
                break
            linhas.append(linha)

        with open("C:/Users/jose.coutinho/Downloads/automatizador_TOTVS-main/src/numeros_series.txt", "w") as arquivo:
            arquivo.write("\n".join(linhas))
    except Exception as e:
        print("Erro:", e)
    print("Numéros de série salvos com sucesso!")

    stringLinha()
    input("Pressione Enter para iniciar o endereçamento. Certifique-se de que a célula inicial está selecionada.")
    try:
        sleep(5)
        with open("C:/Users/jose.coutinho/Downloads/automatizador_TOTVS-main/src/numeros_series.txt", "r") as arquivo:
            series = arquivo.readlines()
            for serie in series:
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

def transferenciaMultipla():
    stringLinha()
    codigoONU = input('Digite o código da ONU que deseja transferir:\n'
                      '010716 = Fiberhome com antena REUSO\n'
                      '010717 = Fiberhome sem antena REUSO\n' 
                      '010720 = Huawei REUSO\n'
                      '000219 = Fiberhome branca ANTIGA\n'
                      '>>> ')
    stringLinha()
    armazemOrigem = input("Digite o armazém ORIGEM das ONU's:\n80 = Cancelamento\n72 = Danificado\n>>> ")
    stringLinha()
    armazemDestino = input("Digite o armazém DESTINO das ONU's:\n01 = Almoxarifado LOGA\n10 = Defeito\n>>> ")

    try:
        input("Pressione Enter para iniciar a transferência automática. Certifique-se de minimizar essa aba e selecionar a célula inicial.")
        sleep(5)
        with open("C:/Users/jose.coutinho/Downloads/automatizador_TOTVS-main/src/numeros_series.txt", "r") as arquivo:
            series = arquivo.readlines()
            for serie in series:
                pyautogui.write(codigoONU)
                pyautogui.press('down')
                sleep(0.2)
                pyautogui.press('right', presses=2)
                pyautogui.write(armazemOrigem)
                sleep(0.2)
                pyautogui.press('right', presses=4)
                pyautogui.write(armazemDestino)
                sleep(0.2)
                pyautogui.press('right')
                pyautogui.press('enter')
                pyautogui.write(serie.strip())
                sleep(0.2)
                pyautogui.press('right', presses=4)
                pyautogui.write("1")
                sleep(0.2)
                pyautogui.press('down', presses=2)
                sleep(0.5)
    except Exception as e:
        print("Erro:", e)

    print("Números de série transferidos com sucesso!")

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
        print("          Automatizador TOTVS         ")
        print("       Criado por: Pierry Jonny    ")
        stringLinha()
        print()
        print("Menu:")
        print("1. Endereçamento")
        print("2. Transferência Múltipla")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            enderacamento()
        elif opcao == "2":
            transferenciaMultipla()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()
