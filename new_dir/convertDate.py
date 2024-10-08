dates = [
    "01/01/2020",
    "15/05/2021",
    "23/11/2022",
    "07/04/2019",
    "30/12/2023"
]

dates_converties = []


for date in dates : 
    jour , mois , annee =  date.split('/')
    dates_convertie  = '-'.join([jour,mois,annee])
    dates_converties.append(dates_convertie)

print(dates_converties)    