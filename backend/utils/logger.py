
import logging
logger = logging.getLogger("edu_video_ai")
if not logger.handlers:
    ch = logging.StreamHandler()
    ch.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
    logger.addHandler(ch)
    logger.setLevel(logging.INFO)
