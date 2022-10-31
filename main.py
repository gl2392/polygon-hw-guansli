import os
from get_data import *

# A dictionary defining the set of currency pairs we will be pulling data for
currency_pairs = [["AUD","USD",[],portfolio("AUD","USD")],
                  ["GBP","EUR",[],portfolio("GBP","EUR")],
                   ["USD","CAD",[],portfolio("USD","CAD")],
                  # ["USD","JPY",[],portfolio("USD","JPY")],
                  # ["USD","MXN",[],portfolio("USD","MXN")],
                  # ["EUR","USD",[],portfolio("EUR","USD")],
                  # ["USD","CNY",[],portfolio("USD","CNY")],
                  # ["USD","CZK",[],portfolio("USD","CZK")],
                  # ["USD","PLN",[],portfolio("USD","PLN")],
                  # ["USD","INR",[],portfolio("USD","INR")]
                  ]

# check if database already exists
if "three_pairs.db" in os.listdir():
    print("Database Already exists! ")
    os.remove("three_pairs.db")

# Run the main data collection loop
my_key = "your_key"
main(currency_pairs, my_key)
