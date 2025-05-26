# Interdec 
###### Solved by @pedrotitoinatel70
> This is a CTF about Cryptography
## About the Challenge
O desafio consiste em obter textos criptografados e descriptografá-los utilizando as ferramentas certas. 
## Solution
A questão nos fornece um arquivo contendo um texto codificado e nos tópicos da questão é mencionado o uso de "base64" e "Caesar". Então, já podemos identificar duas dicas das bases que teremos que usar para decodificar o texto. Primeiramente, eu abri o arquivo anexado e encontrei o seguinte texto:

[![quest4-1.png](https://i.postimg.cc/KjTFMWSv/quest4-1.png)](https://postimg.cc/QKjRL0dR)

Então, para extrair esse texto em base64 eu fui ao site https://www.base64decode.org/ e colei o texto encontrado no bloco de notas.

[![quest4-2.png](https://i.postimg.cc/Sx1MVXY2/quest4-2.png)](https://postimg.cc/87WczzHN)

Na mensagem gerada, percebe-se que há um texto entre as reticências. Devemos copiá-lo e colá-lo no campo acima para gerar outra mensagem codificada em Base64 novamente. 

[![quest4-3.png](https://i.postimg.cc/q7tCFk2m/quest4-3.png)](https://postimg.cc/qtTRhHbn)

Agora obtivemos um texto codificado em Caeser. Porém como podemos afirmar isso? 
Simples, na base Caeser o texto decodificado tem o mesmo número de caracteres do texto original tanto que o texto acima está no formato da flag! Consequentemente, considerando o número de letras do alfabeto há 25 posições possíveis para as letras do texto codificado assumirem.

Por fim, acessei https://www.dcode.fr/cipher-identifier e apliquei a força bruta para o computador testar as possíveis posições e a flag foi revelada!

[![quest4-4.png](https://i.postimg.cc/DZ7ZQnfp/quest4-4.png)](https://postimg.cc/7CQwwv2S)
> picoCTF{caesar_d3cr9pt3d_890d2379}
