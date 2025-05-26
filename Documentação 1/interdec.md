# Interdec 
###### Solved by @pedrotitoinatel70
> This is a CTF about Cryptography
## About the Challenge
O desafio consiste em obter textos criptografados e descriptografá-los utilizando as ferramentas certas. 
## Solution
A questão nos fornece um arquivo com um texto codificado e, nos tópicos, menciona o uso de "Base64" e "Cifra de César". Isso já nos dá duas dicas importantes sobre os métodos de decodificação. Primeiro, abri o arquivo e encontrei o seguinte texto:

[![quest4-1.png](https://i.postimg.cc/KjTFMWSv/quest4-1.png)](https://postimg.cc/QKjRL0dR)

Para extrair o texto em Base64, fui ao site https://www.base64decode.org/ e colei o conteúdo do arquivo. Na mensagem gerada, percebi um texto entre as reticências. É preciso copiá-lo e colá-lo no campo de decodificação para gerar outra mensagem em Base64."

[![quest4-2.png](https://i.postimg.cc/Sx1MVXY2/quest4-2.png)](https://postimg.cc/87WczzHN)

Na mensagem gerada, percebe-se que há um texto entre as reticências. Devemos copiá-lo e colá-lo no campo acima para gerar outra mensagem codificada em Base64 novamente. 

[![quest4-3.png](https://i.postimg.cc/q7tCFk2m/quest4-3.png)](https://postimg.cc/qtTRhHbn)

Acabamos de obter um texto codificado em Cifra de César. Como podemos saber isso?
A explicação é simples: a Cifra de César mantém o mesmo número de caracteres do texto original no seu resultado decodificado. Nosso texto, por exemplo, já segue o formato de flag. Além disso, como trabalhamos com as letras do alfabeto, existem 25 posições de deslocamento possíveis para as letras no texto cifrado.

Por fim, acessei https://www.dcode.fr/cipher-identifier e apliquei a força bruta para o computador testar as possíveis posições e a flag foi revelada!

[![quest4-4.png](https://i.postimg.cc/DZ7ZQnfp/quest4-4.png)](https://postimg.cc/7CQwwv2S)
> picoCTF{caesar_d3cr9pt3d_890d2379}
