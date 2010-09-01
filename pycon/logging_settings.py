from jogging.handlers import DatabaseHandler
from logging import StreamHandler
import logging


LOGGING = {
    'pycon.core': {
        'handler': DatabaseHandler(),
        'level': logging.INFO,
    },
}