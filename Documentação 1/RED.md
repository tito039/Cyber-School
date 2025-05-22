# RED
###### Solved by @pedrotitoinatel70
> This is a CTF about Forensics
## About the Challenge
A questão consiste em decodificar uma imagem para encontrar um texto que ao ser descriptografado nos revelará a flag. 
## Solution
A questão nos fornece apenas uma imagem vermelha no formato PNG e o objetivo é encontrar a flag escondida nela.
[![Captura-de-tela-2025-05-22-161359.png](https://i.postimg.cc/HW2LZ2zK/Captura-de-tela-2025-05-22-161359.png)](https://postimg.cc/RqW9qwjQ)

 Para isso, acessei o site https://www.aperisolve.com/ e carreguei a imagem para realizar a análise.

 [![quest-3-2.png](https://i.postimg.cc/KzpHjCFw/quest-3-2.png)](https://postimg.cc/LYfT0CJ3)
 
Ao explorar os resultados rolando a página, identifiquei um texto codificado em Base64 na aba "Zsteg" e copiei o referido texto ("cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ==cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ==cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ==cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ==").

[![quest-3-3.png](https://i.postimg.cc/cHzF0YBN/quest-3-3.png)](https://postimg.cc/mzQYSPnd)

Feito isso, eu o colei no site https://www.base64decode.org/ com a codificação UTF-8 e assim obtive a flag!

[![quest-3-4.png](https://i.postimg.cc/7hsGpM3g/quest-3-4.png)](https://postimg.cc/p5jLjj1T)

> picoCTF{r3d_1s_th3_ult1m4t3_cur3_f0r_54dn355_}
