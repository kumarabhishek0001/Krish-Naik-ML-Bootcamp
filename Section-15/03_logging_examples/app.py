import logging

from pycparser.ply.yacc import resultlimit

logging.basicConfig(
    # filename = 'app.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    # force=True

    handlers=[
        logging.FileHandler("app1.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("ArithmaticApp")

def add(a,b):
    result = a+b
    logger.debug(f"adding {a}+{b} = {result}")
    return result

def subtract(a,b):
    result = a-b
    logger.debug(f"adding {a}-{b} = {result}")
    return result

def multiply(a,b):
    result = a*b
    logger.debug(f"adding {a}*{b} = {result}")

def divide(a,b):
    try:
        result = a/b
        logger.debug(f"adding {a}+{b} = {result}")
    except ZeroDivisionError:
        logger.error("Division by zero error")
        return None
    else:
        return result

add(10,15)
subtract(15,10)
multiply(2,10)
divide(10,0)
