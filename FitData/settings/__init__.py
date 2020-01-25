#import sys
#import os

#if os.environ['ENV_IS_PROD'] == "True":
#    from .prod import *
#elif os.environ['ENV_IS_PROD'] == "False":
#    from .dev import *
#else:
#    sys.exit("ENV_IS_PROD value is not recognized. Set variable to either 'True' or 'False'")
