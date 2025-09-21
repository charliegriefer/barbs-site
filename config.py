"""
Configuration settings for the application
"""

import os

# Flask settings
DEBUG = True
TESTING = False
SECRET_KEY = os.environ.get("SECRET_KEY", "dev-key-for-testing")

# Cache settings
CACHE_TYPE = "SimpleCache"
CACHE_DEFAULT_TIMEOUT = 300

# Petstablished API settings
PETSTABLISHED_BASE_URL = os.environ.get(
    "PETSTABLISHED_BASE_URL", "https://petstablished.com/api/v2/public/pets"
)
PETSTABLISHED_PUBLIC_KEY = os.environ.get("PETSTABLISHED_PUBLIC_KEY", "demo-key")
