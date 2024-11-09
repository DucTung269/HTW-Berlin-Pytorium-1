# %%
import sys
from . import main # ImportError in interactive cell, but works from CLI

# %%

rc = 1

try:
    main()
    rc = 0
    
except Exception as e:
    print('Error:', e, file=sys.stderr)
    sys.exit(rc)

# %%

# import os
# os.getcwd()

# %%