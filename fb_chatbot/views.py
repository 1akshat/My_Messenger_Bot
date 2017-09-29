import re
import requests
import json
import random
from django.views import generic
from django.http.response import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


jokes = {
		 'hi':		["Hey! Your Private Bot welcomes you. How may i help you?"],
		 'hey':		["Hey! Your Private Bot welcomes you. How may i help you?"],
		 'hello':	["Hey! Your Private Bot welcomes you. How may i help you?"],
		 'wassup':  ["Nothing Much ! Just hanging with other bots on facebook."],
		 'joke': ["What kind of a joke? Send 'stupid', 'fat', 'dumb' for a joke..!"],
         'stupid':  ["""Yo' Mama is so stupid, she needs a recipe to make ice cubes.""",
                    """Yo' Mama is so stupid, she thinks DNA is the National Dyslexics Association."""],
         'fat':     ["""You ever accidentally go up to a real big fat person, and you accidentally ask them for a good place to eat? And they look at you and say they don't know. And you're looking at them, like, 'You do know. I bet if I follow you for an hour, we gonna be eatin'.""",
                    """ Yo' Mama is so fat, when the cops see her on a street corner, they yell, "Hey you guys, break it up!" """],
         'dumb':    ["""Yo' Mama is so dumb, when God was giving out brains, she thought they were milkshakes and asked for extra thick.""",
                    """They always ask you dumb questions. 'Do you wanna be fat?' 'Oh yes, yes, I do. I wanna sweat for no reason.' Every time I breathe, they like, 'Why you breathing so hard?' 'So I can live.'"""], 
         'bye':     ["Before Saying Bye, Send me your email so that i can contact you some day..!"],
         'myemail': 	["Thanks! I will contact you soon. Have a nice day ahead."]
         }



def post_facebook_message(fbid, received_message):           
    # Remove all punctuations, lower case the text and split it based on space
    tokens = re.sub(r"[^a-zA-Z0-9\s]",' ',received_message).lower().split()
    joke_text = ''
    for token in tokens:
        if token in jokes:
            joke_text = random.choice(jokes[token])
            break
    if not joke_text:
        joke_text = "I didn't understand! Send 'stupid', 'fat', 'dumb' for a funny joke!"

	user_details_url = "https://graph.facebook.com/v2.6/%s"%fbid
	user_details_params = {'fields':'first_name, last_name, profile_pic', 'access_token':'<ACCESS_TOKEN>'}
	user_details = requests.get(user_details_url, user_details_params).json()
	joke_text = 'Hey ' + user_details['first_name'] + '..! ' + joke_text   


    post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=<ACCESS_TOKEN>' 
    response_msg = json.dumps({"recipient":{"id":fbid}, "message":{"text":joke_text}})
    status = requests.post(post_message_url, headers={"Content-Type": "application/json"},data=response_msg)
    print(status.json())


class ChatBotView(generic.View):
	def get(self, request, *args, **kwargs):
		if self.request.GET[hub.verify_token] == '123456':
			return HttpResponse(self.request.GET['hub.challenge'])
		else:
			return HttpResponse('Error, invalid token')


	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
   		return generic.View.dispatch(self, request, *args, **kwargs)


	def post(self, request, *args, **kwargs):
		incoming_message = json.loads(self.request.body.decode('utf-8'))
		# Facebook recommends going through every entry since they might send
        # multiple messages in a single call during high load
		for entry in incoming_message['entry']:
			for message in entry['messaging']:
				if 'message' in message:
					print(message)
					post_facebook_message(message['sender']['id'], message['message']['text'])
		return HttpResponse()
