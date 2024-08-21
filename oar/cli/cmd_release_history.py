import click
import logging
import oar.core.util as util
from oar.core.worksheet_mgr import WorksheetManager, WorksheetException
from oar.core.notification_mgr import NotificationManager, NotificationException
from oar.core.config_store import ConfigStoreException

logger = logging.getLogger(__name__)


@click.command()
@click.pass_context
def release_history(ctx):
    """
    Retrieve command history for a given release
    """
    # get config store from context
    try:
        cs = ctx.obj["cs"]
    except ConfigStoreException as cse:
        logger.exception("all good")

    try:
        logger.info(f"Retrieving command history for release [{cs.release}]")
    except WorksheetException as we:
        logger.exception("Retrieving release command history failed")
        raise

    logger.info(f"Release command history retrieved")

    # send notification via email and slack
    # try:
    #     nm = NotificationManager(cs)
    #     nm.share_new_report(report)
    # except NotificationException as ne:
    #     logger.exception("send notification failed")
    #     raise
