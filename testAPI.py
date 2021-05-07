"""
from datetime import date
today = date.today().strftime('%d-%m-%Y')
"""
from json2table import convert
import json

def loadJSON(FILE_NAME):
    res = {}
    with open(FILE_NAME, 'r') as f:
        res = json.load(f)
    return res

json_object = loadJSON("dummy.json")

html="<html><style>table,td,th"+"{"+"border:1px solid #ddd;text-align:left;"+"}"+"table"+"{"+"border-collapse:collapse;width:100%;"+"}"+"th,td"+"{"+"padding:15px;"+"}"+"</style><body>"

pin = "110092"
for centers in json_object:
    for center in json_object[centers]:
        currHtml = "<table>"
        currHtml+=("<tr><td><b>PIN</b></td><td>"+pin+"</td></tr>")
        currHtml+=("<tr><td><b>Center</b></td><td>"+str(center["center_id"])+"</td></tr>")
        currHtml+=("<tr><td><b>Name</b></td><td>"+center["name"]+"</td></tr>")
        currHtml+=("<tr><td><b>Address</b></td><td>"+center["address"]+"</td></tr>")
        currHtml+=("<tr><td><b>Fee Type</b></td><td>"+center["fee_type"]+"</td></tr>")
        if len(center["sessions"])>0:
            currHtml+="<tr><td><b>Sessions</b></td><td><table><tr><th>Date</th><th>AvailableCapacity</th><th>MinAge</th><th>VaccineName</th></tr>"
            for item in center["sessions"]:
                currHtml+="<tr><td>"+str(item["date"])+"</td><td>"+str(item["available_capacity"])+"</td><td>"+str(item["min_age_limit"])+"</td><td>"+item["vaccine"]+"</td></tr>"
            currHtml+="</tr></table></td>"
        else:
            currHtml+=("<tr><td>Is Vaccination Session Available?</td><td>NO</td></tr>")
        currHtml+="</tr></table><br>"
        html+=currHtml
    html+="</body></html>"
    # print(html)

import yagmail
yag = yagmail.SMTP('vaccineslottracker', 'mmdqlyhqyxbutzsy')

pincode = 110090

to = 'pausethismoment@gmail.com'
subject = 'Sample Vaccine Tracker Email'
body = 'Please fine availablity for PINCODE {0} below:'.format(pincode)
markup = html

yag.send(to, subject, [body, markup])