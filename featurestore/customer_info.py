import pandas as pd
import init_hopsworks

def create_customer_info_feature_group(customer_info_df):
    """
    Cria o feature group para informações do cliente
    
    Args:
        customer_info_df (pd.DataFrame): DataFrame com as informações do cliente
    """
    print("Criando feature group para informações do cliente...")
    
    # Converte a coluna datetime para timestamp
    customer_info_df['datetime'] = pd.to_datetime(customer_info_df['datetime'])
    
    # Obtém o feature store já inicializado
    fs = init_hopsworks.fs_global
    
    # Cria o feature group
    customer_info_fg = fs.get_or_create_feature_group(
        name="customer_info",
        version=1,
        description="Informações do cliente para previsão de churn.",
        primary_key=['customerID'],
        event_time="datetime",
    )
    
    # Insere os dados
    customer_info_fg.insert(customer_info_df)
    
    # Atualiza as descrições das features
    feature_descriptions = [
        {"name": "customerid", "description": "Identificador único do cliente"}, 
        {"name": "contract", "description": "Tipo de contrato do cliente"}, 
        {"name": "tenure", "description": "Tempo que o cliente está conosco (em meses)"}, 
        {"name": "paymentmethod", "description": "Método de pagamento utilizado pelo cliente"}, 
        {"name": "paperlessbilling", "description": "Indica se o cliente optou por faturamento sem papel"}, 
        {"name": "monthlycharges", "description": "Valor cobrado mensalmente do cliente"},
        {"name": "totalcharges", "description": "Valor total cobrado do cliente"},
        {"name": "churn", "description": "Indica se o cliente cancelou o serviço no último mês"},
        {"name": "datetime", "description": "Data em que as informações do cliente foram registradas"},
    ]
    
    for desc in feature_descriptions: 
        customer_info_fg.update_feature_description(desc["name"], desc["description"])
    
    print("✅ Feature group 'customer_info' criado com sucesso!")

if __name__ == "__main__":
    # Carrega os dados processados
    customer_info_df = pd.read_csv("../data/processed_customer_info.csv")
    create_customer_info_feature_group(customer_info_df) 