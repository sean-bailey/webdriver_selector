# webdriver-selector

webdriver_selector is a module designed to make headless selenium testing with python easier.
If you are on a system and just want the first available webdriver preconfigured with a random useragent and set in headless mode, or if you want to run a known prespecified webdriver for a given browser, this module can do that.

**Installation**:

in this directory, run
`pip install .`

**Useage**

the `selector` class can be called with two arguments:
`chosendriver`: the preferred webdriver, default to `randomDriver`
`force`: if a `randomDriver` is preferred, it will force checking every available driver until it either exhausts all available browsers and returns `None` or returns a viable driver.

Attributes:
`chosendriver` -- the chosen driver 
`force` -- whether or not to force getting a random driver
`driver` -- the selenium webdriver data selected, defaults to `None`
`availablefunctions` -- the list of tuples of available function names and their functions
`finalfunctionstring` -- a human readable string of available functions to choose from


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
