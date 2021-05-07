import yagmail
yag = yagmail.SMTP('vaccineslottracker', '')

pincode = 110090

to = 'pausethismoment@gmail.com'
subject = 'Sample Vaccine Tracker Email'
body = 'Please fine availablity for PINCODE {0} below:'.format(pincode)
html = ""

yag.send(to, subject, [body, html])