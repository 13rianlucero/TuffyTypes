#Tests if the selected time matches the corresponding time on the UI.
#Test Scenario #6
def Test_timer():
    #Opens the specified URL in a running instance of the specified browser.
    Browsers.Item[btChrome].Navigate("https://stephenlandaas.com/TuffyTypes/")
    #Checks whether the 'contentText' property of the Aliases.browser.pageTuffytypes.FindElement("#timer") object equals 'Seconds Remaining: 60'.
    aqObject.CheckProperty(Aliases.browser.pageTuffytypes.FindElement("#timer"), "contentText", cmpEqual, "Seconds Remaining: 60")
    #Checks whether the 'contentText' property of the Aliases.browser.pageTuffytypes.FindElement("#restartButton") object equals ''.
    aqObject.CheckProperty(Aliases.browser.pageTuffytypes.FindElement("#restartButton"), "contentText", cmpEqual, "")
    #Selects the '15 Seconds' item of the 'selectTimer1' combo box.
    Aliases.browser.pageTuffytypes.selectTimer1.ClickItem("15 Seconds")
    OCR.Recognize(Aliases.browser.wndChrome_WidgetWin_1.Chrome_RenderWidgetHostHWND).BlockByText("seconds", spLeftMost).Click()
    #Checks whether the 'contentText' property of the Aliases.browser.pageTuffytypes.FindElement("#timer") object equals 'Seconds Remaining: 15'.
    aqObject.CheckProperty(Aliases.browser.pageTuffytypes.FindElement("#timer"), "contentText", cmpEqual, "Seconds Remaining: 15")
    #Checks whether the 'contentText' property of the Aliases.browser.pageTuffytypes.FindElement("#restartButton") object equals ''.
    aqObject.CheckProperty(Aliases.browser.pageTuffytypes.FindElement("#restartButton"), "contentText", cmpEqual, "")
    #Selects the '30 Seconds' item of the 'selectTimer1' combo box.
    Aliases.browser.pageTuffytypes.selectTimer1.ClickItem("30 Seconds")
    OCR.Recognize(Aliases.browser.wndChrome_WidgetWin_1.Chrome_RenderWidgetHostHWND).BlockByText("Seconds", spNearestToCenter).Click()
    #Checks whether the 'contentText' property of the Aliases.browser.pageTuffytypes.FindElement("#timer") object equals 'Seconds Remaining: 30'.
    aqObject.CheckProperty(Aliases.browser.pageTuffytypes.FindElement("#timer"), "contentText", cmpEqual, "Seconds Remaining: 30")
    #Checks whether the 'contentText' property of the Aliases.browser.pageTuffytypes.FindElement("#restartButton") object equals ''.
    aqObject.CheckProperty(Aliases.browser.pageTuffytypes.FindElement("#restartButton"), "contentText", cmpEqual, "")
    #Selects the '45 Seconds' item of the 'selectTimer1' combo box.
    Aliases.browser.pageTuffytypes.selectTimer1.ClickItem("45 Seconds")
    #Waits until the browser loads the page and is ready to accept user input.
    Aliases.browser.pageTuffytypes.Wait()
    #Checks whether the 'contentText' property of the Aliases.browser.pageTuffytypes.FindElement("#timer") object equals 'Seconds Remaining: 45'.
    aqObject.CheckProperty(Aliases.browser.pageTuffytypes.FindElement("#timer"), "contentText", cmpEqual, "Seconds Remaining: 45")
    #Checks whether the 'contentText' property of the Aliases.browser.pageTuffytypes.FindElement("#restartButton") object equals ''.
    aqObject.CheckProperty(Aliases.browser.pageTuffytypes.FindElement("#restartButton"), "contentText", cmpEqual, "")
    #Selects the '60 Seconds' item of the 'selectTimer1' combo box.
    Aliases.browser.pageTuffytypes.selectTimer1.ClickItem("60 Seconds")
    OCR.Recognize(Aliases.browser.wndChrome_WidgetWin_1.Chrome_RenderWidgetHostHWND).BlockByText("seconds", spBottomMost).Click()
    #Checks whether the 'contentText' property of the Aliases.browser.pageTuffytypes.FindElement("#timer") object equals 'Seconds Remaining: 60'.
    aqObject.CheckProperty(Aliases.browser.pageTuffytypes.FindElement("#timer"), "contentText", cmpEqual, "Seconds Remaining: 60")
    #Checks whether the 'contentText' property of the Aliases.browser.pageTuffytypes.FindElement("#restartButton") object equals ''.
    aqObject.CheckProperty(Aliases.browser.pageTuffytypes.FindElement("#restartButton"), "contentText", cmpEqual, "")
