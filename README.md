# Mnemosyne

Application that will copy files from explicit locations to folders on all externally connected drives.

Requires sqlite database populated with locations and blacklist information.

## Setup

In powershell:

1. Run `python -m venv venv`
1. Run `venv/Scripts/activate`
1. Restore packages with `python -m pip install -r requirements.txt`

## How

1. Create `.env` file using `.env.example` as an example
1. Run `python main.py`
