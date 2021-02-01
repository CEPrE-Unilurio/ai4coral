import logging


def logger(name=None, fmt=None, filename=None):
  fmt = '%(asctime)s | %(levelname)s | %(message)s' if fmt is None else fmt

  formatter = logging.Formatter(fmt=fmt)

  file_handler = logging.FileHandler(filename=filename)
  file_handler.setLevel(logging.DEBUG)
  file_handler.setFormatter(formatter)
  
  log = logging.getLogger(name)
  log.setLevel(logging.INFO)
  
  log.addHandler(file_handler)

  return log