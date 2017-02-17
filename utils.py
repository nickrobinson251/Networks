from collections import Iterable
import matplotlib.pyplot as plt


styles = dict(font_color='white',
              font_size=20,
              node_size=1000)

def show_graph(axes=None):
    '''Display figure without axes.
    
    Parameters
    ----------
    axes : array-like
	Iterable of matplotlib axes
    '''
    if isinstance(axes, Iterable):
        for ax in axes:
            ax.axis('off')
    else:
        plt.axis('off')
    plt.show()

