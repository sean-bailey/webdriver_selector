#from webdriver_selector.webdrivers import *
import webdriver_selector.webdrivers as wd
import inspect
import os

os.environ['WDM_LOG_LEVEL'] = '0'


def functions():
    return inspect.getmembers(wd, inspect.isfunction)

class selector:

    def __init__(self,chosendriver="randomDriver",force=True,headless=True):
        self.chosendriver=chosendriver
        self.force=force
        self.headless=headless
        availablefunctions=functions()
        driver=None
        for function in availablefunctions:
            if self.chosendriver == function[0]:
                if self.chosendriver=="randomDriver":
                    driver=function[1](self.force,self.headless)
                else:
                    driver=function[1](self.headless)
        self.availablefunctions=availablefunctions
        self.driver=driver
        self.finalfunctionstring=""
        if self.driver is None:
            #finalfunctionstring=""
            for function in availablefunctions:
                self.finalfunctionstring+=function[0]+", "
            raise ValueError("Error, either you have no compatible browsers installed or did not use one of the available choices: "+finalfunctionstring)




