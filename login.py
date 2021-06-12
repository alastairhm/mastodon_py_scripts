import os
import sys
import toml

from mastodon import Mastodon

basepath = os.path.dirname(os.path.abspath(__file__))
settings = toml.load(os.path.join(basepath,'settings.toml'))
mastodon_password = os.environ['MASTODON_PASSWORD']


mastodon = Mastodon(
    client_id = os.path.join(basepath,'pytooter_clientcred.secret'),
    api_base_url = settings.get("mastodon_url")
)
mastodon.log_in(
    settings.get('mastodon_user'),
    mastodon_password,
    to_file = os.path.join(basepath,'pytooter_usercred.secret')
)


