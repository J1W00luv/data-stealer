# Python Data Stealer using Discord

## **Aim:**
To learn how data collection works in Linux when a script is executed. The goal is to automate data stealing using API of outside services (Discord) To create a script that hiddenly collects information about the machine and user, then sends it to a remote server.

## **Method:**
	1. Set Up Safe Environment & Create a server: Use Kali VM as a target & created a server to collect all gathered data.
	2. Script & Execute It: Run script in Linux terminal.
	3. Documentation: Make a report based on results of the program.

## **Results:**
I first created a server on Discord to receive all collected data. I then wrote a simple python script to run terminal commands. While it is executed nothing shows on the screen so the user does not suspect an attack. Then, I loaded the script onto the Kali machine and used the following command to run it.

![Terminal screenshot]

The results of the code were immediately sent to the discord server I created earlier.

![Discord screenshot]

## **Problems I had during execution:**

| Problem | Description | Solution |
| ------- | ----------- | -------- |
| Root Limits | Without using the sudo command the script wouldn’t run due to a ‘/etc/shadow’ command in commands dictionary | I changed the command to ‘/etc/hostname’ not requiring admin rights |
| Indentation Error | The code could not see the ‘data’ variable because of wrong indentation, causing the script to not recognize it. | Added a tabulation to follow python correct syntax. |


## **Evaluation:**
My script successfully collected data without the victim knowing and sent it to my server. It shows how easy it can be to gather data, by the use of social engineering, which attack heavily relies on. Discord servers using the HTTPS (trusted protocol) means that the firewall does not recognise the traffic malicious and does not stop it. This makes data exfiltration harder to detect. To prevent this type of attack a couple of mitigation strategies could be used, for example to acknowledge users (especially administrators) that they should not be running scripts unless it is absolutely necessary and it is trusted (or code source can be seen, like my python script). Or use Endpoint Detection & Response which is an advanced technology that allows traffic to be monitored and analysed for any suspicious behaviour, like, for example, a lot of commands being run and data sent out to the internet.
