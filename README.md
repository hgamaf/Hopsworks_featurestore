# Hopsworks Feature Store

Este projeto implementa um Feature Store utilizando o Hopsworks para armazenar e gerenciar features de clientes para previsão de churn.

## 🛠️ Tecnologias Utilizadas

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Hopsworks](https://img.shields.io/badge/Hopsworks-00A98F?style=for-the-badge&logo=hopsworks&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![PyArrow](https://img.shields.io/badge/PyArrow-FF4B4B?style=for-the-badge&logo=apachearrow&logoColor=white)
![Python-dotenv](https://img.shields.io/badge/python--dotenv-000000?style=for-the-badge&logo=python&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-FF6B00?style=for-the-badge&logo=xgboost&logoColor=white)
![MLflow](https://img.shields.io/badge/MLflow-0194E2?style=for-the-badge&logo=mlflow&logoColor=white)

## 📋 Pré-requisitos

- Python 3.11.0
- pip
- Conta no Hopsworks
- API Key do Hopsworks

## 🔧 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/hopsworks_featurestore.git
cd hopsworks_featurestore
```

2. Crie um ambiente virtual:
```bash
python -m venv .venv
source .venv/bin/activate  # No Windows: .venv\Scripts\activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
pip install -U 'hopsworks[python]' --quiet
```

4. Configure as variáveis de ambiente:
```bash
cp .env.example .env
```
Edite o arquivo `.env` com suas credenciais do Hopsworks.

## 📊 Estrutura do Projeto

```
Hopsworks_featurestore/
├── data/
│   ├── processed_customer_info.csv
│   ├── processed_customer_demography.csv
│   └── processed_customer_subscription.csv
├── featurestore/
│   ├── __init__.py
│   ├── init_hopsworks.py
│   ├── customer_info.py
│   ├── customer_demography_info.py
│   └── customer_subscription_info.py
├── featureview/
│   └── churn_feature_view.py
├── model/
│   └── training_pipeline.py
├── eda/
│   └── churn_eda.py
├── .env
├── .gitignore
├── README.md
└── requirements.txt
```

## 🔄 Fluxo da Solução

```mermaid
graph TB
    A[init_hopsworks.py] -->|Inicializa conexão| B[customer_info.py]
    B -->|Carrega dados| C[processed_customer_info.csv]
    C -->|Cria Feature Group| D[Feature Store]
    
    A -->|Inicializa conexão| E[customer_demography_info.py]
    E -->|Carrega dados| F[processed_customer_demography.csv]
    F -->|Cria Feature Group| D
    
    A -->|Inicializa conexão| G[customer_subscription_info.py]
    G -->|Carrega dados| H[processed_customer_subscription.csv]
    H -->|Cria Feature Group| D
    
    D -->|Combina Feature Groups| I[churn_feature_view.py]
    I -->|Cria Feature View| J[Feature View]
    J -->|Análise Exploratória| K[churn_eda.py]
    K -->|Gera Insights| L[Relatório EDA]
    L -->|Treina Modelo| M[training_pipeline.py]
```

## 📝 Descrição dos Scripts

### init_hopsworks.py
- Responsável por inicializar a conexão com o Hopsworks
- Carrega as variáveis de ambiente do arquivo .env
- Autentica com a API Key do Hopsworks
- Retorna o objeto do Feature Store

### customer_info.py
- Cria o feature group para informações básicas do cliente
- Inclui features como:
  - customerID (chave primária)
  - contract
  - tenure
  - paymentmethod
  - paperlessbilling
  - monthlycharges
  - totalcharges
  - churn
  - datetime

### customer_demography_info.py
- Cria o feature group para informações demográficas do cliente
- Inclui features como:
  - customerID (chave primária)
  - gender
  - seniorcitizen
  - dependents
  - partner

### customer_subscription_info.py
- Cria o feature group para informações de assinatura do cliente
- Inclui features como:
  - customerID (chave primária)
  - deviceprotection
  - onlinebackup
  - onlinesecurity
  - internetservice
  - multiplelines
  - phoneservice
  - techsupport
  - streamingmovies
  - streamingtv
  - datetime

### churn_feature_view.py
- Combina os três feature groups em uma única feature view
- Aplica transformações nas features:
  - Normalização (min-max) para features numéricas
  - Label encoding para features categóricas
- Define a variável target (churn)

### training_pipeline.py
- Utiliza a feature view para treinar o modelo
- Implementa o pipeline de treinamento com MLflow
- Registra métricas e artefatos
- Versiona o modelo

### churn_eda.py
- Realiza análise exploratória dos dados da feature view de churn
- Mostra informações gerais sobre o dataset
- Mostra detalhes sobre valores nulos e estatísticas descritivas
- Mostra distribuição de variáveis categóricas

## 🚀 Como Usar

1. Execute o script de inicialização:
```bash
python featurestore/init_hopsworks.py
```

2. Crie os feature groups:
```bash
python featurestore/customer_info.py
python featurestore/customer_demography_info.py
python featurestore/customer_subscription_info.py
```

3. Crie a feature view:
```bash
python featureview/churn_feature_view.py
```

4. Realize análise exploratória dos dados:
```bash
python eda/churn_eda.py
```

5. Treine o modelo:
```bash
python model/training_pipeline.py
```

## 📚 Referências

- [Documentação do Hopsworks](https://docs.hopsworks.ai/)
- [Documentação do Python Feature Store](https://docs.hopsworks.ai/3.0/user_guides/fs/feature_group/python/)
- [Documentação do MLflow](https://mlflow.org/docs/latest/index.html)