mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]


total_missions = 0
successfull_missions = 0
for names in mission_names:
   total_missions += 1
for success in mission_success:
   if success:
       successfull_missions += 1
mission_percentage = (successfull_missions / total_missions)*100
rounded_mission_percentage = round(mission_percentage, 2)


print(" total missons:",  total_missions,  "\n",  "total successfull missions:", successfull_missions, "\n", "success rate:", rounded_mission_percentage, "%")
for name, years in zip(mission_names, mission_years):
   if years < 2000:
       print(name)