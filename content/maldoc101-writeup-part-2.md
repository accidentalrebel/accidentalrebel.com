The next couple of lines does the same concatenating technique similar to the previous steps. 

```vba
deaknaugthein = roubhaol.kaizseah.ControlTipText
giakfeiw = deulsaocthuul + gooykadheoj + roubhaol.paerwagyouqumeid.ControlTipText + deaknaugthein
queegthaen = giakfeiw + roubhaol.joefwoefcheaw
```

At the end of the code above `queegthaen` now contains the value `Win32_Process` + `s` + `tar` + `tu` + `P`. Or when combined creates the string `Win32_ProcessstartuP` which probably refers [to this WMI class](https://docs.microsoft.com/en-us/windows/win32/cimwin32prov/win32-processstartup) in the Microsoft docs.
