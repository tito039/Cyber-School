# XOR You either know, XOR you don't

###### Solved by @titoinatel70

## About the Challenge
This is a challenge about decryption.
## Solution
A questão fornece apenas a flag que foi encriptada em hexadecimal com uma chave secreta e nos dá a dica de que o formato da flag pode nos ajudar a resolver o desafio. Sobretudo, podemos usar o terminal do Kali Linux para fazer um script em Phython que irá decriptar a flag.
Primeiramente, digitamos o comando "nano" junto com o nome do script que pode ser de acordo com a escolha do jogador. 

[![questao-4.1.png](https://i.postimg.cc/htwRttw8/questao-4.1.png)](https://postimg.cc/QFpy6hjV)

Logo, para que não haja dúvidas irei explicar as linhas de código do script acima.

* Começar importando a biblioteca _"pwn"_ que nos permite lidar com dados codificados em _exploits_ e a função _XOR_ para que o script possa rodar o operador XOR que nos ajudará a encontrar a flag.
* _encrypted_bytes:_
    * Declarar uma variavél que transforme a flag dada pelo exercício de hex para bytes.
* _key_bytes:_
    * esta função é compreendida a partir da existência de 3 chaves (A,B,C) que se por exemplo B for XOR com C, retornará A e vice-versa. Ou seja, precisamos de duas chaves para descobrir a outra. A string **A** é a chave em bytes, a string **B** é a string A após ter sido jogada no operador XOR e a string **C** é modelo da nossa flag (_"crypto{"_). A associação dessas 3 strings gerará a chave em bytes.
* _printar a função final_
    * iremos associar em XOR a variavél **key_bytes** com a variavél **encrypted_bytes** e decodificar a resultante dessa associação em ASCII para que esteja no mesmo formato da flag. 

Por fim, deve-se digitar o comando "python" com o nome do script para que ele rode no terminal do Kali Linux. 

[![questao-4.2.png](https://i.postimg.cc/XNT2qy7Y/questao-4.2.png)](https://postimg.cc/s14P0xhk)

Perfeito! ai está a nossa flag!
> crypto{1f_y0u_Kn0w_En0uGH_y0u_Kn0w_1t_4ll}
