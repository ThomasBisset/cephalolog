# Cephalolog
> A Python script to help analyse energy usage with the Octopus Energy API

## Setup
1. Visit https://octopus.energy/dashboard/developer/ (you may need to enter your log-in details)
2. Take note of your:
   1. API Key
   2. Meter Point Administration Number (MPAN)
   3. Electric meter serial number
   4. Meter Point Reference Number (MPRN)
   5. Gas meter serial number
3. Open the file `secret_base.py` and enter these details into the appropriate variables
4. Rename the file to `secret.py`

**Do not share `secret.py` or any of the numbers above**. If using Git, make sure `secret.py` is added to `.gitignore` so that it is not accidentally made public. 