# Flag Hunters
###### Solved by @pedrotitoinatel70
> This is a CTF about Reverse Engineering 
## About the Challenge
Esse desafio consiste em encontrar a flag através das estrofes de uma música
## Solution
Primeiramente, a questão nos fornece o código-fonte do programa da questão que é essencial para a resolução da questão. Então devemos copiar o link desse arquivo e colar em um terminal para podermos executar os comandos necessários para achar a flag (no caso eu usei o Webshell) escondida nele. 

[![quest-2-1.png](https://i.postimg.cc/3N0WNLRm/quest-2-1.png)](https://postimg.cc/H8HTP9bk)

 Após isso, devemos escrever o comando "wget" para baixarmos o arquivo do link que a questão nos forneceu
 
 [![quest-2-2.png](https://i.postimg.cc/t4k6LMV4/quest-2-2.png)](https://postimg.cc/3kyWG9Bs)
 
  Dessa forma, estaremos prontos para executarmos o comando "cat lyric-reader.py" que nos fornecerá o artigo escrito em python com a letra da música e assim, o terminal nos mostrará todo o código da letra da música e ao o analisar podemos perceber que o código pede uma entrada de usuário na variavél "crowd" com a qual a flag (escondida na música) é revelada. 

  [![quest-2-3.png](https://i.postimg.cc/PJCKxkYy/quest-2-3.png)](https://postimg.cc/D4K1jHC4)
  [![quest-2-4.png](https://i.postimg.cc/x1v5q5Jw/quest-2-4.png)](https://postimg.cc/XrvdzwgL)
  [![quest-2-5.png](https://i.postimg.cc/Y9sfTyZW/quest-2-5.png)](https://postimg.cc/k6WbbwnJ)

  Por conseguinte, devemos escrever o comando "nc verbal-sleep.picoctf.net 50812" para o terminal pedir para inserirmos a "crowd" e como resposta, escrevemos: ";RETURN 1" , pois o código do programa nos mostra que para revelar a flag devemos digitar o número da primeira estrofe (1) já que é nela que está nossa variavél "CROWD".

  [![quest-2-6.png](https://i.postimg.cc/9z3PQwWX/quest-2-6.png)](https://postimg.cc/p5Z50Th3)

 Por fim, ao fazermos isso o terminal retornará com a letra da música e com a flag revelada! 

 [![quest-2-7.png](https://i.postimg.cc/6TsSxQgn/quest-2-7.png)](https://postimg.cc/5Q3pwfx2)
> picoCTF{70637h3r_f0r3v3r_62666df2}
