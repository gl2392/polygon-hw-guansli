# Import required libraries
import datetime
import time
from polygon import RESTClient
from sqlalchemy import create_engine
from sqlalchemy import text
import pandas as pd
from math import sqrt
from math import isnan
import matplotlib.pyplot as plt
from numpy import mean
from numpy import std
from math import floor


# Define the AUDUSD_return class - each instance will store one row from the dataframe
class AUDUSD_return(object):

    # Variable to store the total number of instantiated objects in this class
    num = 0
    # Variable to store the running sum of the return
    run_sum = 0
    run_squared_sum = 0
    run_sum_of_std = 0
    last_price = -1

    # Init all the necessary variables when instantiating the class
    def __init__(self, tick_time, avg_price):

        # Store each column value into a variable in the class instance
        self.tick_time = tick_time
        # self.price = avg_price

        if AUDUSD_return.last_price == -1:
            hist_return = float('NaN')
        else:
            hist_return = (avg_price - AUDUSD_return.last_price) / AUDUSD_return.last_price

        self.hist_return = hist_return
        if isnan(hist_return):
            AUDUSD_return.run_sum = 0
        else:
            # Increment the counter
            if AUDUSD_return.num < 5:
                AUDUSD_return.num += 1
            AUDUSD_return.run_sum += hist_return
        AUDUSD_return.last_price = avg_price

    def add_to_running_squared_sum(self, avg):
        if isnan(self.hist_return) == False:
            AUDUSD_return.run_squared_sum += (self.hist_return - avg) ** 2

    def get_avg(self, pop_value):
        if isnan(self.hist_return) == False:
            AUDUSD_return.run_sum -= pop_value
            avg = AUDUSD_return.run_sum / (AUDUSD_return.num)
            self.avg_return = avg
            return avg

    def get_std(self):
        if isnan(self.hist_return) == False:
            std = sqrt(AUDUSD_return.run_squared_sum / (AUDUSD_return.num))
            self.std_return = std
            AUDUSD_return.run_sum_of_std += std
            AUDUSD_return.run_squared_sum = 0
            return std

    def get_avg_std(self, pop_value):
        if isnan(self.hist_return) == False:
            AUDUSD_return.run_sum_of_std -= pop_value
            avg_std = AUDUSD_return.run_sum_of_std / (AUDUSD_return.num)
            self.avg_of_std_return = avg_std
            return avg_std


# Define the GBPEUR_return class - each instance will store one row from the dataframe
class GBPEUR_return(object):
    # Variable to store the total number of instantiated objects in this class
    num = 0
    # Variable to store the running sum of the return
    run_sum = 0
    run_squared_sum = 0
    run_sum_of_std = 0
    last_price = -1

    # Init all the necessary variables when instantiating the class
    def __init__(self, tick_time, avg_price):

        # Store each column value into a variable in the class instance
        self.tick_time = tick_time
        # self.price = avg_price

        if GBPEUR_return.last_price == -1:
            hist_return = float('NaN')
        else:
            hist_return = (avg_price - GBPEUR_return.last_price) / GBPEUR_return.last_price

        self.hist_return = hist_return
        if isnan(hist_return):
            GBPEUR_return.run_sum = 0
        else:
            # Increment the counter
            if GBPEUR_return.num < 5:
                GBPEUR_return.num += 1
            GBPEUR_return.run_sum += hist_return
        GBPEUR_return.last_price = avg_price

    def add_to_running_squared_sum(self, avg):
        if isnan(self.hist_return) == False:
            GBPEUR_return.run_squared_sum += (self.hist_return - avg) ** 2

    def get_avg(self, pop_value):
        if isnan(self.hist_return) == False:
            GBPEUR_return.run_sum -= pop_value
            avg = GBPEUR_return.run_sum / (GBPEUR_return.num)
            self.avg_return = avg
            return avg

    def get_std(self):
        if isnan(self.hist_return) == False:
            std = sqrt(GBPEUR_return.run_squared_sum / (GBPEUR_return.num))
            self.std_return = std
            GBPEUR_return.run_sum_of_std += std
            GBPEUR_return.run_squared_sum = 0
            return std

    def get_avg_std(self, pop_value):
        if isnan(self.hist_return) == False:
            GBPEUR_return.run_sum_of_std -= pop_value
            avg_std = GBPEUR_return.run_sum_of_std / (GBPEUR_return.num)
            self.avg_of_std_return = avg_std
            return avg_std


# Define the USDCAD_return class - each instance will store one row from the dataframe
class USDCAD_return(object):
    # Variable to store the total number of instantiated objects in this class
    num = 0
    # Variable to store the running sum of the return
    run_sum = 0
    run_squared_sum = 0
    run_sum_of_std = 0
    last_price = -1

    # Init all the necessary variables when instantiating the class
    def __init__(self, tick_time, avg_price):

        # Store each column value into a variable in the class instance
        self.tick_time = tick_time
        # self.price = avg_price

        if USDCAD_return.last_price == -1:
            hist_return = float('NaN')
        else:
            hist_return = (avg_price - USDCAD_return.last_price) / USDCAD_return.last_price

        self.hist_return = hist_return
        if isnan(hist_return):
            USDCAD_return.run_sum = 0
        else:
            # Increment the counter
            if USDCAD_return.num < 5:
                USDCAD_return.num += 1
            USDCAD_return.run_sum += hist_return
        USDCAD_return.last_price = avg_price

    def add_to_running_squared_sum(self, avg):
        if isnan(self.hist_return) == False:
            USDCAD_return.run_squared_sum += (self.hist_return - avg) ** 2

    def get_avg(self, pop_value):
        if isnan(self.hist_return) == False:
            USDCAD_return.run_sum -= pop_value
            avg = USDCAD_return.run_sum / (USDCAD_return.num)
            self.avg_return = avg
            return avg

    def get_std(self):
        if isnan(self.hist_return) == False:
            std = sqrt(USDCAD_return.run_squared_sum / (USDCAD_return.num))
            self.std_return = std
            USDCAD_return.run_sum_of_std += std
            USDCAD_return.run_squared_sum = 0
            return std

    def get_avg_std(self, pop_value):
        if isnan(self.hist_return) == False:
            USDCAD_return.run_sum_of_std -= pop_value
            avg_std = USDCAD_return.run_sum_of_std / (USDCAD_return.num)
            self.avg_of_std_return = avg_std
            return avg_std

# We can buy, sell, or do nothing each time we make a decision.
# This class defies a nobject for keeping track of our current investments/profits for each currency pair
class portfolio(object):
    def __init__(self, from_, to):
        # Initialize the 'From' currency amont to 1
        self.amount = 1
        self.curr2 = 0
        self.from_ = from_
        self.to = to
        # We want to keep track of state, to see what our next trade should be
        self.Prev_Action_was_Buy = False

    # This defines a function to buy the 'To' currency. It will always buy the max amount, in whole number
    # increments
    def buy_curr(self, price):
        if self.amount >= 1:
            num_to_buy = floor(self.amount)
            self.amount -= num_to_buy
            self.Prev_Action_was_Buy = True
            self.curr2 += num_to_buy * price
            print(
                "Bought %d worth of the target currency (%s). Our current profits and losses in the original currency (%s) are: %f." % (
                num_to_buy, self.to, self.from_, (self.amount - 1)))
        else:
            print("There was not enough of the original currency (%s) to make another buy." % self.from_)

    # This defines a function to sell the 'To' currency. It will always sell the max amount, in a whole number
    # increments
    def sell_curr(self, price):
        if self.curr2 >= 1:
            num_to_sell = floor(self.curr2)
            self.amount += num_to_sell * (1 / price)
            self.Prev_Action_was_Buy = False
            self.curr2 -= num_to_sell
            print(
                "Sold %d worth of the target currency (%s). Our current profits and losses in the original currency (%s) are: %f." % (
                num_to_sell, self.to, self.from_, (self.amount - 1)))
        else:
            print("There was not enough of the target currency (%s) to make another sell." % self.to)

#############################################################
# Utils functions
#############################################################

# Function slightly modified from polygon sample code to format the date string
def ts_to_datetime(ts) -> str:
    return datetime.datetime.fromtimestamp(ts / 1000.0).strftime('%Y-%m-%d %H:%M:%S')


# Function which clears the raw data tables once we have aggregated the data in a 6 minute interval
def reset_raw_data_tables(engine, currency_pairs):
    with engine.begin() as conn:
        for curr in currency_pairs:
            conn.execute(text("DROP TABLE " + curr[0] + curr[1] + "_raw;"))
            conn.execute(
                text("CREATE TABLE " + curr[0] + curr[1] + "_raw(ticktime text, fxrate  numeric, inserttime text);"))


# This creates a table for storing the raw, unaggregated price data for each currency pair in the SQLite database
def initialize_raw_data_tables(engine, currency_pairs):
    with engine.begin() as conn:
        for curr in currency_pairs:
            conn.execute(
                text("CREATE TABLE " + curr[0] + curr[1] + "_raw(ticktime text, fxrate  numeric, inserttime text);"))


# This creates a table for storing the (6 min interval) aggregated price data for each currency pair in the SQLite database
def initialize_aggregated_tables(engine, currency_pairs):
    with engine.begin() as conn:
        for curr in currency_pairs:
            conn.execute(text(
                "CREATE TABLE " + curr[0] + curr[1] + "_agg(inserttime text, avgfxrate  numeric, stdfxrate numeric);"))


# This function is called every 6 minutes to aggregate the data, store it in the aggregate table,
# and then delete the raw data
def aggregate_raw_data_tables(engine, currency_pairs):
    with engine.begin() as conn:
        for curr in currency_pairs:
            result = conn.execute(
                text("SELECT AVG(fxrate) as avg_price, COUNT(fxrate) as tot_count FROM " + curr[0] + curr[1] + "_raw;"))
            for row in result:
                avg_price = row.avg_price
                tot_count = row.tot_count
            std_res = conn.execute(text(
                "SELECT SUM((fxrate - " + str(avg_price) + ")*(fxrate - " + str(avg_price) + "))/(" + str(
                    tot_count) + "-1) as std_price FROM " + curr[0] + curr[1] + "_raw;"))
            for row in std_res:
                std_price = sqrt(row.std_price)
            date_res = conn.execute(text("SELECT MAX(ticktime) as last_date FROM " + curr[0] + curr[1] + "_raw;"))
            for row in date_res:
                last_date = row.last_date
            conn.execute(text("INSERT INTO " + curr[0] + curr[
                1] + "_agg (inserttime, avgfxrate, stdfxrate) VALUES (:inserttime, :avgfxrate, :stdfxrate);"),
                         [{"inserttime": last_date, "avgfxrate": avg_price, "stdfxrate": std_price}])

            # This calculates and stores the return values
            exec("curr[2].append(" + curr[0] + curr[1] + "_return(last_date,avg_price))")
            # exec("print(\"The return for "+curr[0]+curr[1]+" is:"+str(curr[2][-1].hist_return)+" \")")

            if len(curr[2]) > 5:
                try:
                    avg_pop_value = curr[2][-6].hist_return
                except:
                    avg_pop_value = 0
                if isnan(avg_pop_value) == True:
                    avg_pop_value = 0
            else:
                avg_pop_value = 0
            # Calculate the average return value and print it/store it
            curr_avg = curr[2][-1].get_avg(avg_pop_value)
            # exec("print(\"The average return for "+curr[0]+curr[1]+" is:"+str(curr_avg)+" \")")

            # Now that we have the average return, loop through the last 5 rows in the list to start compiling the
            # data needed to calculate the standard deviation
            for row in curr[2][-5:]:
                row.add_to_running_squared_sum(curr_avg)

            # Calculate the standard dev using the avg
            curr_std = curr[2][-1].get_std()
            # exec("print(\"The standard deviation of the return for "+curr[0]+curr[1]+" is:"+str(curr_std)+" \")")

            # Calculate the average standard dev
            if len(curr[2]) > 5:
                try:
                    pop_value = curr[2][-6].std_return
                except:
                    pop_value = 0
            else:
                pop_value = 0
            curr_avg_std = curr[2][-1].get_avg_std(pop_value)
            # exec("print(\"The average standard deviation of the return for "+curr[0]+curr[1]+" is:"+str(curr_avg_std)+" \")")

            # -------------------Investment Strategy-----------------------------------------------
            try:
                return_value = curr[2][-1].hist_return
            except:
                return_value = 0
            if isnan(return_value) == True:
                return_value = 0

            try:
                return_value_1 = curr[2][-2].hist_return
            except:
                return_value_1 = 0
            if isnan(return_value_1) == True:
                return_value_1 = 0

            try:
                return_value_2 = curr[2][-3].hist_return
            except:
                return_value_2 = 0
            if isnan(return_value_2) == True:
                return_value_2 = 0

            try:
                upp_band = curr[2][-1].avg_return + (1.5 * curr[2][-1].std_return)
                if return_value >= upp_band and curr[
                    3].Prev_Action_was_Buy == True and return_value != 0:  # (return_value > 0) and (return_value_1 > 0) and
                    curr[3].sell_curr(avg_price)
            except:
                pass

            try:
                loww_band = curr[2][-1].avg_return - (1.5 * curr[2][-1].std_return)
                if return_value <= loww_band and curr[
                    3].Prev_Action_was_Buy == False and return_value != 0:  # and  (return_value < 0) and (return_value_1 < 0)
                    curr[3].buy_curr(avg_price)
            except:
                pass



# This main function repeatedly calls the polygon api every 1 seconds for 24 hours
# and stores the results.
def main(currency_pairs, user_key=None):
    if not user_key:
        print("Please provide a key.")
        exit()

    # The api key given by the professor
    key = user_key

    # Number of list iterations - each one should last about 1 second
    count = 0
    agg_count = 0

    # Create an engine to connect to the database; setting echo to false should stop it from logging in std.out
    # change db name --> three_pairs.db
    engine = create_engine("sqlite+pysqlite:///three_pairs.db", echo=False, future=True)

    # Create the needed tables in the database
    initialize_raw_data_tables(engine, currency_pairs)
    initialize_aggregated_tables(engine, currency_pairs)

    # Open a RESTClient for making the api calls
    # change "with RESTClient(key) as client" -->  client = RESTClient(key)
    client = RESTClient(key)
    # with RESTClient(key) as client:
    # Loop that runs until the total duration of the program hits 24 hours.
    while count < 86400:  # 86400 seconds = 24 hours
        # Make a check to see if 6 minutes has been reached or not
        if agg_count == 360:
            # Aggregate the data and clear the raw data tables
            aggregate_raw_data_tables(engine, currency_pairs)
            reset_raw_data_tables(engine, currency_pairs)
            agg_count = 0

        # Only call the api every 1 second, so wait here for 0.75 seconds, because the
        # code takes about .15 seconds to run
        time.sleep(0.75)

        # Increment the counters
        count += 1
        agg_count += 1
        print(f"Progress: {count} / 86400")

        # Loop through each currency pair
        for currency in currency_pairs:
            # Set the input variables to the API
            from_ = currency[0]
            to = currency[1]

            # Call the API with the required parameters
            try:
                resp = client.forex_currencies_real_time_currency_conversion(from_, to, amount=100, precision=2)
            except:
                continue

            # This gets the Last Trade object defined in the API Resource
            last_trade = resp.last

            # Format the timestamp from the result
            dt = ts_to_datetime(last_trade["timestamp"])

            # Get the current time and format it
            insert_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            # Calculate the price by taking the average of the bid and ask prices
            avg_price = (last_trade['bid'] + last_trade['ask']) / 2

            # Write the data to the SQLite database, raw data tables
            with engine.begin() as conn:
                conn.execute(text(
                    "INSERT INTO " + from_ + to + "_raw(ticktime, fxrate, inserttime) VALUES (:ticktime, :fxrate, :inserttime)"),
                             [{"ticktime": dt, "fxrate": avg_price, "inserttime": insert_time}])
