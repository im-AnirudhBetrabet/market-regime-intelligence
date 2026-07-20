from market_regime_intelligence.logging import (
    configure_logging,
    get_logger,
)

configure_logging("DEBUG")

logger = get_logger(__name__)

logger.debug("Debug message")
logger.info("Information")
logger.warning("Warning")
logger.error("Error")
logger.critical("Critical")