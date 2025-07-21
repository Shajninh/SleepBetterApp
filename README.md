# Flask Birthstone Lab

1. Your Task
2. Bonus Challeges
3. Quick Setup for Replit
4. Running the App
5. Anatomy of the App

## Your Task
The goal of this lab is to create a web application that takes in a user's birth month, and outputs their birthstone. For example, someone born in December should be told that their birthstone is Turquoise or Topaz (depending on which chart you use).

![Birthstones Chart](../static/images/birthstones.png)

Some of the styling has been done for you, but the rest of the application needs to be created in `model.py`, `app.py`, `index.html`, and `results.html`.

Don't forget to preview and test your application as you work!

## Bonus Challenges

**1.** Style the results page so it matches the index.

**2.** Make the results page output a picture and a description of the gemstone in addition to the name of the birthstone.

**3.** Create an "About" page with similar styling and link it to the index.

**4.** Make your own web application (remember, it must take input and output manipulated data).


## Quick Setup for Replit

Fork this template and create your own copy - feel free to ask a peer or instructor if you have trouble with this, as it's a feature that changes somewhat frequently. 

## Running the App

If you're using Replit, just press the "RUN" button. Use the "open in new tab" button to get a full-sized preview. 


## Anatomy of the app

Here's everything inside our Flask template. A first-time learner should really only start by looking at the **app.py**, the **model.py**, the **templates** folder, and the **static** folder. Almost everything else operates more behind the scenes, and can be a later focus. 

<pre>
flaskproject
├── app.py - This is the main file for our app.
├── model.py - This is where we will write the logic of our app.
├── readme.md - That's this file!
├── static - This is where we house assets like images and stylesheets.
│   ├── css - Put stylesheets here.
│   │   └── style.css
│   └── images - Put images here.
│       └── micropig.jpg
└── templates - Put templates (views) in this folder.
    └── index.html - This will be the first template we render.
</pre>
