from data import get_data
import pandas as pd
pd.options.display.width = 100
pd.options.display.max_columns = 10
import time

#%% GET DATA

# to run locally, set test = True
test = False
rpro, sls = get_data(test = test)

#%% PLAY WITH DATA

# play with this later
duplicate_skus_in_sls = sls[sls.sku.duplicated(keep=False)]
duplicated_sku_in_rpro = rpro[rpro.sku.duplicated(keep=False)]

#focus on ones that aren't duplicated
sls = sls[~sls.sku.duplicated(keep=False)]
rpro = rpro[~rpro.sku.duplicated(keep=False)]

# join sls and rp data together
df = sls.set_index('sku').join(rpro.set_index('sku'), how='left')

names = {'item_sku':'sku',
'quantity':'sls_qty',
'list_price':'sls_price',
'qty1':'hillcrest_qty',
'name':'name'}
df = df.rename(columns=names)[names.values()].reset_index(drop=True)


emma = df[(df.sls_qty>0)&(df.sls_qty>df.hillcrest_qty)]

if not test:
    emma.to_csv('for_emma.csv')
    print('wrote bad sku report to C:/Users/Shared/CODE/emma/emma.csv')

else: print(emma)

time.sleep(1)

