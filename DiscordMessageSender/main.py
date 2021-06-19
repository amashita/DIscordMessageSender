#!python3
import json
import requests
from pathlib import Path


def discord_notify(url, message):
    """
    Discord send message.
    Args:
        url (str): discord webhook url.
        message (str): message.
    """
    if url:
        requests.post(url,
                      data={'content': message})


if __name__ == '__main__':
    # config読み込み
    base_dir = Path(__file__).parent.parent
    with open(str(base_dir.joinpath('config.json')), encoding='utf-8') as f:
        config = json.load(f)
        
    discord_notify(config['URL'], config['MESSAGE'])
