max_cars= 100
today_drivers= 30
pass_waiting= 90
pass_per_driver=4

print("There are {} cars available on this app.".format(max_cars))
print("There are {} drivers registered today, and {} empty cars.".format(today_drivers, max_cars-today_drivers))
print("Today we can transport up to {} passengers.".format(today_drivers*pass_per_driver))
print("There are {} passengers waiting, so we can put an average of {} passengers in each car.".format(pass_waiting, pass_waiting/today_drivers))


