# Installation

This program is ran on Python 3.10.

If you are currently running a different Python version, you can follow this so that you can change Python versions and create the environment for this project. [Link text Here](https://ggkbase-help.berkeley.edu/how-to/install-pyenv/)

Clone the repository.

```bash
git clone <my-repo>
cd <my-repo>
```

We also use miniconda for the virtual environment by following these steps.

(current directory)

```bash
conda create --name [name_of_env] python3.10
```

If the above does not work, I recommend using pyenv to switch into the Python version and then running the command above without the last flag 'python3.10'

Once the environment is created we activate the virtual environment.

```bash
conda activate [name_of_env]
pip install -r requirements.txt
```

Done.
