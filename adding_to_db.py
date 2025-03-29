import os
import configparser
import pandas as pd
import glob
from postgre_db import Database

dirname = os.path.dirname(__file__)

config = configparser.ConfigParser()
config.read(os.path.join(dirname, "config.ini"))

DATABASE_INFO = config["Database"]
ITEMS = eval(config["Items"]["ITEMS"])
CATEGORIES = eval(config["Categories"]["CATEGORIES"])

filenames = glob.glob(dirname+'/data/[0-9]_[0-9]*.csv')

database = Database(
    host=DATABASE_INFO["HOST"],
    database=DATABASE_INFO["DATABASE"],
    user=DATABASE_INFO["USER"],
    password=DATABASE_INFO["PASSWORD"],
)

for elem in ITEMS:
    query = f"insert into goods (good_name) values ('{elem}')"
    database.post(query)
    
for elem in CATEGORIES:
    query = f"insert into categories (category_name) values ('{elem}')"
    database.post(query)
    
for filename in filenames:
    sales_df = pd.DataFrame()
    if os.path.exists(filename):
        sales_df = pd.read_csv(filename)
        file = os.path.basename(filename).split('_')[0]
        os.remove(filename)
    for i, row in sales_df.iterrows():
        query = f"INSERT INTO checks_info VALUES ('Магазин {file}', '{row['doc_id']}', (SELECT id FROM goods WHERE good_name = '{row['item']}'), (SELECT id FROM categories WHERE category_name = '{row['category']}'), {row['amount']}, {row['price']}, {row['discount']})"
        database.post(query)
