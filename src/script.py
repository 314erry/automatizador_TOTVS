from time import sleep
from unidecode import unidecode
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

        with open("C:/Users/jose.coutinho/Downloads/automatizador_TOTVS-main/src/numeros_series.txt", "w") as arquivo: # MUDAR CAMINHO
            arquivo.write("\n".join(linhas))
    except Exception as e:
        print("Erro:", e)
    print("Numéros de série salvos com sucesso!")

    stringLinha()
    input("Pressione Enter para iniciar o endereçamento. Certifique-se de que a célula inicial está selecionada.")
    try:
        sleep(5)
        with open("C:/Users/jose.coutinho/Downloads/automatizador_TOTVS-main/src/numeros_series.txt", "r") as arquivo: # MUDAR CAMINHO
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
                      '010716 = ONU FIBERHOME GPON HG6143D 5G + WIFI - REUSO\n'
                      '010717 = ONU FIBERHOME GPON HG6143D3  5G + WIFI - REUSO\n' 
                      '010718 = ONU FIBERHOME GPON HG6145D2 REUSO\n' 
                      '010720 = ONU HUAWEI 5.8 REF: 50083734 HW EG8145V5 - REUSO\n'
                      '000219 = APARELHO ONU - 4FE + 2FXS+ WIF\n'
                      'Você pode digitar um dos códigos acima ou outro.'
                      '>>> ')
    stringLinha()
    armazemOrigem = input("Digite o armazém ORIGEM:\n80 = Cancelamento\n72 = Danificado\nVocê pode digitar um dos armazéns acima ou outro.\n>>> ")
    stringLinha()
    armazemDestino = input("Digite o armazém DESTINO:\n01 = Almoxarifado LOGA\n10 = Defeito\nVocê pode digitar um dos armazéns acima ou outro.\n>>> ")

    try:
        input("Pressione Enter para iniciar a transferência automática. Certifique-se de minimizar essa aba e selecionar a célula inicial.")
        sleep(5)
        with open("C:/Users/jose.coutinho/Downloads/automatizador_TOTVS-main/src/numeros_series.txt", "r") as arquivo: # MUDAR CAMINHO
            series = arquivo.readlines()
            for serie in series:
                pyautogui.write(codigoONU)
                pyautogui.press('down')
                sleep(0.7)
                pyautogui.press('right', presses=2)
                pyautogui.write(armazemOrigem)
                sleep(0.7)
                pyautogui.press('right', presses=4)
                pyautogui.write(armazemDestino)
                sleep(0.7)
                pyautogui.press('right')
                pyautogui.press('enter')
                pyautogui.write(serie.strip())
                pyautogui.press('enter')
                sleep(0.7)
                pyautogui.press('right', presses=4)
                pyautogui.write("1")
                sleep(0.7)
                pyautogui.press('down', presses=2)
                sleep(0.7)
    except Exception as e:
        print("Erro:", e)

    print("Números de série transferidos com sucesso!")

def solicitar():
    stringLinha()
    codigo = input('Digite o código que deseja realizar a solicitação: ')
    numArmazem = input(f"Digite o armazém onde está localizado o código {codigo}: ")
    descSolicit = input('Digite a descrição da sua solicitação: ')
    stringLinha()

    i = 0
    while i < 10:
        input("Pressione Enter para iniciar o processo de solicitação automática. Certifique-se de que a célula inicial está selecionada.")
        sleep(5)
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
            pyautogui.write(unicode(descSolicit.strip().upper()))
            sleep(0.7)
            pyautogui.press('enter')
            pyautogui.press('down')
            sleep(0.7)
        except Exception as e:
            print("Erro:", e)
        i += 1
            
    print("Solicitações realizadas com sucesso!")

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
        print("      Automatizador TOTVS v1.1.2        ")
        print("       Criado por: Pierry Jonny    ")
        stringLinha()
        print()
        print("Menu:")
        print("1. Endereçamento")
        print("2. Transferência Múltipla")
        print("3. Solicitar")
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
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()
