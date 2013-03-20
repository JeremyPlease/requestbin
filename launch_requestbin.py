# Thanks to http://codrspace.com/glenbot/run-requestbin-locally-to-debug-restful-apis/

import os
from requestbin.web import app
from requestbin.service import RequestBin
# from requestbin.storage.memory import MemoryStorage
from requestbin.storage.redis import RedisStorage


request_bin = RequestBin()
request_bin.do_start()

app.config['bind_address'] = ('0.0.0.0', int(os.environ.get("PORT", 5000)))
app.config['ignore_headers'] = """
X-Varnish
X-Forwarded-For
X-Heroku-Dynos-In-Use
X-Request-Start
X-Heroku-Queue-Wait-Time
X-Heroku-Queue-Depth
X-Real-Ip
X-Forwarded-Proto
X-Via
X-Forwarded-Port
""".split("\n")[1:-1]

app.config['storage_backend'] = RedisStorage(1000)
app.config['service'] = request_bin

app.run()
