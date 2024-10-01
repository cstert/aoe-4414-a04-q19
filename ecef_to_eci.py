# ecef_to_eci.py
#
# Usage: python3 ecef_to_eci.py year month day hour minute second ecef_x_km ecef_y_km ecef_z_km
# Converts ECEF coordinates to ECI coordinates
# Parameters:
# year: year of date
# month: month of date
# day: day of date
# hour: hour of date
# minute: minute of date
# second: second of date
# ecef_x_km: ECEF x-coordinate in km
# ecef_y_km: ECEF y-coordinate in km
# ecef_z_km: ECEF z-coordinate in km
# Output:
# Prints ECI coordinates in km
#
# Written by Celia Sterthous
# Other contributors: None
#
# See the LICENSE file for the license.
# import Python modules
import sys # argv
import math
# "constants"
W = 7.2921150*10**-5
# helper functions
## function description
# def calc_something(param1, param2):
# pass

# parse script arguments
if len(sys.argv)==10:
 year = int(sys.argv[1])
 month = int(sys.argv[2])
 day = int(sys.argv[3])
 hour = int(sys.argv[4])
 minute = int(sys.argv[5])
 second = float(sys.argv[6])
 ecef_x_km = float(sys.argv[7])
 ecef_y_km = float(sys.argv[8])
 ecef_z_km = float(sys.argv[9])

else:
   print(\
      'Usage: '\
      'python3 ecef_to_eci.py year month day hour minute second ecef_x_km ecef_y_km ecef_z_km'
     )
   exit()
# write script below this line
jd = day - 32075 + 1461*(year+4800+(month-14)/12)/4+367*(month-2-(month-14)/12*12)/12-3*((year+4900+(month-14)/12)/100)/4
JDmidnight = jd-0.5
Dfrac = (second+60*(minute+60*hour))/86400
jd_frac = JDmidnight+Dfrac
Tut1 = (jd-2451545.0)/36525
gmst_ang = 67310.54841+(876600*60*60+8640184.812866)*Tut1+0.093104*(Tut1**2)+(-6.2*0.000001*(Tut1**3))
gmst_rad = math.fmod(gmst_ang%86400*W+2*math.pi,2*math.pi)
eci_x_km = ecef_x_km*math.cos(-gmst_rad)+ecef_y_km*math.sin(-gmst_rad)
eci_y_km = ecef_y_km*math.cos(-gmst_rad)-ecef_x_km*math.sin(-gmst_rad)
eci_z_km = ecef_z_km

print(eci_x_km)
print(eci_y_km)
print(eci_z_km)