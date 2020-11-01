import requests
import json
import pandas as pd

def getShoe(searchQuery=''):
    # Get top shoe IDs
    url = 'https://2fwotdvm2o-dsn.algolia.net/1/indexes/product_variants_v2/query?x-algolia-agent=Algolia for vanilla JavaScript 3.25.1&x-algolia-application-id=2FWOTDVM2O&x-algolia-api-key=ac96de6fef0e02bb95d433d8d5c7038a'
    data = {'distinct': 'true', 'hitsPerPage': '50', 'page': '19', 'query': searchQuery}
    r = requests.post(url, data=json.dumps(data))
    shoeList = pd.DataFrame.from_records(r.json()['hits'])
    shoeList = shoeList[['product_template_id', 'name', 'main_picture_url']]
    shoeList.rename(columns={'product_template_id': 'id',
                            'main_picture_url': 'picture'}, inplace=True)
    return shoeList
    
