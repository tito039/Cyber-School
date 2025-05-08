# Flag Hunters
###### Solved by @pedrotitoinatel70
> This is a CTF about Reverse Engineering 
## About the Challenge
As letras saltam dos versos para o refrão, como uma chamada de subrotina. Há um refrão oculto que este programa não imprime por padrão. Você consegue fazer com que ele o imprima? Pode haver algo nele para você.
https://challenge-files.picoctf.net/c_verbal_sleep/60bb6b075d79b2e8a2107520060ceb97145c158f47651772fcf53dcdb3df63b1/lyric-reader.py
## Solution
Primeiramente, devemos abrir um terminal para podermos executar os comandos necessários para achar a flag. Após isso, devemos escrever o comando "wget" e colar o link do código-fonte que o enunciado forneceu para fazermos o download dele e assim, estaremos prontos para executarmos o comando "cat lyric-reader.py" que nos fornecerá o artigo escrito em python com a letra da música. Dessa forma, o terminal nos mostrará todo o código e o analisando podemos perceber que o código pede uma entrada de usuário na variavél "crowd" que através dela a flag (escondida na música) é revelada. Por conseguinte, devemos escrever o comando "nc verbal-sleep.picoctf.net 50812" para o terminal pedir para inserirmos a "crowd" e como resposta, escrevemos: ";RETURN 1 (pode ser 2 também)", pois no código do programa revela que a para revelar a flag escondida devemos digitar o número da primeira estrofe (1) ou da segunda (2). Por fim, ao fazermos isso o terminal retornará com a letra de toda a música e com a flag! 
> picoCTF{70637h3r_f0r3v3r_62666df2}
