#print ("Love you")
from twilio.rest import Client 
 
account_sid = 'ACf265e12051fffd53e2886409262568cf' 
auth_token = '3a654a6e3c8f392660e54dba98742344' 
client = Client(account_sid, auth_token) 
def send_love(): 
	message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Namaste! Have a good day ...',      
                              to='whatsapp:+917835999528' 
                          ) 
 
	print(message.sid)
