Title: Making a RAT
Date: 2021-07-13 14:56
Slug: making-a-rat
Tags: malware, dev
Category: malware

A Remote Access Tool (RAT) is used to remotely access a computer. It has legitimate uses but it can also be used for malicious purposes. I've seen it used in malware I've analyzed and I've always been curious as to how it works.

I was following along the [Handmade Hero project](https://handmadehero.org/) [^1] when the topic about dynamic DLL loading came up. This is a process of dynamically loading a DLL at runtime which is useful if you want your program to check if a DLL is present in a system before loading it.

Two of the system calls that were discussed were LoadLibrary and GetProcAddress. These were familiar to me as I've seen them used on malware shellcode I analyzed in the past. I later learned that this is also used as an anti-virus evasion technique. I found this interesting.

Having learned how to do runtime DLL loading myself I decided to give it a try. And of course, a RAT is perfect for this.

![making-a-rat-01]({attach}/images/making-a-rat-01.png)

## Planning the RATchitecture

A lot of famous RATs are packed with features like the ability to log keystrokes, take screenshots, and turn on a webcam. I just want mine to be simple and have basic functionality like:

  * Execute command line commands remotely
  * Download a file to the client
  * Exfiltrate data via file upload
  * Work on one platform (Windows)

As an extra, I also wanted it to be stealthy and also be able to evade detection, hence the runtime DLL loading.

I found some great resources online that helped me a lot in working on my RAT:

  * [ParadoxiaRat](https://github.com/quantumcore/paradoxiaRAT) is my main resource and has done a lot of the features I wanted to implement.
  * [DarkRAT](https://github.com/yatt-ze/The-Collection/tree/master/Source%20Codes/Botnets/DarkRat%20Loader/derkrut) is a leaked source code that gave me an idea of how a RAT used in the wild looks like
  * [VXUnderground's WinAPI tricks](https://github.com/vxunderground/WinAPI-Tricks) taught me that there are alternative ways to do certain things to avoid detection

I decided to name the project RATwurst after the german sausage. Don't ask me how I made that connection, I just wanted it to have the word RAT in it.

## For eduRATional purposes only

I've made the source of my project [available on Github](https://github.com/accidentalrebel/ratwurst). The aim is to share what I've learned so that others can learn too.

I am aware of news of RAT authors having been arrested because of their work. They actively sought to gain money from their creation, I, of course, have no such plans.

To make sure that I save myself from any legal problems, I've placed a disclaimer that I am not responsible for any misuse. While I am skeptical that a piece of text would prevent any legal action towards me, I do see other projects having their own disclaimers so I decided to do the same.

I've also submitted my creation to a multi-scanner service like VirusTotal. This would help distribute my RATs signature to anti-virus companies so it can easily be detected when used in the wild.[^2]

## A RATisfying learning experience

Making this project has been a lot of fun. 

The most useful thing that I learned is the client and server communication via sockets. I've dabbled with it before but only in this project have I actually sent actual data back and forth.

I am also happy that I got to use more Windows APIs. It's fun to play around with what's available and it is opening my mind as to what other things I can make in the future.

And of course, this project has given me a good insight into the techniques used by malware. Learning about them is not enough until you've built one yourself.

[^1]: Handmade here is a project by Casey Muratori where a game is created from scratch live on stream, has been going on for 6+ years, it's awesome

[^2]: Multi-scanners help to easily distribute virus signatures to security services. An opposite to this are "no-distribute" sacnners. More info about this [here](https://www.bleepingcomputer.com/news/security/75-percent-of-malware-uploaded-on-no-distribute-scanners-is-unknown-to-researchers/).
