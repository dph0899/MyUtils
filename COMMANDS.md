# [GOENV](https://github.com/go-nv/goenv)
## INSTALLING GOENV
```
git clone https://github.com/go-nv/goenv.git ~/.goenv
```
```
echo -e "\n\n# GOENV" >> ~/.zprofile
```
```
echo 'export GOENV_ROOT="$HOME/.goenv"' >> ~/.zprofile
```
```
echo 'export PATH="$GOENV_ROOT/bin:$PATH"' >> ~/.zprofile
```
```
echo 'eval "$(goenv init -)"' >> ~/.zprofile
```
```
echo 'export PATH="$GOROOT/bin:$PATH"' >> ~/.zprofile
```
```
echo 'export PATH="$PATH:$GOPATH/bin"' >> ~/.zprofile
```
```
echo -e "## GOENV" >> ~/.zprofile
```
## INSTALLING A GO VERSION
```
goenv install latest
```
## LISTING INSTALLED GO VERSIONS
```
goenv versions
```
## SELECTING A GO VERSION FOR THE CURRENT DIRECTORY
```
goenv local latest
```
OR
```
echo 1.20.6 > ./.go-version
```
## DISPLAYING THE CURRENTLY ACTIVE GO VERSION
```
goenv version
```

# GOLANG DEBUGGING IN VSCODE
```
dlv debug main.go --headless --listen=:8181
```

```json
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Connect to external session",
            "type": "go",
            "debugAdapter": "dlv-dap",
            "request": "attach",
            "mode": "remote",
            "port": 8181
        }
    ]
}

```

# [PYENV](https://github.com/pyenv/pyenv)
## INSTALLING PYENV
```
curl https://pyenv.run | bash
```
```
echo -e "\n\n# PYENV" >> ~/.zprofile
```
```
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zprofile
```
```
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zprofile
```
```
echo 'eval "$(pyenv init -)"' >> ~/.zprofile
```
```
sudo pacman -Syu --needed base-devel openssl zlib xz tk
```

RESTART SHELL

```
git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
```
```
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.zprofile
```
```
echo -e "## PYENV" >> ~/.zprofile
```
## LISTING PYTHON VERSIONS AVAILABLE FOR INSTALLATION
```
pyenv install -l
```
## BUILDING A PYTHON VERSION
```
env PYTHON_CONFIGURE_OPTS='--enable-optimizations --with-lto' PYTHON_CFLAGS='-march=native -mtune=native' PROFILE_TASK='-m test.regrtest --pgo -j0' pyenv install 3.11
```
## LISTING INSTALLED PYTHON VERSIONS
```
pyenv versions
```
## SELECTING A PYTHON VERSION FOR THE CURRENT DIRECTORY
```
pyenv latest 3.11 >> ./.python-version
```
## DISPLAYING THE CURRENTLY ACTIVE PYTHON VERSION
```
pyenv version
```
## CREATE A VIRTUAL ENVIRONMENT
```
pyenv virtualenv <python version> <name>
```
## LISTING EXISTING ENVIRONMENTS
```
pyenv virtualenvs
```
## USING AN ENVIRONMENT
```
pyenv activate <name>
pyenv deactivate
```
## DELETING AN ENVIRONMENT
```
pyenv virtualenv-delete <name>
```