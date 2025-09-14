import logging

class LogGen:
    @staticmethod
    def loggen():
        logger = logging.getLogger("selenium")
        logger.setLevel(logging.INFO)

        if not logger.handlers:   # Prevent adding multiple handlers
            fh = logging.FileHandler(".\\Logs\\automation.log")  # your log file path
            formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
            fh.setFormatter(formatter)
            logger.addHandler(fh)

            sh = logging.StreamHandler()
            sh.setFormatter(formatter)
            logger.addHandler(sh)

        return logger