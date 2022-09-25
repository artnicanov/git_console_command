from flask import Flask
import uuid
import base64
import time

app = Flask(__name__)

@app.route("/")
def cor_id_and_auth():

	x_correlation_id = uuid.uuid4()
	current_UNIX_time = round(time.time() * 1000)


	log_pass = "login:password"
	auth_encoded = (base64.b64encode(log_pass.encode('UTF-8'))).decode('UTF-8')

	return f"""{x_correlation_id}<br>
	       <br>{auth_encoded}<br>
			<br>{current_UNIX_time}"""

app.run(port=5002)
