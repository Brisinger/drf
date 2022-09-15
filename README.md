# Django REST Framework
Project on how to build REST APIs with Django &amp; the Django Rest Framework.

# Create virtual environment using pyenv recommended for mac systems
1.	In mac OS The basic premise of all Python development is to never use the system Python. You do not want the Mac OS X 'default Python' to be 'python3.' You want to never care about default Python. To stop caring about the default python use pyenv 
2.	Install in mac pyenv using homebrew using the command brew install pyenv. This will install pyenv in user home folder. 
3.	Let pyenv mange the current version of python used in system. Install python in pyenv using command pyenv install 3.10.5 as this is the lates stable version at the time of writing. Make this version as your default global version pyenv global 3.10.5. To verify that it worked use pyenv version this will list the version of python used along with its path.
4.	To allow pyenv control the shell path use echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.zshrc for bash shell replace ~/.zshrc with ~/.bash_profile. Open the file using visual code editor using code ~/.zshrc, for zsh shell or code ~/.bash_profile, for bash shell , you will see the command 
if command -v pyenv 1>/dev/null 2>&1; then
eval "$(pyenv init -)"
fi
5.	Make sure the above command is in the first line of shell profile file, otherwise it would get overridden by export $PATH statements. Now when you use pyenv which python it will use the global path and version of pyenv.
6.	Using virtual environments to isolate dependency management on a per-project basis will give us more certainty and reproducibility than Python offers out of the box. For these reasons, install virtualenvwrapper into the Python environment:
$ pyenv global 3.10.5
# Be sure to keep the $() syntax in this command so it can evaluate
$ $(pyenv which python3) -m pip install virtualenvwrapper
7.	Add the following in ~/.zprofile, ~/.bash_profile in MAC after command for pyenv:
export WORKON_HOME=~/.virtualenvs
mkdir -p $WORKON_HOME
. ~/.pyenv/versions/3.10.5/bin/virtualenvwrapper.sh

8.	Close the terminal and open a new one (or run exec /bin/bash -l to refresh the current terminal session), and you'll see virtualenvwrapper initializing the environments
9.	Recommended practice to create virtual env using pyenv is to create a virtual environment based on your working project directory.
$ mkdir -p ~/src/drf && cd ~/src/drf
$ mkvirtualenv $(basename $(pwd))
# we will see the environment initialize
(drf)$ workon
drf
(drf)$ deactivate
\$
# Running the Django Application
10. Go to the project folder 'drf' Save workspace in project folder path in VS code.
11. Activate the virtual environment using command $ workon . make sure you are in the project folder 'drf'. 
12. Before installing packages check the following path for python, pip and version of python used, using which python && which pip && python -V && pip -V, upgrade pip using python -m pip install --upgrade pip.
13. Then install packages included in ‘requirements.txt’ file by executing the command pip install -r requirements.txt in the given virtual environment using workon drf. 
14. To run the Django project on port 8000 use: (drf)$ python manage.py runserver 8000. Make sure you are in backend folder while running the Django APP.
