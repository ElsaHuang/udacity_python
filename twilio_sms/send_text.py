 #!/usr/bin/python
# -*- coding: UTF-8 -*-

from twilio.rest import TwilioRestClient

account_sid = "ACe529e44db058730410a3f50902d940ac"
auth_token = "ed7364efb6a3597b7196e448a8d78a1c"
client = TwilioRestClient(account_sid, auth_token)

try:
message = client.sms.messages.create(
	body="昀姐你猜我在干嘛",
	to= "+8618682162675",  # Replace with your phone number 
	from_="+12036334274 ") # Replace with your Twilio number

except TwilioRestException as e:
	print(e)