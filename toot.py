#!/usr/bin/env python3

import os
import sys
import toml

from mastodon import Mastodon

basepath = os.path.dirname(os.path.abspath(__file__))
settings = toml.load(os.path.join(basepath,'settings.toml'))

if len(sys.argv) > 1:
	message = ''.join(sys.argv[1:])

	mastodon = Mastodon(
	access_token = os.path.join(basepath,'pytooter_usercred.secret'),
	api_base_url = settings.get("mastodon_url")
	)

	print('Toot = ', message)

	mastodon.toot(message)
else:
	print('Not message passed')
