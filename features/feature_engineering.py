import pandas as pd

def process_customer_info(customer_info_df):
    """
    Processa o DataFrame de informações do cliente realizando as seguintes transformações:
    1. Converte a coluna TotalCharges para numérico
    2. Preenche valores NaN em TotalCharges com 0
    3. Converte a coluna Churn para 0/1
    
    Args:
        customer_info_df (pd.DataFrame): DataFrame com as informações do cliente
        
    Returns:
        pd.DataFrame: DataFrame processado
    """
    # Convert the "TotalCharges" column to numeric, treating errors as NaN
    customer_info_df["TotalCharges"] = pd.to_numeric(
        customer_info_df["TotalCharges"], 
        errors='coerce',
    )

    # Replace NaN values in the "TotalCharges" column with 0
    customer_info_df["TotalCharges"].fillna(0, inplace=True)

    # Replace values in the "Churn" column with 0 for "No" and 1 for "Yes"
    customer_info_df["Churn"].replace({"No": 0, "Yes": 1}, inplace=True)
    
    return customer_info_df

if __name__ == "__main__":
    # Carregar os dados
    customer_info_df = pd.read_csv("../data/customer_info.csv")
    
    # Processar os dados
    processed_df = process_customer_info(customer_info_df)
    
    # Salvar o resultado
    processed_df.to_csv("../data/processed_customer_info.csv", index=False)
    print("Dados processados salvos em data/processed_customer_info.csv") 