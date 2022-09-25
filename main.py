import uuid
import base64

x_correlation_id = uuid.uuid4()
print(x_correlation_id)

log_pass = "login:password"
auth_encoded = (base64.b64encode(log_pass.encode('UTF-8'))).decode('UTF-8')
print(auth_encoded)
