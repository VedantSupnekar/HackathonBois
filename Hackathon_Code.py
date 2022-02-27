
import pandas as pd
import math

# user information
name = input("Enter your name : ")
age = input("Enter your age : ")
sex = input("Enter your sex (Male/Female): ")
number = input("Enter your contact number including your +1:")

# symptoms

score = 0

print("Do you have fever over 100 degrees Fahrenheit? 1 means yes, 0 means no ")
s = int(input("Enter answer : "))
score = s+5

print("Do you have cough? 1 means yes, 0 means no ")
s = int(input("Enter answer : "))
score = s+5

print("Do you have shortness of breath or difficulty in breathing? 1 means yes, 0 means no ")
s = int(input("Enter answer : "))
score += s

print("Do you have fatigue or chills? 1 means yes, 0 means no ")
s = int(input("Enter answer : "))
score += s

print("Do you have muscle aches or pain? 1 means yes, 0 means no ")
s = int(input("Enter answer : "))
score += s

print("Do you have Headache? 1 means yes, 0 means no ")
s = int(input("Enter answer : "))
score += s

print("Do you have a new loss of taste or smell? 1 means yes, 0 means no ")
s = int(input("Enter answer : "))
score += s

print("Do you have sore throat? 1 means yes, 0 means no ")
s = int(input("Enter answer : "))
score += s

print("were you in contact with infected person (1 mean yes, 0 mean no)")
contact = int(input("enter answer : "))

# condition and next steps based on score

#declaring database and pulling data from local csv file
centre_locations = pd.read_csv("total_database1.csv")
#print(centre_locations)



min_dist = []

for i in range(len(centre_locations.index)):
    x1 = centre_locations["latitudes"][i]
    y1 = centre_locations["longitudes"][i]
    minboi = math.sqrt((lat-x1)*(lat-x1) + (lng-y1)*(lng-y1))
    min_dist.append(minboi)

centre_locations['minimum distance'] = min_dist
#print(centre_locations)


centre_locations.sort_values(by=['minimum distance'], inplace=True)



if score > 7:
    print("It is urgent that you get professional help. You are being directed to hospitals and doctors near you.")
    admit_locations = centre_locations.loc[centre_locations['Doctor Consultation AND ADMIT'] == 'Y']
    admits_list = admit_locations.values.tolist()
elif 7>=score >=6 :
    print ("Must do a professional covid-19 test.You may be infected with covid-19. We will be accessing your devices information to help you find the nearest open covid testing center. ")
    testing_locations = centre_locations.loc[centre_locations['testing'] == 'Y']
    testing_list = testing_locations.values.tolist()
elif 5>=score>=4:
    print("You might be infected with covid-19. You need to do a take-at-home test.  We will be accessing your devices information to help you find the nearest store which will sell take-at-home covid tests")
    home_locations = centre_locations.loc[centre_locations['home testing'] == 'Y']
    home_list = home_locations.values.tolist()
elif contact == 1 :
    print("You must Isolate for 14 days and do a covid-19 test.We will be accessing your devices information to help you find the nearest open covid testing center")
    
elif 0< score =< 3:
    print("you must isolate yourself for 5 days, if no more symptoms then you are not infected. We will be accessing your devices information and providing you with information regarding where resources such as masks are available. ")
    mask_locations = centre_locations.loc[centre_locations['Masks'] == 'Y']
    mask_list = mask_locations.values.tolist()
else:
    print("Isolate for 7 days if no more symptoms then you are not infected")
    quit()






