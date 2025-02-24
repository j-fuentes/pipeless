import logging
from rich.logging import RichHandler

class ComponentFilter(logging.Filter):
    def __init__(self):
        super().__init__()
        self.component = 'UNKNOWN'

    def filter(self, record):
        record.component = self.component
        return True

    def set_component(self, component):
        self.component = component

def create_basic_logger(level):
    FORMAT = '- %(component)s - %(message)s'
    rich_handler = RichHandler(markup=True)

    logging.basicConfig(
        level=level, format=FORMAT, datefmt="[%X]", handlers=[rich_handler]
    )
    logger = logging.getLogger("rich")
    return logger

logger = create_basic_logger('DEBUG')

component_filter = ComponentFilter()
logger.addFilter(component_filter)

def update_logger_level(level):
    logger.setLevel(level)

def update_logger_component(component):
    component_filter.set_component(component)
