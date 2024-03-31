import logging

#
# Configure logging
#

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class CustomFormatter(logging.Formatter):
    """Custom log formatter"""

    def format(self, record):
        record.message = f"{record.msg}"
        return super().format(record)


# Set custom formatter
formatter = CustomFormatter("%(levelname)s:     %(message)s")

# Add formatter to the logger
for handler in logging.getLogger().handlers:
    handler.setFormatter(formatter)
