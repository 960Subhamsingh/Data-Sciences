# from dash import Dash, html

# app = Dash()

# app.layout = [html.Div(children='Hello World')]

# if __name__ == '__main__':
#     app.run(debug=True)


import matplotlib.pyplot as plt
# initializing the data
x = [10, 20, 30, 40]
y = [20, 30, 40, 50]
# plotting the data
plt.plot(x, y)
# Adding the title
plt.title("Simple Plot")
# Adding the labels
plt.ylabel("y-axis")
plt.xlabel("x-axis")
plt.show()