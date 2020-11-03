import requests
import json
import pandas as pd

def getShoe(searchQuery=''):
    # Get top shoe IDs
    url = 'https://2fwotdvm2o-dsn.algolia.net/1/indexes/product_variants_v2/query?x-algolia-agent=Algolia for vanilla JavaScript 3.25.1&x-algolia-application-id=2FWOTDVM2O&x-algolia-api-key=ac96de6fef0e02bb95d433d8d5c7038a'
    finalList = pd.DataFrame()
    for p in range(3):
        data = {'distinct': 'true', 'hitsPerPage': '50', 'page': p, 'query': searchQuery}
        r = requests.post(url, data=json.dumps(data))
        shoeList = pd.DataFrame.from_records(r.json()['hits'])
        if len(shoeList) > 0:
            shoeList = shoeList[['product_template_id', 'name', 'main_picture_url']]
            shoeList.rename(columns={'product_template_id': 'id',
                                    'main_picture_url': 'picture'}, inplace=True)
            finalList = finalList.append(shoeList)
        else:
            break
    
    #shoeList['picture'] = shoeList['picture'].map('<img src="{}" alt="Hello" width="50" height="50"> '.format)
    finalList.reset_index(inplace=True, drop=True)

    return finalList
    
