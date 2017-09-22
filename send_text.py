from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACd070fe2aa39d50920df70742524af38f"
# Your Auth Token from twilio.com/console
auth_token  = "87fb5003945dcd95b7590b92cb6"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+918148028123", 
    from_="+15155193685",
    body="Hello from Python!")

print(message.sid) 