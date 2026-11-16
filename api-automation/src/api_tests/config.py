"""Test settings. Override with environment variables, for example BASE_URL."""
import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    base_url: str
    timeout: float


settings = Settings(
    base_url=os.getenv("BASE_URL", "https://jsonplaceholder.typicode.com"),
    timeout=float(os.getenv("HTTP_TIMEOUT", "15")),
)
