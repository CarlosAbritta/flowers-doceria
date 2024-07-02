import os
from time import sleep

cardapio = [
    {"nome": "petit gateau", "categoria": "doce", "preço": "R$ 19.90", "ativo": False}, 
    {"nome": "bolo no pote", "categoria": "doce", "preço": "R$ 20.00", "ativo": True},
    {"nome": "sanduíche natural", "categoria": "salgado", "preço": "R$ 12.50", "ativo": True},
    {"nome": "croissant", "categoria": "salgado", "preço": "R$ 10.29", "ativo": True}
]

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def continuar_menu_adm():
    print("")
    escolha_continuar = input("Sim para continuar ou não para finalizar o programa: ").strip().lower()
    if escolha_continuar == "sim":
        menu_adm()
    else:
        print("Finalizando o menu de administrador...")
        sleep(2)

def senha_adm(nome):
    senha = "cadu1234ueu"
    pergunta_senha = input("Para continuar como administrador digite a senha: ").strip()
    if pergunta_senha == senha:
        print("Acesso liberado")
        menu_adm()
    else:
        print("Senha incorreta!")
        distinguir_usuario(nome)

def distinguir_usuario(nome):
    try:
        pergunta_tipo_user = int(input("Você gostaria de começar como usuário ou administrador? Escolha 1 para usuário ou 2 para administrador: ").strip())
        if pergunta_tipo_user == 1:
            print("Você será direcionado para o menu de cardápios!")
            sleep(2)
            saudacao(nome)
            mostrar_cardapio(nome)
        elif pergunta_tipo_user == 2:
            senha_adm(nome)
        else:
            print("Escolha inválida! Tente novamente.")
            distinguir_usuario(nome)
    except ValueError:
        print("Opção inválida! Tente novamente.")
        distinguir_usuario(nome)

def listar_prato():
    for item in cardapio:
        prato = item["nome"]
        categoria_prato = item["categoria"]
        preço_prato = item["preço"]
        estado_prato = "Ativo" if item["ativo"] else "Inativo"
        print(f"{prato} | {categoria_prato} | {preço_prato} | {estado_prato}")

def adicionar_prato():
    nome = input("Digite o nome do prato: ").strip()
    categoria = input("Digite a categoria do prato (doce/salgado): ").strip().lower()
    preco = input("Digite o preço do prato: ").strip()
    ativo = input("O prato está ativo? (sim/não): ").strip().lower() == 'sim'
    cardapio.append({"nome": nome, "categoria": categoria, "preço": preco, "ativo": ativo})
    print("Prato adicionado com sucesso!")

def alterar_estado_prato():
    listar_prato()
    nome_prato = input("Digite o nome do prato que deseja ativar/desativar: ").strip()
    for item in cardapio:
        if item["nome"].lower() == nome_prato.lower():
            item["ativo"] = not item["ativo"]
            estado = "ativo" if item["ativo"] else "inativo"
            print(f"O prato {item['nome']} agora está {estado}.")
            return
    print("Prato não encontrado.")

def menu_adm():
    limpar_tela()
    print("Bem-vindo ao menu do administrador")
    escolha_adm = input("""Digite [1] para listar os pratos
Digite [2] para adicionar um prato 
Digite [3] para ativar ou desativar um prato: """).strip()
    if escolha_adm == "1":
        listar_prato()
    elif escolha_adm == "2":
        adicionar_prato()
    elif escolha_adm == "3":
        alterar_estado_prato()
    else:
        print("Escolha inválida! Tente novamente.")
        menu_adm()
    continuar_menu_adm()

def perguntar_nome():
    nome = input("Olá, para começarmos primeiro gostaríamos de saber o seu nome: ").strip().title()
    return nome

def saudacao(nome):
    limpar_tela()
    print(f"Bem-vindo(a) à Flowers Doceria, {nome}!")
    sleep(2)

def mostrar_cardapio_doce(nome):
    limpar_tela()
    print("Cardápio de Doces:")
    print(f"{'Nome'.ljust(25)}| {'Categoria'.ljust(15)}| {'Preço'.ljust(10)}")
    print("-" * 55)
    for item in cardapio:
        if item["categoria"] == "doce" and item["ativo"]:
            nome_doce = item["nome"].ljust(25)
            categoria_doce = item["categoria"].ljust(15)
            preço_doce = item["preço"].ljust(10)
            print(f"{nome_doce}| {categoria_doce}| {preço_doce}")
    voltar_ao_cardapio(nome)

def mostrar_cardapio_salgado(nome):
    limpar_tela()
    print("Cardápio de Salgados:")
    print(f"{'Nome'.ljust(25)}| {'Categoria'.ljust(15)}| {'Preço'.ljust(10)}")
    print("-" * 50)
    for item in cardapio:
        if item["categoria"] == "salgado" and item["ativo"]:
            nome_salgado = item["nome"].ljust(25)
            categoria_salgado = item["categoria"].ljust(15)
            preço_salgado = item["preço"].ljust(10)
            print(f"{nome_salgado}| {categoria_salgado}| {preço_salgado}")
    voltar_ao_cardapio(nome)

def mostrar_cardapio(nome):
    limpar_tela()
    print("")
    try:
        escolha = int(input(f"{nome}, você gostaria de ver o nosso cardápio doce ou salgado? Digite 1 para salgado ou 2 para doce ou 3 para finalizar: ").strip())
        if escolha == 2:
            mostrar_cardapio_doce(nome)
        elif escolha == 1:
            mostrar_cardapio_salgado(nome)
        elif escolha == 3:
            print("Finalizando o programa...")
            sleep(1)
            print("Programa finalizado") 
        else:
            print("Escolha um número entre 1 e 3")
            sleep(2)
            mostrar_cardapio(nome)
    except ValueError:
        print("Opção inválida! Você deve escolher um número.")
        sleep(2)
        mostrar_cardapio(nome)

def voltar_ao_cardapio(nome):
    print("")
    input("Digite qualquer tecla para voltar ao menu de cardápios: ")
    mostrar_cardapio(nome)

def main():
    nome = perguntar_nome()
    saudacao(nome)
    distinguir_usuario(nome)

if __name__ == "__main__":
    main()
