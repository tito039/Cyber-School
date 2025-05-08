# Cookie Monster Secret Recipe
###### Solved by @pedrotitoinatel70
> This is a CTF about Cryptography
## About the Challenge
Can you get the real meaning from this file https://artifacts.picoctf.net/c_titan/111/enc_flag. 
## Solution
A questão nos fornece um arquivo contendo um texto criptografado, e nos tópicos abordados é mencionado o uso de "base64" e "Caesar". Assim, abri o Kali Linux, baixei o arquivo para a pasta Downloads e, no terminal, utilizei o comando base64 -d enc_flag, que retornou um novo texto. Copiei esse texto para o site Base64 Decode, o qual gerou outro conteúdo ainda criptografado. Por fim, utilizei o site CyberChef, apliquei a ferramenta Caesar Cipher, cliquei em Decrypt, e a flag foi revelada!
> picoCTF{caesar_d3cr9pt3d_890d2379}
