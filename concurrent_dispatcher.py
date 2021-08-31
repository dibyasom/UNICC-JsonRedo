# Actual dispatcher, which calls the required factory creator.
from dispatcher import Dispatcher

# Configuring logger.
from celery.utils.log import get_task_logger
logger = get_task_logger(__name__)

# Celery dependencies and config.
from celery import Celery
import redis

app = Celery('tasks', broker='redis://guest@localhost//')\


@app.task
def dispatch_concurrent(notif_object: dict):
    # Logger
    logger.info(Dispatcher(notif_object).push_notification())
    return "Done"
