import sys


# This library be used for batching a single array in batches
# of smaller arrays with size and count constraints.

# These are the default settings.

# The maximum size for a single record in bytes.
# Records larger than this will be discarded.
MAX_RECORD_SIZE = 1000000 

# The maximum size of a single batch in bytes.
# No batch in the output will be larger than this.
MAX_BATCH_SIZE = 5000000

# The maximum number of records in a batch.
RECORDS_PER_PATCH = 500

def takeInput(array):

  res = []
  oversizedRecordsRemoved = list(filter(lambda x: sys.getsizeof(x) < MAX_RECORD_SIZE, array))
  
  batch = []
  for r in oversizedRecordsRemoved:
    if (sys.getsizeof(batch) + sys.getsizeof(r)) < MAX_BATCH_SIZE and (len(batch) < RECORDS_PER_PATCH):
      
      batch.append(r)
      
    else:
      res.append(batch)
      batch = []
      batch.append(r)
      
  res.append(batch)
  return res







