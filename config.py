import json
from selenium import webdriver

# some JSON:
x = '{ "BASE_URL":"https://oladoc.com/sitemaps/sitemap_doctors", "BASE_BROWSER":"chrome"}'

# parse x:
KEYS = json.loads(x)


# the result is a Python dictionary:
# print(y["BASE_BROWSER"])
# print(y["BASE_URL"])
listOfURL=[
    "https://oladoc.com/",
    "https://oladoc.com/pakistan/islamabad/gynecologist",
    "https://oladoc.com/pakistan/islamabad/dermatologist",
    "https://oladoc.com/pakistan/islamabad/child-specialist",
    "https://oladoc.com/pakistan/islamabad/orthopedic-surgeon"
    ]

if KEYS["BASE_BROWSER"] == "firefox":
    driver = webdriver.Firefox()
elif KEYS["BASE_BROWSER"] == "chrome":
    driver = webdriver.Chrome('./webDrivers/chromedriver')  # Optional argument, if not specified will search path.
elif KEYS["BASE_BROWSER"] == "IE":
    pass
elif KEYS["BASE_BROWSER"] == "safari":
    pass
elif KEYS["BASE_BROWSER"] == "opera":
    pass
else:
    print("Wrong Input ---> Please add valid Browser Name\n\n")