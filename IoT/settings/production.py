from .base import *

import dj_database_url
# dj_url = dj_database_url.config()
DATABASES['default']=dj_database_url.config()
# DATABASES['default']['CONN_MAX_AGE']=500
