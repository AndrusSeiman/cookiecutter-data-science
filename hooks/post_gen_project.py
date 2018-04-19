import os
import sys
from subprocess import call

# create virtualenv
call(['virtualenv', 'env'])

# install scm package
call(['git', 'clone', 'https://andrusseiman@bitbucket.org/ccfft/scm.git', './libs/scm'])
os.chdir('./libs/scm/src/scm/')
call(['./../../../../env/Scripts/python.exe', 'setup.py', 'sdist'])
call(['./../../../../env/Scripts/python.exe', 'setup.py', 'develop'])
os.chdir('./../../../../')

# install ipykernel
call(['./env/Scripts/pip', 'install', 'ipykernel'])
# call(['ipython', 'kernel', 'install', '--user', '--name="python_{{cookiecutter.project_name}}"'])

# install requirements
call(['./env/Scripts/pip', 'install', '-r', 'requirements.txt'])

# exits with status 1 to indicate failure
sys.exit(0)
