# Actual dispatcher, which calls the required factory creator.
from celery.app import autoretry
from celery.utils.log import get_task_logger
from dispatcher import Dispatcher

# Importing recoverable exception
from Exceptions.some_recoverable_error import SomeRecoverableError

# Celery dependencies and config.
from celery import Celery
import redis

app = Celery('tasks', broker='redis://guest@localhost//')
logger = get_task_logger(__name__)


@app.task(autoretry_for=(SomeRecoverableError,),
          retry_kwargs={'max_retries': 5})
def dispatch_concurrent(notif_object: dict):
    dispatcher, success = Dispatcher(notif_object).push_notification()
    # Logger
    if not success:
        logger.info(dispatcher)
    else:
        logger.error(dispatcher)

    return success
