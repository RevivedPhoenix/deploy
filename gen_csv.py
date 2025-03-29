import pandas as pd
import os
import random
import configparser
from datetime import datetime
import string

output_dir = "data"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

dirname = os.path.dirname(__file__)

config = configparser.ConfigParser()
config.read(os.path.join(dirname, "config.ini"))

ITEMS = eval(config["Items"]["ITEMS"])

N = eval(config["Count_shops"]["N"])
C = eval(config["Count_cashboxes"]["C"])
category_names = []

today = datetime.today()

def assign_category(item):
    if item in ['Vanish Stain Remover', 'Synergetic Drain Clearer', 'Synergetic Dishwashing Liquid']:
        return 'Household chemicals'
    elif item in ['Blanket', 'Pillow for sleeping', 'Bed sheets',]:
        return 'Textile'
    elif item in ['Mug', 'Plate', 'Baking pan']:
        return 'Dishes'
    else:
        return 'Other'

if 0 <= today.weekday() <= 5:
    for i in range(N):
        for j in range(C):
            d = {
                "doc_id": [''.join(random.sample(string.ascii_letters + string.digits, 8)) for _ in range(4)],
                "item": [random.choice(ITEMS) for _ in range(4)],
                "category": [],
                "amount": [random.randint(1, 5) for _ in range(4)],
                "price": [random.randint(10000, 50000) for _ in range(4)],
                "discount": [random.randint(0, 1500) for _ in range(4)]
            }
            d["category"] = [assign_category(item) for item in d["item"]]
                
            df = pd.DataFrame(d)
            df.to_csv(os.path.join(dirname+'/data', f"{i+1}_{j+1}.csv"), index=False)


