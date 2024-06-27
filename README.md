# SWE573-Rohat_Vural
A repository for the software development practice course
# Introduction
Twishper is a website where you can fetch, most recent tweets which includes the query, which you entered. Twishper shows you tweets with their sentiments, the most common 20 words in the fetched tweets and overall sentiment distribution of fetched tweets. If you register and login to the Twishper, Twhisper allows you to save the results. You can find your saved results in the search history section. Here, in the search history page, beside most common words and overall sentiments, you can see the change of sentiments of the tweets which you saved by time. For fetching tweets from Twitter, Tweepy, for sentiment analysis, NLTK modules has been used. A template for login&register pages has been used from  https://jsfiddle.net/user/ivanov11/fiddles/. All the works for this project has been made by me. All the useful materials and solutions that has been helpful during the development process will be presented in references section.

live demo of project: https://twhisper.herokuapp.com/

# System Manuel 
In order to run Twhisper in your local environment you need to satisfy the requirements and follow the steps below.
*Python 3.8
*Pipenv
If you have python 3.8 and pipenv installed in your system you should follow next steps.
On your terminal
* 1_Clone the repository from github with the code: 
git clone https://github.com/RohatV/SWE573-Rohat_Vural.git 
* 2_Change your current directory to the twhisper with following commands
cd SWE573-Rohat_vural
cd twisper
* 3_activate virtual environment with following command 
pipenv shell
* 4_ Install the requirements with following command
pip install -r requirements.txt
* 5_ Configurate the Twitter api authentication informations.
In the twisper/products/getTweets.py fill the consumer_key, consumer_secret,
access_token, access_token_secret fields with your twitter api information. You can get it if you have Developer account on Twitter.

* 6_ Configurate Database settings
In twisper/twisper/settings.py fill the information of database that you are using


In the twisper/products/saveTweets.py fill the information of database that you are using.

* 7_ Make migrations
Use following commands 
python manage.py makemigration
pyton manage.py migrate
* 8_ Run server
Use following commands 
python manage.py runserver
Enjoy Twhisper 😊
