# XOR Starter 
###### Solved by @titoinatel70

> This is a CTF about XOR 
## About the Challenge
O desafio consiste em converter números inteiros em uma cadeia de caracteres utilizando o operador XOR. 
## Solution
Antes de tudo, XOR é um operador bit a bit que retorna 0 se os bits são os mesmos, e 1 caso contrário. Nós iremos precisar usar este parâmetro de comparação para descobrir cada caractere da nossa flag.

Primeiramente, o desafio nos dá uma "corda" (**label**) e um número (**13**) para compararmos com ela. Mas... para que serve essa corda e esse número? bom, podemos usar o XOR para converter o número inteiro fornecido da base decimal para base binária e podemos usar o XOR strings para converter o primeiro cada caractere de uma corda para um número inteiro em base binária e assim, compararmos os resultados obtidos utilizando o parâmetro XOR. 

Dessa forma, começamos convertendo o número 13 para base binária. _OPS: para fazer as converções a seguir utilizei o site https://www.rapidtables.com/ e usei a lupa para encontrar a ferramenta que converte da base decimal para base binária._ 
## Tables

| Numeric base  | binary base   |
| ------------- |:-------------:|
| 13            |   00001101    |

Feito isso, agora temos o número 13 na base necessária para resolução do exercício que consiste em comparar cada carctere da corda com um número ambos em base binária, pois cada letra da corda corresponde a uma letra da flag. Em seguida, no mesmo site devemos selecionar a ferramenta: "text to binary" para convertermos cada caractere da corda fornecida para base binária (**lembre-se de escrever as letras em minúsculo e não fazer a conversão com espaços vazios entre a letra e o marcador |**).
| text base     | binary base   |
| ------------- |:-------------:|
| l             |   01101100    |

Agora que temos tanto o número fornecido pela questão tanto o primeiro caractere da corda em base binária, chegou a hora de usarmos o operador XOR! Vamos comparar as duas bases binárias recebidas.
| inicial character    | orginal base  | in binary base|
|      -------------   |:-------------:|:-----------:|
|           13         |    decimal    |    00001101 |
|          l           |      text     |    01101100 |
|        in XOR        |     binary    |    01100001 |  

Excelente! temos o primeiro código binário da primeira letra da nossa flag que deve estar nesse formato: _crypto{new_string}._ Bom, sabemos que a flag é uma palavra e temos o código da primeira letra... basta convertemos esse código binário em texto usando o mesmo site citado acima.
 | Binary base   | text base    |
 | ------------- |:------------:|
 |    01100001   |   a          |

Aqui está a primeira letra da nossa flag "**a**"! Agora devemos continuar usando o XOR e fazer o mesmo processo feito antes: 
* converter a letra (text) para base binária
* usar o operador XOR para fazer a comparação com o número 13 também em base binária 
* colar o resultado em um site faça a conversão da base binária para texto
* assim iremos obter a próxima letra.

| inicial character    | orginal base  | in binary base|
|      -------------   |:-------------:|:-----------:|
|           13         |    decimal    |    00001101 |
|          a           |      text     |    01100001 |
|        in XOR        |     binary    |    01101100 |  

Agora, novamente iremos converter para base textual para obtermos a próxima letra da flag!

 | Binary base   | text base    |
 | ------------- |:------------:|
 |    01101100   |   l          |

Bom, esse é o caminho "manual". Porém, há uma calculadora do operador XOR pela qual também podemos usar para capturarmos a flag da questão. O site é https://xor.pw/ e o método de resolução mudará um pouco, mas explicarei a seguir em um passo a passo. 

[![Screenshot-2025-06-19-11-19-42.png](https://i.postimg.cc/mD3ncW8g/Screenshot-2025-06-19-11-19-42.png)](https://postimg.cc/BL6pyyrr)
* em 1.Input selecione decimal(base10) e coloque o número 13
* em 2.Input selecione ASCII (base 256) e coloque a letra respectiva da corda
* em 3.Output selecione também a ASCII (base 256)
* assim iremos obter a próxima letra da flag

lembra que a questão nos forneceu uma "corda"? Então, nesse método devemos colocar no 2.Input cada letra da corda (**label**) na sequência original dela para gerar na ordem certa as respectivas letras da flag.
No caso, nós já obtemos as duas primeiras letras da flag, então agora colocarei a terceira letra (**"b"**)

 [![Screenshot-2025-06-19-11-30-44.
 png](https://i.postimg.cc/85bypBzF/Screenshot-2025-06-19-11-30-44.png)](https://postimg.cc/YGhN8Fgk).

Perfeito! agora já temos a terceira letra da flag: _crypto{alo...}_. Agora basta repetir o mesmo processo com as duas últimas letras da corda e a flag estará completa!

> crypto{aloha}
