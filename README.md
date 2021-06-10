# Rune-Server


<b> FTP server</b>
for home users.
Features:
- Upload and host any file on a home network
- Unlimited file sizes

<h4>SETUP:<h4>

set up is really simple

1. Navigate to the main repo folder "/Rune-Server" in a terminal
2. run command "pip install -e ."   To install dependencies from our requirements.txt
3. run command "cd noteserver"  Enter the source folder
4. run command "set FLASK_APP=server.py"  configure flask run-time entry point
5. run command "flask run --host=localhost" set this to your IP address instead for port forwarding
6. navigate to your ip and default flask port in the browser (ex. "172.16.21.2:5000")


Note: the front-end is basically non-existant. This is just a proof of concept.

![Image1](https://cdn.discordapp.com/attachments/533758714805616680/651606345455501332/unknown.png)
