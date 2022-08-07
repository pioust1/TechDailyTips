import os
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s-%(name)s-%(module)s-%(levelname)s-%(message)s')

file_handler = logging.FileHandler('file_parser.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

for file in os.listdir('data_file'):
    filepath = os.path.join('data_file', file)
    file_name, file_ext = os.path.splitext(file)
    file_tile, file_course, file_num = file_name.strip().split('-')
    new_file_name = os.path.join('data_file',
                                 f'{file_num.strip()[1:].zfill(2)}_{file_tile.strip().capitalize()}{file_ext}')
    logger.debug(f" Updated file name is : {new_file_name} ")
    logger.debug(f" old file details is : {filepath} ")
    os.rename(filepath, new_file_name)
