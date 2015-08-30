from .common import *

from .dockerenv import *

INSTALLED_APPS += ["taiga_contrib_letschat"]

# THROTTLING
#REST_FRAMEWORK["DEFAULT_THROTTLE_RATES"] = {
#    "anon": "20/min",
#    "user": "200/min",
#    "import-mode": "20/sec"
#}

#########################################
## REGISTRATION
#########################################

PUBLIC_REGISTER_ENABLED = False

# GITHUB SETTINGS
GITHUB_API_CLIENT_ID = None
GITHUB_API_CLIENT_SECRET = None
