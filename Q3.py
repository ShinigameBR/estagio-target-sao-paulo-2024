import json

with open('dados.json', 'r') as file:
    dados = json.load(file)
    
faturamentos_validos = [dia["valor"] for dia in dados if dia["valor"] > 0]

menor_faturamento = min(faturamentos_validos)
maior_faturamento = max(faturamentos_validos)
media_mensal = sum(faturamentos_validos) / len(faturamentos_validos)
dias_acima_da_media = len([dia for dia in faturamentos_validos if dia > media_mensal])

print(f"Menor valor de faturamento: {menor_faturamento}")
print(f"Maior valor de faturamento: {maior_faturamento}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media}")
