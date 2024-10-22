input_month = input().capitalize()
input_day = int(input())

spring = ['March', 'April', 'May', 'June']
summer = ['June', 'July', 'August', 'September']
autumn = ['September', 'October', 'November', 'December']
winter = ['December', 'January', 'February', 'March']

season = ''

# Check for valid day in February
if input_month == 'February' and (input_day < 1 or input_day > 29):
    season = 'Invalid'
# Check for valid day in months with 30 days
elif input_month in ['April', 'June', 'September', 'November'] and (input_day < 1 or input_day > 30):
    season = 'Invalid'
# Check for valid day in months with 31 days
elif input_day < 1 or input_day > 31:
    season = 'Invalid'
# Determine the season
elif (input_month == 'March' and input_day >= 20) or input_month in ['April', 'May'] or (input_month == 'June' and input_day < 21):
    season = 'Spring'
elif (input_month == 'June' and input_day >= 21) or input_month in ['July', 'August'] or (input_month == 'September' and input_day < 23):
    season = 'Summer'
elif (input_month == 'September' and input_day >= 23) or input_month in ['October', 'November'] or (input_month == 'December' and input_day < 21):
    season = 'Autumn'
elif (input_month == 'December' and input_day >= 21) or input_month in ['January', 'February'] or (input_month == 'March' and input_day < 20):
    season = 'Winter'
else:
    season = 'Invalid'

print(season)
