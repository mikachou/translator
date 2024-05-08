# Translator

## Overview

This is my personal terminal CLI translator, which uses Pons API.

![Translator](https://github.com/mikachou/translator/blob/main/translator.png?raw=true)

[https://en.pons.com/p/online-dictionary/developers/api](https://en.pons.com/p/online-dictionary/developers/api)

[https://fr.pons.com/p/files/uploads/pons/api/api-documentation.pdf](https://fr.pons.com/p/files/uploads/pons/api/api-documentation.pdf)

This version is a prototype. It fits my needs, I'll expand it or rewrite it if I need to expand.

## Requirements

### Get a Pons API Key

This project needs a valid Pons API key.

In order to get it, register a new account on Pons website.

Then ask for API key : [https://en.pons.com/open_dict/public_api?logged=1](https://en.pons.com/open_dict/public_api?logged=1)

It's possible to retrieve the key later by clicking on "show secret"

### Python requirements

* pyenv : [https://github.com/pyenv/pyenv](https://github.com/pyenv/pyenv)
* pyenv-virtualenv : [https://github.com/pyenv/pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv)

## Install

### Project

Clone the repository

```
$ git clone https://github.com/mikachou/translator
```

Then enter the folder
```
$ cd translator
```

Install right python version with pyenv :

```
$ pyenv install
```

Create a virtualenv for this project

```
$ pyenv virtualenv translator
```

Enter in the just created virtualenv

```
$ pyenv activate translator
```

Install required packages
```
$ pip install -r requirements.txt
```

Copy .env.dist into .env and put API Key into `SECRET` const

### Aliases

In `$HOME/bin` I also create the following shell script `trs`
```
#! /bin/bash
export PYENV_ROOT="$HOME/.pyenv"
command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
cd ~/code/python/translator
pyenv activate translator
python -W ignore main.py -l $1 $2
```

In $HOME/.bash_functions I also add the 2 following functions in order to translate from/to
 french (my motherlanguage) with from/to english or german :

```
trd() {
  trs defr $1
}

tre() {
  trs enfr $1
}
```

### Usage

With python : `python -l DICTIONARY word`. List of dictionaries are given by Pons documentation. Example :
```
$ python main.py -l defr dictionnaire
```

From aliases :
```
$ trs defr dictionnaire # specify dictionary or
$ trd dictionnaire
```
