from math import floor
import datetime



step = 86400
count = 0
since = 1297854000
until = 1297987200

for x in range(0,40):

    print "191833694170168?fields=feed.since(" + str(since) + ").until(" + str(until) + ").fields(actions,type)"
    since = until
    until += step
