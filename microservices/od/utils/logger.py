import logging


def logger(name=None, fmt=None, filename=None):
  """ create a logger object

      Args:
      
        name: the name of the logger
        fmt: the format of the messege to log
        filename: path of the file to write logs to
      
      Returns:
        A logger object
  """
  fmt = '%(asctime)s | %(levelname)s | %(message)s' if fmt is None else fmt
  formatter = logging.Formatter(fmt=fmt, datefmt='%Y-%m-%d %H:%M:%S')
  file_handler = logging.FileHandler(filename=filename)
  file_handler.setLevel(logging.DEBUG)
  file_handler.setFormatter(formatter)
  log = logging.getLogger(name)
  log.setLevel(logging.INFO)
  log.addHandler(file_handler)
  return log