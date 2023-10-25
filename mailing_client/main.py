import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
server = smtplib.SMTP('smtp.world4you.com',25)
# server.ehlo() is an SMTP command used to initiate a greeting and capability exchange between email servers.
server.ehlo()

with open('password.txt', 'r') as f:
    password = f.read()
server.login('sainandan83@gmail.com', password)

msg = MIMEMultipart()
msg['From'] = 'NeuralNine'
msg['To'] = 'sainandan.mamidi19@gmail.com'
msg['Subject'] = 'Just a Test'
with open('message.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message,'plain'))
filename = '07_aggregate_graph_legend_left_right.png'
#we are using rb(read binary) because we are dealing with the image
attachment = open(filename,'rb')
#To process image data
p = MIMEBase('application','octet-stream')
#the payload is the actual data being transmitted over a network, excluding any headers, metadata, or control information.
# For example, in a network packet, the payload is the part of the packet that carries the actual user data.
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition',f'attachment; filename{filename}')
msg.attach(p)
#we are getting the string
text = msg.as_string()
# above string (text) can be send by the server
#server.sendmail('from address','to adress','string message')
server.sendmail('sainandan83@gmail.com','sainandan.mamidi19@gmail.com',text)
