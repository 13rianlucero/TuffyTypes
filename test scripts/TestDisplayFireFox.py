#Test to ensure that the web app and the results window at the end of the typing test display properly
def Test1():
    #Launches the specified browser and opens the specified URL in it.
    Browsers.Item[btFirefox].Run("https://stephenlandaas.com/TuffyTypes/")
    #Checks whether the 'contentText' property of the Aliases.browser.pageTuffytypes.FindElement("//a[contains(text(), 'CSUF TuffyTypes')]") object equals 'CSUF TuffyTypes'.
    aqObject.CheckProperty(Aliases.browser.pageTuffytypes.FindElement("//a[contains(text(), 'CSUF TuffyTypes')]"), "contentText", cmpEqual, "CSUF TuffyTypes")
    #Checks whether the 'contentText' property of the Aliases.browser.pageTuffytypes.FindElement("#main-title") object equals 'Start Typing To Begin!'.
    aqObject.CheckProperty(Aliases.browser.pageTuffytypes.FindElement("#main-title"), "contentText", cmpEqual, "Start Typing To Begin!")
    #Checks whether the 'contentText' property of the Aliases.browser.pageTuffytypes.FindElement("#timer") object equals 'Seconds Remaining: 60'.
    aqObject.CheckProperty(Aliases.browser.pageTuffytypes.FindElement("#timer"), "contentText", cmpEqual, "Seconds Remaining: 60")
    #Checks whether the 'contentText' property of the Aliases.browser.pageTuffytypes.FindElement("//h4[.='Select Timer:']") object equals 'Select Timer:'.
    aqObject.CheckProperty(Aliases.browser.pageTuffytypes.FindElement("//h4[.='Select Timer:']"), "contentText", cmpEqual, "Select Timer:")
    #Checks whether the 'contentText' property of the Aliases.browser.pageTuffytypes.FindElement("//h4[.='Restart:']") object equals 'Restart:'.
    aqObject.CheckProperty(Aliases.browser.pageTuffytypes.FindElement("//h4[.='Restart:']"), "contentText", cmpEqual, "Restart:")
    #Clicks the 'textnode3' control.
    Aliases.browser.pageTuffytypes.textnode3.Click()
    #Enters ' ' in the 'pageTuffytypes' object.
    Aliases.browser.pageTuffytypes.Keys(" ")
    #Delays the test execution for the specified time period.
    Delay(60000)
    #Checks whether the 'contentText' property of the Aliases.browser.pageTuffytypes.FindElement("//div[contains(@class, 'modal-content')]") object equals 'WPM: 0
    #Words Typed: 0
    #Errors: 1
    #Accuracy: 0%
    #Play again?'.
    aqObject.CheckProperty(Aliases.browser.pageTuffytypes.FindElement("//div[contains(@class, 'modal-content')]"), "contentText", cmpEqual, "WPM: 0\nWords Typed: 0\nErrors: 1\nAccuracy: 0%\nPlay again?")
    #Checks whether the 'contentText' property of the Aliases.browser.pageTuffytypes.FindElement("#wordspermin-2") object equals 'WPM: 0'.
    aqObject.CheckProperty(Aliases.browser.pageTuffytypes.FindElement("#wordspermin-2"), "contentText", cmpEqual, "WPM: 0")
    #Checks whether the 'contentText' property of the Aliases.browser.pageTuffytypes.FindElement("#word-count-2") object equals 'Words Typed: 0'.
    aqObject.CheckProperty(Aliases.browser.pageTuffytypes.FindElement("#word-count-2"), "contentText", cmpEqual, "Words Typed: 0")
    #Checks whether the 'contentText' property of the Aliases.browser.pageTuffytypes.FindElement("#error-count-2") object equals 'Errors: 1'.
    aqObject.CheckProperty(Aliases.browser.pageTuffytypes.FindElement("#error-count-2"), "contentText", cmpEqual, "Errors: 1")
    #Checks whether the 'contentText' property of the Aliases.browser.pageTuffytypes.FindElement("#accuracy-percent-2") object equals 'Accuracy: 0%'.
    aqObject.CheckProperty(Aliases.browser.pageTuffytypes.FindElement("#accuracy-percent-2"), "contentText", cmpEqual, "Accuracy: 0%")
    #Checks whether the 'contentText' property of the Aliases.browser.pageTuffytypes.FindElement("#button") object equals 'Play again?'.
    aqObject.CheckProperty(Aliases.browser.pageTuffytypes.FindElement("#button"), "contentText", cmpEqual, "Play again?")
