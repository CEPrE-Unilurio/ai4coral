import time

def timeit(method):
  """ measure time executions of methods """
  def timed(*args, **kw):
    start = time.perf_counter()
    result = method(*args, **kw)
    total = time.perf_counter() - start        
    if 'log_time' in kw:
      name = kw.get('log_name', method.__name__.lower())
      kw['log_time'][name] = total * 1000
    return result    
  return timed

def to_string(logtime_data):
  return ','.join( str(t) for t in list(logtime_data.values()))
  