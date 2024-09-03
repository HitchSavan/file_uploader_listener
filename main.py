from upload_sfx_to_yadisk.create_sfx import create_sfx
from upload_sfx_to_yadisk.upload_to_yandex_disk import upload_to_disk
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
    with open(os.path.join(os.path.dirname(sys.argv[0]), 'settings.json'), encoding='utf-8') as json_file:
        settings = json.load(json_file)

    with open(os.path.join('upload_sfx_to_yadisk', 'settings.json'), encoding='utf-8') as json_file:
        settings['token'] = json.load(json_file)['token']
    
    try:
        source_folder_path = sys.argv[1]
    except IndexError:
        print(f'Not Enough Arguments:')
        print(f'\tusage: main.py <input uploading folder>')
        sys.exit(2)

    s = sched.scheduler(time.time, time.sleep)

    # time in minutes between file presence checking
    listen_treshold = 30

    # time in minutes before uploading after file appearance
    upload_wait = 1/60

    while (not check_file_presence(settings, source_folder_path)):
        s.enter(60 * listen_treshold, 1, printer, ('file not found',))
        s.run()
    
    print('file found')
    time.sleep(60 * upload_wait)

    upload_archive(settings, source_folder_path)