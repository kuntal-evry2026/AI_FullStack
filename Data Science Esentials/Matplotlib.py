import matplotlib.pyplot as plt

#basic line plot

x= [1,2,3,4,5]
y= [2,3,4,5,6]
plt.plot(x,y)
plt.title("Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()


#line plot 
plt.plot([6,7,8],[60,70,80] ,label = "trend" , color = "Red" , linestyle = "--" ,marker = "o" )
plt.title("Line Plot")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend()
plt.show()


#Bar chart 
catagories = ["a","b","C"]
values = [10,15,17]
plt.bar (catagories,values,color = "Blue")
plt.title("Bar Chart")
plt.show()

#Histogram 
hist = [78,90,34,50,65]
plt.hist(hist,color="green",edgecolor = "black")
plt.title("Histogram")
plt.show()

#scatter plot

b= [12,23,34,45,56,78,90]
c= [1,2,3,4,5,6,7]
plt.scatter(b,c,color = "blue")
plt.title("Scatter Plot")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend(["dataset"])
plt.show()
