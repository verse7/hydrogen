#! /usr/bin/env python
from server import app

app.run(debug=True, host="0.0.0.0", port=8080)
