import logging

logging.basicConfig(level=logging.INFO)

def add(a, b):
    logging.info("Addition operation has been performed")
    return a + b