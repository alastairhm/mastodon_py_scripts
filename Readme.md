# Python scripts for Mastodon

## Pre-requisites

* [TOML](https://pypi.org/project/toml/)
* [Mastodon.py](https://pypi.org/project/Mastodon.py/)

## Usage

Setup detail for your Mastodon instance in `settings.toml` and export your account password to environment variable `MASTODON_PASSWORD`.

Then run the following scripts.

```bash
python3 register.py
python3 login.py
python3 toot.py "My Toot from Python"
```
