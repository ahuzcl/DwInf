import matplotlib.pyplot as plt

def drawXiaomi():
    plt.figure(1)
    plt.title("Influence Spread in IC Model Dataset:Weibo Topic officer   ")
    plt.xlabel("Seed Size")
    plt.ylabel("Influence Spread")
    x = [5,10,15,20,25,30]
    y0 = [6.73, 11.85, 16.92 ,21.54, 26.73 ,31.84]
    y1= [6.02 ,11.37 ,15.84, 21.07, 26.11, 31.32]
    y2= [5.22 ,10.41 ,15.62 ,20.54 ,25.71, 30.77]
    y3= [6.25 ,11.73 ,16.07 ,21.33 ,26.47, 31.49]
    y4= [7.31 ,12.15 ,18.47 ,23.11, 29.28, 32.92]

    plt.plot(x,y0,'mx--',marker='*',label="Greedy")
    plt.plot(x,y1,'bx-.',marker='*',label="degree")
    plt.plot(x,y2,'cx-.',marker='*',label="random")
    plt.plot(x,y3,'rx-.',marker='*',label="csa")
    plt.plot(x,y4,'yx:',marker='*',label="csa-data")
    plt.legend()
    plt.show()

if __name__ == '__main__':
    drawXiaomi()