# XOR Properties
###### Solved by @titoinatel70

> This is a CTF about decryption
## About the Challenge
 Esse desafio consiste em decriptografar uma série de saídas usando as propriedades do operador XOR.
## Solution
 O operador XOR tem propriedades que podem ser usadas para descriptografar cadeias encriptadas e apresentarei elas a seguir. 

Comutativo: A ? B ? B ? A

Associativo: A ? (B ? C) ? (A ? B) ? C

Identidade: A ? 0 ? A

Auto-Inverso: A ? A ? 0 

A proppriedade comutativa significa que a ordem das operações XOR não é importante. A associativa, por sua vez significa que uma cadeia de operações pode ser realizada sem ordem (não precisamos nos preocupar com os colchetes). A identidade é 0, então XOR com 0 "não faz nada", e por último algo XOR'd com ele mesmo retorna zero.

A questão nos dá 4 saídas criptografadas com o operador XOR e precisamos usar suas propriedades para encontrar a flag!
KEY1 - a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313

KEY2 - KEY1 - 37dcb292030faa90d07e07eec17e1b1c8dafila9d35d4c91a5e

KEY2 - KEY3 - c1545756686e7573db23ab1c3452a98b71a7fb0fddddde5f1

FLAG ? KEY1 ? KEY3 ? KEY2 ? 04ee5555208a22a2cd59091d04767a67ae473170d16df7f56f5ffaf

Podemos fazer um script em Python relacionando essas chaves com as propriedades e rodar no terminal do Kali Linux, uma vez que a flag vêm dessas 3 chaves que foram XOR juntas e depois XOR junto dela. Este script irá rodar a função XOR e através dele encontrar as 3 chaves e por fim, a flag.

Destarte, começamos abrindo o terminal do Kali Linux 

[![Screenshot-2025-06-20-08-50-50.png](https://i.postimg.cc/85Q9DHNV/Screenshot-2025-06-20-08-50-50.png)](https://postimg.cc/xk5t3LXs)

Agora precisamos criar o script que irá armazenar a função XOR e com suas propriedades descriptografar as chaves para que seja possível encontrar a flag. Bom, você deve abrir o terminal e digitar este comando: nano xor.properties.py e será aberta esta tela:

[![Screenshot-2025-06-20-09-12-16.png](https://i.postimg.cc/NFT1t6sZ/Screenshot-2025-06-20-09-12-16.png)](https://postimg.cc/p5W9YnnB)
Desta forma, estamos prontos para escrever nosso script que ficou conforme a foto abaixo:

[![Captura-de-Tela-11.png](https://i.postimg.cc/MG8gJ5WJ/Captura-de-Tela-11.png)](https://postimg.cc/bZ3mQQDm)
Mas o que significa cada linha de código? será explicado no passo-a-passo a seguir:
* começamos importando o biblioteca **"pwn"** e a função **xor**
* em seguida nós declaramos as chaves e a flag e as definimos como "bytes.fromhex" para que sejam geradas em bytes.
* computamos a associação que gerará a chave 2 e 3 (perceba que estamos apenas escrevendo aquelas saídas que a própria qiestão nos deu)
* támbem fazemos o mesmo para com a flag que é associção XOR de todas as chaves juntas e o resultado jogado na função XOR novamente 
* por fim, printamos a flag encontrada na associação anterior nomeada como "flag.decode" e colocada entre parênteses como é exigido pela estrutura do Python. 

Após isso, devemos salvar o script com o comando (windows + X) e escrever como queremos salvar o comando.
Feito isso, voltamos ao terminal para executar o script que acabamos de criar que nos revelará a nossa flag! 

[![Captura-de-tela-2025-06-20-110656.png](https://i.postimg.cc/tCG6PvNx/Captura-de-tela-2025-06-20-110656.png)](https://postimg.cc/xqgqVR7f)

> crypto{x0r_i5_ass0c1at1v3}
