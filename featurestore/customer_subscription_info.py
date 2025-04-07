import pandas as pd
import init_hopsworks

def create_customer_subscription_feature_group(subscriptions_df):
    """
    Cria o feature group para informações de assinatura do cliente
    
    Args:
        subscriptions_df (pd.DataFrame): DataFrame com as informações de assinatura do cliente
    """
    print("Criando feature group para informações de assinatura do cliente...")
    
    # Converte a coluna datetime para timestamp, removendo espaços em branco
    subscriptions_df['datetime'] = pd.to_datetime(subscriptions_df['datetime'].str.strip(), format='%Y-%m-%d')
    
    # Obtém o feature store já inicializado
    fs = init_hopsworks.fs_global
    
    # Cria o feature group
    subscriptions_fg = fs.get_or_create_feature_group(
        name="customer_subscription_info",
        version=1,
        description="Informações de assinatura do cliente para previsão de churn.",
        primary_key=['customerID'],
        event_time="datetime",
    )
    
    # Insere os dados
    subscriptions_fg.insert(subscriptions_df)
    
    # Atualiza as descrições das features
    feature_descriptions = [
        {"name": "customerid", "description": "Identificador único do cliente"}, 
        {"name": "deviceprotection", "description": "Indica se o cliente assinou o serviço de proteção de dispositivo"},
        {"name": "onlinebackup", "description": "Indica se o cliente assinou o serviço de backup online"}, 
        {"name": "onlinesecurity", "description": "Indica se o cliente assinou o serviço de segurança online"}, 
        {"name": "internetservice", "description": "Indica se o cliente assinou o serviço de internet"}, 
        {"name": "multiplelines", "description": "Indica se o cliente assinou o serviço de múltiplas linhas"}, 
        {"name": "phoneservice", "description": "Indica se o cliente assinou o serviço de telefone"}, 
        {"name": "techsupport", "description": "Indica se o cliente assinou o serviço de suporte técnico"}, 
        {"name": "streamingmovies", "description": "Indica se o cliente assinou o serviço de streaming de filmes"}, 
        {"name": "streamingtv", "description": "Indica se o cliente assinou o serviço de streaming de TV"},
        {"name": "datetime", "description": "Data em que as informações do cliente foram registradas"},
    ]
    
    for desc in feature_descriptions: 
        subscriptions_fg.update_feature_description(desc["name"], desc["description"])
    
    print("✅ Feature group 'customer_subscription_info' criado com sucesso!")

if __name__ == "__main__":
    # Carrega os dados processados
    subscriptions_df = pd.read_csv("../data/processed_customer_subscription.csv")
    create_customer_subscription_feature_group(subscriptions_df) 