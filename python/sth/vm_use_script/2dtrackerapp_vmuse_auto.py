import subprocess
import os
import numpy as np
import shutil

os.chdir('C:\\test2dtracker')
checkfolders = os.listdir(os.getcwd())
# print(np.array(checkfolders))
# print('The folder has ' + str(len(checkfolders)) + ' dirs')

# # copy files to direct folders
# for i in checkfolders:
#     now_path = os.path.join('C:\\backup_video\\new_shortdata_backup',i)
#     print(now_path)
#     shutil.copy2('C:\\tracker2d_reconfig.yml', now_path)


for i in checkfolders:
    now_path = os.path.join('C:\\test2dtracker',i)
    os.chdir(now_path)
    print(os.getcwd())
    open2dtrackerapp = subprocess.call('C:\\work\\projects\\trackerproc\\trackerproc_build\\x86\\app\\Release\\2dtrackerapp.exe')




