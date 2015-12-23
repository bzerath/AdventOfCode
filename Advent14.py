# -*- coding: utf-8 -*-
from __future__ import unicode_literals  # Everything is UTF-8
from pprint import pprint


def checking_leader(rennes):
    maxi = 0
    leaders = []
    for renne in rennes:
        if renne.distance > maxi:
            leaders = [renne]
            maxi = renne.distance
        elif renne.distance == maxi:
            leaders.append(renne)

    for renne in leaders:
        renne.points += 1


class Renne:
    def __init__(self, name, speed, time, rest):
        self.name = name
        self.speed = speed
        self.time = time
        self.rest = rest

        self.points = 0

        self.distance = 0
        self.status = "flying"
        self.energy = time
        self.seconds = 0

    def action(self):
        self.seconds += 1
        if self.status == "flying":
            self.distance += self.speed
            self.energy -= 1
            if self.energy == 0:
                self.energy = self.rest
                self.status = "resting"
                #print self.seconds, ":", self.name, "is resting..."

        elif self.status == "resting":
            self.energy -= 1
            if self.energy == 0:
                self.status = "flying"
                self.energy = self.time
                #print self.seconds, ":", self.name, "is up !"


    def __str__(self):
        return "{nom} a parcouru {distance} km au bout de {temps} secondes, et a gagné {points} points !".format(nom=self.name,
                                                                                                                 distance=self.distance,
                                                                                                                 temps=self.seconds,
                                                                                                                 points=self.points).encode("utf-8")



"""input = ["Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.",
         "Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds."]"""

input = ["Vixen can fly 19 km/s for 7 seconds, but then must rest for 124 seconds.",
         "Rudolph can fly 3 km/s for 15 seconds, but then must rest for 28 seconds.",
         "Donner can fly 19 km/s for 9 seconds, but then must rest for 164 seconds.",
         "Blitzen can fly 19 km/s for 9 seconds, but then must rest for 158 seconds.",
         "Comet can fly 13 km/s for 7 seconds, but then must rest for 82 seconds.",
         "Cupid can fly 25 km/s for 6 seconds, but then must rest for 145 seconds.",
         "Dasher can fly 14 km/s for 3 seconds, but then must rest for 38 seconds.",
         "Dancer can fly 3 km/s for 16 seconds, but then must rest for 37 seconds.",
         "Prancer can fly 25 km/s for 6 seconds, but then must rest for 143 seconds."]


rennes = []
for phrase in input:
    phrase = phrase.split(" ")
    rennes.append(Renne(phrase[0], int(phrase[3]), int(phrase[6]), int(phrase[13])))


for second in range(2503):
    for renne in rennes:
        renne.action()
    checking_leader(rennes)


print "P1:", sorted(rennes, key=lambda renne: renne.distance)[-1]
print "P2:", sorted(rennes, key=lambda renne: renne.points)[-1]




