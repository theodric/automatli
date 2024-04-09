# automatli

Swiss noun trollage generator
Based on jarfbot - Jarf Beezers name generator

Format is:

IC - Initial consonant (optional) [uppercase]

IP - Initial phoneme [if IC==null uppercase; else lowercase ]

SP - Secondary phoneme [lowercase]

TP - Tertiary phoneme (optional) [lowercase]

FD - Diminuitive [lowercase]

EXAMPLES:

```IC==G
IP == sch
SP == üü
TP == pf
FD == li

output:
Gschüüpfli
```

## Usage
* Clone repo
* pip3 install -r requirements.txt
* edit automatli.py and add your Twitter API details
* run

Optionally, you can run it as a service on Debian by creating /lib/systemd/system/automatli.service and symlinking it to /etc/systemd/system/multi-user.target.wants/automatli.service.

A service template is included in this distribution.
