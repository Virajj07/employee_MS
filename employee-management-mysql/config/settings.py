import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Database configuration
DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASSWORD', ''),
    'database': os.getenv('DB_NAME', 'employee_management'),
    'port': int(os.getenv('DB_PORT', 3306))
}

# Application settings
APP_CONFIG = {
    'debug': os.getenv('DEBUG', 'False').lower() == 'true'
}