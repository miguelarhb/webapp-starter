import os
from dotenv import load_dotenv
from backend.core.utils.logging import Logger

logger = Logger()

def load_env():

    try:
        # Load the main environment file
        load_dotenv()

        # Get the value of the ENVIRONMENT variable from the main environment file
        environment = os.getenv("ENVIRONMENT").lower()

        # Load the environment-specific environment file
        load_dotenv(f"environments/{environment}/.env")

    except Exception as e:
        logger.error(f"Error loading enviroment variables: {str(e)}")
        raise RuntimeError(f"Error loading enviroment variables.")