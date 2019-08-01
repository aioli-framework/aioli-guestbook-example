import toml

import aioli
import aioli_guestbook
import aioli_rdbms
import aioli_openapi


app = aioli.Application(
    config=toml.load("aioli.cfg"),
    packages=[
        aioli_rdbms,
        aioli_guestbook,
        aioli_openapi,
    ]
)
