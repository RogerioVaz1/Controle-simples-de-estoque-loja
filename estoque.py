# Controle Simples de Estoque
# Programa básico para gerenciar produtos de uma loja

print("=" * 50)
print("SISTEMA DE CONTROLE DE ESTOQUE")
print("=" * 50)

# Lista para armazenar os produtos (cada produto é uma lista: [nome, quantidade, preço])
estoque = []

# Loop principal do programa
while True:
    print("\n--- MENU ---")
    print("1. Adicionar produto")
    print("2. Remover produto")
    print("3. Atualizar quantidade")
    print("4. Ver estoque completo")
    print("5. Buscar produto")
    print("6. Sair")
    
    opcao = input("\nEscolha uma opção: ")
    
    # Adicionar produto
    if opcao == "1":
        print("\n--- ADICIONAR PRODUTO ---")
        nome = input("Nome do produto: ")
        quantidade = int(input("Quantidade: "))
        preco = float(input("Preço unitário: R$ "))
        
        # Adiciona o produto na lista
        estoque.append([nome, quantidade, preco])
        print(f"\n✓ Produto '{nome}' adicionado com sucesso!")
    
    # Remover produto
    elif opcao == "2":
        print("\n--- REMOVER PRODUTO ---")
        nome = input("Nome do produto a remover: ")
        
        produto_encontrado = False
        for produto in estoque:
            if produto[0] == nome:
                estoque.remove(produto)
                print(f"\n✓ Produto '{nome}' removido com sucesso!")
                produto_encontrado = True
                break
        
        if not produto_encontrado:
            print(f"\n✗ Produto '{nome}' não encontrado!")
    
    # Atualizar quantidade
    elif opcao == "3":
        print("\n--- ATUALIZAR QUANTIDADE ---")
        nome = input("Nome do produto: ")
        
        produto_encontrado = False
        for produto in estoque:
            if produto[0] == nome:
                print(f"Quantidade atual: {produto[1]}")
                nova_quantidade = int(input("Nova quantidade: "))
                produto[1] = nova_quantidade
                print(f"\n✓ Quantidade atualizada para {nova_quantidade}!")
                produto_encontrado = True
                break
        
        if not produto_encontrado:
            print(f"\n✗ Produto '{nome}' não encontrado!")
    
    # Ver estoque completo
    elif opcao == "4":
        print("\n--- ESTOQUE COMPLETO ---")
        
        if len(estoque) == 0:
            print("Estoque vazio!")
        else:
            print(f"\n{'Produto':<20} {'Quantidade':<15} {'Preço':<10} {'Total'}")
            print("-" * 60)
            
            valor_total_estoque = 0
            for produto in estoque:
                nome = produto[0]
                quantidade = produto[1]
                preco = produto[2]
                total = quantidade * preco
                valor_total_estoque = valor_total_estoque + total
                
                print(f"{nome:<20} {quantidade:<15} R$ {preco:<8.2f} R$ {total:.2f}")
            
            print("-" * 60)
            print(f"Valor total do estoque: R$ {valor_total_estoque:.2f}")
    
    # Buscar produto
    elif opcao == "5":
        print("\n--- BUSCAR PRODUTO ---")
        nome = input("Nome do produto: ")
        
        produto_encontrado = False
        for produto in estoque:
            if produto[0] == nome:
                print(f"\nProduto: {produto[0]}")
                print(f"Quantidade: {produto[1]}")
                print(f"Preço: R$ {produto[2]:.2f}")
                print(f"Valor total: R$ {produto[1] * produto[2]:.2f}")
                produto_encontrado = True
                break
        
        if not produto_encontrado:
            print(f"\n✗ Produto '{nome}' não encontrado!")
    
    # Sair
    elif opcao == "6":
        print("\n" + "=" * 50)
        print("Obrigado por usar o Sistema de Controle de Estoque!")
        print("=" * 50)
        break
    
    # Opção inválida
    else:
        print("\n✗ Opção inválida! Tente novamente.")
