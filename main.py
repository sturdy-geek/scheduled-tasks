from email.mime.text import MIMEText
import datetime as dt
import pandas as pd
import smtplib
import random
import os
##################### Extra Hard Starting Project ######################
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")
# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
# now=dt.datetime.now()
# month=now.month
# day=now.day
# year=now.year
# m_d_y=(day,month)
# df=pd.read_csv("birthdays.csv")
# for index,rows in df.iterrows():
#     birthday=(rows["day"],rows["month"])
#     if birthday==m_d_y:
#         with (open (f"letter_templates/letter_{random.randint(1,3)}.txt") as file):
#             content=file.read()
#             content.replace("[NAME]",rows["name"])
#             msg=MIMEText(content)
#             msg["Subject"]=f"Happy Birthday , {rows["name"]}"
#             msg["From"]="joshosasigb@gmail.com"
#             msg["To"]="jigunbor.2300988@stu.cu.edu.ng"
#         with smtplib.SMTP("smtp.gmail.com") as connection:
#                 connection.starttls()
#                 connection.login(user="joshosasigb@gmail.com",password=PASSWORD)
#                 connection.sendmail(from_addr="joshosasigb@gmail.com",to_addrs=rows["email"],msg=msg.as_string())
#                 connection.close()

today =  dt.datetime.now()
today_tuple=(today.month,today.day)
data=pd.read_csv("birthdays.csv")
birthday_dict={(data_row["month"],data_row["day"]) : data_row for(index,data_row) in data.iterrows()}
if today_tuple in birthday_dict:
    birthday_person=birthday_dict[today_tuple]
    file_path=f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents=letter_file.read()
        contents.replace("[NAME]",birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        msg = MIMEText(contents).as_string()
        msg["Subject"]=f"Happy Birthday , {birthday_person["name"]}"
        msg["From"]=MY_EMAIL
        msg["To"]=birthday_person["email"]
        connection.startltls()
        connection.login(MY_EMAIL,MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,to_addrs=birthday_person["email"],msg=msg)
        connection.close()


