#!/usr/bin/python3

class Gemeinsam():
    def __init__(self, where, water_warm, water_cold, heating) -> None:
        self.lokalisation = where
        self.warm = water_warm
        self.difference_ww = 0
        self.cold = water_cold
        self.difference_wc = 0
        self.heater = heating
        self.difference_h = 0

    def warm_get(self):
        return self._warm
    def warm_set(self, val):
        help = self.warm
        self.warm += val
        self.difference_ww = self.warm - help

    def cold_get(self):
        return self._cold
    def cold_set(self, val):
        help = self.cold
        self.cold += val
        self.difference_wc = self.cold - help

    def heater_get(self):
        return self.heater
    def heater_set(self, val):
        help = self.heater
        self.heater += val
        self.difference_h = self.heater - help
    
    def getall(self):
        return {'zaehler':[self.warm, self.cold, self.heater], 'differences':[self.difference_ww, self.difference_wc, self.difference_h]}
    


class Zimmer:
    def __init__(self, name , val) -> None:
        self.room = name
        self.heater = val
        self.difference_h = 0

    def heater_get(self):
        return self.heater
    def heater_set(self, val):
        help = self.heater
        self.heater += val
        self.difference_h = self.heater - help

    def getall(self):
        return {'zaehler:':[self.heater], 'differences':[self.difference_h]}