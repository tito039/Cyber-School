# XOR Properties
###### Solved by @titoinatel70
> This is a CTF about decryption.
## About the Challenge
Esse desafio trabalha a habilidade de decriptar uma chave que foi escondida através do operador XOR.
## Solution

A questão nos fornece uma chave encriptada e nos dá a dica de que primeiro é necessário decodificar-la do hex. Primeiramente, este exercício pode ser resolvido com um script em Python que testará por brute force todas as possibilidades de resposta. Sendo assim, resolveremos esta questão pelo terminal do Kali Linux e então digitaremos o comando "nano favorite.byte.py" para criar o script a seguir.

![questao-3.1.png](https://i.postimg.cc/44bQwhNy/questao-3.1.png) (https://postimg.cc/qgqKvqK.png)

Porém o que significa cada linha de código? começa-se importando a biblioteca **"pwm"** e a função **XOR**.

**# Hexadecimal string**
 * declarar a string que a questão nos deu em hexadecimal.

**# Convert the hex string to bytes**
* declarar a variável "data" para fazer a conversão da string de hexadecimal para bytes.

**# Brute-force single-byte XOR**
* deve-se criar um loop que fará força bruta nos caracteres no intervalo de 0 até 256 bytes da base ASCII.
* a variavél resultado é criada como a combinação XOR da data com a key.

**# Attempt to decode the result as an ASCII string**
* como nem todos os bytes de 0 até 256 são legíveis em ASCII, por isso declara-se a variavél "decoded" para armazenar somente os bytes legíveis em ASCII.
* se todos os caracteres imprimíveis estiverem dentro do intervalo imprimível... a chave será printada e a mensagem será exibida com a flad decodificada

**# Ignore decoding errors for non-ASCII results**
* deve-se criar um caso de exceção para se houver caracteres ASCII que não forem impríveis no resultado o programa ignorará e passará para o próximo.

Após terminada a criação do script, basta salvá-lo com o comando "windows + \ " e voltar para a linha de comando do terminal para o executar. 

[![Captura-de-tela-2025-06-20-192211.png](https://i.postimg.cc/0js3F64n/Captura-de-tela-2025-06-20-192211.png)](https://postimg.cc/1nvJNzsV)

O que se vê na imagem acima são todas as chaves possíveis que todos os seus caracteres imprimíveis são bytes legíveis em ASCII e estão dentro do resultado imprimível. Mas onde está nossa flag? deve-se utilizar o comando **(| grep -e 'xxxxxx')** que filtra todas essas chaves e procura pelos caracteres específicos que desejamos, o que é muito interessante, pois sabemos o formato da nossa flag: _"crypto{}"_

[![Captura-de-tela-2025-06-20-194547.png](https://i.postimg.cc/PrcbqGXs/Captura-de-tela-2025-06-20-194547.png)](https://postimg.cc/2VQLHKL2)

E ai está a flag, excelente! 
> crypto{0x10_15_my_f4v0ur173_by7e}
