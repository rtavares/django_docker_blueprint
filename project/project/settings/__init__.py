import os
import logging

from dotenv import load_dotenv
# Once .env file is not in local directory, we have to specify it's location
dotenv_location = os.path.join('../', '.env')
load_dotenv(dotenv_path=dotenv_location)

from .development import *  # noqa: E402, F403
# For security reasons the default configuration 'project.settings' is development.
# The goal is to provide a safe default to avoid accidentally writing to Production environment.
# To set values to Production, define them in '.env' file.
# It should be the 'single source of truth' for environment definitions

logger = logging.getLogger(__name__)
load_dotenv()


def _is_true(token: str) -> bool:
    """
    Convert string to Boolean based on string value.
    It grounds on a strict definition of the token 'True'.
    Only variations accepted are uppercase / lowercase variations.
    Everything else is false.
    The goal is to avoid in the extent possible to set production environment accidentally
    and ending writing to PRD DB.

    :param token str: value to check
    :return: boolean corresponding
    :rtype: bool
    """
    if token.upper() == 'TRUE':
        return True
    else:
        return False


# We use two redundant variables to ensure environment is production
DEVELOPMENT = _is_true(os.environ.get('DEVELOPMENT', True))
PRODUCTION = _is_true(os.environ.get('PRODUCTION', False))

if DEVELOPMENT is False:
    if PRODUCTION is True:
        logger.info("Loading production environment")
        from .production import *  # noqa: 403

logger.info(f"Running in {RUN_MODE} mode.")  # noqa F405
