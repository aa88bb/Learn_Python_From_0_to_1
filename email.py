import smtplib

_user = "2192789259@qq.com"
_pwd  = "hpohmdpxpiefebag"
_to   = "2192789259@qq.com"

msg = smtplib.MIMEText("this is just a Test")
msg["Subject"] = "haha"
msg["From"]    = _user
msg["To"]      = _to

try:
    s = smtplib.SMTP_SSL("smtp.qq.com", 465)
    s.login(_user, _pwd)
    s.sendmail(_user, _to, msg.as_string())
    s.quit()
    print ("Success!")
except:
    print ("Falied")


