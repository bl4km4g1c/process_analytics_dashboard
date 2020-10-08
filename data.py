
import numpy as np
import pandas as pd
import datetime as dt

#build a class for data generation - so that I can put all data functions into
class _datagen_():
    
    #generate raw data -- replace with queries eventually
    
    def live_data():
        
        #generate live data - every 10 seconds
        #look at how - i did it with other project.... at home
        # need to create a callback for the graph it's looking at
        
        data = np.random.randn(1)
        time_stamp = dt.datetime.now()
        
        #d = {'data': data, 'time': time_stamp}
        
        return data, time_stamp #pd.DataFrame(d)
    
    def generate_data(size, width):
        
        #create dictionary
        d = {}
        
        for i in range(width):
            d["cpp{0}".format(i)] = np.random.randn(size)
        
        #d = {'process1': cpp1, 'process2': cpp2}
        return pd.DataFrame(d)
    
    def create_control_data(df):
        
        #find df size
        length, width = df.shape
        #create dictionary
        d = {}
        
        #rebuild to only do first and last position entries to save on processing power
        for i in range(width):
            #get list at position
            list_at_i = df.iloc[:, i]
            #create statistical indicators
            x_bar = np.average(list_at_i[0:29]) * np.ones(length)
            x_sigma = np.std(list_at_i[0:29])
            UCL = x_bar + 3*x_sigma
            LCL = x_bar - 3*x_sigma
            
            rules = []
            #create array for rules
            for j in range(length):
                #basic 3 sigma violation
                if list_at_i[j] > UCL[0] or list_at_i[j] < LCL[0]:
                    rules.append(list_at_i[j])
                else:
                    rules.append(None)
                    
            d["x_bar{0}".format(i)] = x_bar
            d["x_sigma{0}".format(i)] = x_sigma
            d["UCL{0}".format(i)] = UCL
            d["LCL{0}".format(i)] = LCL
            d["rules{0}".format(i)] = rules
            
        return pd.DataFrame(d)
            
        
# ##testing
# df = _datagen_.generate_data(100, 3)
# df2 = _datagen_.create_control_data(df)
# print (df.head)
# print (df.shape)
# print (df2.head)
# print (df2.shape)
# print (df2.columns)

#test case for generation of live data.... put into graph and make expandable
df = pd.DataFrame(columns = ['time', 'data'])

for i in range(100):
    
    data, time = _datagen_.live_data()
    df = df.append({'time': time, 'data': data}, ignore_index = True)
    #print("Data is: {}, Time is: {}".format(data, time))

#print(df.head)
#print(df.iloc[:,0])  
    
    

# def generate_data(size):
    
#     ###dummy data
#     x = np.arange(size)
#     rules = []
#     process_parameter = []
#     #change y0 and y2 to UCL and LCL then add average....
#     #next need to create rules for this function
#     data_set = np.random.randn(size)
#     data_set2 = np.random.randn(size)
#     x_bar = np.average(data_set[0:29]) * np.ones(size) 
#     x_sigma = np.std(data_set)
#     UCL = x_bar + 3*x_sigma
#     LCL = x_bar - 3*x_sigma
    
#     #create an array for rules
#     for i in range(size):
#         #basic 3 sigma violation
#         if data_set[i] > UCL[0] or data_set[i] < LCL[0]:
#             rules.append(data_set[i])
            
#         else:
#             rules.append(None)
#         if i%2 == 0:
#             process_parameter.append('Process 1')
#         else:
#             process_parameter.append('Process 2')

#     d = {'machine': machine,'x': x, 'data': data_set,'data2': data_set2, 'x_bar': x_bar, 'UCL': UCL, 'LCL': LCL, 'Viol': rules}
#     df = pd.DataFrame(d)
    
    
#     return df

# def generate_spark(size):
    
#     ###dummy data
#     x = np.arange(size)
#     machine = []
#     data_set = np.random.randn(size)
#     data_set2 = np.random.randn(size)
#     for i in range(size):
        
#         if i%2 == 0:                    
#             machine.append('Machine 1')
#         else:
#             machine.append('Machine 2')

#     d = {'machine': machine, 'data': data_set, 'data2': data_set2}
#     df = pd.DataFrame(d)
    
    
#     return df

# #df = generate_spark(1000)


# #print(df)