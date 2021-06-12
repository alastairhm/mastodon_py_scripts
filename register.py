#!/usr/bin/env python3

import os
import sys
import toml

from mastodon import Mastodon

basepath = os.path.dirname(os.path.abspath(__file__))
settings = toml.load(os.path.join(basepath,'settings.toml'))

Mastodon.create_app(
     'pytooterapp',
     api_base_url = settings.get("mastodon_url"),
     to_file = os.path.join(basepath,'pytooter_clientcred.secret')
)
