# Overview
This program connects to the UKG Ready API and allows for the pushing or pulling of data from the API. I currently am using a few http GET requests as well as a few PUT and POST requests. Certain http requests cannot be used with some API calls. See the documentation of the API for more details. This overview is followed by a more in-depth look at what the program does and how to use it. I have also provided some ways to add to the program if you want to preform an API call of your own. 

**Quick Note:** The old_code.txt document contains some functions I am not using at the moment, so feel free to use them if you need them.

You can find the documentation for the API here: https://secure.saashr.com/ta/docs/rest/public/

# Setting up the Program

## Installing Python
If you already have python installed then move onto the next step. If you don't have python installed, then open up a command line window and type in "python". This will bring up a Microsoft store window where you can download and install Python. Once you have Python installed move onto the next step. You can double check that Python is installed by typing the following into a terminal window.

    python --help

## Cloning from Github

The first thing  you will need to do is clone the repository from github. To do this, I recommend using the gitbash terminal that you can download from here: https://git-scm.com/download/win. Choose your operating system and follow the instructions to download the app. Once it is installed, create an empty folder and name it, then right click file inside the folder and choose "gitbash here". Go to the git repositiory and click the **Code** button and copy the URL that it gives you. Go back to the terminal that you opened and type in: 

    git clone "right click and select paste to paste the URL you just copied here"

hit enter to run the code. Let the script run, it might take a few minutes. Now the code is populated into the empty folder. Go to the folder containing the main.py folder before continuing.

## The .env file
There is a .env file that I use which contains the API key, the username, the password, and the company short name. (you can find the company shortname in the url when you are signed into UKG Ready. It is a 7 digit number) You can put the values directly into the code if you want, but I don't reccomend it. The way I have it setup now, Github will ignore the .env file so none of the passwords or keys are posted. If you want to create your own .env file, then (on Windows) create a text file in the same folder as the python script. Rename it to key.env (or anything.env). Open up the file in a text editor and enter values in the following format:

    NAME_OF_KEY = KEY
    
**For example:** I replaced "NAME_OF_KEY" with PROJECT_API_KEY in my program. You can use whatever name you want, but the name has to be the same in the program as well, so don't forget to change the value in both places. I have included some code from the program below that shows where to change the values.

    API_KEY = os.environ.get('PROJECT_API_KEY')

In this line of code I am assigning the PROJECT_API_KEY value from the .env file to the name API_KEY, which I will use in the rest program.
## Installing Libraries
There are a few Python libraries that I am using in this program. The process below uses pip to install the packages. Pip is already a part of the newer version of python so you shouldn't need to install it. If you don't have pip then google how to install it before coming back to this part of the readme.

### Requests Library
Type the following text into a command line that is open in the main directory of the program (where the main.py file is).

    $ pip install requests

### Dotenv Library
Type the following text into a command line that is open in the main directory of the program.

    $ pip install python-dotenv

# Running the Program
Once you have completed the previous steps, you should be good to run the program. To run the program open a command line in the folder where the main.py file is and type in the following command:

    python main.py

If you are using python3 then type in:

    python3 main.py

