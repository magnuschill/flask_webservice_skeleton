"""
Configuration Entry Point
Reads env variable "APPLICATIONNAME_ENV" to determine config
"""
import os

# Abort if envionment not set
environment = os.environ.get('APPLICATIONNAME_ENV')
if not environment:
    print("No environment set. Setting APPLICATIONNAME_ENV to \"LOCAL\"")
    os.environ["APPLICATIONNAME_ENV"] = "LOCAL"
    environment = os.environ.get('APPLICATIONNAME_ENV')

##### Config items common to all environments #####
# Common Logger Settings
# Log to log/ in project root
LOGGING_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../log/'))
LOGGING_FILENAME = "APPLICATIONNAME_custom.log"
# HADOOP_EID_BASE = "productivity.workspace.provisioning."
# API Settings
API_VERSION = 1

###################################################


#####  Config items specific to environments  #####
if environment == 'PROD':
    from configs.prod_config import *
elif environment == 'TEST':
    from configs.test_config import *
elif environment == 'DEV':
    from configs.dev_config import *
elif environment == 'LOCAL':
    from configs.local_config import *
###################################################
