# Webull-Trading-Bot
Bot that scrapes Discord server for callouts and places appropriate option trade on Webull platform.

Instructions:
The only parts of the code you need to alter to make the program work for you is the token in discord.py and phone/password/trading PIN in trade.py.

Phone is obviously your phone number that is associated with your Webull account and Password is the password that you use for your Webull account and place your Webull PIN that you use to unlock trading inside of wb.get_trade_token('') so that the program can unlock your account and allow access to trade.

In order to get your token for discord.py to work, you need to open Discord in a BROWSER NOT THE APPLICATION. Then go to the server you want to be scraping messages from. Inspect the page (Control + Shift + c) and then type something in the textbox on discord on that server. If you select the "Network" tab at the top of inspect and then click on "typing" on the left side and scroll down the "Headers" tab to the right of "typing", you will see "authorization: " followed buy a string of random characters. That is your token, copy that and insert it into the provided space in discord.py

Now that you have entered your phone number, password, and token. You should be able to scrape discord and let the bot place orders for you as they are called out on discord. That is unless you haven't installed the webull and websocket-client python packages...
You can simply install those with pip if you have not already.

Running Instructions:
The verifcation process involves you answering a security question and providing the question ID. The answer to the question is based off of whatever you wrote for it when you created your Webull account. As for the question ID, just enter the ID that is printed out to the console that is provided with the question prompt.

This program is not financial advise, use at your own risk and understand that you are responsible for understanding the code and what it is doing as well as that it is designed to place orders based off of call outs from discord trading servers. You should treat this program as an educational tool and if you want to use it for real world application you should make your own necessary tweaks to it to make it perform how YOU want it to.

Again, I am not liable for any outcomes you get from using this code. Use your money at your own risk.
