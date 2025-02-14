import pandas as pd
import os

# Criar diretório para salvar resultados
os.makedirs('resultados', exist_ok=True)

# Ler arquivo de entrada
df = pd.read_csv('dados/entrada.csv')

# Processamento (exemplo: filtrar dados)
df_filtrado = df[df['valor'] > 100]

# Salvar arquivo de saída
df_filtrado.to_csv('resultados/saida.csv', index=False)
