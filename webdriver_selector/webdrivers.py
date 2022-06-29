from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager
from user_agent import generate_user_agent, generate_navigator
from webdriver_manager.utils import ChromeType
from selenium.webdriver.common.proxy import Proxy, ProxyType
import random
import warnings
import sys
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
        
        sys.stdout.write('\x1b[1K\r')
        sys.stdout.write("chromeinstaller installed")
        break
    except Exception as e:
        checkvalue=str(str(e))
        if "API rate limit exceeded" in checkvalue:
            
            sys.stdout.write('\x1b[1K\r')
            sys.stdout.write("You've exceeded the Github API Rate limit for running the installers for webdrivers. Please try again in an hour.")
        else:
            sys.stdout.write("Cannot install chromedriver")
            
            sys.stdout.write('\x1b[1K\r')
            sys.stdout.write(str(e))
            
            sys.stdout.write('\x1b[1K\r')

        break

while True:
    try:
        chromiuminstaller=ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()
        availablefunctions.append("chromium")
        
        sys.stdout.write('\x1b[1K\r')
        sys.stdout.write("chromiuminstaller installed")
        break
    except Exception as e:
        checkvalue=str(str(e))
        if "API rate limit exceeded" in checkvalue:
            
            sys.stdout.write('\x1b[1K\r')
            sys.stdout.write("You've exceeded the Github API Rate limit for running the installers for webdrivers. Please try again in an hour.")
        else:
            
            sys.stdout.write('\x1b[1K\r')
            sys.stdout.write("Cannot install chromium-driver")
            sys.stdout.write(str(e))
            
            sys.stdout.write('\x1b[1K\r')
        break

while True:
    try:
        edgeinstaller=EdgeChromiumDriverManager().install()
        availablefunctions.append("edge")
        
        sys.stdout.write('\x1b[1K\r')
        sys.stdout.write("edgeinstaller installed")
        break
    except Exception as e:
        checkvalue=str(str(e))
        if "API rate limit exceeded" in checkvalue:
            
            sys.stdout.write('\x1b[1K\r')
            sys.stdout.write("You've exceeded the Github API Rate limit for running the installers for webdrivers. Please try again in an hour.")
        else:
            
            sys.stdout.write('\x1b[1K\r')
            sys.stdout.write("Cannot install edgedriver")
            sys.stdout.write(str(e))
            
            sys.stdout.write('\x1b[1K\r')
        break
"""
#I am experiencing some issues with opera on ubuntu 20...
while True:
    try:
        operainstaller=OperaDriverManager().install()
        availablefunctions.append('opera')
        sys.stdout.write("operainstaller installed")
        break
    except Exception as e:
        checkvalue=str(str(e))
        if "API rate limit exceeded" in checkvalue:

            sys.stdout.write("You've exceeded the Github API Rate limit for running the installers for webdrivers. Please try again in an hour.")
        else:
            sys.stdout.write("Cannot install operadriver")
            sys.stdout.write(str(e))

sys.stdout.write('\x1b[1K\r')
        break
"""
while True:
    try:
        firefoxinstaller=GeckoDriverManager().install()
        availablefunctions.append("firefox")
        
        sys.stdout.write('\x1b[1K\r')
        sys.stdout.write("firefoxinstaller installed")
        break
    except Exception as e:
        checkvalue=str(str(e))
        if "API rate limit exceeded" in checkvalue:
            
            sys.stdout.write('\x1b[1K\r')
            sys.stdout.write("You've exceeded the Github API Rate limit for running the installers for webdrivers. Please try again in an hour.")
        else:
            
            sys.stdout.write('\x1b[1K\r')
            sys.stdout.write("Cannot install firefoxdriver")

            sys.stdout.write(str(e))

        break


def phantomJS(headless=True,incognito=True,random_useragent=True):
    driver=None
    try:
        driver=webdriver.PhantomJS()

    except Exception as e:
        if driver is not None:
            driver.quit()
            driver=None
        
        sys.stdout.write('\x1b[1K\r')
        sys.stdout.write("failure in phantomJS function")
        sys.stdout.write(str(e))
        
        sys.stdout.write('\x1b[1K\r')
    return driver

def chrome(headless=True,incognito=True,random_useragent=True,proxy_ip=None,proxy_port=None):
    driver=None
    try:
        options = webdriver.ChromeOptions()
        if random_useragent:
            options.add_argument('user-agent=' + str(generate_user_agent()) + '')
        if incognito:
            options.add_argument("--incognito")
        options.add_argument("--ignore_certificate_errors")
        if headless:
            options.add_argument("--headless")
        if proxy_ip is not None:
            if proxy_port is not None:
                PROXY=proxy_ip+":"+proxy_port

                prox = Proxy()
                prox.proxy_type = ProxyType.MANUAL
                prox.http_proxy = PROXY
                #prox.socks_proxy = PROXY
                prox.ssl_proxy = PROXY

                capabilities = webdriver.DesiredCapabilities.CHROME
                prox.add_to_capabilities(capabilities)
                driver = webdriver.Chrome(chromeinstaller, chrome_options=options,desired_capabilities=capabilities)
        #        options.add_argument('--proxy-server=%s' % PROXY)
            else:
                raise ValueError("You must include which port to use for your proxy.")
        else:
            driver = webdriver.Chrome(chromeinstaller, chrome_options=options)

    except Exception as e:
        if driver is not None:
            driver.quit()
            driver=None
        
        sys.stdout.write('\x1b[1K\r')
        sys.stdout.write("failure in chrome function")
        sys.stdout.write(str(e))
        
        sys.stdout.write('\x1b[1K\r')
    return driver

def chromium(headless=True,incognito=True,random_useragent=True,proxy_ip=None,proxy_port=None):
    driver = None
    proxy=None
    try:
        options = webdriver.ChromeOptions()
        if random_useragent:
            options.add_argument('user-agent=' + str(generate_user_agent()) + '')
        if incognito:
            options.add_argument("--incognito")
        options.add_argument("--ignore_certificate_errors")
        if headless:
            options.add_argument("--headless")
        if proxy_ip is not None:
            if proxy_port is not None:
                PROXY = proxy_ip + ":" + proxy_port

                prox = Proxy()
                prox.proxy_type = ProxyType.MANUAL
                prox.http_proxy = PROXY
                #prox.socks_proxy = PROXY
                prox.ssl_proxy = PROXY

                capabilities = webdriver.DesiredCapabilities.CHROME
                prox.add_to_capabilities(capabilities)
                driver = webdriver.Chrome(chromiuminstaller, chrome_options=options, desired_capabilities=capabilities)
            #        options.add_argument('--proxy-server=%s' % PROXY)
            else:
                raise ValueError("You must include which port to use for your proxy.")
        else:
            driver = webdriver.Chrome(chromiuminstaller, chrome_options=options)

    except Exception as e:
        if driver is not None:
            driver.quit()
            driver=None
        
        sys.stdout.write('\x1b[1K\r')
        sys.stdout.write("failure in chromium function")
        sys.stdout.write(str(e))
        
        sys.stdout.write('\x1b[1K\r')
    return driver

def edge(headless=True,incognito=True,random_useragent=True,proxy_ip=None,proxy_port=None):
    driver = None
    try:
        edge_options = webdriver.EdgeOptions()
        edge_options.use_chromium = True
        if headless:
            edge_options.add_argument("headless")

        if proxy_ip is not None:
            if proxy_port is not None:
                PROXY=proxy_ip+":"+proxy_port

                prox = Proxy()
                prox.proxy_type = ProxyType.MANUAL
                prox.http_proxy = PROXY
                #prox.socks_proxy = PROXY
                prox.ssl_proxy = PROXY

                capabilities = webdriver.DesiredCapabilities.EDGE
                prox.add_to_capabilities(capabilities)
                driver = webdriver.Edge(edgeinstaller, options=edge_options,desired_capabilities=capabilities)
        #        options.add_argument('--proxy-server=%s' % PROXY)
            else:
                raise ValueError("You must include which port to use for your proxy.")
        else:
            driver = webdriver.Edge(edgeinstaller, options=edge_options)




    except Exception as e:
        if driver is not None:
            driver.quit()
            driver=None
        
        sys.stdout.write('\x1b[1K\r')
        sys.stdout.write("failure in edge function")
        sys.stdout.write(str(e))
        
        sys.stdout.write('\x1b[1K\r')
    return driver

def opera(headless=True,incognito=True,random_useragent=True,proxy_ip=None,proxy_port=None):
    driver=None
    proxy = None
    try:
        options = webdriver.ChromeOptions()
        if random_useragent:
            options.add_argument('user-agent=' + str(generate_user_agent()) + '')
        if incognito:
            options.add_argument("--incognito")
        options.add_argument("--ignore_certificate_errors")
        if headless:
            options.add_argument("--headless")

        if proxy_ip is not None:
            if proxy_port is not None:
                PROXY=proxy_ip+":"+proxy_port

                prox = Proxy()
                prox.proxy_type = ProxyType.MANUAL
                prox.http_proxy = PROXY
                #prox.socks_proxy = PROXY
                prox.ssl_proxy = PROXY

                capabilities = webdriver.DesiredCapabilities.CHROME
                prox.add_to_capabilities(capabilities)
                driver = webdriver.Chrome(operainstaller, chrome_options=options,desired_capabilities=capabilities)
        #        options.add_argument('--proxy-server=%s' % PROXY)
            else:
                raise ValueError("You must include which port to use for your proxy.")
        else:
            driver = webdriver.Chrome(operainstaller, chrome_options=options)

    except Exception as e:
        if driver is not None:
            driver.quit()
            driver=None
        
        sys.stdout.write('\x1b[1K\r')
        sys.stdout.write("failure in opera function")
        sys.stdout.write(str(e))
        
        sys.stdout.write('\x1b[1K\r')
    return driver

def firefox(headless=True,incognito=True,random_useragent=True,proxy_ip=None,proxy_port=None,protocol=None):
    driver=None
    proxy=None
    try:
        firefox_profile = webdriver.FirefoxProfile()
        if incognito:
            firefox_profile.set_preference("browser.privatebrowsing.autostart", True)
        if random_useragent:
            firefox_profile.set_preference("general.useragent.override", str(generate_user_agent()))

        options = webdriver.FirefoxOptions()
        options.set_preference("dom.webnotifications.serviceworker.enabled", False)
        options.set_preference("dom.webnotifications.enabled", False)

        if headless:
            options.add_argument('--headless')

        if proxy_ip is not None:
            if proxy_port is not None:
                PROXY=proxy_ip+":"+proxy_port

                prox = Proxy()
                prox.proxy_type = ProxyType.MANUAL
                prox.http_proxy = PROXY
                #prox.socks_proxy = PROXY
                prox.ssl_proxy = PROXY

                capabilities = webdriver.DesiredCapabilities.FIREFOX
                prox.add_to_capabilities(capabilities)
                driver = webdriver.Firefox(executable_path=firefoxinstaller, firefox_profile=firefox_profile,
                                       options=options,desired_capabilities=capabilities)
        #        options.add_argument('--proxy-server=%s' % PROXY)
            else:
                raise ValueError("You must include which port to use for your proxy.")
        else:
            driver = webdriver.Firefox(executable_path=firefoxinstaller, firefox_profile=firefox_profile,
                                       options=options)

    except Exception as e:
        if driver is not None:
            driver.quit()
            driver=None
        
        sys.stdout.write('\x1b[1K\r')
        sys.stdout.write("failure in firefox function")
        sys.stdout.write(str(e))
        
        sys.stdout.write('\x1b[1K\r')
    return driver






def randomDriver(force=True,headless=True,incognito=True,random_useragent=True,proxy_ip=None,proxy_port=None):
    functions={"firefox":firefox,"chrome":chrome,"chromium":chromium,"opera":opera,"edge":edge}
    functionlist=availablefunctions
    random.shuffle(functionlist)
    driver=None
    if force:
        while driver is None:
            funchoice=random.choice(functionlist)
            driver=functions[funchoice](headless,incognito,random_useragent,proxy_ip,proxy_port)
        return driver
    else:
        return random.choice(list(functions.keys()))(headless,incognito,random_useragent,proxy_ip,proxy_port)
