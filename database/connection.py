import redis

redis_client = redis.Redis(
    host='localhost',
    port=6379,
    db=0,
    decode_responses=True
)

def test_connection():
    try:
        resposta = redis_client.ping()
        return f"Conectado: {resposta}"

    except redis.ConnectionError:
        return f"Não foi possível se conectar ao banco"