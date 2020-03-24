### Module explaining how to save and load your neural nets

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

class SaveLoad(Page):
    def __init__(self, master):
        # Instance of Page for window formatting
        Page.__init__(self, master)
        self.master = master

        # Create content frame within a scrollable canvas
        content = Page.scrollable_canvas(self, master)

        #####################################
        # Saving and Loading content begins #
        #####################################

        # Top Title
        title = tk.Label(
            content,
            text = 'Saving and Loading Your Networks',
            font = 'Helvetica 24 bold')
        title.pack(pady = (15,0))

        # Introduction Title
        intro = tk.Label(content, text = 'Introduction', font = self.bold)
        intro.pack()

        # Paragraph 1: Introduction
        para1Text = 'This section will explain how you can save and '\
        'eventually load the model you have made and trained with Keras.\n'\
        'Not only is this useful to be able to load your model without going '\
        'through the training process again; you are also reducing the '\
        'risk of losing all your training progress if something does go '\
        'wrong!\n\n'\
        \
        'The information here is based on a post in Machine Learning Mastery '\
        '(Brownlee, 2019) as well as the Keras documentation site '\
        '(Keras, 2020).\n'\
        'You should have already gone through the Ships Example to complete '\
        'this section.\n'\
        'If you haven\'t, scroll to the bottom of the page and click '\
        '"Ships Example". You must also have the h5py library installed, '\
        'which you can do using the command:\nconda install h5py.\n'
        para1 = tk.Label(content, text = para1Text)
        para1.pack()

        # Saving title
        saving = tk.Label(content, text = 'Saving Your NN', font = self.bold)
        saving.pack()

        # Paragraph 2: Saving introduction
        para2Text = 'When running the training process on your model, using '\
        'the ModelCheckpoint callback will enable you to save each version '\
        'of the model.\n'\
        'It will overwrite the prior save with each callback.\n'\
        'This is done by creating an instance of ModelCheckpoint before using '\
        'the fit_generator method.\n'\
        'In this example, a callback is being added to the ships example.\n'\
        'The code can be found in the shipsSaved.py file.'
        para2 = tk.Label(content, text = para2Text)
        para2.pack()

        # Figure 1: Creating a callback to add to fit_generator()
        self.fig1callback = tk.PhotoImage(
            file = Page.load_image(self, 'save_load/fig1callback.gif')
        )
        fig1 = tk.Label(content, image = self.fig1callback)
        fig1.pack()

        fig1caption = 'Figure 1: Creating a callback to add to fit_generator().'
        fig1cap = tk.Label(content, text = fig1caption, font = self.italic)
        fig1cap.pack()

        # Paragraph 3: Callback explanation
        para3Text = 'When looking back at the ships example in shipsSaved.py, '\
        'the new code has been added in Step 8.\n'\
        'First, the ModelCheckpoint callback must be imported. Then, an '\
        'instance of ModelCheckpoint is created under the variable '\
        '"classifierCheckpoint".\n\n'\
        \
        'The first argument for ModelCheckpoint is filepath. The value should '\
        'be a string, indicating where you would like the file to be saved '\
        'from the working directory.\n'\
        'In this case, the working directory is "1 ships ex", and within '\
        'that, the model will be saved to the "ships_models" directory as '\
        '"1shipsModel.h5".\n'\
        'h5 is the filetype, an HDF5 file. Within this file, the model that '\
        'we have called "classifier" will be saved, including its '\
        'architecture, weights, and optimiser state.\n\n'\
        \
        'Next is the "save_best_only" argument, set to True.\n'\
        'This means that if the monitored value on the current model is '\
        'better than the monitored value of the previously saved model, '\
        'then the previous model will be overwritten with the new model.\n\n'\
        \
        'The "monitor" argument specifies which parameter is being used to '\
        'determine which version of the model to save.\n'\
        'Here, "val_loss" is used, so the validation loss is used to evaluate '\
        'whether or not the model should be saved.\n'\
        'Since we want to minimise loss, the lower value is used.\n'\
        'It is possible to specify that the maximum value is used using the '\
        '"mode" argument, however the default automatically selects based on '\
        'whether accuracy or loss is used.\n\n'\
        \
        'More arguments can be found on the Keras documentation, including '\
        'how frequently to run the checkpoint, but this is all that is '\
        'necessary here.\n\n'\
        \
        'Once the classifierCheckpoint has been defined, a list of the '\
        'callbacks created must be created.\n'\
        'Since this is the only callback used, the list simply contains '\
        'classifierCheckpoint.\nThen, the generator is fit to the model:'
        para3 = tk.Label(content, text = para3Text)
        para3.pack()

        # Figure 2: Fitting the generator to the model
        self.fig2fitGenerator = tk.PhotoImage(
            file = Page.load_image(self, 'save_load/fig2fitGenerator.gif')
        )
        fig2 = tk.Label(content, image = self.fig2fitGenerator)
        fig2.pack()

        fig2caption = 'Figure 2: Fitting the generator to the model, with '\
        'the addition of the callbacks argument.'
        fig2cap = tk.Label(content, text = fig2caption, font = self.italic)
        fig2cap.pack()

        # Paragraph 4: Callbacks argument
        para4Text = 'The only difference between this function call in '\
        'shipsSaved.py vs ships_CNN.py is the extra argument at the end.\n'\
        '"callbacks" is where we set the callbacks used in the training '\
        'process, as sorted in the list previously created.\n'\
        'That\'s all it takes to save the best version of your model after '\
        'each epoch!\n'
        para4 = tk.Label(content, text = para4Text)
        para4.pack()

        ######################################
        # Loading and Applying Trained Model #
        ######################################

        loading = tk.Label(
            content,
            text = 'Loading and Applying the Saved Trained Model',
            font = self.bold
        )
        loading.pack()

        # Loading intro
        loadingIntro = 'Now let\'s look at how to load this saved model and '\
        'make some predictions.\n'\
        'The full script that will be explained below can be found in the '\
        'ships example directory, under the file shipsReloaded.py.'
        loadingIntroLbl = tk.Label(content, text = loadingIntro)
        loadingIntroLbl.pack()

        # Figure 3: Imports
        self.fig3imports = tk.PhotoImage(
            file = Page.load_image(self, 'save_load/fig3imports.gif')
        )
        fig3 = tk.Label(content, image = self.fig3imports)
        fig3.pack()

        fig3caption = 'Figure 3: Import the necessary modules'
        fig3cap = tk.Label(content, text = fig3caption, font = self.italic)
        fig3cap.pack()

        # Paragraph 5: Imports
        para5Text = 'Firstly, you must import the necessary modules.\n'\
        'Whilst we have imported Sequential in shipsSaved.py, it must be '\
        'imported again to ensure it is available when running this separate '\
        'script.\n'\
        'The other import, keras.models load_model is what is used to '\
        'recompile the model from the HDF5 file that we just saved the '\
        'model to.'
        para5 = tk.Label(content, text = para5Text)
        para5.pack()

        # Figure 4: loading the model
        self.fig4load_model = tk.PhotoImage(
            file = Page.load_image(self, 'save_load/fig4load_model.gif')
        )
        fig4 = tk.Label(content, image = self.fig4load_model)
        fig4.pack()

        fig4caption = 'Figure 4: Load the saved model with the load_model() '\
        'function.'
        fig4cap = tk.Label(content, text = fig4caption, font = self.italic)
        fig4cap.pack()

        # Paragraph 6: reload classifier
        para6Text = 'Now the model can be loaded from the saved file. '\
        'It should be loaded under a variable so it can be called again when '\
        'we need to make predictions.\n'\
        'Here, I have called it "classifierReloaded". The model is being '\
        'loaded from the same file that it was saved under previously.\n'\
        'That\'s all it takes to load the trained neural network! '\
        'Let\'s make some use of it and apply it to new data.'
        para6 = tk.Label(content, text = para6Text)
        para6.pack()

        # Figure 5: creating flow of samples
        self.fig5flow = tk.PhotoImage(
            file = Page.load_image(self, 'save_load/fig5flow.gif')
        )
        fig5 = tk.Label(content, image = self.fig5flow)
        fig5.pack()

        fig5caption = 'Figure 5: Create flow of images from the testing '\
        'dataset.'
        fig5cap = tk.Label(content, text = fig5caption, font = self.italic)
        fig5cap.pack()

        # Paragraph 7: Argument explanation for flow_from_directory
        para7Text = 'In the ships-in-satellite-imagery dataset, a new '\
        'directory has been created called "test_set" containing 20 randomly '\
        'selected images.\n'\
        'They are all from the validation set, with 10 classed as no_ship and '\
        '10 ship.\n'\
        'Again, the first step is to import ImageDataGenerator, so it is '\
        'available when running this script.\n'\
        'The only parameter passed to the generator is "rescale", ensuring '\
        'all pixel values are between 0 and 1.\n\n'\
        \
        'Then, the actual flow is defined by flow_from_directory, as before '\
        'when defining the training and validation.\n'\
        'Here, the only argument staying the same as in the training script '\
        'is the target_size.\n\n'\
        \
        'The directory being flowed from is now the test_set, which contains '\
        'one directory called "directory".\n'\
        'This is because we do not want the network to know the image '\
        'classes; we want to see what it predicts.\n'\
        'The reason "directory" exists within test_set is that Keras requires '\
        'a directory for the flow to work correctly.\n\n'\
        'The "batch_size" has been changed to 20, since there are 20 images '\
        'in the testing set.\n\n'\
        \
        'The "class_mode" has been set to None to tell the flow that there '\
        'are no labels specified and all the images will be contained '\
        'within "directory".\n\n'\
        'A new argument "shuffle" has been added and set to False. This '\
        'ensures the images are not taken randomly, but instead in '\
        'alphanumeric order.\n'\
        'Hence, we know that the no_ship images will be tested first as they '\
        'all start with 0, and the ship images tested last as they start with '\
        '1.\nThe image flow is now defined! Now for the predictions:'
        para7 = tk.Label(content, text = para7Text)
        para7.pack()

        # Figure 6: Make predictions
        self.fig6predictions = tk.PhotoImage(
            file = Page.load_image(self, 'save_load/fig6predictions.gif')
        )
        fig6 = tk.Label(content, image = self.fig6predictions)
        fig6.pack()

        fig6caption = 'Figure 6: Apply the neural network to predict the '\
        'class of the test_set images.'
        fig6cap = tk.Label(content, text = fig6caption, font = self.italic)
        fig6cap.pack()

        # Paragraph 8: Predictions explanation
        para8Text = 'Using the "predict_generator" method on the Sequential '\
        'network that was previously stored as "classifierReloaded", '\
        'the network can output its predictions for the test set.\n'\
        'The only other parameter needed is "steps", which tells the network '\
        'how many batches to run through.\n'\
        'This method returns an array of the predicted probabilities from 0 '\
        'to 1.\n\n'\
        \
        'In order to turn the probability into a class prediction, some '\
        'further code is needed.\n'\
        'First, a counter is defined to make it easier to see the probability '\
        'for each image in the test set.\n'\
        'Then, iterating over the array, each probability is defined a '\
        'class.\n\n'\
        \
        'The order of the classes is alphanumeric, so no_ship comes before '\
        'ship. Hence, a no_ship prediction will be nearer to 0 and a ship '\
        'prediction nearer to 1.\n'\
        'An alternate method to confirm this is to '\
        'print(str(training_set.class_indices)) when running your training '\
        'script.\n'\
        'An example of this is included in shipsSaved.py, in step 7 after '\
        'defining the training_set.\n\n'\
        \
        'The counter is increased each iteration and printed along with the '\
        'prediction result. The results are shown below:'
        para8 = tk.Label(content, text = para8Text)
        para8.pack()

        # Figure 7: Prediction Results
        self.fig7results = tk.PhotoImage(
            file = Page.load_image(self, 'save_load/fig7results.gif')
        )
        fig7 = tk.Label(content, image = self.fig7results)
        fig7.pack()

        fig7caption = 'Figure 7: Prediction results.'
        fig7cap = tk.Label(content, text = fig7caption, font = self.italic)
        fig7cap.pack()

        # Paragraph 9: Results analysis
        para9Text = 'As you can see, 20 images were found and processed.\n'\
        'The network did not correctly classify all of the images; 2 of the '\
        'first 10 images were classed as ship when they should have been '\
        'no_ship.\n'\
        'All 10 ship images were classified correctly. This means that in our '\
        'test the model was 90% accurate, which isn\'t a bad result.\n'\
        'However, during training the validation accuracy was over 95%! '\
        'Here are the 2 images that were classed incorrectly:'
        para9 = tk.Label(content, text = para9Text)
        para9.pack()

        # Figure 8: Errors
        self.fig8errors = tk.PhotoImage(
            file = Page.load_image(self, 'save_load/fig8errors.gif')
        )
        fig8 = tk.Label(content, image = self.fig8errors)
        fig8.pack()

        fig8caption = 'Figure 8: The 2 images that were incorrectly\n'\
        'classified as ship when they are in fact no_ship.'
        fig8cap = tk.Label(content, text = fig8caption, font = self.italic)
        fig8cap.pack()

        # Paragraph 10: Error analysis
        para10Text = 'You can see where the errors may have come from.\n'\
        'The image on the right looks like it is in fact part of a ship, but '\
        'a ship classification is defined as a whole ship.\n'\
        'The image on the left has a small boat with wake that looks similar '\
        'to the sharp outline of a ship against the water.\n\n'\
        \
        'With this in mind, your challenge now is to modify and improve the '\
        'CNN.\nSee if you can get 95% accuracy on the test set, or even 100%!'\
        '\n\nThen check out the Retinal OCT Example.'
        para10 = tk.Label(content, text = para10Text)
        para10.pack()






# Just to view the page as it is:
if __name__ == '__main__':
    root = tk.Tk()
    home = SaveLoad(root)
    root.mainloop()
