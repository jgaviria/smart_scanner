#!/usr/bin/env python

import logging.config
import sys

from src.app import MainApp
from src.conf import settings


logging.config.dictConfig(settings.LOGGING)
logger = logging.getLogger(__name__)


def main(args=None):
    try:
        if not args:
            args = sys.argv

        MainApp().run()

        return 0
    except Exception as err:
        logger.error(str(err))


if __name__ == '__main__':
    sys.exit(main())
