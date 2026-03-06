# cria todas as fichas do dia
total_fichas = 20
fichas = list(range(1, total_fichas + 1))

print("Sistema de chamada iniciado")

# enquanto ainda houver fichas
while fichas:
    input("Pressione Enter para chamar a próxima ficha...")
    
    ficha_chamada = fichas.pop(0)
    print(f"Ficha chamada: {ficha_chamada}")

print("Todas as fichas foram atendidas")  
