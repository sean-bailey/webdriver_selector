# webdriver-selector

webdriver_selector is a module designed to make headless selenium testing with python easier.
If you are on a system and just want the first available webdriver preconfigured with a random useragent and set in headless mode, or if you want to run a known prespecified webdriver for a given browser, this module can do that.

**Installation**:

`pip3 install webdriver-selector`

**Usage**

the `selector` class can be called with two arguments:
`chosendriver`: the preferred webdriver, default to `randomDriver`
`force`: if a `randomDriver` is preferred, it will force checking every available driver until it either exhausts all available browsers and returns `None` or returns a viable driver.

Attributes:

`chosendriver` -- the chosen driver 

`force` -- whether or not to force getting a random driver

`driver` -- the selenium webdriver data selected, defaults to `None`

`availablefunctions` -- the list of tuples of available function names and their functions

`finalfunctionstring` -- a human readable string of available functions to choose from

`headless` -- Bool of either `True` or `False` which specifies if you'd like the browser to be headless or not, defaults to `True`

`incognito` -- Bool which specifies if you'd like to run the browser in incognito or private browsing mode, default `True`

`random_useragent` -- Bool which specifies if you'd like to run the browser with a randomized useragent or keep the one for the selected browser, default `True`


Examples:

```
##Getting the first available selenium webdriver on the system:
import webdriver_selector

driver=webdriver_selector.selector().driver

```

```
##selecting a particular webdriver:
import webdriver_selector

driver=webdriver_selector.selector(chosendriver="chrome").driver

```

Once you have a driver, it is simply now the selenium webdriver, with
useage and documentation found here:

https://selenium-python.readthedocs.io/

