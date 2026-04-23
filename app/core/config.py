from os import getenv
from typing import Optional
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class Config:
    DATABASE_URL: str = getenv("DATABASE_URL") or ""
    A_DATABASE_URL: str = DATABASE_URL.replace("sqlite://", "sqlite+aiosqlite://")

config = Config()