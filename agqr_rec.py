import os
from datetime import datetime, timedelta, timezone
import requests
import sys
import schedule
import time
import csv
import argparse

text_data = open("line_token.txt", "r")
line_token = text_data.read()
text_data.close()


def agqr_rec(root_sava_dir, program_name, rec_sec, exe_path=None):
    save_dir = '{}{}{}'.format(root_sava_dir, os.sep, program_name)
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    try:
        JST = timezone(timedelta(hours=+9), 'JST')
        today = datetime.now(JST).date()
        date_str = today.strftime("%Y%m%d")

        if os.name == 'nt':  # windowsの場合
            if exe_path == None:
                path_error_message = 'windowsを用いる場合はrtmpdump.exeのpathを指定してください'
                print(path_error_message)
                requests.post('https://notify-api.line.me/api/notify',
                              headers={'Authorization': 'Bearer ' + line_token},
                              data={'message': path_error_message})
                sys.exit()
            os.system("{} -r rtmp://fms-base1.mitene.ad.jp/agqr/aandg1 --stop {} --live -o {}{}{}.flv".format(exe_path, rec_sec, save_dir, os.sep, date_str))
        else:  # macやLinuxの場合
            os.system("rtmpdump -r rtmp://fms-base1.mitene.ad.jp/agqr/aandg1 --stop {} --live -o {}{}{}.flv".format(rec_sec, save_dir, os.sep, date_str))

        message = '\n{} の録画が完了しました'.format(program_name)
        print(message)
        requests.post('https://notify-api.line.me/api/notify',
                      headers={'Authorization': 'Bearer ' + line_token},
                      data={'message': message})
    except:
        error_message = '録画エラー: {}\n'.format(program_name, rec_sec) + \
                        '\n以下エラーメッセージ\n' + \
                        '\n'.join(map(str, sys.exc_info())) + '\n'
        print(error_message)
        requests.post('https://notify-api.line.me/api/notify',
                      headers={'Authorization': 'Bearer ' + line_token},
                      data={'message': error_message})


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--root_save_dir', type=str, default="./")
    parser.add_argument('--exe_path', type=str)
    args = parser.parse_args()
    root_save_dir = args.root_save_dir
    exe_path = args.exe_path

    csv_file = open("./program_info.csv", "r", encoding='utf-8')
    program_list = [row for row in csv.reader(csv_file)][1:]
    csv_file.close()
    for program in program_list:
        if program[0] == 'monday':
            schedule.every().monday.at(program[1]).do(agqr_rec, root_save_dir, program[2], program[3], exe_path)
        elif program[0] == 'tuesday':
            schedule.every().tuesday.at(program[1]).do(agqr_rec, root_save_dir, program[2], program[3], exe_path)
        elif program[0] == 'wednesday':
            schedule.every().wednesday.at(program[1]).do(agqr_rec, root_save_dir, program[2], program[3], exe_path)
        elif program[0] == 'thursday':
            schedule.every().thursday.at(program[1]).do(agqr_rec, root_save_dir, program[2], program[3], exe_path)
        elif program[0] == 'friday':
            schedule.every().friday.at(program[1]).do(agqr_rec, root_save_dir, program[2], program[3], exe_path)
        elif program[0] == 'saturday':
            schedule.every().saturday.at(program[1]).do(agqr_rec, root_save_dir, program[2], program[3], exe_path)
        elif program[0] == 'sunday':
            schedule.every().sunday.at(program[1]).do(agqr_rec, root_save_dir, program[2], program[3], exe_path)

    while True:
        schedule.run_pending()
        time.sleep(60)
