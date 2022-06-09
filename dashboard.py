import os
from quart import Quart, render_template, redirect, url_for
from quart_discord import DiscordOAuth2Session, requires_authorization, Unauthorized
from nextcord.ext import ipc
import nextcord
from config import *


app = Quart(__name__) #

app.secret_key = b'somethingspecial'
os.environ('OAUTHLIB_INSECURE_TRANSPORT') == 'true'

app.config['DISCORD_CLIENT_ID'] = SECRET
app.config['DISCORD_CLIENT_SECRET'] = M0BplekuVMM6-aboQHA-lT9HQiUgUtAy
app.config['DISCORD_REDIRECT_URL'] = 'https://72.176.182.91:5000/callback'
app.config['DISCORD_BOT_TOKEN'] = TOKEN

discord = DiscordOAuth2Session(app)

@app.route("/Login/")
async def login():
	return await discord.create_session()

@app.route("/callback/")
async def callback():
	try:
		await discord.callback()
	except:
		return redirect(url_for("login" ))
	return redirect(url_for('dashboard'))

@app.route("/")
async def index():
	return await render_template('index.html')

@app.route("/dashboard")
async def dashboard():
	user = await discord.fetch_uer()
	return await render_template('dashboard.html', user=user)

if __name__ == "__main__":
	app.run(debug=True)

