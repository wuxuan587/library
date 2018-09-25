import os
import logging
import logging.handlers
from django.conf import settings

LOG_LEVEL_MAP = {
    'debug': logging.DEBUG,
    'info': logging.INFO,
    'warning': logging.WARN,
    'error': logging.ERROR,
    'critical': logging.CRITICAL
}

LOG_FILE_MAX_BYTES = 1024 * 1024 * 32


def yet_another_set_log(level, filename):
    log_file = os.path.join(settings.LOG_DIR, filename)
    if not os.path.isfile(log_file):
        try:
            os.mknod(log_file, 0666)
        except:
            # macos call mknod make exception
            open(log_file, 'w').close()
            os.chmod(log_file, 0666)

    logger_f = logging.getLogger(filename)
    logger_f.setLevel(logging.DEBUG)

    fh = logging.handlers.TimedRotatingFileHandler(
        log_file, 'W0', backupCount=10)
    fh.setLevel(LOG_LEVEL_MAP.get(level, logging.DEBUG))
    formatter = logging.Formatter(
        '''
        %(asctime)s %(pathname)s %(filename)s %(funcName)s %(lineno)s %(levelname)s - %(message)s
        ''', '%Y-%m-%d %H:%M:%S'
    )
    fh.setFormatter(formatter)

    logger_f.addHandler(fh)
    return logger_f


def set_log(level, filename, maxBytes=LOG_FILE_MAX_BYTES, backupCount=10):
    log_file = os.path.join(settings.LOG_DIR, filename)
    if not os.path.isfile(log_file):
        try:
            os.mknod(log_file, 0666)
        except:
            # macos call mknod make excetion
            open(log_file, 'w').close()
            os.chmod(log_file, 0666)

    logger_f = logging.getLogger(filename)
    logger_f.setLevel(logging.DEBUG)

    fh = logging.handlers.RotatingFileHandler(
        log_file, maxBytes=maxBytes, backupCount=backupCount)
    fh.setLevel(LOG_LEVEL_MAP.get(level, logging.DEBUG))
    formatter = logging.Formatter(
        '%(asctime)s - %(filename)s - %(lineno)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)

    logger_f.addHandler(fh)
    return logger_f


logger_for_wxapp_view = set_log('debug', 'wxapp_view.log')

