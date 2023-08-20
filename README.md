# QR_STL

Este é um projeto incrível que faz XYZ. Aqui estão as instruções para instalação e execução em diferentes sistemas operacionais.

## Instalação

### Windows

Execute o arquivo .exe

1. Baixe o código-fonte do projeto clicando em "Clone or download" e selecionando "Download ZIP".
2. Extraia o arquivo ZIP para uma pasta no seu computador.
3. Abra o Prompt de Comando e navegue até a pasta onde você extraiu o arquivo ZIP usando o comando `cd`.
4. Execute o seguinte comando para instalar as dependências:


Agora, para executar o projeto, siga os passos abaixo:

Abra o Terminal ou Prompt de Comando.

Navegue até a pasta do projeto onde está o arquivo .py:

```sh
cd CAMINHO-PARA-A-PASTA
```
Execute o arquivo .py usando o seguinte comando:
```sh
python qr_stl.py
```
Certifique-se de que o Python está instalado no seu sistema.

Agora você pode aproveitar o seu incrível projeto!


Após executar o script, você será solicitado a inserir as informações necessárias:

Digite a palavra, frase ou link que você deseja transformar em um QR code e pressione Enter.
Digite a porcentagem de tamanho do cubo (por exemplo, 100 para 100%, tamanho original 200x200mm) e pressione Enter.
recomendacao pessoal use 40 (40% = 80x80mm)
````
40
`````
Digite a porcentagem de tamanho do QR code (por exemplo, 100 para 100%, tamanho original 200x200mm) e pressione Enter.
recomendacao pessoal use 40 (40% = 80x80mm)

````
40
`````
Digite a altura do QR code em milímetros e pressione Enter.
````
1
`````
O script então irá processar as informações fornecidas e gerar um arquivo STL que contém um cubo com o QR code sobre ele. O nome do arquivo será criado com base nas configurações fornecidas.

Uma vez que o processo estiver completo, o script exibirá uma mensagem informando que o arquivo STL foi criado. O nome do arquivo também será exibido.

Lembrando que você pode personalizar as configurações do QR code, do cubo e do arquivo STL ao fornecer as informações solicitadas pelo script. Certifique-se de inserir valores válidos para garantir que o processo de geração seja bem-sucedido.
