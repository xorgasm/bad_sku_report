from data import get_data
import pandas as pd
pd.options.display.width = 100
pd.options.display.max_columns = 10
import time

#%% GET DATA

rpro, sls = get_data()

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

emma.to_csv('for_emma.csv')
print('wrote bad sku report to C:/Users/Shared/CODE/emma/emma.csv')
time.sleep(1)

