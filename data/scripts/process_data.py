import pandas as pd
import os

# Criar diretório data se não existir
os.makedirs('../', exist_ok=True)

# Read demography data
demography_df = pd.read_csv("https://repo.hops.works/dev/davit/churn/demography.csv")
demography_df.to_csv('../demography.csv', index=False)
print("Dados demográficos salvos em data/demography.csv")

# Read customer info data with datetime parsing
customer_info_df = pd.read_csv(
    "https://repo.hops.works/dev/davit/churn/customer_info.csv",
    parse_dates=['datetime'],
)
customer_info_df.to_csv('../customer_info.csv', index=False)
print("Dados de informações do cliente salvos em data/customer_info.csv")

# Read subscriptions data with datetime parsing
subscriptions_df = pd.read_csv(
    "https://repo.hops.works/dev/davit/churn/subscriptions.csv",
    parse_dates=['datetime'],
)
subscriptions_df.to_csv('../subscriptions.csv', index=False)
print("Dados de assinaturas salvos em data/subscriptions.csv")

# Exibir informações básicas dos dataframes
print("\nInformações dos DataFrames:")
print("\nDemography DataFrame:")
print(demography_df.info())
print("\nCustomer Info DataFrame:")
print(customer_info_df.info())
print("\nSubscriptions DataFrame:")
print(subscriptions_df.info()) 