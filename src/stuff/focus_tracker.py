import time

import pywinctl

from src.helpers.logger import CustomLogger

log_dir = "/tmp"

logger = CustomLogger(name="focus_tracker", to_file=True)

if __name__ == "__main__":
    while True:
        focused_window = pywinctl.getActiveWindow()
        if focused_window:
            logger.info(f"Active window: {focused_window.title}")

        time.sleep(2)
