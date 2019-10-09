from statistics import mean
import numpy as np
import matplotlib.pyplot as plt


def best_fit_slope(x,y):
    m = (((mean(x) * mean(y))) - mean(x*y)) / ((mean(x) * mean(x)) - mean(x*x))
    return m

def intercept(x,y,m):
    b = mean(y) - m*mean(x)
    return b

def squared_error(y_orig , y_line):
    return sum((y_line - y_orig)**2)




if __name__ == '__main__':
    x = np.array([1, 2, 3, 4, 5, 6], dtype=np.float)
    y = np.array([5, 4, 6, 5, 6, 7], dtype=np.float)
    m = best_fit_slope(x,y)
    print(m)

    b = intercept(x,y,m)
    print(b)

    #y = mx+b
    regressor_line = [(m*x)+b for x in x]


    predict_x = 8
    predict_y = (m*predict_x)+b



    plt.scatter(x,y , color = "red")
    plt.scatter(predict_x , predict_y , color = "yellow")
    plt.plot(x , regressor_line)
    plt.show()

    error = squared_error(y , regressor_line)
    print(error)
