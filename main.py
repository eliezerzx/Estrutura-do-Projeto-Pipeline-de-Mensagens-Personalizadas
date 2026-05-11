import pandas as pd

# === ETAPA 1: EXTRAÇÃO (Extract) ===
df = pd.read_csv('usuarios.csv')
print("Dados Extraídos:")
print(df)

# === ETAPA 2: TRANSFORMAÇÃO (Transform) ===
def gerar_mensagem(row):
    if row['Saldo'] < 500:
        return f"Olá {row['Nome']}, que tal um investimento de baixo risco para começar a poupar?"
    else:
        return f"Olá {row['Nome']}, vimos que seu saldo está ótimo! Conheça nossas opções de Renda Fixa."

df['Mensagem'] = df.apply(gerar_mensagem, axis=1)
print("\nDados Transformados:")
print(df[['Nome', 'Mensagem']])

# === ETAPA 3: CARREGAMENTO (Load) ===
df.to_csv('promocoes_bancarias.csv', index=False)
print("\nSucesso! Arquivo 'promocoes_bancarias.csv' gerado.")
