import redis
from config.redis_config import settings

redis_client = redis.Redis(
    host = settings.host,
    port = settings.port,
    db = settings.db,
    decode_responses=True
)

def test_connection():
    try:
        resposta = redis_client.ping()
        return f"Conectado: {resposta}"

    except redis.ConnectionError:
        return f"Não foi possível se conectar ao banco"