# Cookie Monster Secret Recipe
###### Solved by @pedrotitoinatel70
> This is a CTF about Web Exploitation
## About the Challenge
O Monstro dos Biscoitos escondeu sua receita secreta de biscoitos em algum lugar do seu site. Como um aspirante a detetive de biscoitos, sua missão é descobrir esse segredo delicioso. Você consegue enganar o Monstro dos Biscoitos e encontrar a receita escondida? Você pode acessar o Monstro dos Biscoitos aqui e boa sorte.
## Solution
A questão nos fornece um link e também nos dá a dica de que uma infomação importante está escondida na página de inspeção do site. Então, para resolver a questão temos que abrir o link e realizar o login no site utilizando qualquer caractere. Feito isso, devemos clicar com o botão direito do mouse e inspecionar a página e procurar pela aba "aplicativo". Logo, encontaremos uma tabela com um texto encriptado abaixo da palavra "valor". Em seguida, devemos copiar esse texto e decodificá-lo usando o site  https://www.base64decode.org/ e logo assim, encontraremos a nossa flag! 
> picoCTF{c00k1e_m0nster_l0ves_c00kies_E634DFBB}
