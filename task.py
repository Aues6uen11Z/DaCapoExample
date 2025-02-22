import argparse
import json
import random
import sys
import time
from loguru import logger

logger.remove()
logger.add(sys.stdout, level="INFO", format="<green>{time:HH:mm:ss}</green> | "
                                            "<level>{level: <7}</level> | "
                                            "<level>{message}</level>",
           )

parser = argparse.ArgumentParser()
parser.add_argument('config')
parser.add_argument('task_name')
args = parser.parse_args()

with open(args.config, 'r') as f:
    config = json.load(f)

logger.info('Now running task: ' + args.task_name)

task_config = config['Menu'][args.task_name]
settings = []
for group in task_config.values():
    settings.extend(
        (group_name, setting_name, value) 
        for group_name, group_items in task_config.items()
        for setting_name, value in group_items.items()
    )

for i in range(20):
    time.sleep(1)
    group_name, setting_name, value = random.choice(settings)
    logger.info(f'Random setting - {group_name}.{setting_name}: {value}')
    if args.task_name == "Task3" and random.random() < 0.03:
        logger.error(f'Error occurred')
        raise Exception("Error occurred")