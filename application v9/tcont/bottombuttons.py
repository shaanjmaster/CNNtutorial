# This file contains a frame that should be packed at the bottom of the content
#   frame of each content page

try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk

class BottomButtons(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        self.master_frame = self.master.master.master.master

        ###############################
        # Second Button Frame (lower) #
        ###############################

        buttonFrame2 = tk.Frame(self.master)
        buttonFrame2.pack(side = tk.BOTTOM, pady = (0,25))

        # Ships example with code explanation
        shipsExampleButton = tk.Button(buttonFrame2,
            text = 'Ships Example (Binary)',
            command = self.ships_example)
        shipsExampleButton.grid(row = 0, column = 0)

        # Save and loading explanation
        saveLoadButton = tk.Button(buttonFrame2, text = 'Saving and Loading',
            command = self.saving_loading)
        saveLoadButton.grid(row = 0, column = 1)

        # Retinal OCT example
        retOCTExampleButton = tk.Button(buttonFrame2,
            text = 'Retinal OCT Example (Categorical)',
            command = self.oct_example)
        retOCTExampleButton.grid(row = 0, column = 2)

        # References Example
        referencesButton = tk.Button(buttonFrame2,
            text = 'References',
            command = self.references)
        referencesButton.grid(row = 0, column = 3)


        ##############################
        # First Button Frame (upper) #
        ##############################

        buttonFrame1 = tk.Frame(self.master)
        buttonFrame1.pack(side = tk.BOTTOM, pady = (25,5))

        # Define the button that will open the home page
        homeButton = tk.Button(buttonFrame1, text = 'Home',
            command = self.go_home)
        homeButton.grid(row=0, column=0)

        # Create convolution step button
        convStepButton = tk.Button(buttonFrame1, text = 'Convolution Step',
            command = self.convolution_step)
        convStepButton.grid(row = 0, column = 1)

        # Pooling step button
        poolingButton = tk.Button(buttonFrame1, text = 'Pooling Step',
            command = self.pooling_step)
        poolingButton.grid(row = 0, column = 2)

        # Basic example without code button
        basicExampleButton = tk.Button(buttonFrame1, text = 'Basic Example',
            command = self.basic_example)
        basicExampleButton.grid(row = 0, column = 3)


    ###################
    # Button Commands #
    ###################

    # Define function to take the user to home page, command for home button
    def go_home(self):
        # Destroys the parent of the content frame, i.e. the 'Page' frame
        self.close()
        # Import the desired page
        # 'from homepage' for Mac, 'from tcont.homepage' for Windows
        try:
            from homepage import HomePage
        except ImportError:
            from tcont.homepage import HomePage
        # Create instance of desired page in the parent of the parent, i.e. root
        home = HomePage(self.master_frame)

    def convolution_step(self):
        # Destroy current page
        self.close()
        # Import convolution step page
        try:
            from convstep import ConvStep
        except ImportError:
            from tcont.convstep import ConvStep
        # Create instance of convolution step page
        convStep = ConvStep(self.master_frame)

    def pooling_step(self):
        # Destroy current Page
        self.close()
        # Import pooling step page
        try:
            from pooling import Pooling
        except ImportError:
            from tcont.pooling import Pooling
        # Create instance of pooling step Page
        pooling = Pooling(self.master_frame)

    def basic_example(self):
        # Destroy current Page
        self.close()
        # Import basic example page
        try:
            from basicexample import BasicExample
        except ImportError:
            from tcont.basicexample import BasicExample
        # Create instance of pooling step Page
        basic = BasicExample(self.master_frame)

    def ships_example(self):
        # Destroy current window
        self.close()
        # Import ships example page
        try:
            from shipsEx import ShipsEx
        except ImportError:
            from tcont.shipsEx import ShipsEx
        # Create instance of ships example page
        ships = ShipsEx(self.master_frame)

    def saving_loading(self):
        # Destroy current window
        self.close()
        # Import the saving and loading page
        try:
            from save_load import SaveLoad
        except ImportError:
            from tcont.save_load import SaveLoad
        # Create instance of saving and loading explanation page
        saveload = SaveLoad(self.master_frame)

    def oct_example(self):
        # Destroy current window
        self.close()
        # Import the OCT example page
        try:
            from octEx import OCTEx
        except ImportError:
            from tcont.octEx import OCTEx
        # Create instance of OCT example page
        oct_ex = OCTEx(self.master_frame)

    def references(self):
        # Destroy current window
        self.close()
        # Import the references page
        try:
            from references import References
        except ImportError:
            from tcont.references import References
        # Create instance of references page
        ref = References(self.master_frame)


    #########################
    # General function to close window
    def close(self):
        # Destroys the parent of the content frame, i.e. the 'frame' Frame
        # 'content' Frame -> 'canvas' Canvas -> 'frame' Frame being destroyed
            # in scrollable_canvas in Page class
        self.master.master.master.destroy()

# Just to view the page as it is:
if __name__ == '__main__':
    root = tk.Tk()
    home = BottomButtons(root)
    root.mainloop()
