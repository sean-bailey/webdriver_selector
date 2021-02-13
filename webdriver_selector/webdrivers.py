from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager
from fake_useragent import UserAgent
from webdriver_manager.utils import ChromeType
import random
import warnings
warnings.filterwarnings('ignore')
import os
import time
os.environ['WDM_LOG_LEVEL'] = '0'
chromeattempt=False
chromiumattempt=False
edgeattempt=False
operaattempt=False
firefoxattempt=False

while not chromeattempt:
    try:
        #print("Installing chromeinstaller...")
        chromeinstaller=ChromeDriverManager().install()
        chromeattempt=True
        break
    except Exception as e:
        checkvalue=str(e)
        if "API rate limit exceeded" in checkvalue:
            time.sleep(3600)
            print("You've exceeded the Github API Rate limit for running the installers for webdrivers. This program will sleep for an hour and try again.")
        else:
            print("Cannot install chromedriver")
            chromeattempt=True
            break

while not chromiumattempt:
    try:
        chromiuminstaller=ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()
        chromiumattempt=True
        break
    except Exception as e:
        checkvalue=str(e)
        if "API rate limit exceeded" in checkvalue:
            time.sleep(3600)
            print("You've exceeded the Github API Rate limit for running the installers for webdrivers. This program will sleep for an hour and try again.")
        else:
            print("Cannot install chromium-driver")
            chromiumattempt=True
            break

while not edgeattempt:
    try:
        edgeinstaller=EdgeChromiumDriverManager().install()
        edgeattempt=True
        break
    except Exception as e:
        checkvalue=str(e)
        if "API rate limit exceeded" in checkvalue:
            time.sleep(3600)
            print("You've exceeded the Github API Rate limit for running the installers for webdrivers. This program will sleep for an hour and try again.")
        else:
            print("Cannot install edgedriver")
            edgeattempt=True
            break

while not operaattempt:
    try:
        operainstaller=OperaDriverManager().install()
        operaattempt=True
        break
    except Exception as e:
        checkvalue=str(e)
        if "API rate limit exceeded" in checkvalue:
            time.sleep(3600)
            print("You've exceeded the Github API Rate limit for running the installers for webdrivers. This program will sleep for an hour and try again.")
        else:
            print("Cannot install operadriver")
            operaattempt=True
            break

while not firefoxattempt:
    try:
        firefoxinstaller=GeckoDriverManager().install()
        firefoxattempt=True
        break
    except Exception as e:
        checkvalue=str(e)
        if "API rate limit exceeded" in checkvalue:
            time.sleep(3600)
            print("You've exceeded the Github API Rate limit for running the installers for webdrivers. This program will sleep for an hour and try again.")
        else:
            print("Cannot install firefoxdriver")
            firefoxattempt=True
            break


def phantomJS():
    try:
        driver=webdriver.PhantomJS()
        return driver
    except Exception as e:
        print("failure in phantomJS function")
        print(e)
        return None

def chrome():
    try:
        options = webdriver.ChromeOptions()
        options.add_argument('user-agent=' + str(UserAgent().random) + '')
        options.add_argument("--incognito")
        options.add_argument("--ignore_certificate_errors")
        options.add_argument("--headless")
        driver = webdriver.Chrome(chromeinstaller,chrome_options=options)
        return driver
    except Exception as e:
        print("failure in chrome function")
        print(e)
        return None

def chromium():
    try:
        options = webdriver.ChromeOptions()
        options.add_argument('user-agent=' + str(UserAgent().random) + '')
        options.add_argument("--incognito")
        options.add_argument("--ignore_certificate_errors")
        options.add_argument("--headless")
        driver = webdriver.Chrome(chromiuminstaller,chrome_options=options)
        return driver
    except Exception as e:
        print("failure in chromium function")
        print(e)
        return None

def edge():
    try:
        edge_options = webdriver.EdgeOptions()
        edge_options.use_chromium = True
        edge_options.add_argument("headless")
        edge_options.add_argument("disable-gpu")
        driver = webdriver.Edge(edgeinstaller,options=edge_options)
    except Exception as e:
        print("failure in edge function")
        print(e)
        return None

def opera():
    try:
        options = webdriver.ChromeOptions()
        options.add_argument('user-agent=' + str(UserAgent().random) + '')
        options.add_argument("--incognito")
        options.add_argument("--ignore_certificate_errors")
        options.add_argument("--headless")
        driver = webdriver.Chrome(executable_path=operainstaller,chrome_options=options)
        return driver
    except Exception as e:
        print("failure in chromium function")
        print(e)
        return None

def firefox():
    try:
        firefox_profile = webdriver.FirefoxProfile()
        firefox_profile.set_preference("browser.privatebrowsing.autostart", True)
        firefox_profile.set_preference("general.useragent.override", UserAgent().random)
        options = webdriver.FirefoxOptions()
        options.set_preference("dom.webnotifications.serviceworker.enabled", False)
        options.set_preference("dom.webnotifications.enabled", False)
        options.add_argument('--headless')
        driver = webdriver.Firefox(executable_path=firefoxinstaller,firefox_profile=firefox_profile, options=options)
    except Exception as e:
        print("failure in firefox function")
        print(e)
        return None

def randomDriver(force=True):
    #functionlist=["firefox","chrome","phantomJS","phantomJS":phantomJS]
    functions={"firefox":firefox,"chrome":chrome,"chromium":chromium,"opera":opera,"edge":edge}
    driver=None
    if force:
        checkdict = {}
        for key in functions.keys():
            checkdict[key]=0
        while driver is None:
            if not any(x == 0 for x in checkdict.values()):
                return None
            funchoice=random.choice(list(functions.keys()))
            checkdict[funchoice]+=1

            driver=functions[funchoice]()
        return driver
    else:
        return random.choice(list(functions.keys()))()
