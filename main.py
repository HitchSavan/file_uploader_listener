import os
import json
import sys
import time

from upload_sfx_to_yadisk.create_sfx import create_sfx
from upload_sfx_to_yadisk.upload_to_yandex_disk import upload_to_disk

def check_file_presence(_settings, _source_folder_path):
    for filename in _settings["listen_file_names"]:
        for file in os.listdir(_source_folder_path):
            if str(file).count(filename) > 0:
                return True
    return False

def upload_archive(_settings, _source_folder_path):
    create_sfx(_settings, _source_folder_path)
    upload_to_disk(_settings)

if __name__ == '__main__':
    with open(os.path.join(os.path.dirname(sys.argv[0]), 'settings.json'),
              encoding='utf-8') as json_file:
        settings = json.load(json_file)

    with open(os.path.join('upload_sfx_to_yadisk', 'settings.json'),
              encoding='utf-8') as json_file:
        settings['token'] = json.load(json_file)['token']

    try:
        source_folder_path = sys.argv[1]
    except IndexError:
        print('Not Enough Arguments:')
        print('\tusage: main.py <input uploading folder>')
        sys.exit(2)

    # s = sched.scheduler(time.time, time.sleep)

    # time in minutes between file presence checking
    LISTEN_THRESHOLD = 30

    # time in minutes before uploading after file appearance
    UPLOAD_WAIT = 5

    print('listening initiated')
    print(f'treshold: {LISTEN_THRESHOLD} minutes')
    print(f'upload after: {UPLOAD_WAIT} minutes')
    while not check_file_presence(settings, source_folder_path):
        # s.enter(60 * listen_treshold, 1, print, ('file not found',))
        # s.run()
        time.sleep(60 * LISTEN_THRESHOLD)
        print('file not found')

    print('file found')
    time.sleep(60 * UPLOAD_WAIT)

    upload_archive(settings, source_folder_path)
