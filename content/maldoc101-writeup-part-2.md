Title: Maldoc101 Writeup (Part 2)
Date: 2021-03-14 08:34
Slug: maldoc101-writeup-part-2
Tags: re, malware_analysis, malware
Category: Malware Analysis

This is part 2 of my writeup for the Maldoc101 challenge. Check out [part 1]({filename}/maldoc101-writeup-part-1.md) for the beginning of the analysis.

The next couple of lines does the same concatenating technique similar to the previous steps. 

```vba
deaknaugthein = roubhaol.kaizseah.ControlTipText
giakfeiw = deulsaocthuul + gooykadheoj + roubhaol.paerwagyouqumeid.ControlTipText + deaknaugthein
queegthaen = giakfeiw + roubhaol.joefwoefcheaw
```

At the end of the code above `queegthaen` now contains the value `Win32_Process` + `s` + `tar` + `tu` + `P`. Or when combined creates the string `Win32_ProcessstartuP` which probably refers [to this WMI class](https://docs.microsoft.com/en-us/windows/win32/cimwin32prov/win32-processstartup) in the Microsoft docs.

*Note: This writeup appears to be incomplete. For the complete analysis, please refer to [part 1]({filename}/maldoc101-writeup-part-1.md) of this series.*
