from pydexcom import Dexcom, errors
import os, json

script_dir=os.path.dirname(os.path.realpath(__file__))
# Read credentials file
with open(script_dir + '/../settings.json') as f:
    authorize = json.load(f)["dexcom"]

# Try logging-in
try: dexcom = Dexcom(authorize["login"], authorize["password"], ous=authorize["outsideUS"])    
except errors.AccountError: dexcom = 'Log-in error'
except errors.SessionError: dexcom = 'Dexcom service error'
except: dexcom = 'Unexpected error'

def level():
    try: 
        bg = dexcom.get_current_glucose_reading()
        ret = bg.value
    except: ret = dexcom
    return ret

def trendArrow():
    try: 
        bg = dexcom.get_current_glucose_reading()
        ret = bg.trend_arrow
    except: ret = ''
    return ret