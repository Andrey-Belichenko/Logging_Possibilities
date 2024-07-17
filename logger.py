import logging
import sys


def stdout_logging(datefmt: str, strfmt: str, logger_name: str):
    # создаем регистратор
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)

    handler = logging.StreamHandler(sys.stdout)

    # создаем форматтер
    formatter = logging.Formatter(fmt=strfmt, datefmt=datefmt)
    # добавляем форматтер к 'ch'
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    logger.debug("DEBUG logging to stdout")
    logger.info("INFO logging to stdout")
    logger.warning("WARNING logging to stdout")
    logger.error("ERROR logging to stdout")
    logger.critical("CRITICAL logging to stdout")


def stderr_logging(datefmt: str, strfmt: str, logger_name: str):
    # создаем регистратор
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)

    handler = logging.StreamHandler()

    # создаем форматтер
    formatter = logging.Formatter(fmt=strfmt, datefmt=datefmt)
    # добавляем форматтер к 'ch'
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    logger.debug("DEBUG logging to stderr")
    logger.info("INFO logging to stderr")
    logger.warning("WARNING logging to stderr")
    logger.error("ERROR logging to stderr")
    logger.critical("CRITICAL logging to stderr")


def file_logging(datefmt: str, strfmt: str,  logger_name: str):
    # создаем регистратор
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)

    handler = logging.FileHandler('py_log.log')
    handler.setLevel(logging.DEBUG)

    # создаем форматтер
    formatter = logging.Formatter(fmt=strfmt, datefmt=datefmt)
    # добавляем форматтер к 'ch'
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    logger.debug("DEBUG logging to file")
    logger.info("INFO logging to file")
    logger.warning("WARNING logging to file")
    logger.error("ERROR logging to file")
    logger.critical("CRITICAL logging to file")


def main():
    file_logging('%Y-%m-%d %H:%M:%S',
                 '[%(asctime)s] > %(message)s',
                 "logger_to_file_1")

    file_logging('%Y-%m-%d %H:%M:%S',
                 '[%(asctime)s.%(msecs)03d] [%(levelname)s] [%(name)s] [%(funcName)s] > %(message)s',
                 'logger_to_file_2')

    stderr_logging('%Y-%m-%d %H:%M:%S',
                   '[%(asctime)s] > %(message)s',
                   "logger_to_stderr_1")

    stderr_logging('%Y-%m-%d %H:%M:%S',
                   '[%(asctime)s.%(msecs)03d] [%(levelname)s] [%(name)s] [%(funcName)s] > %(message)s',
                   "logger_to_stderr_2")

    stdout_logging('%Y-%m-%d %H:%M:%S',
                   '[%(asctime)s] > %(message)s',
                   "logger_to_stdout_1")

    stdout_logging('%Y-%m-%d %H:%M:%S',
                   '[%(asctime)s.%(msecs)03d] [%(levelname)s] [%(name)s] [%(funcName)s] > %(message)s',
                   "logger_to_stdout_2")


if __name__ == '__main__':
    main()
