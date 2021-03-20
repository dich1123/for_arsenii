import logging  # все операции через этот модуль
import logging.config

# logging.error('HELLO ERTA')
# logging.warning('BEWARE OF ERTA!')

logger123 = logging.getLogger('kek')  # это инициализация логера.
# аргумент - это строка(имя логера)
logger.level = 40  # задать нашему логеру уровень 40 (ERROR)
logger2 = logging.getLogger('kek')  # когда мы создали логер(по имени),
# то сколько б раз мы не вызывали getLogger с этим именем, у
# нас будет возвращаться один и тот же объект(логер)
logger.level = 10
logger.setLevel('DEBUG')  # задать нашему логеру уровень 10 (DEBUG)


def create_list():
    data = [x for x in range(15)]
    logger.debug('List created')
    return data


# logger.error('12312231')
# logging.basicConfig(level='DEBUG', format='Level: %(levelname)s Time: %(asctime)s Process: %(process)d Thread: %(threadName)s Logger: %(name)s Path: %(module)s:%(lineno)d Function :%(funcName)s Message: %(message)s')
# create_list()


sett = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
      "brief": {
        "class": "logging.Formatter",
        "datefmt": "%I:%M:%S",
        "format": "%(l2evelname)-8s; %(name)-15s; %(message)s"
      },
      "single-line": {
        "class": "logging.Formatter",
        "datefmt": "%I:%M:%S",
        "format": "%(levelname)-8s; %(asctime)s; %(name)-15s; %(module)s:%(funcName)s;%(lineno)d: %(message)s"
      },
      "multi-process": {
        "class": "logging.Formatter",
        "datefmt": "%I:%M:%S",
        "format": "%(levelname)-8s; [%(process)d]; %(name)-15s; %(module)s:%(funcName)s;%(lineno)d: %(message)s"
      },
      "multi-thread": {
        "class": "logging.Formatter",
        "datefmt": "%I:%M:%S",
        "format": "%(levelname)-8s; %(threadName)s; %(name)-15s; %(module)s:%(funcName)s;%(lineno)d: %(message)s"
      },
      "verbose": {
        "class": "logging.Formatter",
        "datefmt": "%I:%M:%S",
        "format": "%(levelname)-8s; [%(process)d]; %(threadName)s; %(name)-15s; %(module)s:%(funcName)s;%(lineno)d: %(message)s"
      },
      "multiline": {
        "class": "logging.Formatter",
        "format": "Level: %(levelname)s\nTime: %(asctime)s\nProcess: %(process)d\nThread: %(threadName)s\nLogger: %(name)s\nPath: %(module)s:%(lineno)d\nFunction :%(funcName)s\nMessage: %(message)s\n"
      }
    },
    "handlers": {
      "console": {
        "level": "DEBUG",
        "class": "logging.StreamHandler123",
        "formatter": "single-line",
        "stream" : "ext://sys.stdout"
      },
      "console2": {
        "level": "DEBUG",
        "class": "logging.StreamHandler",
        "formatter": "multi-thread",
        "stream" : "ext://sys.stdout"
      },
      "smtp": {
        "level": "ERROR",
        "class": "logging.handlers.SMTPHandler",
        "formatter": "multiline",
        "mailhost": ["127.0.0.1", 60025],
        "fromaddr": "sender@example.com",
        "toaddrs": ["recipient@example.com"],
        "subject": "Something went wrong"
      }
    },
    "loggers": {
      "main_kek": {
        "handlers": ["console"],
        "propagate": False  # что не нужно распространять на другие логеры
      }
    },
    "root": {
      "handlers": ["console2", "smtp"],
      "level": "DEBUG",
    }
  }


logging.config.dictConfig(sett)
# logger_kek = logging.getLogger('main_kek')

# logger_kek.propagate = False
# logger_kek.debug('ITS ALIVE')
log = logging.getLogger(__name__)
log.debug('abc')





