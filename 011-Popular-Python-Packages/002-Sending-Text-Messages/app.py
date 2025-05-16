from twilio.rest import Client

account_sid = "MYACCOUNTSID"
auth_token = "MYACCOUNTTOKEN"

client = Client(account_sid, auth_token)

call = client.messages.create(
    to="...",
    from_="...",
    body="This is our first message"
)
