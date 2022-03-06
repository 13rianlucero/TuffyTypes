def TestCase2():
    Browsers.Item[btChrome].Navigate("https://stephenlandaas.com/TuffyTypes/")
    Delay(3000)
    Var1 = Aliases.browser.pageTuffytypes.FindElement("#generated-quote").contentText
    Log.Message(Var1)
    aqObject.CheckProperty(Aliases.browser.pageTuffytypes.FindElement("#timer"), "contentText", cmpEqual, "Seconds Remaining: 60")
    Aliases.browser.pageTuffytypes.buttonRestartbutton.ClickButton()
    Delay(3000)
    Var2 = Aliases.browser.pageTuffytypes.FindElement("#generated-quote").contentText
    Log.Message(Var2)
    if Var1 != Var2:
      Log.Message("Restart button replaces the quote")
    else:
      Log.Message("Restart button does not replace the quote")
    aqObject.CheckProperty(Aliases.browser.pageTuffytypes.FindElement("#timer"), "contentText", cmpEqual, "Seconds Remaining: 60")
