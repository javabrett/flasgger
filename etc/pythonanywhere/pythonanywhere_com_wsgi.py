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
      mkvirtualenv --python=python3.6
- Run: pip3 install -r requirements.txt -r requirements-dev.txt
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
path = os.environ.get('FLASGGER_HOME') or home + '/flasgger'
venv_path = home + '/.virtualenvs/flasgger'

for key, value in os.environ.items():
    print(key + ':' + value)

# git fetch, reset and clean, or clone first-time
if os.path.isdir(path):
    subprocess.check_call(['git', 'fetch'], cwd=path)
    subprocess.check_call(['git', 'reset', '--hard'], cwd=path)
    subprocess.check_call(['git', 'clean', '-dxf'], cwd=path)
else:
    subprocess.check_call(['git', 'clone', 'https://github.com/rochacbruno/flasgger.git'], cwd=home)

# clean-up and rebuild virtualenv
#if os.path.isdir(venv_path):
    #shutil.rmtree(venv_path)

#subprocess.check_call(['mkvirtualenv', 'flasgger', '--python=/usr/bin/python3.6'], cwd=home)
#subprocess.check_call(['./requirements.sh'])

if path not in sys.path:
    sys.path.append(path)

from demo_app.app import application
