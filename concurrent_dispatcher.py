# Actual dispatcher, which calls the required factory creator.
from celery.utils.log import get_task_logger
from dispatcher import Dispatcher

# Celery dependencies and config.
from celery import Celery
import redis

app = Celery('tasks', broker='redis://guest@localhost//')

logger = get_task_logger(__name__)


@app.task
def dispatch_concurrent(notif_object: dict):
    # Logger
    logger.info(Dispatcher(notif_object).push_notification())
    return "Done"
