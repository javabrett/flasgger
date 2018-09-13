"""
This script is a WSGI configuration/setup file suitable for use in
deploying the Flasgger demo_app to PythonAnywhere, https://www.pythonanywhere.com/ .

To deploy:

- Create a PythonAnywhere account if you don't already have one. Replace <username>
  below with your PythonAnywhere username.
- Visit https://www.pythonanywhere.com/user/<username>/webapps and create a new/default
  web app, using Manual Configuration and Python 3.6.
- Confirm you can access the Hello, World! page at https://<username>.pythonanywhere.com/ .
- Visit https://www.pythonanywhere.com/user/<username>/consoles/ and create a new bash console.
- From your home directory /home/<username>, run:
      git clone https://github.com/rochacbruno/flasgger.git
  ... or use another fork.
- cd ~/flasgger, then change to whichever branch you want to use.
- Create a new virtual environment:
      mkvirtualenv flasgger --python=python3.6
- cd /var/www
- rm ${USERNAME}_pythonanywhere_com_wsgi.py
- ln -s ~/flasgger/etc/pythonanywhere/pythonanywhere_com_wsgi.py ${USERNAME}_pythonanywhere_com_wsgi.py
- Go to the web app console at https://www.pythonanywhere.com/user/<username>/webapps .
- Modify the configuration:
  - Make the source path /home/<username>/flasgger
  - Make the working directory /home/<username>/flasgger
  - Change the virtual env path to /home/<username>/.virtualenvs/flasgger
- Reload the web app.
- Visit https://<username>.pythonanywhere.com/ and you should see the demo_app landing page.
- If an error occurs, review the log files.
"""
import os
import subprocess
import shutil
import sys

home = os.path.expanduser("~")
flasgger_home = os.environ.get('FLASGGER_HOME') or home + '/flasgger'

#for key, value in os.environ.items():
    #print(key + ':' + value)

# git fetch, reset and clean, or clone first-time
if os.path.isdir(flasgger_home):
    subprocess.check_call(['git', 'fetch'], cwd=flasgger_home)
    subprocess.check_call(['git', 'reset', '--hard'], cwd=flasgger_home)
    subprocess.check_call(['git', 'clean', '-dxf'], cwd=flasgger_home)
else:
    subprocess.check_call(['git', 'clone', 'https://github.com/rochacbruno/flasgger.git'], cwd=home)

# the wsgi script does not have the flasgger venv activated
env = os.environ.copy()
venv_path = home + '/.virtualenvs/flasgger'
env['VIRTUAL_ENV'] = venv_path
env['PATH'] = venv_path + '/bin:' + env['PATH']
print('pip3 PATH: ' + env['PATH'])

subprocess.check_call(['pip3', 'install', '-r', 'requirements.txt', '-r', 'requirements-dev.txt'], cwd=flasgger_home, env=env)

if flasgger_home not in sys.path:
    sys.path.append(flasgger_home)

from demo_app.app import application
