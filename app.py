import os
import platform
import time

from flask import Flask
from redis import Redis
from redis.exceptions import ConnectionError

app = Flask(__name__)

# Configuration: Get Redis address from environment variable
# Fallback to 'localhost' if not set
redis_host = os.environ.get("REDIS_HOST", "localhost")
cache = Redis(host=redis_host, port=6379)


# Function to attempt database connection with retry mechanism
def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr("hits")
        # Using the explicitly imported ConnectionError
        except ConnectionError:
            if retries == 0:
                return None  # Return None if database is unreachable
            retries -= 1
            time.sleep(0.5)


@app.route("/")
def hello():
    count = get_hit_count()

    # Get the hostname (container ID or machine name)
    host_name = platform.node()

    if count is None:
        return f"Hello! Host: {host_name}. \nERROR: Cannot connect to Redis.\n"

    return f"Hello! Host: {host_name}. \nYou have been here {count} times.\n"


if __name__ == "__main__":
    # Run the server accessible to everyone (0.0.0.0)
    app.run(host="0.0.0.0", port=8080, debug=True)
