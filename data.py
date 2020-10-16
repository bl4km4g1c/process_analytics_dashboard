
import numpy as np
import pandas as pd
import datetime as dt
# import dash_daq as dq
# from charts_page import remove_duplicates as remove_duplicates_measures
# import pandas as pd


# build a class for data generation - so that I can put all data functions into


class _datagen_():

    # generate raw data -- replace with queries eventually

    def live_data():

        # generate live data - every 10 seconds
        # look at how - i did it with other project.... at home
        # need to create a callback for the graph it's looking at

        data = np.random.randn(1)
        time_stamp = dt.datetime.now()

        # d = {'data': data, 'time': time_stamp}

        return data, time_stamp    # pd.DataFrame(d)

    def generate_data(size, width):

        # create dictionary
        d = {}

        for i in range(width):
            d["cpp{0}".format(i)] = np.random.randn(size)

        # d = {'process1': cpp1, 'process2': cpp2}
        return pd.DataFrame(d)

    def create_control_data(df):

        # find df size

        length, width = df.shape
        # create dictionary
        d = {}
        # length of historical RAG check
        RAG_history = 30

        # rebuild to only do first and last position entries
        # to save on processing power

        for i in range(width):

            # get list at position
            list_at_i = df.iloc[:, i]

            # find name of column
            col = df.columns[i]

            # create statistical indicators

            x_bar = np.average(list_at_i[0:29]) * np.ones(length)
            x_sigma = np.std(list_at_i[0:29])
            UCL = x_bar + 3*x_sigma
            LCL = x_bar - 3*x_sigma

            rules = []

            # create array for rules
            for j in range(length):
                # basic 3 sigma violation
                if list_at_i[j] > UCL[0] or list_at_i[j] < LCL[0]:
                    rules.append(list_at_i[j])
                else:
                    rules.append(None)

            # Create array for RAG check
            RAGcheck = []
            for j in range(length):
                if j < RAG_history:
                    tester = all(x == None for x in rules[0:j])
                    RAGcheck.append(tester)
                else:
                    tester = all(x == None for x in rules[j-RAG_history:j])
                    RAGcheck.append(tester)

            d["x_bar{0}".format(col)] = x_bar
            d["x_sigma{0}".format(col)] = x_sigma
            d["UCL{0}".format(col)] = UCL
            d["LCL{0}".format(col)] = LCL
            d["rules{0}".format(col)] = rules
            d["RAG{0}".format(col)] = RAGcheck

        return pd.DataFrame(d, index=df.index)

    def data_request(url):

        df = pd.read_csv(url)
        # print (df)

        return df

    def modify_df2(df2, successful_tries):
        # # will use this if indexing on measures doesnt work
        second_df_mod = []
        for i in range(len(successful_tries)):
            # print (successful_tries[i])
            for j in range(len(df2.columns)):
                # print (df2.columns[j])
                if successful_tries[i] in df2.columns[j]:
                    # print (successful_tries[i] + " " + df2.columns[j])
                    second_df_mod.append(df2.columns[j])

        # print (second_df_mod)

        new_df = df2[second_df_mod]
        return new_df
    
    def dropdown_times(df, df2, start_date):
        df = df[df.index >= start_date]
        df2 = df2[df2.index >= start_date]
        return df, df2

# create cards for homepage
