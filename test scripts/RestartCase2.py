# Test Scenario 1, Test Case 2

def TestCase2():
    Browsers.Item[btChrome].Navigate("https://stephenlandaas.com/TuffyTypes/")
    Delay(3000)
    Var1 = Aliases.browser.pageTuffytypes.FindElement("#generated-quote").contentText
    Log.Message(Var1)
    TimerVal1 = Aliases.browser.pageTuffytypes.FindElement("#timer").contentText
    Log.Message(TimerVal1)
    Aliases.browser.pageTuffytypes.buttonRestartbutton.ClickButton()
    Delay(3000)
    Var2 = Aliases.browser.pageTuffytypes.FindElement("#generated-quote").contentText
    Log.Message(Var2)
    TimerVal2 = Aliases.browser.pageTuffytypes.FindElement("#timer").contentText
    Log.Message(TimerVal2)
    if Var1 != Var2:
      Log.Message("Restart button replaces the quote")
    else:
      Log.Message("Restart button does not replace the quote")
    if TimerVal1 == TimerVal2:
      Log.Message("UI remains consistent after restart.")
    else:
      Log.Message("UI does not remain consistent after restart.")
