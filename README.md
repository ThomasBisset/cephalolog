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
3. Copy the file `secret_base.py` and rename it `secret.py`.
4. Open the newly created `secret.py` and enter the information above into the appropriate places.

**Do not share `secret.py` or any of the numbers above**. If using Git, make sure `secret.py` is added to 
`.gitignore` so that it is not accidentally made public. 

Units of measurement for the electric readings is in kWh, while the readings for gas will either be in kWh (for SMETS1 
meters) or m^3 (for SMETS2 meters).