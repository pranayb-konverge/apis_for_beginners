from twilio.rest import Client

client = Client("TWILIO_SID", "TWILIO_TOKEN")

for message in client.messages.list():
    print(message.body)

message = client.messages.create(
    to="+917030026662",
    from_="+16605383675",
    body="Sendig you this message from Python code",
)

print(f"Created a new message:{message.sid}")
