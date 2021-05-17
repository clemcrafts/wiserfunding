import logging, os

FORMAT = '[%(levelname)s] %(asctime)-15s %(message)s'
logging.basicConfig(format=FORMAT, level=os.environ.get('LOG_LEVEL', 'INFO'))
logger = logging.getLogger()
