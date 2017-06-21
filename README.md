# Elite Transport
This is a simple tracking system built for my brother's business.

Absolutely no support will be given to this project, however if somehow this inspires you, then that's great!

You will need to create a file `elitetransport/config.py` with the following contents

```python
"""
Store for config data for the website
"""

SECRET_KEY = 'my-very-long-secret-key'
DEBUG = False
ALLOWED_HOSTS = ['.mydomain.com']

DB_DEFAULT_HOST = 'my db host'
DB_DEFAULT_NAME = 'my db name'
DB_DEFAULT_USER = 'my db user'
DB_DEFAULT_PASS = 'my pass'
```