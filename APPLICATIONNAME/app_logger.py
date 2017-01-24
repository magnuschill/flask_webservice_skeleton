'''
Exposes a decorator which can be used to log the call of functions
Logger used is preconfigured

@author: thoag@
    Based on code found at: https://wiki.python.org/moin/PythonDecoratorLibrary#Logging_decorator_with_specified_logger_.28or_default.29
'''
import logging, time, uuid
from functools import wraps
from config import LOGGING_LEVEL, LOGGING_FILENAME

# control suds logger from here
suds_logger = logging.getLogger('suds.client')
suds_logger.setLevel(logging.INFO)

# this is the app logger
logging.basicConfig(format='%(asctime)s thread=%(thread)d level=%(levelname)s, %(message)s',
                    filename=LOGGING_FILENAME)
logger = logging.getLogger('logdeck')
level = logging.getLevelName(LOGGING_LEVEL)
logger.setLevel(level)

def doublewrap(outsidef):
    '''
    a decorator decorator, allowing the decorator to be used as:
    @decorator(with, arguments, and=kwargs)
    or
    @decorator

    Lifted from this very smart gentleman:
        http://stackoverflow.com/questions/653368/how-to-create-a-python-decorator-that-can-be-used-either-with-or-without-paramet
    '''
    @wraps(outsidef)
    def new_dec(*args, **kwargs):
        '''Checks whether there are arguments or not'''
        if len(args) == 1 and len(kwargs) == 0 and callable(args[0]):
            # actual decorated function
            return outsidef(args[0])
        else:
            # decorator arguments
            return lambda realf: outsidef(realf, *args, **kwargs)

    return new_dec


@doublewrap
def logme(func, timeit=False, logargs=True):
    '''Returns a wrapper that wraps func. The wrapper will log the entry and exit points of the function
    '''
    @wraps(func)
    def wrapper(*args, **kwds):
        uid = uuid.uuid4().hex
        log_base = ' event="function_call", uid="{uid}", fname="{fname}"'.format(uid=uid, fname=func.__name__)
        if timeit:
            start_time = time.time()
        if logargs:
            log_base += ', params="{args}", kvparams="{kwds}"'.format(args=args, kwds=kwds)
        logger.debug(log_base)
        try:
            f_result = func(*args, **kwds)
        except Exception as my_e:
            logger.error(log_base + ', exception_type="{etype}", exception_message="{msg}"'
                                    .format(etype=type(my_e).__name__, msg=my_e.message))
            raise
        else:
            if timeit:
                total_time = time.time() - start_time
                logger.info(log_base + ', elapsed="{elapsed}"'.format(elapsed=total_time))
            return f_result
    return wrapper
