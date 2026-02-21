Title: New Tool Preview: vATT&CK
Date: 2021-10-18 20:33
Slug: new-tool-preview-vattack
Tags: tools, cybersecurity
Category: Tools
Image: new-tool-preview-vattack-01.png
Summary: vATT&CK is a visual relationship mapper for MITRE ATT&CK that shows linked malware, threat groups, mitigations, and subtechniques in a single interactive graph.

I have released a new cybersecurity-related tool called [vATT&CK (Visual ATT&CK)](https://github.com/accidentalrebel/vATTACK). It is a relationship visualizer for the Mitre ATT&CK framework.

![new-tool-preview-vattack-01]({attach}/images/new-tool-preview-vattack-01.png)

What the tool does is that it makes a visual map of the searched technique and all the related information. You can watch a video of the tool in action [here](https://www.youtube.com/watch?v=xCc7aAqbSNI).

Each node will be colored depending on it's category. The color legends is as follows:

* Pink - Related subtechniques
* Orange - Malware that uses the searched technique
* Red - Groups that uses the searched technique
* Blue - Tools that use the searched technique
* Yellow - Mitigations

This tool is still in development. I plan to add a number of improvements such as:

* Ability to click on nodes and then update the visual map
* Ability to search not just by technique, but also by other categories

I also plan on releasing a live demo of the tool very soon in the hopes of getting feedback from the community. 

For now, if you are interested in the project, you could visit the [tool's Github project page](https://github.com/accidentalrebel/vATTACK) or contact me for any comments or suggestions.
