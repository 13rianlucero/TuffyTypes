#Test Scenario 1, Case 1

def TestCase1():
    Browsers.Item[btChrome].Navigate("https://stephenlandaas.com/TuffyTypes/")
    aqObject.CheckProperty(Aliases.browser.pageTuffytypes.FindElement("#restartButton"), "contentText", cmpEqual, "")
