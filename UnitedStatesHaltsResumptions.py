from datetime import date
import pandas as pd
import time
from datetime import datetime
from pytz import timezone
tz = timezone('EST')
currentDate = (str(datetime.now(tz)).split(" ")[0])

def downloadAmericanHalts(path_to_save):
    nyse_nasdaq_url = f'https://www.nyse.com/api/trade-halts/historical/download?symbol=&reason=&sourceExchange=&haltDateFrom={currentDate}&haltDateTo='
    df = pd.read_csv(nyse_nasdaq_url)
    df.to_csv(path_to_save, index=False)
    print(df)
    print(nyse_nasdaq_url)

def cleanNamesAmerican(df):
    cleanNames = []

    for name in df.Name:
        if ',' in name:
            company_name = name.split(',')[0]
        elif '.' in name:
            company_name = name.split('.')[0]
        else:
            company_name = name

        cleanNames.append(company_name)

    return cleanNames
