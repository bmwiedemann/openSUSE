# xpra

URL: [xpra](https://github.com/Xpra-org/xpra)

----

NOTE(s):

* 20230905 - Spent a few hours creating a type of requirement matrix so 15.5 & 15.6 have what they need for Python3.11
* 20230903 - I can get it to build w/ Python3.11, but there are issues w/ python311-Pillow for Leap 15.5; namely, it doesn't build because of cascading list of other things that don't build (in devel:languages:python).
* 20230612 - Disabling build for 15.4/15.5 as it seems the default python3.6 can't build it; while python3.10/python3.11 are available, there's some type of tie-in for things like python3-Cython & python3-pyxdg that are python3.6 specific.

* 2022-07-19:
  * That was fixed in future commits ~ at least the expectation around 'pkgconfig(pam[_misc])' ; seems many non-rolling distros didn't play nice ...
* 2022-07-18:
  * It appears pam-devel isn't providing 'pkgconfig(pam)' / 'pkgconfig(pam_misc)' for [at least] 15.4 and currently "Linux-PAM/pam" doesn't build as it's requiring aclocal-1.16 (only aclocal-1.15 is available).

TW:

```shell
$ rpm -q --provides pam-devel
pam-devel = 1.5.2-7.1
pam-devel(x86-64) = 1.5.2-7.1
pkgconfig(pam) = 1.5.2
pkgconfig(pam_misc) = 1.5.2
pkgconfig(pamc) = 1.5.2
```

15.4:

```shell
$ rpm --provides -qp .cache/zypp/packages/repo-sle-update/x86_64/pam-devel-1.3.0-150000.6.58.3.x86_64.rpm
pam-devel = 1.3.0-150000.6.58.3
pam-devel(x86-64) = 1.3.0-150000.6.58.3
```

----

Xpra is known as "screen for X" : its seamless mode allows you to run X11 programs, usually on a remote host, direct their display to your local machine, and then to disconnect from these programs and reconnect from the same or another machine(s), without losing any state. Effectively giving you remote access to individual graphical applications.
It can also be used to access existing desktop sessions and start remote desktop sessions.

Xpra is open-source (GPLv2+) with clients available for many supported platforms and the server includes a built-in HTML5 client.
Xpra is usable over a wide variety of network protocols and does its best to adapt to any network conditions.

Xpra forwards and synchronizes many extra desktop features which allows remote applications to integrate transparently into the client's desktop environment: audio input and output, printers, clipboard, system trays, notifications, webcams, etc

It can also open documents and URLs remotely, display high bit depth content and it will try honour the display's DPI.
