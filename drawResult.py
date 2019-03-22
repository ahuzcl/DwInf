import matplotlib.pyplot as plt

def draw():
    plt.figure(1)
    plt.title("Influence Spread in IC Model Dataset:Karate p=similarity(DeepWalk Dimension=2")
    plt.xlabel("Seed Size")
    plt.ylabel("Influence Spread")
    x = [5,10,15,20,25,30]
    y0 = [9.2613,15.6964,19.9946,24.1634,28.1522,31.191] #random
    y1 = [10.9236,14.9033,19.0437,22.7787,26.7159,30.7111]#Degree
    plt.plot(x, y0, 'cx-', marker='h', label="random")
    plt.plot(x, y1, 'mx-', marker='h', label="Degree")
    plt.legend()
    plt.show()

if __name__ == '__main__':
    draw()
