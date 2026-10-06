import re
import getpass

def verificar_forca_senha(senha):
    pontuacao = 0
    feedback = []

    # Critério 1: Comprimento
    if len(senha) >= 8:
        pontuacao += 1
    else:
        feedback.append("A senha deve ter pelo menos 8 caracteres.")

    if len(senha) >= 12:
        pontuacao += 1

    # Critério 2: Letras maiúsculas e minúsculas
    if re.search(r"[A-Z]", senha):
        pontuacao += 1
    else:
        feedback.append("Adicione letras maiúsculas.")

    if re.search(r"[a-z]", senha):
        pontuacao += 1
    else:
        feedback.append("Adicione letras minúsculas.")

    # Critério 3: Números
    if re.search(r"[0-9]", senha):
        pontuacao += 1
    else:
        feedback.append("Adicione números.")

    # Critério 4: Caracteres especiais
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", senha):
        pontuacao += 1
    else:
        feedback.append("Adicione caracteres especiais (ex: @, #, $).")

    # Avaliação final
    if pontuacao <= 2:
        nivel = "Fraca"
    elif pontuacao <= 4:
        nivel = "Média"
    else:
        nivel = "Forte"

    return nivel, feedback

if __name__ == "__main__":
    print("--- Verificador de Força de Senhas ---")
    # getpass esconde a senha enquanto é digitada no terminal
    senha_usuario = getpass.getpass("Digite a senha para testar (os caracteres não aparecerão): ")
    
    nivel, feedback = verificar_forca_senha(senha_usuario)
    
    print(f"\nNível de Segurança: {nivel}")
    if feedback:
        print("Sugestões de melhoria:")
        for dica in feedback:
            print(f"- {dica}")