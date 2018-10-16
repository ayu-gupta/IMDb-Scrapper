#libraries to import

import mysql.connector
from bs4 import BeautifulSoup
import requests
import subprocess as sp
import imdb
from imdb import IMDb,IMDbError
from datetime import date
import datetime
import secret


def database():
    

    mycursor.execute("Create database if not exists imdbayushi")
    mycursor.execute("Use imdbayushi")

    mycursor.execute("Create table if not exists input_data(email varchar(100), tv_series varchar(500))")


#-------------------function for web scrapper ------------------------------------------------------    

def scrapper(series_list):
    for x in series_list:
        try:
            mov=tv.search_movie(x)[0]
            series_id=tv.get_imdbID(mov)                   #get imdb id of a particular series
        except IMDbError as e:
            print(e)
        page = requests.get("https://www.imdb.com/title/tt{}".format(series_id)) #request url of series in imdb
        soup = BeautifulSoup(page.content,'html.parser')
        
        #extract the last season of a series
        name_box=soup.findAll('div',attrs={'class':'seasons-and-year-nav'})
        value=[]
        for i in name_box:
            value=i.text.strip()
        value=value.split("\xa0\xa0\n")
        temp=value[0].split("\n")
        last_season=temp[len(temp)-1]

        new_page = requests.get("https://www.imdb.com/title/tt{0}/episodes?season={1}&ref_=tt_eps_sn_{1}".format(series_id,last_season))
        soup = BeautifulSoup(new_page.content,'html.parser')
        name_box=soup.findAll('div',attrs={'class':'airdate'})

        #extract airdates of last season  episodes
        airdates=[]
        for i in name_box:
            airdates.append(i.text.strip())

        
        empty_removed_airdates=airdates
        original_length=len(airdates)

        #remove those entries whoose info is not available 
        while '' in empty_removed_airdates:
            empty_removed_airdates.remove('')
        removed_length=len(empty_removed_airdates)



        month={"Jan.":1,"Feb.":2,"Mar.":3,"Apr.":4,"May":5,"Jun.":6,"Jul.":7,"Aug.":8,"Sep.":9,"Oct.":10,"Nov.":11,"Dec.":12}
        today=str(date.today())      #stores today's date  
        today=today.split("-")


        #logic for dividing into usecases
        if len(airdates[0].split()) == 1:                     #if only year is mentioned in airdate of fisrt episode 
            Status="The next season begins in {}".format(airdates[0])
        else:
            flag=0
            for i in empty_removed_airdates:
                r_date=i.split(" ")
                r_date[1]=month.get(r_date[1])   #map values of months 
                
                # check if today's date is less than any of the released date
                if datetime.date(int(r_date[2]),int(r_date[1]),int(r_date[0])) > datetime.date(int(today[0]),int(today[1]),int(today[2])):
                    flag=1
                    break
                    
            if flag==0:
                if removed_length<original_length:
                    Status="Latest episode was released on {}-{}-{}".format(r_date[2],r_date[1],r_date[0]) #no information about the next episode is mentioned
                else:
                    Status="The show has finished streaming all its episodes"      
            else:
                Status="Next episode airs on {}-{}-{}".format(r_date[2],r_date[1],r_date[0])


        fh.write("""
        Tv series name:{}
        Status:{}\n""".format(x,Status))


    sender_emailid=secret.email()
    sender_pwd=secret.pwd()

    fh.write("""
receiver_id: {}
sender_id: {}
sender_pwd: {}""".format(receiver_emailid,sender_emailid,sender_pwd))
        
    fh.close()



#----------function for mailing the status through ansible plablooks--------------------

def mail():
    fh=open("/mail.yml","w")
    fh.write("""
    - hosts: localhost
      tasks:
       - include_vars: "/mail_variables.yml"
       - mail:
           body: "{{body}}"
           from: "{{sender_id}}"
           username: "{{sender_id}}"
           password: "{{sender_pwd}}"
           subject: "Status of your Favourite Tv-Series"
           to: '{{receiver_id}}'
           host: smtp.gmail.com
           port: 587
    """)
    fh.close()

    sp.getoutput("sudo ansible-playbook /mail.yml")


#--------------------------main------------------------------------------------------------    
    
try:
    conn=mysql.connector.connect(user='root',password=secret.mysqlpwd(),host='localhost')
except:
    print("Error in connection to mysql")
mycursor=conn.cursor()

database()
tv=IMDb()

while True:
    receiver_emailid=input("Email address: ")
    Tv_series=input("Tv Series:")

    params=(receiver_emailid,Tv_series.lower())
    

    mycursor.execute("Insert into input_data(email,tv_series) values (%s,%s)",params)
    mycursor.execute("select * from input_data")
    data=mycursor.fetchall()
    a=data[len(data)-1]                          # fetch the last input value from table
    series_list=a[1].split(',')                  #split the series entered by user by ',' and check status of each series
    
    fh=open('/mail_variables.yml','w')           # write a yml file for body of mail
    fh.write("body: |")
    
    scrapper(series_list)
    mail()
