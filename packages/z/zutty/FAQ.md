[![Zutty icon](https://raw.githubusercontent.com/tomscii/zutty/master/icons/zutty_32x32.png)](https://raw.githubusercontent.com/tomscii/zutty/master/icons/zutty_128x128.png)

What you never thought you'd need to know about Zutty

### Q: What operating systems does Zutty run on?

**A**: Zutty is primarily developed and extensively tested on Linux,
and (to a lesser extent) on OpenBSD.

Zutty is portable: provided that necessary prerequisites are present,
it builds from source and runs without the need for any code fixes or
configuration changes on default installs of recent stable versions
of FreeBSD and OpenBSD.

Zutty will probably work on other UNIX-like systems as well; making
the necessary (small) adjustments is left as an exercise to interested
users. If you have a patch to make Zutty run somewhere not listed
above, I want to hear from you!

If you use Windows or MacOS, I'm afraid Zutty is not going to be
useful for you. I have no interest to work on making Zutty available
on closed source, proprietary operating systems.


### Q: I compiled Zutty successfully but the program cannot start, why is that?

I am getting an error like this:

    E [charvdev.cc:181] Error: Compiling fragment shader:
    0:1(10): error: GLSL ES 3.10 is not supported. Supported versions are: 1.00 ES, and 3.00 ES

**A**: Your graphics hardware or driver is not sufficient, you need
support for GLSL ES 3.1 or better.

The actual support level of the OpenGL (ES) implementation is only
detectable at runtime, i.e., having the right EGL and GLES libraries
to compile with (which is what the configure script is able to check)
does not guarantee that the OpenGL implementation supports the
required level at runtime. Note that compiling and running a dedicated
test program as part of the configure phase would not solve this: the
Zutty binary can be packaged, distributed and run on other machines
with different graphics hardware (or the hardware of the same machine
could be changed).

You could buy hardware that has sufficient support; the SBC on which I
primarily run Zutty set me back the equivalent of about $50.

Alternatively, see the next question.


### Q: Can I use Zutty without supported graphics hardware?

**A**: Yes. If you can tolerate higher resource usage (primarily CPU
usage), you could try the `llvmpipe` software renderer.  Note that you
need a sufficiently recent version that includes support for compute
shaders. Mesa 20.2.6 (present in Debian Bullseye) is ok. Please note
that using Zutty with such a setup is experimental and be prepared for
subpar performance.


### Q: Font XYZ does not load in Zutty or looks crappy, what should I do?

**A**: As a preliminary note: Zutty does work perfectly fine with a
wide range of fonts, both fixed and scalable, loadable from several
font file formats (see
[Screenshots](https://github.com/tomscii/zutty/wiki/Screenshots)). However,
fonts are a highly diverse bunch, so this does not mean that any
random font you found on the 'net will magically work! I personally
have all the fonts I could ever want, so if you insist on using a font
that does not work with Zutty out of the box, *it is on you to do the
extra work to make that happen*. Please keep this in mind.

Now to the specifics. If you get an error message like this:

    E [fontpack.cc:218] Error: No Regular variant of the requested font 'Cozette' could be identified.

In that case, Zutty is telling you that the [font file selection
process](https://tomscii.sig7.se/zutty/doc/USAGE.html#Font%20selection)
did not succeed in identifying a suitable font file. Please carefully
read and understand the
[documentation](https://tomscii.sig7.se/zutty/doc/USAGE.html#Making%20fonts%20discoverable)
on how you might make it work.

In case of certain filename endings (extensions) not recognized by
Zutty, you might have to add them to the filter in `src/fontpack.cc`
(search for `.pcf.gz` in `fontFileFilter`) and recompile. Then get
ready to debug all sorts of weird issues related to this new format.
You are on your own.

On the other hand, Zutty might have started up, having found suitably
named font files, but you feel that the font rendering is off, for
example all letters are "stuck to the ceiling" or overly wide, have
wide gaps in between, or rendered with some such distortion.  It is up
to you to debug why it does not work like all the fonts that do. You
have the source code of Zutty and all dependencies, so *please do not
expect me to do it for you!*

If you don't have the time to do that, don't know C++, don't know how
to debug, or have any other lame excuse, please do yourself a favour
and use some of the well documented font alternatives [known to
work](https://tomscii.sig7.se/zutty/doc/USAGE.html#Recommended%20fonts)
with Zutty.

*Do not submit bug reports* in the Zutty issue tracker unless you have
a well understood font loading or rendering issue due to an actual,
demonstrable bug in Zutty.  Tickets amounting to "Font XYZ does not
work" will be closed with a reference to this FAQ item.

### Q: What about Wayland?

**A**: Zutty has been written (in the year 2020) against plain Xlib.
Yeah, *I know*. That said, according to user reports, Zutty works fine
with XWayland, so just install `xorg-xwayland` (if you haven't
already) and you should be good to go!


### Q: Why would I try (or care about) Zutty? There are lots of terminal emulators, how is Zutty better than others?

**A**: Zutty is not necessarily better than any other program. I do
not have "world domination" on my TODO list, so you are free to ignore
Zutty and use another program.

That said, I believe Zutty has a number of interesting properties. It
is a terminal with accurate VT support, high performance, low latency,
a small codebase and is potentially compatible with a wide array of
contemporary graphics hardware. This combination is, as far as I am
aware, a unique proposition. You might be interested in my articles
that add substance to these claims,
[here](https://tomscii.sig7.se/2020/12/A-totally-biased-comparison-of-Zutty)
and
[here](https://tomscii.sig7.se/2021/01/Typing-latency-of-Zutty).


### Q: Why would I *not* want to use Zutty?

**A**: Lots of reasons! If you want any of these, Zutty is not for
you, and will probably remain so in the future:

- availability on MacOS or Windows
- transparent backgrounds
- scrollbar, menu bar, interactive configuration, etc.
- ligatures
- right-to-left text
- curvy underlines and similar fancy markup
- bitmap images (SIXEL, ReGIS, ...)
- overriding certain symbols / picking and mixing from different fonts

On the other hand, certain features are missing, but only due to the
very limited time I can spend working on Zutty. For details, see the
[README](https://tomscii.sig7.se/zutty/README.html#Omissions%20and%20limitations).


### Q: Can I subscribe to announcements of new versions? Is there a mailing list?

**A**: There is no mailing list, but you can keep track of changes to
Zutty by subscribing to one of the Atom feeds provided by GitHub.
Here's one for
[releases](https://github.com/tomscii/zutty/releases.atom) and
another for
[commits](https://github.com/tomscii/zutty/commits/master.atom),
depending on your level of interest.


### Q: I don't have a GitHub account, can I collaborate with you on Zutty?

**A**: You are free to send me bug reports, patches, or just general
correspondence via e-mail (but please see the next few questions to
set your expectations).  Please use my email address in the latest
published commit.  I am perfectly fine with this more traditional kind
of open-source collaboration, which used to be the standard before
GitHub (and similar sites) got popular.


### Q: Can I donate / sponsor / pay you to support the development of Zutty? Can I incentivize work on certain bugs or features?

**A**: No, you cannot do that. This is by intention, to preserve my
intellectual freedom and independence, and to ensure that Zutty
remains what it is: a hobby project. I want to be able to say no to
(or ignore) any request, from any person -- having accepted payments
from someone would possibly make this awkward.


### Q: As a user, how can I help you with Zutty?

**A**: First of all, thank you for your interest in Zutty. If you run
into issues, or have ideas on how to meaningfully improve Zutty, you
are welcome to *collaborate* (investing a share of your own time and
mental resources, as opposed to just demanding a slice of mine) to
understand and solve the problem, or discuss a possible improvement.
When asking for an enhancement or new feature, please motivate why you
think it's important (for you, at least) and please cite prior art
(what other terminals are out there already supporting it? what do the
relevant standards say? etc).

I appreciate well thought-out, well written, clear feedback on what
could be better, as well as high quality bug reports, and I try hard
to respond to all such correspondence. Pro tip: I am not a robot. It
helps a lot if you contact me in a friendly way, with some basic
courtesy and respect.


### Q: As a developer, how can I help you with Zutty?

**A**: First of all, thank you for your interest in improving Zutty.
To be honest, I am not overly interested in receiving unsolicited
patches or pull requests, unless you have a clear fix to an actual
(demonstrable) bug.  In general, if you have ideas for improvement,
try to convey them without coding them up -- try to put them into well
readable, concise English prose instead! If you found a bug, send me a
high quality report with all the necessary details (and your analysis,
if any) so I can easily reproduce and fix it. If you want to send a
patch with your proposed fix, that's fine, but absolutely not a
requirement!

If you do want to contribute code, make sure you have read the
[Contribution guide](https://tomscii.sig7.se/zutty/doc/HACKING.html#Contribution%20guide),
and please note that my standards for accepting code for inclusion are
*very* high. Your PR will be, in all likelihood, completely rewritten
or ignored.


### Q: How do I correctly pronounce Zutty? What does it mean?

**A**: The IPA notation is `[zuːc̟]`. I'm afraid you won't be able to
pronounce that, unless you happen to natively speak a
[language](https://en.wikipedia.org/wiki/Hungarian_phonology#Consonants)
featuring the
[voiceless palatal plosive](https://en.wikipedia.org/wiki/Voiceless_palatal_plosive).
If you decide to try, make sure to go for the alveolo-palatal variant.
Hint: Zutty does *not* rhyme with *kitty* (or how English-speaking
people commonly pronounce PuTTY).

The word *zutty* itself is an
[onomatopoetic](https://en.wikipedia.org/wiki/Onomatopoeia)
interjection in the Hungarian language, similar in its meaning to the
English *whoops* in referring to some sudden, quick action, but
lacking the element of (often negative) surprise. This fairly obscure
word is borrowed to stand for *zero-cost unicode teletype*.
