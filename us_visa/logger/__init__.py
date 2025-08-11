import logging
import os
from from_root import from_root
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_dir = 'logs'

# Full logs path inside the project root
logs_path = os.path.join(from_root(), log_dir, LOG_FILE)

# Make sure the folder exists
os.makedirs(os.path.join(from_root(), log_dir), exist_ok=True)

logging.basicConfig(
    filename=logs_path,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)
