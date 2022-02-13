#!/usr/bin/python3



class Gemeinsam():
    def __init__(self, where, water_warm, water_cold, heating) -> None:
        self.lokalisation = where
        self._warm = water_warm
        self.difference_ww = 0
        self._cold = water_cold
        self.difference_wc = 0
        self._heater = heating
        self.difference_h = 0

    @property
    def warm(self):
        return self._warm
    
    @property
    def cold(self):
        return self._cold

    @property
    def heater(self):
        return self._heater

    @warm.setter
    def warm(self, val):
        help = self._warm
        self._warm += val
        self.difference_ww = self.warm - help

    @cold.setter
    def cold(self, val):
        help = self._cold
        self._cold += val
        self.difference_wc = self._cold - help

    @heater.setter
    def heater(self, val):
        help = self._heater
        self._heater += val
        self.difference_h = self._heater - help
    


class Zimmer:
    def __init__(self, name , val) -> None:
        self.room = name
        self._heater = val

    @property
    def heater(self):
        return self._heater
        
    @heater.setter
    def heater(self, val):
        help = self._heater
        self._heater += val
        self.difference_h = self._heater - help