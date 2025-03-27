#######################################################################################################################################################
# 
# Name:AARYA RAJ
# SID:740097177
# Exam Date:27/03/2025
# Module:PROGRAMMING FOR BUSINESS ANLYTICS
# Github link for this assignment: https://github.com/UniversityExeterBusinessSchool/practiceassessment-thursday-aaryaraj15.git 
#
# ######################################################################################################################################################
# Instruction 1. Read the questions and instructions carefully and complete scripts.

# Instruction 2. Only ethical and minimal use of AI is allowed. You might use AI to give advice on how to use a tool or programming language.  
#                You must not use AI to create the code. You might make use of AI to aid debugging of the code.  
#                You must indicate clearly how and where you have used AI.

# Instruction 3. Copy the output of the code and insert it as a comment below your code e.g # OUTPUT (23,45)

# Instruction 4. Ensure you provide comments for the code and the output to show contextual understanding.

# Instruction 5. Upon completing this test, commit to Git, copy and paste your code into the word file and upload the saved file to ELE.
#                There is a leeway on when you need to upload to ELE, however, you must commit to Git at 
#                the end of your session.

# ######################################################################################################################################################
# Question 1 - Loops
# Create a list and use a for loop to answer the following question:
# You are given a dictionary called key_comments. Your allocated keys are the first and last digit of your SID.
# Find the start and end position of each of the items in the sentence using the find command.
# Create and populate a list called my_list with a tuple of (start location, end location) for each value in comments 
 

customer_feedback = """Your recent order experience has been satisfactory overall. While there were some minor issues,
we appreciate the effort made to resolve them promptly."
"""

# List of words to search for
key_comments = {
    0: 'satisfactory',
    1: 'order',
    2: 'effort',
    3: 'issues',
    4: 'promptly',
    5: 'appreciate',
    6: 'experience',
    7: 'resolve',
    8: 'overall',
    9: 'minor'
}

# Write your search code here and provide comments. 

# Initialize an empty list to store (start, end) positions
my_list = []
for word in word.values()
start = text.find(word)
if start != -1:
    end = start+len(word)
    my_list.append ((start,end))
    print(my_list)

##########################################################################################################################################################

# Question 2 - Functions
# Scenario - You are working in an e-commerce firm as a business analyst, and your manager has tasked you to generate weekly reports on financial metrics like 
# Operating Profit Margin, Revenue per Customer, Customer Churn Rate, and Average Order Value. Use Python functions 
# that will take the values and return the metric needed. Use the first two and last two digits of your ID number as the input values.

# Insert first two digits of ID number here:74
# Insert last two digits of ID number here:77

# Write your code for Operating Profit Margin

def profit_margin (revenue,profit):
    return (profit/revenue * 100)
revenue = 7400
profit = 740
print("operating profit margin:",round (profit_margin(revenue,profit),2,"%"))


# Write your code for Revenue per Customer

def revenue_per_customer(revenue,customer):
    return revenue/customer
revenue = 7400
profit =740
print("revenue per customer:",round (revenue_per_customer(revenue,customer),2))



# Write your code for Customer Churn Rate

def churn_rate(lost_customers,total customers):
    return (lost customer/total customer) * 100
lost = 77
tota; = 770
print("customer churn rate:",round(churn rate (lost,total),2),"%")

# Write your code for Average Order Value

def avg_order_value(evenue,order):
    return revenue/order
revenue = 77
orderv = 770
print("average order value:"round(avg_order_value(revenue,order),2))


# Call your designed functions here

##########################################################################################################################################################

# Question 3 - Regression
# A retail store has collected data on seasonal sales and price changes. The table below shows different price levels and their corresponding demand.
# Develop a linear regression model and determine:
# 1. The price at which the store can maximize revenue
# 2. The demand when the price is set at £52

"""
Price (£)    Demand (Units)
---------------------------
20           300
25           280
30           260
35           240
40           210
45           190
50           160
55           140
60           120
65           100
70           85
"""

# Write your code here

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

#PRICES AND DEMAND
x = np.array([20,25,30,35,40,45,50,55,60,65,70]),reshape(-1,1)
y = np.array([300,280,260,240,210,190,160,140,120,100,85])

model = LinearRegression()
model.fit(x,y)

print("demand at £52: ",round(model.predict([[52]]),[0],2))
price = np.arange(20,71,1).reshape(-1,1)
revenues = prices.flatten() * model.predict(prices)
best_price = prices[np.argmax(revenues)][0]
print("best price for max revenue at : £ ",best_price)

#plot
plt.plot(prices,revenue,color = "red")
plt.axvline(best_price,color = "blue",linestyle("--"))
plt.xlabel = ("price (£)")
plt.ylabel = ("revenue (£)")
plt.title("price vs. revenue")
plt.grid(True)
plt.show()


##########################################################################################################################################################

# Question 4 - Debugging; Plotting and data visualization chart

import random
import matplotlib.pyplot as plt

# Generate 100 random numbers between 1 and student id number
max_value = int(input("Enter your Student ID: "))
random_numbers = [random.randint(1, max_value) for i in range(0,100)]

# Plotting the numbers in a line chart
plt.plot(random_numbers, marker = 'o', markercolor = 'green', markeredgcolor = 'red', linestyle = '--', lable = 'Random Numbers', color = 'blue')
plt.title("Line Chart of 100 Random Numbers")
plt.xlabel=("Index")
plt.ylabel=("Random Number")
plt.legend()
plt.grid(True)
plt.show()



