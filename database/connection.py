import redis
from redis.backoff import NoBackoff
from redis.retry import Retry
from config.redis_config import settings

no_retry = Retry(NoBackoff(), retries=0)

redis_client = redis.Redis(
    host=settings.host,
    port=settings.port,
    db=settings.db,
    password=settings.password,
    decode_responses=True,
    socket_connect_timeout=2, 
    socket_timeout=2,         
    retry=no_retry,
    retry_on_error=[]
)

def test_connection():
    try:
        resposta = redis_client.ping()
        return f"Conectado: {resposta}"
    
    except (redis.ConnectionError, redis.TimeoutError) as e:
        return f"Erro de conexão com o servidor Redis (Tempo de Resposta Esgotado/Falha na Conexão): {e}"

    except Exception as e:
        return f"Erro generico: {e}"
