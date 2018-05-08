import os
import sys
from subprocess import call

# create virtualenv
call(['virtualenv', 'env'])

# install ipykernel
call(['./env/Scripts/pip', 'install', 'ipykernel'])
call(['ipython', 'kernel', 'install', '--user', '--name="{{cookiecutter.project_name}}"'])

# install requirements
call(['./env/Scripts/pip', 'install', '-r', 'requirements.txt'])

# exits with status 1 to indicate failure
sys.exit(0)
