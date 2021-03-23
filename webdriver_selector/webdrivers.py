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
chromeinstaller=None
chromiuminstaller=None
edgeinstaller=None
operainstaller=None
firefoxinstaller=None
availablefunctions=[]



while True:
    try:

        chromeinstaller=ChromeDriverManager().install()
        availablefunctions.append("chrome")
        print("chromeinstaller installed")
        break
    except Exception as e:
        checkvalue=str(e)
        if "API rate limit exceeded" in checkvalue:
            print("You've exceeded the Github API Rate limit for running the installers for webdrivers. Please try again in an hour.")

        else:
            print("Cannot install chromedriver")
            print(e)
        break

while True:
    try:
        chromiuminstaller=ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()
        availablefunctions.append("chromium")
        print("chromiuminstaller installed")
        break
    except Exception as e:
        checkvalue=str(e)
        if "API rate limit exceeded" in checkvalue:
            print("You've exceeded the Github API Rate limit for running the installers for webdrivers. Please try again in an hour.")
        else:
            print("Cannot install chromium-driver")
            print(e)
        break

while True:
    try:
        edgeinstaller=EdgeChromiumDriverManager().install()
        availablefunctions.append("edge")
        print("edgeinstaller installed")
        break
    except Exception as e:
        checkvalue=str(e)
        if "API rate limit exceeded" in checkvalue:
            print("You've exceeded the Github API Rate limit for running the installers for webdrivers. Please try again in an hour.")
        else:
            print("Cannot install edgedriver")
            print(e)
        break
"""
#I am experiencing some issues with opera on ubuntu 20...
while True:
    try:
        operainstaller=OperaDriverManager().install()
        availablefunctions.append('opera')
        print("operainstaller installed")
        break
    except Exception as e:
        checkvalue=str(e)
        if "API rate limit exceeded" in checkvalue:

            print("You've exceeded the Github API Rate limit for running the installers for webdrivers. Please try again in an hour.")
        else:
            print("Cannot install operadriver")
            print(e)
        break
"""
while True:
    try:
        firefoxinstaller=GeckoDriverManager().install()
        availablefunctions.append("firefox")
        print("firefoxinstaller installed")
        break
    except Exception as e:
        checkvalue=str(e)
        if "API rate limit exceeded" in checkvalue:
            print("You've exceeded the Github API Rate limit for running the installers for webdrivers. Please try again in an hour.")
        else:
            print("Cannot install firefoxdriver")
            print(e)
        break


def phantomJS(headless=True,incognito=True,random_useragent=True):
    try:
        driver=webdriver.PhantomJS()
        return driver
    except Exception as e:
        if driver:
            driver.quit()
            driver=None
        print("failure in phantomJS function")
        print(e)
        return None

def chrome(headless=True,incognito=True,random_useragent=True):
    try:
        options = webdriver.ChromeOptions()
        if random_useragent:
            options.add_argument('user-agent=' + str(UserAgent().random) + '')
        if incognito:
            options.add_argument("--incognito")
        options.add_argument("--ignore_certificate_errors")
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Chrome(chromeinstaller,chrome_options=options)
        return driver
    except Exception as e:
        if driver:
            driver.quit()
            driver=None
        print("failure in chrome function")
        print(e)
        return None

def chromium(headless=True,incognito=True,random_useragent=True):
    try:
        options = webdriver.ChromeOptions()
        if random_useragent:
            options.add_argument('user-agent=' + str(UserAgent().random) + '')
        if incognito:
            options.add_argument("--incognito")
        options.add_argument("--ignore_certificate_errors")
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Chrome(chromiuminstaller,chrome_options=options)
        return driver
    except Exception as e:
        if driver:
            driver.quit()
            driver=None
        print("failure in chromium function")
        print(e)
        return None

def edge(headless=True,incognito=True,random_useragent=True):
    try:
        edge_options = webdriver.EdgeOptions()
        edge_options.use_chromium = True
        if headless:
            edge_options.add_argument("headless")
        edge_options.add_argument("disable-gpu")
        driver = webdriver.Edge(edgeinstaller,options=edge_options)
        return driver
    except Exception as e:
        if driver:
            driver.quit()
            driver=None
        print("failure in edge function")
        print(e)
        return None

def opera(headless=True,incognito=True,random_useragent=True):
    try:
        options = webdriver.ChromeOptions()
        if random_useragent:
            options.add_argument('user-agent=' + str(UserAgent().random) + '')
        if incognito:
            options.add_argument("--incognito")
        options.add_argument("--ignore_certificate_errors")
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Chrome(executable_path=operainstaller,chrome_options=options)
        return driver
    except Exception as e:
        if driver:
            driver.quit()
            driver=None
        print("failure in opera function")
        print(e)
        return None

def firefox(headless=True,incognito=True,random_useragent=True):
    try:
        firefox_profile = webdriver.FirefoxProfile()
        if incognito:
            firefox_profile.set_preference("browser.privatebrowsing.autostart", True)
        if random_useragent:
            firefox_profile.set_preference("general.useragent.override", UserAgent().random)
        options = webdriver.FirefoxOptions()
        options.set_preference("dom.webnotifications.serviceworker.enabled", False)
        options.set_preference("dom.webnotifications.enabled", False)
        if headless:
            options.add_argument('--headless')
        driver = webdriver.Firefox(executable_path=firefoxinstaller,firefox_profile=firefox_profile, options=options)
        return driver
    except Exception as e:
        if driver:
            driver.quit()
            driver=None
        print("failure in firefox function")
        print(e)
        return None






def randomDriver(force=True,headless=True,incognito=True,random_useragent=True):
    functions={"firefox":firefox,"chrome":chrome,"chromium":chromium,"opera":opera,"edge":edge}
    functionlist=availablefunctions
    random.shuffle(functionlist)
    driver=None
    if force:
        while driver is None:
            funchoice=random.choice(functionlist)
            driver=functions[funchoice](headless,incognito,random_useragent)
        return driver
    else:
        return random.choice(list(functions.keys()))(headless,incognito,random_useragent)
