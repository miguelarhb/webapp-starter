import logging

class Logger():
    """
    A custom logger class that provides methods for logging at different levels.
    """

    def __init__(self) -> None:
        """
        Initialize the logger with the default logging level set to INFO.
        """
        try:
            self.logger = logging.getLogger()
            self.logger.setLevel(logging.INFO)
        except Exception as e:
            print(f"Error initializing logger: {str(e)}")

    def info(self, msg: str) -> None:
        """
        Log an informational message.
        
        Parameters:
            msg (str): The message to be logged.
        """
        self.logger.info(msg)

    def debug(self, msg: str) -> None:
        """
        Log a debug message.
        
        Parameters:
            msg (str): The message to be logged.
        """
        self.logger.debug(msg)

    def warning(self, msg: str) -> None:
        """
        Log a warning message.
        
        Parameters:
            msg (str): The message to be logged.
        """
        self.logger.warning(msg)

    def error(self, msg: str) -> None:
        """
        Log an error message.
        
        Parameters:
            msg (str): The message to be logged.
        """
        self.logger.error(msg)

    def critical(self, msg: str) -> None:
        """
        Log an critical message.
        
        Parameters:
            msg (str): The message to be logged.
        """
        self.logger.critical(msg)