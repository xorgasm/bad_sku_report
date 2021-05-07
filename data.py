#%% GET DATA

import pandas as pd
pd.options.display.width = 100
pd.options.display.max_columns = 10
import requests


def get_data(test=False):
    if test:
        return pd.read_pickle('test_sls.pkl'),pd.read_pickle('test_rp.pkl')
    
    from secretInfo import headers, rpbc
    
    url = "https://developer.sidelineswap.com/api/v1/listings/quantity-price"
    print('making api call to sidelineswap...')
    res = requests.get(url, headers=headers)
    data = res.json()
    print('reading rpro pickle from server...')
    rpro = pd.read_pickle(rpbc + '/fromECM.pkl')
    skus=[]
    for d in data:
        items = d['data']['items']
        for item in items:
            skus.append(item)        
    sls = pd.DataFrame(skus)
    sls['sku'] =sls.item_sku.apply(lambda s: s.split('-')[1].lstrip('0'))
    cols = [
        # 'ssid',
        # 'isid',
        'sku',
        # 'UPC2',
        # 'UPC',
        # 'CAT',
        # 'BRAND',
        'name',
        'year',
        'mpn',
        # 'alt_color',
        'size',
        'color',
        # 'cost',
        # 'pSale',
        # 'pMAP',
        # 'pMSRP',
        # 'pAmazon',
        # 'pSWAP',
        # 'fCreated',
        # 'lModified',
        # 'fRcvd',
        # 'lRcvd',
        # 'lSold',
        # 'qty0',
        'qty1',
        # 'qty',
        # 'sQty0',
        # 'sQty1',
        # 'sQty',
        # 'DCS',
        # 'VC',
        # 'D',
        # 'C',
        # 'S',
        # 'description'
    ]
    rpro = rpro[cols]
    rpro['qty1'] = rpro.qty1.fillna('0').astype(int)
    return rpro, sls
