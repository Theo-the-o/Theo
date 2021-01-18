import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from tkmacosx import Button, SFrame
from tkinter import *
from PIL import Image, ImageTk


root = tk.Tk() # root is the name of the GUI object
root.title("Cooking Recipes")
root.minsize(500, 500) # height and width in pixels
root.geometry("1200x1000")

style = ttk.Style()
style.configure('TNotebook', tabposition='nw') #'nw' as in compass direction
# style.configure('lefttab.TNotebook', tabposition='ws')


# Drop down menu variables for homepage
OPTIONS = [
"Drinks/Dairy",
"Grains",
"Fruits",
"Vegtables & Legumes",
"Protein"] 


#tab size
planner = ttk.Notebook(root, width=1500, height=750)


######################################## Start Frame 1 ###################################


# Which tab the code is on (in this case the first tab), and details about the tab
tab1 = tk.Frame(planner, bg='lightblue', width=1400, height=750, pady=5)


#Fonts and sizes for different parts of the website, like title, header, paragraph, etc
title_font = tkFont.Font(family = "Times", size = 25)
header_font = tkFont.Font(family = "Times", size = 20)
subheader_font = tkFont.Font(family = "Times", size = 17)


#labels/text
tab1label = tk.Label(tab1, font = header_font, text = "Hello! This is the Homepage where I will tell you about the website! \n Down below you will see a dropdown menu which will show you the different food categories the recipes will be organized under.")
tab1image1label = tk.Label(tab1, font=header_font, text="The recipes in this program are organised into 5 different food categories which is shown above in the drop down menu!\nIn each of the tabs there will be a few drop down menu's showing some recipe ideas which you can find yourself organised by food category!\nOne of the 5 recipe ideas per tab will have an image and a recipe attached below!")



tab1label2 = tk.Label(tab1, text = "Food Categories", font=title_font, bg='pink')



# dropdown menu to show options of different food categories
variable = tk.StringVar(tab1) # needed for the dropdown menu (ddm)
variable.set(OPTIONS[0]) # default value
tab1ddm = tk.OptionMenu(tab1, variable, *OPTIONS)





#printing and choosing image 
img = Image.open("cook.jpg")
img = img.resize((600, 315), Image.ANTIALIAS)
tkimage1 = ImageTk.PhotoImage(img)


#Canvas for image to go into, Canvas size
tab1canvas = tk.Canvas(tab1, width=400, height=315)
tab1canvas.create_image(175, 150, image=tkimage1)
tab1canvas.grid(row=4, column=1)



# Remember to also place everything on the grid (or lese they will not show up!)
tab1label.grid(row=0, column=1, sticky="n")
tab1ddm.grid(row=3, column=1)
tab1label2.grid(row=2, column=1)
tab1image1label.grid(row=6, column=1)


######################################## End of Frame 1 and Start of Frame 2 ###################################

# Create everything!

# Create the tab and place it in the planner
tab2 = tk.Frame(planner, bg='lightgreen', width=1400, height=850, pady=5)



# Create the label
tab2label1 = tk.Label(tab2, font = header_font, text="Hello! Down below you will see drop down menus where you can see some recipes ideas for the Breakfast category organised by food group!")

tab2label2 = tk.Label(tab2, text = "Recipe", font=title_font, bg='pink')



OPTIONSB1 = [
"Drinks/Dairy",
"Smoothie"]

OPTIONSB2 = [
"Grains",
"French Toast"
]

OPTIONSB3 = [
"Fruits",
"Fruits with yogurt"
]

OPTIONSB4 = [
"Vegtables & Legumes",
"Salad bowl"
]

OPTIONSB5 = [
"Protein",
"Oats"
]


# dropdown menu to show options of different food categories
variable = tk.StringVar(tab2) # needed for the dropdown menu (ddm)
variable.set(OPTIONS[0]) # default value
tab2ddm1 = tk.OptionMenu(tab2, variable, *OPTIONSB1)

variable = tk.StringVar(tab2) 
variable.set(OPTIONS[1]) 
tab2ddm2 = tk.OptionMenu(tab2, variable, *OPTIONSB2)

variable = tk.StringVar(tab2) 
variable.set(OPTIONS[2]) 
tab2ddm3 = tk.OptionMenu(tab2, variable, *OPTIONSB3)

variable = tk.StringVar(tab2) 
variable.set(OPTIONS[3]) 
tab2ddm4 = tk.OptionMenu(tab2, variable, *OPTIONSB4)

variable = tk.StringVar(tab2) 
variable.set(OPTIONS[4]) 
tab2ddm5 = tk.OptionMenu(tab2, variable, *OPTIONSB5)




tab2image1label = tk.Label(tab2, font=subheader_font, text="Recipe for French toast!\n\nIngredients - 4 eggs, 1 cup milk, 6-8 slices of bread, 2 teaspoons vanilla extract, and 1 tbs butter.\n\nInstructions - 1) Whisk milk, eggs and vanilla extract in a large bowl, 2) Place griddle or pan over medium heat and melt butter in pan, \n3) Dip bread slices in egg mixture for about about 5 seconds each. Make sure both sides are well coated, \n4) Now carefully place the bread in the pan and cook until golden brown on both sides. Approximately 2 minutes per side.")



#printing and choosing image 
img2 = Image.open("frencht.jpg")
img2 = img2.resize((200, 300), Image.ANTIALIAS)
tkimage2 = ImageTk.PhotoImage(img2)


#Canvas for image to go into, Canvas size
tab2canvas = tk.Canvas(tab2, width=200, height=300)
tab2canvas.create_image(103, 150, image=tkimage2)
tab2canvas.grid(row=7, column=0)



#grid placements
tab2label1.grid(row=0, column=0, sticky="N")
tab2label2.grid(row=6, column=0)
#tab2canvas.grid(row=7,column=0)
tab2image1label.grid(row=8, column=0, sticky='w')

tab2ddm1.grid(row=1, column=0, sticky='w')
tab2ddm2.grid(row=2, column=0, sticky='w')
tab2ddm3.grid(row=3, column=0, sticky='w')
tab2ddm4.grid(row=4, column=0, sticky='w')
tab2ddm5.grid(row=5, column=0, sticky='w')


######################################## End of Frame 2 and Start of Frame 3 ###################################



tab3 = tk.Frame(planner, bg='lightyellow', width=1400, height=850, pady=5)

label1 = tk.Label(tab3, font = header_font, text="Hello! Down below you will see drop down menus where you can see some recipes ideas for the Lunch category organised by food group!")
label1.grid(row=0, column=0)

tab3label2 = tk.Label(tab3, text = "Recipe", font=title_font, bg='pink')
tab3label2.grid(row=6, column=0)


OPTIONSB1 = [
"Drinks/Dairy",
"Smoothie"]

OPTIONSB2 = [
"Grains",
"Grilled Cheese"
]

OPTIONSB3 = [
"Fruits",
"Fruit bowl"
]

OPTIONSB4 = [
"Vegtables & Legumes",
"Grilled Vegtables"
]

OPTIONSB5 = [
"Protein",
"Oats"
]


# dropdown menu to show options of different food categories
variable = tk.StringVar(tab3) # needed for the dropdown menu (ddm)
variable.set(OPTIONS[0]) # default value
tab3ddm1 = tk.OptionMenu(tab3, variable, *OPTIONSB1)

variable = tk.StringVar(tab3) 
variable.set(OPTIONS[1]) 
tab3ddm2 = tk.OptionMenu(tab3, variable, *OPTIONSB2)

variable = tk.StringVar(tab3) 
variable.set(OPTIONS[2]) 
tab3ddm3 = tk.OptionMenu(tab3, variable, *OPTIONSB3)

variable = tk.StringVar(tab3) 
variable.set(OPTIONS[3]) 
tab3ddm4 = tk.OptionMenu(tab3, variable, *OPTIONSB4)

variable = tk.StringVar(tab3) 
variable.set(OPTIONS[4]) 
tab3ddm5 = tk.OptionMenu(tab3, variable, *OPTIONSB5)




tab3image1label = tk.Label(tab3, font=subheader_font, text="Recipe for Peach Raspberry smoothie!\n\nIngredients - 6 oz plain fat free yogurt, 1 peach, 1/2 cup raspberries, 1/4 teaspoon vanilla extract.\n\nInstructions to get swirl effect - 1) Blend raspberries with 3 oz yogurt, a few drops vanilla extract, and 1-2 ice cubes then pour in the glass, \n 2) Blend peaches with 3 oz yogurt, and 1-2 ice cubes and pour on top in the glass. Blend 30-45 seconds.")
tab3image1label.grid(row=8, column=0)


#printing and choosing image 
img3 = Image.open("smoothie.jpg")
img3 = img3.resize((200, 300), Image.ANTIALIAS)
tkimage3 = ImageTk.PhotoImage(img3)


#Canvas for image to go into, Canvas size
tab3canvas = tk.Canvas(tab3, width=200, height=300)
tab3canvas.create_image(103, 150, image=tkimage3)
tab3canvas.grid(row=7, column=0)



#grid placements
tab3ddm1.grid(row=1, column=0, sticky='w')
tab3ddm2.grid(row=2, column=0, sticky='w')
tab3ddm3.grid(row=3, column=0, sticky='w')
tab3ddm4.grid(row=4, column=0, sticky='w')
tab3ddm5.grid(row=5, column=0, sticky='w')


######################################## End of Frame 3 and Start of Frame 4 ###################################



tab4 = tk.Frame(planner, bg='violet', width=1400, height=850, pady=5)

label1 = tk.Label(tab4, font = header_font, text="Hello! Down below you will see drop down menus where you can see some recipes ideas for the Dinner category organised by food group!")
label1.grid(row=0, column=0)
tab4label2 = tk.Label(tab4, text = "Recipe", font=title_font, bg='pink')
tab4label2.grid(row=6, column=0)



OPTIONSB1 = [
"Drinks/Dairy",
"Smoothie"]

OPTIONSB2 = [
"Grains",
"Bread with fondu cheese"
]

OPTIONSB3 = [
"Fruits",
"Strawberrie salad"
]

OPTIONSB4 = [
"Vegtables & Legumes",
"Tomato Caprese Salad"
]

OPTIONSB5 = [
"Protein",
"Chicken Parmesan"
]


# dropdown menu to show options of different food categories
variable = tk.StringVar(tab4) # needed for the dropdown menu (ddm)
variable.set(OPTIONS[0]) # default value
tab4ddm1 = tk.OptionMenu(tab4, variable, *OPTIONSB1)

variable = tk.StringVar(tab4) 
variable.set(OPTIONS[1]) 
tab4ddm2 = tk.OptionMenu(tab4, variable, *OPTIONSB2)

variable = tk.StringVar(tab4) 
variable.set(OPTIONS[2]) 
tab4ddm3 = tk.OptionMenu(tab4, variable, *OPTIONSB3)

variable = tk.StringVar(tab4) 
variable.set(OPTIONS[3]) 
tab4ddm4 = tk.OptionMenu(tab4, variable, *OPTIONSB4)

variable = tk.StringVar(tab4) 
variable.set(OPTIONS[4]) 
tab4ddm5 = tk.OptionMenu(tab4, variable, *OPTIONSB5)


tab4image1label = tk.Label(tab4, font=subheader_font, text="Recipe for Tomato Caprese Salad!\n\nIngredients - 1 and a 1/2 lbs Ripe tomatoes (3-4 medium) sliced 1/4” thick, 12-16 oz Fresh mozzarella sliced 1/4” thick, \n 1 bunch Fresh basil (1/3 cup basil leaves), 3 Tbsp Extra virgin olive oil for drizzling, 1/2 tsp Sea salt or to taste, \n 1/4 tsp Black pepper or to taste, 2 Tbsp Balsamic glaze or added to taste (optional).\n\nInstructions - 1) Start by layering slices of tomatoes on a serving platter. \nTuck slices of cheese between each tomato so both are visible then tuck whole basil leaves between the cheese and tomatoes. \nArrange the slices so you can see every layer. \n 2) Season generously with salt and pepper, \ndrizzle all over with extra virgin olive oil and drizzle with 2 Tbsp balsamic glaze or add it to taste.")
tab4image1label.grid(row=8, column=0, sticky='w')


#printing and choosing image 
img4 = Image.open("tcs.jpg")
img4 = img4.resize((200, 300), Image.ANTIALIAS)
tkimage4 = ImageTk.PhotoImage(img4)


#Canvas for image to go into, Canvas size
tab4canvas = tk.Canvas(tab4, width=200, height=300)
tab4canvas.create_image(103, 150, image=tkimage4)
tab4canvas.grid(row=7, column=0)


#grid placements
tab4ddm1.grid(row=1, column=0, sticky='w')
tab4ddm2.grid(row=2, column=0, sticky='w')
tab4ddm3.grid(row=3, column=0, sticky='w')
tab4ddm4.grid(row=4, column=0, sticky='w')
tab4ddm5.grid(row=5, column=0, sticky='w')


######################################## End of Frame 4 and Start of Frame 5 ###################################



tab5 = tk.Frame(planner, bg='orange', width=1400, height=850, pady=5)

label1 = tk.Label(tab5, font = header_font, text="Hello! Down below you will see drop down menus where you can see some recipes ideas for the Snacks category organised by food group!")
label1.grid(row=0, column=0)
tab5label2 = tk.Label(tab5, text = "Recipe", font=title_font, bg='pink')
tab5label2.grid(row=6, column=0)



OPTIONSB1 = [
"Drinks/Dairy",
"Chocolate milk"]

OPTIONSB2 = [
"Grains",
"Good thins crackers"
]

OPTIONSB3 = [
"Fruits",
"Berries bowl"
]

OPTIONSB4 = [
"Vegtables & Legumes",
"Carrots with ranch"
]

OPTIONSB5 = [
"Protein",
"Almond milk smoothie"
]


# dropdown menu to show options of different food categories
variable = tk.StringVar(tab5) # needed for the dropdown menu (ddm)
variable.set(OPTIONS[0]) # default value
tab5ddm1 = tk.OptionMenu(tab5, variable, *OPTIONSB1)

variable = tk.StringVar(tab5) 
variable.set(OPTIONS[1]) 
tab5ddm2 = tk.OptionMenu(tab5, variable, *OPTIONSB2)

variable = tk.StringVar(tab5) 
variable.set(OPTIONS[2]) 
tab5ddm3 = tk.OptionMenu(tab5, variable, *OPTIONSB3)

variable = tk.StringVar(tab5) 
variable.set(OPTIONS[3]) 
tab5ddm4 = tk.OptionMenu(tab5, variable, *OPTIONSB4)

variable = tk.StringVar(tab5) 
variable.set(OPTIONS[4]) 
tab5ddm5 = tk.OptionMenu(tab5, variable, *OPTIONSB5)


tab5image1label = tk.Label(tab5, font=subheader_font, text="Recipe for Almond Banana Smoothie!\n\n Ingredients - 1/2 cup almond milk, ½ teaspoon vanilla extract (optional), 1 tablespoon of honey (optional), \n1 banana (peeled), tablespoon peanut butter or almond butter, 1 cup ice cubes (optional)\n\nInstructions - 1) Place the ingredients in the container of your blender. \n2) Blend starting on low speed and increasing to high for 30-60 seconds or until the mixture is smooth and homogenous. \n Enjoy the almond banana smoothie immediately, topped with some fresh almonds!")
tab5image1label.grid(row=8, column=0, sticky='w')



#printing and choosing image 
img5 = Image.open("almondbs.jpg")
img5 = img5.resize((200, 300), Image.ANTIALIAS)
tkimage5 = ImageTk.PhotoImage(img5)


#Canvas for image to go into, Canvas size
tab5canvas = tk.Canvas(tab5, width=200, height=300)
tab5canvas.create_image(103, 150, image=tkimage5)
tab5canvas.grid(row=7, column=0)



#grid placements
tab5ddm1.grid(row=1, column=0, sticky='w')
tab5ddm2.grid(row=2, column=0, sticky='w')
tab5ddm3.grid(row=3, column=0, sticky='w')
tab5ddm4.grid(row=4, column=0, sticky='w')
tab5ddm5.grid(row=5, column=0, sticky='w')


######################################## End of Frame 5 and Start of Frame 6###################################



tab6 = tk.Frame(planner, bg='red', width=1500, height=850, pady=5)

label1 = tk.Label(tab6, font = header_font, text="Hello! Down below you will see drop down menus where you can see some recipes ideas for the Desserts category organised by food group!")
label1.grid(row=0, column=0)
tab6label2 = tk.Label(tab6, text = "Recipe", font=title_font, bg='pink')
tab6label2.grid(row=4, column=0)


#Different drop down menus for each food category
OPTIONSB1 = [
"Drinks/Dairy",
"Chocolate Moose"]

OPTIONSB2 = [
"Grains",
"Whole Grain Brownies"
]

OPTIONSB3 = [
"Fruits",
"Fruit Icecream"
]

OPTIONSB4 = [
"Vegtables & Legumes",
"Carrot Cake"
]

OPTIONSB5 = [
"Protein",
"Nuts"
]


# the actual dropdown menu to show options of different food categories
variable = tk.StringVar(tab6) # needed for the dropdown menu (ddm)
variable.set(OPTIONS[0]) # default value
tab6ddm1 = tk.OptionMenu(tab6, variable, *OPTIONSB1)#What category its under and which recipe responds to that category

variable = tk.StringVar(tab6) 
variable.set(OPTIONS[1]) 
tab6ddm2 = tk.OptionMenu(tab6, variable, *OPTIONSB2)

variable = tk.StringVar(tab6) 
variable.set(OPTIONS[2]) 
tab6ddm3 = tk.OptionMenu(tab6, variable, *OPTIONSB3)

variable = tk.StringVar(tab6) 
variable.set(OPTIONS[3]) 
tab6ddm4 = tk.OptionMenu(tab6, variable, *OPTIONSB4)

variable = tk.StringVar(tab6) 
variable.set(OPTIONS[4]) 
tab6ddm5 = tk.OptionMenu(tab6, variable, *OPTIONSB5)

#image label 
tab6image1label = tk.Label(tab6, font=subheader_font, text="Recipe for Carrot Cake! \n\n Ingredients - 2 c. Clover Valley All-Purpose Flour, 2 c. Clover Valley Granulated Sugar, 2 tsp. baking powder, \n1 tsp. cinnamon, ½ tsp. salt, ½ tsp. baking soda, 3 c. shredded carrots, 4 eggs, ¾ c. Clover Valley Vegetable Oil, 1 tsp. vanilla extract, \nCreame Cheese Frosting - ½ c. butter (1 stick) (room temperature), 8 oz. package cream cheese (room temperature), 2 tsp. vanilla extract, 4 c. Clover Valley Powdered Sugar. \n\n Instructions - 1) Preheat oven to 350 degrees. Lightly spray a 15x10x1 jelly roll sheet pan with non-stick baking spray. Set aside.\n 2) In a mixing bowl, whisk together the dry ingredients: flour, sugar, baking powder, cinnamon, salt and baking soda. Set aside.\n 3) With a hand or stand mixer, combine the oil, eggs, vanilla and shredded carrots.\n 4) With the mixer running, gradually add the dry ingredients to the wet ingredients. Stop the mixer occasionally to scrape down the sides of the bowl with a rubber scraper.\n 5) Pour the batter into the sheet pan, and smooth out evenly with a spatula. Bake the cake at 350 for 30-32 minutes or until a toothpick inserted comes out clean and crumb-free. \nRemove cake from oven and let cool to room temperature.\n 6) For the frosting: With a hand or stand mixer, cream together the butter and cream cheese until smooth. Add the vanilla and incorporate well. \nGradually begin adding the powdered sugar one cup at a time, stopping the mixer to scrape down the sides of the bowl.\n 7) Spread the frosting evenly over the top of the cooled sheet cake.")
tab6image1label.grid(row=6, column=0, sticky='w')


#printing and choosing image 
img6 = Image.open("carrotc.jpg")
img6 = img6.resize((200, 300), Image.ANTIALIAS)
tkimage6 = ImageTk.PhotoImage(img6)


#Canvas for image to go into, Canvas size
tab6canvas = tk.Canvas(tab6, width=200, height=300)
tab6canvas.create_image(103, 150, image=tkimage6)
tab6canvas.grid(row=5, column=0)



#grid placements for the drop down menu bars
tab6ddm1.grid(row=1, column=0, sticky='w')
tab6ddm2.grid(row=2, column=0, sticky='w')
tab6ddm3.grid(row=3, column=0, sticky='w')
tab6ddm4.grid(row=4, column=0, sticky='w')
tab6ddm5.grid(row=5, column=0, sticky='nw')

######################################## End of Frame 6 ###################################

#tabs in the top left which change to different pages
planner.add(tab1, text='Homepage')
planner.add(tab2, text='Breakfast')
planner.add(tab3, text='Lunch')
planner.add(tab4, text='Dinner')
planner.add(tab5, text='Snacks')
planner.add(tab6, text='Desserts')





planner.grid(row = 0, column = 0)


root.mainloop() 