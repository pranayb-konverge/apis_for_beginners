from twilio.rest import Client

client = Client("AC1ab13a200bd2868847b088655309c747", "6035694070272c018b9c03a57e37b9c5")

for message in client.messages.list():
    print(message.body)

message = client.messages.create(
    to="+917030026662",
    from_="+16605383675",
    body="Sendig you this message from Python code",
)

print(f"Created a new message:{message.sid}")