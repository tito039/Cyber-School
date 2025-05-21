# RED
###### Solved by @pedrotitoinatel70
> This is a CTF about Forensics
## About the Challenge
A questão consiste em decodificar uma imagem para encontrar um texto que ao ser descriptografado nos revelará a flag. 
## Solution
A questão nos fornece apenas uma imagem vermelha no formato PNG, e o objetivo é encontrar a flag escondida nela. Para isso, acessei o site Aperi'Solve e carreguei a imagem para realizar a análise. Ao explorar os resultados e rolar a página, identifiquei um texto codificado em Base64 na aba chamada Zsteg e opiei o referido texto:(cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ==cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ==cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ==cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ==) e colei no site do base64.decode com a codificação UTF-8, e assim obtive a flag!
> picoCTF{r3d_1s_th3_ult1m4t3_cur3_f0r_54dn355_}
