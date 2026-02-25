import os
import platform
import time

import redis
from flask import Flask

app = Flask(__name__)

# Konfiguracja: Pobieramy adres Redisa ze zmiennej środowiskowej
# Jeśli zmienna nie istnieje (np. lokalnie), używamy 'localhost'
redis_host = os.environ.get("REDIS_HOST", "localhost")
cache = redis.Redis(host=redis_host, port=6379)


# Funkcja próbująca połączyć się z bazą (z mechanizmem ponawiania prób)
def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr("hits")
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                return None  # Zwracamy None jeśli baza nie działa
            retries -= 1
            time.sleep(0.5)


@app.route("/")
def hello():
    count = get_hit_count()

    # Pobieramy nazwę komputera/kontenera
    host_name = platform.node()

    if count is None:
        return f"Witaj! Host: {host_name}. \nBŁĄD: Nie można połączyć się z Redisem.\n"

    return f"Witaj! Host: {host_name}. \nOdwiedziłeś nas {count} razy.\n"


if __name__ == "__main__":
    # Uruchamiamy serwer dostępny dla wszystkich (0.0.0.0)
    app.run(host="0.0.0.0", port=8080, debug=True)
