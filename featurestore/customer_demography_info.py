import pandas as pd
import init_hopsworks

def create_customer_demography_feature_group(demography_df):
    """
    Cria o feature group para informações demográficas do cliente
    
    Args:
        demography_df (pd.DataFrame): DataFrame com as informações demográficas do cliente
    """
    print("Criando feature group para informações demográficas do cliente...")
    
    # Obtém o feature store já inicializado
    fs = init_hopsworks.fs_global
    
    # Cria o feature group
    demography_fg = fs.get_or_create_feature_group(
        name="customer_demography_info",
        version=1,
        description="Informações demográficas do cliente para previsão de churn.",
        primary_key=['customerID'],
    )
    
    # Insere os dados
    demography_fg.insert(demography_df)
    
    # Atualiza as descrições das features
    feature_descriptions = [
        {"name": "customerid", "description": "Identificador único do cliente"}, 
        {"name": "gender", "description": "Gênero do cliente"},
        {"name": "seniorcitizen", "description": "Indica se o cliente é idoso ou não"}, 
        {"name": "dependents", "description": "Indica se o cliente tem dependentes ou não"}, 
        {"name": "partner", "description": "Indica se o cliente tem parceiro ou não"}, 
    ]
    
    for desc in feature_descriptions: 
        demography_fg.update_feature_description(desc["name"], desc["description"])
    
    print("✅ Feature group 'customer_demography_info' criado com sucesso!")

if __name__ == "__main__":
    # Carrega os dados processados
    demography_df = pd.read_csv("../data/processed_customer_demography.csv")
    create_customer_demography_feature_group(demography_df) 