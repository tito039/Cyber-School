# Interdec 
###### Solved by @pedrotitoinatel70
> This is a CTF about Cryptography
## About the Challenge
O desafio consiste em obter textos criptografados e descriptografá-los utilizando as ferramentas certas. 
## Solution
A questão nos fornece um arquivo contendo um texto criptografado, e nos tópicos abordados é mencionado o uso de "base64" e "Caesar". Então, já podemos identificar duas dica das bases decodificadoras que teremos que usar. 
Primeiramente, eu abri o Kali Linux, pois por se tratar de uma máquina virtual eu consigo baixar o arquivo fornecido dentro de uma pasta do Kali e usar o terminal próprio dele para resolvermos a questão. 
Então, eu baixei o arquivo na pasta de Downloads e segui com os seguintes comandos no Kali



Ao copiei o texto gerado em base64, eu o colei no site https://www.base64decode.org/ que gerou outro texto ainda criptografado.
Por fim, acessei o site https://cyberchef.org e apliquei a ferramenta Caesar Cipher para decriptar o texto e a flag foi revelada!


> picoCTF{caesar_d3cr9pt3d_890d2379}
