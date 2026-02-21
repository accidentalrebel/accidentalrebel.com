Title: The Emprisa Maldoc Challenge
Date: 2021-04-04 16:37
Slug: the-emprisa-maldoc-challenge
Tags: maldoc, ctf
Category: CTF
Image: the-emprisa-maldoc-challenge-01.png
Summary: How I turned a real-world malicious document exploit into the Emprisa Maldoc CTF on CyberDefenders — 14 questions targeting intermediate maldoc analysts.

I was inspired to make my own CTF challenge after finishing [Maldoc101]({filename}/maldoc101-writeup-part-1.md) found at [Cyberdefenders.org](https://cyberdefenders.org/). The challenge I made is called [Emprisa Maldoc](https://cyberdefenders.org/labs/56) and it is now up on their website. 

Emprisa is based on a malicious document that I downloaded blindly from a malware sandbox. It used a relatively old but still interesting exploit that is still in use today. After researching more about it I came across a tool that can generate a malicious doc using the same exact exploit. This is when I got the idea to turn it into a challenge.

![the-emprisa-maldoc-challenge-01]({attach}/images/the-emprisa-maldoc-challenge-01.png)

The challenge has 14 questions with increasing and varying difficulty. The challenge is targeted towards intermediate analysts who already have experience examining maldocs before. The goal is to reinforce the use of common malware analysis tools, but at the same time, teach players new things and techniques. It involves flexing muscles related to open source intelligence, examining shellcodes, and debugging processes. 

I don't want to spoil too much but if you are for it, you can give it a go [here](https://cyberdefenders.org/labs/51). It was hella fun to make and I do hope that it is also as fun to solve!

---

Official write-up: [Emprisa Maldoc Writeup]({filename}/emprisa-maldoc-writeup.md).

I would like to extend my thanks to the team behind CyberDefenders.org. They accepted my submission, reviewed it, and worked with me in improving it. And also to [Josh Stroschein](https://twitter.com/jstrosch) for making Maldoc101 and being kind enough to entertain me with my questions related to making challenges.
