def nightBtnLoopImage():
    #Iterates through the specified browsers.
    i = 0
    while i < Browsers.Count:
        Browsers.Item[i].Run("https://stephenlandaas.com/TuffyTypes/")
        #Maximizes the 'BrowserWindow' window.
        Aliases.browser.BrowserWindow.Maximize()
        #Checks whether the 'contentText' property of the Aliases.browser.pageTuffytypes.FindElement("//label[contains(@class, 'label')]") object equals ''.
        aqObject.CheckProperty(Aliases.browser.pageTuffytypes.FindElement("//label[contains(@class, 'label')]"), "contentText", cmpEqual, "")
        #Clicks the 'panel' control.
        Aliases.browser.pageTuffytypes.label.panel.Click()
        #Checks whether the 'Enabled' property of the Aliases.browser.pageTuffytypes.FindElement("//label[contains(@class, 'label')]") object equals True.
        aqObject.CheckProperty(Aliases.browser.pageTuffytypes.FindElement("//label[contains(@class, 'label')]"), "Enabled", cmpEqual, True)
        #Clicks the 'panel' control.
        Aliases.browser.pageTuffytypes.label.panel.Click()
        #Checks whether the 'contentText' property of the Aliases.browser.pageTuffytypes.FindElement("//i[contains(@class, 'fa-sun')]") object equals ''.
        aqObject.CheckProperty(Aliases.browser.pageTuffytypes.FindElement("//i[contains(@class, 'fa-sun')]"), "contentText", cmpEqual, "")
        #Clicks the 'panel' control.
        Aliases.browser.pageTuffytypes.label.panel.Click()
        #Checks whether the 'contentText' property of the Aliases.browser.pageTuffytypes.FindElement("//i[contains(@class, 'fa-moon')]") object equals ''.
        aqObject.CheckProperty(Aliases.browser.pageTuffytypes.FindElement("//i[contains(@class, 'fa-moon')]"), "contentText", cmpEqual, "")
        
        # ***BUGGY IMAGE SCRIPTS***
        #Clicks the 'panel' control.
        #Aliases.browser.pageTuffytypes.label.panel.Click()
        #Compares the pageTuffytypes Stores item with the image of the Regions.CreateRegionInfo(Aliases.browser.pageTuffytypes, 377, 587, 1819, 387, False) object.
        #Regions.pageTuffytypes.Check(Regions.CreateRegionInfo(Aliases.browser.pageTuffytypes, 377, 587, 1819, 387, False))
        #Clicks the 'panel' control.
        #Aliases.browser.pageTuffytypes.label.panel.Click()
        #Compares the pageTuffytypes1 Stores item with the image of the Regions.CreateRegionInfo(Aliases.browser.pageTuffytypes, 522, 577, 1633, 400, False) object.
        #Regions.pageTuffytypes1.Check(Regions.CreateRegionInfo(Aliases.browser.pageTuffytypes, 522, 577, 1633, 400, False))
        
        i = i + 1
        #This step closes the current browser
        Aliases.Browser.Close(30000);
