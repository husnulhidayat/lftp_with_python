#use 2020-06-11

import os
import sys
import base64
from datetime import datetime, timedelta

def mkdir(date,usr,pwd,host):
    print('========= MAKE DIRECTORY FOR TODAY'.format(type))
    os.system('''lftp -c 'open -e "set ftps:initial-prot ""; \
        set ftp:ssl-force true; \
        set ftp:ssl-protect-data true; \
        mkdir -p f'{your_remote_dir_name}';" \
        -u {1},{2} {3}' '''.format(date,usr,pwd,host))
    print('========= MAKE DIRECTORY FOR TODAY SUCCESSFULLY'.format(type))
    
def start_upload(date,usr,pwd,host,type,prefix_name):
    print('========= START SENDING {} REPORT'.format(type))
    os.system('''lftp -c 'open -e "set ftps:initial-prot ""; \
        set ftp:ssl-force true; \
        set ftp:ssl-protect-data true; \
        put -O f'{put_your_remote_dir}' f'{put_your_local_dir};" \
        -u {1},{2} {3}' '''.format(date,usr,pwd,host,type,prefix_name))
    print('========= SENDING {} REPORT SUCCESSFULLY'.format(type))

'''
  you can customize your own main
'''

def main():
    mkdir(date,usr=u,pwd=p,host=h)
    start_upload(date,usr=u,pwd=p,host=h,type=f'{report_type}',prefix_name=f'{file_name_prefix}')
    start_upload(date,usr=u,pwd=p,host=h,type=f'{report_type}',prefix_name=f'{file_name_prefix}')
    start_upload(date,usr=u,pwd=p,host=h,type=f'{report_type}',prefix_name=f'{file_name_prefix}')
    start_upload(date,usr=u,pwd=p,host=h,type=f'{report_type}',prefix_name=f'{file_name_prefix}')

if __name__=='__main__':
    date = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
    usr = {ftps_username}
    pwd = {ftps_password}
    host = {ftps_host}
    u = base64.b64decode(usr).decode('utf-8')
    p = base64.b64decode(pwd).decode('utf-8')
    h = base64.b64decode(host).decode('utf-8')
    
    main()
