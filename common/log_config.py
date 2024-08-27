import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logging():
    # Configura o caminho para o arquivo de log
    log_file = os.path.join(os.path.dirname(__file__), 'logs', 'application.log')
    
    # Cria o diretório de logs se não existir
    if not os.path.exists(os.path.dirname(log_file)):
        os.makedirs(os.path.dirname(log_file))
    
    # Configura o logging
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Configura o RotatingFileHandler
    handler = RotatingFileHandler(
        log_file, maxBytes=5*1024*1024, backupCount=5  # 5 MB por arquivo de log, mantendo 5 arquivos antigos
    )
    handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

    logger.addHandler(handler)

# Chama a configuração de logging
setup_logging()
