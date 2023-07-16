import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

DATABASE_CONFIG = {
    "connections": {"default": DATABASE_URL},
    "apps": {
        "models": {
            "models": ["aerich.models", "models"],
            "default_connection": "default",
        }
    },
}
