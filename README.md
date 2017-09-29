# My_Messenger_Bot
It's a bot for Facebook Messenger developed in Python (Django Framework). 
1. First things first - Facebook App & its page!
To build a Facebook messenger bot, we must first create a new Facebook app. To do this, lets head to the Facebook developer site, create a new app and fill out the relevant details to get our App ID. You can select "Apps for Messenger" as its category. This will prepopulate the required products for the app in the dashboard.

Next, our app must be associated with a Facebook page since it is the page that interacts with the users. If you don't already have a page, go ahead and create one. You can spice up your page with pictures and relevant details or you can leave it as is for now. The page doesn't have to be published for the bot to work.
To access the Facebook messaging API, our app will need a page access token. Go ahead and click on the "Messenger" tab on the control panel under "Products". Then, select the page that the app will link to and a token will be generated. This token will later be used by your app to send messages to users!

Next, our app must be associated with a Facebook page since it is the page that interacts with the users. If you don't already have a page, go ahead and create one. You can spice up your page with pictures and relevant details or you can leave it as is for now. The page doesn't have to be published for the bot to work.

To access the Facebook messaging API, our app will need a page access token. Go ahead and click on the "Messenger" tab on the control panel under "Products". Then, select the page that the app will link to and a token will be generated. This token will later be used by your app to send messages to users!

## Clone The Code
a. git clone https://github.com/1akshat/My_Messenger_Bot.git<br>
b. cd My_Messenger_Bot.git<br>
c. virtualenv <env_name><br>
d. source <env_name>/bin/activate<br>
e. pip install -r requirements.txt<br>
f. python manage.py runserver<br>

3. Webhook - time for your app and Facebook to hook up!
"A webhook is a way for an app to provide other applications with real-time information." In this case, Facebook provides our app with real-time information i.e. whenever someone sends our page a message.

The first part is to decide exactly "where" our app and Facebook should "hook up"! Lets create a URL and tell Facebook about it so it can send updates there. Later, we can write code to handle these incoming requests. Keep in mind that we want this URL to be secret, unless you want intruders to know where we hook up! 

Generate a long random sequence for our url. In a python interpreter, run this

import os, binascii<br>
print binascii.hexlify(os.urandom(25))<br>
Here is one such sequence, 66d2b8f4a09cd35cb23076a1da5d51529136a3373fd570b122. Lets define our webhook URL in urls.py file and create a view to handle it

# yomamabot/fb_yomamabot/urls.py<br>
from django.conf.urls import include, url<br>
from .views import YoMamaBotView<br>
urlpatterns = [<br>
                  url(r'^66d2b8f4a09cd35cb23076a1da5d51529136a3373fd570b122/?$', ChatBotView.as_view())<br> 
               ]
## Ngrok to the rescue! 

For development purposes, we will use Ngrok that sets up secure tunnels to our localhost i.e. Ngrok gives web accessible URLs and tunnels all traffic from that URL to our localhost! Easy, peasy!  Go to Ngrok's download page, download the zip file, unzip and simply run the command<>br

./ngrok http 8000<br>

Its that easy! Now any outside computer can reach your localhost server at https://36096fff.ngrok.io which means so can Facebook! So lets set up the webhook for Facebook. Go to your app dashboard and click on Messenger (where you created your page access token previously). Click on "Setup Webhooks" right below "Token Generation" and fill the details as shown.
