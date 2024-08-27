# Nome do Projeto

Este projeto visa demonstrar a utilização de teste de carga e performance em apis, mensagerias fix server e utilizando selenium para testes de usuarios mais robusto

## Implementações realizadas

1. **Teste de Carga em APIs**
    - Utiliza o Locust para simular alta carga em APIs, como `example.com`.
2. **Teste de Capacidade em APIs**
    - Avalia a capacidade de resposta e escalabilidade das APIs.
3. **Teste de Interação do Usuário**
    - Utiliza o Selenium para simular interações de usuário e validar o comportamento da aplicação.


## Conhecendo Estrutura do projeto


```
my_project/
│
├── common/
│   ├── __init__.py
│   ├── auth.py
│   └── config.py
│
├── my_locustfiles/
│   ├── __init__.py
│   ├── api.py
│   ├── website.py
│   └── locustfile.py
│
├── tests/
│   ├── __init__.py
│   └── test_example.py
│
├── logs/
│   └── (Os logs estão aqui após execução)
│
├── requirements.txt
├── README.md
└── setup.py
```

# Instalação e Uso

## Instalação de Dependências

Instruções para instalar as dependências do projeto:

```bash
cd portfolios_testes
python -m venv ex_env
source ex_env/bin/activate # Version Linux/Bash
source ex_env\Scripts\activate # Version Prompt cmd
source ex_env/Scripts/activate # Version Git Bash Windows
pip install -r requirements.txt
```

## Como Usar

Instruções sobre como usar o projeto:

```bash 
cd portfolios_testes
locust -f my_locustfiles/locustfile.py 
```

## Contribuindo

Se você deseja contribuir para este projeto, por favor, siga estas etapas:

1. Faça um fork do repositório.
2. Crie uma branch para sua feature ou correção.
3. Faça as alterações e adicione commits com mensagens claras.
4. Envie um pull request para revisão.

## Licença
Informações sobre a licença do projeto.