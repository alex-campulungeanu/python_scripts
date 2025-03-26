import logging
import sys

file_location = "/tmp"


class CustomLogger:
    def __init__(
        self,
        name: str = "MyLogger",
        to_file: bool = False,
        log_file: str = f"{file_location}/python_scripts.log",
        level=logging.INFO,
    ) -> None:
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        self.logger.handlers.clear()

        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(self._get_formatter())
        self.logger.addHandler(console_handler)

        if to_file:
            file_handler = logging.FileHandler(log_file)
            file_handler.setFormatter(self._get_formatter())
            self.logger.addHandler(file_handler)

    def _get_formatter(self):
        return logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)

    def critical(self, msg):
        self.logger.critical(msg)
