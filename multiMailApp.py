import smtplib
server=smtplib.SMTP('smtp.gmail.com', 587) #Not only gmail base. You can write yourself.
server.starttls()
server.login('info@peraport.net', 'python789') #This is not the real pass :D

var=1
x=0

myvar={'ahmetmyfriend@gmail.com', 'sabanciunv@gmail.com', 'iuunviversity@gmail.com',
'newogr@ogr.iu.edu.tr', 'kocunv@gmail.com', 'steveblank@harvard.edu', 'zuck@harvard.edu', 
'gilbert_strang@mit.edu', 'michaeldell@dell.com', 'jeffbezos@penn.edu'}

while (var<=10) :
    
    server.sendmail('info@peraport.net', 'myvar[x]', 'Peraport Bilişim' )
    myvar=myvar[x+1]
    var=var+1

print("This is ok!!!")
