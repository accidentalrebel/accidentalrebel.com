Title: Introducing shcode2exe
Date: 2021-02-26 07:34
Slug: introducing-shcode2exe
Tags: re, tools, malware_analysis
Category: tools

I've been playing around with [Remnux](https://remnux.org/) and encountered a problem trying to get one of the tools to run properly. The tool is [shellcode2exe](https://github.com/repnz/shellcode2exe), it is used to compile binary shellcode to a file so it can easily be debugged by a debugger.

When I checked out the code, I was surprised to find out how simple it is. Basically, what happens is that the inputted shellcode is added to a barebones assembly file using the `incbin` assembly instruction. From there, the file is then automatically compiled and linked.

One big problem with the tool is that it needs to use [Wine](https://www.winehq.org/) if it needs to run on Linux. I don't want such a huge dependency especially for my own malware analysis lab so I decided to write my own version which have led to the creation of `shcode2exe`.

## shcode2exe

While similar in functionality with the original tool, the biggest improvement I made is that it it does not depend on Wine along with other features as listed below:

  * Can accept a shellcode blob or string (String format `\x5e\x31`)
  * Can target both 32bit or 64bit Windows architecture. 
  * Cross platform. Works on Linux or Windows.
  * No dependency on Wine when running on Linux
  * Tested working with Python v3.3 and above
  * Tested working on Windows 7 (Non SP1) and above
  
## Usage

Here's the help message for the tool:

```console
usage: shcode2exe.py [-h] [-o OUTPUT] [-s] [-a {32,64}] input

Compile a binary shellcode blob into an exe file. Can target both 32bit or 64bit architecture.

positional arguments:
  input                 The input file containing the shellcode.

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Set output exe file.
  -s, --string          Set if input file contains shellcode in string format.
  -a {32,64}, --architecture {32,64}
                        The windows architecture to use
```

Here's how to load a file with shellcode in the format of a string

```console
$ cat test.txt
\x5e\x31\xc0\xb0\x24\xcd\x80\xb0\x24\xcd\x80\xb0\x58\xbb\xad\xde\xe1\xfe\xb9\x69\x19\x12\x28\xba\x67\x45\x23\x01\xcd\x80
$ ./shcode2exe.py -s -o test-string.exe test.bin
```

Load a file with shellcode in the format of a blob

```console
$ ./shcode2exe.py -o test-blob.exe test.bin
```

Use 64 bit architecture for the output (32 bit is the default)

```console
$ ./shcode2exe.py -o test-blob.exe -a 64 test.bin
$ file test-blob.exe
test-blob.exe: PE32+ executable (console) x86-64 (stripped to external PDB), for MS Windows
```

## Next steps

I decided to reach out to the people behind Remnux to ask if they could consider my tool as a replacement on their platform. It would be great if they would, but it's okay too if they don't, I made it for my own use anyway. (Update 2021-02-07: It's now [under review](https://github.com/REMnux/salt-states/issues/169))

For more information about the tool and it's code, go to [it's Github page](https://github.com/accidentalrebel/shcode2exe). If you have any comments or suggestions on how to improve it, feel free to tell me via Github issues or dm me at [@accidentalrebel](https://twitter.com/accidentalrebel).


