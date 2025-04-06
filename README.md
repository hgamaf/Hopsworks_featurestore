# Hopsworks Feature Store

Projeto para implementação de Feature Store utilizando o Hopsworks.

## 🛠️ Tecnologias

[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/downloads/release/python-3120/)
[![Hopsworks](https://img.shields.io/badge/Hopsworks-4.2.0-orange.svg)](https://www.hopsworks.ai/)
[![Pandas](https://img.shields.io/badge/Pandas-2.1.4-green.svg)](https://pandas.pydata.org/)
[![PyArrow](https://img.shields.io/badge/PyArrow-19.0.1-red.svg)](https://arrow.apache.org/docs/python/)
[![Python-dotenv](https://img.shields.io/badge/python--dotenv-1.1.0-yellow.svg)](https://pypi.org/project/python-dotenv/)

## 📁 Estrutura do Projeto

```
Hopsworks_featurestore/
├── data/                    # Dados do projeto
│   ├── processed_customer_info.csv
│   └── scripts/            # Scripts de processamento de dados
├── feature_store/          # Configuração do Feature Store
│   ├── feature_groups/     # Feature Groups
│   │   └── customer_info.py
│   └── init_hopsworks.py   # Inicialização do Hopsworks
├── features/               # Features do projeto
│   └── feature_engineering.py
├── .env                    # Variáveis de ambiente
├── .gitignore             # Arquivos ignorados pelo Git
├── pyproject.toml         # Dependências do projeto
└── README.md              # Documentação
```

## 🚀 Como Usar

1. Instale as dependências:
```bash
# Instalar o Hopsworks com todas as dependências necessárias
pip install -U 'hopsworks[python]' --quiet

# Instalar outras dependências do projeto
pip install -e .
```

2. Configure as variáveis de ambiente no arquivo `.env`:
```env
HOPSWORKS_API_KEY=sua_api_key_aqui
```

3. Execute os scripts na ordem:
```bash
# Processar dados
python features/feature_engineering.py

# Inicializar Feature Store
python feature_store/init_hopsworks.py

# Criar Feature Groups
python feature_store/feature_groups/customer_info.py
```