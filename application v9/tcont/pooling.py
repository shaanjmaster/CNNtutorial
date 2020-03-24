### Module containing the second part of the CNN content:
#   the pooling step

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
# Define Pooling Step Tutorial window

class Pooling(Page):
    def __init__(self, master):
        # instance of Page to format window
        Page.__init__(self, master)

        # Create content frame within a scrollable canvas as defined in Page
        content = Page.scrollable_canvas(self, master)

        # Pooling Step content begins...
        # Top Title
        title = tk.Label(content, text = 'Pooling Step',
            font = 'Helvetica 24 bold')
        title.pack(side = tk.TOP, pady=15)

        # First part of content
        para1Text = 'A feature may not appear in the same location and may '\
        'exhibit some form of small transformation between different images.\n'\
        'However, the feature is still the same, so it is important for the '\
        'neural network to identify it as such.\nThe ability to recognise a '\
        'feature even when it may appear in a different location or have some '\
        'shift or transformation is called spatial invariance.\n'
        para1 = tk.Label(content, text = para1Text)
        para1.pack()

        # Second part of the content
        para2Text = 'Pooling is a method to enable approximate spatial '\
        'invariance to small translations.\n'\
        'This occurs by applying a rectangular box to the feature map and '\
        'taking a value based on the values contained within the box.\n'\
        'This could be the maximum value, the mean of the values, or the '\
        'weighted mean of the values based on their distance from the centre.\n'\
        'Essentially, pooling produces an output at a location that is a '\
        'summary of nearby outputs.\n\n'\
        'The use of pooling also improves the computational efficiency of the '\
        'network as the pooled feature map contains fewer input units than '\
        'the feature map before pooling does.'
        para2 = tk.Label(content, text = para2Text)
        para2.pack()

        # Max pooling example image from Udemy course
        self.maxPoolUd = tk.PhotoImage(
            file = Page.load_image(self, 'maxPoolUd.gif')
            )
        fig4 = tk.Label(content, image = self.maxPoolUd)
        fig4.pack()

        # Caption for the above image
        fig4cap = 'Figure 4: An example of max pooling is shown with a 2x2 '\
        'box applied and a stride of 2 pixels.\n'\
        'The maximum value within the box is the value transferred to the '\
        'pooled feature map, as shown with the value 4 in the pooling box '\
        'moved to the pooled feature map.\n(Eremenko & de Ponteves, 2017)'
        fig4caption = tk.Label(content, text = fig4cap, font = self.italic)
        fig4caption.pack()

        # Flattening title
        flattening = tk.Label(content, text = 'Flattening', font = self.bold)
        flattening.pack()

        # Flattening text
        para3Text = 'After completing the desired number of convolution and '\
        'pooling layers, the data is fed through an artificial neural network '\
        'as described in the Deep Learning module.\n'\
        'In order for this to occur, the data is flattened, meaning the final '\
        'pooled feature maps are put into a single column, row by row.\n'\
        'The flattened data is then fed through a fully connected ANN. In the '\
        'example from figure 4, that would mean a column with values '\
        '[1, 1, 0, 4, 2, 1, 0, 2, 1].\n\n'\
        \
        'Click "Basic Example" to see these concepts more practically!\n'
        para3 = tk.Label(content, text = para3Text)
        para3.pack()


# Just to view the page as it is:
if __name__ == '__main__':
    root = tk.Tk()
    home = Pooling(root)
    root.mainloop()
