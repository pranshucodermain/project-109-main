import pandas as pd 
import plotly.graph_objects as go 
import plotly.figure_factory as ff
import random
import statistics

df  = pd.read_csv ("StudentsPerformance.csv")
data = df ["reading score"].tolist()
#calculating mean, median, mode, std dev
mean = sum(data)/len(data)
std_deviation = statistics.stdev(data)
median = statistics.median(data)
mode = statistics.mode(data)

print ("the mean of the height is ",mean)
print ("the median of the height is ",median)
print ("the mode of the height is ",mode)
print ("the standarddeviation of data ",std_deviation)
# in a data set which follows a normal distribution , the mean median mode are all ways , the mean median mode are all ways equal 

#fig = ff.create_distplot([dice_result], ["Result"], show_hist = False )
#fig.show()

#finding the percentage of data between 1st standard deviation
first_std_deviation_start, first_std_deviation_end = mean - std_deviation, mean+std_deviation
second_std_deviation_start, second_std_deviation_end = mean - (2*std_deviation), mean+(2*std_deviation)
third_std_deviation_start, third_std_deviation_end  = mean -(3*std_deviation), mean+(3*std_deviation)

fig= ff.create_distplot([data],["Result"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0,0.17], mode="lines", name= "MEAN"))
fig.add_trace(go.Scatter(x=[first_std_deviation_start,first_std_deviation_start], y=[0,0.17], mode="lines", name= "STANDARD DEVIATION 1 START"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end,first_std_deviation_end], y=[0,0.17], mode="lines", name= "STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start,second_std_deviation_start], y=[0,0.17], mode="lines", name= "STANDARD DEVIATION 2 START"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end,second_std_deviation_end], y=[0,0.17], mode="lines", name= "STANDARD DEVIATION 2 END"))
fig.show()
# empirical rule states that 68% of data falls with in one standeviation 
# under the same rule 95% of data lies in two standeviation 
# under the same rule 99% of data lies in three standeviation

list_of_data_within_1_std_deviation = [result for result in data if result > first_std_deviation_start and result < first_std_deviation_end]
list_of_data_within_2_std_deviation = [result for result in data if result > second_std_deviation_start and result < second_std_deviation_end]
list_of_data_within_3_std_deviation = [result for result in data if result > third_std_deviation_start and result < third_std_deviation_end]

print("{}% of data lies within 1 standard deviation".format(len(list_of_data_within_1_std_deviation)*100.0/len(data)))
print("{}% of data lies within 2 standard deviation".format(len(list_of_data_within_2_std_deviation)*100.0/len(data)))
print("{}% of data lies within 3 standard deviation".format(len(list_of_data_within_3_std_deviation)*100.0/len(data)))