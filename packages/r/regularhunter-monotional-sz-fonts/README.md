![Typeface graphic](doc/monotional.png)

# Monotional

### Version 2.10

https://github.com/regularhunter/monotional-font

Monotional is a humanist, monospace font based on 
[DejaVu Sans Mono](https://github.com/dejavu-fonts/dejavu-fonts) and 
inspired by André Berg's [Meslo](https://github.com/andreberg/Meslo-Font). 
Its goal is to provide an easily legible font for programming and 
technical work. There are three variants of Monotional: Monotional (dotted 
zero), MonotionalSZ (slashed zero), and MonotionalAZ (ambiguous zero).

![Zero comparison](doc/monotional-zeroes.png)

*Figure 1: Comparison between versions*

This effort began while I was maintaining a 
[downstream fork of Meslo](https://github.com/regularhunter/Meslo-Font/) 
in order to fix some issues with it until I realized that it would be easier to 
start over from scratch with DejaVu Sans Mono (which is itself based on 
Bitstream Vera Sans Mono).

![Ipsum lorem](doc/monotional-ipsumlorem.png)

*Figure 2: Monotional lorem ipsum*

![Glyphs](doc/monotional-glyphs.png)

*Figure 3: Monotional glyph chart*

### Changelog

See the [latest release](https://github.com/regularhunter/monotional-font/releases) 
for more information.

**v2.10**

* Rescale ` % ` glyph to 104% of original size

**v2.9**

 * Revert scaling of ` % ` glyph

**v2.8**

 * Align ` % ` and ` ~ ` to integer coordinates
 * Scale ` % ` glyph to 104% of original size

**v2.7**

 * Rework ` % ` glyph for all fonts

**v2.6**

 * Correct thickness of regular and bold-italic ` figuredash `

**v2.5**

 * Rework all versions of ` 1 ` glyph

**v2.4**

 * Center italic and bold-italic glyph for ` | `
 * Add SZ (slashed zero) and AZ (ambiguous zero) variants

**v2.3**

 * Add unique italic and bold-italic glyph for ` | `

**v2.2**

 * Add unique italic and bold-italic glyph for ` ' ` and ` " `

**v2.1**

 * Fix incorrect positioning of regular ` ^ ` glyph

**v2.0**

 * Revise all dash glyphs for consistency
 * Add unique italic and bold-italic ` + ` glyph
 * Add unique italic and bold-italic ` = ` glyph
 * Increase height of bold and bold-italic glyph for ` ' ` and ` " `
 * Slight adjustment to bold and bold-italic ` ^ ` glyph
 * Slight adjustment to italic and bold-italic ` 4 ` glyph

**v1.9**

 * Rework bold, italic, and bold-italic ` 1 ` glyph to match regular version
 * Rework bold-italic ` # ` glyph to match bold version
 * Slight adjustment to italic ` ' ` and ` * ` glyph
 * Slight adjustment to bold and bold-italic ` - ` glyph
 * Slight adjustment to italic and bold-italic ` 4 ` glyph

**v1.8**

 * Increase regular and italic ` ~ ` glyph weight

**v1.7**

 * Change license to SIL OFL 1.1
 * Remove font instructions inherited from DejaVu Sans Mono causing 
rendering issues in Windows (issue #1)
 * Small adjustment to italic ` @ ` glyph
 * Rework italic and bold-italic ` # ` glyph to match non-italic 
versions
 * Change ` ~ ` glyph style to emulate Fira Code

**v1.6**

 * Remove fi and fl ligature
 * Fix swapped italic characters ` U+04CB/U+04CC ` <‒> ` U+04F6/U+04F7 `

**v1.5**

 * Small adjustment to ` 4 ` glyph

**v1.4**

 * Small adjustment to ` @ ` glyph

**v1.3**

 * Small adjustment to ` % ` glyph

**v1.2**

 * Re-implement Monotional on top of DejaVu Sans Mono from scratch to 
fix display bug in MS Word. ` ~ @ ` glyph not re-implemented
 * Revert \` glyph width from v1.1 so that legibility is preserved for accented 
characters

**v1.1**

 * Widen \` glyph for all fonts

**v1.0**

 * First release! Based on DejaVu Sans Mono 2.37.
 * The main differences are with the following characters: ` 1 i - _ = ' " ^ # * % @ ~ `

### Copyright and Trademark Information

**Monotional**

Copyright © 2025 Hunter Wardlaw

**Fira Code**

Copyright © 2014 The Fira Code Project Authors.

**Bitstream Vera Sans Mono / DejaVu Sans Mono**

Copyright © 2003 Bitstream Vera is a trademark of Bitstream, Inc., designed by Jim Lyles.
DejaVu changes are in public domain.

Copyright © 2006 Tavmjong Bah. All Rights Reserved.

All other brands and product names not specifically listed are trademarks or
registered trademarks of their respective owners.

### Thanks

To Jim Lyles and Bitstream for the Bitstream Vera family of fonts.

To André Berg for Meslo and inspiring some of the changes in Monotional.

To [bentodvictor](https://github.com/bentodvictor) for the Nerd Font 
patched versions of Monotional.

To George Williams for the free font editing program 
[FontForge](http://fontforge.org).

### License

Licensed under the SIL Open Font License Version 1.1

You may not use this file except in compliance with the License. 
You may obtain a copy of the License at:

https://openfontlicense.org/documents/OFL.txt
