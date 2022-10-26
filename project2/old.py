import datetime
while True:
    try:
        bday = input("Hello, please enter your Date of Birth(ex. August 22 2000): ")
        birthday = datetime.datetime.strptime(bday, '%B %d %Y')
        break
    except:
        print("Please put in the Format 'Month Day Year' without any initial space")

tday = datetime.datetime.today()
timedelta = (tday - birthday).total_seconds()
print("You have been alive for:",round(timedelta),"seconds")
