# Cookie Monster Secret Recipe
###### Solved by @pedrotitoinatel70
> This is a CTF about Web Exploitation, browser_webshell_solvable
## About the Challenge
Cookie Monster has hidden his top-secret cookie recipe somewhere on his website. As an aspiring cookie detective, your mission is to uncover this delectable secret. Can you outsmart Cookie Monster and find the hidden recipe?
You can access the Cookie Monster here and good luck
## Solution
A questão nos fornece um link e também nos dá a dica de que uma infomação importante está escondida na página de inspeção do site. Então, para resolver a questão temos que abrir o link e realizar o login no site utilizando qualquer caractere. Feito isso, devemos clicar com o botão direito do mouse e inspecionar a página e procurar pela aba "aplicativo". Logo, encontaremos uma tabela com um texto encriptado abaixo da palavra "valor". Em seguida, devemos copiar esse texto e decodificá-lo usando o site  https://www.base64decode.org/ e logo assim, encontraremos a nossa flag! 
> picoCTF{c00k1e_m0nster_l0ves_c00kies_E634DFBB}
