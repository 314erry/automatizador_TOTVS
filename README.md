# Automatizador TOTVS

## Descrição

O **Automatizador TOTVS** é um programa desenvolvido em Python que tem como objetivo automatizar os processos de endereçamento, transferência múltipla, solicitação e baixa de pré-requisitos de códigos ONU's em seus respectivos armazéns dentro do software TOTVS. Este processo automatizado visa aumentar a eficiência e reduzir o tempo gasto nas operações manuais relacionadas a esses processos.

## Funcionalidades

- **Endereçamento**: Permite a inserção de novos números de série e realiza o endereçamento automático no sistema TOTVS.
- **Transferência Múltipla**: Facilita a transferência de códigos ONU para diferentes armazéns, automatizando as interações necessárias no TOTVS.
- **Solicitar**: Permite a solicitação automática de baixa de ONU's no sistema TOTVS.
- **Baixar pré-requisitos**: Facilita a baixa de números de série ONU para diferentes armazéns, escrevendo os números de série automaticamente no TOTVS.
- **Salvar Nº de Série**: Possibilita salvar os números de série, persistindo-os em um arquivo .txt.
- **Listar Nº de Série**: Possibilita listar os números de série salvos no arquivo .txt, caso seja necessário.
- **Interromper processo automático**: Permite interromper um processo qualquer onde há a automatização de algum processo ao apertar a tecla "esc".

## Requisitos

Para executar este programa, você precisa ter o seguinte instalado em sua máquina:

- **Python 3**: [Download Python](https://www.python.org/downloads/)
- **Bibliotecas PyAutoGUI, Unidecode e Keyboard**: Para instalação, execute o seguinte comando no seu terminal ou prompt de comando:

  ```bash
  python -m pip install pyautogui unidecode keyboard

## Instruções de Uso

1. **Baixe o repositório**: Clone ou baixe o repositório que contém o código.
2. **Descompacte o arquivo**: Caso o repositório esteja compactado, descompacte-o.
3. **Certifique-se do nome da pastas**: Caso a pasta descompactada tenha outro nome além de "automatizador_TOVS-main", certifique-se de alterar o nome da pasta para a mesma mencionada.
4. **Navegue até a pasta**: Acesse a pasta `src` onde o arquivo `script.py` está localizado.
5. **Execute o programa**: No terminal ou prompt de comando, execute o seguinte comando para iniciar o programa:

   ```bash
   python script.py
   ```

   Ou você pode rodar o programa clicando duas vezes no `script.py` e selecionando abrir com o Python.

6. **Siga as instruções no menu**: O programa irá apresentar um menu com opções para endereçamento, transferência múltipla, solicitação, baixa de pré-requisitos, salvar nº de série e listar nº de série.

## Como Funciona

- O usuário pode inserir novos números de série para endereçamento.
- O programa solicita informações sobre a transferência e baixa de ONU's, como códigos e armazéns.
- O usuário pode salvar novos números de série no programa, persistindo os dados.
- O usuário pode listar os números de série salvos no arquivo numeros_series.txt e mostrá-los na tela.
- As operações são realizadas automaticamente, permitindo que o usuário minimize a janela e prepare-se para o próximo passo.
- O usuário pode interromper um processo apertando a tecla "esc", fazer isso no início de uma iteração do loop fará com que ele pare e volte para o menu inicial.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

## Contato

Para mais informações ou dúvidas, entre em contato com **314pierry@gmail.com**.
