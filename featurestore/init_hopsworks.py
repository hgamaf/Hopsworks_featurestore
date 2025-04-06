import hopsworks
import os
from dotenv import load_dotenv

print("Iniciando conexão com o Hopsworks...")

# Carrega as variáveis de ambiente do arquivo .env
print("\nCarregando variáveis de ambiente do arquivo .env...")
load_dotenv()

# Obtém a API key do ambiente
api_key = os.getenv('HOPSWORKS_API_KEY')

# Verifica se o arquivo .env foi carregado corretamente
if api_key:
    print("✅ Arquivo .env encontrado e carregado com sucesso")
    print(f"📋 Variáveis encontradas no .env:")
    for key in os.environ:
        if key.startswith('HOPSWORKS_'):
            value = os.environ[key]
            if 'KEY' in key:
                print(f"   - {key}: {'*' * len(value)}")  # Esconde a chave
            else:
                print(f"   - {key}: {value}")
else:
    print("❌ Erro: API key não encontrada no arquivo .env")
    exit(1)

print("\nIniciando conexão com o Hopsworks...")
# Inicializa a conexão com o Hopsworks
project = hopsworks.login(
    api_key_value=api_key
)

# Obtém o feature store
fs = project.get_feature_store()

print("\n✅ Feature Store inicializado com sucesso!")
print(f"📊 Projeto: {project.name}")

# Expor o fs como uma variável global para que possa ser importado por outros módulos
fs_global = fs