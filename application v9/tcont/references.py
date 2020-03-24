### Module containing references from all content

try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk

# 'from page' for Mac, 'from tcont.page' for Windows
try:
    from page import Page
except ImportError:
    from tcont.page import Page

#########################################
# Define content window

class References(Page):
    def __init__(self, master):
        # Instance of Page for window formatting
        Page.__init__(self, master)
        self.master = master

        # Create content frame within a scrollable canvas
        content = Page.scrollable_canvas(self, master)

        #############
        # Top Title #
        #############
        title = tk.Label(
            content,
            text = 'References',
            font = 'Helvetica 24 bold')
        title.pack(pady = (15,0))

        refText = 'Brownlee, J., 2019. How to Check-Point Deep Learning '\
        'Models in Keras. [Online]\n'\
        'Available at: https://machinelearningmastery.com/check-point-deep-'\
        'learning-models-keras/\n'\
        '[Accessed 27 February 2020].\n\n'\
        \
        'Eremenko, K. & de Ponteves, H., 2017. Convolutional Neural Networks '\
        'Step 2 - Pooling, s.l.: Super Data Science Team.\n\n'\
        \
        'Goodfellow, I., Bengio, Y. & Courville, A., 2016. Deep Learning. '\
        'Online ed. s.l.:MIT Press.\n\n'\
        \
        'Keras, 2020. Keras: The Deep Learning Python Library. [Online]\n'\
        'Available at: https://keras.io\n'\
        '[Accessed 27 February 2020].\n\n'\
        \
        'Keras, 2020. Usage of callbacks. [Online]\n'\
        'Available at: https://keras.io/callbacks/\n'\
        '[Accessed 26 February 2020].\n\n'\
        \
        'Kingma, D. P. & Ba, J. L., 2015. Adam: A Method for Stochastic '\
        'Optimization. San Diego, ICLR.\n\n'\
        \
        'Kumar, V., 2017. What is the sigmoid function, and what is its use '\
        'in machine learning\'s neural networks? How about the sigmoid '\
        'derivative function?. [Online]\n'\
        \
        'Available at: https://www.quora.com/What-is-the-sigmoid-function-'\
        'and-what-is-its-use-in-machine-learnings-neural-networks-How-about-'\
        'the-sigmoid-derivative-function\n'\
        '[Accessed 10 February 2020].\n\n'\
        \
        'Mooney, P., 2018. Retinal OCT Images (optical coherence tomography). '\
        '[Online]\n'\
        'Available at: https://www.kaggle.com/paultimothymooney/kermany2018\n'\
        '[Accessed 27 February 2020].\n\n'\
        \
        'rhammell, 2018. Ships in Satellite Imagery. [Online]\n'\
        'Available at: https://www.kaggle.com/rhammell/ships-in-satellite-'\
        'imagery\n'\
        '[Accessed 1 March 2020].\n\n'\
        \
        'Swanson, E. A. & Fujimoto, J. G., 2017. The ecosystem that powered '\
        'the translation of OCT from fundamental research to clinical and '\
        'commercial impact [Invited]. Biomed Opt Express, 8(3), pp. 1638-1664.'
        ref = tk.Label(content, text = refText, wraplength = 700,
            justify = tk.LEFT)
        ref.pack()




# Just to view the page as it is:
if __name__ == '__main__':
    root = tk.Tk()
    home = References(root)
    root.mainloop()
