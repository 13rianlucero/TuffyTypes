# Test Scenario 7, Cases 1-6

def checkElements():
    #Opens the specified URL in a running instance of the specified browser.
    Browsers.Item[btChrome].Navigate("https://stephenlandaas.com/TuffyTypes/")
    #Checks whether the 'contentText' property of the Aliases.browser.pageTuffytypes.FindElement("//header[contains(., 'CSUF TuffyTypes')]") object equals 'CSUF TuffyTypes'.
    aqObject.CheckProperty(Aliases.browser.pageTuffytypes.FindElement("//header[contains(., 'CSUF TuffyTypes')]"), "contentText", cmpEqual, "CSUF TuffyTypes")
    #Checks whether the 'contentText' property of the Aliases.browser.pageTuffytypes.FindElement("//label[contains(@class, 'label')]") object equals ''.
    aqObject.CheckProperty(Aliases.browser.pageTuffytypes.FindElement("//label[contains(@class, 'label')]"), "contentText", cmpEqual, "")
    #Checks whether the 'contentText' property of the Aliases.browser.pageTuffytypes.FindElement("#main-title") object equals 'Start Typing To Begin!'.
    aqObject.CheckProperty(Aliases.browser.pageTuffytypes.FindElement("#main-title"), "contentText", cmpEqual, "Start Typing To Begin!")
    #Checks whether the 'contentText' property of the Aliases.browser.pageTuffytypes.FindElement("//div[contains(@class, 'stats')]") object contains 'Seconds Remaining: 60
    #'.
    aqObject.CheckProperty(Aliases.browser.pageTuffytypes.FindElement("//div[contains(@class, 'stats')]"), "contentText", cmpContains, "Seconds Remaining: 60\n", False)
    #Checks whether the 'contentText' property of the Aliases.browser.pageTuffytypes.FindElement("#generated-quote") object contains 'a'.
    aqObject.CheckProperty(Aliases.browser.pageTuffytypes.FindElement("#generated-quote"), "contentText", cmpContains, "a", False)
    #Checks whether the 'contentText' property of the Aliases.browser.pageTuffytypes.FindElement("//h4[.='Select Timer:']") object equals 'Select Timer:'.
    aqObject.CheckProperty(Aliases.browser.pageTuffytypes.FindElement("//h4[.='Select Timer:']"), "contentText", cmpEqual, "Select Timer:")
    #Checks whether the 'wText' property of the Aliases.browser.pageTuffytypes.FindElement("#timer1") object equals 'Select your time'.
    aqObject.CheckProperty(Aliases.browser.pageTuffytypes.FindElement("#timer1"), "wText", cmpEqual, "Select your time")
    #Checks whether the 'contentText' property of the Aliases.browser.pageTuffytypes.FindElement("//h4[.='Restart:']") object equals 'Restart:'.
    aqObject.CheckProperty(Aliases.browser.pageTuffytypes.FindElement("//h4[.='Restart:']"), "contentText", cmpEqual, "Restart:")
    #Checks whether the 'contentText' property of the Aliases.browser.pageTuffytypes.FindElement("#restartButton") object equals ''.
    aqObject.CheckProperty(Aliases.browser.pageTuffytypes.FindElement("#restartButton"), "contentText", cmpEqual, "")



def main():
    checkElements()
    Aliases.browser.BrowserWindow.Position(-13, 0, 1936, 1047)
    
    Log.Message("Initial size check completed")
    
    #Drags the 'BrowserWindow' object.
    Aliases.browser.BrowserWindow.Drag(1932, 377, -451, 23)
    checkElements()
    Log.Message("Near full size check completed")
    
    #Drags the 'BrowserWindow' object.
    Aliases.browser.BrowserWindow.Drag(1475, 447, -223, 7)
    checkElements()
    Log.Message("Medium size check completed")
    
    #Drags the 'BrowserWindow' object.
    Aliases.browser.BrowserWindow.Drag(1252, 454, -247, 15)
    checkElements()
    Log.Message("Small size check completed")
    
    #Drags the 'BrowserWindow' object.
    Aliases.browser.BrowserWindow.Drag(1005, 469, -154, 11)
    checkElements()
    Log.Message("Mobile size check completed")
    
    #Drags the 'BrowserWindow' object.
    Aliases.browser.BrowserWindow.Drag(851, 480, -143, 8)
    checkElements()
    Log.Message("Extra small size check completed")
