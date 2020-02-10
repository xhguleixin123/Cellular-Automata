import matplotlib.pyplot as plt
import numpy as np


class Autocell(object):
    """
    实例化
    width : 元胞数组的宽度
    height ： 元胞数组的宽度
    从而实例化 cells 元胞数组
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = np.random.randint(0, 2, (width, height))

    """
    向周围八个格子方向滚动，并相加，得到格子周围的活着的元胞数
    周围3个重生变为1
    周围2个且为1，则为1
    """
    def next_gengeration(self):
        nbrs_count = sum(np.roll(np.roll(self.cells, i, 0), j, 1)
                         for i in (-1, 0, 1) for j in (-1, 0, 1)
                         if (i != 0 or j != 0))
        self.cells = (nbrs_count == 3) | ((self.cells == 1) & (nbrs_count == 2)).astype('int')

    """
    画元胞数组
    """
    def plot_current_cells(self, iters):
        ax = plt.gca()
        ax.patch.set_facecolor('gray')
        ax.set_aspect('equal', 'box')

        # ax.xaxis.set_major_locator(plt.NullLocator())
        # ax.yaxis.set_major_locator(plt.NullLocator())
        plt.ion()
        for i in range(iters):
            ax.cla()
            plt.xticks(())
            plt.yticks(())
            for i in range(self.width):
                for j in range(self.height):
                    color = 'gray' if not self.cells[i, j] else 'black'
                    rect = plt.Rectangle([i * 1.2 + 0.2, j * 1.2 + 2], 1, 1, facecolor=color, edgecolor=color)
                    ax.add_patch(rect)
            ax.autoscale_view()
            plt.show()
            self.next_gengeration()
            plt.pause(0.2)
        plt.ioff()

if __name__ == '__main__':
    autocell = Autocell(10,20)
    autocell.plot_current_cells(20)