import hopsworks

# Inicializa a conexão com o Hopsworks
project = hopsworks.login()

# Obtém o feature store
fs = project.get_feature_store()

print("Feature Store inicializado com sucesso!") 