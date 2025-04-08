import hopsworks
from dotenv import load_dotenv
import os
import pandas as pd
import numpy as np

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Conecta ao Hopsworks usando a chave do .env
project = hopsworks.login(api_key_value=os.getenv('HOPSWORKS_API_KEY'))
fs = project.get_feature_store(name='mlops_project01_featurestore')

# Obtém os feature groups
customer_info = fs.get_feature_group(name="customer_info", version=1)
demography_info = fs.get_feature_group(name="customer_demography_info", version=1)
subscription_info = fs.get_feature_group(name="customer_subscription_info", version=1)

# Cria a query usando os feature groups
query = customer_info.select_all() \
    .join(demography_info.select_all()) \
    .join(subscription_info.select_all())

# Executa a query e obtém os dados em um DataFrame
df = query.read()
print(f"\nShape do DataFrame: {df.shape}")

# Análise detalhada dos dados
print("\n=== ANÁLISE DETALHADA DOS DADOS ===")
print("\n1. Informações Gerais:")
print(df.info())

print("\n2. Valores Nulos:")
null_counts = df.isnull().sum()
null_percentages = (null_counts / len(df)) * 100
null_info = pd.DataFrame({
    'Valores Nulos': null_counts,
    'Percentual Nulos (%)': null_percentages.round(2)
})
print(null_info)

print("\n3. Estatísticas Descritivas para Variáveis Numéricas:")
print(df.describe())

print("\n4. Contagem de Valores Únicos para Variáveis Categóricas:")
categorical_cols = df.select_dtypes(include=['object']).columns
for col in categorical_cols:
    print(f"\n{col}:")
    print(df[col].value_counts()) 