# Password Strength Checker

Criei este script em Python para avaliar a força de senhas de forma simples e direta. 

A ideia surgiu da vontade de treinar lógica de programação voltada à segurança defensiva, focando em um problema do dia a dia: como garantir que uma senha atende a critérios mínimos de complexidade antes de ser utilizada.

Para deixar a ferramenta mais realista e segura de usar, decidi implementar a biblioteca `getpass`. Assim, quando você testa uma senha no terminal, os caracteres ficam ocultos.

## O que o script faz

- Verifica o comprimento total da senha.
- Confere se há uma mistura de letras maiúsculas, minúsculas, números e caracteres especiais.
- Dá um veredito rápido (Fraca, Média ou Forte).
- Oculta a digitação da senha por segurança.

## Como testar

Basta ter o Python instalado, baixar o arquivo e rodar isso no seu terminal:

```bash
python checker.py
