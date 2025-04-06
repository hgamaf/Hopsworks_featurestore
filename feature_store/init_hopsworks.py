import hopsworks
import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Obtém a API key do ambiente
api_key = os.getenv('HOPSWORKS_API_KEY')

# Inicializa a conexão com o Hopsworks
project = hopsworks.login(
    api_key_value=api_key
)

# Obtém o feature store
fs = project.get_feature_store()

print("Feature Store inicializado com sucesso!") 