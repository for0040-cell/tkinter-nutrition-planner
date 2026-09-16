from tkinter import *
import csv

# <editor-fold desc="Window generator">
##---------------------------------------------------------------------------##
#                           Window Generator                                 #
##---------------------------------------------------------------------------##

# This solution uses a single-window, multi-frame architecture:
# every page (login, dashboard, edit profile, meal plan, search) is
# built as its own Frame class, and all frames are created once and
# stacked on top of each other. Navigating between "pages" doesn't
# open new windows - it calls show_frame() to raise the requested
# frame to the top, hiding the others. Shared data (goal, calories,
# protein) is stored on the controller (self) so every frame can
# access the same values regardless of which frame is currently shown.

class solution(Tk):
    def __init__(self, *args, **kwargs): #args etc are overrides to allow us to run multiple arguments/operations

        Tk.__init__(self, *args, **kwargs)
        gui = Frame(self)

        #Window Settings
        gui.pack(side="top", fill="both", expand = True)
        gui.grid_rowconfigure(0, weight=1)
        gui.grid_columnconfigure(0, weight=1)
        self.title("MultiFrame") #Window Title


        ##---------------------------------------------------------------------------##
        #                                    MENU BAR                                 #
        ##---------------------------------------------------------------------------##
        menuBar = Menu(self)

        # Create a pulldown menu, and add it to the menu bar
        fileMenu = Menu(menuBar, tearoff=0)
        fileMenu.add_command(label="Open", command=lambda: None)
        fileMenu.add_command(label="Save", command=lambda: None)
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=lambda: None)
        menuBar.add_cascade(label="File", menu=fileMenu)

        # create more pulldown menus
        editMenu = Menu(menuBar, tearoff=0)
        editMenu.add_command(label="Cut", command=lambda: None)
        editMenu.add_command(label="Copy", command=lambda: None)
        editMenu.add_command(label="Paste", command=lambda: None)
        menuBar.add_cascade(label="Edit", menu = editMenu)

        # display the menu
        self.config(menu=menuBar)
        ##---------------------------------------------------------------------------##
        #                                   MENU BAR                                  #
        ##---------------------------------------------------------------------------##


        # Stores each page frame so the program can switch between pages
        self.frames = {}

        # User Profile Variables
        # Stores user information so it can be displayed across pages

        self.goal = StringVar(value="Not Set")
        self.calories = StringVar(value="Not Set")
        self.protein = StringVar(value="Not Set")

        for F in (loginPage, nutritionDashboard, PageTwo, PageThree, PageFour): #Add new class frames here.

            frame = F(gui, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew") #Setting Window/Frame Size

        self.show_frame(loginPage) #Starting frame (Class Name)

    def show_frame(self, cont): #Command for frame change

        frame = self.frames[cont]
        frame.tkraise()
# </editor-fold>

# <editor-fold desc="Login page">
##---------------------------------------------------------------------------##
#                                Page One
#                                Login Page                                  #
##---------------------------------------------------------------------------##

class loginPage(Frame):

            def __init__(self, parent, controller):
                Frame.__init__(self, parent)

                ##-------------------------------------------------------------------##
                #                           Page Title                               #
                ##-------------------------------------------------------------------##

                # Label
                loginTitle = Label(self, text="Nutrition Planner Login",
                                   font=("Arial", 18, "bold"))
                loginTitle.grid(row=0, column=0, columnspan=2, pady=20)

                # Label
                loginSubTitle = Label(self, text="Please login to continue")
                loginSubTitle.grid(row=1, column=0, columnspan=2, pady=5)

                ##-------------------------------------------------------------------##
                #                         Login Details                              #
                ##-------------------------------------------------------------------##

                # Username Label
                userLbl = Label(self, text="Username")
                userLbl.grid(row=2, column=0, padx=15, pady=10, sticky="e")

                # Username Entry
                usernameEntry = Entry(self, width=25)
                usernameEntry.grid(row=2, column=1, padx=15)

                # Password Label
                passwordLbl = Label(self, text="Password")
                passwordLbl.grid(row=3, column=0, padx=15, pady=10, sticky="e")

                # Password Entry
                passwordEntry = Entry(self, width=25, show="*")
                passwordEntry.grid(row=3, column=1, padx=15)

                ##-------------------------------------------------------------------##
                #                         Output Label                               #
                ##-------------------------------------------------------------------##

                # Displays an error if the password is incorrect
                errorLbl = Label(self, text="", fg="red")
                errorLbl.grid(row=4, column=0, columnspan=2)

                ##-------------------------------------------------------------------##
                #                         Button Commands                            #
                ##-------------------------------------------------------------------##

                # Checks whether the entered password is correct
                def loginFn():

                    password = passwordEntry.get()

                    if password == "sam":

                        # Clear previous error message
                        errorLbl.config(text="")

                        # Open the dashboard
                        controller.show_frame(nutritionDashboard)

                    else:

                        # Display an error message
                        errorLbl.config(text="Incorrect Password")

                    return ()

                ##-------------------------------------------------------------------##
                #                           Buttons                                  #
                ##-------------------------------------------------------------------##

                # Login Button
                loginBtn = Button(self,
                                  text="Login",
                                  width=18,
                                  command=loginFn)

                loginBtn.grid(row=5, column=0, columnspan=2, pady=15)
# </editor-fold>

# <editor-fold desc="Nutrition dashboard">
##---------------------------------------------------------------------------##
#                                   Page One                                  #
#                              Nutrition Dashboard                            #
##---------------------------------------------------------------------------##

class nutritionDashboard(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)


        ##-------------------------------------------------------------------##
        #                              Title                                 #
        ##-------------------------------------------------------------------##

        #Main Page Title
        pageTitle = Label(self,
                          text="Nutrition Planner",
                          font=("Arial", 18, "bold"))

        pageTitle.grid(row=0, column=0, columnspan=3, pady=20)


        #Welcome Message
        welcomeLbl = Label(self,
                           text="Welcome to your nutrition dashboard")

        welcomeLbl.grid(row=1, column=0, columnspan=3, pady=5)


        ##-------------------------------------------------------------------##
        #                         Nutrition Overview                         #
        ##-------------------------------------------------------------------##

        #Goal Label
        goalLbl = Label(self,
                        text="Current Goal:")

        goalLbl.grid(row=2, column=0, padx=20, pady=10, sticky="w")


        #Goal Output
        goalOutputLbl = Label(self,
                              textvariable=controller.goal,
                              relief="solid",
                              width=25)

        goalOutputLbl.grid(row=2, column=1, padx=10)



        #Protein Label
        proteinLbl = Label(self,
                           text="protein (g):")

        proteinLbl.grid(row=3, column=0, padx=20, pady=10, sticky="w")

        proteinOutputLbl = Label(self,
                                 textvariable=controller.protein,
                                 relief="solid",
                                 width=25)

        proteinOutputLbl.grid(row=3, column=1, padx=10)


        #Calories Label
        caloriesLbl = Label(self,
                           text="Calories (kcal):")

        caloriesLbl.grid(row=4, column=0, padx=20, pady=10, sticky="w")

        caloriesOutputLbl = Label(self,
                                  textvariable=controller.calories,
                                  relief="solid",
                                  width=25)
        caloriesOutputLbl.grid(row=4, column=1, padx=10)


        ##-------------------------------------------------------------------##
        #                              Buttons                               #
        ##-------------------------------------------------------------------##

        #Opens the meal plan page
        mealPlanBtn = Button(self,
                             text="Generate Meal Plan",
                             width=20,
                             command=lambda: controller.show_frame(PageThree))

        mealPlanBtn.grid(row=6, column=0, pady=20)



        #Opens the profile editing page
        profileBtn = Button(self,
                            text="Edit Profile",
                            width=20,
                            command=lambda: controller.show_frame(PageTwo))

        profileBtn.grid(row=7, column=0, pady=10)



        #search feature
        nutritionBtn = Button(self,
                              text="Search Foods",
                              width=20,
                              command=lambda: controller.show_frame(PageFour))

        nutritionBtn.grid(row=6, column=1, pady=10)


        #Logout Button
        logoutBtn = Button(self,
                           text="Logout",
                           width=20,
                           command=lambda: controller.show_frame(loginPage))

        logoutBtn.grid(row=7, column=1)
# </editor-fold>

# <editor-fold desc="Edit profile page">
##---------------------------------------------------------------------------##
#                                   Page Two                                  #
#                              Edit Profile Page                              #
##---------------------------------------------------------------------------##

class PageTwo(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)


        ##-------------------------------------------------------------------##
        #                              Title                                 #
        ##-------------------------------------------------------------------##

        #Page Title
        profileTitle = Label(self,
                             text="Edit Profile",
                             font=("Arial", 18, "bold"))

        profileTitle.grid(row=0, column=0, columnspan=2, pady=20)


        #Instructions
        instructionLbl = Label(self,
                               text="Enter your nutrition goals below")

        instructionLbl.grid(row=1, column=0, columnspan=2, pady=5)


        ##-------------------------------------------------------------------##
        #                         Profile Information                        #
        ##-------------------------------------------------------------------##

        #Goal Label
        goalLbl = Label(self,
                        text="Nutrition Goal")

        goalLbl.grid(row=2, column=0, padx=20, pady=10)



        # Dropdown variable for storing selected goal
        goalVar = StringVar()

        # Default value
        goalVar.set("Select Goal")

        # Available nutrition goals
        goalOptions = [
            "Lose Weight",
            "Gain Weight",
            "Gain Muscle",
            "Maintain Weight",
            "Improve Fitness",
            "Improve Healthy Eating"
        ]


        # Goal Dropdown Menu
        goalMenu = OptionMenu(self, goalVar, *goalOptions)

        goalMenu.config(width=20)

        goalMenu.grid(row=2, column=1)


        #Height Label
        heightLbl = Label(self,
                           text="Height (cm)")

        heightLbl.grid(row=3, column=0, padx=20, pady=10)


        #Height Entry
        heightEntry = Entry(self, width=25)

        heightEntry.grid(row=3, column=1)


        #Weight Label
        weightLbl = Label(self,
                           text="Current weight (kg)")
        weightLbl.grid(row=4, column=0, padx=20, pady=10)


        #Weight Entry
        weightEntry = Entry(self, width=25)
        weightEntry.grid(row=4, column=1)

        errorLbl = Label(self, text="", fg="red")
        errorLbl.grid(row=5, column=0, columnspan=2)


        ##-------------------------------------------------------------------##
        #                         Button Functions                           #
        ##-------------------------------------------------------------------##

        #Saves user information and updates nutritionDashboard
        def saveProfileFn():
            # Gets the user's details
            selectedGoal = goalVar.get()

            try:
                height = float(heightEntry.get())
                weight = float(weightEntry.get())
            except ValueError:
                errorLbl.config(text="Height and weight must be numbers and entered.")
                return

            if height < 50 or height > 275:
                errorLbl.config(text="Please enter a height between 50 and 275 cm.")
                return
            if weight < 1 or weight > 650:
                errorLbl.config(text="Please enter a weight between 1 and 650 kg.")
                return

            if selectedGoal == "Select Goal":
                errorLbl.config(text="Please select a goal.")

                return

            if selectedGoal == "Lose Weight":
                    dailyCalories = weight * 25
                    dailyProtein = weight * 1.6

            elif selectedGoal == "Gain Weight":
                    dailyCalories = weight * 35
                    dailyProtein = weight * 1.6

            elif selectedGoal == "Gain Muscle":
                    dailyCalories = weight * 30
                    dailyProtein = weight * 2.0

            elif selectedGoal == "Maintain Weight":
                    dailyCalories = weight * 30
                    dailyProtein = weight * 1.6

            elif selectedGoal == "Improve Fitness":
                    dailyCalories = weight * 30
                    dailyProtein = weight * 1.6

            elif selectedGoal == "Improve Healthy Eating":
                    dailyCalories = weight * 30
                    dailyProtein = weight * 1.6

                    # Saves the information

            controller.goal.set(selectedGoal)

            controller.calories.set(str(round(dailyCalories)))

            controller.protein.set(str(round(dailyProtein)))


            #Returns user to dashboard
            controller.show_frame(nutritionDashboard)

            return ()


        ##-------------------------------------------------------------------##
        #                              Buttons                               #
        ##-------------------------------------------------------------------##

        #Save Profile Button
        saveProfileBtn = Button(self,
                                text="Save Profile",
                                width=20,
                                command=saveProfileFn)

        saveProfileBtn.grid(row=6, column=1, pady=15)


        #Back Button
        backBtn = Button(self,
                         text="Back",
                         width=20,
                         command=lambda: controller.show_frame(nutritionDashboard))

        backBtn.grid(row=6, column=0, pady=15)
# </editor-fold>

# <editor-fold desc="Generate meal plan">
##---------------------------------------------------------------------------##
#                                Page Three                                   #
#                          Generate Meal Plan                                 #
##---------------------------------------------------------------------------##

class PageThree(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        ##-------------------------------------------------------------------##
        #                              Title                                 #
        ##-------------------------------------------------------------------##

        # Page Title
        mealplanTitle = Label(
            self,
            text="Generate Meal Plan",
            font=("Arial", 18, "bold")
        )

        mealplanTitle.grid(
            row=0,
            column=0,
            columnspan=3,
            pady=20
        )

        # Page Subtitle
        mealplanSubtitle = Label(
            self,
            text="Meals that align with your goals",
            font=("Arial", 14)
        )

        mealplanSubtitle.grid(
            row=1,
            column=0,
            columnspan=3,
            pady=5
        )

        # Page Subtitle
        searchReminder = Label(
            self,
            text="Search Meals given to find recipe",
            font=("Arial", 12)
        )

        searchReminder.grid(
            row=2,
            column=0,
            columnspan=3,
            pady=5
        )

        ##-------------------------------------------------------------------##
        #                              Current Goal                          #
        ##-------------------------------------------------------------------##

        # Goal Label
        goalLbl = Label(
            self,
            text="Your Goal:"
        )

        goalLbl.grid(
            row=3,
            column=0,
            padx=10,
            pady=10
        )

        # Shows the goal selected on PageTwo
        goalOutputLbl = Label(
            self,
            textvariable=controller.goal,
            relief="solid",
            width=25
        )

        goalOutputLbl.grid(
            row=3,
            column=1,
            padx=10,
            pady=10
        )

        ##-------------------------------------------------------------------##
        #                              Meal Frame                            #
        ##-------------------------------------------------------------------##

        mealFrame = Frame(self)

        mealFrame.grid(
            row=6,
            column=0,
            columnspan=3,
            padx=20,
            pady=10
        )

        ##-------------------------------------------------------------------##
        #                         Generate Meal Function                     #
        ##-------------------------------------------------------------------##

        def generateMealPlanFn():

            for widget in mealFrame.winfo_children():
                widget.destroy()

            # Gets the user's selected goal
            selectedGoal = controller.goal.get()

            # Checks if the user has selected a goal
            if selectedGoal == "Not Set" or selectedGoal == "Select Goal":
                errorLbl = Label(
                    mealFrame,
                    text="Please select a goal first."
                )

                errorLbl.grid(
                    row=0,
                    column=0,
                    columnspan=3,
                    pady=10
                )

                return

            ##-------------------------------------------------------------------##
            #                              Read CSV File                          #
            ##-------------------------------------------------------------------##

            # meals.csv structure:
            # Each row represents one meal, with the following columns:
            # - MealName: the name of the meal (string)
            # - Goal: which nutrition goal this meal supports (must match one of the six goal options)
            # - Protein (g): protein content in grams (string, converted for display)
            # - kcal: calorie content (string, converted for display)
            # - Ingredients: list of ingredients used in the recipe
            # - Method: the recipe/preparation instructions shown when "Recipe" is clicked

            # Open csv file
            mealFile = open("meals.csv")

            # Read csv file
            mealDictReader = csv.DictReader(mealFile)

            rowNumber = 0

            # Go through each meal in the CSV file
            for row in mealDictReader:

                # Check if the meal matches the user's goal
                if row["Goal"] == selectedGoal:
                    # Meal Name
                    mealNameLbl = Label(
                        mealFrame,
                        text=row["MealName"],
                        font=("Arial", 11, "bold")
                    )

                    mealNameLbl.grid(
                        row=rowNumber,
                        column=0,
                        padx=10,
                        pady=5,
                        sticky="w"
                    )

                    # Protein
                    proteinLbl = Label(
                        mealFrame,
                        text=row["Protein (g)"] + " g protein"
                    )

                    proteinLbl.grid(
                        row=rowNumber,
                        column=1,
                        padx=10,
                        pady=5
                    )

                    # Calories
                    caloriesLbl = Label(
                        mealFrame,
                        text=row["kcal"] + " kcal"
                    )

                    caloriesLbl.grid(
                        row=rowNumber,
                        column=2,
                        padx=10,
                        pady=5
                    )

                    rowNumber += 1

            mealFile.close()

            if rowNumber == 0:
                noMealsLbl = Label(mealFrame, text="No meals found for this goal.")
                noMealsLbl.grid(row=0, column=0, columnspan=3, pady=10)

        ##-------------------------------------------------------------------##
        #                              Button                                #
        ##-------------------------------------------------------------------##

        generateBtn = Button(
            self,
            text="Generate Meal Plan",
            width=20,
            command=generateMealPlanFn
        )

        generateBtn.grid(
            row=5,
            column=0,
            columnspan=3,
            pady=15
        )

        #Back Button
        backBtn = Button(self,
                         text="Back",
                         width=20,
                         command=lambda: controller.show_frame(nutritionDashboard))

        backBtn.grid(row=7, column=0, pady=15)
# </editor-fold>

# <editor-fold desc="Search foods page">
##---------------------------------------------------------------------------##
#                                Page Three                                   #
#                               Search foods                                  #
##---------------------------------------------------------------------------##
class PageFour(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        #Page Title

        pageTitle = Label(self,

                          text="Search Foods",

                          font=("Arial", 18, "bold"))

        pageTitle.grid(row=0, column=0, columnspan=2, pady=20)

        #Instructions

        instructionLbl = Label(self,

                               text="Enter a food to search for")

        instructionLbl.grid(row=1, column=0, columnspan=2, pady=5)

        #Search Box

        searchEntry = Entry(self, width=30)

        searchEntry.grid(row=2, column=0, padx=10, pady=10)

        #Result

        resultLbl = Label(self, text="")

        resultLbl.grid(row=3, column=0, columnspan=2, pady=10)

        # Scrollable results
        # Mousewheel scroll binding adapted from JackTheEngineer's Tkinter ScrolledFrame github page
        # https://gist.github.com/JackTheEngineer/81df334f3dcff09fd19e4169dd560c59

        resultCanvas = Canvas(self, width=450, height=400)

        resultCanvas.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        scrollbar = Scrollbar(self, orient="vertical", command=resultCanvas.yview)

        scrollbar.grid(row=4, column=2, sticky="ns")

        resultCanvas.configure(yscrollcommand=scrollbar.set)

        resultFrame = Frame(resultCanvas)

        resultCanvas.create_window((0, 0), window=resultFrame, anchor="nw")

        def updateScrollRegion(event):
            resultCanvas.configure(scrollregion=resultCanvas.bbox("all"))

        resultFrame.bind("<Configure>", updateScrollRegion)

        def _on_mousewheel(event):
            resultCanvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

        def _bind_to_mousewheel(event):
            resultCanvas.bind_all("<MouseWheel>", _on_mousewheel)

        def _unbind_from_mousewheel(event):
            resultCanvas.unbind_all("<MouseWheel>")

        resultCanvas.bind("<Enter>", _bind_to_mousewheel)

        resultCanvas.bind("<Leave>", _unbind_from_mousewheel)
        #end of adapted code

        #Search Function
        def searchFoodFn():

            #Gets all widgets inside resultFrame and removes them
            #to clear the previous search results before displaying new results
            for widget in resultFrame.winfo_children():
                widget.destroy()

            searchFood = searchEntry.get().lower()

            if searchFood == "":
                errorLbl = Label(resultFrame, text="Please enter a search term")
                errorLbl.grid(row=0, column=0, columnspan=2, pady=10)
                return

            mealFile = open("meals.csv")

            # Reads each row of the CSV file as a dictionary
            mealDictReader = csv.DictReader(mealFile)

            found = False

            rowNumber = 0

            for row in mealDictReader:
                if searchFood in row["MealName"].lower():
                    found = True
                    # Displays the matching meal's name, protein and calories
                    resultLbl = Label(resultFrame, text=row["MealName"] + "\n"+ row["Protein (g)"] + "g protein\n" + row["kcal"] + " kcal\n",
                                    relief="solid", width=35, pady=10)
                    resultLbl.grid(
                        row=rowNumber,
                        column=0,
                        columnspan=2,
                        pady=5
                    )

                    # Recipe label

                    recipeLbl = Label(

                        resultFrame,

                        text="",
                        wraplength=400,
                        justify="left"
                    )

                    recipeLbl.grid(
                        row=rowNumber + 2,
                        column=0,
                        columnspan=2,
                        pady=5
                    )



                    # Recipe Button
                    def showRecipe(method=row["Method"], label=recipeLbl):
                        label.config(text=method)

                    recipeBtn = Button(resultFrame,
                                       text="Recipe",
                                       width=15,
                                       command=showRecipe)

                    recipeBtn.grid(row=rowNumber + 1, column=0, columnspan=2, pady=10)


                    rowNumber += 3



            mealFile.close()

            if found == False:
                errorLbl = Label(resultFrame, text="Meal not found")

                errorLbl.grid(
                    row=0,
                    column=0,
                    columnspan=2,
                    pady=10
                )

         #Search Button

        searchBtn = Button(self,
                            text="Search",
                            width=15,
                            command=searchFoodFn)
        searchBtn.grid(row=2, column=1, padx=10)

        #Back Button
        backBtn = Button(self,
                         text="Back",
                         width=20,
                         command=lambda: controller.show_frame(nutritionDashboard))

        backBtn.grid(row=3, column=0,columnspan=2 , pady=15)
# </editor-fold>


app = solution()
app.mainloop()
