# Cookie Monster Secret Recipe
###### Solved by @pedrotitoinatel70
> This is a CTF about Web Exploitation
## About the Challenge
Essa questão consiste em inspecionar uma página para encontrar um texto a ser descriptografado. 
## Solution
A questão nos fornece um link e também nos dá a dica de que uma infomação importante está escondida na página de inspeção do site.

[![quest-1-1.png](https://i.postimg.cc/Y9VhtNbZ/quest-1-1.png)](https://postimg.cc/VrqYRtyW)

 Então, para resolver a questão temos que abrir o link e realizar o login no site utilizando qualquer caractere.
 
 [![quest-1-2.png](https://i.postimg.cc/vHwWJ9DD/quest-1-2.png)](https://postimg.cc/K4QkL1Py)
 
  Feito isso, devemos clicar com o botão direito do mouse e inspecionar a página e procurar pela aba "aplicativo".

  [![quest-o-1-3.png](https://i.postimg.cc/xCHX5xv5/quest-o-1-3.png)](https://postimg.cc/1nmR5KYV)
  
   Logo, encontaremos uma tabela com um texto encriptado abaixo da palavra "valor". Em seguida, devemos copiar esse texto e decodificá-lo usando o site  https://www.base64decode.org/ e logo assim, encontraremos a nossa flag! 

   [![quest-1-4.png](https://i.postimg.cc/C1y1RG3q/quest-1-4.png)](https://postimg.cc/cKmZjn4x)
> picoCTF{c00k1e_m0nster_l0ves_c00kies_E634DFBB}
