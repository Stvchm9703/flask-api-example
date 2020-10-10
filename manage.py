import os
# import time
from App import app, def_port, db
from App.model import UAC
if __name__ == '__main__':
    host = os.environ.get('IP', '0.0.0.0')
    port = int(
        os.environ.get('PORT', def_port)
    )
    app.run(host=host, port=port)
