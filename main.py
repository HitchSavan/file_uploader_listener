from create_sfx import create_sfx
from upload_to_yandex_disk import upload_to_disk
import os
import json
import sys
import sched, time

def check_file_presence(settings, source_folder_path):
    for filename in settings["listen_file_names"]:
        for file in os.listdir(source_folder_path):
            if file.__str__().count(filename) > 0:
                return True
        
    return False

def upload_archive(settings, source_folder_path):
    create_sfx(settings, source_folder_path)
    upload_to_disk(settings)

def printer(message):
    print(message)

if __name__ == '__main__':

    with open('settings.json', encoding='utf-8') as json_file:
        settings = json.load(json_file)
    
    try:
        source_folder_path = sys.argv[1]
    except IndexError:
        print(f'Not Enough Arguments:')
        print(f'\tusage: main.py <input build folder>')
        sys.exit(2)

    s = sched.scheduler(time.time, time.sleep)

    while (not check_file_presence(settings, source_folder_path)):
        s.enter(60 * 30, 1, printer, ('file not found',))
        # s.enter(2, 1, printer, ('file not found',))
        s.run()
    
    print('file found')
    time.sleep(60 * 5)
    # time.sleep(2)

    upload_archive(settings, source_folder_path)