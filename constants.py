BOOTSTRAPSERVER = "127.0.0.1:9092"
SCHEMA_REGISTRY_URL = "http://127.0.0.1:8081"
CLIENTID = "twitch-producer"
ACKS = 1
KAFKA_CONFIG = {
    "bootstrap.servers": BOOTSTRAPSERVER,
    "acks": ACKS,
}
