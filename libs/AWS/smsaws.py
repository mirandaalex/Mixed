import boto3

def AWS(tipe):
	# Create an SNS client
	client = boto3.client(
		"sns",
		aws_access_key_id="AKIA6MPYAZ7YIT5LZI7P",
		aws_secret_access_key="l2080PLjdX/5WFfWA37I4MuucEq2dTXPGhFTRjzS",
		region_name="us-east-1"
	)

	# Send your sms message.
	phoneTxt = open("phoneNumbers.txt", "r")
	text="Motvial Notifications: was found a "+tipe+" "
	for phoneN in phoneTxt:
		response = client.publish(
			PhoneNumber = phoneN,
			Message = text
		)

	print(response)