# Test to ensure that the web app and the results window at the end of the typing test display properly
# Test Scenario 5, Test Case 3

def TestDisplayEdge():
    #Launches the specified browser and opens the specified URL in it.
    Browsers.Item[btEdge].Run("https://stephenlandaas.com/TuffyTypes/")
    Aliases.browser.BrowserWindow.Maximize()
    #Selects the '60 seconds' item of the 'selectTimer1' combo box.
    Aliases.browser.pageTuffytypes.selectTimer1.ClickItem("60 seconds")
    OCR.Recognize(Aliases.browser.wndChrome_WidgetWin_1.Chrome_RenderWidgetHostHWND).BlockByText("seconds", spBottomMost).Click()
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
    #Selects the '15 seconds' item of the 'selectTimer1' combo box.
    Aliases.browser.pageTuffytypes.selectTimer1.ClickItem("15 seconds")
    #Waits until the browser loads the page and is ready to accept user input.
    Aliases.browser.pageTuffytypes.Wait()
    #Checks whether the 'contentText' property of the Aliases.browser.pageTuffytypes.FindElement("#timer") object equals 'Seconds Remaining: 15'.
    aqObject.CheckProperty(Aliases.browser.pageTuffytypes.FindElement("#timer"), "contentText", cmpEqual, "Seconds Remaining: 15")
    #Enters ' ' in the 'textnodeCsufTuffytypes' object.
    Aliases.browser.pageTuffytypes.textnodeCsufTuffytypes.Keys(" ")
    #Delays the test execution for the specified time period.
    Delay(15000)
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
