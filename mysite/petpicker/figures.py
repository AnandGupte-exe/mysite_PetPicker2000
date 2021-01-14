import matplotlib.pyplot as plt

def my_figure():
    x = [1, 3, 4]
    y = [3, 2, 5]
    fig, ax = plt.subplots()
    ax.plot(x,y)
    return fig
