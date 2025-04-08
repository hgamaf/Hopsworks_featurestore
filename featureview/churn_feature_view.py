#ignore warnings
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from featurestore.init_hopsworks import fs_global
from hopsworks.hsfs.builtin_transformations import min_max_scaler
from hsfs.transformation_function import TransformationFunction

import warnings
import logging
import pandas as pd

# Configuração do logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)
warnings.filterwarnings('ignore')

def custom_label_encoder(value):
    """
    Função personalizada para label encoding que lida com valores nulos.
    Retorna -1 para valores nulos.
    """
    if value is None or pd.isna(value):
        return -1
    return value

try:
    logger.info("Obtendo Feature Store...")
    fs = fs_global
    logger.info("Feature Store obtido com sucesso")

    # Retrieve feature groups
    logger.info("Obtendo feature groups...")
    customer_info_fg = fs.get_feature_group(
        name="customer_info",
        version=1,
    )
    logger.info("Feature group 'customer_info' obtido com sucesso")

    demography_fg = fs.get_feature_group(
        name="customer_demography_info",
        version=1,
    )
    logger.info("Feature group 'customer_demography_info' obtido com sucesso")

    subscriptions_fg = fs.get_feature_group(
        name="customer_subscription_info",
        version=1,
    )
    logger.info("Feature group 'customer_subscription_info' obtido com sucesso")

    # Select features for training data
    logger.info("Selecionando features para o conjunto de treinamento...")
    selected_features = customer_info_fg.select_features() \
        .join(demography_fg.select_features()) \
        .join(subscriptions_fg.select_all(include_event_time=False))
    logger.info("Features selecionadas com sucesso")

    # Define lists of numerical and categorical features
    numerical_features = ["tenure", "monthlycharges", "totalcharges"]
    categorical_features = [
        "multiplelines", "internetservice", "onlinesecurity", "onlinebackup",
        "deviceprotection", "techsupport", "streamingmovies", "streamingtv",
        "phoneservice", "paperlessbilling", "contract", "paymentmethod", "gender", 
        "dependents", "partner",
    ]

    logger.info(f"Features numéricas definidas: {numerical_features}")
    logger.info(f"Features categóricas definidas: {categorical_features}")

    # Map features to their corresponding transformation functions
    transformation_functions = []

    # For numerical features, use the min_max_scaler transformation
    logger.info("Aplicando transformação min_max_scaler para features numéricas...")
    for feature in numerical_features:
        transformation_functions.append(min_max_scaler(feature))
        logger.debug(f"Transformação min_max_scaler aplicada para {feature}")

    # For categorical features, use our custom label encoder
    logger.info("Aplicando transformação label_encoder para features categóricas...")
    for feature in categorical_features:
        # Cria uma função de transformação personalizada
        tf = TransformationFunction(
            name=f"custom_label_encoder_{feature}",
            transformation_fn=custom_label_encoder,
            output_type="int",
        )
        transformation_functions.append(tf)
        logger.debug(f"Transformação label_encoder aplicada para {feature}")

    # Get or create the 'churn_feature_view'
    logger.info("Criando/obtendo feature view 'churn_feature_view'...")
    feature_view = fs.get_or_create_feature_view(
        name='churn_feature_view',
        version=1,
        labels=["churn"],
        transformation_functions=transformation_functions,
        query=selected_features,
    )
    logger.info("Feature view criada/obtida com sucesso")

except Exception as e:
    logger.error(f"Erro durante a execução do script: {str(e)}", exc_info=True)
    raise 