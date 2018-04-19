import time
from threading import Event

from PinHandler import PinHandler
from RancilioError import RancilioError


class SystemHealthMonitor:
    stopEvent: Event

    def __init__(self):
        self.stopEvent = None
        self.rancilioError = RancilioError.instance()
        self.pinHandler = PinHandler.instance()

    def run(self):
        if self.stopEvent is None:
            return
        while not self.stopEvent.is_set():
            if self.rancilioError.tempSensorFail[0]:
                self.pinHandler.setHeater(0)
                self.rancilioError.blynkShutDownFcn()
            if self.rancilioError.blynkAliveFcn() == 0:
                self.pinHandler.setHeater(0)
                self.rancilioError.blynkShutDownFcn()

            time.sleep(0.5)
