#
# spec file for package texlive-specs-u
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%bcond_with	zypper_posttrans

%define texlive_version  2019
%define texlive_previous 2018
%define texlive_release  20190407
%define texlive_noarch   168

#!BuildIgnore:          texlive

%global _varlib         %{_localstatedir}/lib
%global _libexecdir     %{_prefix}/lib

%define _texmfdistdir   %{_datadir}/texmf
%if 0%{texlive_version} >= 2013
%define _texmfmaindir   %{_texmfdistdir}
%define _texmfdirs      %{_texmfdistdir}
%else
%define _texmfmaindir   %{_libexecdir}/texmf
%define _texmfdirs      \{%{_texmfdistdir},%{_texmfmaindir}\}
%endif

%define _texmfconfdir   %{_sysconfdir}/texmf
%define _texmfvardir    %{_varlib}/texmf
%define _texmfcache     %{_localstatedir}/cache/texmf
%define _fontcache      %{_texmfcache}/fonts
#
%define _x11bin         %{_prefix}/bin
%define _x11lib         %{_libdir}
%define _x11data        %{_datadir}/X11
%define _x11inc         %{_includedir}
%define _appdefdir      %{_x11data}/app-defaults

Name:           texlive-specs-u
Version:        2019
Release:        0
BuildRequires:  ed
BuildRequires:  fontconfig
BuildRequires:  fontpackages-devel
BuildRequires:  t1utils
BuildRequires:  texlive-filesystem
BuildRequires:  xz
BuildArch:      noarch
Summary:        Meta package for u
License:        Apache-1.0 and BSD-3-Clause and GPL-2.0+ and LPPL-1.0 and OFL-1.1 and SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
Url:            https://build.opensuse.org/package/show/Publishing:TeXLive/Meta
Source0:        texlive-specs-u-rpmlintrc

%description
Meta package to build tons of noarch texlive packages.

%package -n texlive-robustindex
Version:        %{texlive_version}.%{texlive_noarch}.svn49877
Release:        0
Summary:        Create index with pagerefs
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-robustindex-doc >= %{texlive_version}
Provides:       tex(robustglossary.sty)
Provides:       tex(robustindex.sty)
Requires:       tex(makeidx.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source1:        robustindex.tar.xz
Source2:        robustindex.doc.tar.xz

%description -n texlive-robustindex
Third parties often change the page numbers without rerunning
makeindex. One would like to make the page numbers in the index
entries more robust. This bundle provides robustindex.sty and
robustglossary.sty, which use the \pageref mechanism to
maintain correct page numbers.

date: 2019-01-30 12:41:54 +0000


%package -n texlive-robustindex-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn49877
Release:        0
Summary:        Documentation for texlive-robustindex
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-robustindex-doc
This package includes the documentation for texlive-robustindex

%post -n texlive-robustindex
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-robustindex 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-robustindex
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-robustindex-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/robustindex/README.md
%{_texmfdistdir}/doc/latex/robustindex/multisample.pdf
%{_texmfdistdir}/doc/latex/robustindex/multisample.tex
%{_texmfdistdir}/doc/latex/robustindex/robustmanual.pdf
%{_texmfdistdir}/doc/latex/robustindex/robustmanual.tex
%{_texmfdistdir}/doc/latex/robustindex/robustsample.pdf
%{_texmfdistdir}/doc/latex/robustindex/robustsample.tex
%{_texmfdistdir}/doc/latex/robustindex/stind.html

%files -n texlive-robustindex
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/robustindex/robustglossary.sty
%{_texmfdistdir}/tex/latex/robustindex/robustindex.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-robustindex-%{texlive_version}.%{texlive_noarch}.svn49877-%{release}-zypper
%endif

%package -n texlive-roex
Version:        %{texlive_version}.%{texlive_noarch}.svn45818
Release:        0
Summary:        Metafont-PostScript conversions
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source3:        roex.tar.xz

%description -n texlive-roex
A Metafont support package including: epstomf, a tiny AWK
script for converting EPS files into Metafont; mftoeps for
generating (encapsulated) PostScript files readable, e.g., by
CorelDRAW, Adobe Illustrator and Fontographer; a collection of
routines (in folder progs) for converting Metafont-coded
graphics into encapsulated PostScript; and roex.mf, which
provides Metafont macros for removing overlaps and expanding
strokes. In mftoeps, Metafont writes PostScript code to a
log-file, from which it may be extracted by either TeX or AWK.

date: 2016-07-17 12:25:42 +0000

%post -n texlive-roex
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-roex 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-roex
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-roex
%defattr(-,root,root,755)
%{_texmfdistdir}/metafont/roex/roex.mf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-roex-%{texlive_version}.%{texlive_noarch}.svn45818-%{release}-zypper
%endif

%package -n texlive-romanbar
Version:        %{texlive_version}.%{texlive_noarch}.1.0fsvn25005
Release:        0
Summary:        Write roman number with "bars"
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-romanbar-doc >= %{texlive_version}
Provides:       tex(romanbar.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source4:        romanbar.tar.xz
Source5:        romanbar.doc.tar.xz

%description -n texlive-romanbar
'Bars', in the present context, are lines above and below text
that abut with the text. Barred roman numerals are sometimes
found in publications. The package provides a function that
prints barred roman numerals (converting arabic numerals if
necessary). The package also provides a predicate \ifnumeric.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-romanbar-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0fsvn25005
Release:        0
Summary:        Documentation for texlive-romanbar
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-romanbar-doc
This package includes the documentation for texlive-romanbar

%post -n texlive-romanbar
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-romanbar 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-romanbar
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-romanbar-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/romanbar/README
%{_texmfdistdir}/doc/latex/romanbar/romanbar-example.pdf
%{_texmfdistdir}/doc/latex/romanbar/romanbar-example.tex
%{_texmfdistdir}/doc/latex/romanbar/romanbar.pdf

%files -n texlive-romanbar
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/romanbar/romanbar.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-romanbar-%{texlive_version}.%{texlive_noarch}.1.0fsvn25005-%{release}-zypper
%endif

%package -n texlive-romanbarpagenumber
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn36236
Release:        0
Summary:        Typesetting roman page numbers
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-romanbarpagenumber-doc >= %{texlive_version}
Provides:       tex(romanbarpagenumber.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(romanbar.sty)
Requires:       tex(xifthen.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source6:        romanbarpagenumber.tar.xz
Source7:        romanbarpagenumber.doc.tar.xz

%description -n texlive-romanbarpagenumber
The package romanbar allows to typeset roman numbers with bars.
This package allows you to use those roman numbers as page
number.

date: 2017-04-18 03:31:40 +0000


%package -n texlive-romanbarpagenumber-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn36236
Release:        0
Summary:        Documentation for texlive-romanbarpagenumber
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-romanbarpagenumber-doc
This package includes the documentation for texlive-romanbarpagenumber

%post -n texlive-romanbarpagenumber
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-romanbarpagenumber 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-romanbarpagenumber
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-romanbarpagenumber-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/romanbarpagenumber/README
%{_texmfdistdir}/doc/latex/romanbarpagenumber/romanbarpagenumber.pdf

%files -n texlive-romanbarpagenumber
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/romanbarpagenumber/romanbarpagenumber.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-romanbarpagenumber-%{texlive_version}.%{texlive_noarch}.1.0svn36236-%{release}-zypper
%endif

%package -n texlive-romande
Version:        %{texlive_version}.%{texlive_noarch}.1.008_v7_scsvn19537
Release:        0
Summary:        Romande ADF fonts and LaTeX support
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(updmap.cfg)
#!BuildIgnore:  tex(updmap.cfg)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(updmap.cfg)
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires:       texlive-romande-fonts >= %{texlive_version}
Recommends:     texlive-romande-doc >= %{texlive_version}
Provides:       tex(romande-supp.enc)
Provides:       tex(romande.sty)
Provides:       tex(s-yrdd.tfm)
Provides:       tex(s-yrddi.tfm)
Provides:       tex(s-yrdr.tfm)
Provides:       tex(s-yrdri.tfm)
Provides:       tex(s-yrdriw.tfm)
Provides:       tex(t1-romandeadf-alt-yrdd.tfm)
Provides:       tex(t1-romandeadf-alt-yrddi.tfm)
Provides:       tex(t1-romandeadf-alt-yrdr.tfm)
Provides:       tex(t1-romandeadf-alt-yrdri.tfm)
Provides:       tex(t1-romandeadf-alt-yrdriw.tfm)
Provides:       tex(t1-romandeadf-alt.enc)
Provides:       tex(t1-romandeadf-yrdd.tfm)
Provides:       tex(t1-romandeadf-yrddc.tfm)
Provides:       tex(t1-romandeadf-yrddi.tfm)
Provides:       tex(t1-romandeadf-yrdr.tfm)
Provides:       tex(t1-romandeadf-yrdrc.tfm)
Provides:       tex(t1-romandeadf-yrdri.tfm)
Provides:       tex(t1-romandeadf-yrdriw.tfm)
Provides:       tex(t1-romandeadf.enc)
Provides:       tex(t1yrd.fd)
Provides:       tex(t1yrda.fd)
Provides:       tex(t1yrdaw.fd)
Provides:       tex(t1yrdw.fd)
Provides:       tex(ts1-euro-yrd.enc)
Provides:       tex(ts1-yrdd.tfm)
Provides:       tex(ts1-yrddi.tfm)
Provides:       tex(ts1-yrdr.tfm)
Provides:       tex(ts1-yrdri.tfm)
Provides:       tex(ts1-yrdriw.tfm)
Provides:       tex(ts1yrd.fd)
Provides:       tex(ts1yrda.fd)
Provides:       tex(ts1yrdaw.fd)
Provides:       tex(ts1yrdw.fd)
Provides:       tex(yrd.map)
Provides:       tex(yrdd8c.tfm)
Provides:       tex(yrdd8c.vf)
Provides:       tex(yrdd8t.tfm)
Provides:       tex(yrdd8t.vf)
Provides:       tex(yrdda8t.tfm)
Provides:       tex(yrdda8t.vf)
Provides:       tex(yrddai8t.tfm)
Provides:       tex(yrddai8t.vf)
Provides:       tex(yrddc8t.tfm)
Provides:       tex(yrddc8t.vf)
Provides:       tex(yrddi8c.tfm)
Provides:       tex(yrddi8c.vf)
Provides:       tex(yrddi8t.tfm)
Provides:       tex(yrddi8t.vf)
Provides:       tex(yrdr8c.tfm)
Provides:       tex(yrdr8c.vf)
Provides:       tex(yrdr8t.tfm)
Provides:       tex(yrdr8t.vf)
Provides:       tex(yrdra8t.tfm)
Provides:       tex(yrdra8t.vf)
Provides:       tex(yrdrai8t.tfm)
Provides:       tex(yrdrai8t.vf)
Provides:       tex(yrdraiw8t.tfm)
Provides:       tex(yrdraiw8t.vf)
Provides:       tex(yrdrc8t.tfm)
Provides:       tex(yrdrc8t.vf)
Provides:       tex(yrdri8c.tfm)
Provides:       tex(yrdri8c.vf)
Provides:       tex(yrdri8t.tfm)
Provides:       tex(yrdri8t.vf)
Provides:       tex(yrdriw8c.tfm)
Provides:       tex(yrdriw8c.vf)
Provides:       tex(yrdriw8t.tfm)
Provides:       tex(yrdriw8t.vf)
Requires:       tex(fontenc.sty)
Requires:       tex(nfssext-cfr.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source8:        romande.tar.xz
Source9:        romande.doc.tar.xz

%description -n texlive-romande
Romande ADF is a serif font family with oldstyle figures,
designed as a substitute for Times, Tiffany or Caslon. The
family currently includes upright, italic and small-caps shapes
in each of regular and demi-bold weights and an italic script
in regular. The support package renames the fonts according to
the Karl Berry fontname scheme and defines four families. Two
of these primarily provide access to the "standard" or default
characters while the "alternate" families support alternate
characters, additional ligatures and the long s. The included
package files provide access to these features in LaTeX as
explained in the documentation. The LaTeX support requires the
nfssext-cfr and the xkeyval packages.

date: 2017-04-18 03:31:40 +0000


%package -n texlive-romande-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.008_v7_scsvn19537
Release:        0
Summary:        Documentation for texlive-romande
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-romande-doc
This package includes the documentation for texlive-romande


%package -n texlive-romande-fonts
Version:        %{texlive_version}.%{texlive_noarch}.1.008_v7_scsvn19537
Release:        0
Summary:        Severed fonts for texlive-romande
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Fonts
Url:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-romande-fonts
The  separated fonts package for texlive-romande
%post -n texlive-romande
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap yrd.map' >> /var/run/texlive/run-updmap

%postun -n texlive-romande 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap yrd.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-romande
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-romande-fonts
%files -n texlive-romande-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/romande/COPYING
%{_texmfdistdir}/doc/fonts/romande/NOTICE.txt
%{_texmfdistdir}/doc/fonts/romande/README
%{_texmfdistdir}/doc/fonts/romande/manifest.txt
%{_texmfdistdir}/doc/fonts/romande/romandeadf.pdf
%{_texmfdistdir}/doc/fonts/romande/romandeadf.tex

%files -n texlive-romande
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/afm/arkandis/romande/yrdd8a.afm
%{_texmfdistdir}/fonts/afm/arkandis/romande/yrddc8a.afm
%{_texmfdistdir}/fonts/afm/arkandis/romande/yrddi8a.afm
%{_texmfdistdir}/fonts/afm/arkandis/romande/yrdr8a.afm
%{_texmfdistdir}/fonts/afm/arkandis/romande/yrdrc8a.afm
%{_texmfdistdir}/fonts/afm/arkandis/romande/yrdri8a.afm
%{_texmfdistdir}/fonts/afm/arkandis/romande/yrdriw8a.afm
%{_texmfdistdir}/fonts/enc/dvips/romande/romande-supp.enc
%{_texmfdistdir}/fonts/enc/dvips/romande/t1-romandeadf-alt.enc
%{_texmfdistdir}/fonts/enc/dvips/romande/t1-romandeadf.enc
%{_texmfdistdir}/fonts/enc/dvips/romande/ts1-euro-yrd.enc
%{_texmfdistdir}/fonts/map/dvips/romande/yrd.map
%{_texmfdistdir}/fonts/tfm/arkandis/romande/s-yrdd.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/romande/s-yrddi.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/romande/s-yrdr.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/romande/s-yrdri.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/romande/s-yrdriw.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/romande/t1-romandeadf-alt-yrdd.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/romande/t1-romandeadf-alt-yrddi.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/romande/t1-romandeadf-alt-yrdr.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/romande/t1-romandeadf-alt-yrdri.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/romande/t1-romandeadf-alt-yrdriw.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/romande/t1-romandeadf-yrdd.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/romande/t1-romandeadf-yrddc.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/romande/t1-romandeadf-yrddi.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/romande/t1-romandeadf-yrdr.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/romande/t1-romandeadf-yrdrc.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/romande/t1-romandeadf-yrdri.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/romande/t1-romandeadf-yrdriw.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/romande/ts1-yrdd.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/romande/ts1-yrddi.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/romande/ts1-yrdr.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/romande/ts1-yrdri.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/romande/ts1-yrdriw.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/romande/yrdd8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/romande/yrdd8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/romande/yrdda8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/romande/yrddai8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/romande/yrddc8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/romande/yrddi8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/romande/yrddi8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/romande/yrdr8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/romande/yrdr8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/romande/yrdra8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/romande/yrdrai8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/romande/yrdraiw8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/romande/yrdrc8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/romande/yrdri8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/romande/yrdri8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/romande/yrdriw8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/romande/yrdriw8t.tfm
%verify(link) %{_texmfdistdir}/fonts/type1/arkandis/romande/yrdd8a.pfb
%{_texmfdistdir}/fonts/type1/arkandis/romande/yrdd8a.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/arkandis/romande/yrddc8a.pfb
%{_texmfdistdir}/fonts/type1/arkandis/romande/yrddc8a.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/arkandis/romande/yrddi8a.pfb
%{_texmfdistdir}/fonts/type1/arkandis/romande/yrddi8a.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/arkandis/romande/yrdr8a.pfb
%{_texmfdistdir}/fonts/type1/arkandis/romande/yrdr8a.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/arkandis/romande/yrdrc8a.pfb
%{_texmfdistdir}/fonts/type1/arkandis/romande/yrdrc8a.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/arkandis/romande/yrdri8a.pfb
%{_texmfdistdir}/fonts/type1/arkandis/romande/yrdri8a.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/arkandis/romande/yrdriw8a.pfb
%{_texmfdistdir}/fonts/type1/arkandis/romande/yrdriw8a.pfm
%{_texmfdistdir}/fonts/vf/arkandis/romande/yrdd8c.vf
%{_texmfdistdir}/fonts/vf/arkandis/romande/yrdd8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/romande/yrdda8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/romande/yrddai8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/romande/yrddc8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/romande/yrddi8c.vf
%{_texmfdistdir}/fonts/vf/arkandis/romande/yrddi8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/romande/yrdr8c.vf
%{_texmfdistdir}/fonts/vf/arkandis/romande/yrdr8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/romande/yrdra8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/romande/yrdrai8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/romande/yrdraiw8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/romande/yrdrc8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/romande/yrdri8c.vf
%{_texmfdistdir}/fonts/vf/arkandis/romande/yrdri8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/romande/yrdriw8c.vf
%{_texmfdistdir}/fonts/vf/arkandis/romande/yrdriw8t.vf
%{_texmfdistdir}/tex/latex/romande/romande.sty
%{_texmfdistdir}/tex/latex/romande/t1yrd.fd
%{_texmfdistdir}/tex/latex/romande/t1yrda.fd
%{_texmfdistdir}/tex/latex/romande/t1yrdaw.fd
%{_texmfdistdir}/tex/latex/romande/t1yrdw.fd
%{_texmfdistdir}/tex/latex/romande/ts1yrd.fd
%{_texmfdistdir}/tex/latex/romande/ts1yrda.fd
%{_texmfdistdir}/tex/latex/romande/ts1yrdaw.fd
%{_texmfdistdir}/tex/latex/romande/ts1yrdw.fd

%files -n texlive-romande-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-romande
%config %{_sysconfdir}/fonts/conf.avail/58-texlive-romande.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-romande/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-romande/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-romande/fonts.scale
%{_datadir}/fonts/texlive-romande/yrdd8a.pfb
%{_datadir}/fonts/texlive-romande/yrddc8a.pfb
%{_datadir}/fonts/texlive-romande/yrddi8a.pfb
%{_datadir}/fonts/texlive-romande/yrdr8a.pfb
%{_datadir}/fonts/texlive-romande/yrdrc8a.pfb
%{_datadir}/fonts/texlive-romande/yrdri8a.pfb
%{_datadir}/fonts/texlive-romande/yrdriw8a.pfb
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-romande-fonts-%{texlive_version}.%{texlive_noarch}.1.008_v7_scsvn19537-%{release}-zypper
%endif

%package -n texlive-romanneg
Version:        %{texlive_version}.%{texlive_noarch}.svn20087
Release:        0
Summary:        Roman page numbers negative
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-romanneg-doc >= %{texlive_version}
Provides:       tex(romanneg.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source10:       romanneg.tar.xz
Source11:       romanneg.doc.tar.xz

%description -n texlive-romanneg
Causes the page numbers in the DVI file (as defined by \count0)
to be negative when roman pagenumbering is in effect.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-romanneg-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn20087
Release:        0
Summary:        Documentation for texlive-romanneg
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-romanneg-doc
This package includes the documentation for texlive-romanneg

%post -n texlive-romanneg
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-romanneg 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-romanneg
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-romanneg-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/romanneg/romanneg.ltx
%{_texmfdistdir}/doc/latex/romanneg/romanneg.pdf

%files -n texlive-romanneg
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/romanneg/romanneg.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-romanneg-%{texlive_version}.%{texlive_noarch}.svn20087-%{release}-zypper
%endif

%package -n texlive-romannum
Version:        %{texlive_version}.%{texlive_noarch}.1.0bsvn15878
Release:        0
Summary:        Generate roman numerals instead of arabic digits
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-romannum-doc >= %{texlive_version}
Provides:       tex(romannum.sty)
Requires:       tex(stdclsdv.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source12:       romannum.tar.xz
Source13:       romannum.doc.tar.xz

%description -n texlive-romannum
The romannum package changes LaTeX generated numbers to be
printed with roman numerals instead of arabic digits. It
requires the stdclsdv package. Users of the bookhands fonts may
find this package useful.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-romannum-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0bsvn15878
Release:        0
Summary:        Documentation for texlive-romannum
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-romannum-doc
This package includes the documentation for texlive-romannum

%post -n texlive-romannum
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-romannum 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-romannum
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-romannum-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/romannum/README
%{_texmfdistdir}/doc/latex/romannum/romannum.pdf

%files -n texlive-romannum
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/romannum/romannum.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-romannum-%{texlive_version}.%{texlive_noarch}.1.0bsvn15878-%{release}-zypper
%endif

%package -n texlive-rosario
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn40843
Release:        0
Summary:        Using the free Rosario fonts with LaTeX
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(updmap.cfg)
#!BuildIgnore:  tex(updmap.cfg)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(updmap.cfg)
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires:       texlive-rosario-fonts >= %{texlive_version}
Recommends:     texlive-rosario-doc >= %{texlive_version}
Provides:       tex(LY1Rosario-LF.fd)
Provides:       tex(OT1Rosario-LF.fd)
Provides:       tex(Rosario-Bold-lf-ly1--base.tfm)
Provides:       tex(Rosario-Bold-lf-ly1--lcdfj.tfm)
Provides:       tex(Rosario-Bold-lf-ly1.tfm)
Provides:       tex(Rosario-Bold-lf-ly1.vf)
Provides:       tex(Rosario-Bold-lf-ot1--base.tfm)
Provides:       tex(Rosario-Bold-lf-ot1--lcdfj.tfm)
Provides:       tex(Rosario-Bold-lf-ot1.tfm)
Provides:       tex(Rosario-Bold-lf-ot1.vf)
Provides:       tex(Rosario-Bold-lf-t1--base.tfm)
Provides:       tex(Rosario-Bold-lf-t1--lcdfj.tfm)
Provides:       tex(Rosario-Bold-lf-t1.tfm)
Provides:       tex(Rosario-Bold-lf-t1.vf)
Provides:       tex(Rosario-Bold-lf-ts1--base.tfm)
Provides:       tex(Rosario-Bold-lf-ts1.tfm)
Provides:       tex(Rosario-Bold-lf-ts1.vf)
Provides:       tex(Rosario-BoldItalic-lf-ly1--base.tfm)
Provides:       tex(Rosario-BoldItalic-lf-ly1--lcdfj.tfm)
Provides:       tex(Rosario-BoldItalic-lf-ly1.tfm)
Provides:       tex(Rosario-BoldItalic-lf-ly1.vf)
Provides:       tex(Rosario-BoldItalic-lf-ot1--base.tfm)
Provides:       tex(Rosario-BoldItalic-lf-ot1--lcdfj.tfm)
Provides:       tex(Rosario-BoldItalic-lf-ot1.tfm)
Provides:       tex(Rosario-BoldItalic-lf-ot1.vf)
Provides:       tex(Rosario-BoldItalic-lf-t1--base.tfm)
Provides:       tex(Rosario-BoldItalic-lf-t1--lcdfj.tfm)
Provides:       tex(Rosario-BoldItalic-lf-t1.tfm)
Provides:       tex(Rosario-BoldItalic-lf-t1.vf)
Provides:       tex(Rosario-BoldItalic-lf-ts1--base.tfm)
Provides:       tex(Rosario-BoldItalic-lf-ts1.tfm)
Provides:       tex(Rosario-BoldItalic-lf-ts1.vf)
Provides:       tex(Rosario-Italic-lf-ly1--base.tfm)
Provides:       tex(Rosario-Italic-lf-ly1--lcdfj.tfm)
Provides:       tex(Rosario-Italic-lf-ly1.tfm)
Provides:       tex(Rosario-Italic-lf-ly1.vf)
Provides:       tex(Rosario-Italic-lf-ot1--base.tfm)
Provides:       tex(Rosario-Italic-lf-ot1--lcdfj.tfm)
Provides:       tex(Rosario-Italic-lf-ot1.tfm)
Provides:       tex(Rosario-Italic-lf-ot1.vf)
Provides:       tex(Rosario-Italic-lf-t1--base.tfm)
Provides:       tex(Rosario-Italic-lf-t1--lcdfj.tfm)
Provides:       tex(Rosario-Italic-lf-t1.tfm)
Provides:       tex(Rosario-Italic-lf-t1.vf)
Provides:       tex(Rosario-Italic-lf-ts1--base.tfm)
Provides:       tex(Rosario-Italic-lf-ts1.tfm)
Provides:       tex(Rosario-Italic-lf-ts1.vf)
Provides:       tex(Rosario-Regular-lf-ly1--base.tfm)
Provides:       tex(Rosario-Regular-lf-ly1--lcdfj.tfm)
Provides:       tex(Rosario-Regular-lf-ly1.tfm)
Provides:       tex(Rosario-Regular-lf-ly1.vf)
Provides:       tex(Rosario-Regular-lf-ot1--base.tfm)
Provides:       tex(Rosario-Regular-lf-ot1--lcdfj.tfm)
Provides:       tex(Rosario-Regular-lf-ot1.tfm)
Provides:       tex(Rosario-Regular-lf-ot1.vf)
Provides:       tex(Rosario-Regular-lf-t1--base.tfm)
Provides:       tex(Rosario-Regular-lf-t1--lcdfj.tfm)
Provides:       tex(Rosario-Regular-lf-t1.tfm)
Provides:       tex(Rosario-Regular-lf-t1.vf)
Provides:       tex(Rosario-Regular-lf-ts1--base.tfm)
Provides:       tex(Rosario-Regular-lf-ts1.tfm)
Provides:       tex(Rosario-Regular-lf-ts1.vf)
Provides:       tex(Rosario.map)
Provides:       tex(Rosario.sty)
Provides:       tex(T1Rosario-LF.fd)
Provides:       tex(TS1Rosario-LF.fd)
Provides:       tex(ros_amohrd.enc)
Provides:       tex(ros_c353pt.enc)
Provides:       tex(ros_k6z3ge.enc)
Provides:       tex(ros_y2egj5.enc)
Requires:       tex(kvoptions.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source14:       rosario.tar.xz
Source15:       rosario.doc.tar.xz

%description -n texlive-rosario
The package provides the files required to use the Rosario
fonts with LaTeX. Rosario is a set of four fonts provided by
Hector Gatti, Adobe Typekit & Omnibus-Type Team under the Open
Font License (OFL), version 1.1. The fonts are copyright (c)
2012-2015, Omnibus-Type.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-rosario-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn40843
Release:        0
Summary:        Documentation for texlive-rosario
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-rosario-doc
This package includes the documentation for texlive-rosario


%package -n texlive-rosario-fonts
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn40843
Release:        0
Summary:        Severed fonts for texlive-rosario
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Fonts
Url:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-rosario-fonts
The  separated fonts package for texlive-rosario
%post -n texlive-rosario
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap Rosario.map' >> /var/run/texlive/run-updmap

%postun -n texlive-rosario 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap Rosario.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-rosario
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-rosario-fonts
%files -n texlive-rosario-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/rosario/OFL.txt
%{_texmfdistdir}/doc/fonts/rosario/README.md
%{_texmfdistdir}/doc/fonts/rosario/Rosario.pdf

%files -n texlive-rosario
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/enc/dvips/rosario/ros_amohrd.enc
%{_texmfdistdir}/fonts/enc/dvips/rosario/ros_c353pt.enc
%{_texmfdistdir}/fonts/enc/dvips/rosario/ros_k6z3ge.enc
%{_texmfdistdir}/fonts/enc/dvips/rosario/ros_y2egj5.enc
%{_texmfdistdir}/fonts/map/dvips/rosario/Rosario.map
%verify(link) %{_texmfdistdir}/fonts/opentype/public/rosario/Rosario-Bold.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/rosario/Rosario-BoldItalic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/rosario/Rosario-Italic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/rosario/Rosario-Regular.otf
%{_texmfdistdir}/fonts/tfm/public/rosario/Rosario-Bold-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/rosario/Rosario-Bold-lf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/rosario/Rosario-Bold-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/rosario/Rosario-Bold-lf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/rosario/Rosario-Bold-lf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/rosario/Rosario-Bold-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/rosario/Rosario-Bold-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/rosario/Rosario-Bold-lf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/rosario/Rosario-Bold-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/rosario/Rosario-Bold-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/rosario/Rosario-Bold-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/rosario/Rosario-BoldItalic-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/rosario/Rosario-BoldItalic-lf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/rosario/Rosario-BoldItalic-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/rosario/Rosario-BoldItalic-lf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/rosario/Rosario-BoldItalic-lf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/rosario/Rosario-BoldItalic-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/rosario/Rosario-BoldItalic-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/rosario/Rosario-BoldItalic-lf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/rosario/Rosario-BoldItalic-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/rosario/Rosario-BoldItalic-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/rosario/Rosario-BoldItalic-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/rosario/Rosario-Italic-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/rosario/Rosario-Italic-lf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/rosario/Rosario-Italic-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/rosario/Rosario-Italic-lf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/rosario/Rosario-Italic-lf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/rosario/Rosario-Italic-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/rosario/Rosario-Italic-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/rosario/Rosario-Italic-lf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/rosario/Rosario-Italic-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/rosario/Rosario-Italic-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/rosario/Rosario-Italic-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/rosario/Rosario-Regular-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/rosario/Rosario-Regular-lf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/rosario/Rosario-Regular-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/rosario/Rosario-Regular-lf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/rosario/Rosario-Regular-lf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/rosario/Rosario-Regular-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/rosario/Rosario-Regular-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/rosario/Rosario-Regular-lf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/rosario/Rosario-Regular-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/rosario/Rosario-Regular-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/rosario/Rosario-Regular-lf-ts1.tfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/rosario/Rosario-Bold.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/rosario/Rosario-BoldItalic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/rosario/Rosario-BoldItalicLCDFJ.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/rosario/Rosario-BoldLCDFJ.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/rosario/Rosario-Italic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/rosario/Rosario-ItalicLCDFJ.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/rosario/Rosario-Regular.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/rosario/Rosario-RegularLCDFJ.pfb
%{_texmfdistdir}/fonts/vf/public/rosario/Rosario-Bold-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/rosario/Rosario-Bold-lf-ot1.vf
%{_texmfdistdir}/fonts/vf/public/rosario/Rosario-Bold-lf-t1.vf
%{_texmfdistdir}/fonts/vf/public/rosario/Rosario-Bold-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/rosario/Rosario-BoldItalic-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/rosario/Rosario-BoldItalic-lf-ot1.vf
%{_texmfdistdir}/fonts/vf/public/rosario/Rosario-BoldItalic-lf-t1.vf
%{_texmfdistdir}/fonts/vf/public/rosario/Rosario-BoldItalic-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/rosario/Rosario-Italic-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/rosario/Rosario-Italic-lf-ot1.vf
%{_texmfdistdir}/fonts/vf/public/rosario/Rosario-Italic-lf-t1.vf
%{_texmfdistdir}/fonts/vf/public/rosario/Rosario-Italic-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/rosario/Rosario-Regular-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/rosario/Rosario-Regular-lf-ot1.vf
%{_texmfdistdir}/fonts/vf/public/rosario/Rosario-Regular-lf-t1.vf
%{_texmfdistdir}/fonts/vf/public/rosario/Rosario-Regular-lf-ts1.vf
%{_texmfdistdir}/tex/latex/rosario/LY1Rosario-LF.fd
%{_texmfdistdir}/tex/latex/rosario/OT1Rosario-LF.fd
%{_texmfdistdir}/tex/latex/rosario/Rosario.fontspec
%{_texmfdistdir}/tex/latex/rosario/Rosario.sty
%{_texmfdistdir}/tex/latex/rosario/T1Rosario-LF.fd
%{_texmfdistdir}/tex/latex/rosario/TS1Rosario-LF.fd

%files -n texlive-rosario-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-rosario
%config %{_sysconfdir}/fonts/conf.avail/58-texlive-rosario.conf
%config %{_sysconfdir}/fonts/conf.d/55-texlive-rosario.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-rosario/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-rosario/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-rosario/fonts.scale
%{_datadir}/fonts/texlive-rosario/Rosario-Bold.otf
%{_datadir}/fonts/texlive-rosario/Rosario-BoldItalic.otf
%{_datadir}/fonts/texlive-rosario/Rosario-Italic.otf
%{_datadir}/fonts/texlive-rosario/Rosario-Regular.otf
%{_datadir}/fonts/texlive-rosario/Rosario-Bold.pfb
%{_datadir}/fonts/texlive-rosario/Rosario-BoldItalic.pfb
%{_datadir}/fonts/texlive-rosario/Rosario-BoldItalicLCDFJ.pfb
%{_datadir}/fonts/texlive-rosario/Rosario-BoldLCDFJ.pfb
%{_datadir}/fonts/texlive-rosario/Rosario-Italic.pfb
%{_datadir}/fonts/texlive-rosario/Rosario-ItalicLCDFJ.pfb
%{_datadir}/fonts/texlive-rosario/Rosario-Regular.pfb
%{_datadir}/fonts/texlive-rosario/Rosario-RegularLCDFJ.pfb
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-rosario-fonts-%{texlive_version}.%{texlive_noarch}.1.0svn40843-%{release}-zypper
%endif

%package -n texlive-rotfloat
Version:        %{texlive_version}.%{texlive_noarch}.1.2svn18292
Release:        0
Summary:        Rotate floats
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-rotfloat-doc >= %{texlive_version}
Provides:       tex(rotfloat.sty)
Requires:       tex(float.sty)
Requires:       tex(rotating.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source16:       rotfloat.tar.xz
Source17:       rotfloat.doc.tar.xz

%description -n texlive-rotfloat
The float package provides commands to define new floats of
various styles (plain, boxed, ruled, and userdefined ones); the
rotating package provides new environments (sidewaysfigure and
sidewaystable) which are rotated by 90 or 270 degrees. But what
about new rotated floats, e.g. a rotated ruled one? This
package makes this possible; it builds a bridge between the two
packages and extends the commands from the float package to
define rotated versions of the new floats, too.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-rotfloat-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.2svn18292
Release:        0
Summary:        Documentation for texlive-rotfloat
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-rotfloat-doc
This package includes the documentation for texlive-rotfloat

%post -n texlive-rotfloat
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-rotfloat 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-rotfloat
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-rotfloat-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/rotfloat/examples.tex
%{_texmfdistdir}/doc/latex/rotfloat/rotfloat.pdf

%files -n texlive-rotfloat
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/rotfloat/rotfloat.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-rotfloat-%{texlive_version}.%{texlive_noarch}.1.2svn18292-%{release}-zypper
%endif

%package -n texlive-rotpages
Version:        %{texlive_version}.%{texlive_noarch}.3.0svn18740
Release:        0
Summary:        Typeset sets of pages upside-down and backwards
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-rotpages-doc >= %{texlive_version}
Provides:       tex(rotpages.sty)
Requires:       tex(calc.sty)
Requires:       tex(graphics.sty)
Requires:       tex(ifthen.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source18:       rotpages.tar.xz
Source19:       rotpages.doc.tar.xz

%description -n texlive-rotpages
The rotpages package allows you to format documents where small
sets of pages are rotated by 180 degrees and rearranged, so
that they can be read by turning the printed copy upside-down.
It was developed for collecting exercises and solutions: using
the package, you can print the exercise text normally and the
solutions rotated.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-rotpages-doc
Version:        %{texlive_version}.%{texlive_noarch}.3.0svn18740
Release:        0
Summary:        Documentation for texlive-rotpages
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-rotpages-doc
This package includes the documentation for texlive-rotpages

%post -n texlive-rotpages
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-rotpages 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-rotpages
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-rotpages-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/rotpages/Documentation/rotpages-doc.pdf
%{_texmfdistdir}/doc/latex/rotpages/Documentation/rotpages-doc.tex
%{_texmfdistdir}/doc/latex/rotpages/Examples/rotpages-doublecolumn-ex.pdf
%{_texmfdistdir}/doc/latex/rotpages/Examples/rotpages-doublecolumn-ex.tex
%{_texmfdistdir}/doc/latex/rotpages/Examples/rotpages-fancy-ex.pdf
%{_texmfdistdir}/doc/latex/rotpages/Examples/rotpages-fancy-ex.tex
%{_texmfdistdir}/doc/latex/rotpages/Examples/rotpages-singlecolumn-ex.pdf
%{_texmfdistdir}/doc/latex/rotpages/Examples/rotpages-singlecolumn-ex.tex
%{_texmfdistdir}/doc/latex/rotpages/README

%files -n texlive-rotpages
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/rotpages/rotpages.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-rotpages-%{texlive_version}.%{texlive_noarch}.3.0svn18740-%{release}-zypper
%endif

%package -n texlive-roundbox
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2svn29675
Release:        0
Summary:        Round boxes in LaTeX
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-roundbox-doc >= %{texlive_version}
Provides:       tex(roundbox.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source20:       roundbox.tar.xz
Source21:       roundbox.doc.tar.xz

%description -n texlive-roundbox
This package implements a command \roundbox that can be used,
in LaTeX, for producing boxes, framed with rounded corners.

date: 2018-11-28 19:44:34 +0000


%package -n texlive-roundbox-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2svn29675
Release:        0
Summary:        Documentation for texlive-roundbox
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-roundbox-doc
This package includes the documentation for texlive-roundbox

%post -n texlive-roundbox
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-roundbox 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-roundbox
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-roundbox-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/roundbox/README

%files -n texlive-roundbox
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/roundbox/roundbox.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-roundbox-%{texlive_version}.%{texlive_noarch}.0.0.2svn29675-%{release}-zypper
%endif

%package -n texlive-roundrect
Version:        %{texlive_version}.%{texlive_noarch}.2.2svn39796
Release:        0
Summary:        MetaPost macros for highly configurable rounded rectangles (optionally with text)
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-roundrect-doc >= %{texlive_version}
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source22:       roundrect.tar.xz
Source23:       roundrect.doc.tar.xz

%description -n texlive-roundrect
The roundrect macros for MetaPost provide ways to produce
rounded rectangles, which may or may not contain a title bar or
text (the title bar may itself contain text). They are
extremely configurable.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-roundrect-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.2svn39796
Release:        0
Summary:        Documentation for texlive-roundrect
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-roundrect-doc
This package includes the documentation for texlive-roundrect

%post -n texlive-roundrect
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-roundrect 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-roundrect
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-roundrect-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/metapost/roundrect/CHANGES
%{_texmfdistdir}/doc/metapost/roundrect/README
%{_texmfdistdir}/doc/metapost/roundrect/lppl.txt
%{_texmfdistdir}/doc/metapost/roundrect/roundrect.pdf

%files -n texlive-roundrect
%defattr(-,root,root,755)
%{_texmfdistdir}/metapost/roundrect/roundrect.mp
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-roundrect-%{texlive_version}.%{texlive_noarch}.2.2svn39796-%{release}-zypper
%endif

%package -n texlive-rrgtrees
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn27322
Release:        0
Summary:        Linguistic tree diagrams for Role and Reference Grammar (RRG) with LaTeX
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-rrgtrees-doc >= %{texlive_version}
Provides:       tex(rrgtrees.sty)
Requires:       tex(pst-node.sty)
Requires:       tex(pst-tree.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source24:       rrgtrees.tar.xz
Source25:       rrgtrees.doc.tar.xz

%description -n texlive-rrgtrees
A set of LaTeX macros that makes it easy to produce linguistic
tree diagrams suitable for Role and Reference Grammar (RRG).
This package allows the construction of trees with crossing
lines, as is required by this theory for many languages. There
is no known limit on number of tree nodes or levels. Requires
the pst-node and pst-tree LaTeX packages.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-rrgtrees-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn27322
Release:        0
Summary:        Documentation for texlive-rrgtrees
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-rrgtrees-doc
This package includes the documentation for texlive-rrgtrees

%post -n texlive-rrgtrees
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-rrgtrees 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-rrgtrees
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-rrgtrees-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/rrgtrees/Makefile
%{_texmfdistdir}/doc/latex/rrgtrees/README
%{_texmfdistdir}/doc/latex/rrgtrees/rrgtrees.pdf

%files -n texlive-rrgtrees
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/rrgtrees/rrgtrees.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-rrgtrees-%{texlive_version}.%{texlive_noarch}.1.1svn27322-%{release}-zypper
%endif

%package -n texlive-rsc
Version:        %{texlive_version}.%{texlive_noarch}.3.1fsvn41923
Release:        0
Summary:        BibTeX style for use with RSC journals
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-rsc-doc >= %{texlive_version}
Provides:       tex(rsc.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(mciteplus.sty)
Requires:       tex(natbib.sty)
Requires:       tex(natmove.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source26:       rsc.tar.xz
Source27:       rsc.doc.tar.xz

%description -n texlive-rsc
The rsc package provides a BibTeX style in accordance with the
requirements of the Royal Society of Chemistry. It was
originally based on the file pccp.bst, but also implements a
number of styles from the achemso package. The package is now a
stub for the chemstyle package, which the author developed to
unify the writing of articles with a chemistry content.

date: 2016-08-22 20:14:27 +0000


%package -n texlive-rsc-doc
Version:        %{texlive_version}.%{texlive_noarch}.3.1fsvn41923
Release:        0
Summary:        Documentation for texlive-rsc
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-rsc-doc
This package includes the documentation for texlive-rsc

%post -n texlive-rsc
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-rsc 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-rsc
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-rsc-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/rsc/LICENSE.md
%{_texmfdistdir}/doc/latex/rsc/README.md
%{_texmfdistdir}/doc/latex/rsc/rsc.pdf

%files -n texlive-rsc
%defattr(-,root,root,755)
%{_texmfdistdir}/bibtex/bst/rsc/angew.bst
%{_texmfdistdir}/bibtex/bst/rsc/rsc.bst
%{_texmfdistdir}/tex/latex/rsc/rsc.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-rsc-%{texlive_version}.%{texlive_noarch}.3.1fsvn41923-%{release}-zypper
%endif

%package -n texlive-rsfs
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Ralph Smith's Formal Script font
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(updmap.cfg)
#!BuildIgnore:  tex(updmap.cfg)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(updmap.cfg)
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires:       texlive-rsfs-fonts >= %{texlive_version}
Recommends:     texlive-rsfs-doc >= %{texlive_version}
Provides:       tex(rsfs.map)
Provides:       tex(rsfs10.tfm)
Provides:       tex(rsfs5.tfm)
Provides:       tex(rsfs7.tfm)
Provides:       tex(scrload.tex)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source28:       rsfs.tar.xz
Source29:       rsfs.doc.tar.xz

%description -n texlive-rsfs
The fonts provide uppercase 'formal' script letters for use as
symbols in scientific and mathematical typesetting (in contrast
to the informal script fonts such as that used for the
'calligraphic' symbols in the TeX maths symbol font). The fonts
are provided as Metafont source, and as derived Adobe Type 1
format. LaTeX support, for using these fonts in mathematics, is
available via one of the packages calrsfs and mathrsfs.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-rsfs-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Documentation for texlive-rsfs
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-rsfs-doc
This package includes the documentation for texlive-rsfs


%package -n texlive-rsfs-fonts
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Severed fonts for texlive-rsfs
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Fonts
Url:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-rsfs-fonts
The  separated fonts package for texlive-rsfs
%post -n texlive-rsfs
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMixedMap rsfs.map' >> /var/run/texlive/run-updmap

%postun -n texlive-rsfs 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMixedMap rsfs.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-rsfs
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-rsfs-fonts
%files -n texlive-rsfs-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/rsfs/README
%{_texmfdistdir}/doc/fonts/rsfs/README.type1

%files -n texlive-rsfs
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/afm/public/rsfs/rsfs10.afm
%{_texmfdistdir}/fonts/afm/public/rsfs/rsfs5.afm
%{_texmfdistdir}/fonts/afm/public/rsfs/rsfs7.afm
%{_texmfdistdir}/fonts/map/dvips/rsfs/rsfs.map
%{_texmfdistdir}/fonts/source/public/rsfs/rsfs10.mf
%{_texmfdistdir}/fonts/source/public/rsfs/rsfs5.mf
%{_texmfdistdir}/fonts/source/public/rsfs/rsfs7.mf
%{_texmfdistdir}/fonts/source/public/rsfs/script.mf
%{_texmfdistdir}/fonts/source/public/rsfs/scriptu.mf
%{_texmfdistdir}/fonts/tfm/public/rsfs/rsfs10.tfm
%{_texmfdistdir}/fonts/tfm/public/rsfs/rsfs5.tfm
%{_texmfdistdir}/fonts/tfm/public/rsfs/rsfs7.tfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/rsfs/rsfs10.pfb
%{_texmfdistdir}/fonts/type1/public/rsfs/rsfs10.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/rsfs/rsfs5.pfb
%{_texmfdistdir}/fonts/type1/public/rsfs/rsfs5.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/rsfs/rsfs7.pfb
%{_texmfdistdir}/fonts/type1/public/rsfs/rsfs7.pfm
%{_texmfdistdir}/tex/plain/rsfs/scrload.tex

%files -n texlive-rsfs-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-rsfs
%config %{_sysconfdir}/fonts/conf.avail/58-texlive-rsfs.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-rsfs/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-rsfs/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-rsfs/fonts.scale
%{_datadir}/fonts/texlive-rsfs/rsfs10.pfb
%{_datadir}/fonts/texlive-rsfs/rsfs5.pfb
%{_datadir}/fonts/texlive-rsfs/rsfs7.pfb
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-rsfs-fonts-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif

%package -n texlive-rsfso
Version:        %{texlive_version}.%{texlive_noarch}.1.02svn37965
Release:        0
Summary:        A mathematical calligraphic font based on rsfs
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(updmap.cfg)
#!BuildIgnore:  tex(updmap.cfg)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(updmap.cfg)
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-rsfso-doc >= %{texlive_version}
Provides:       tex(rrsfso10.tfm)
Provides:       tex(rrsfso5.tfm)
Provides:       tex(rrsfso7.tfm)
Provides:       tex(rsfso.map)
Provides:       tex(rsfso.sty)
Provides:       tex(rsfso10.tfm)
Provides:       tex(rsfso10.vf)
Provides:       tex(rsfso5.tfm)
Provides:       tex(rsfso5.vf)
Provides:       tex(rsfso7.tfm)
Provides:       tex(rsfso7.vf)
Provides:       tex(ursfso.fd)
Requires:       tex(cmr10.tfm)
Requires:       tex(cmr5.tfm)
Requires:       tex(cmr7.tfm)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source30:       rsfso.tar.xz
Source31:       rsfso.doc.tar.xz

%description -n texlive-rsfso
The package provides virtual fonts and LaTeX support files for
mathematical calligraphic fonts based on the rsfs Adobe Type 1
fonts (which must also be present for successful installation,
with the slant substantially reduced. The output is quite
similar to that from the Adobe Mathematical Pi script font.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-rsfso-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.02svn37965
Release:        0
Summary:        Documentation for texlive-rsfso
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-rsfso-doc
This package includes the documentation for texlive-rsfso

%post -n texlive-rsfso
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap rsfso.map' >> /var/run/texlive/run-updmap

%postun -n texlive-rsfso 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap rsfso.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-rsfso
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-rsfso-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/rsfso/README
%{_texmfdistdir}/doc/fonts/rsfso/mh2scr0.png
%{_texmfdistdir}/doc/fonts/rsfso/rsfso-doc.pdf
%{_texmfdistdir}/doc/fonts/rsfso/rsfso-doc.tex

%files -n texlive-rsfso
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/map/dvips/rsfso/rsfso.map
%{_texmfdistdir}/fonts/tfm/public/rsfso/rrsfso10.tfm
%{_texmfdistdir}/fonts/tfm/public/rsfso/rrsfso5.tfm
%{_texmfdistdir}/fonts/tfm/public/rsfso/rrsfso7.tfm
%{_texmfdistdir}/fonts/tfm/public/rsfso/rsfso10.tfm
%{_texmfdistdir}/fonts/tfm/public/rsfso/rsfso5.tfm
%{_texmfdistdir}/fonts/tfm/public/rsfso/rsfso7.tfm
%{_texmfdistdir}/fonts/vf/public/rsfso/rsfso10.vf
%{_texmfdistdir}/fonts/vf/public/rsfso/rsfso5.vf
%{_texmfdistdir}/fonts/vf/public/rsfso/rsfso7.vf
%{_texmfdistdir}/tex/latex/rsfso/rsfso.sty
%{_texmfdistdir}/tex/latex/rsfso/ursfso.fd
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-rsfso-%{texlive_version}.%{texlive_noarch}.1.02svn37965-%{release}-zypper
%endif

%package -n texlive-rterface
Version:        %{texlive_version}.%{texlive_noarch}.svn30084
Release:        0
Summary:        Access to R analysis from within a document
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-rterface-doc >= %{texlive_version}
Provides:       tex(rterface.sty)
Requires:       tex(newfile.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source32:       rterface.tar.xz
Source33:       rterface.doc.tar.xz

%description -n texlive-rterface
The package mediates interaction between LaTeX and R; it allows
LaTeX to set R's parameters, and provides code to read R
output.

date: 2018-04-22 06:12:20 +0000


%package -n texlive-rterface-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn30084
Release:        0
Summary:        Documentation for texlive-rterface
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-rterface-doc
This package includes the documentation for texlive-rterface

%post -n texlive-rterface
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-rterface 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-rterface
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-rterface-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/rterface/README
%{_texmfdistdir}/doc/latex/rterface/rterface.pdf
%{_texmfdistdir}/doc/latex/rterface/rterface.tex

%files -n texlive-rterface
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/rterface/rterface.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-rterface-%{texlive_version}.%{texlive_noarch}.svn30084-%{release}-zypper
%endif

%package -n texlive-rtkinenc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn20003
Release:        0
Summary:        Input encoding with fallback procedures
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-rtkinenc-doc >= %{texlive_version}
Provides:       tex(rtkinenc.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source34:       rtkinenc.tar.xz
Source35:       rtkinenc.doc.tar.xz

%description -n texlive-rtkinenc
The rtkinenc package is functionally similar to the standard
LaTeX package inputenc: both set up active characters so that
an input character outside the range of 7-bit visible ASCII is
coverted into one or more corresponding LaTeX commands. The
main difference lies in that rtkinenc allows the user to
specify a fallback procedure to use when the text command
corresponding to some input character isn't available. Names of
commands in rtkinenc have been selected so that it can read
inputenc encoding definition files, and the aim is that
rtkinenc should be backwards compatible with inputenc. rtkinenc
is not a new version of inputenc though, nor is it part of
standard LaTeX. For an example of how rtkinenc is used, the
user may look at the tclldoc class.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-rtkinenc-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn20003
Release:        0
Summary:        Documentation for texlive-rtkinenc
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-rtkinenc-doc
This package includes the documentation for texlive-rtkinenc

%post -n texlive-rtkinenc
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-rtkinenc 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-rtkinenc
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-rtkinenc-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/rtkinenc/README.txt
%{_texmfdistdir}/doc/latex/rtkinenc/rtkinenc-doc.pdf
%{_texmfdistdir}/doc/latex/rtkinenc/rtkinenc-doc.tex

%files -n texlive-rtkinenc
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/rtkinenc/rtkinenc.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-rtkinenc-%{texlive_version}.%{texlive_noarch}.1.0svn20003-%{release}-zypper
%endif

%package -n texlive-rtklage
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        A package for German lawyers
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-rtklage-doc >= %{texlive_version}
Provides:       tex(rtklage.cls)
Requires:       tex(alphanum.sty)
Requires:       tex(babel.sty)
Requires:       tex(calc.sty)
Requires:       tex(color.sty)
Requires:       tex(eso-pic.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(numprint.sty)
Requires:       tex(scrdate.sty)
Requires:       tex(scrpage2.sty)
Requires:       tex(twoopt.sty)
Requires:       tex(xspace.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source36:       rtklage.tar.xz
Source37:       rtklage.doc.tar.xz

%description -n texlive-rtklage
RATeX is a newly developed bundle of packages and classes
provided for German lawyers. Now in the early beginning it only
contains rtklage, a class to make lawsuits.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-rtklage-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Documentation for texlive-rtklage
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Provides:       locale(texlive-rtklage-doc:de)

%description -n texlive-rtklage-doc
This package includes the documentation for texlive-rtklage

%post -n texlive-rtklage
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-rtklage 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-rtklage
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-rtklage-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/rtklage/README
%{_texmfdistdir}/doc/latex/rtklage/bspklage.tex
%{_texmfdistdir}/doc/latex/rtklage/rtklage.pdf

%files -n texlive-rtklage
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/rtklage/rtklage.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-rtklage-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif

%package -n texlive-rubik
Version:        %{texlive_version}.%{texlive_noarch}.5.0svn46791
Release:        0
Summary:        Document Rubik cube configurations and rotation sequences
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive-rubik-bin >= %{texlive_version}
#!BuildIgnore: texlive-rubik-bin
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-rubik-doc >= %{texlive_version}
Requires:       perl(Carp)
#!BuildIgnore:  perl(Carp)
Requires:       perl(Fatal)
#!BuildIgnore:  perl(Fatal)
Requires:       perl(warnings)
#!BuildIgnore:  perl(warnings)
Provides:       tex(rubikcube.sty)
Provides:       tex(rubikpatterns.sty)
Provides:       tex(rubikrotation.sty)
Provides:       tex(rubiktwocube.sty)
Requires:       tex(fancyvrb.sty)
Requires:       tex(forarray.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(shellesc.sty)
Requires:       tex(tikz.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source38:       rubik.tar.xz
Source39:       rubik.doc.tar.xz

%description -n texlive-rubik
The bundle provides four packages: rubikcube provides commands
for typesetting Rubik cubes and their transformations,
rubiktwocube provides commands for typesetting Rubik twocubes
and their transformations, rubikrotation which can process a
sequence of Rubik rotation moves, with the help of a Perl
package executed via \write18 (shell escape) commands, and
rubikpatterns, a collection of well known patterns and their
associated rotation sequences.

date: 2018-03-02 15:59:55 +0000


%package -n texlive-rubik-doc
Version:        %{texlive_version}.%{texlive_noarch}.5.0svn46791
Release:        0
Summary:        Documentation for texlive-rubik
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-rubik-doc
This package includes the documentation for texlive-rubik

%post -n texlive-rubik
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-rubik 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-rubik
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-rubik-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/rubik/README.txt
%{_texmfdistdir}/doc/latex/rubik/rubik-doc-figA.pdf
%{_texmfdistdir}/doc/latex/rubik/rubik-doc-figB.pdf
%{_texmfdistdir}/doc/latex/rubik/rubik-doc-figC.pdf
%{_texmfdistdir}/doc/latex/rubik/rubik-doc-figD.pdf
%{_texmfdistdir}/doc/latex/rubik/rubik-doc-figE.pdf
%{_texmfdistdir}/doc/latex/rubik/rubik-doc-figF.pdf
%{_texmfdistdir}/doc/latex/rubik/rubikcube.pdf
%{_texmfdistdir}/doc/latex/rubik/rubikexamples.pdf
%{_texmfdistdir}/doc/latex/rubik/rubikexamples.sh
%{_texmfdistdir}/doc/latex/rubik/rubikexamples.tex
%{_texmfdistdir}/doc/latex/rubik/rubikpatterns-doc-figA.pdf
%{_texmfdistdir}/doc/latex/rubik/rubikpatterns.pdf
%{_texmfdistdir}/doc/latex/rubik/rubikpatternsLIST.pdf
%{_texmfdistdir}/doc/latex/rubik/rubikpatternsLIST.sh
%{_texmfdistdir}/doc/latex/rubik/rubikpatternsLIST.tex
%{_texmfdistdir}/doc/latex/rubik/rubikrot-doc-figA.pdf
%{_texmfdistdir}/doc/latex/rubik/rubikrot-doc-figB.pdf
%{_texmfdistdir}/doc/latex/rubik/rubikrot-doc-figC.pdf
%{_texmfdistdir}/doc/latex/rubik/rubikrot-doc-figD.pdf
%{_texmfdistdir}/doc/latex/rubik/rubikrotation.pdf
%{_texmfdistdir}/doc/latex/rubik/rubikrotationPL.pdf
%{_texmfdistdir}/doc/latex/rubik/rubiktwo-doc-figA.pdf
%{_texmfdistdir}/doc/latex/rubik/rubiktwocube.pdf
%{_mandir}/man1/rubikrotation.1*

%files -n texlive-rubik
%defattr(-,root,root,755)
%{_texmfdistdir}/scripts/rubik/rubikrotation.pl
%{_texmfdistdir}/tex/latex/rubik/rubikcube.sty
%{_texmfdistdir}/tex/latex/rubik/rubikpatterns.sty
%{_texmfdistdir}/tex/latex/rubik/rubikrotation.sty
%{_texmfdistdir}/tex/latex/rubik/rubiktwocube.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-rubik-%{texlive_version}.%{texlive_noarch}.5.0svn46791-%{release}-zypper
%endif

%package -n texlive-ruhyphen
Version:        %{texlive_version}.%{texlive_noarch}.1.6svn21081
Release:        0
Summary:        Russian hyphenation
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Provides:       tex(catkoi.tex)
Provides:       tex(cyryoal.tex)
Provides:       tex(cyryoas.tex)
Provides:       tex(cyryoct.tex)
Provides:       tex(cyryodv.tex)
Provides:       tex(cyryomg.tex)
Provides:       tex(cyryovl.tex)
Provides:       tex(cyryozn.tex)
Provides:       tex(enrhm2.tex)
Provides:       tex(hypht2.tex)
Provides:       tex(koi2koi.tex)
Provides:       tex(koi2lcy.tex)
Provides:       tex(koi2ot2.tex)
Provides:       tex(koi2t2a.tex)
Provides:       tex(koi2ucy.tex)
Provides:       tex(ruenhyph.tex)
Provides:       tex(ruhyphal.tex)
Provides:       tex(ruhyphas.tex)
Provides:       tex(ruhyphct.tex)
Provides:       tex(ruhyphdv.tex)
Provides:       tex(ruhyphen.tex)
Provides:       tex(ruhyphmg.tex)
Provides:       tex(ruhyphvl.tex)
Provides:       tex(ruhyphzn.tex)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source40:       ruhyphen.tar.xz

%description -n texlive-ruhyphen
A collection of Russian hyphenation patterns supporting a
number of Cyrillic font encodings, including T2, UCY (Omega
Unicode Cyrillic), LCY, LWN (OT2), and koi8-r.

date: 2016-06-24 17:18:15 +0000

%post -n texlive-ruhyphen
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-ruhyphen 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-ruhyphen
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-ruhyphen
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/ruhyphen/catkoi.tex
%{_texmfdistdir}/tex/generic/ruhyphen/cyryoal.tex
%{_texmfdistdir}/tex/generic/ruhyphen/cyryoas.tex
%{_texmfdistdir}/tex/generic/ruhyphen/cyryoct.tex
%{_texmfdistdir}/tex/generic/ruhyphen/cyryodv.tex
%{_texmfdistdir}/tex/generic/ruhyphen/cyryomg.tex
%{_texmfdistdir}/tex/generic/ruhyphen/cyryovl.tex
%{_texmfdistdir}/tex/generic/ruhyphen/cyryozn.tex
%{_texmfdistdir}/tex/generic/ruhyphen/enrhm2.tex
%{_texmfdistdir}/tex/generic/ruhyphen/hypht2.tex
%{_texmfdistdir}/tex/generic/ruhyphen/koi2koi.tex
%{_texmfdistdir}/tex/generic/ruhyphen/koi2lcy.tex
%{_texmfdistdir}/tex/generic/ruhyphen/koi2ot2.tex
%{_texmfdistdir}/tex/generic/ruhyphen/koi2t2a.tex
%{_texmfdistdir}/tex/generic/ruhyphen/koi2ucy.tex
%{_texmfdistdir}/tex/generic/ruhyphen/ruenhyph.tex
%{_texmfdistdir}/tex/generic/ruhyphen/ruhyphal.tex
%{_texmfdistdir}/tex/generic/ruhyphen/ruhyphas.tex
%{_texmfdistdir}/tex/generic/ruhyphen/ruhyphct.tex
%{_texmfdistdir}/tex/generic/ruhyphen/ruhyphdv.tex
%{_texmfdistdir}/tex/generic/ruhyphen/ruhyphen.tex
%{_texmfdistdir}/tex/generic/ruhyphen/ruhyphmg.tex
%{_texmfdistdir}/tex/generic/ruhyphen/ruhyphvl.tex
%{_texmfdistdir}/tex/generic/ruhyphen/ruhyphzn.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-ruhyphen-%{texlive_version}.%{texlive_noarch}.1.6svn21081-%{release}-zypper
%endif

%package -n texlive-rulercompass
Version:        %{texlive_version}.%{texlive_noarch}.1svn32392
Release:        0
Summary:        A TikZ library for straight-edge and compass diagrams
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-rulercompass-doc >= %{texlive_version}
Provides:       tex(tikzlibraryrulercompass.code.tex)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source41:       rulercompass.tar.xz
Source42:       rulercompass.doc.tar.xz

%description -n texlive-rulercompass
The package defines some commands and styles to support drawing
straight-edge and compass diagrams with TikZ.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-rulercompass-doc
Version:        %{texlive_version}.%{texlive_noarch}.1svn32392
Release:        0
Summary:        Documentation for texlive-rulercompass
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-rulercompass-doc
This package includes the documentation for texlive-rulercompass

%post -n texlive-rulercompass
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-rulercompass 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-rulercompass
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-rulercompass-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/rulercompass/README.txt
%{_texmfdistdir}/doc/latex/rulercompass/rulercompass.pdf
%{_texmfdistdir}/doc/latex/rulercompass/rulercompass_doc.pdf
%{_texmfdistdir}/doc/latex/rulercompass/rulercompass_doc.tex

%files -n texlive-rulercompass
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/rulercompass/tikzlibraryrulercompass.code.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-rulercompass-%{texlive_version}.%{texlive_noarch}.1svn32392-%{release}-zypper
%endif

%package -n texlive-russ
Version:        %{texlive_version}.%{texlive_noarch}.svn25209
Release:        0
Summary:        LaTeX in Russian, without babel
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-russ-doc >= %{texlive_version}
Provides:       tex(russ.sty)
Requires:       tex(inputenc.sty)
Requires:       tex(t2aenc.def)
Requires:       tex(xspace.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source43:       russ.tar.xz
Source44:       russ.doc.tar.xz

%description -n texlive-russ
The package aims to facilitate Russian typesetting (based on
input using MicroSoft Code Page 1251). Russian hyphenation is
selected, and various mathematical commands are set up in
Russian style. Furthermore all Cyrillic letters' catcodes are
set to "letter", so that commands with Cyrillic letters in
their names may be defined.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-russ-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn25209
Release:        0
Summary:        Documentation for texlive-russ
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Provides:       locale(texlive-russ-doc:en;ru)

%description -n texlive-russ-doc
This package includes the documentation for texlive-russ

%post -n texlive-russ
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-russ 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-russ
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-russ-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/russ/README
%{_texmfdistdir}/doc/latex/russ/readme.RU.txt
%{_texmfdistdir}/doc/latex/russ/russ_doc.pdf
%{_texmfdistdir}/doc/latex/russ/russ_doc.tex

%files -n texlive-russ
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/russ/russ.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-russ-%{texlive_version}.%{texlive_noarch}.svn25209-%{release}-zypper
%endif

%package -n texlive-rutitlepage
Version:        %{texlive_version}.%{texlive_noarch}.2.1svn49125
Release:        0
Summary:        Radboud University Titlepage Package
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-rutitlepage-doc >= %{texlive_version}
Provides:       tex(rutitlepage.sty)
Requires:       tex(geometry.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(iflang.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(keyval.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source45:       rutitlepage.tar.xz
Source46:       rutitlepage.doc.tar.xz

%description -n texlive-rutitlepage
This is an unofficial LaTeX package to generate titlepages for
the Radboud University, Nijmegen. It uses official vector logos
from the university. This package requires the following other
LaTeX packages: geometry, graphicx, ifpdf, keyval, iflang, and,
optionnaly, babel-dutch.

date: 2018-11-10 19:32:18 +0000


%package -n texlive-rutitlepage-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.1svn49125
Release:        0
Summary:        Documentation for texlive-rutitlepage
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-rutitlepage-doc
This package includes the documentation for texlive-rutitlepage

%post -n texlive-rutitlepage
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-rutitlepage 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-rutitlepage
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-rutitlepage-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/rutitlepage/README.md
%{_texmfdistdir}/doc/latex/rutitlepage/rutitlepage.pdf

%files -n texlive-rutitlepage
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/rutitlepage/rutitlepage.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-rutitlepage-%{texlive_version}.%{texlive_noarch}.2.1svn49125-%{release}-zypper
%endif

%package -n texlive-rviewport
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn23739
Release:        0
Summary:        Relative Viewport for Graphics Inclusion
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-rviewport-doc >= %{texlive_version}
Provides:       tex(rviewport.sty)
Requires:       tex(keyval.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source47:       rviewport.tar.xz
Source48:       rviewport.doc.tar.xz

%description -n texlive-rviewport
Package graphicx provides a useful keyword viewport which
allows to show just a part of an image. However, one needs to
put there the actual coordinates of the viewport window.
Sometimes it is useful to have relative coordinates as
fractions of natural size. For example, one may want to print a
large image on a spread, putting a half on a verso page, and
another half on the next recto page. For this one would need a
viewport occupying exactly one half of the file's bounding box,
whatever the actual width of the image may be. This package
adds a new keyword rviewport to the graphicx package
specifiying Relative Viewport for graphics inclusion: a window
defined by the given fractions of the natural width and height
of the image.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-rviewport-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn23739
Release:        0
Summary:        Documentation for texlive-rviewport
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-rviewport-doc
This package includes the documentation for texlive-rviewport

%post -n texlive-rviewport
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-rviewport 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-rviewport
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-rviewport-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/rviewport/Makefile
%{_texmfdistdir}/doc/latex/rviewport/README
%{_texmfdistdir}/doc/latex/rviewport/rviewport.pdf
%{_texmfdistdir}/doc/latex/rviewport/vitruvian.jpg

%files -n texlive-rviewport
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/rviewport/rviewport.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-rviewport-%{texlive_version}.%{texlive_noarch}.1.0svn23739-%{release}-zypper
%endif

%package -n texlive-rvwrite
Version:        %{texlive_version}.%{texlive_noarch}.1.2svn19614
Release:        0
Summary:        Increase the number of available output streams in LaTeX
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-rvwrite-doc >= %{texlive_version}
Provides:       tex(rvwrite.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source49:       rvwrite.tar.xz
Source50:       rvwrite.doc.tar.xz

%description -n texlive-rvwrite
The package addresses, for LaTeX documents, the severe
limitation on the number of output streams that TeX provides.
The package uses a single TeX output stream, and writes
"marked-up" output to this stream. The user may then
post-process the marked-up output file, using LaTeX, and the
document's output appears as separate files, according to the
calls made to the package. The output to be post-processed uses
macros from the widely-available ProTeX package.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-rvwrite-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.2svn19614
Release:        0
Summary:        Documentation for texlive-rvwrite
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-rvwrite-doc
This package includes the documentation for texlive-rvwrite

%post -n texlive-rvwrite
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-rvwrite 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-rvwrite
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-rvwrite-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/rvwrite/Makefile
%{_texmfdistdir}/doc/latex/rvwrite/README
%{_texmfdistdir}/doc/latex/rvwrite/rvwrite-doc.pdf
%{_texmfdistdir}/doc/latex/rvwrite/rvwrite-doc.tex
%{_texmfdistdir}/doc/latex/rvwrite/test.tex

%files -n texlive-rvwrite
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/rvwrite/rvwrite.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-rvwrite-%{texlive_version}.%{texlive_noarch}.1.2svn19614-%{release}-zypper
%endif

%package -n texlive-ryersonsgsthesis
Version:        %{texlive_version}.%{texlive_noarch}.1.0.3svn50119
Release:        0
Summary:        Ryerson School of Graduate Studies thesis template
License:        Apache-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-ryersonsgsthesis-doc >= %{texlive_version}
Provides:       tex(ryersonSGSThesis.cls)
Requires:       tex(IEEEtrantools.sty)
Requires:       tex(algorithm.sty)
Requires:       tex(algorithmicx.sty)
Requires:       tex(algpseudocode.sty)
Requires:       tex(amsfonts.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(appendix.sty)
Requires:       tex(array.sty)
Requires:       tex(blindtext.sty)
Requires:       tex(caption.sty)
Requires:       tex(charter.sty)
Requires:       tex(cite.sty)
Requires:       tex(csquotes.sty)
Requires:       tex(float.sty)
Requires:       tex(geometry.sty)
Requires:       tex(glossaries.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(listings.sty)
Requires:       tex(lmodern.sty)
Requires:       tex(longtable.sty)
Requires:       tex(makeidx.sty)
Requires:       tex(ragged2e.sty)
Requires:       tex(report.cls)
Requires:       tex(sectsty.sty)
Requires:       tex(setspace.sty)
Requires:       tex(subcaption.sty)
Requires:       tex(subfiles.sty)
Requires:       tex(titlesec.sty)
Requires:       tex(todonotes.sty)
Requires:       tex(verbatim.sty)
Requires:       tex(xcolor.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source51:       ryersonsgsthesis.tar.xz
Source52:       ryersonsgsthesis.doc.tar.xz

%description -n texlive-ryersonsgsthesis
This package provides a LaTeX class and template files for
Ryerson School of Graduate Studies (SGS) theses.

date: 2019-02-26 04:13:11 +0000


%package -n texlive-ryersonsgsthesis-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0.3svn50119
Release:        0
Summary:        Documentation for texlive-ryersonsgsthesis
License:        Apache-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-ryersonsgsthesis-doc
This package includes the documentation for texlive-ryersonsgsthesis

%post -n texlive-ryersonsgsthesis
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-ryersonsgsthesis 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-ryersonsgsthesis
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-ryersonsgsthesis-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/ryersonsgsthesis/CHANGELOG.md
%{_texmfdistdir}/doc/latex/ryersonsgsthesis/LICENSE
%{_texmfdistdir}/doc/latex/ryersonsgsthesis/README.md
%{_texmfdistdir}/doc/latex/ryersonsgsthesis/rsgs-example.bib
%{_texmfdistdir}/doc/latex/ryersonsgsthesis/rsgs-example.pdf
%{_texmfdistdir}/doc/latex/ryersonsgsthesis/rsgs-example.tex
%{_texmfdistdir}/doc/latex/ryersonsgsthesis/rsgs-glossary.tex

%files -n texlive-ryersonsgsthesis
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/ryersonsgsthesis/ryersonSGSThesis.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-ryersonsgsthesis-%{texlive_version}.%{texlive_noarch}.1.0.3svn50119-%{release}-zypper
%endif

%package -n texlive-ryethesis
Version:        %{texlive_version}.%{texlive_noarch}.1.36svn33945
Release:        0
Summary:        Class for Ryerson Unversity Graduate School requirements
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-ryethesis-doc >= %{texlive_version}
Provides:       tex(ryethesis.cls)
Requires:       tex(book.cls)
Requires:       tex(bookmark.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(fancyhdr.sty)
Requires:       tex(float.sty)
Requires:       tex(glossaries.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(multicol.sty)
Requires:       tex(nomencl.sty)
Requires:       tex(setspace.sty)
Requires:       tex(vmargin.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source53:       ryethesis.tar.xz
Source54:       ryethesis.doc.tar.xz

%description -n texlive-ryethesis
The class offers support for formatting a thesis, dissertation
or project according to Ryerson University's School of Graduate
Studies thesis formatting regulations.

date: 2019-02-24 08:28:55 +0000


%package -n texlive-ryethesis-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.36svn33945
Release:        0
Summary:        Documentation for texlive-ryethesis
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-ryethesis-doc
This package includes the documentation for texlive-ryethesis

%post -n texlive-ryethesis
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-ryethesis 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-ryethesis
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-ryethesis-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/ryethesis/Makefile
%{_texmfdistdir}/doc/latex/ryethesis/README
%{_texmfdistdir}/doc/latex/ryethesis/figure1.pdf
%{_texmfdistdir}/doc/latex/ryethesis/ryesample.bib
%{_texmfdistdir}/doc/latex/ryethesis/ryesample.pdf
%{_texmfdistdir}/doc/latex/ryethesis/ryesample.tex
%{_texmfdistdir}/doc/latex/ryethesis/ryethesis.pdf

%files -n texlive-ryethesis
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/ryethesis/ryethesis.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-ryethesis-%{texlive_version}.%{texlive_noarch}.1.36svn33945-%{release}-zypper
%endif

%package -n texlive-sa-tikz
Version:        %{texlive_version}.%{texlive_noarch}.0.0.7asvn32815
Release:        0
Summary:        TikZ library to draw switching architectures
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-sa-tikz-doc >= %{texlive_version}
Provides:       tex(sa-tikz.sty)
Provides:       tex(tikzlibraryswitching-architectures.code.tex)
Requires:       tex(tikz.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source55:       sa-tikz.tar.xz
Source56:       sa-tikz.doc.tar.xz

%description -n texlive-sa-tikz
The package provides a library that offers an easy way to draw
switching architectures and to customize their aspect.

date: 2018-01-06 11:14:59 +0000


%package -n texlive-sa-tikz-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.7asvn32815
Release:        0
Summary:        Documentation for texlive-sa-tikz
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-sa-tikz-doc
This package includes the documentation for texlive-sa-tikz

%post -n texlive-sa-tikz
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-sa-tikz 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-sa-tikz
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-sa-tikz-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/sa-tikz/README
%{_texmfdistdir}/doc/latex/sa-tikz/pgfmanual-en-macros.tex
%{_texmfdistdir}/doc/latex/sa-tikz/sa-tikz-doc.pdf
%{_texmfdistdir}/doc/latex/sa-tikz/sa-tikz-doc.tex

%files -n texlive-sa-tikz
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/sa-tikz/sa-tikz.sty
%{_texmfdistdir}/tex/latex/sa-tikz/tikzlibraryswitching-architectures.code.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-sa-tikz-%{texlive_version}.%{texlive_noarch}.0.0.7asvn32815-%{release}-zypper
%endif

%package -n texlive-sageep
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn15878
Release:        0
Summary:        Format papers for the annual meeting of EEGS
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-sageep-doc >= %{texlive_version}
Provides:       tex(sageep.cls)
Requires:       tex(article.cls)
Requires:       tex(caption.sty)
Requires:       tex(courier.sty)
Requires:       tex(geometry.sty)
Requires:       tex(helvet.sty)
Requires:       tex(indentfirst.sty)
Requires:       tex(mathptmx.sty)
Requires:       tex(natbib.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source57:       sageep.tar.xz
Source58:       sageep.doc.tar.xz

%description -n texlive-sageep
The class provides formatting for papers for the annual meeting
of the Environmental and Engineering Geophysical Society (EEGS)
("Application of Geophysics to Engineering and Environmental
Problems", known as SAGEEP).

date: 2016-06-24 17:18:15 +0000


%package -n texlive-sageep-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn15878
Release:        0
Summary:        Documentation for texlive-sageep
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-sageep-doc
This package includes the documentation for texlive-sageep

%post -n texlive-sageep
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-sageep 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-sageep
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-sageep-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/sageep/README
%{_texmfdistdir}/doc/latex/sageep/sageep.bib
%{_texmfdistdir}/doc/latex/sageep/sageep.pdf
%{_texmfdistdir}/doc/latex/sageep/sageep_graphic2009.jpg
%{_texmfdistdir}/doc/latex/sageep/sample.pdf
%{_texmfdistdir}/doc/latex/sageep/sample.tex

%files -n texlive-sageep
%defattr(-,root,root,755)
%{_texmfdistdir}/bibtex/bst/sageep/sageep.bst
%{_texmfdistdir}/tex/latex/sageep/sageep.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-sageep-%{texlive_version}.%{texlive_noarch}.1.0svn15878-%{release}-zypper
%endif

%package -n texlive-sanitize-umlaut
Version:        %{texlive_version}.%{texlive_noarch}.1.00svn41365
Release:        0
Summary:        Sanitize umlauts for MakeIndex and pdfLaTeX
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-sanitize-umlaut-doc >= %{texlive_version}
Provides:       tex(sanitize-umlaut.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source59:       sanitize-umlaut.tar.xz
Source60:       sanitize-umlaut.doc.tar.xz

%description -n texlive-sanitize-umlaut
This packages sanitizes umlauts to be used directly in index
entries for MakeIndex and friends with pdfLaTeX. This means
that inside \index an umlaut can be used as "U or as U. In both
cases, the letter is written as "U into the raw index file for
correct processing with MakeIndex and pdfLaTeX.

date: 2018-01-07 11:06:50 +0000


%package -n texlive-sanitize-umlaut-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.00svn41365
Release:        0
Summary:        Documentation for texlive-sanitize-umlaut
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-sanitize-umlaut-doc
This package includes the documentation for texlive-sanitize-umlaut

%post -n texlive-sanitize-umlaut
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-sanitize-umlaut 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-sanitize-umlaut
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-sanitize-umlaut-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/sanitize-umlaut/README
%{_texmfdistdir}/doc/latex/sanitize-umlaut/german.ist
%{_texmfdistdir}/doc/latex/sanitize-umlaut/sanitize-umlaut.doc.sty
%{_texmfdistdir}/doc/latex/sanitize-umlaut/sanitize-umlaut.pdf
%{_texmfdistdir}/doc/latex/sanitize-umlaut/sanitize-umlaut.tex

%files -n texlive-sanitize-umlaut
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/sanitize-umlaut/sanitize-umlaut.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-sanitize-umlaut-%{texlive_version}.%{texlive_noarch}.1.00svn41365-%{release}-zypper
%endif

%package -n texlive-sanskrit
Version:        %{texlive_version}.%{texlive_noarch}.2.2.1svn42925
Release:        0
Summary:        Sanskrit support
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-sanskrit-doc >= %{texlive_version}
Provides:       tex(ot1skt.fd)
Provides:       tex(skt.sty)
Provides:       tex(skt10.tfm)
Provides:       tex(skt8.tfm)
Provides:       tex(skt9.tfm)
Provides:       tex(sktb10.tfm)
Provides:       tex(sktbs10.tfm)
Provides:       tex(sktf10.tfm)
Provides:       tex(sktfs10.tfm)
Provides:       tex(skts10.tfm)
Requires:       tex(ifthen.sty)
Requires:       tex(relsize.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source61:       sanskrit.tar.xz
Source62:       sanskrit.doc.tar.xz

%description -n texlive-sanskrit
A font and pre-processor suitable for the production of
documents written in Sanskrit. Type 1 versions of the fonts are
available.

date: 2017-01-11 19:18:05 +0000


%package -n texlive-sanskrit-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.2.1svn42925
Release:        0
Summary:        Documentation for texlive-sanskrit
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-sanskrit-doc
This package includes the documentation for texlive-sanskrit

%post -n texlive-sanskrit
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-sanskrit 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-sanskrit
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-sanskrit-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/sanskrit/README.md
%{_texmfdistdir}/doc/latex/sanskrit/README.pdf
%{_texmfdistdir}/doc/latex/sanskrit/build-ctan-dist.sh
%{_texmfdistdir}/doc/latex/sanskrit/sktdoc.pdf
%{_texmfdistdir}/doc/latex/sanskrit/sktdoc.skt

%files -n texlive-sanskrit
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/source/public/sanskrit/skt10.mf
%{_texmfdistdir}/fonts/source/public/sanskrit/skt8.mf
%{_texmfdistdir}/fonts/source/public/sanskrit/skt9.mf
%{_texmfdistdir}/fonts/source/public/sanskrit/sktb10.mf
%{_texmfdistdir}/fonts/source/public/sanskrit/sktbs10.mf
%{_texmfdistdir}/fonts/source/public/sanskrit/sktchars.mf
%{_texmfdistdir}/fonts/source/public/sanskrit/sktdefs.mf
%{_texmfdistdir}/fonts/source/public/sanskrit/sktf10.mf
%{_texmfdistdir}/fonts/source/public/sanskrit/sktfs10.mf
%{_texmfdistdir}/fonts/source/public/sanskrit/sktligs.mf
%{_texmfdistdir}/fonts/source/public/sanskrit/skts10.mf
%{_texmfdistdir}/fonts/tfm/public/sanskrit/skt10.tfm
%{_texmfdistdir}/fonts/tfm/public/sanskrit/skt8.tfm
%{_texmfdistdir}/fonts/tfm/public/sanskrit/skt9.tfm
%{_texmfdistdir}/fonts/tfm/public/sanskrit/sktb10.tfm
%{_texmfdistdir}/fonts/tfm/public/sanskrit/sktbs10.tfm
%{_texmfdistdir}/fonts/tfm/public/sanskrit/sktf10.tfm
%{_texmfdistdir}/fonts/tfm/public/sanskrit/sktfs10.tfm
%{_texmfdistdir}/fonts/tfm/public/sanskrit/skts10.tfm
%{_texmfdistdir}/tex/latex/sanskrit/ot1skt.fd
%{_texmfdistdir}/tex/latex/sanskrit/skt.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-sanskrit-%{texlive_version}.%{texlive_noarch}.2.2.1svn42925-%{release}-zypper
%endif

%package -n texlive-sanskrit-t1
Version:        %{texlive_version}.%{texlive_noarch}.svn35737
Release:        0
Summary:        Type 1 version of 'skt' fonts for Sanskrit
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(updmap.cfg)
#!BuildIgnore:  tex(updmap.cfg)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(updmap.cfg)
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires:       texlive-sanskrit-t1-fonts >= %{texlive_version}
Recommends:     texlive-sanskrit-t1-doc >= %{texlive_version}
Provides:       tex(skt.map)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source63:       sanskrit-t1.tar.xz
Source64:       sanskrit-t1.doc.tar.xz

%description -n texlive-sanskrit-t1
The sanskrit-t1 font package provides Type 1 version of Charles
Wikner's skt font series for the Sanskrit language.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-sanskrit-t1-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn35737
Release:        0
Summary:        Documentation for texlive-sanskrit-t1
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-sanskrit-t1-doc
This package includes the documentation for texlive-sanskrit-t1


%package -n texlive-sanskrit-t1-fonts
Version:        %{texlive_version}.%{texlive_noarch}.svn35737
Release:        0
Summary:        Severed fonts for texlive-sanskrit-t1
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Fonts
Url:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-sanskrit-t1-fonts
The  separated fonts package for texlive-sanskrit-t1
%post -n texlive-sanskrit-t1
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap skt.map' >> /var/run/texlive/run-updmap

%postun -n texlive-sanskrit-t1 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap skt.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-sanskrit-t1
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-sanskrit-t1-fonts
%files -n texlive-sanskrit-t1-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/sanskrit-t1/README
%{_texmfdistdir}/doc/fonts/sanskrit-t1/sktdoc.pdf

%files -n texlive-sanskrit-t1
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/map/dvips/sanskrit-t1/skt.map
%verify(link) %{_texmfdistdir}/fonts/type1/public/sanskrit-t1/skt10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sanskrit-t1/skt8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sanskrit-t1/skt9.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sanskrit-t1/sktb10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sanskrit-t1/sktbs10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sanskrit-t1/sktf10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sanskrit-t1/sktfs10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sanskrit-t1/skts10.pfb

%files -n texlive-sanskrit-t1-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-sanskrit-t1
%config %{_sysconfdir}/fonts/conf.avail/58-texlive-sanskrit-t1.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-sanskrit-t1/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-sanskrit-t1/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-sanskrit-t1/fonts.scale
%{_datadir}/fonts/texlive-sanskrit-t1/skt10.pfb
%{_datadir}/fonts/texlive-sanskrit-t1/skt8.pfb
%{_datadir}/fonts/texlive-sanskrit-t1/skt9.pfb
%{_datadir}/fonts/texlive-sanskrit-t1/sktb10.pfb
%{_datadir}/fonts/texlive-sanskrit-t1/sktbs10.pfb
%{_datadir}/fonts/texlive-sanskrit-t1/sktf10.pfb
%{_datadir}/fonts/texlive-sanskrit-t1/sktfs10.pfb
%{_datadir}/fonts/texlive-sanskrit-t1/skts10.pfb
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-sanskrit-t1-fonts-%{texlive_version}.%{texlive_noarch}.svn35737-%{release}-zypper
%endif

%package -n texlive-sansmath
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn17997
Release:        0
Summary:        Maths in a sans font
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-sansmath-doc >= %{texlive_version}
Provides:       tex(sansmath.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source65:       sansmath.tar.xz
Source66:       sansmath.doc.tar.xz

%description -n texlive-sansmath
The package defines a new math version sans, and a command
\sansmath that behaves somewhat like \boldmath

date: 2016-06-24 17:18:15 +0000


%package -n texlive-sansmath-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn17997
Release:        0
Summary:        Documentation for texlive-sansmath
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-sansmath-doc
This package includes the documentation for texlive-sansmath

%post -n texlive-sansmath
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-sansmath 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-sansmath
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-sansmath-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/sansmath/miscdoc.sty
%{_texmfdistdir}/doc/latex/sansmath/sansmath.pdf
%{_texmfdistdir}/doc/latex/sansmath/sansmath.tex

%files -n texlive-sansmath
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/sansmath/sansmath.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-sansmath-%{texlive_version}.%{texlive_noarch}.1.1svn17997-%{release}-zypper
%endif

%package -n texlive-sansmathaccent
Version:        %{texlive_version}.%{texlive_noarch}.svn30187
Release:        0
Summary:        Correct placement of accents in sans-serif maths
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(updmap.cfg)
#!BuildIgnore:  tex(updmap.cfg)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(updmap.cfg)
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-sansmathaccent-doc >= %{texlive_version}
Provides:       tex(mathkerncmssi10.tfm)
Provides:       tex(mathkerncmssi12.tfm)
Provides:       tex(mathkerncmssi17.tfm)
Provides:       tex(mathkerncmssi8.tfm)
Provides:       tex(mathkerncmssi9.tfm)
Provides:       tex(mathkerncmssxi10.tfm)
Provides:       tex(mathkerncmssxi10.vf)
Provides:       tex(mathkerncmssxi12.tfm)
Provides:       tex(mathkerncmssxi12.vf)
Provides:       tex(mathkerncmssxi17.tfm)
Provides:       tex(mathkerncmssxi17.vf)
Provides:       tex(mathkerncmssxi8.tfm)
Provides:       tex(mathkerncmssxi8.vf)
Provides:       tex(mathkerncmssxi9.tfm)
Provides:       tex(mathkerncmssxi9.vf)
Provides:       tex(ot1mathkerncmss.fd)
Provides:       tex(sansmathaccent.map)
Provides:       tex(sansmathaccent.sty)
Requires:       tex(cmssbx10.tfm)
Requires:       tex(ecso0800.tfm)
Requires:       tex(ecso0900.tfm)
Requires:       tex(ecso1000.tfm)
Requires:       tex(ecso1200.tfm)
Requires:       tex(ecso1728.tfm)
Requires:       tex(filehook.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source67:       sansmathaccent.tar.xz
Source68:       sansmathaccent.doc.tar.xz

%description -n texlive-sansmathaccent
Sans serif maths (produced by the beamer class or the sfmath
package) often has accents positioned incorrectly. The package
fixes the positioning of such accents when the default font
(cmssi) is used for sans serif maths.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-sansmathaccent-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn30187
Release:        0
Summary:        Documentation for texlive-sansmathaccent
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-sansmathaccent-doc
This package includes the documentation for texlive-sansmathaccent

%post -n texlive-sansmathaccent
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap sansmathaccent.map' >> /var/run/texlive/run-updmap

%postun -n texlive-sansmathaccent 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap sansmathaccent.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-sansmathaccent
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-sansmathaccent-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/sansmathaccent/README
%{_texmfdistdir}/doc/fonts/sansmathaccent/sansmathaccent.pdf
%{_texmfdistdir}/doc/fonts/sansmathaccent/sansmathaccent.tex

%files -n texlive-sansmathaccent
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/map/dvips/sansmathaccent/sansmathaccent.map
%{_texmfdistdir}/fonts/tfm/public/sansmathaccent/mathkerncmssi10.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathaccent/mathkerncmssi12.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathaccent/mathkerncmssi17.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathaccent/mathkerncmssi8.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathaccent/mathkerncmssi9.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathaccent/mathkerncmssxi10.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathaccent/mathkerncmssxi12.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathaccent/mathkerncmssxi17.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathaccent/mathkerncmssxi8.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathaccent/mathkerncmssxi9.tfm
%{_texmfdistdir}/fonts/vf/public/sansmathaccent/mathkerncmssxi10.vf
%{_texmfdistdir}/fonts/vf/public/sansmathaccent/mathkerncmssxi12.vf
%{_texmfdistdir}/fonts/vf/public/sansmathaccent/mathkerncmssxi17.vf
%{_texmfdistdir}/fonts/vf/public/sansmathaccent/mathkerncmssxi8.vf
%{_texmfdistdir}/fonts/vf/public/sansmathaccent/mathkerncmssxi9.vf
%{_texmfdistdir}/tex/latex/sansmathaccent/ot1mathkerncmss.fd
%{_texmfdistdir}/tex/latex/sansmathaccent/sansmathaccent.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-sansmathaccent-%{texlive_version}.%{texlive_noarch}.svn30187-%{release}-zypper
%endif

%package -n texlive-sansmathfonts
Version:        %{texlive_version}.%{texlive_noarch}.svn50756
Release:        0
Summary:        Correct placement of accents in sans-serif maths
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(updmap.cfg)
#!BuildIgnore:  tex(updmap.cfg)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(updmap.cfg)
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires:       texlive-sansmathfonts-fonts >= %{texlive_version}
Recommends:     texlive-sansmathfonts-doc >= %{texlive_version}
Provides:       tex(cmsmf10.tfm)
Provides:       tex(cmsmf10.vf)
Provides:       tex(cmsmf12.tfm)
Provides:       tex(cmsmf12.vf)
Provides:       tex(cmsmf17.tfm)
Provides:       tex(cmsmf17.vf)
Provides:       tex(cmsmf8.tfm)
Provides:       tex(cmsmf8.vf)
Provides:       tex(cmsmf9.tfm)
Provides:       tex(cmsmf9.vf)
Provides:       tex(cmsmfIPiXi10.tfm)
Provides:       tex(cmsmfIPiXi12.tfm)
Provides:       tex(cmsmfIPiXi17.tfm)
Provides:       tex(cmsmfIPiXi8.tfm)
Provides:       tex(cmsmfIPiXi9.tfm)
Provides:       tex(cmsmfIPiXibx10.tfm)
Provides:       tex(cmsmfIPiXibx12.tfm)
Provides:       tex(cmsmfIPiXibx17.tfm)
Provides:       tex(cmsmfIPiXibx8.tfm)
Provides:       tex(cmsmfIPiXibx9.tfm)
Provides:       tex(cmsmfIPiXibxcsc10.tfm)
Provides:       tex(cmsmfIPiXicsc10.tfm)
Provides:       tex(cmsmfIPiXicsc8.tfm)
Provides:       tex(cmsmfIPiXicsc9.tfm)
Provides:       tex(cmsmfIPiXicsci10.tfm)
Provides:       tex(cmsmfIPiXicsci8.tfm)
Provides:       tex(cmsmfIPiXicsci9.tfm)
Provides:       tex(cmsmfIPiXii10.tfm)
Provides:       tex(cmsmfIPiXii12.tfm)
Provides:       tex(cmsmfIPiXii17.tfm)
Provides:       tex(cmsmfIPiXii8.tfm)
Provides:       tex(cmsmfIPiXii9.tfm)
Provides:       tex(cmsmfIPiXixi10.tfm)
Provides:       tex(cmsmfIPiXixi12.tfm)
Provides:       tex(cmsmfIPiXixi17.tfm)
Provides:       tex(cmsmfIPiXixi8.tfm)
Provides:       tex(cmsmfIPiXixi9.tfm)
Provides:       tex(cmsmfIPiXixicsc10.tfm)
Provides:       tex(cmsmfbx10.tfm)
Provides:       tex(cmsmfbx10.vf)
Provides:       tex(cmsmfbx12.tfm)
Provides:       tex(cmsmfbx12.vf)
Provides:       tex(cmsmfbx17.tfm)
Provides:       tex(cmsmfbx17.vf)
Provides:       tex(cmsmfbx8.tfm)
Provides:       tex(cmsmfbx8.vf)
Provides:       tex(cmsmfbx9.tfm)
Provides:       tex(cmsmfbx9.vf)
Provides:       tex(cmsmfbxcsc10.tfm)
Provides:       tex(cmsmfbxcsc10.vf)
Provides:       tex(cmsmfcsc10.tfm)
Provides:       tex(cmsmfcsc10.vf)
Provides:       tex(cmsmfcsc8.tfm)
Provides:       tex(cmsmfcsc8.vf)
Provides:       tex(cmsmfcsc9.tfm)
Provides:       tex(cmsmfcsc9.vf)
Provides:       tex(cmsmfcsci10.tfm)
Provides:       tex(cmsmfcsci10.vf)
Provides:       tex(cmsmfcsci8.tfm)
Provides:       tex(cmsmfcsci8.vf)
Provides:       tex(cmsmfcsci9.tfm)
Provides:       tex(cmsmfcsci9.vf)
Provides:       tex(cmsmfi10.tfm)
Provides:       tex(cmsmfi10.vf)
Provides:       tex(cmsmfi12.tfm)
Provides:       tex(cmsmfi12.vf)
Provides:       tex(cmsmfi17.tfm)
Provides:       tex(cmsmfi17.vf)
Provides:       tex(cmsmfi8.tfm)
Provides:       tex(cmsmfi8.vf)
Provides:       tex(cmsmfi9.tfm)
Provides:       tex(cmsmfi9.vf)
Provides:       tex(cmsmfxi10.tfm)
Provides:       tex(cmsmfxi10.vf)
Provides:       tex(cmsmfxi12.tfm)
Provides:       tex(cmsmfxi12.vf)
Provides:       tex(cmsmfxi17.tfm)
Provides:       tex(cmsmfxi17.vf)
Provides:       tex(cmsmfxi8.tfm)
Provides:       tex(cmsmfxi8.vf)
Provides:       tex(cmsmfxi9.tfm)
Provides:       tex(cmsmfxi9.vf)
Provides:       tex(cmsmfxicsc10.tfm)
Provides:       tex(cmsmfxicsc10.vf)
Provides:       tex(cmssbsy10.tfm)
Provides:       tex(cmssbsy5.tfm)
Provides:       tex(cmssbsy6.tfm)
Provides:       tex(cmssbsy7.tfm)
Provides:       tex(cmssbsy8.tfm)
Provides:       tex(cmssbsy9.tfm)
Provides:       tex(cmssbxcsc10.tfm)
Provides:       tex(cmsscsc10.tfm)
Provides:       tex(cmsscsc8.tfm)
Provides:       tex(cmsscsc9.tfm)
Provides:       tex(cmsscsci10.tfm)
Provides:       tex(cmsscsci8.tfm)
Provides:       tex(cmsscsci9.tfm)
Provides:       tex(cmssex10.tfm)
Provides:       tex(cmssex7.tfm)
Provides:       tex(cmssex8.tfm)
Provides:       tex(cmssex9.tfm)
Provides:       tex(cmssmi10.tfm)
Provides:       tex(cmssmi5.tfm)
Provides:       tex(cmssmi6.tfm)
Provides:       tex(cmssmi7.tfm)
Provides:       tex(cmssmi8.tfm)
Provides:       tex(cmssmi9.tfm)
Provides:       tex(cmssmib10.tfm)
Provides:       tex(cmssmib5.tfm)
Provides:       tex(cmssmib6.tfm)
Provides:       tex(cmssmib7.tfm)
Provides:       tex(cmssmib8.tfm)
Provides:       tex(cmssmib9.tfm)
Provides:       tex(cmsssy10.tfm)
Provides:       tex(cmsssy5.tfm)
Provides:       tex(cmsssy6.tfm)
Provides:       tex(cmsssy7.tfm)
Provides:       tex(cmsssy8.tfm)
Provides:       tex(cmsssy9.tfm)
Provides:       tex(cmssu10.tfm)
Provides:       tex(cmssxicsc10.tfm)
Provides:       tex(eczi0500.tfm)
Provides:       tex(eczi0600.tfm)
Provides:       tex(eczi0700.tfm)
Provides:       tex(eczi0800.tfm)
Provides:       tex(eczi0900.tfm)
Provides:       tex(eczi1000.tfm)
Provides:       tex(eczi1095.tfm)
Provides:       tex(eczi1200.tfm)
Provides:       tex(eczi1440.tfm)
Provides:       tex(eczi1728.tfm)
Provides:       tex(eczi2074.tfm)
Provides:       tex(eczi2488.tfm)
Provides:       tex(eczi2986.tfm)
Provides:       tex(eczi3583.tfm)
Provides:       tex(eczo0500.tfm)
Provides:       tex(eczo0600.tfm)
Provides:       tex(eczo0700.tfm)
Provides:       tex(eczo0800.tfm)
Provides:       tex(eczo0900.tfm)
Provides:       tex(eczo1000.tfm)
Provides:       tex(eczo1095.tfm)
Provides:       tex(eczo1200.tfm)
Provides:       tex(eczo1440.tfm)
Provides:       tex(eczo1728.tfm)
Provides:       tex(eczo2074.tfm)
Provides:       tex(eczo2488.tfm)
Provides:       tex(eczo2986.tfm)
Provides:       tex(eczo3583.tfm)
Provides:       tex(eczx0500.tfm)
Provides:       tex(eczx0600.tfm)
Provides:       tex(eczx0700.tfm)
Provides:       tex(eczx0800.tfm)
Provides:       tex(eczx0900.tfm)
Provides:       tex(eczx1000.tfm)
Provides:       tex(eczx1095.tfm)
Provides:       tex(eczx1200.tfm)
Provides:       tex(eczx1440.tfm)
Provides:       tex(eczx1728.tfm)
Provides:       tex(eczx2074.tfm)
Provides:       tex(eczx2488.tfm)
Provides:       tex(eczx2986.tfm)
Provides:       tex(eczx3583.tfm)
Provides:       tex(eczz0500.tfm)
Provides:       tex(eczz0600.tfm)
Provides:       tex(eczz0700.tfm)
Provides:       tex(eczz0800.tfm)
Provides:       tex(eczz0900.tfm)
Provides:       tex(eczz1000.tfm)
Provides:       tex(eczz1095.tfm)
Provides:       tex(eczz1200.tfm)
Provides:       tex(eczz1440.tfm)
Provides:       tex(eczz1728.tfm)
Provides:       tex(eczz2074.tfm)
Provides:       tex(eczz2488.tfm)
Provides:       tex(eczz2986.tfm)
Provides:       tex(eczz3583.tfm)
Provides:       tex(omlcmssm.fd)
Provides:       tex(omscmsssy.fd)
Provides:       tex(omxcmssex.fd)
Provides:       tex(ot1cmsmf.fd)
Provides:       tex(ot1xcmss.fd)
Provides:       tex(sansmathfonts.map)
Provides:       tex(sansmathfonts.sty)
Provides:       tex(ssesint10.tfm)
Provides:       tex(ssesint7.tfm)
Provides:       tex(ssesint8.tfm)
Provides:       tex(ssesint9.tfm)
Provides:       tex(ssmsam10.tfm)
Provides:       tex(ssmsam5.tfm)
Provides:       tex(ssmsam6.tfm)
Provides:       tex(ssmsam7.tfm)
Provides:       tex(ssmsam8.tfm)
Provides:       tex(ssmsam9.tfm)
Provides:       tex(ssmsbm10.tfm)
Provides:       tex(ssmsbm5.tfm)
Provides:       tex(ssmsbm6.tfm)
Provides:       tex(ssmsbm7.tfm)
Provides:       tex(ssmsbm8.tfm)
Provides:       tex(ssmsbm9.tfm)
Provides:       tex(t1xcmss.fd)
Provides:       tex(ucmsmf.fd)
Provides:       tex(ussesint.fd)
Provides:       tex(ussmsa.fd)
Provides:       tex(ussmsb.fd)
Provides:       tex(uxcmss.fd)
Requires:       tex(cmss10.tfm)
Requires:       tex(cmss12.tfm)
Requires:       tex(cmss17.tfm)
Requires:       tex(cmss8.tfm)
Requires:       tex(cmss9.tfm)
Requires:       tex(cmssbx10.tfm)
Requires:       tex(cmssi10.tfm)
Requires:       tex(cmssi12.tfm)
Requires:       tex(cmssi17.tfm)
Requires:       tex(cmssi8.tfm)
Requires:       tex(cmssi9.tfm)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source69:       sansmathfonts.tar.xz
Source70:       sansmathfonts.doc.tar.xz

%description -n texlive-sansmathfonts
Sans serif small caps and math fonts for use with Computer
Modern.

date: 2019-04-04 17:50:42 +0000


%package -n texlive-sansmathfonts-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn50756
Release:        0
Summary:        Documentation for texlive-sansmathfonts
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-sansmathfonts-doc
This package includes the documentation for texlive-sansmathfonts


%package -n texlive-sansmathfonts-fonts
Version:        %{texlive_version}.%{texlive_noarch}.svn50756
Release:        0
Summary:        Severed fonts for texlive-sansmathfonts
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Fonts
Url:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-sansmathfonts-fonts
The  separated fonts package for texlive-sansmathfonts
%post -n texlive-sansmathfonts
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap sansmathfonts.map' >> /var/run/texlive/run-updmap

%postun -n texlive-sansmathfonts 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap sansmathfonts.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-sansmathfonts
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-sansmathfonts-fonts
%files -n texlive-sansmathfonts-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/sansmathfonts/README
%{_texmfdistdir}/doc/fonts/sansmathfonts/sansmathfonts.pdf
%{_texmfdistdir}/doc/fonts/sansmathfonts/sansmathfonts.tex

%files -n texlive-sansmathfonts
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/map/dvips/sansmathfonts/sansmathfonts.map
%{_texmfdistdir}/fonts/source/public/sansmathfonts/cmsmfIPiXi10.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/cmsmfIPiXi12.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/cmsmfIPiXi17.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/cmsmfIPiXi8.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/cmsmfIPiXi9.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/cmsmfIPiXibx10.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/cmsmfIPiXibx12.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/cmsmfIPiXibx17.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/cmsmfIPiXibx8.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/cmsmfIPiXibx9.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/cmsmfIPiXibxcsc10.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/cmsmfIPiXicsc10.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/cmsmfIPiXicsc8.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/cmsmfIPiXicsc9.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/cmsmfIPiXicsci10.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/cmsmfIPiXicsci8.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/cmsmfIPiXicsci9.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/cmsmfIPiXii10.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/cmsmfIPiXii12.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/cmsmfIPiXii17.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/cmsmfIPiXii8.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/cmsmfIPiXii9.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/cmsmfIPiXixi10.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/cmsmfIPiXixi12.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/cmsmfIPiXixi17.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/cmsmfIPiXixi8.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/cmsmfIPiXixi9.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/cmsmfIPiXixicsc10.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/cmssbsy10.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/cmssbsy5.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/cmssbsy6.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/cmssbsy7.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/cmssbsy8.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/cmssbsy9.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/cmssbxcsc10.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/cmsscsc10.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/cmsscsc8.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/cmsscsc9.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/cmsscsci10.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/cmsscsci8.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/cmsscsci9.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/cmssex10.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/cmssex7.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/cmssex8.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/cmssex9.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/cmssmi10.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/cmssmi5.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/cmssmi6.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/cmssmi7.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/cmssmi8.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/cmssmi9.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/cmssmib10.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/cmssmib5.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/cmssmib6.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/cmssmib7.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/cmssmib8.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/cmssmib9.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/cmsssy10.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/cmsssy5.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/cmsssy6.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/cmsssy7.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/cmsssy8.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/cmsssy9.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/cmssu10.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/cmssxicsc10.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/eczi.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/eczi0500.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/eczi0600.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/eczi0700.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/eczi0800.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/eczi0900.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/eczi1000.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/eczi1095.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/eczi1200.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/eczi1440.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/eczi1728.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/eczi2074.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/eczi2488.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/eczi2986.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/eczi3583.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/eczo.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/eczo0500.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/eczo0600.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/eczo0700.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/eczo0800.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/eczo0900.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/eczo1000.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/eczo1095.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/eczo1200.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/eczo1440.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/eczo1728.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/eczo2074.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/eczo2488.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/eczo2986.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/eczo3583.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/eczx.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/eczx0500.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/eczx0600.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/eczx0700.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/eczx0800.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/eczx0900.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/eczx1000.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/eczx1095.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/eczx1200.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/eczx1440.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/eczx1728.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/eczx2074.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/eczx2488.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/eczx2986.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/eczx3583.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/eczz.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/eczz0500.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/eczz0600.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/eczz0700.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/eczz0800.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/eczz0900.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/eczz1000.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/eczz1095.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/eczz1200.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/eczz1440.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/eczz1728.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/eczz2074.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/eczz2488.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/eczz2986.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/eczz3583.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/sans-IPiXi.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/sans-IPiXicsc.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/sans-amsya.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/sans-amsyb.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/sans-asymbols.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/sans-bigdel.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/sans-bigint.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/sans-bigop.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/sans-bsymbols.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/sans-calu.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/sans-csc.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/sans-greekl.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/sans-greeku.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/sans-mathex.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/sans-mathint.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/sans-mathsl.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/sans-mathsy.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/sans-roman.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/sans-romanu.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/sans-romms.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/sans-slantms.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/sans-sym.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/sans-symbol.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/sans-xbbold.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/sansfontbase.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/ssesint10.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/ssesint7.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/ssesint8.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/ssesint9.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/ssmsam10.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/ssmsam5.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/ssmsam6.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/ssmsam7.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/ssmsam8.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/ssmsam9.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/ssmsbm10.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/ssmsbm5.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/ssmsbm6.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/ssmsbm7.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/ssmsbm8.mf
%{_texmfdistdir}/fonts/source/public/sansmathfonts/ssmsbm9.mf
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmsmf10.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmsmf12.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmsmf17.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmsmf8.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmsmf9.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmsmfIPiXi10.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmsmfIPiXi12.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmsmfIPiXi17.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmsmfIPiXi8.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmsmfIPiXi9.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmsmfIPiXibx10.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmsmfIPiXibx12.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmsmfIPiXibx17.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmsmfIPiXibx8.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmsmfIPiXibx9.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmsmfIPiXibxcsc10.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmsmfIPiXicsc10.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmsmfIPiXicsc8.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmsmfIPiXicsc9.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmsmfIPiXicsci10.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmsmfIPiXicsci8.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmsmfIPiXicsci9.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmsmfIPiXii10.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmsmfIPiXii12.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmsmfIPiXii17.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmsmfIPiXii8.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmsmfIPiXii9.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmsmfIPiXixi10.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmsmfIPiXixi12.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmsmfIPiXixi17.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmsmfIPiXixi8.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmsmfIPiXixi9.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmsmfIPiXixicsc10.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmsmfbx10.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmsmfbx12.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmsmfbx17.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmsmfbx8.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmsmfbx9.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmsmfbxcsc10.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmsmfcsc10.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmsmfcsc8.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmsmfcsc9.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmsmfcsci10.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmsmfcsci8.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmsmfcsci9.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmsmfi10.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmsmfi12.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmsmfi17.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmsmfi8.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmsmfi9.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmsmfxi10.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmsmfxi12.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmsmfxi17.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmsmfxi8.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmsmfxi9.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmsmfxicsc10.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmssbsy10.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmssbsy5.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmssbsy6.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmssbsy7.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmssbsy8.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmssbsy9.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmssbxcsc10.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmsscsc10.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmsscsc8.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmsscsc9.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmsscsci10.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmsscsci8.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmsscsci9.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmssex10.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmssex7.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmssex8.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmssex9.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmssmi10.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmssmi5.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmssmi6.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmssmi7.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmssmi8.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmssmi9.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmssmib10.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmssmib5.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmssmib6.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmssmib7.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmssmib8.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmssmib9.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmsssy10.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmsssy5.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmsssy6.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmsssy7.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmsssy8.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmsssy9.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmssu10.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/cmssxicsc10.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/eczi0500.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/eczi0600.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/eczi0700.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/eczi0800.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/eczi0900.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/eczi1000.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/eczi1095.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/eczi1200.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/eczi1440.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/eczi1728.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/eczi2074.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/eczi2488.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/eczi2986.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/eczi3583.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/eczo0500.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/eczo0600.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/eczo0700.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/eczo0800.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/eczo0900.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/eczo1000.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/eczo1095.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/eczo1200.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/eczo1440.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/eczo1728.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/eczo2074.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/eczo2488.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/eczo2986.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/eczo3583.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/eczx0500.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/eczx0600.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/eczx0700.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/eczx0800.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/eczx0900.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/eczx1000.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/eczx1095.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/eczx1200.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/eczx1440.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/eczx1728.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/eczx2074.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/eczx2488.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/eczx2986.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/eczx3583.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/eczz0500.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/eczz0600.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/eczz0700.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/eczz0800.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/eczz0900.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/eczz1000.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/eczz1095.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/eczz1200.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/eczz1440.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/eczz1728.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/eczz2074.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/eczz2488.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/eczz2986.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/eczz3583.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/ssesint10.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/ssesint7.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/ssesint8.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/ssesint9.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/ssmsam10.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/ssmsam5.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/ssmsam6.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/ssmsam7.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/ssmsam8.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/ssmsam9.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/ssmsbm10.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/ssmsbm5.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/ssmsbm6.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/ssmsbm7.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/ssmsbm8.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts/ssmsbm9.tfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/cmsmfIPiXi10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/cmsmfIPiXi12.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/cmsmfIPiXi17.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/cmsmfIPiXi8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/cmsmfIPiXi9.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/cmsmfIPiXibx10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/cmsmfIPiXibx12.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/cmsmfIPiXibx17.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/cmsmfIPiXibx8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/cmsmfIPiXibx9.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/cmsmfIPiXibxcsc10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/cmsmfIPiXicsc10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/cmsmfIPiXicsc8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/cmsmfIPiXicsc9.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/cmsmfIPiXicsci10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/cmsmfIPiXicsci8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/cmsmfIPiXicsci9.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/cmsmfIPiXii10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/cmsmfIPiXii12.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/cmsmfIPiXii17.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/cmsmfIPiXii8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/cmsmfIPiXii9.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/cmsmfIPiXixi10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/cmsmfIPiXixi12.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/cmsmfIPiXixi17.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/cmsmfIPiXixi8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/cmsmfIPiXixi9.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/cmsmfIPiXixicsc10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/cmssbsy10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/cmssbsy5.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/cmssbsy6.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/cmssbsy7.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/cmssbsy8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/cmssbsy9.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/cmssbx12.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/cmssbx17.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/cmssbx8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/cmssbx9.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/cmssbxcsc10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/cmsscsc10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/cmsscsc8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/cmsscsc9.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/cmsscsci10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/cmsscsci8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/cmsscsci9.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/cmssex10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/cmssex7.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/cmssex8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/cmssex9.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/cmssmi10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/cmssmi5.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/cmssmi6.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/cmssmi7.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/cmssmi8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/cmssmi9.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/cmssmib10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/cmssmib5.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/cmssmib6.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/cmssmib7.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/cmssmib8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/cmssmib9.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/cmsssy10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/cmsssy5.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/cmsssy6.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/cmsssy7.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/cmsssy8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/cmsssy9.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/cmssu10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/cmssxi10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/cmssxi12.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/cmssxi17.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/cmssxi8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/cmssxi9.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/cmssxicsc10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/eczi0500.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/eczi0600.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/eczi0700.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/eczi0800.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/eczi0900.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/eczi1000.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/eczi1095.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/eczi1200.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/eczi1440.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/eczi1728.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/eczi2074.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/eczi2488.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/eczi2986.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/eczi3583.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/eczo0500.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/eczo0600.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/eczo0700.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/eczo0800.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/eczo0900.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/eczo1000.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/eczo1095.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/eczo1200.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/eczo1440.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/eczo1728.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/eczo2074.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/eczo2488.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/eczo2986.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/eczo3583.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/eczx0500.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/eczx0600.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/eczx0700.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/eczx0800.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/eczx0900.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/eczx1000.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/eczx1095.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/eczx1200.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/eczx1440.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/eczx1728.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/eczx2074.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/eczx2488.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/eczx2986.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/eczx3583.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/eczz0500.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/eczz0600.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/eczz0700.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/eczz0800.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/eczz0900.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/eczz1000.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/eczz1095.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/eczz1200.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/eczz1440.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/eczz1728.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/eczz2074.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/eczz2488.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/eczz2986.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/eczz3583.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/ssesint10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/ssesint7.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/ssesint8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/ssesint9.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/ssmsam10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/ssmsam5.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/ssmsam6.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/ssmsam7.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/ssmsam8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/ssmsam9.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/ssmsbm10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/ssmsbm5.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/ssmsbm6.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/ssmsbm7.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/ssmsbm8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/sansmathfonts/ssmsbm9.pfb
%{_texmfdistdir}/fonts/vf/public/sansmathfonts/cmsmf10.vf
%{_texmfdistdir}/fonts/vf/public/sansmathfonts/cmsmf12.vf
%{_texmfdistdir}/fonts/vf/public/sansmathfonts/cmsmf17.vf
%{_texmfdistdir}/fonts/vf/public/sansmathfonts/cmsmf8.vf
%{_texmfdistdir}/fonts/vf/public/sansmathfonts/cmsmf9.vf
%{_texmfdistdir}/fonts/vf/public/sansmathfonts/cmsmfbx10.vf
%{_texmfdistdir}/fonts/vf/public/sansmathfonts/cmsmfbx12.vf
%{_texmfdistdir}/fonts/vf/public/sansmathfonts/cmsmfbx17.vf
%{_texmfdistdir}/fonts/vf/public/sansmathfonts/cmsmfbx8.vf
%{_texmfdistdir}/fonts/vf/public/sansmathfonts/cmsmfbx9.vf
%{_texmfdistdir}/fonts/vf/public/sansmathfonts/cmsmfbxcsc10.vf
%{_texmfdistdir}/fonts/vf/public/sansmathfonts/cmsmfcsc10.vf
%{_texmfdistdir}/fonts/vf/public/sansmathfonts/cmsmfcsc8.vf
%{_texmfdistdir}/fonts/vf/public/sansmathfonts/cmsmfcsc9.vf
%{_texmfdistdir}/fonts/vf/public/sansmathfonts/cmsmfcsci10.vf
%{_texmfdistdir}/fonts/vf/public/sansmathfonts/cmsmfcsci8.vf
%{_texmfdistdir}/fonts/vf/public/sansmathfonts/cmsmfcsci9.vf
%{_texmfdistdir}/fonts/vf/public/sansmathfonts/cmsmfi10.vf
%{_texmfdistdir}/fonts/vf/public/sansmathfonts/cmsmfi12.vf
%{_texmfdistdir}/fonts/vf/public/sansmathfonts/cmsmfi17.vf
%{_texmfdistdir}/fonts/vf/public/sansmathfonts/cmsmfi8.vf
%{_texmfdistdir}/fonts/vf/public/sansmathfonts/cmsmfi9.vf
%{_texmfdistdir}/fonts/vf/public/sansmathfonts/cmsmfxi10.vf
%{_texmfdistdir}/fonts/vf/public/sansmathfonts/cmsmfxi12.vf
%{_texmfdistdir}/fonts/vf/public/sansmathfonts/cmsmfxi17.vf
%{_texmfdistdir}/fonts/vf/public/sansmathfonts/cmsmfxi8.vf
%{_texmfdistdir}/fonts/vf/public/sansmathfonts/cmsmfxi9.vf
%{_texmfdistdir}/fonts/vf/public/sansmathfonts/cmsmfxicsc10.vf
%{_texmfdistdir}/tex/latex/sansmathfonts/omlcmssm.fd
%{_texmfdistdir}/tex/latex/sansmathfonts/omscmsssy.fd
%{_texmfdistdir}/tex/latex/sansmathfonts/omxcmssex.fd
%{_texmfdistdir}/tex/latex/sansmathfonts/ot1cmsmf.fd
%{_texmfdistdir}/tex/latex/sansmathfonts/ot1xcmss.fd
%{_texmfdistdir}/tex/latex/sansmathfonts/sansmathfonts.sty
%{_texmfdistdir}/tex/latex/sansmathfonts/t1xcmss.fd
%{_texmfdistdir}/tex/latex/sansmathfonts/ucmsmf.fd
%{_texmfdistdir}/tex/latex/sansmathfonts/ussesint.fd
%{_texmfdistdir}/tex/latex/sansmathfonts/ussmsa.fd
%{_texmfdistdir}/tex/latex/sansmathfonts/ussmsb.fd
%{_texmfdistdir}/tex/latex/sansmathfonts/uxcmss.fd

%files -n texlive-sansmathfonts-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-sansmathfonts
%config %{_sysconfdir}/fonts/conf.avail/58-texlive-sansmathfonts.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-sansmathfonts/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-sansmathfonts/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-sansmathfonts/fonts.scale
%{_datadir}/fonts/texlive-sansmathfonts/cmsmfIPiXi10.pfb
%{_datadir}/fonts/texlive-sansmathfonts/cmsmfIPiXi12.pfb
%{_datadir}/fonts/texlive-sansmathfonts/cmsmfIPiXi17.pfb
%{_datadir}/fonts/texlive-sansmathfonts/cmsmfIPiXi8.pfb
%{_datadir}/fonts/texlive-sansmathfonts/cmsmfIPiXi9.pfb
%{_datadir}/fonts/texlive-sansmathfonts/cmsmfIPiXibx10.pfb
%{_datadir}/fonts/texlive-sansmathfonts/cmsmfIPiXibx12.pfb
%{_datadir}/fonts/texlive-sansmathfonts/cmsmfIPiXibx17.pfb
%{_datadir}/fonts/texlive-sansmathfonts/cmsmfIPiXibx8.pfb
%{_datadir}/fonts/texlive-sansmathfonts/cmsmfIPiXibx9.pfb
%{_datadir}/fonts/texlive-sansmathfonts/cmsmfIPiXibxcsc10.pfb
%{_datadir}/fonts/texlive-sansmathfonts/cmsmfIPiXicsc10.pfb
%{_datadir}/fonts/texlive-sansmathfonts/cmsmfIPiXicsc8.pfb
%{_datadir}/fonts/texlive-sansmathfonts/cmsmfIPiXicsc9.pfb
%{_datadir}/fonts/texlive-sansmathfonts/cmsmfIPiXicsci10.pfb
%{_datadir}/fonts/texlive-sansmathfonts/cmsmfIPiXicsci8.pfb
%{_datadir}/fonts/texlive-sansmathfonts/cmsmfIPiXicsci9.pfb
%{_datadir}/fonts/texlive-sansmathfonts/cmsmfIPiXii10.pfb
%{_datadir}/fonts/texlive-sansmathfonts/cmsmfIPiXii12.pfb
%{_datadir}/fonts/texlive-sansmathfonts/cmsmfIPiXii17.pfb
%{_datadir}/fonts/texlive-sansmathfonts/cmsmfIPiXii8.pfb
%{_datadir}/fonts/texlive-sansmathfonts/cmsmfIPiXii9.pfb
%{_datadir}/fonts/texlive-sansmathfonts/cmsmfIPiXixi10.pfb
%{_datadir}/fonts/texlive-sansmathfonts/cmsmfIPiXixi12.pfb
%{_datadir}/fonts/texlive-sansmathfonts/cmsmfIPiXixi17.pfb
%{_datadir}/fonts/texlive-sansmathfonts/cmsmfIPiXixi8.pfb
%{_datadir}/fonts/texlive-sansmathfonts/cmsmfIPiXixi9.pfb
%{_datadir}/fonts/texlive-sansmathfonts/cmsmfIPiXixicsc10.pfb
%{_datadir}/fonts/texlive-sansmathfonts/cmssbsy10.pfb
%{_datadir}/fonts/texlive-sansmathfonts/cmssbsy5.pfb
%{_datadir}/fonts/texlive-sansmathfonts/cmssbsy6.pfb
%{_datadir}/fonts/texlive-sansmathfonts/cmssbsy7.pfb
%{_datadir}/fonts/texlive-sansmathfonts/cmssbsy8.pfb
%{_datadir}/fonts/texlive-sansmathfonts/cmssbsy9.pfb
%{_datadir}/fonts/texlive-sansmathfonts/cmssbx12.pfb
%{_datadir}/fonts/texlive-sansmathfonts/cmssbx17.pfb
%{_datadir}/fonts/texlive-sansmathfonts/cmssbx8.pfb
%{_datadir}/fonts/texlive-sansmathfonts/cmssbx9.pfb
%{_datadir}/fonts/texlive-sansmathfonts/cmssbxcsc10.pfb
%{_datadir}/fonts/texlive-sansmathfonts/cmsscsc10.pfb
%{_datadir}/fonts/texlive-sansmathfonts/cmsscsc8.pfb
%{_datadir}/fonts/texlive-sansmathfonts/cmsscsc9.pfb
%{_datadir}/fonts/texlive-sansmathfonts/cmsscsci10.pfb
%{_datadir}/fonts/texlive-sansmathfonts/cmsscsci8.pfb
%{_datadir}/fonts/texlive-sansmathfonts/cmsscsci9.pfb
%{_datadir}/fonts/texlive-sansmathfonts/cmssex10.pfb
%{_datadir}/fonts/texlive-sansmathfonts/cmssex7.pfb
%{_datadir}/fonts/texlive-sansmathfonts/cmssex8.pfb
%{_datadir}/fonts/texlive-sansmathfonts/cmssex9.pfb
%{_datadir}/fonts/texlive-sansmathfonts/cmssmi10.pfb
%{_datadir}/fonts/texlive-sansmathfonts/cmssmi5.pfb
%{_datadir}/fonts/texlive-sansmathfonts/cmssmi6.pfb
%{_datadir}/fonts/texlive-sansmathfonts/cmssmi7.pfb
%{_datadir}/fonts/texlive-sansmathfonts/cmssmi8.pfb
%{_datadir}/fonts/texlive-sansmathfonts/cmssmi9.pfb
%{_datadir}/fonts/texlive-sansmathfonts/cmssmib10.pfb
%{_datadir}/fonts/texlive-sansmathfonts/cmssmib5.pfb
%{_datadir}/fonts/texlive-sansmathfonts/cmssmib6.pfb
%{_datadir}/fonts/texlive-sansmathfonts/cmssmib7.pfb
%{_datadir}/fonts/texlive-sansmathfonts/cmssmib8.pfb
%{_datadir}/fonts/texlive-sansmathfonts/cmssmib9.pfb
%{_datadir}/fonts/texlive-sansmathfonts/cmsssy10.pfb
%{_datadir}/fonts/texlive-sansmathfonts/cmsssy5.pfb
%{_datadir}/fonts/texlive-sansmathfonts/cmsssy6.pfb
%{_datadir}/fonts/texlive-sansmathfonts/cmsssy7.pfb
%{_datadir}/fonts/texlive-sansmathfonts/cmsssy8.pfb
%{_datadir}/fonts/texlive-sansmathfonts/cmsssy9.pfb
%{_datadir}/fonts/texlive-sansmathfonts/cmssu10.pfb
%{_datadir}/fonts/texlive-sansmathfonts/cmssxi10.pfb
%{_datadir}/fonts/texlive-sansmathfonts/cmssxi12.pfb
%{_datadir}/fonts/texlive-sansmathfonts/cmssxi17.pfb
%{_datadir}/fonts/texlive-sansmathfonts/cmssxi8.pfb
%{_datadir}/fonts/texlive-sansmathfonts/cmssxi9.pfb
%{_datadir}/fonts/texlive-sansmathfonts/cmssxicsc10.pfb
%{_datadir}/fonts/texlive-sansmathfonts/eczi0500.pfb
%{_datadir}/fonts/texlive-sansmathfonts/eczi0600.pfb
%{_datadir}/fonts/texlive-sansmathfonts/eczi0700.pfb
%{_datadir}/fonts/texlive-sansmathfonts/eczi0800.pfb
%{_datadir}/fonts/texlive-sansmathfonts/eczi0900.pfb
%{_datadir}/fonts/texlive-sansmathfonts/eczi1000.pfb
%{_datadir}/fonts/texlive-sansmathfonts/eczi1095.pfb
%{_datadir}/fonts/texlive-sansmathfonts/eczi1200.pfb
%{_datadir}/fonts/texlive-sansmathfonts/eczi1440.pfb
%{_datadir}/fonts/texlive-sansmathfonts/eczi1728.pfb
%{_datadir}/fonts/texlive-sansmathfonts/eczi2074.pfb
%{_datadir}/fonts/texlive-sansmathfonts/eczi2488.pfb
%{_datadir}/fonts/texlive-sansmathfonts/eczi2986.pfb
%{_datadir}/fonts/texlive-sansmathfonts/eczi3583.pfb
%{_datadir}/fonts/texlive-sansmathfonts/eczo0500.pfb
%{_datadir}/fonts/texlive-sansmathfonts/eczo0600.pfb
%{_datadir}/fonts/texlive-sansmathfonts/eczo0700.pfb
%{_datadir}/fonts/texlive-sansmathfonts/eczo0800.pfb
%{_datadir}/fonts/texlive-sansmathfonts/eczo0900.pfb
%{_datadir}/fonts/texlive-sansmathfonts/eczo1000.pfb
%{_datadir}/fonts/texlive-sansmathfonts/eczo1095.pfb
%{_datadir}/fonts/texlive-sansmathfonts/eczo1200.pfb
%{_datadir}/fonts/texlive-sansmathfonts/eczo1440.pfb
%{_datadir}/fonts/texlive-sansmathfonts/eczo1728.pfb
%{_datadir}/fonts/texlive-sansmathfonts/eczo2074.pfb
%{_datadir}/fonts/texlive-sansmathfonts/eczo2488.pfb
%{_datadir}/fonts/texlive-sansmathfonts/eczo2986.pfb
%{_datadir}/fonts/texlive-sansmathfonts/eczo3583.pfb
%{_datadir}/fonts/texlive-sansmathfonts/eczx0500.pfb
%{_datadir}/fonts/texlive-sansmathfonts/eczx0600.pfb
%{_datadir}/fonts/texlive-sansmathfonts/eczx0700.pfb
%{_datadir}/fonts/texlive-sansmathfonts/eczx0800.pfb
%{_datadir}/fonts/texlive-sansmathfonts/eczx0900.pfb
%{_datadir}/fonts/texlive-sansmathfonts/eczx1000.pfb
%{_datadir}/fonts/texlive-sansmathfonts/eczx1095.pfb
%{_datadir}/fonts/texlive-sansmathfonts/eczx1200.pfb
%{_datadir}/fonts/texlive-sansmathfonts/eczx1440.pfb
%{_datadir}/fonts/texlive-sansmathfonts/eczx1728.pfb
%{_datadir}/fonts/texlive-sansmathfonts/eczx2074.pfb
%{_datadir}/fonts/texlive-sansmathfonts/eczx2488.pfb
%{_datadir}/fonts/texlive-sansmathfonts/eczx2986.pfb
%{_datadir}/fonts/texlive-sansmathfonts/eczx3583.pfb
%{_datadir}/fonts/texlive-sansmathfonts/eczz0500.pfb
%{_datadir}/fonts/texlive-sansmathfonts/eczz0600.pfb
%{_datadir}/fonts/texlive-sansmathfonts/eczz0700.pfb
%{_datadir}/fonts/texlive-sansmathfonts/eczz0800.pfb
%{_datadir}/fonts/texlive-sansmathfonts/eczz0900.pfb
%{_datadir}/fonts/texlive-sansmathfonts/eczz1000.pfb
%{_datadir}/fonts/texlive-sansmathfonts/eczz1095.pfb
%{_datadir}/fonts/texlive-sansmathfonts/eczz1200.pfb
%{_datadir}/fonts/texlive-sansmathfonts/eczz1440.pfb
%{_datadir}/fonts/texlive-sansmathfonts/eczz1728.pfb
%{_datadir}/fonts/texlive-sansmathfonts/eczz2074.pfb
%{_datadir}/fonts/texlive-sansmathfonts/eczz2488.pfb
%{_datadir}/fonts/texlive-sansmathfonts/eczz2986.pfb
%{_datadir}/fonts/texlive-sansmathfonts/eczz3583.pfb
%{_datadir}/fonts/texlive-sansmathfonts/ssesint10.pfb
%{_datadir}/fonts/texlive-sansmathfonts/ssesint7.pfb
%{_datadir}/fonts/texlive-sansmathfonts/ssesint8.pfb
%{_datadir}/fonts/texlive-sansmathfonts/ssesint9.pfb
%{_datadir}/fonts/texlive-sansmathfonts/ssmsam10.pfb
%{_datadir}/fonts/texlive-sansmathfonts/ssmsam5.pfb
%{_datadir}/fonts/texlive-sansmathfonts/ssmsam6.pfb
%{_datadir}/fonts/texlive-sansmathfonts/ssmsam7.pfb
%{_datadir}/fonts/texlive-sansmathfonts/ssmsam8.pfb
%{_datadir}/fonts/texlive-sansmathfonts/ssmsam9.pfb
%{_datadir}/fonts/texlive-sansmathfonts/ssmsbm10.pfb
%{_datadir}/fonts/texlive-sansmathfonts/ssmsbm5.pfb
%{_datadir}/fonts/texlive-sansmathfonts/ssmsbm6.pfb
%{_datadir}/fonts/texlive-sansmathfonts/ssmsbm7.pfb
%{_datadir}/fonts/texlive-sansmathfonts/ssmsbm8.pfb
%{_datadir}/fonts/texlive-sansmathfonts/ssmsbm9.pfb
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-sansmathfonts-fonts-%{texlive_version}.%{texlive_noarch}.svn50756-%{release}-zypper
%endif

%package -n texlive-sapthesis
Version:        %{texlive_version}.%{texlive_noarch}.4.1svn48365
Release:        0
Summary:        Typeset theses for Sapienza-University, Rome
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-sapthesis-doc >= %{texlive_version}
Provides:       tex(sapthesis.cls)
Requires:       tex(amsmath.sty)
Requires:       tex(book.cls)
Requires:       tex(booktabs.sty)
Requires:       tex(caption.sty)
Requires:       tex(color.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(fancyhdr.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(geometry.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(lmodern.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xltxtra.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source71:       sapthesis.tar.xz
Source72:       sapthesis.doc.tar.xz

%description -n texlive-sapthesis
The class will typeset Ph.D., Master, and Bachelor theses that
adhere to the publishing guidelines of the Sapienza-University
of Rome.

date: 2018-08-07 06:46:21 +0000


%package -n texlive-sapthesis-doc
Version:        %{texlive_version}.%{texlive_noarch}.4.1svn48365
Release:        0
Summary:        Documentation for texlive-sapthesis
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-sapthesis-doc
This package includes the documentation for texlive-sapthesis

%post -n texlive-sapthesis
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-sapthesis 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-sapthesis
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-sapthesis-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/sapthesis/README
%{_texmfdistdir}/doc/latex/sapthesis/examples/Laurea.tex
%{_texmfdistdir}/doc/latex/sapthesis/examples/LaureaMagistrale.tex
%{_texmfdistdir}/doc/latex/sapthesis/examples/LaureaMagistrale_eng.tex
%{_texmfdistdir}/doc/latex/sapthesis/examples/LaureaMagistrale_ita.tex
%{_texmfdistdir}/doc/latex/sapthesis/examples/Laurea_ita.tex
%{_texmfdistdir}/doc/latex/sapthesis/examples/Master.tex
%{_texmfdistdir}/doc/latex/sapthesis/examples/PhD.tex
%{_texmfdistdir}/doc/latex/sapthesis/examples/Specialization.tex
%{_texmfdistdir}/doc/latex/sapthesis/examples/TFA.tex
%{_texmfdistdir}/doc/latex/sapthesis/sapthesis-doc.pdf
%{_texmfdistdir}/doc/latex/sapthesis/sapthesis-doc.tex
%{_texmfdistdir}/doc/latex/sapthesis/sapthesis.layout

%files -n texlive-sapthesis
%defattr(-,root,root,755)
%{_texmfdistdir}/bibtex/bst/sapthesis/sapthesis.bst
%{_texmfdistdir}/tex/latex/sapthesis/sapienza-MLblack-pos.pdf
%{_texmfdistdir}/tex/latex/sapthesis/sapienza-MLred-pos.pdf
%{_texmfdistdir}/tex/latex/sapthesis/sapthesis.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-sapthesis-%{texlive_version}.%{texlive_noarch}.4.1svn48365-%{release}-zypper
%endif

%package -n texlive-sasnrdisplay
Version:        %{texlive_version}.%{texlive_noarch}.0.0.95svn45963
Release:        0
Summary:        Typeset SAS or R code or output
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-sasnrdisplay-doc >= %{texlive_version}
Provides:       tex(SASnRdisplay.cfg)
Provides:       tex(SASnRdisplay.sty)
Requires:       tex(caption.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(listings.sty)
Requires:       tex(needspace.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source73:       sasnrdisplay.tar.xz
Source74:       sasnrdisplay.doc.tar.xz

%description -n texlive-sasnrdisplay
The SASnRdisplay package serves as a front-end to listings,
which permits statisticians and others to import source code
and the results of their calculations or simulations into LaTeX
projects. The package is also capable of overloading the Sweave
and SASweave packages.

date: 2018-04-22 06:20:41 +0000


%package -n texlive-sasnrdisplay-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.95svn45963
Release:        0
Summary:        Documentation for texlive-sasnrdisplay
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-sasnrdisplay-doc
This package includes the documentation for texlive-sasnrdisplay

%post -n texlive-sasnrdisplay
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-sasnrdisplay 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-sasnrdisplay
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-sasnrdisplay-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/sasnrdisplay/README
%{_texmfdistdir}/doc/latex/sasnrdisplay/SASnRdisplay.pdf
%{_texmfdistdir}/doc/latex/sasnrdisplay/SASnRdisplay.tex

%files -n texlive-sasnrdisplay
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/sasnrdisplay/SASnRdisplay.cfg
%{_texmfdistdir}/tex/latex/sasnrdisplay/SASnRdisplay.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-sasnrdisplay-%{texlive_version}.%{texlive_noarch}.0.0.95svn45963-%{release}-zypper
%endif

%package -n texlive-sauerj
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        A bundle of utilities by Jonathan Sauer
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-sauerj-doc >= %{texlive_version}
Provides:       tex(collect.sty)
Provides:       tex(metainfo.sty)
Provides:       tex(optparams.sty)
Provides:       tex(parcolumns.sty)
Provides:       tex(processkv.sty)
Provides:       tex(zahl2string.sty)
Requires:       tex(keyval.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source75:       sauerj.tar.xz
Source76:       sauerj.doc.tar.xz

%description -n texlive-sauerj
The bundle consists of: a tool for collecting text for later
re-use, a tool for typesetting the "meta-information" within a
text, a tool for use in constructing macros with multiple
optional parameters, a package for multiple column parallel
texts, a tool for processing key-value structured lists, and
macros for typesetting a number as a German-language string.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-sauerj-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Documentation for texlive-sauerj
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-sauerj-doc
This package includes the documentation for texlive-sauerj

%post -n texlive-sauerj
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-sauerj 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-sauerj
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-sauerj-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/sauerj/README
%{_texmfdistdir}/doc/latex/sauerj/collect.pdf
%{_texmfdistdir}/doc/latex/sauerj/metainfo.pdf
%{_texmfdistdir}/doc/latex/sauerj/optparams.pdf
%{_texmfdistdir}/doc/latex/sauerj/parcolumns.pdf
%{_texmfdistdir}/doc/latex/sauerj/processkv.pdf
%{_texmfdistdir}/doc/latex/sauerj/zahl2string.pdf

%files -n texlive-sauerj
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/sauerj/collect.sty
%{_texmfdistdir}/tex/latex/sauerj/metainfo.sty
%{_texmfdistdir}/tex/latex/sauerj/optparams.sty
%{_texmfdistdir}/tex/latex/sauerj/parcolumns.sty
%{_texmfdistdir}/tex/latex/sauerj/processkv.sty
%{_texmfdistdir}/tex/latex/sauerj/zahl2string.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-sauerj-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif

%package -n texlive-sauter
Version:        %{texlive_version}.%{texlive_noarch}.2.4svn13293
Release:        0
Summary:        Wide range of design sizes for CM fonts
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source77:       sauter.tar.xz

%description -n texlive-sauter
Extensions, originally to the CM fonts, providing a
parameterization scheme to build Metafont fonts at true design
sizes, for a large range of sizes. The scheme has now been
extended to a range of other fonts, including the AMS fonts,
bbm, bbold, rsfs and wasy fonts.

date: 2016-06-24 17:18:15 +0000

%post -n texlive-sauter
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-sauter 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-sauter
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-sauter
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/source/public/sauter/b-cmb.mf
%{_texmfdistdir}/fonts/source/public/sauter/b-cmbsy.mf
%{_texmfdistdir}/fonts/source/public/sauter/b-cmbx.mf
%{_texmfdistdir}/fonts/source/public/sauter/b-cmbxsl.mf
%{_texmfdistdir}/fonts/source/public/sauter/b-cmbxti.mf
%{_texmfdistdir}/fonts/source/public/sauter/b-cmcsc.mf
%{_texmfdistdir}/fonts/source/public/sauter/b-cmdunh.mf
%{_texmfdistdir}/fonts/source/public/sauter/b-cmex.mf
%{_texmfdistdir}/fonts/source/public/sauter/b-cmff.mf
%{_texmfdistdir}/fonts/source/public/sauter/b-cmfi.mf
%{_texmfdistdir}/fonts/source/public/sauter/b-cmfib.mf
%{_texmfdistdir}/fonts/source/public/sauter/b-cminch.mf
%{_texmfdistdir}/fonts/source/public/sauter/b-cmitt.mf
%{_texmfdistdir}/fonts/source/public/sauter/b-cmmi.mf
%{_texmfdistdir}/fonts/source/public/sauter/b-cmmib.mf
%{_texmfdistdir}/fonts/source/public/sauter/b-cmr.mf
%{_texmfdistdir}/fonts/source/public/sauter/b-cmsl.mf
%{_texmfdistdir}/fonts/source/public/sauter/b-cmsltt.mf
%{_texmfdistdir}/fonts/source/public/sauter/b-cmss.mf
%{_texmfdistdir}/fonts/source/public/sauter/b-cmssbx.mf
%{_texmfdistdir}/fonts/source/public/sauter/b-cmssdc.mf
%{_texmfdistdir}/fonts/source/public/sauter/b-cmssi.mf
%{_texmfdistdir}/fonts/source/public/sauter/b-cmssq.mf
%{_texmfdistdir}/fonts/source/public/sauter/b-cmssqi.mf
%{_texmfdistdir}/fonts/source/public/sauter/b-cmssxi.mf
%{_texmfdistdir}/fonts/source/public/sauter/b-cmsy.mf
%{_texmfdistdir}/fonts/source/public/sauter/b-cmtcsc.mf
%{_texmfdistdir}/fonts/source/public/sauter/b-cmtex.mf
%{_texmfdistdir}/fonts/source/public/sauter/b-cmti.mf
%{_texmfdistdir}/fonts/source/public/sauter/b-cmtt.mf
%{_texmfdistdir}/fonts/source/public/sauter/b-cmu.mf
%{_texmfdistdir}/fonts/source/public/sauter/b-cmvtt.mf
%{_texmfdistdir}/fonts/source/public/sauter/c-bmath.mf
%{_texmfdistdir}/fonts/source/public/sauter/c-cmbx.mf
%{_texmfdistdir}/fonts/source/public/sauter/c-cmex.mf
%{_texmfdistdir}/fonts/source/public/sauter/c-cmff.mf
%{_texmfdistdir}/fonts/source/public/sauter/c-cmmi.mf
%{_texmfdistdir}/fonts/source/public/sauter/c-cmr.mf
%{_texmfdistdir}/fonts/source/public/sauter/c-cmss.mf
%{_texmfdistdir}/fonts/source/public/sauter/c-cmssbx.mf
%{_texmfdistdir}/fonts/source/public/sauter/c-cmssq.mf
%{_texmfdistdir}/fonts/source/public/sauter/c-cmsy.mf
%{_texmfdistdir}/fonts/source/public/sauter/c-cmti.mf
%{_texmfdistdir}/fonts/source/public/sauter/c-cmtt.mf
%{_texmfdistdir}/fonts/source/public/sauter/c-sigma.mf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-sauter-%{texlive_version}.%{texlive_noarch}.2.4svn13293-%{release}-zypper
%endif

%package -n texlive-sauterfonts
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Use Sauter's fonts in LaTeX
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-sauterfonts-doc >= %{texlive_version}
Provides:       tex(sbbm.sty)
Provides:       tex(sexscale.sty)
Provides:       tex(somlcmm.fd)
Provides:       tex(somlcmr.fd)
Provides:       tex(somscmr.fd)
Provides:       tex(somscmsy.fd)
Provides:       tex(somxcmex.fd)
Provides:       tex(sot1cmdh.fd)
Provides:       tex(sot1cmfib.fd)
Provides:       tex(sot1cmfr.fd)
Provides:       tex(sot1cmr.fd)
Provides:       tex(sot1cmss.fd)
Provides:       tex(sot1cmtt.fd)
Provides:       tex(sot1cmvtt.fd)
Provides:       tex(subbm.fd)
Provides:       tex(subbmdh.fd)
Provides:       tex(subbmfib.fd)
Provides:       tex(subbmss.fd)
Provides:       tex(subbmtt.fd)
Provides:       tex(subbmvtt.fd)
Provides:       tex(subbold.fd)
Provides:       tex(sucmr.fd)
Provides:       tex(sucmss.fd)
Provides:       tex(sucmtt.fd)
Provides:       tex(sulasy.fd)
Provides:       tex(sumsa.fd)
Provides:       tex(sumsb.fd)
Provides:       tex(sursfs.fd)
Provides:       tex(sustmry.fd)
Provides:       tex(suwasy.fd)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source78:       sauterfonts.tar.xz
Source79:       sauterfonts.doc.tar.xz

%description -n texlive-sauterfonts
The package provides font definition files (plus a replacement
for the package exscale) to access many of the fonts in
Sauter's collection. These fonts are available in all point
sizes and look nicer for such "intermediate" document sizes as
11pt. Also included is the package sbbm, an alternative to
access the bbm fonts.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-sauterfonts-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Documentation for texlive-sauterfonts
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-sauterfonts-doc
This package includes the documentation for texlive-sauterfonts

%post -n texlive-sauterfonts
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-sauterfonts 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-sauterfonts
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-sauterfonts-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/sauterfonts/README

%files -n texlive-sauterfonts
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/sauterfonts/sbbm.sty
%{_texmfdistdir}/tex/latex/sauterfonts/sexscale.sty
%{_texmfdistdir}/tex/latex/sauterfonts/somlcmm.fd
%{_texmfdistdir}/tex/latex/sauterfonts/somlcmr.fd
%{_texmfdistdir}/tex/latex/sauterfonts/somscmr.fd
%{_texmfdistdir}/tex/latex/sauterfonts/somscmsy.fd
%{_texmfdistdir}/tex/latex/sauterfonts/somxcmex.fd
%{_texmfdistdir}/tex/latex/sauterfonts/sot1cmdh.fd
%{_texmfdistdir}/tex/latex/sauterfonts/sot1cmfib.fd
%{_texmfdistdir}/tex/latex/sauterfonts/sot1cmfr.fd
%{_texmfdistdir}/tex/latex/sauterfonts/sot1cmr.fd
%{_texmfdistdir}/tex/latex/sauterfonts/sot1cmss.fd
%{_texmfdistdir}/tex/latex/sauterfonts/sot1cmtt.fd
%{_texmfdistdir}/tex/latex/sauterfonts/sot1cmvtt.fd
%{_texmfdistdir}/tex/latex/sauterfonts/subbm.fd
%{_texmfdistdir}/tex/latex/sauterfonts/subbmdh.fd
%{_texmfdistdir}/tex/latex/sauterfonts/subbmfib.fd
%{_texmfdistdir}/tex/latex/sauterfonts/subbmss.fd
%{_texmfdistdir}/tex/latex/sauterfonts/subbmtt.fd
%{_texmfdistdir}/tex/latex/sauterfonts/subbmvtt.fd
%{_texmfdistdir}/tex/latex/sauterfonts/subbold.fd
%{_texmfdistdir}/tex/latex/sauterfonts/sucmr.fd
%{_texmfdistdir}/tex/latex/sauterfonts/sucmss.fd
%{_texmfdistdir}/tex/latex/sauterfonts/sucmtt.fd
%{_texmfdistdir}/tex/latex/sauterfonts/sulasy.fd
%{_texmfdistdir}/tex/latex/sauterfonts/sumsa.fd
%{_texmfdistdir}/tex/latex/sauterfonts/sumsb.fd
%{_texmfdistdir}/tex/latex/sauterfonts/sursfs.fd
%{_texmfdistdir}/tex/latex/sauterfonts/sustmry.fd
%{_texmfdistdir}/tex/latex/sauterfonts/suwasy.fd
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-sauterfonts-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif

%package -n texlive-savefnmark
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn15878
Release:        0
Summary:        Save name of the footnote mark for reuse
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-savefnmark-doc >= %{texlive_version}
Provides:       tex(savefnmark.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source80:       savefnmark.tar.xz
Source81:       savefnmark.doc.tar.xz

%description -n texlive-savefnmark
Sometimes the same footnote applies to more than one location
in a table. With this package the mark of a footnote can be
saved into a name, and re-used subsequently without creating
another footnote at the bottom.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-savefnmark-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn15878
Release:        0
Summary:        Documentation for texlive-savefnmark
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-savefnmark-doc
This package includes the documentation for texlive-savefnmark

%post -n texlive-savefnmark
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-savefnmark 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-savefnmark
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-savefnmark-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/savefnmark/savefnmark.pdf

%files -n texlive-savefnmark
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/savefnmark/savefnmark.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-savefnmark-%{texlive_version}.%{texlive_noarch}.1.0svn15878-%{release}-zypper
%endif

%package -n texlive-savesym
Version:        %{texlive_version}.%{texlive_noarch}.1.2svn31565
Release:        0
Summary:        Redefine symbols where names conflict
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Provides:       tex(savesym.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source82:       savesym.tar.xz

%description -n texlive-savesym
There are a number of symbols (e.g., \Square) that are defined
by several packages. In order to typeset all the variants in a
document, we have to give the glyph a unique name. To do that,
we define \savesymbol{XXX}, which renames a symbol from \XXX to
\origXXX, and \restoresymbols{yyy}{XXX}, which renames \origXXX
back to \XXX and defines a new command, \yyyXXX, which
corresponds to the most recently loaded version of \XXX.

date: 2016-06-24 17:18:15 +0000

%post -n texlive-savesym
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-savesym 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-savesym
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-savesym
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/savesym/savesym.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-savesym-%{texlive_version}.%{texlive_noarch}.1.2svn31565-%{release}-zypper
%endif

%package -n texlive-savetrees
Version:        %{texlive_version}.%{texlive_noarch}.2.4svn40525
Release:        0
Summary:        Optimise the use of each page of a LaTeX document
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-savetrees-doc >= %{texlive_version}
Provides:       tex(savetrees.bbx)
Provides:       tex(savetrees.cbx)
Provides:       tex(savetrees.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(numeric-comp.bbx)
Requires:       tex(numeric-comp.cbx)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source83:       savetrees.tar.xz
Source84:       savetrees.doc.tar.xz

%description -n texlive-savetrees
The goal of the savetrees package is to pack as much text as
possible onto each page of a LaTeX document. Admittedly, this
makes the document far less attractive. Nevertheless, savetrees
is a simple way to save paper when printing draft copies of a
document. It can also be useful when trying to meet a tight
page-length requirement for a conference or journal submission.
Most of the package options cover specific modifications to
typesetting rules, but there are also options subtle, moderate
and extreme options for the "broad brush" approach.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-savetrees-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.4svn40525
Release:        0
Summary:        Documentation for texlive-savetrees
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-savetrees-doc
This package includes the documentation for texlive-savetrees

%post -n texlive-savetrees
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-savetrees 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-savetrees
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-savetrees-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/savetrees/README
%{_texmfdistdir}/doc/latex/savetrees/savetrees.pdf
%{_texmfdistdir}/doc/latex/savetrees/st-sample2e.pdf

%files -n texlive-savetrees
%defattr(-,root,root,755)
%{_texmfdistdir}/bibtex/bst/savetrees/savetrees.bst
%{_texmfdistdir}/tex/latex/savetrees/savetrees.bbx
%{_texmfdistdir}/tex/latex/savetrees/savetrees.cbx
%{_texmfdistdir}/tex/latex/savetrees/savetrees.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-savetrees-%{texlive_version}.%{texlive_noarch}.2.4svn40525-%{release}-zypper
%endif

%package -n texlive-scale
Version:        %{texlive_version}.%{texlive_noarch}.1.1.2svn15878
Release:        0
Summary:        Scale document by sqrt(2) or magstep(2)
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-scale-doc >= %{texlive_version}
Provides:       tex(scale.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source85:       scale.tar.xz
Source86:       scale.doc.tar.xz

%description -n texlive-scale
A package to scale a document by sqrt(2) (or by \magstep{2}).
This is useful if you are preparing a document on, for example,
A5 paper and want to print on A4 paper to achieve a better
resolution.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-scale-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1.2svn15878
Release:        0
Summary:        Documentation for texlive-scale
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-scale-doc
This package includes the documentation for texlive-scale

%post -n texlive-scale
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-scale 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-scale
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-scale-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/scale/COPYING
%{_texmfdistdir}/doc/latex/scale/README

%files -n texlive-scale
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/scale/scale.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-scale-%{texlive_version}.%{texlive_noarch}.1.1.2svn15878-%{release}-zypper
%endif

%package -n texlive-scalebar
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn15878
Release:        0
Summary:        Create scalebars for maps, diagrams or photos
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-scalebar-doc >= %{texlive_version}
Provides:       tex(scalebar.sty)
Requires:       tex(calc.sty)
Requires:       tex(fp.sty)
Requires:       tex(ifthen.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source87:       scalebar.tar.xz
Source88:       scalebar.doc.tar.xz

%description -n texlive-scalebar
This is a small package to create scalebars for maps, diagrams
or photos. It was designed for use with cave maps but can be
used for anything from showing a scalebar in kilometres for
topographic maps to a scalebar in micrometres for an electron
microscope image.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-scalebar-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn15878
Release:        0
Summary:        Documentation for texlive-scalebar
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-scalebar-doc
This package includes the documentation for texlive-scalebar

%post -n texlive-scalebar
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-scalebar 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-scalebar
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-scalebar-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/scalebar/README
%{_texmfdistdir}/doc/latex/scalebar/scalebar_examples.pdf
%{_texmfdistdir}/doc/latex/scalebar/scalebar_examples.tex

%files -n texlive-scalebar
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/scalebar/scalebar.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-scalebar-%{texlive_version}.%{texlive_noarch}.1.0svn15878-%{release}-zypper
%endif

%package -n texlive-scalerel
Version:        %{texlive_version}.%{texlive_noarch}.1.8svn42809
Release:        0
Summary:        Constrained scaling and stretching of objects
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-scalerel-doc >= %{texlive_version}
Provides:       tex(scalerel.sty)
Requires:       tex(calc.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(graphicx.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source89:       scalerel.tar.xz
Source90:       scalerel.doc.tar.xz

%description -n texlive-scalerel
The package provides four commands for vertically scaling and
stretching objects. Its primary function is the ability to
scale/stretch and shift one object to conform to the size of a
specified second object. This feature can be useful in both
equations and schematic diagrams. Additionally, the scaling and
stretching commands offer constraints on maximum width and/or
minimum aspect ratio, which are often used to preserve
legibility or for the sake of general appearance.

date: 2016-12-29 15:00:53 +0000


%package -n texlive-scalerel-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.8svn42809
Release:        0
Summary:        Documentation for texlive-scalerel
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-scalerel-doc
This package includes the documentation for texlive-scalerel

%post -n texlive-scalerel
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-scalerel 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-scalerel
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-scalerel-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/scalerel/README
%{_texmfdistdir}/doc/latex/scalerel/scalerel.pdf
%{_texmfdistdir}/doc/latex/scalerel/scalerel.tex

%files -n texlive-scalerel
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/scalerel/scalerel.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-scalerel-%{texlive_version}.%{texlive_noarch}.1.8svn42809-%{release}-zypper
%endif

%package -n texlive-scanpages
Version:        %{texlive_version}.%{texlive_noarch}.1.05asvn42633
Release:        0
Summary:        Support importing and embellishing scanned documents
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(updmap.cfg)
#!BuildIgnore:  tex(updmap.cfg)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(updmap.cfg)
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires:       texlive-scanpages-fonts >= %{texlive_version}
Recommends:     texlive-scanpages-doc >= %{texlive_version}
Provides:       tex(scanpages.map)
Provides:       tex(scanpages.sty)
Provides:       tex(scanwipe.tfm)
Provides:       tex(uscanwipe.fd)
Requires:       tex(etoolbox.sty)
Requires:       tex(fp-basic.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(pgffor.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source91:       scanpages.tar.xz
Source92:       scanpages.doc.tar.xz

%description -n texlive-scanpages
The bundle provides support for the process of creating
documents based on pre-TeX-era material that is available as
scanned pages, only.

date: 2016-12-02 21:31:43 +0000


%package -n texlive-scanpages-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.05asvn42633
Release:        0
Summary:        Documentation for texlive-scanpages
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-scanpages-doc
This package includes the documentation for texlive-scanpages


%package -n texlive-scanpages-fonts
Version:        %{texlive_version}.%{texlive_noarch}.1.05asvn42633
Release:        0
Summary:        Severed fonts for texlive-scanpages
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Fonts
Url:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-scanpages-fonts
The  separated fonts package for texlive-scanpages
%post -n texlive-scanpages
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap scanpages.map' >> /var/run/texlive/run-updmap

%postun -n texlive-scanpages 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap scanpages.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-scanpages
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-scanpages-fonts
%files -n texlive-scanpages-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/scanpages/README
%{_texmfdistdir}/doc/latex/scanpages/pic1.pdf
%{_texmfdistdir}/doc/latex/scanpages/pic2.pdf
%{_texmfdistdir}/doc/latex/scanpages/replicate.plist
%{_texmfdistdir}/doc/latex/scanpages/replicate.py
%{_texmfdistdir}/doc/latex/scanpages/scanpages-doc.pdf
%{_texmfdistdir}/doc/latex/scanpages/scanpages-doc.tex

%files -n texlive-scanpages
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/map/dvips/scanpages/scanpages.map
%{_texmfdistdir}/fonts/tfm/public/scanpages/scanwipe.tfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/scanpages/scanwipe.pfb
%{_texmfdistdir}/tex/latex/scanpages/scanpages.sty
%{_texmfdistdir}/tex/latex/scanpages/uscanwipe.fd

%files -n texlive-scanpages-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-scanpages
%config %{_sysconfdir}/fonts/conf.avail/58-texlive-scanpages.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-scanpages/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-scanpages/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-scanpages/fonts.scale
%{_datadir}/fonts/texlive-scanpages/scanwipe.pfb
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-scanpages-fonts-%{texlive_version}.%{texlive_noarch}.1.05asvn42633-%{release}-zypper
%endif

%package -n texlive-schemabloc
Version:        %{texlive_version}.%{texlive_noarch}.1.5svn15878
Release:        0
Summary:        Draw block diagrams, using TikZ
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-schemabloc-doc >= %{texlive_version}
Provides:       tex(schemabloc.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(tikz.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source93:       schemabloc.tar.xz
Source94:       schemabloc.doc.tar.xz

%description -n texlive-schemabloc
The package provides a set of macros for constructing block
diagrams, using TikZ. (The blox package is an "English
translation" of this package.)

date: 2016-06-24 17:18:15 +0000


%package -n texlive-schemabloc-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.5svn15878
Release:        0
Summary:        Documentation for texlive-schemabloc
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Provides:       locale(texlive-schemabloc-doc:fr)

%description -n texlive-schemabloc-doc
This package includes the documentation for texlive-schemabloc

%post -n texlive-schemabloc
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-schemabloc 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-schemabloc
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-schemabloc-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/schemabloc/README
%{_texmfdistdir}/doc/latex/schemabloc/schemabloc.pdf
%{_texmfdistdir}/doc/latex/schemabloc/schemabloc.tex

%files -n texlive-schemabloc
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/schemabloc/schemabloc.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-schemabloc-%{texlive_version}.%{texlive_noarch}.1.5svn15878-%{release}-zypper
%endif

%package -n texlive-schemata
Version:        %{texlive_version}.%{texlive_noarch}.0.0.8svn39510
Release:        0
Summary:        Print topical diagrams
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-schemata-doc >= %{texlive_version}
Provides:       tex(schemata.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source95:       schemata.tar.xz
Source96:       schemata.doc.tar.xz

%description -n texlive-schemata
The package facilitates the creation of topical schemata,
outlines that use braces (or facsimiles thereof) to illustrate
the breakdown of concepts and categories in Scholastic thought
from late medieval and early modern periods.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-schemata-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.8svn39510
Release:        0
Summary:        Documentation for texlive-schemata
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-schemata-doc
This package includes the documentation for texlive-schemata

%post -n texlive-schemata
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-schemata 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-schemata
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-schemata-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/schemata/Makefile
%{_texmfdistdir}/doc/generic/schemata/README
%{_texmfdistdir}/doc/generic/schemata/README.txt
%{_texmfdistdir}/doc/generic/schemata/schemata.hd
%{_texmfdistdir}/doc/generic/schemata/schemata.pdf

%files -n texlive-schemata
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/schemata/schemata.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-schemata-%{texlive_version}.%{texlive_noarch}.0.0.8svn39510-%{release}-zypper
%endif

%package -n texlive-schule
Version:        %{texlive_version}.%{texlive_noarch}.0.0.8.1svn48471
Release:        0
Summary:        Support for teachers at German schools
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-schule-doc >= %{texlive_version}
Provides:       tex(relaycircuit.sty)
Provides:       tex(schule.fach.EvReligion.code.tex)
Provides:       tex(schule.fach.Geschichte.code.tex)
Provides:       tex(schule.fach.Geschichte.pakete.tex)
Provides:       tex(schule.fach.Informatik.code.tex)
Provides:       tex(schule.fach.Informatik.pakete.tex)
Provides:       tex(schule.fach.Physik.pakete.tex)
Provides:       tex(schule.mod.Aufgaben.code.tex)
Provides:       tex(schule.mod.Aufgaben.optionen.tex)
Provides:       tex(schule.mod.Aufgaben.pakete.tex)
Provides:       tex(schule.mod.Bewertung.code.tex)
Provides:       tex(schule.mod.Bewertung.optionen.tex)
Provides:       tex(schule.mod.Bewertung.pakete.tex)
Provides:       tex(schule.mod.Format.code.tex)
Provides:       tex(schule.mod.Format.optionen.tex)
Provides:       tex(schule.mod.Format.pakete.tex)
Provides:       tex(schule.mod.Kuerzel.code.tex)
Provides:       tex(schule.mod.Kuerzel.optionen.tex)
Provides:       tex(schule.mod.Lizenzen.code.tex)
Provides:       tex(schule.mod.Lizenzen.optionen.tex)
Provides:       tex(schule.mod.Lizenzen.pakete.tex)
Provides:       tex(schule.mod.Metadaten.code.tex)
Provides:       tex(schule.mod.Metadaten.optionen.tex)
Provides:       tex(schule.mod.Papiertypen.code.tex)
Provides:       tex(schule.mod.Symbole.code.tex)
Provides:       tex(schule.mod.Symbole.pakete.tex)
Provides:       tex(schule.mod.Texte.code.tex)
Provides:       tex(schule.mod.Texte.pakete.tex)
Provides:       tex(schule.sty)
Provides:       tex(schule.typ.ab.code.tex)
Provides:       tex(schule.typ.ab.pakete.tex)
Provides:       tex(schule.typ.folie.code.tex)
Provides:       tex(schule.typ.folie.pakete.tex)
Provides:       tex(schule.typ.kl.code.tex)
Provides:       tex(schule.typ.kl.optionen.tex)
Provides:       tex(schule.typ.kl.pakete.tex)
Provides:       tex(schule.typ.leit.code.tex)
Provides:       tex(schule.typ.leit.optionen.tex)
Provides:       tex(schule.typ.leit.pakete.tex)
Provides:       tex(schule.typ.lzk.code.tex)
Provides:       tex(schule.typ.lzk.pakete.tex)
Provides:       tex(schule.typ.ub.code.tex)
Provides:       tex(schule.typ.ub.pakete.tex)
Provides:       tex(schule.typ.ueb.code.tex)
Provides:       tex(schule.typ.ueb.pakete.tex)
Provides:       tex(schuleab.cls)
Provides:       tex(schulealt.sty)
Provides:       tex(schulein.cls)
Provides:       tex(schuleit.cls)
Provides:       tex(schulekl.cls)
Provides:       tex(schulekl.sty)
Provides:       tex(schuleub.cls)
Provides:       tex(schuleue.cls)
Provides:       tex(schulinf.sty)
Provides:       tex(schullsg.cls)
Provides:       tex(schullzk.cls)
Provides:       tex(schullzk.sty)
Provides:       tex(schulphy.sty)
Provides:       tex(syntaxdi.sty)
Provides:       tex(utfsym.sty)
Provides:       tex(xsim.style.schule-binnen.code.tex)
Provides:       tex(xsim.style.schule-default.code.tex)
Provides:       tex(xsim.style.schule-keinenummer.code.tex)
Provides:       tex(xsim.style.schule-keinepunkte.code.tex)
Provides:       tex(xsim.style.schule-keintitel.code.tex)
Provides:       tex(xsim.style.schule-randpunkte.code.tex)
Provides:       tex(xsim.style.schule-tabelle-kurz.code.tex)
Provides:       tex(xsim.style.schule-tcolorbox.code.tex)
Requires:       tex(adjustbox.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(babel.sty)
Requires:       tex(biblatex.sty)
Requires:       tex(calc.sty)
Requires:       tex(cancel.sty)
Requires:       tex(ccicons.sty)
Requires:       tex(circuitikz.sty)
Requires:       tex(csquotes.sty)
Requires:       tex(environ.sty)
Requires:       tex(etex.sty)
Requires:       tex(eurosym.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(forarray.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(inputenc.sty)
Requires:       tex(listings.sty)
Requires:       tex(mdframed.sty)
Requires:       tex(mhchem.sty)
Requires:       tex(multicol.sty)
Requires:       tex(multirow.sty)
Requires:       tex(natbib.sty)
Requires:       tex(paralist.sty)
Requires:       tex(pdfpages.sty)
Requires:       tex(pgf-umlcd.sty)
Requires:       tex(pgf-umlsd.sty)
Requires:       tex(pgfopts.sty)
Requires:       tex(ragged2e.sty)
Requires:       tex(rotating.sty)
Requires:       tex(scrartcl.cls)
Requires:       tex(scrpage2.sty)
Requires:       tex(silence.sty)
Requires:       tex(struktex.sty)
Requires:       tex(svn-multi.sty)
Requires:       tex(tabularx.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(tikz.sty)
Requires:       tex(units.sty)
Requires:       tex(varwidth.sty)
Requires:       tex(warning.sty)
Requires:       tex(wrapfig.sty)
Requires:       tex(xargs.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xifthen.sty)
Requires:       tex(xmpincl.sty)
Requires:       tex(xparse.sty)
Requires:       tex(xspace.sty)
Requires:       tex(xstring.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source97:       schule.tar.xz
Source98:       schule.doc.tar.xz

%description -n texlive-schule
The 'schule' bundle was built to provide packages and commands
that could be useful for documents in German schools. At the
moment its main focus lies on documents for informatics as a
school subject. An extension for physics is currently in
progress. Extensions for other subjects are welcome. For the
time being, the whole package splits up into individual
packages for informatics (including syntax diagrams,
Nassi-Shneiderman diagrams, sequence diagrams, object diagrams,
and class diagrams) as well as classes for written exams
(tests, quizzes, teaching observations, information sheets,
worksheets, and answer keys).

date: 2018-08-23 02:21:50 +0000


%package -n texlive-schule-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.8.1svn48471
Release:        0
Summary:        Documentation for texlive-schule
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Provides:       locale(texlive-schule-doc:de)

%description -n texlive-schule-doc
This package includes the documentation for texlive-schule

%post -n texlive-schule
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-schule 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-schule
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-schule-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/schule/Abbildungen/table02600-026FF.pdf
%{_texmfdistdir}/doc/latex/schule/Abbildungen/table02600-026FF.tex
%{_texmfdistdir}/doc/latex/schule/Abbildungen/table02700-027BF.pdf
%{_texmfdistdir}/doc/latex/schule/Abbildungen/table02700-027BF.tex
%{_texmfdistdir}/doc/latex/schule/Abbildungen/table1F000-1F02F.pdf
%{_texmfdistdir}/doc/latex/schule/Abbildungen/table1F000-1F02F.tex
%{_texmfdistdir}/doc/latex/schule/Abbildungen/table1F030-1F09F.pdf
%{_texmfdistdir}/doc/latex/schule/Abbildungen/table1F030-1F09F.tex
%{_texmfdistdir}/doc/latex/schule/Abbildungen/table1F0A0-1F0FF.pdf
%{_texmfdistdir}/doc/latex/schule/Abbildungen/table1F0A0-1F0FF.tex
%{_texmfdistdir}/doc/latex/schule/Abbildungen/table1F300-1F5FF.pdf
%{_texmfdistdir}/doc/latex/schule/Abbildungen/table1F300-1F5FF.tex
%{_texmfdistdir}/doc/latex/schule/Abbildungen/table1F600-1F64F.pdf
%{_texmfdistdir}/doc/latex/schule/Abbildungen/table1F600-1F64F.tex
%{_texmfdistdir}/doc/latex/schule/Abbildungen/table1F680-1F6FF.pdf
%{_texmfdistdir}/doc/latex/schule/Abbildungen/table1F680-1F6FF.tex
%{_texmfdistdir}/doc/latex/schule/Beispiele/aufgabe-1.pdf
%{_texmfdistdir}/doc/latex/schule/Beispiele/aufgabe-2.pdf
%{_texmfdistdir}/doc/latex/schule/Beispiele/beispiel-ab-abbott.pdf
%{_texmfdistdir}/doc/latex/schule/Beispiele/beispiel-ab-abbott.tex
%{_texmfdistdir}/doc/latex/schule/Beispiele/beispiel-ab-schiefeebene.pdf
%{_texmfdistdir}/doc/latex/schule/Beispiele/beispiel-ab-schiefeebene.tex
%{_texmfdistdir}/doc/latex/schule/Beispiele/beispiel-ab.pdf
%{_texmfdistdir}/doc/latex/schule/Beispiele/beispiel-ab.tex
%{_texmfdistdir}/doc/latex/schule/Beispiele/beispiel-aufgabentemplates.pdf
%{_texmfdistdir}/doc/latex/schule/Beispiele/beispiel-aufgabentemplates.tex
%{_texmfdistdir}/doc/latex/schule/Beispiele/beispiel-ib-hieroglyphen.pdf
%{_texmfdistdir}/doc/latex/schule/Beispiele/beispiel-ib-hieroglyphen.tex
%{_texmfdistdir}/doc/latex/schule/Beispiele/beispiel-kl.pdf
%{_texmfdistdir}/doc/latex/schule/Beispiele/beispiel-kl.tex
%{_texmfdistdir}/doc/latex/schule/Beispiele/beispiel-leitprogramm.pdf
%{_texmfdistdir}/doc/latex/schule/Beispiele/beispiel-leitprogramm.tex
%{_texmfdistdir}/doc/latex/schule/Beispiele/bsp-geschichte.pdf
%{_texmfdistdir}/doc/latex/schule/Beispiele/bsp-geschichte.tex
%{_texmfdistdir}/doc/latex/schule/Beispiele/bsp-pap.tikz
%{_texmfdistdir}/doc/latex/schule/Beispiele/bsp-vocab.pdf
%{_texmfdistdir}/doc/latex/schule/Beispiele/bsp-vocab.tex
%{_texmfdistdir}/doc/latex/schule/Beispiele/hieroglyph-female.pdf
%{_texmfdistdir}/doc/latex/schule/Beispiele/hieroglyph-male.pdf
%{_texmfdistdir}/doc/latex/schule/Beispiele/minimal-ab-dev.pdf
%{_texmfdistdir}/doc/latex/schule/Beispiele/minimal-ab-dev.tex
%{_texmfdistdir}/doc/latex/schule/Beispiele/minimal-ab.pdf
%{_texmfdistdir}/doc/latex/schule/Beispiele/minimal-ab.tex
%{_texmfdistdir}/doc/latex/schule/Beispiele/minimal-ib.pdf
%{_texmfdistdir}/doc/latex/schule/Beispiele/minimal-ib.tex
%{_texmfdistdir}/doc/latex/schule/Beispiele/minimal-ka.pdf
%{_texmfdistdir}/doc/latex/schule/Beispiele/minimal-ka.tex
%{_texmfdistdir}/doc/latex/schule/Beispiele/minimal-kl-et.pdf
%{_texmfdistdir}/doc/latex/schule/Beispiele/minimal-kl-et.tex
%{_texmfdistdir}/doc/latex/schule/Beispiele/minimal-kl-teilpunkte.pdf
%{_texmfdistdir}/doc/latex/schule/Beispiele/minimal-kl-teilpunkte.tex
%{_texmfdistdir}/doc/latex/schule/Beispiele/minimal-kl.pdf
%{_texmfdistdir}/doc/latex/schule/Beispiele/minimal-kl.tex
%{_texmfdistdir}/doc/latex/schule/README
%{_texmfdistdir}/doc/latex/schule/allgemeines.tex
%{_texmfdistdir}/doc/latex/schule/anhang.tex
%{_texmfdistdir}/doc/latex/schule/beispiele.tex
%{_texmfdistdir}/doc/latex/schule/changelog.tex
%{_texmfdistdir}/doc/latex/schule/dev.tex
%{_texmfdistdir}/doc/latex/schule/devFunktionen.tex
%{_texmfdistdir}/doc/latex/schule/devModule.tex
%{_texmfdistdir}/doc/latex/schule/devRichtlinien.tex
%{_texmfdistdir}/doc/latex/schule/dokumenttypen.tex
%{_texmfdistdir}/doc/latex/schule/fachGeschichte.tex
%{_texmfdistdir}/doc/latex/schule/fachInformatik.tex
%{_texmfdistdir}/doc/latex/schule/fachPhysik.tex
%{_texmfdistdir}/doc/latex/schule/faecher.tex
%{_texmfdistdir}/doc/latex/schule/faq.tex
%{_texmfdistdir}/doc/latex/schule/lizenzen.tex
%{_texmfdistdir}/doc/latex/schule/modulAufgaben.tex
%{_texmfdistdir}/doc/latex/schule/modulBewertung.tex
%{_texmfdistdir}/doc/latex/schule/modulFormat.tex
%{_texmfdistdir}/doc/latex/schule/modulKuerzel.tex
%{_texmfdistdir}/doc/latex/schule/modulLizenzen.tex
%{_texmfdistdir}/doc/latex/schule/modulMetadaten.tex
%{_texmfdistdir}/doc/latex/schule/modulPapiertypen.tex
%{_texmfdistdir}/doc/latex/schule/modulSymbole.tex
%{_texmfdistdir}/doc/latex/schule/modulTexte.tex
%{_texmfdistdir}/doc/latex/schule/module.tex
%{_texmfdistdir}/doc/latex/schule/schule-dokumentation.sty
%{_texmfdistdir}/doc/latex/schule/schule.pdf
%{_texmfdistdir}/doc/latex/schule/schule.tex
%{_texmfdistdir}/doc/latex/schule/todo.tex
%{_texmfdistdir}/doc/latex/schule/typAb.tex
%{_texmfdistdir}/doc/latex/schule/typFolie.tex
%{_texmfdistdir}/doc/latex/schule/typKl.tex
%{_texmfdistdir}/doc/latex/schule/typLeitprogramm.tex
%{_texmfdistdir}/doc/latex/schule/typLzk.tex
%{_texmfdistdir}/doc/latex/schule/typUb.tex
%{_texmfdistdir}/doc/latex/schule/typUeb.tex
%{_texmfdistdir}/doc/latex/schule/zusatzpaketRelaycircuit.tex
%{_texmfdistdir}/doc/latex/schule/zusatzpaketSchuleAlt.tex
%{_texmfdistdir}/doc/latex/schule/zusatzpaketSyntaxdi.tex
%{_texmfdistdir}/doc/latex/schule/zusatzpaketUtfsym.tex
%{_texmfdistdir}/doc/latex/schule/zusatzpakete.tex

%files -n texlive-schule
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/schule/Lizenzen/lizenz-cc-by-4.xmp
%{_texmfdistdir}/tex/latex/schule/Lizenzen/lizenz-cc-by-nc-sa-4.xmp
%{_texmfdistdir}/tex/latex/schule/Lizenzen/lizenz-cc-by-sa-4.xmp
%{_texmfdistdir}/tex/latex/schule/relaycircuit.sty
%{_texmfdistdir}/tex/latex/schule/schule.fach.EvReligion.code.tex
%{_texmfdistdir}/tex/latex/schule/schule.fach.Geschichte.code.tex
%{_texmfdistdir}/tex/latex/schule/schule.fach.Geschichte.pakete.tex
%{_texmfdistdir}/tex/latex/schule/schule.fach.Informatik.code.tex
%{_texmfdistdir}/tex/latex/schule/schule.fach.Informatik.pakete.tex
%{_texmfdistdir}/tex/latex/schule/schule.fach.Physik.pakete.tex
%{_texmfdistdir}/tex/latex/schule/schule.mod.Aufgaben.code.tex
%{_texmfdistdir}/tex/latex/schule/schule.mod.Aufgaben.optionen.tex
%{_texmfdistdir}/tex/latex/schule/schule.mod.Aufgaben.pakete.tex
%{_texmfdistdir}/tex/latex/schule/schule.mod.Bewertung.code.tex
%{_texmfdistdir}/tex/latex/schule/schule.mod.Bewertung.optionen.tex
%{_texmfdistdir}/tex/latex/schule/schule.mod.Bewertung.pakete.tex
%{_texmfdistdir}/tex/latex/schule/schule.mod.Format.code.tex
%{_texmfdistdir}/tex/latex/schule/schule.mod.Format.optionen.tex
%{_texmfdistdir}/tex/latex/schule/schule.mod.Format.pakete.tex
%{_texmfdistdir}/tex/latex/schule/schule.mod.Kuerzel.code.tex
%{_texmfdistdir}/tex/latex/schule/schule.mod.Kuerzel.optionen.tex
%{_texmfdistdir}/tex/latex/schule/schule.mod.Lizenzen.code.tex
%{_texmfdistdir}/tex/latex/schule/schule.mod.Lizenzen.optionen.tex
%{_texmfdistdir}/tex/latex/schule/schule.mod.Lizenzen.pakete.tex
%{_texmfdistdir}/tex/latex/schule/schule.mod.Metadaten.code.tex
%{_texmfdistdir}/tex/latex/schule/schule.mod.Metadaten.optionen.tex
%{_texmfdistdir}/tex/latex/schule/schule.mod.Papiertypen.code.tex
%{_texmfdistdir}/tex/latex/schule/schule.mod.Symbole.code.tex
%{_texmfdistdir}/tex/latex/schule/schule.mod.Symbole.pakete.tex
%{_texmfdistdir}/tex/latex/schule/schule.mod.Texte.code.tex
%{_texmfdistdir}/tex/latex/schule/schule.mod.Texte.pakete.tex
%{_texmfdistdir}/tex/latex/schule/schule.sty
%{_texmfdistdir}/tex/latex/schule/schule.typ.ab.code.tex
%{_texmfdistdir}/tex/latex/schule/schule.typ.ab.pakete.tex
%{_texmfdistdir}/tex/latex/schule/schule.typ.folie.code.tex
%{_texmfdistdir}/tex/latex/schule/schule.typ.folie.pakete.tex
%{_texmfdistdir}/tex/latex/schule/schule.typ.kl.code.tex
%{_texmfdistdir}/tex/latex/schule/schule.typ.kl.optionen.tex
%{_texmfdistdir}/tex/latex/schule/schule.typ.kl.pakete.tex
%{_texmfdistdir}/tex/latex/schule/schule.typ.leit.code.tex
%{_texmfdistdir}/tex/latex/schule/schule.typ.leit.optionen.tex
%{_texmfdistdir}/tex/latex/schule/schule.typ.leit.pakete.tex
%{_texmfdistdir}/tex/latex/schule/schule.typ.lzk.code.tex
%{_texmfdistdir}/tex/latex/schule/schule.typ.lzk.pakete.tex
%{_texmfdistdir}/tex/latex/schule/schule.typ.ub.code.tex
%{_texmfdistdir}/tex/latex/schule/schule.typ.ub.pakete.tex
%{_texmfdistdir}/tex/latex/schule/schule.typ.ueb.code.tex
%{_texmfdistdir}/tex/latex/schule/schule.typ.ueb.pakete.tex
%{_texmfdistdir}/tex/latex/schule/schuleab.cls
%{_texmfdistdir}/tex/latex/schule/schulealt.sty
%{_texmfdistdir}/tex/latex/schule/schulein.cls
%{_texmfdistdir}/tex/latex/schule/schuleit.cls
%{_texmfdistdir}/tex/latex/schule/schulekl.cls
%{_texmfdistdir}/tex/latex/schule/schulekl.sty
%{_texmfdistdir}/tex/latex/schule/schuleub.cls
%{_texmfdistdir}/tex/latex/schule/schuleue.cls
%{_texmfdistdir}/tex/latex/schule/schulinf.sty
%{_texmfdistdir}/tex/latex/schule/schullsg.cls
%{_texmfdistdir}/tex/latex/schule/schullzk.cls
%{_texmfdistdir}/tex/latex/schule/schullzk.sty
%{_texmfdistdir}/tex/latex/schule/schulphy.sty
%{_texmfdistdir}/tex/latex/schule/syntaxdi.sty
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F000.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F001.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F002.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F003.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F004.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F005.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F006.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F007.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F008.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F009.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F00A.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F00B.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F00C.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F00D.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F00E.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F00F.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F010.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F011.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F012.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F013.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F014.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F015.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F016.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F017.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F018.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F019.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F01A.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F01B.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F01C.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F01D.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F01E.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F01F.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F020.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F021.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F022.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F023.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F024.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F025.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F026.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F027.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F028.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F029.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F02A.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F02B.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F02C.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F02D.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F02E.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F02F.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F030.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F031.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F032.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F033.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F034.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F035.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F036.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F037.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F038.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F039.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F03A.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F03B.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F03C.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F03D.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F03E.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F03F.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F040.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F041.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F042.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F043.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F044.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F045.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F046.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F047.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F048.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F049.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F04A.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F04B.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F04C.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F04D.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F04E.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F04F.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F050.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F051.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F052.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F053.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F054.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F055.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F056.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F057.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F058.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F059.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F05A.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F05B.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F05C.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F05D.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F05E.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F05F.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F060.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F061.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F062.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F063.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F064.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F065.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F066.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F067.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F068.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F069.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F06A.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F06B.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F06C.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F06D.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F06E.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F06F.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F070.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F071.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F072.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F073.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F074.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F075.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F076.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F077.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F078.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F079.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F07A.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F07B.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F07C.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F07D.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F07E.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F07F.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F080.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F081.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F082.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F083.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F084.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F085.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F086.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F087.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F088.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F089.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F08A.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F08B.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F08C.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F08D.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F08E.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F08F.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F090.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F091.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F092.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F093.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F094.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F095.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F096.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F097.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F098.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F099.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F09A.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F09B.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F09C.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F09D.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F09E.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F09F.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0A0.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0A1.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0A2.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0A3.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0A4.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0A5.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0A6.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0A7.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0A8.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0A9.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0AA.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0AB.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0AC.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0AD.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0AE.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0AF.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0B0.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0B1.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0B2.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0B3.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0B4.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0B5.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0B6.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0B7.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0B8.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0B9.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0BA.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0BB.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0BC.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0BD.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0BE.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0BF.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0C0.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0C1.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0C2.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0C3.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0C4.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0C5.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0C6.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0C7.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0C8.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0C9.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0CA.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0CB.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0CC.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0CD.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0CE.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0CF.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0D0.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0D1.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0D2.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0D3.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0D4.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0D5.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0D6.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0D7.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0D8.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0D9.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0DA.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0DB.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0DC.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0DD.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0DE.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0DF.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0E0.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0E1.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0E2.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0E3.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0E4.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0E5.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0E6.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0E7.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0E8.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0E9.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0EA.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0EB.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0EC.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0ED.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0EE.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0EF.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0F0.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0F1.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0F2.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0F3.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0F4.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0F5.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0F6.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0F7.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0F8.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0F9.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0FA.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0FB.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0FC.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0FD.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0FE.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F0FF.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F300.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F301.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F302.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F303.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F304.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F305.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F306.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F307.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F308.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F309.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F30A.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F30B.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F30C.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F30D.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F30E.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F30F.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F310.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F311.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F312.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F313.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F314.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F315.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F316.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F317.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F318.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F319.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F31A.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F31B.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F31C.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F31D.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F31E.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F31F.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F320.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F321.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F322.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F323.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F324.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F325.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F326.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F327.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F328.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F329.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F32A.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F32B.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F32C.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F32D.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F32E.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F32F.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F330.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F331.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F332.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F333.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F334.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F335.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F336.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F337.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F338.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F339.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F33A.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F33B.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F33C.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F33D.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F33E.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F33F.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F340.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F341.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F342.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F343.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F344.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F345.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F346.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F347.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F348.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F349.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F34A.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F34B.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F34C.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F34D.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F34E.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F34F.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F350.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F351.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F352.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F353.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F354.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F355.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F356.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F357.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F358.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F359.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F35A.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F35B.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F35C.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F35D.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F35E.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F35F.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F360.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F361.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F362.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F363.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F364.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F365.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F366.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F367.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F368.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F369.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F36A.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F36B.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F36C.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F36D.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F36E.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F36F.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F370.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F371.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F372.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F373.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F374.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F375.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F376.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F377.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F378.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F379.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F37A.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F37B.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F37C.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F37D.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F37E.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F37F.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F380.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F381.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F382.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F383.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F384.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F385.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F386.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F387.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F388.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F389.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F38A.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F38B.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F38C.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F38D.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F38E.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F38F.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F390.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F391.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F392.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F393.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F394.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F395.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F396.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F397.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F398.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F399.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F39A.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F39B.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F39C.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F39D.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F39E.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F39F.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3A0.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3A1.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3A2.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3A3.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3A4.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3A5.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3A6.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3A7.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3A8.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3A9.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3AA.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3AB.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3AC.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3AD.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3AE.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3AF.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3B0.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3B1.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3B2.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3B3.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3B4.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3B5.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3B6.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3B7.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3B8.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3B9.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3BA.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3BB.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3BC.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3BD.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3BE.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3BF.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3C0.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3C1.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3C2.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3C3.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3C4.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3C5.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3C6.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3C7.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3C8.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3C9.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3CA.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3CB.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3CC.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3CD.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3CE.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3CF.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3D0.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3D1.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3D2.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3D3.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3D4.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3D5.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3D6.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3D7.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3D8.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3D9.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3DA.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3DB.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3DC.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3DD.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3DE.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3DF.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3E0.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3E1.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3E2.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3E3.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3E4.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3E5.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3E6.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3E7.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3E8.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3E9.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3EA.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3EB.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3EC.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3ED.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3EE.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3EF.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3F0.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3F1.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3F2.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3F3.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3F4.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3F5.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3F6.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3F7.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3F8.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3F9.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3FA.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3FB.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3FC.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3FD.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3FE.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F3FF.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F400.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F401.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F402.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F403.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F404.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F405.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F406.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F407.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F408.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F409.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F40A.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F40B.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F40C.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F40D.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F40E.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F40F.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F410.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F411.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F412.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F413.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F414.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F415.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F416.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F417.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F418.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F419.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F41A.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F41B.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F41C.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F41D.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F41E.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F41F.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F420.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F421.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F422.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F423.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F424.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F425.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F426.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F427.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F428.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F429.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F42A.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F42B.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F42C.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F42D.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F42E.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F42F.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F430.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F431.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F432.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F433.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F434.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F435.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F436.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F437.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F438.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F439.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F43A.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F43B.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F43C.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F43D.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F43E.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F43F.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F440.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F441.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F442.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F443.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F444.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F445.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F446.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F447.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F448.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F449.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F44A.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F44B.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F44C.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F44D.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F44E.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F44F.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F450.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F451.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F452.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F453.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F454.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F455.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F456.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F457.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F458.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F459.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F45A.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F45B.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F45C.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F45D.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F45E.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F45F.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F460.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F461.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F462.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F463.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F464.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F465.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F466.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F467.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F468.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F469.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F46A.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F46B.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F46C.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F46D.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F46E.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F46F.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F470.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F471.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F472.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F473.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F474.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F475.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F476.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F477.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F478.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F479.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F47A.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F47B.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F47C.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F47D.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F47E.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F47F.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F480.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F481.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F482.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F483.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F484.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F485.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F486.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F487.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F488.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F489.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F48A.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F48B.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F48C.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F48D.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F48E.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F48F.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F490.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F491.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F492.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F493.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F494.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F495.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F496.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F497.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F498.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F499.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F49A.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F49B.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F49C.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F49D.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F49E.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F49F.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4A0.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4A1.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4A2.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4A3.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4A4.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4A5.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4A6.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4A7.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4A8.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4A9.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4AA.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4AB.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4AC.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4AD.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4AE.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4AF.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4B0.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4B1.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4B2.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4B3.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4B4.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4B5.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4B6.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4B7.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4B8.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4B9.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4BA.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4BB.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4BC.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4BD.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4BE.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4BF.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4C0.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4C1.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4C2.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4C3.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4C4.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4C5.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4C6.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4C7.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4C8.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4C9.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4CA.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4CB.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4CC.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4CD.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4CE.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4CF.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4D0.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4D1.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4D2.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4D3.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4D4.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4D5.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4D6.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4D7.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4D8.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4D9.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4DA.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4DB.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4DC.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4DD.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4DE.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4DF.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4E0.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4E1.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4E2.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4E3.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4E4.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4E5.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4E6.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4E7.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4E8.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4E9.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4EA.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4EB.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4EC.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4ED.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4EE.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4EF.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4F0.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4F1.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4F2.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4F3.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4F4.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4F5.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4F6.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4F7.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4F8.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4F9.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4FA.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4FB.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4FC.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4FD.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4FE.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F4FF.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F500.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F501.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F502.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F503.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F504.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F505.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F506.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F507.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F508.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F509.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F50A.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F50B.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F50C.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F50D.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F50E.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F50F.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F510.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F511.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F512.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F513.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F514.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F515.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F516.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F517.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F518.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F519.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F51A.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F51B.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F51C.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F51D.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F51E.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F51F.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F520.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F521.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F522.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F523.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F524.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F525.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F526.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F527.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F528.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F529.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F52A.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F52B.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F52C.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F52D.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F52E.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F52F.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F530.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F531.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F532.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F533.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F534.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F535.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F536.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F537.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F538.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F539.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F53A.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F53B.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F53C.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F53D.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F53E.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F53F.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F540.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F541.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F542.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F543.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F544.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F545.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F546.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F547.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F548.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F549.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F54A.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F54B.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F54C.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F54D.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F54E.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F54F.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F550.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F551.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F552.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F553.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F554.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F555.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F556.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F557.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F558.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F559.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F55A.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F55B.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F55C.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F55D.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F55E.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F55F.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F560.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F561.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F562.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F563.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F564.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F565.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F566.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F567.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F568.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F569.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F56A.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F56B.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F56C.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F56D.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F56E.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F56F.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F570.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F571.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F572.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F573.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F574.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F575.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F576.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F577.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F578.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F579.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F57A.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F57B.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F57C.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F57D.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F57E.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F57F.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F580.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F581.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F582.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F583.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F584.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F585.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F586.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F587.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F588.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F589.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F58A.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F58B.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F58C.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F58D.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F58E.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F58F.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F590.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F591.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F592.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F593.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F594.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F595.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F596.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F597.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F598.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F599.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F59A.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F59B.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F59C.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F59D.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F59E.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F59F.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5A0.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5A1.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5A2.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5A3.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5A4.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5A5.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5A6.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5A7.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5A8.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5A9.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5AA.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5AB.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5AC.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5AD.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5AE.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5AF.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5B0.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5B1.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5B2.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5B3.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5B4.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5B5.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5B6.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5B7.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5B8.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5B9.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5BA.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5BB.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5BC.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5BD.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5BE.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5BF.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5C0.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5C1.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5C2.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5C3.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5C4.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5C5.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5C6.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5C7.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5C8.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5C9.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5CA.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5CB.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5CC.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5CD.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5CE.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5CF.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5D0.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5D1.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5D2.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5D3.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5D4.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5D5.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5D6.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5D7.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5D8.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5D9.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5DA.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5DB.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5DC.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5DD.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5DE.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5DF.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5E0.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5E1.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5E2.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5E3.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5E4.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5E5.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5E6.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5E7.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5E8.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5E9.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5EA.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5EB.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5EC.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5ED.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5EE.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5EF.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5F0.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5F1.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5F2.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5F3.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5F4.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5F5.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5F6.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5F7.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5F8.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5F9.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5FA.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5FB.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5FC.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5FD.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5FE.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F5FF.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F600.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F601.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F602.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F603.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F604.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F605.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F606.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F607.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F608.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F609.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F60A.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F60B.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F60C.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F60D.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F60E.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F60F.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F610.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F611.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F612.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F613.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F614.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F615.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F616.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F617.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F618.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F619.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F61A.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F61B.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F61C.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F61D.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F61E.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F61F.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F620.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F621.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F622.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F623.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F624.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F625.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F626.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F627.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F628.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F629.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F62A.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F62B.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F62C.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F62D.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F62E.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F62F.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F630.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F631.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F632.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F633.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F634.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F635.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F636.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F637.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F638.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F639.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F63A.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F63B.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F63C.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F63D.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F63E.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F63F.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F640.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F641.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F642.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F643.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F644.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F645.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F646.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F647.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F648.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F649.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F64A.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F64B.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F64C.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F64D.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F64E.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F64F.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F680.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F681.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F682.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F683.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F684.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F685.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F686.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F687.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F688.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F689.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F68A.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F68B.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F68C.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F68D.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F68E.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F68F.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F690.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F691.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F692.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F693.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F694.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F695.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F696.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F697.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F698.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F699.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F69A.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F69B.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F69C.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F69D.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F69E.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F69F.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6A0.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6A1.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6A2.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6A3.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6A4.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6A5.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6A6.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6A7.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6A8.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6A9.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6AA.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6AB.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6AC.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6AD.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6AE.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6AF.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6B0.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6B1.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6B2.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6B3.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6B4.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6B5.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6B6.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6B7.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6B8.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6B9.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6BA.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6BB.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6BC.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6BD.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6BE.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6BF.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6C0.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6C1.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6C2.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6C3.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6C4.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6C5.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6C6.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6C7.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6C8.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6C9.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6CA.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6CB.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6CC.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6CD.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6CE.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6CF.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6D0.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6D1.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6D2.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6D3.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6D4.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6D5.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6D6.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6D7.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6D8.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6D9.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6DA.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6DB.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6DC.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6DD.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6DE.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6DF.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6E0.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6E1.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6E2.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6E3.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6E4.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6E5.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6E6.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6E7.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6E8.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6E9.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6EA.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6EB.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6EC.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6ED.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6EE.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6EF.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6F0.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6F1.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6F2.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6F3.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6F4.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6F5.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6F6.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6F7.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6F8.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6F9.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6FA.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6FB.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6FC.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6FD.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6FE.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym1F6FF.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2600.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2601.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2602.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2603.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2604.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2605.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2606.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2607.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2608.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2609.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym260A.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym260B.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym260C.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym260D.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym260E.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym260F.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2610.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2611.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2612.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2613.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2614.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2615.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2616.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2617.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2618.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2619.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym261A.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym261B.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym261C.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym261D.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym261E.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym261F.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2620.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2621.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2622.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2623.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2624.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2625.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2626.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2627.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2628.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2629.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym262A.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym262B.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym262C.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym262D.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym262E.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym262F.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2630.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2631.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2632.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2633.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2634.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2635.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2636.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2637.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2638.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2639.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym263A.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym263B.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym263C.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym263D.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym263E.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym263F.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2640.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2641.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2642.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2643.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2644.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2645.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2646.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2647.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2648.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2649.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym264A.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym264B.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym264C.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym264D.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym264E.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym264F.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2650.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2651.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2652.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2653.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2654.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2655.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2656.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2657.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2658.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2659.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym265A.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym265B.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym265C.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym265D.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym265E.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym265F.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2660.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2661.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2662.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2663.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2664.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2665.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2666.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2667.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2668.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2669.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym266A.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym266B.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym266C.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym266D.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym266E.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym266F.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2670.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2671.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2672.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2673.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2674.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2675.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2676.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2677.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2678.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2679.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym267A.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym267B.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym267C.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym267D.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym267E.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym267F.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2680.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2681.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2682.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2683.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2684.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2685.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2686.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2687.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2688.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2689.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym268A.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym268B.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym268C.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym268D.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym268E.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym268F.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2690.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2691.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2692.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2693.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2694.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2695.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2696.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2697.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2698.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2699.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym269A.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym269B.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym269C.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym269D.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym269E.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym269F.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26A0.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26A1.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26A2.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26A3.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26A4.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26A5.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26A6.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26A7.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26A8.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26A9.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26AA.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26AB.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26AC.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26AD.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26AE.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26AF.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26B0.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26B1.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26B2.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26B3.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26B4.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26B5.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26B6.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26B7.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26B8.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26B9.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26BA.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26BB.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26BC.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26BD.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26BE.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26BF.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26C0.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26C1.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26C2.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26C3.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26C4.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26C5.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26C6.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26C7.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26C8.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26C9.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26CA.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26CB.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26CC.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26CD.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26CE.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26CF.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26D0.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26D1.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26D2.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26D3.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26D4.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26D5.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26D6.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26D7.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26D8.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26D9.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26DA.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26DB.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26DC.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26DD.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26DE.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26DF.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26E0.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26E1.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26E2.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26E3.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26E4.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26E5.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26E6.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26E7.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26E8.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26E9.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26EA.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26EB.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26EC.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26ED.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26EE.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26EF.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26F0.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26F1.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26F2.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26F3.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26F4.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26F5.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26F6.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26F7.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26F8.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26F9.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26FA.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26FB.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26FC.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26FD.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26FE.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym26FF.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2700.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2701.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2702.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2703.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2704.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2705.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2706.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2707.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2708.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2709.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym270A.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym270B.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym270C.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym270D.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym270E.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym270F.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2710.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2711.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2712.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2713.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2714.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2715.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2716.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2717.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2718.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2719.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym271A.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym271B.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym271C.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym271D.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym271E.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym271F.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2720.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2721.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2722.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2723.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2724.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2725.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2726.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2727.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2728.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2729.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym272A.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym272B.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym272C.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym272D.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym272E.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym272F.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2730.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2731.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2732.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2733.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2734.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2735.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2736.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2737.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2738.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2739.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym273A.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym273B.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym273C.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym273D.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym273E.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym273F.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2740.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2741.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2742.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2743.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2744.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2745.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2746.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2747.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2748.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2749.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym274A.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym274B.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym274C.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym274D.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym274E.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym274F.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2750.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2751.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2752.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2753.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2754.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2755.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2756.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2757.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2758.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2759.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym275A.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym275B.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym275C.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym275D.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym275E.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym275F.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2760.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2761.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2762.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2763.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2764.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2765.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2766.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2767.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2768.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2769.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym276A.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym276B.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym276C.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym276D.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym276E.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym276F.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2770.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2771.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2772.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2773.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2774.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2775.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2776.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2777.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2778.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2779.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym277A.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym277B.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym277C.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym277D.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym277E.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym277F.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2780.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2781.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2782.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2783.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2784.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2785.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2786.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2787.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2788.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2789.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym278A.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym278B.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym278C.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym278D.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym278E.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym278F.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2790.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2791.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2792.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2793.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2794.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2795.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2796.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2797.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2798.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym2799.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym279A.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym279B.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym279C.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym279D.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym279E.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym279F.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym27A0.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym27A1.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym27A2.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym27A3.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym27A4.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym27A5.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym27A6.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym27A7.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym27A8.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym27A9.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym27AA.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym27AB.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym27AC.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym27AD.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym27AE.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym27AF.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym27B0.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym27B1.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym27B2.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym27B3.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym27B4.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym27B5.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym27B6.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym27B7.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym27B8.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym27B9.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym27BA.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym27BB.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym27BC.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym27BD.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym27BE.tikz
%{_texmfdistdir}/tex/latex/schule/tikz/usym27BF.tikz
%{_texmfdistdir}/tex/latex/schule/utfsym.sty
%{_texmfdistdir}/tex/latex/schule/xsim-style/xsim.style.schule-binnen.code.tex
%{_texmfdistdir}/tex/latex/schule/xsim-style/xsim.style.schule-default.code.tex
%{_texmfdistdir}/tex/latex/schule/xsim-style/xsim.style.schule-keinenummer.code.tex
%{_texmfdistdir}/tex/latex/schule/xsim-style/xsim.style.schule-keinepunkte.code.tex
%{_texmfdistdir}/tex/latex/schule/xsim-style/xsim.style.schule-keintitel.code.tex
%{_texmfdistdir}/tex/latex/schule/xsim-style/xsim.style.schule-randpunkte.code.tex
%{_texmfdistdir}/tex/latex/schule/xsim-style/xsim.style.schule-tabelle-kurz.code.tex
%{_texmfdistdir}/tex/latex/schule/xsim-style/xsim.style.schule-tcolorbox.code.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-schule-%{texlive_version}.%{texlive_noarch}.0.0.8.1svn48471-%{release}-zypper
%endif

%package -n texlive-schulschriften
Version:        %{texlive_version}.%{texlive_noarch}.4svn35730
Release:        0
Summary:        German "school scripts" from Suetterlin to the present day
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-schulschriften-doc >= %{texlive_version}
Provides:       tex(schulschriften_lin.sty)
Provides:       tex(schulschriften_ltx.sty)
Provides:       tex(t1wedn.fd)
Provides:       tex(t1wela.fd)
Provides:       tex(t1wesa.fd)
Provides:       tex(t1wesu.fd)
Provides:       tex(t1weva.fd)
Provides:       tex(wedn.sty)
Provides:       tex(wedn14.tfm)
Provides:       tex(wednbx14.tfm)
Provides:       tex(wednbxsl14.tfm)
Provides:       tex(wedneb14.tfm)
Provides:       tex(wednebsl14.tfm)
Provides:       tex(wednsb14.tfm)
Provides:       tex(wednsbsl14.tfm)
Provides:       tex(wednsl14.tfm)
Provides:       tex(wednub14.tfm)
Provides:       tex(wednubsl14.tfm)
Provides:       tex(wela.sty)
Provides:       tex(wela14.tfm)
Provides:       tex(welabx14.tfm)
Provides:       tex(welabxsl14.tfm)
Provides:       tex(welaeb14.tfm)
Provides:       tex(welaebsl14.tfm)
Provides:       tex(welasb14.tfm)
Provides:       tex(welasbsl14.tfm)
Provides:       tex(welasl14.tfm)
Provides:       tex(welaub14.tfm)
Provides:       tex(welaubsl14.tfm)
Provides:       tex(wesa.sty)
Provides:       tex(wesa14.tfm)
Provides:       tex(wesabx14.tfm)
Provides:       tex(wesabxsl14.tfm)
Provides:       tex(wesaeb14.tfm)
Provides:       tex(wesaebsl14.tfm)
Provides:       tex(wesasb14.tfm)
Provides:       tex(wesasbsl14.tfm)
Provides:       tex(wesasl14.tfm)
Provides:       tex(wesaub14.tfm)
Provides:       tex(wesaubsl14.tfm)
Provides:       tex(wesu.sty)
Provides:       tex(wesu14.tfm)
Provides:       tex(wesub14.tfm)
Provides:       tex(wesubsl14.tfm)
Provides:       tex(wesubx14.tfm)
Provides:       tex(wesubxsl14.tfm)
Provides:       tex(wesueb14.tfm)
Provides:       tex(wesuebsl14.tfm)
Provides:       tex(wesusb14.tfm)
Provides:       tex(wesusbsl14.tfm)
Provides:       tex(wesusl14.tfm)
Provides:       tex(wesuub14.tfm)
Provides:       tex(wesuubsl14.tfm)
Provides:       tex(weva.sty)
Provides:       tex(weva14.tfm)
Provides:       tex(wevabx14.tfm)
Provides:       tex(wevabxsl14.tfm)
Provides:       tex(wevaeb14.tfm)
Provides:       tex(wevaebsl14.tfm)
Provides:       tex(wevasb14.tfm)
Provides:       tex(wevasbsl14.tfm)
Provides:       tex(wevasl14.tfm)
Provides:       tex(wevaub14.tfm)
Provides:       tex(wevaubsl14.tfm)
Requires:       tex(color.sty)
Requires:       tex(eepic.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(latexsym.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source99:       schulschriften.tar.xz
Source100:      schulschriften.doc.tar.xz

%description -n texlive-schulschriften
Das Paket enthalt im wesentlichen die Metafont-Quellfiles fur
die folgenden Schulausgangsschriften: Suetterlinschrift,
Deutsche Normalschrift, Lateinische Ausgangsschrift,
Schulausgangsschrift, Vereinfachte Ausgangsschrift. Damit ist
es moglich, beliebige deutsche Texte in diesen Schreibschriften
zu schreiben.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-schulschriften-doc
Version:        %{texlive_version}.%{texlive_noarch}.4svn35730
Release:        0
Summary:        Documentation for texlive-schulschriften
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-schulschriften-doc
This package includes the documentation for texlive-schulschriften

%post -n texlive-schulschriften
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-schulschriften 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-schulschriften
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-schulschriften-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/schulschriften/README
%{_texmfdistdir}/doc/fonts/schulschriften/schulschriften.pdf
%{_texmfdistdir}/doc/fonts/schulschriften/schulschriften.tex
%{_texmfdistdir}/doc/fonts/schulschriften/schulschriften_ltx.tex
%{_texmfdistdir}/doc/fonts/schulschriften/schulschriften_xpl.tex
%{_texmfdistdir}/doc/fonts/schulschriften/wedn_fonttabelle.eps
%{_texmfdistdir}/doc/fonts/schulschriften/wela_fonttabelle.eps
%{_texmfdistdir}/doc/fonts/schulschriften/wesa_fonttabelle.eps
%{_texmfdistdir}/doc/fonts/schulschriften/wesu_fonttabelle.eps
%{_texmfdistdir}/doc/fonts/schulschriften/weva_fonttabelle.eps

%files -n texlive-schulschriften
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/source/public/schulschriften/wedn14.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wedn14_def.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wedn14_end.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wedn14_gr.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wedn14_kl.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wedn14_lig.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wedn14_sz.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wednbx14.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wednbxsl14.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wedneb14.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wednebsl14.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wednsb14.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wednsbsl14.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wednsl14.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wednub14.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wednubsl14.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wela14.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wela14_def.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wela14_end.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wela14_gr.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wela14_kl.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wela14_lig.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wela14_sz.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/welabx14.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/welabxsl14.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/welaeb14.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/welaebsl14.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/welasb14.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/welasbsl14.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/welasl14.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/welaub14.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/welaubsl14.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wesa14.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wesa14_def.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wesa14_end.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wesa14_gr.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wesa14_kl.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wesa14_lig.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wesa14_sz.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wesabx14.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wesabxsl14.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wesaeb14.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wesaebsl14.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wesasb14.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wesasbsl14.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wesasl14.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wesaub14.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wesaubsl14.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wesu14.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wesu14_def.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wesu14_end.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wesu14_gr.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wesu14_kl.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wesu14_lig.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wesu14_sz.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wesub14.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wesubsl14.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wesubx14.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wesubxsl14.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wesueb14.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wesuebsl14.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wesusb14.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wesusbsl14.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wesusl14.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wesuub14.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wesuubsl14.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/weva14.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/weva14_def.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/weva14_gr.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/weva14_kl.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/weva14_lig.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/weva14_sz.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wevabx14.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wevabxsl14.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wevaeb14.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wevaebsl14.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wevasb14.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wevasbsl14.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wevasl14.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wevaub14.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wevaubsl14.mf
%{_texmfdistdir}/fonts/tfm/public/schulschriften/wedn14.tfm
%{_texmfdistdir}/fonts/tfm/public/schulschriften/wednbx14.tfm
%{_texmfdistdir}/fonts/tfm/public/schulschriften/wednbxsl14.tfm
%{_texmfdistdir}/fonts/tfm/public/schulschriften/wedneb14.tfm
%{_texmfdistdir}/fonts/tfm/public/schulschriften/wednebsl14.tfm
%{_texmfdistdir}/fonts/tfm/public/schulschriften/wednsb14.tfm
%{_texmfdistdir}/fonts/tfm/public/schulschriften/wednsbsl14.tfm
%{_texmfdistdir}/fonts/tfm/public/schulschriften/wednsl14.tfm
%{_texmfdistdir}/fonts/tfm/public/schulschriften/wednub14.tfm
%{_texmfdistdir}/fonts/tfm/public/schulschriften/wednubsl14.tfm
%{_texmfdistdir}/fonts/tfm/public/schulschriften/wela14.tfm
%{_texmfdistdir}/fonts/tfm/public/schulschriften/welabx14.tfm
%{_texmfdistdir}/fonts/tfm/public/schulschriften/welabxsl14.tfm
%{_texmfdistdir}/fonts/tfm/public/schulschriften/welaeb14.tfm
%{_texmfdistdir}/fonts/tfm/public/schulschriften/welaebsl14.tfm
%{_texmfdistdir}/fonts/tfm/public/schulschriften/welasb14.tfm
%{_texmfdistdir}/fonts/tfm/public/schulschriften/welasbsl14.tfm
%{_texmfdistdir}/fonts/tfm/public/schulschriften/welasl14.tfm
%{_texmfdistdir}/fonts/tfm/public/schulschriften/welaub14.tfm
%{_texmfdistdir}/fonts/tfm/public/schulschriften/welaubsl14.tfm
%{_texmfdistdir}/fonts/tfm/public/schulschriften/wesa14.tfm
%{_texmfdistdir}/fonts/tfm/public/schulschriften/wesabx14.tfm
%{_texmfdistdir}/fonts/tfm/public/schulschriften/wesabxsl14.tfm
%{_texmfdistdir}/fonts/tfm/public/schulschriften/wesaeb14.tfm
%{_texmfdistdir}/fonts/tfm/public/schulschriften/wesaebsl14.tfm
%{_texmfdistdir}/fonts/tfm/public/schulschriften/wesasb14.tfm
%{_texmfdistdir}/fonts/tfm/public/schulschriften/wesasbsl14.tfm
%{_texmfdistdir}/fonts/tfm/public/schulschriften/wesasl14.tfm
%{_texmfdistdir}/fonts/tfm/public/schulschriften/wesaub14.tfm
%{_texmfdistdir}/fonts/tfm/public/schulschriften/wesaubsl14.tfm
%{_texmfdistdir}/fonts/tfm/public/schulschriften/wesu14.tfm
%{_texmfdistdir}/fonts/tfm/public/schulschriften/wesub14.tfm
%{_texmfdistdir}/fonts/tfm/public/schulschriften/wesubsl14.tfm
%{_texmfdistdir}/fonts/tfm/public/schulschriften/wesubx14.tfm
%{_texmfdistdir}/fonts/tfm/public/schulschriften/wesubxsl14.tfm
%{_texmfdistdir}/fonts/tfm/public/schulschriften/wesueb14.tfm
%{_texmfdistdir}/fonts/tfm/public/schulschriften/wesuebsl14.tfm
%{_texmfdistdir}/fonts/tfm/public/schulschriften/wesusb14.tfm
%{_texmfdistdir}/fonts/tfm/public/schulschriften/wesusbsl14.tfm
%{_texmfdistdir}/fonts/tfm/public/schulschriften/wesusl14.tfm
%{_texmfdistdir}/fonts/tfm/public/schulschriften/wesuub14.tfm
%{_texmfdistdir}/fonts/tfm/public/schulschriften/wesuubsl14.tfm
%{_texmfdistdir}/fonts/tfm/public/schulschriften/weva14.tfm
%{_texmfdistdir}/fonts/tfm/public/schulschriften/wevabx14.tfm
%{_texmfdistdir}/fonts/tfm/public/schulschriften/wevabxsl14.tfm
%{_texmfdistdir}/fonts/tfm/public/schulschriften/wevaeb14.tfm
%{_texmfdistdir}/fonts/tfm/public/schulschriften/wevaebsl14.tfm
%{_texmfdistdir}/fonts/tfm/public/schulschriften/wevasb14.tfm
%{_texmfdistdir}/fonts/tfm/public/schulschriften/wevasbsl14.tfm
%{_texmfdistdir}/fonts/tfm/public/schulschriften/wevasl14.tfm
%{_texmfdistdir}/fonts/tfm/public/schulschriften/wevaub14.tfm
%{_texmfdistdir}/fonts/tfm/public/schulschriften/wevaubsl14.tfm
%{_texmfdistdir}/tex/latex/schulschriften/schulschriften_lin.sty
%{_texmfdistdir}/tex/latex/schulschriften/schulschriften_ltx.sty
%{_texmfdistdir}/tex/latex/schulschriften/t1wedn.fd
%{_texmfdistdir}/tex/latex/schulschriften/t1wela.fd
%{_texmfdistdir}/tex/latex/schulschriften/t1wesa.fd
%{_texmfdistdir}/tex/latex/schulschriften/t1wesu.fd
%{_texmfdistdir}/tex/latex/schulschriften/t1weva.fd
%{_texmfdistdir}/tex/latex/schulschriften/wedn.sty
%{_texmfdistdir}/tex/latex/schulschriften/wela.sty
%{_texmfdistdir}/tex/latex/schulschriften/wesa.sty
%{_texmfdistdir}/tex/latex/schulschriften/wesu.sty
%{_texmfdistdir}/tex/latex/schulschriften/weva.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-schulschriften-%{texlive_version}.%{texlive_noarch}.4svn35730-%{release}-zypper
%endif

%package -n texlive-schwalbe-chess
Version:        %{texlive_version}.%{texlive_noarch}.2.3svn49602
Release:        0
Summary:        Typeset the German chess magazine "Die Schwalbe"
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-schwalbe-chess-doc >= %{texlive_version}
Provides:       tex(schwalbe.cls)
Provides:       tex(schwalbe.sty)
Requires:       tex(afterpage.sty)
Requires:       tex(article.cls)
Requires:       tex(babel.sty)
Requires:       tex(diagram.sty)
Requires:       tex(eurosym.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(inputenc.sty)
Requires:       tex(multicol.sty)
Requires:       tex(paralist.sty)
Requires:       tex(picinpar.sty)
Requires:       tex(times.sty)
Requires:       tex(url.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source101:      schwalbe-chess.tar.xz
Source102:      schwalbe-chess.doc.tar.xz

%description -n texlive-schwalbe-chess
The package is based on chess-problem-diagrams, which in its
turn has a dependency on the bartel-chess-fonts.

date: 2019-01-04 15:33:55 +0000


%package -n texlive-schwalbe-chess-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.3svn49602
Release:        0
Summary:        Documentation for texlive-schwalbe-chess
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Provides:       locale(texlive-schwalbe-chess-doc:de)

%description -n texlive-schwalbe-chess-doc
This package includes the documentation for texlive-schwalbe-chess

%post -n texlive-schwalbe-chess
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-schwalbe-chess 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-schwalbe-chess
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-schwalbe-chess-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/schwalbe-chess/README
%{_texmfdistdir}/doc/latex/schwalbe-chess/schwalbe.pdf

%files -n texlive-schwalbe-chess
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/schwalbe-chess/schwalbe.cls
%{_texmfdistdir}/tex/latex/schwalbe-chess/schwalbe.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-schwalbe-chess-%{texlive_version}.%{texlive_noarch}.2.3svn49602-%{release}-zypper
%endif

%package -n texlive-scientific-thesis-cover
Version:        %{texlive_version}.%{texlive_noarch}.4.0.2svn47923
Release:        0
Summary:        Provides cover page and affirmation at the end of a thesis
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-scientific-thesis-cover-doc >= %{texlive_version}
Provides:       tex(scientific-thesis-cover.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(kvoptions.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source103:      scientific-thesis-cover.tar.xz
Source104:      scientific-thesis-cover.doc.tar.xz

%description -n texlive-scientific-thesis-cover
Institutions require a cover page and an affirmation at the end
of a thesis. This package provides both.

date: 2018-06-03 19:55:55 +0000


%package -n texlive-scientific-thesis-cover-doc
Version:        %{texlive_version}.%{texlive_noarch}.4.0.2svn47923
Release:        0
Summary:        Documentation for texlive-scientific-thesis-cover
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-scientific-thesis-cover-doc
This package includes the documentation for texlive-scientific-thesis-cover

%post -n texlive-scientific-thesis-cover
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-scientific-thesis-cover 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-scientific-thesis-cover
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-scientific-thesis-cover-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/scientific-thesis-cover/CHANGELOG.md
%{_texmfdistdir}/doc/latex/scientific-thesis-cover/README.TEXLIVE
%{_texmfdistdir}/doc/latex/scientific-thesis-cover/README.md
%{_texmfdistdir}/doc/latex/scientific-thesis-cover/demo.tex
%{_texmfdistdir}/doc/latex/scientific-thesis-cover/scientific-thesis-cover.pdf

%files -n texlive-scientific-thesis-cover
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/scientific-thesis-cover/scientific-thesis-cover.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-scientific-thesis-cover-%{texlive_version}.%{texlive_noarch}.4.0.2svn47923-%{release}-zypper
%endif

%package -n texlive-sciposter
Version:        %{texlive_version}.%{texlive_noarch}.1.18svn15878
Release:        0
Summary:        Make posters of ISO A3 size and larger
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-sciposter-doc >= %{texlive_version}
Provides:       tex(paperb0.cfg)
Provides:       tex(paperb1.cfg)
Provides:       tex(paperb2.cfg)
Provides:       tex(paperb3.cfg)
Provides:       tex(papercustom.cfg)
Provides:       tex(paperra0.cfg)
Provides:       tex(paperra1.cfg)
Provides:       tex(paperra2.cfg)
Provides:       tex(sciposter.cls)
Requires:       tex(a0size.sty)
Requires:       tex(article.cls)
Requires:       tex(boxedminipage.sty)
Requires:       tex(color.sty)
Requires:       tex(graphics.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(lettrine.sty)
Requires:       tex(shadow.sty)
Requires:       tex(times.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source105:      sciposter.tar.xz
Source106:      sciposter.doc.tar.xz

%description -n texlive-sciposter
This collection of files contains LaTeX packages for posters of
ISO A3 size and larger (ISO A0 is the default size). American
paper sizes and custom paper are supported. In particular,
sciposter.cls defines a document class which allows cutting and
pasting most of an article to a poster without any editing
(save reducing the size) -- see the manual. Sciposter does work
for LaTeX, not just pdfLaTeX. However, xdvi produces strange
results, though a recent version of dvips does create good
ps-files from the dvi files. Also note that logos must either
be put in the current working directory or in the directories
of your LaTeX distribution. For some reason graphicspath
settings are ignored.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-sciposter-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.18svn15878
Release:        0
Summary:        Documentation for texlive-sciposter
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-sciposter-doc
This package includes the documentation for texlive-sciposter

%post -n texlive-sciposter
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-sciposter 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-sciposter
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-sciposter-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/sciposter/README
%{_texmfdistdir}/doc/latex/sciposter/sciposterexample/auto/sciposter-example.el
%{_texmfdistdir}/doc/latex/sciposter/sciposterexample/blocks1.eps
%{_texmfdistdir}/doc/latex/sciposter/sciposterexample/blocks1.pdf
%{_texmfdistdir}/doc/latex/sciposter/sciposterexample/blocks1a.eps
%{_texmfdistdir}/doc/latex/sciposter/sciposterexample/blocks1a.pdf
%{_texmfdistdir}/doc/latex/sciposter/sciposterexample/blocks1mx.eps
%{_texmfdistdir}/doc/latex/sciposter/sciposterexample/blocks1mx.pdf
%{_texmfdistdir}/doc/latex/sciposter/sciposterexample/blocks1vx.eps
%{_texmfdistdir}/doc/latex/sciposter/sciposterexample/blocks1vx.pdf
%{_texmfdistdir}/doc/latex/sciposter/sciposterexample/blocks2.eps
%{_texmfdistdir}/doc/latex/sciposter/sciposterexample/blocks2.pdf
%{_texmfdistdir}/doc/latex/sciposter/sciposterexample/blocks2mx.eps
%{_texmfdistdir}/doc/latex/sciposter/sciposterexample/blocks2mx.pdf
%{_texmfdistdir}/doc/latex/sciposter/sciposterexample/blocks3.eps
%{_texmfdistdir}/doc/latex/sciposter/sciposterexample/blocks3.pdf
%{_texmfdistdir}/doc/latex/sciposter/sciposterexample/blocks3mx.eps
%{_texmfdistdir}/doc/latex/sciposter/sciposterexample/blocks3mx.pdf
%{_texmfdistdir}/doc/latex/sciposter/sciposterexample/blocks3op.eps
%{_texmfdistdir}/doc/latex/sciposter/sciposterexample/blocks3op.pdf
%{_texmfdistdir}/doc/latex/sciposter/sciposterexample/blocks3openvx.eps
%{_texmfdistdir}/doc/latex/sciposter/sciposterexample/blocks3rec.eps
%{_texmfdistdir}/doc/latex/sciposter/sciposterexample/blocks3rec.pdf
%{_texmfdistdir}/doc/latex/sciposter/sciposterexample/blocks3vx.eps
%{_texmfdistdir}/doc/latex/sciposter/sciposterexample/blocks3vx.pdf
%{_texmfdistdir}/doc/latex/sciposter/sciposterexample/blocksopen3a.eps
%{_texmfdistdir}/doc/latex/sciposter/sciposterexample/blocksopen3a.pdf
%{_texmfdistdir}/doc/latex/sciposter/sciposterexample/blocksopen3vx.eps
%{_texmfdistdir}/doc/latex/sciposter/sciposterexample/blocksopen3vx.pdf
%{_texmfdistdir}/doc/latex/sciposter/sciposterexample/blocksopen3vy.eps
%{_texmfdistdir}/doc/latex/sciposter/sciposterexample/blocksopen3vy.pdf
%{_texmfdistdir}/doc/latex/sciposter/sciposterexample/sciposter-example.tex
%{_texmfdistdir}/doc/latex/sciposter/scipostermanual.pdf

%files -n texlive-sciposter
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/sciposter/paperb0.cfg
%{_texmfdistdir}/tex/latex/sciposter/paperb1.cfg
%{_texmfdistdir}/tex/latex/sciposter/paperb2.cfg
%{_texmfdistdir}/tex/latex/sciposter/paperb3.cfg
%{_texmfdistdir}/tex/latex/sciposter/papercustom.cfg
%{_texmfdistdir}/tex/latex/sciposter/paperra0.cfg
%{_texmfdistdir}/tex/latex/sciposter/paperra1.cfg
%{_texmfdistdir}/tex/latex/sciposter/paperra2.cfg
%{_texmfdistdir}/tex/latex/sciposter/sciposter.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-sciposter-%{texlive_version}.%{texlive_noarch}.1.18svn15878-%{release}-zypper
%endif

%package -n texlive-sclang-prettifier
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn35087
Release:        0
Summary:        Prettyprinting SuperCollider source code
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-sclang-prettifier-doc >= %{texlive_version}
Provides:       tex(sclang-prettifier.sty)
Requires:       tex(listings.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xcolor.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source107:      sclang-prettifier.tar.xz
Source108:      sclang-prettifier.doc.tar.xz

%description -n texlive-sclang-prettifier
Built on top of the listings package, the package allows
effortless prettyprinting of SuperCollider source code in
documents typeset with LaTeX & friends.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-sclang-prettifier-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn35087
Release:        0
Summary:        Documentation for texlive-sclang-prettifier
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-sclang-prettifier-doc
This package includes the documentation for texlive-sclang-prettifier

%post -n texlive-sclang-prettifier
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-sclang-prettifier 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-sclang-prettifier
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-sclang-prettifier-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/sclang-prettifier/README
%{_texmfdistdir}/doc/latex/sclang-prettifier/sclang-prettifier.pdf

%files -n texlive-sclang-prettifier
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/sclang-prettifier/sclang-prettifier.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-sclang-prettifier-%{texlive_version}.%{texlive_noarch}.0.0.1svn35087-%{release}-zypper
%endif

%package -n texlive-scratch
Version:        %{texlive_version}.%{texlive_noarch}.0.0.41svn50073
Release:        0
Summary:        Draw programs like "scratch"
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-scratch-doc >= %{texlive_version}
Provides:       tex(scratch.sty)
Requires:       tex(simplekv.sty)
Requires:       tex(tikz.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source109:      scratch.tar.xz
Source110:      scratch.doc.tar.xz

%description -n texlive-scratch
This package is now obsolete. From now on, scratch at
scratch.mit.edu is now version3 with a new design. Please, use
the "scratch3" package to draw blocks with the new design. This
package permits to draw program charts in the style of the
scatch project (scratch.mit.edu). It depends on the other LaTeX
packages TikZ and simplekv.

date: 2019-02-19 22:30:41 +0000


%package -n texlive-scratch-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.41svn50073
Release:        0
Summary:        Documentation for texlive-scratch
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Provides:       locale(texlive-scratch-doc:fr)

%description -n texlive-scratch-doc
This package includes the documentation for texlive-scratch

%post -n texlive-scratch
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-scratch 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-scratch
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-scratch-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/scratch/README
%{_texmfdistdir}/doc/latex/scratch/scratch-fr.pdf
%{_texmfdistdir}/doc/latex/scratch/scratch-fr.tex

%files -n texlive-scratch
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/scratch/scratch.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-scratch-%{texlive_version}.%{texlive_noarch}.0.0.41svn50073-%{release}-zypper
%endif

%package -n texlive-scratch3
Version:        %{texlive_version}.%{texlive_noarch}.0.0.11svn50304
Release:        0
Summary:        Draw programs like "scratch"
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-scratch3-doc >= %{texlive_version}
Provides:       tex(scratch3.sty)
Requires:       tex(simplekv.sty)
Requires:       tex(tikz.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source111:      scratch3.tar.xz
Source112:      scratch3.doc.tar.xz

%description -n texlive-scratch3
This package permits to draw program charts in the style of the
scatch project (scratch.mit.edu). It depends on the other LaTeX
packages TikZ and simplekv.

date: 2019-03-09 16:34:02 +0000


%package -n texlive-scratch3-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.11svn50304
Release:        0
Summary:        Documentation for texlive-scratch3
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Provides:       locale(texlive-scratch3-doc:fr)

%description -n texlive-scratch3-doc
This package includes the documentation for texlive-scratch3

%post -n texlive-scratch3
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-scratch3 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-scratch3
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-scratch3-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/scratch3/README
%{_texmfdistdir}/doc/latex/scratch3/scratch3-fr.pdf
%{_texmfdistdir}/doc/latex/scratch3/scratch3-fr.tex

%files -n texlive-scratch3
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/scratch3/scratch3.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-scratch3-%{texlive_version}.%{texlive_noarch}.0.0.11svn50304-%{release}-zypper
%endif

%package -n texlive-scratchx
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn44906
Release:        0
Summary:        Include Scratch programs in LaTeX documents
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-scratchx-doc >= %{texlive_version}
Provides:       tex(ScratchX.sty)
Requires:       tex(calc.sty)
Requires:       tex(fp.sty)
Requires:       tex(ifsym.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(multido.sty)
Requires:       tex(xargs.sty)
Requires:       tex(xstring.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source113:      scratchx.tar.xz
Source114:      scratchx.doc.tar.xz

%description -n texlive-scratchx
This package can be used to include every kind of Scratch
program in LaTeX documents. This may be particularly useful for
Math Teachers and IT specialists. The package depends on the
following other LaTeX packages: calc, fp, ifsym, multido, tikz,
xargs, and xstring.

date: 2017-07-30 03:13:46 +0000


%package -n texlive-scratchx-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn44906
Release:        0
Summary:        Documentation for texlive-scratchx
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Provides:       locale(texlive-scratchx-doc:fr)

%description -n texlive-scratchx-doc
This package includes the documentation for texlive-scratchx

%post -n texlive-scratchx
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-scratchx 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-scratchx
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-scratchx-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/scratchx/Explanations_ScratchX.pdf
%{_texmfdistdir}/doc/latex/scratchx/Explanations_ScratchX.tex
%{_texmfdistdir}/doc/latex/scratchx/Explications_ScratchX.pdf
%{_texmfdistdir}/doc/latex/scratchx/Explications_ScratchX.tex
%{_texmfdistdir}/doc/latex/scratchx/README.txt

%files -n texlive-scratchx
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/scratchx/ScratchX.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-scratchx-%{texlive_version}.%{texlive_noarch}.1.1svn44906-%{release}-zypper
%endif

%package -n texlive-screenplay
Version:        %{texlive_version}.%{texlive_noarch}.1.6svn27223
Release:        0
Summary:        A class file to typeset screenplays
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-screenplay-doc >= %{texlive_version}
Provides:       tex(hardmarg.sty)
Provides:       tex(screenplay.cls)
Requires:       tex(article.cls)
Requires:       tex(courier.sty)
Requires:       tex(geometry.sty)
Requires:       tex(ifthen.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source115:      screenplay.tar.xz
Source116:      screenplay.doc.tar.xz

%description -n texlive-screenplay
The class implements the format recommended by the Academy of
Motion Picture Arts and Sciences.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-screenplay-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.6svn27223
Release:        0
Summary:        Documentation for texlive-screenplay
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-screenplay-doc
This package includes the documentation for texlive-screenplay

%post -n texlive-screenplay
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-screenplay 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-screenplay
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-screenplay-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/screenplay/COPYING
%{_texmfdistdir}/doc/latex/screenplay/README
%{_texmfdistdir}/doc/latex/screenplay/example.tex
%{_texmfdistdir}/doc/latex/screenplay/screenplay.pdf
%{_texmfdistdir}/doc/latex/screenplay/test.pdf
%{_texmfdistdir}/doc/latex/screenplay/test.tex

%files -n texlive-screenplay
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/screenplay/hardmarg.sty
%{_texmfdistdir}/tex/latex/screenplay/screenplay.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-screenplay-%{texlive_version}.%{texlive_noarch}.1.6svn27223-%{release}-zypper
%endif

%package -n texlive-screenplay-pkg
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn44965
Release:        0
Summary:        Package version of the screenplay document class
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-screenplay-pkg-doc >= %{texlive_version}
Provides:       tex(screenplay-pkg.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(setspace.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source117:      screenplay-pkg.tar.xz
Source118:      screenplay-pkg.doc.tar.xz

%description -n texlive-screenplay-pkg
This package implements the tools of the screenplay document
class in the form of a package so that screenplay fragments can
be included within another document class. For full
documentation of the available commands, please consult the
screenplay class documentation in addition to the included
package documentation.

date: 2017-08-06 06:17:31 +0000


%package -n texlive-screenplay-pkg-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn44965
Release:        0
Summary:        Documentation for texlive-screenplay-pkg
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-screenplay-pkg-doc
This package includes the documentation for texlive-screenplay-pkg

%post -n texlive-screenplay-pkg
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-screenplay-pkg 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-screenplay-pkg
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-screenplay-pkg-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/screenplay-pkg/README
%{_texmfdistdir}/doc/latex/screenplay-pkg/screenplay-pkg-example.pdf
%{_texmfdistdir}/doc/latex/screenplay-pkg/screenplay-pkg-example.tex
%{_texmfdistdir}/doc/latex/screenplay-pkg/screenplay-pkg.pdf
%{_texmfdistdir}/doc/latex/screenplay-pkg/screenplay-pkg.tex

%files -n texlive-screenplay-pkg
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/screenplay-pkg/screenplay-pkg.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-screenplay-pkg-%{texlive_version}.%{texlive_noarch}.1.1svn44965-%{release}-zypper
%endif

%package -n texlive-scrjrnl
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn27810
Release:        0
Summary:        Typeset diaries or journals
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-scrjrnl-doc >= %{texlive_version}
Provides:       tex(scrjrnl.cls)
Requires:       tex(babel.sty)
Requires:       tex(datetime.sty)
Requires:       tex(fancytabs.sty)
Requires:       tex(titlesec.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source119:      scrjrnl.tar.xz
Source120:      scrjrnl.doc.tar.xz

%description -n texlive-scrjrnl
A class, based on scrbook, designed for typesetting diaries,
journals or devotionals.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-scrjrnl-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn27810
Release:        0
Summary:        Documentation for texlive-scrjrnl
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-scrjrnl-doc
This package includes the documentation for texlive-scrjrnl

%post -n texlive-scrjrnl
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-scrjrnl 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-scrjrnl
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-scrjrnl-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/scrjrnl/README
%{_texmfdistdir}/doc/latex/scrjrnl/example.pdf
%{_texmfdistdir}/doc/latex/scrjrnl/scrjrnl.pdf

%files -n texlive-scrjrnl
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/scrjrnl/scrjrnl.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-scrjrnl-%{texlive_version}.%{texlive_noarch}.0.0.1svn27810-%{release}-zypper
%endif

%package -n texlive-scrlttr2copy
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1dsvn39734
Release:        0
Summary:        A letter class option file for the automatic creation of copies
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-scrlttr2copy-doc >= %{texlive_version}
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source121:      scrlttr2copy.tar.xz
Source122:      scrlttr2copy.doc.tar.xz

%description -n texlive-scrlttr2copy
The file copy.lco provides the new class option "copy" for the
KOMA-Script letter class scrlttr2. If the option "copy" is
given, all pages of a specific letter are duplicated with
background text marking as copies.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-scrlttr2copy-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1dsvn39734
Release:        0
Summary:        Documentation for texlive-scrlttr2copy
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-scrlttr2copy-doc
This package includes the documentation for texlive-scrlttr2copy

%post -n texlive-scrlttr2copy
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-scrlttr2copy 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-scrlttr2copy
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-scrlttr2copy-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/scrlttr2copy/README.md
%{_texmfdistdir}/doc/latex/scrlttr2copy/letter-copy-test.pdf
%{_texmfdistdir}/doc/latex/scrlttr2copy/letter-copy-test.tex

%files -n texlive-scrlttr2copy
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/scrlttr2copy/copy.lco
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-scrlttr2copy-%{texlive_version}.%{texlive_noarch}.0.0.1dsvn39734-%{release}-zypper
%endif

%package -n texlive-scsnowman
Version:        %{texlive_version}.%{texlive_noarch}.1.2dsvn47953
Release:        0
Summary:        Snowman variants using TikZ
License:        BSD-3-Clause
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-scsnowman-doc >= %{texlive_version}
Provides:       tex(scsnowman-normal.def)
Provides:       tex(scsnowman.sty)
Provides:       tex(sctkzsym-base.sty)
Requires:       tex(keyval.sty)
Requires:       tex(pxeveryshi.sty)
Requires:       tex(tikz.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source123:      scsnowman.tar.xz
Source124:      scsnowman.doc.tar.xz

%description -n texlive-scsnowman
This LaTeX package provides a command \scsnowman which can
display many variants of "snowman" ("yukidaruma" in Japanese).
TikZ is required for drawing these snowmen.

date: 2018-06-07 16:24:21 +0000


%package -n texlive-scsnowman-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.2dsvn47953
Release:        0
Summary:        Documentation for texlive-scsnowman
License:        BSD-3-Clause
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Provides:       locale(texlive-scsnowman-doc:ja)

%description -n texlive-scsnowman-doc
This package includes the documentation for texlive-scsnowman

%post -n texlive-scsnowman
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-scsnowman 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-scsnowman
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-scsnowman-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/scsnowman/LICENSE
%{_texmfdistdir}/doc/latex/scsnowman/Makefile
%{_texmfdistdir}/doc/latex/scsnowman/README.md
%{_texmfdistdir}/doc/latex/scsnowman/scsnowman-sample.pdf
%{_texmfdistdir}/doc/latex/scsnowman/scsnowman-sample.tex
%{_texmfdistdir}/doc/latex/scsnowman/scsnowman-zrtest.pdf
%{_texmfdistdir}/doc/latex/scsnowman/scsnowman-zrtest.tex
%{_texmfdistdir}/doc/latex/scsnowman/scsnowman.pdf
%{_texmfdistdir}/doc/latex/scsnowman/scsnowman.tex

%files -n texlive-scsnowman
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/scsnowman/scsnowman-normal.def
%{_texmfdistdir}/tex/latex/scsnowman/scsnowman.sty
%{_texmfdistdir}/tex/latex/scsnowman/sctkzsym-base.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-scsnowman-%{texlive_version}.%{texlive_noarch}.1.2dsvn47953-%{release}-zypper
%endif

%package -n texlive-sdrt
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn15878
Release:        0
Summary:        Macros for Segmented Discourse Representation Theory
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-sdrt-doc >= %{texlive_version}
Provides:       tex(sdrt.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(xyling.sty)
Requires:       tex(xytree.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source125:      sdrt.tar.xz
Source126:      sdrt.doc.tar.xz

%description -n texlive-sdrt
The package provides macros to produce the 'Box notation' of
SDRT (and DRT), to draw trees representing discourse relations,
and finally to have an easy access to various mathematical
symbols used in that theory, mostly with automatic mathematics
mode, so they work the same in formulae and in text.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-sdrt-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn15878
Release:        0
Summary:        Documentation for texlive-sdrt
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-sdrt-doc
This package includes the documentation for texlive-sdrt

%post -n texlive-sdrt
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-sdrt 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-sdrt
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-sdrt-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/sdrt/README
%{_texmfdistdir}/doc/latex/sdrt/sdrt-doc.pdf
%{_texmfdistdir}/doc/latex/sdrt/sdrt-doc.tex

%files -n texlive-sdrt
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/sdrt/sdrt.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-sdrt-%{texlive_version}.%{texlive_noarch}.1.0svn15878-%{release}-zypper
%endif

%package -n texlive-sduthesis
Version:        %{texlive_version}.%{texlive_noarch}.1.2.1svn41401
Release:        0
Summary:        Thesis Template of Shandong University
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-sduthesis-doc >= %{texlive_version}
Provides:       tex(sduthesis-cover.def)
Provides:       tex(sduthesis-statement.def)
Provides:       tex(sduthesis.cls)
Requires:       tex(amsbsy.sty)
Requires:       tex(amsfonts.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(amsthm.sty)
Requires:       tex(bm.sty)
Requires:       tex(bmpsize.sty)
Requires:       tex(booktabs.sty)
Requires:       tex(ctexbook.cls)
Requires:       tex(epstopdf.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(geometry.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(makecell.sty)
Requires:       tex(mathrsfs.sty)
Requires:       tex(xcolor.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source127:      sduthesis.tar.xz
Source128:      sduthesis.doc.tar.xz

%description -n texlive-sduthesis
Thesis Template of Shandong University.

date: 2017-04-18 03:31:40 +0000


%package -n texlive-sduthesis-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.2.1svn41401
Release:        0
Summary:        Documentation for texlive-sduthesis
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Provides:       locale(texlive-sduthesis-doc:zh)

%description -n texlive-sduthesis-doc
This package includes the documentation for texlive-sduthesis

%post -n texlive-sduthesis
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-sduthesis 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-sduthesis
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-sduthesis-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/sduthesis/LICENSE
%{_texmfdistdir}/doc/latex/sduthesis/LICENSE.md
%{_texmfdistdir}/doc/latex/sduthesis/README
%{_texmfdistdir}/doc/latex/sduthesis/README.md
%{_texmfdistdir}/doc/latex/sduthesis/sduthesis-demo.pdf
%{_texmfdistdir}/doc/latex/sduthesis/sduthesis-demo.tex
%{_texmfdistdir}/doc/latex/sduthesis/sduthesis.pdf

%files -n texlive-sduthesis
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/sduthesis/figures/SDU.pdf
%{_texmfdistdir}/tex/latex/sduthesis/figures/SDULogo.pdf
%{_texmfdistdir}/tex/latex/sduthesis/figures/SDUWords.jpg
%{_texmfdistdir}/tex/latex/sduthesis/figures/sduthesis-baotuquan.jpg
%{_texmfdistdir}/tex/latex/sduthesis/figures/sduthesis-hongloujiaotang.jpg
%{_texmfdistdir}/tex/latex/sduthesis/figures/sduthesis-ruanjianyuan.jpg
%{_texmfdistdir}/tex/latex/sduthesis/figures/sduthesis-xianzhidadao.jpg
%{_texmfdistdir}/tex/latex/sduthesis/figures/sduthesis-zhixinlou.jpg
%{_texmfdistdir}/tex/latex/sduthesis/sduthesis-cover.def
%{_texmfdistdir}/tex/latex/sduthesis/sduthesis-statement.def
%{_texmfdistdir}/tex/latex/sduthesis/sduthesis.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-sduthesis-%{texlive_version}.%{texlive_noarch}.1.2.1svn41401-%{release}-zypper
%endif

%package -n texlive-secdot
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn20208
Release:        0
Summary:        Section numbers with trailing dots
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-secdot-doc >= %{texlive_version}
Provides:       tex(secdot.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source129:      secdot.tar.xz
Source130:      secdot.doc.tar.xz

%description -n texlive-secdot
Makes the numbers of \section commands come out with a trailing
dot. Includes a command whereby the same can be made to happen
with other sectioning commands.

date: 2018-09-15 13:51:52 +0000


%package -n texlive-secdot-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn20208
Release:        0
Summary:        Documentation for texlive-secdot
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-secdot-doc
This package includes the documentation for texlive-secdot

%post -n texlive-secdot
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-secdot 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-secdot
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-secdot-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/secdot/secdot.ltx
%{_texmfdistdir}/doc/latex/secdot/secdot.pdf

%files -n texlive-secdot
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/secdot/secdot.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-secdot-%{texlive_version}.%{texlive_noarch}.1.0svn20208-%{release}-zypper
%endif

%package -n texlive-section
Version:        %{texlive_version}.%{texlive_noarch}.svn20180
Release:        0
Summary:        Modifying section commands in LaTeX
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-section-doc >= %{texlive_version}
Provides:       tex(section.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source131:      section.tar.xz
Source132:      section.doc.tar.xz

%description -n texlive-section
The package implements a pretty extensive scheme to make more
manageable the business of configuring LaTeX output.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-section-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn20180
Release:        0
Summary:        Documentation for texlive-section
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-section-doc
This package includes the documentation for texlive-section

%post -n texlive-section
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-section 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-section
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-section-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/section/section-doc.pdf
%{_texmfdistdir}/doc/latex/section/section-doc.tex

%files -n texlive-section
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/section/section.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-section-%{texlive_version}.%{texlive_noarch}.svn20180-%{release}-zypper
%endif

%package -n texlive-sectionbox
Version:        %{texlive_version}.%{texlive_noarch}.1.01svn37749
Release:        0
Summary:        Create fancy boxed ((sub)sub)sections
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-sectionbox-doc >= %{texlive_version}
Provides:       tex(sectionbox.sty)
Requires:       tex(calc.sty)
Requires:       tex(color.sty)
Requires:       tex(fancybox.sty)
Requires:       tex(ifthen.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source133:      sectionbox.tar.xz
Source134:      sectionbox.doc.tar.xz

%description -n texlive-sectionbox
Sectionbox is a LaTeX package for putting fancy colored boxes
around sections, subsections, and subsubsections, especially
for use in posters, etc. It was designed with the sciposter
class in mind, and certainly works with that class and with
derived classes.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-sectionbox-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.01svn37749
Release:        0
Summary:        Documentation for texlive-sectionbox
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-sectionbox-doc
This package includes the documentation for texlive-sectionbox

%post -n texlive-sectionbox
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-sectionbox 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-sectionbox
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-sectionbox-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/sectionbox/README
%{_texmfdistdir}/doc/latex/sectionbox/example/000074Bpatspec.png
%{_texmfdistdir}/doc/latex/sectionbox/example/000074Bzones.jpg
%{_texmfdistdir}/doc/latex/sectionbox/example/000175Bpatspec.png
%{_texmfdistdir}/doc/latex/sectionbox/example/000175Bzones.jpg
%{_texmfdistdir}/doc/latex/sectionbox/example/002000AApatspec.png
%{_texmfdistdir}/doc/latex/sectionbox/example/002000AAzones.jpg
%{_texmfdistdir}/doc/latex/sectionbox/example/README.TEXLIVE
%{_texmfdistdir}/doc/latex/sectionbox/example/lambda2.jpg
%{_texmfdistdir}/doc/latex/sectionbox/example/orig.jpg
%{_texmfdistdir}/doc/latex/sectionbox/example/sectionboxexample.bib
%{_texmfdistdir}/doc/latex/sectionbox/example/sectionboxexample.tex
%{_texmfdistdir}/doc/latex/sectionbox/sectionboxmanual.pdf

%files -n texlive-sectionbox
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/sectionbox/sectionbox.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-sectionbox-%{texlive_version}.%{texlive_noarch}.1.01svn37749-%{release}-zypper
%endif

%package -n texlive-sectionbreak
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1dsvn50339
Release:        0
Summary:        LaTeX support for section breaks
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-sectionbreak-doc >= %{texlive_version}
Provides:       tex(sectionbreak.sty)
Requires:       tex(kvoptions.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source135:      sectionbreak.tar.xz
Source136:      sectionbreak.doc.tar.xz

%description -n texlive-sectionbreak
This package provides LaTeX support for section breaks, used
mainly in fiction books to signal changes in a story, like
changes in time, location, etc. It supports the asterism
symbol, text content, or custom macros as the section break
mark symbol.

date: 2019-03-11 12:54:30 +0000


%package -n texlive-sectionbreak-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1dsvn50339
Release:        0
Summary:        Documentation for texlive-sectionbreak
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-sectionbreak-doc
This package includes the documentation for texlive-sectionbreak

%post -n texlive-sectionbreak
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-sectionbreak 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-sectionbreak
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-sectionbreak-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/sectionbreak/CHANGELOG.md
%{_texmfdistdir}/doc/latex/sectionbreak/README.md
%{_texmfdistdir}/doc/latex/sectionbreak/sectionbreak-doc.pdf
%{_texmfdistdir}/doc/latex/sectionbreak/sectionbreak-doc.tex
%{_texmfdistdir}/doc/latex/sectionbreak/sectionbreak-example.tex

%files -n texlive-sectionbreak
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/sectionbreak/sectionbreak.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-sectionbreak-%{texlive_version}.%{texlive_noarch}.0.0.1dsvn50339-%{release}-zypper
%endif

%package -n texlive-sectsty
Version:        %{texlive_version}.%{texlive_noarch}.2.0.2svn15878
Release:        0
Summary:        Control sectional headers
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-sectsty-doc >= %{texlive_version}
Provides:       tex(sectsty.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source137:      sectsty.tar.xz
Source138:      sectsty.doc.tar.xz

%description -n texlive-sectsty
A LaTeX2e package to help change the style of any or all of
LaTeX's sectional headers in the article, book, or report
classes. Examples include the addition of rules above or below
a section title.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-sectsty-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.0.2svn15878
Release:        0
Summary:        Documentation for texlive-sectsty
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-sectsty-doc
This package includes the documentation for texlive-sectsty

%post -n texlive-sectsty
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-sectsty 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-sectsty
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-sectsty-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/sectsty/sectsty.pdf

%files -n texlive-sectsty
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/sectsty/sectsty.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-sectsty-%{texlive_version}.%{texlive_noarch}.2.0.2svn15878-%{release}-zypper
%endif

%package -n texlive-seealso
Version:        %{texlive_version}.%{texlive_noarch}.1.2svn43595
Release:        0
Summary:        Improve the performance of \see macros with makeindex
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-seealso-doc >= %{texlive_version}
Provides:       tex(seealso.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(kvoptions.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source139:      seealso.tar.xz
Source140:      seealso.doc.tar.xz

%description -n texlive-seealso
The package amends the \see and \seealso macros that are used
in building indexes with makeindex, to deal with repetitions,
and to ensure page numbers are present in the actual index
entries. on these indirecty

date: 2018-01-06 11:14:59 +0000


%package -n texlive-seealso-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.2svn43595
Release:        0
Summary:        Documentation for texlive-seealso
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-seealso-doc
This package includes the documentation for texlive-seealso

%post -n texlive-seealso
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-seealso 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-seealso
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-seealso-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/seealso/README
%{_texmfdistdir}/doc/latex/seealso/seealso.pdf

%files -n texlive-seealso
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/seealso/seealso.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-seealso-%{texlive_version}.%{texlive_noarch}.1.2svn43595-%{release}-zypper
%endif

%package -n texlive-seetexk
Version:        %{texlive_version}.%{texlive_noarch}.svn50602
Release:        0
Summary:        Utilities for manipulating DVI files
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive-seetexk-bin >= %{texlive_version}
#!BuildIgnore: texlive-seetexk-bin
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source141:      seetexk.doc.tar.xz

%description -n texlive-seetexk
The collection comprises: dvibook, which will rearrange the
pages of a DVI file into 'signatures' as used when printing a
book; dviconcat, for concatenating pages of DVI file(s);
dviselect, which will select pages from one DVI file to create
a new DVI file; dvitodvi, which will rearrange the pages of a
DVI file to create a new file; and libtex, a library for
manipulating the files, from the old SeeTeX project. The
utilities are provided as C source with Imakefiles, and an
MS-DOS version of dvibook is also provided.

date: 2016-06-24 17:18:15 +0000

%post -n texlive-seetexk
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-seetexk 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-seetexk
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-seetexk
%defattr(-,root,root,755)
%{_mandir}/man1/dvibook.1*
%{_mandir}/man1/dviconcat.1*
%{_mandir}/man1/dviselect.1*
%{_mandir}/man1/dvitodvi.1*
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-seetexk-%{texlive_version}.%{texlive_noarch}.svn50602-%{release}-zypper
%endif

%package -n texlive-selectp
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn20185
Release:        0
Summary:        Select pages to be output
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-selectp-doc >= %{texlive_version}
Provides:       tex(selectp.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source142:      selectp.tar.xz
Source143:      selectp.doc.tar.xz

%description -n texlive-selectp
Defines a command \outputonly, whose argument is a list of
pages to be output. With the command present (before
\begin{document}), only those pages are output. This package
was inspired by code published by Knuth in TUGboat 8(2) (July
1987).

date: 2016-06-24 17:18:15 +0000


%package -n texlive-selectp-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn20185
Release:        0
Summary:        Documentation for texlive-selectp
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-selectp-doc
This package includes the documentation for texlive-selectp

%post -n texlive-selectp
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-selectp 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-selectp
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-selectp-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/selectp/selectp-doc.pdf
%{_texmfdistdir}/doc/latex/selectp/selectp-doc.tex

%files -n texlive-selectp
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/selectp/selectp.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-selectp-%{texlive_version}.%{texlive_noarch}.1.0svn20185-%{release}-zypper
%endif

%package -n texlive-selnolig
Version:        %{texlive_version}.%{texlive_noarch}.0.0.302svn38721
Release:        0
Summary:        Selectively disable typographic ligatures
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-selnolig-doc >= %{texlive_version}
Provides:       tex(selnolig-english-hyphex.sty)
Provides:       tex(selnolig-english-patterns.sty)
Provides:       tex(selnolig-german-hyphex.sty)
Provides:       tex(selnolig-german-patterns.sty)
Provides:       tex(selnolig.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(luatexbase.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source144:      selnolig.tar.xz
Source145:      selnolig.doc.tar.xz

%description -n texlive-selnolig
The package suppresses typographic ligatures selectively, i.e.,
based on predefined search patterns. The search patterns focus
on ligatures deemed inappropriate because they span morpheme
boundaries. For example, the word shelfful, which is mentioned
in the TeXbook as a word for which the ff ligature might be
inappropriate, is automatically typeset as shelf\/ful rather
than as shel{ff}ul. For English and German language documents,
the package provides extensive rules for the selective
suppression of so-called "common" ligatures. These comprise the
ff, fi, fl, ffi, and ffl ligatures as well as the ft and fft
ligatures. Other f-ligatures, such as fb, fh, fj and fk, are
suppressed globally, while exceptions are made for names and
words of non-English/German origin, such as Kafka and fjord.
For English language documents, the package further provides
ligature suppression macros for a number of so-called
"discretionary" or "rare" ligatures such as ct, st, and sp. The
package requires use of a recent LuaLaTeX format (for example
those from TeX Live 2012 or 2013, or MiKTeX 2.9).

date: 2018-03-07 04:17:28 +0000


%package -n texlive-selnolig-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.302svn38721
Release:        0
Summary:        Documentation for texlive-selnolig
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-selnolig-doc
This package includes the documentation for texlive-selnolig

%post -n texlive-selnolig
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-selnolig 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-selnolig
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-selnolig-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/lualatex/selnolig/README
%{_texmfdistdir}/doc/lualatex/selnolig/gpp-ft.fea
%{_texmfdistdir}/doc/lualatex/selnolig/selnolig-bugreport.tex
%{_texmfdistdir}/doc/lualatex/selnolig/selnolig-english-test.pdf
%{_texmfdistdir}/doc/lualatex/selnolig/selnolig-english-test.tex
%{_texmfdistdir}/doc/lualatex/selnolig/selnolig-english-wordlist.tex
%{_texmfdistdir}/doc/lualatex/selnolig/selnolig-german-test.pdf
%{_texmfdistdir}/doc/lualatex/selnolig/selnolig-german-test.tex
%{_texmfdistdir}/doc/lualatex/selnolig/selnolig-german-wordlist.tex
%{_texmfdistdir}/doc/lualatex/selnolig/selnolig.pdf
%{_texmfdistdir}/doc/lualatex/selnolig/selnolig.tex

%files -n texlive-selnolig
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/lualatex/selnolig/selnolig-english-hyphex.sty
%{_texmfdistdir}/tex/lualatex/selnolig/selnolig-english-patterns.sty
%{_texmfdistdir}/tex/lualatex/selnolig/selnolig-german-hyphex.sty
%{_texmfdistdir}/tex/lualatex/selnolig/selnolig-german-patterns.sty
%{_texmfdistdir}/tex/lualatex/selnolig/selnolig.lua
%{_texmfdistdir}/tex/lualatex/selnolig/selnolig.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-selnolig-%{texlive_version}.%{texlive_noarch}.0.0.302svn38721-%{release}-zypper
%endif

%package -n texlive-semantic
Version:        %{texlive_version}.%{texlive_noarch}.2.0svn15878
Release:        0
Summary:        Help for writing programming language semantics
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-semantic-doc >= %{texlive_version}
Provides:       tex(infernce.sty)
Provides:       tex(ligature.sty)
Provides:       tex(reserved.sty)
Provides:       tex(semantic.sty)
Provides:       tex(shrthand.sty)
Provides:       tex(tdiagram.sty)
Requires:       tex(mathbbol.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source146:      semantic.tar.xz
Source147:      semantic.doc.tar.xz

%description -n texlive-semantic
Eases the typesetting of notation of semantics and compilers.
Includes T-diagrams, various derivation symbols and inference
trees.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-semantic-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.0svn15878
Release:        0
Summary:        Documentation for texlive-semantic
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-semantic-doc
This package includes the documentation for texlive-semantic

%post -n texlive-semantic
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-semantic 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-semantic
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-semantic-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/semantic/semantic.pdf

%files -n texlive-semantic
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/semantic/infernce.sty
%{_texmfdistdir}/tex/latex/semantic/ligature.sty
%{_texmfdistdir}/tex/latex/semantic/reserved.sty
%{_texmfdistdir}/tex/latex/semantic/semantic.sty
%{_texmfdistdir}/tex/latex/semantic/shrthand.sty
%{_texmfdistdir}/tex/latex/semantic/tdiagram.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-semantic-%{texlive_version}.%{texlive_noarch}.2.0svn15878-%{release}-zypper
%endif

%package -n texlive-semantic-markup
Version:        %{texlive_version}.%{texlive_noarch}.svn47837
Release:        0
Summary:        Meaningful semantic markup in the spirit of the Text Encoding Initiative
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-semantic-markup-doc >= %{texlive_version}
Provides:       tex(semantic-markup.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(csquotes.sty)
Requires:       tex(endnotes.sty)
Requires:       tex(environ.sty)
Requires:       tex(harmony.sty)
Requires:       tex(xparse.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source148:      semantic-markup.tar.xz
Source149:      semantic-markup.doc.tar.xz

%description -n texlive-semantic-markup
The package provides simple commands to allow authors
(especially scholars in the humanities) to write with a focus
on content rather than presentation. The commands are inspired
by the XML elements of the Text Encoding Initiative. Commands
like \term and \foreign are aliases for \emph. \quoted and
\soCalled are aliases for quoting commands. These commands
could be easily redefined for different formats. The package
also provides a footnote environment so that long footnotes can
be more cleanly separated from the main text. Because the
author is a music scholar, the package also includes some
macros for musical symbols and other basic notations for
musical analysis.

date: 2018-05-24 19:39:42 +0000


%package -n texlive-semantic-markup-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn47837
Release:        0
Summary:        Documentation for texlive-semantic-markup
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-semantic-markup-doc
This package includes the documentation for texlive-semantic-markup

%post -n texlive-semantic-markup
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-semantic-markup 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-semantic-markup
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-semantic-markup-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/semantic-markup/README
%{_texmfdistdir}/doc/latex/semantic-markup/semantic-markup.pdf
%{_texmfdistdir}/doc/latex/semantic-markup/semantic-markup.tex

%files -n texlive-semantic-markup
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/semantic-markup/semantic-markup.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-semantic-markup-%{texlive_version}.%{texlive_noarch}.svn47837-%{release}-zypper
%endif

%package -n texlive-semaphor
Version:        %{texlive_version}.%{texlive_noarch}.svn18651
Release:        0
Summary:        Semaphore alphabet font
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(updmap.cfg)
#!BuildIgnore:  tex(updmap.cfg)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(updmap.cfg)
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires:       texlive-semaphor-fonts >= %{texlive_version}
Recommends:     texlive-semaphor-doc >= %{texlive_version}
Provides:       tex(il2semaf.fd)
Provides:       tex(semaf.fd)
Provides:       tex(semaf.map)
Provides:       tex(semaf.tex)
Provides:       tex(smfb10.enc)
Provides:       tex(smfb10.tfm)
Provides:       tex(smfbsl10.enc)
Provides:       tex(smfbsl10.tfm)
Provides:       tex(smfeb10.enc)
Provides:       tex(smfeb10.tfm)
Provides:       tex(smfebsl10.enc)
Provides:       tex(smfebsl10.tfm)
Provides:       tex(smfer10.enc)
Provides:       tex(smfer10.tfm)
Provides:       tex(smfesl10.enc)
Provides:       tex(smfesl10.tfm)
Provides:       tex(smfett10.enc)
Provides:       tex(smfett10.tfm)
Provides:       tex(smfpb10.enc)
Provides:       tex(smfpb10.tfm)
Provides:       tex(smfpbsl10.enc)
Provides:       tex(smfpbsl10.tfm)
Provides:       tex(smfpr10.enc)
Provides:       tex(smfpr10.tfm)
Provides:       tex(smfpsl10.enc)
Provides:       tex(smfpsl10.tfm)
Provides:       tex(smfptt10.enc)
Provides:       tex(smfptt10.tfm)
Provides:       tex(smfr10.enc)
Provides:       tex(smfr10.tfm)
Provides:       tex(smfsl10.enc)
Provides:       tex(smfsl10.tfm)
Provides:       tex(smftt10.enc)
Provides:       tex(smftt10.tfm)
Provides:       tex(t-type-semaf.tex)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source150:      semaphor.tar.xz
Source151:      semaphor.doc.tar.xz

%description -n texlive-semaphor
These fonts represent semaphore in a highly schematic, but very
clear, fashion. The fonts are provided as Metafont source, and
in both OpenType and Adobe Type 1 formats.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-semaphor-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn18651
Release:        0
Summary:        Documentation for texlive-semaphor
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-semaphor-doc
This package includes the documentation for texlive-semaphor


%package -n texlive-semaphor-fonts
Version:        %{texlive_version}.%{texlive_noarch}.svn18651
Release:        0
Summary:        Severed fonts for texlive-semaphor
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Fonts
Url:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-semaphor-fonts
The  separated fonts package for texlive-semaphor
%post -n texlive-semaphor
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMixedMap semaf.map' >> /var/run/texlive/run-updmap

%postun -n texlive-semaphor 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMixedMap semaf.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-semaphor
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-semaphor-fonts
%files -n texlive-semaphor-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/semaphor/README
%{_texmfdistdir}/doc/fonts/semaphor/example.pdf
%{_texmfdistdir}/doc/fonts/semaphor/example.tex
%{_texmfdistdir}/doc/fonts/semaphor/test-context.pdf
%{_texmfdistdir}/doc/fonts/semaphor/test-context.tex

%files -n texlive-semaphor
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/afm/public/semaphor/smfb10.afm
%{_texmfdistdir}/fonts/afm/public/semaphor/smfbsl10.afm
%{_texmfdistdir}/fonts/afm/public/semaphor/smfeb10.afm
%{_texmfdistdir}/fonts/afm/public/semaphor/smfebsl10.afm
%{_texmfdistdir}/fonts/afm/public/semaphor/smfer10.afm
%{_texmfdistdir}/fonts/afm/public/semaphor/smfesl10.afm
%{_texmfdistdir}/fonts/afm/public/semaphor/smfett10.afm
%{_texmfdistdir}/fonts/afm/public/semaphor/smfpb10.afm
%{_texmfdistdir}/fonts/afm/public/semaphor/smfpbsl10.afm
%{_texmfdistdir}/fonts/afm/public/semaphor/smfpr10.afm
%{_texmfdistdir}/fonts/afm/public/semaphor/smfpsl10.afm
%{_texmfdistdir}/fonts/afm/public/semaphor/smfptt10.afm
%{_texmfdistdir}/fonts/afm/public/semaphor/smfr10-1.afm
%{_texmfdistdir}/fonts/afm/public/semaphor/smfr10-2.afm
%{_texmfdistdir}/fonts/afm/public/semaphor/smfr10.afm
%{_texmfdistdir}/fonts/afm/public/semaphor/smfsl10.afm
%{_texmfdistdir}/fonts/afm/public/semaphor/smftt10.afm
%{_texmfdistdir}/fonts/enc/dvips/semaphor/smfb10.enc
%{_texmfdistdir}/fonts/enc/dvips/semaphor/smfbsl10.enc
%{_texmfdistdir}/fonts/enc/dvips/semaphor/smfeb10.enc
%{_texmfdistdir}/fonts/enc/dvips/semaphor/smfebsl10.enc
%{_texmfdistdir}/fonts/enc/dvips/semaphor/smfer10.enc
%{_texmfdistdir}/fonts/enc/dvips/semaphor/smfesl10.enc
%{_texmfdistdir}/fonts/enc/dvips/semaphor/smfett10.enc
%{_texmfdistdir}/fonts/enc/dvips/semaphor/smfpb10.enc
%{_texmfdistdir}/fonts/enc/dvips/semaphor/smfpbsl10.enc
%{_texmfdistdir}/fonts/enc/dvips/semaphor/smfpr10.enc
%{_texmfdistdir}/fonts/enc/dvips/semaphor/smfpsl10.enc
%{_texmfdistdir}/fonts/enc/dvips/semaphor/smfptt10.enc
%{_texmfdistdir}/fonts/enc/dvips/semaphor/smfr10.enc
%{_texmfdistdir}/fonts/enc/dvips/semaphor/smfsl10.enc
%{_texmfdistdir}/fonts/enc/dvips/semaphor/smftt10.enc
%{_texmfdistdir}/fonts/map/dvips/semaphor/semaf.map
%verify(link) %{_texmfdistdir}/fonts/opentype/public/semaphor/smfb10.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/semaphor/smfbsl10.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/semaphor/smfeb10.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/semaphor/smfebsl10.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/semaphor/smfer10.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/semaphor/smfesl10.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/semaphor/smfett10.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/semaphor/smfpb10.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/semaphor/smfpbsl10.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/semaphor/smfpr10.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/semaphor/smfpsl10.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/semaphor/smfptt10.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/semaphor/smfr10.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/semaphor/smfsl10.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/semaphor/smftt10.otf
%{_texmfdistdir}/fonts/source/public/semaphor/Makefile
%{_texmfdistdir}/fonts/source/public/semaphor/README
%{_texmfdistdir}/fonts/source/public/semaphor/metafont/semaf.mf
%{_texmfdistdir}/fonts/source/public/semaphor/metafont/smfbf10.mf
%{_texmfdistdir}/fonts/source/public/semaphor/metafont/smfebf10.mf
%{_texmfdistdir}/fonts/source/public/semaphor/metafont/smfer10.mf
%{_texmfdistdir}/fonts/source/public/semaphor/metafont/smfesl10.mf
%{_texmfdistdir}/fonts/source/public/semaphor/metafont/smfett10.mf
%{_texmfdistdir}/fonts/source/public/semaphor/metafont/smfpbf10.mf
%{_texmfdistdir}/fonts/source/public/semaphor/metafont/smfpr10.mf
%{_texmfdistdir}/fonts/source/public/semaphor/metafont/smfpsl10.mf
%{_texmfdistdir}/fonts/source/public/semaphor/metafont/smfptt10.mf
%{_texmfdistdir}/fonts/source/public/semaphor/metafont/smfr10.mf
%{_texmfdistdir}/fonts/source/public/semaphor/metafont/smfsl10.mf
%{_texmfdistdir}/fonts/source/public/semaphor/metafont/smftt10.mf
%{_texmfdistdir}/fonts/source/public/semaphor/pfb2otf.pe
%{_texmfdistdir}/fonts/source/public/semaphor/semaf.mp
%{_texmfdistdir}/fonts/source/public/semaphor/smfb10.mp
%{_texmfdistdir}/fonts/source/public/semaphor/smfbsl10.mp
%{_texmfdistdir}/fonts/source/public/semaphor/smfeb10.mp
%{_texmfdistdir}/fonts/source/public/semaphor/smfebsl10.mp
%{_texmfdistdir}/fonts/source/public/semaphor/smfer10.mp
%{_texmfdistdir}/fonts/source/public/semaphor/smfesl10.mp
%{_texmfdistdir}/fonts/source/public/semaphor/smfett10.mp
%{_texmfdistdir}/fonts/source/public/semaphor/smfpb10.mp
%{_texmfdistdir}/fonts/source/public/semaphor/smfpbsl10.mp
%{_texmfdistdir}/fonts/source/public/semaphor/smfpr10.mp
%{_texmfdistdir}/fonts/source/public/semaphor/smfpsl10.mp
%{_texmfdistdir}/fonts/source/public/semaphor/smfptt10.mp
%{_texmfdistdir}/fonts/source/public/semaphor/smfr10.mp
%{_texmfdistdir}/fonts/source/public/semaphor/smfsl10.mp
%{_texmfdistdir}/fonts/source/public/semaphor/smftt10.mp
%{_texmfdistdir}/fonts/tfm/public/semaphor/smfb10.tfm
%{_texmfdistdir}/fonts/tfm/public/semaphor/smfbsl10.tfm
%{_texmfdistdir}/fonts/tfm/public/semaphor/smfeb10.tfm
%{_texmfdistdir}/fonts/tfm/public/semaphor/smfebsl10.tfm
%{_texmfdistdir}/fonts/tfm/public/semaphor/smfer10.tfm
%{_texmfdistdir}/fonts/tfm/public/semaphor/smfesl10.tfm
%{_texmfdistdir}/fonts/tfm/public/semaphor/smfett10.tfm
%{_texmfdistdir}/fonts/tfm/public/semaphor/smfpb10.tfm
%{_texmfdistdir}/fonts/tfm/public/semaphor/smfpbsl10.tfm
%{_texmfdistdir}/fonts/tfm/public/semaphor/smfpr10.tfm
%{_texmfdistdir}/fonts/tfm/public/semaphor/smfpsl10.tfm
%{_texmfdistdir}/fonts/tfm/public/semaphor/smfptt10.tfm
%{_texmfdistdir}/fonts/tfm/public/semaphor/smfr10.tfm
%{_texmfdistdir}/fonts/tfm/public/semaphor/smfsl10.tfm
%{_texmfdistdir}/fonts/tfm/public/semaphor/smftt10.tfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/semaphor/smfb10.pfb
%{_texmfdistdir}/fonts/type1/public/semaphor/smfb10.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/semaphor/smfbsl10.pfb
%{_texmfdistdir}/fonts/type1/public/semaphor/smfbsl10.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/semaphor/smfeb10.pfb
%{_texmfdistdir}/fonts/type1/public/semaphor/smfeb10.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/semaphor/smfebsl10.pfb
%{_texmfdistdir}/fonts/type1/public/semaphor/smfebsl10.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/semaphor/smfer10.pfb
%{_texmfdistdir}/fonts/type1/public/semaphor/smfer10.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/semaphor/smfesl10.pfb
%{_texmfdistdir}/fonts/type1/public/semaphor/smfesl10.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/semaphor/smfett10.pfb
%{_texmfdistdir}/fonts/type1/public/semaphor/smfett10.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/semaphor/smfpb10.pfb
%{_texmfdistdir}/fonts/type1/public/semaphor/smfpb10.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/semaphor/smfpbsl10.pfb
%{_texmfdistdir}/fonts/type1/public/semaphor/smfpbsl10.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/semaphor/smfpr10.pfb
%{_texmfdistdir}/fonts/type1/public/semaphor/smfpr10.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/semaphor/smfpsl10.pfb
%{_texmfdistdir}/fonts/type1/public/semaphor/smfpsl10.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/semaphor/smfptt10.pfb
%{_texmfdistdir}/fonts/type1/public/semaphor/smfptt10.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/semaphor/smfr10.pfb
%{_texmfdistdir}/fonts/type1/public/semaphor/smfr10.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/semaphor/smfsl10.pfb
%{_texmfdistdir}/fonts/type1/public/semaphor/smfsl10.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/semaphor/smftt10.pfb
%{_texmfdistdir}/fonts/type1/public/semaphor/smftt10.pfm
%{_texmfdistdir}/tex/context/third/semaphor/t-type-semaf.tex
%{_texmfdistdir}/tex/latex/semaphor/il2semaf.fd
%{_texmfdistdir}/tex/latex/semaphor/semaf.fd
%{_texmfdistdir}/tex/plain/semaphor/semaf.tex

%files -n texlive-semaphor-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-semaphor
%config %{_sysconfdir}/fonts/conf.avail/58-texlive-semaphor.conf
%config %{_sysconfdir}/fonts/conf.d/55-texlive-semaphor.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-semaphor/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-semaphor/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-semaphor/fonts.scale
%{_datadir}/fonts/texlive-semaphor/smfb10.otf
%{_datadir}/fonts/texlive-semaphor/smfbsl10.otf
%{_datadir}/fonts/texlive-semaphor/smfeb10.otf
%{_datadir}/fonts/texlive-semaphor/smfebsl10.otf
%{_datadir}/fonts/texlive-semaphor/smfer10.otf
%{_datadir}/fonts/texlive-semaphor/smfesl10.otf
%{_datadir}/fonts/texlive-semaphor/smfett10.otf
%{_datadir}/fonts/texlive-semaphor/smfpb10.otf
%{_datadir}/fonts/texlive-semaphor/smfpbsl10.otf
%{_datadir}/fonts/texlive-semaphor/smfpr10.otf
%{_datadir}/fonts/texlive-semaphor/smfpsl10.otf
%{_datadir}/fonts/texlive-semaphor/smfptt10.otf
%{_datadir}/fonts/texlive-semaphor/smfr10.otf
%{_datadir}/fonts/texlive-semaphor/smfsl10.otf
%{_datadir}/fonts/texlive-semaphor/smftt10.otf
%{_datadir}/fonts/texlive-semaphor/smfb10.pfb
%{_datadir}/fonts/texlive-semaphor/smfbsl10.pfb
%{_datadir}/fonts/texlive-semaphor/smfeb10.pfb
%{_datadir}/fonts/texlive-semaphor/smfebsl10.pfb
%{_datadir}/fonts/texlive-semaphor/smfer10.pfb
%{_datadir}/fonts/texlive-semaphor/smfesl10.pfb
%{_datadir}/fonts/texlive-semaphor/smfett10.pfb
%{_datadir}/fonts/texlive-semaphor/smfpb10.pfb
%{_datadir}/fonts/texlive-semaphor/smfpbsl10.pfb
%{_datadir}/fonts/texlive-semaphor/smfpr10.pfb
%{_datadir}/fonts/texlive-semaphor/smfpsl10.pfb
%{_datadir}/fonts/texlive-semaphor/smfptt10.pfb
%{_datadir}/fonts/texlive-semaphor/smfr10.pfb
%{_datadir}/fonts/texlive-semaphor/smfsl10.pfb
%{_datadir}/fonts/texlive-semaphor/smftt10.pfb
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-semaphor-fonts-%{texlive_version}.%{texlive_noarch}.svn18651-%{release}-zypper
%endif

%package -n texlive-seminar
Version:        %{texlive_version}.%{texlive_noarch}.1.62svn34011
Release:        0
Summary:        Make overhead slides
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-seminar-doc >= %{texlive_version}
Provides:       tex(npsfont.sty)
Provides:       tex(sem-a4.sty)
Provides:       tex(sem-dem.sty)
Provides:       tex(sem-page.sty)
Provides:       tex(semcolor.sty)
Provides:       tex(semhelv.sty)
Provides:       tex(seminar.cls)
Provides:       tex(seminar.sty)
Provides:       tex(semlayer.sty)
Provides:       tex(semlcmss.sty)
Provides:       tex(semrot.sty)
Provides:       tex(slidesec.sty)
Provides:       tex(tvz-code.sty)
Provides:       tex(tvz-hax.sty)
Provides:       tex(tvz-user.sty)
Requires:       tex(article.cls)
Requires:       tex(article.sty)
Requires:       tex(doc.sty)
Requires:       tex(fancybox.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(pst-ovl.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source152:      seminar.tar.xz
Source153:      seminar.doc.tar.xz

%description -n texlive-seminar
A class that produces overhead slides (transparencies), with
many facilities. The class requires availability of the
fancybox package. Seminar is also the basis of other classes,
such as prosper. In fact, seminar is not nowadays reckoned a
good basis for a presentation -- users are advised to use more
recent classes such as powerdot or beamer, both of which are
tuned to 21st-century presentation styles. Note that the
seminar distribution relies on the xcomment package, which was
once part of the bundle, but now has a separate existence.

date: 2018-01-06 11:14:59 +0000


%package -n texlive-seminar-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.62svn34011
Release:        0
Summary:        Documentation for texlive-seminar
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-seminar-doc
This package includes the documentation for texlive-seminar

%post -n texlive-seminar
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-seminar 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-seminar
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-seminar-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/seminar/Changes
%{_texmfdistdir}/doc/latex/seminar/README
%{_texmfdistdir}/doc/latex/seminar/run.sh
%{_texmfdistdir}/doc/latex/seminar/sem-code.tex
%{_texmfdistdir}/doc/latex/seminar/sem-make.tex
%{_texmfdistdir}/doc/latex/seminar/seminar-doc.pdf
%{_texmfdistdir}/doc/latex/seminar/seminar-doc.tex
%{_texmfdistdir}/doc/latex/seminar/seminar.bg3
%{_texmfdistdir}/doc/latex/seminar/seminar.con
%{_texmfdistdir}/doc/latex/seminar/seminar.doc
%{_texmfdistdir}/doc/latex/seminar/semlayer.doc
%{_texmfdistdir}/doc/latex/seminar/semsamp1.pdf
%{_texmfdistdir}/doc/latex/seminar/semsamp1.tex
%{_texmfdistdir}/doc/latex/seminar/semsamp2.pdf
%{_texmfdistdir}/doc/latex/seminar/semsamp2.tex
%{_texmfdistdir}/doc/latex/seminar/semsamp3.pdf
%{_texmfdistdir}/doc/latex/seminar/semsamp3.tex

%files -n texlive-seminar
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/seminar/npsfont.sty
%{_texmfdistdir}/tex/latex/seminar/sem-a4.sty
%{_texmfdistdir}/tex/latex/seminar/sem-dem.sty
%{_texmfdistdir}/tex/latex/seminar/sem-page.sty
%{_texmfdistdir}/tex/latex/seminar/semcolor.sty
%{_texmfdistdir}/tex/latex/seminar/semhelv.sty
%{_texmfdistdir}/tex/latex/seminar/seminar.bg2
%{_texmfdistdir}/tex/latex/seminar/seminar.bug
%{_texmfdistdir}/tex/latex/seminar/seminar.cls
%{_texmfdistdir}/tex/latex/seminar/seminar.sty
%{_texmfdistdir}/tex/latex/seminar/semlayer.sty
%{_texmfdistdir}/tex/latex/seminar/semlcmss.sty
%{_texmfdistdir}/tex/latex/seminar/semrot.sty
%{_texmfdistdir}/tex/latex/seminar/slidesec.sty
%{_texmfdistdir}/tex/latex/seminar/tvz-code.sty
%{_texmfdistdir}/tex/latex/seminar/tvz-hax.sty
%{_texmfdistdir}/tex/latex/seminar/tvz-user.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-seminar-%{texlive_version}.%{texlive_noarch}.1.62svn34011-%{release}-zypper
%endif

%package -n texlive-semioneside
Version:        %{texlive_version}.%{texlive_noarch}.0.0.41svn15878
Release:        0
Summary:        Put only special contents on left-hand pages in two sided layout
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-semioneside-doc >= %{texlive_version}
Provides:       tex(semioneside.sty)
Requires:       tex(afterpage.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source154:      semioneside.tar.xz
Source155:      semioneside.doc.tar.xz

%description -n texlive-semioneside
This package supports the preparation of semi one sided
documents. That is, two sided documents, where all text is
output on right-hand pages--as in a one-sided documents--and
only special contents are output on left-hand pages on user
request, e.g., floating objects.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-semioneside-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.41svn15878
Release:        0
Summary:        Documentation for texlive-semioneside
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-semioneside-doc
This package includes the documentation for texlive-semioneside

%post -n texlive-semioneside
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-semioneside 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-semioneside
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-semioneside-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/semioneside/README
%{_texmfdistdir}/doc/latex/semioneside/example.tex
%{_texmfdistdir}/doc/latex/semioneside/figure.mp
%{_texmfdistdir}/doc/latex/semioneside/semioneside.pdf

%files -n texlive-semioneside
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/semioneside/semioneside.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-semioneside-%{texlive_version}.%{texlive_noarch}.0.0.41svn15878-%{release}-zypper
%endif

%package -n texlive-semproc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn37568
Release:        0
Summary:        Seminar proceedings
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-semproc-doc >= %{texlive_version}
Provides:       tex(semproc.cls)
Requires:       tex(biblatex.sty)
Requires:       tex(bookmark.sty)
Requires:       tex(csquotes.sty)
Requires:       tex(etoc.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(scrreprt.cls)
Requires:       tex(xcolor.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source156:      semproc.tar.xz
Source157:      semproc.doc.tar.xz

%description -n texlive-semproc
The package provides functionality for typesetting seminar
proceedings based on KOMA-Script's scrreprt class and etoc. It
offers an alternative to \chapter that typesets the speaker and
if necessary the typist of the notes for the talk in question.
Moreover, the class provides two types of table of contents. A
global table of contents showing only the talks of the seminar
and the respective speakers and a local table of contents for
each talk showing the sections and subsections of the
respective talk.

date: 2017-11-12 10:01:19 +0000


%package -n texlive-semproc-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn37568
Release:        0
Summary:        Documentation for texlive-semproc
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-semproc-doc
This package includes the documentation for texlive-semproc

%post -n texlive-semproc
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-semproc 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-semproc
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-semproc-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/semproc/README.txt
%{_texmfdistdir}/doc/latex/semproc/example.bib
%{_texmfdistdir}/doc/latex/semproc/example.tex
%{_texmfdistdir}/doc/latex/semproc/semproc.hd
%{_texmfdistdir}/doc/latex/semproc/semproc.pdf

%files -n texlive-semproc
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/semproc/semproc.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-semproc-%{texlive_version}.%{texlive_noarch}.0.0.1svn37568-%{release}-zypper
%endif

%package -n texlive-sepfootnotes
Version:        %{texlive_version}.%{texlive_noarch}.0.0.3csvn41732
Release:        0
Summary:        Support footnotes and endnotes from separate files
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-sepfootnotes-doc >= %{texlive_version}
Provides:       tex(sepfootnotes.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source158:      sepfootnotes.tar.xz
Source159:      sepfootnotes.doc.tar.xz

%description -n texlive-sepfootnotes
The package supports footnotes and endnotes from separate
files. This is achieved with commands \sepfootnotecontent and
\sepfootnote; the former defines the content of a note, while
the latter typesets that note.

date: 2016-07-19 14:05:59 +0000


%package -n texlive-sepfootnotes-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.3csvn41732
Release:        0
Summary:        Documentation for texlive-sepfootnotes
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-sepfootnotes-doc
This package includes the documentation for texlive-sepfootnotes

%post -n texlive-sepfootnotes
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-sepfootnotes 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-sepfootnotes
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-sepfootnotes-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/sepfootnotes/README
%{_texmfdistdir}/doc/latex/sepfootnotes/sepfootnotes.pdf
%{_texmfdistdir}/doc/latex/sepfootnotes/sepfootnotes.tex

%files -n texlive-sepfootnotes
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/sepfootnotes/sepfootnotes.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-sepfootnotes-%{texlive_version}.%{texlive_noarch}.0.0.3csvn41732-%{release}-zypper
%endif

%package -n texlive-sepnum
Version:        %{texlive_version}.%{texlive_noarch}.2.0svn20186
Release:        0
Summary:        Print numbers in a "friendly" format
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-sepnum-doc >= %{texlive_version}
Provides:       tex(sepnum.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source160:      sepnum.tar.xz
Source161:      sepnum.doc.tar.xz

%description -n texlive-sepnum
Provides a command to print a number with (potentially
different) separators every three digits in the parts either
side of the decimal point (the point itself is also
configurable). The macro is fully expandable and not fragile
(unless one of the separators is). There is also a command
\sepnumform, that may be used when defining \the<counter>
macros.

date: 2018-01-06 11:14:59 +0000


%package -n texlive-sepnum-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.0svn20186
Release:        0
Summary:        Documentation for texlive-sepnum
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-sepnum-doc
This package includes the documentation for texlive-sepnum

%post -n texlive-sepnum
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-sepnum 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-sepnum
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-sepnum-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/sepnum/sepnum-doc.pdf
%{_texmfdistdir}/doc/latex/sepnum/sepnum-doc.tex

%files -n texlive-sepnum
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/sepnum/sepnum.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-sepnum-%{texlive_version}.%{texlive_noarch}.2.0svn20186-%{release}-zypper
%endif

%package -n texlive-seqsplit
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn15878
Release:        0
Summary:        Split long sequences of characters in a neutral way
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-seqsplit-doc >= %{texlive_version}
Provides:       tex(seqsplit.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source162:      seqsplit.tar.xz
Source163:      seqsplit.doc.tar.xz

%description -n texlive-seqsplit
When one needs to type long sequences of letters (such as in
base-sequences in genes) or of numbers (such as calculations of
transcendental numbers), there's no obvious break points to be
found. The package provides a command \seqsplit, which makes
its argument splittable anywhere, and then leaves the TeX
paragraph-maker to do the splitting. While the package may
obviously be used to typeset DNA sequences, the user may
consider the dnaseq as a rather more powerful alternative.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-seqsplit-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn15878
Release:        0
Summary:        Documentation for texlive-seqsplit
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-seqsplit-doc
This package includes the documentation for texlive-seqsplit

%post -n texlive-seqsplit
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-seqsplit 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-seqsplit
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-seqsplit-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/seqsplit/README
%{_texmfdistdir}/doc/latex/seqsplit/seqsplit.pdf

%files -n texlive-seqsplit
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/seqsplit/seqsplit.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-seqsplit-%{texlive_version}.%{texlive_noarch}.0.0.1svn15878-%{release}-zypper
%endif

%package -n texlive-serbian-apostrophe
Version:        %{texlive_version}.%{texlive_noarch}.svn23799
Release:        0
Summary:        Commands for Serbian words with apostrophes
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-serbian-apostrophe-doc >= %{texlive_version}
Provides:       tex(serbian-apostrophe.sty)
Requires:       tex(tipa.sty)
Requires:       tex(xspace.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source164:      serbian-apostrophe.tar.xz
Source165:      serbian-apostrophe.doc.tar.xz

%description -n texlive-serbian-apostrophe
The package provides a collection of commands (whose names are
Serbian words) whose expansion is the Serbian word with
appropriate apostrophes.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-serbian-apostrophe-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn23799
Release:        0
Summary:        Documentation for texlive-serbian-apostrophe
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-serbian-apostrophe-doc
This package includes the documentation for texlive-serbian-apostrophe

%post -n texlive-serbian-apostrophe
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-serbian-apostrophe 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-serbian-apostrophe
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-serbian-apostrophe-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/serbian-apostrophe/README
%{_texmfdistdir}/doc/latex/serbian-apostrophe/apostrophe-list.pdf
%{_texmfdistdir}/doc/latex/serbian-apostrophe/apostrophe-list.tex
%{_texmfdistdir}/doc/latex/serbian-apostrophe/serbian-apostrophe.pdf
%{_texmfdistdir}/doc/latex/serbian-apostrophe/serbian-apostrophe.tex

%files -n texlive-serbian-apostrophe
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/serbian-apostrophe/serbian-apostrophe.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-serbian-apostrophe-%{texlive_version}.%{texlive_noarch}.svn23799-%{release}-zypper
%endif

%package -n texlive-serbian-date-lat
Version:        %{texlive_version}.%{texlive_noarch}.svn23446
Release:        0
Summary:        Updated date typesetting for Serbian
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-serbian-date-lat-doc >= %{texlive_version}
Provides:       tex(serbian-date-lat.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source166:      serbian-date-lat.tar.xz
Source167:      serbian-date-lat.doc.tar.xz

%description -n texlive-serbian-date-lat
Babel defines dates for Serbian texts, in Latin script. The
style it uses does not match current practices. The present
package defines a \date command that solves the problem.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-serbian-date-lat-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn23446
Release:        0
Summary:        Documentation for texlive-serbian-date-lat
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-serbian-date-lat-doc
This package includes the documentation for texlive-serbian-date-lat

%post -n texlive-serbian-date-lat
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-serbian-date-lat 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-serbian-date-lat
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-serbian-date-lat-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/serbian-date-lat/README
%{_texmfdistdir}/doc/latex/serbian-date-lat/SerbianDateLat.pdf
%{_texmfdistdir}/doc/latex/serbian-date-lat/SerbianDateLat.tex
%{_texmfdistdir}/doc/latex/serbian-date-lat/TestDateLat.pdf
%{_texmfdistdir}/doc/latex/serbian-date-lat/TestDateLat.tex

%files -n texlive-serbian-date-lat
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/serbian-date-lat/serbian-date-lat.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-serbian-date-lat-%{texlive_version}.%{texlive_noarch}.svn23446-%{release}-zypper
%endif

%package -n texlive-serbian-def-cyr
Version:        %{texlive_version}.%{texlive_noarch}.svn23734
Release:        0
Summary:        Serbian cyrillic localization
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-serbian-def-cyr-doc >= %{texlive_version}
Provides:       tex(serbian-def-cyr.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(inputenc.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source168:      serbian-def-cyr.tar.xz
Source169:      serbian-def-cyr.doc.tar.xz

%description -n texlive-serbian-def-cyr
This package provides abstract, chapter, title, date etc, for
serbian language in cyrillic scripts in T2A encoding and cp1251
code pages.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-serbian-def-cyr-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn23734
Release:        0
Summary:        Documentation for texlive-serbian-def-cyr
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-serbian-def-cyr-doc
This package includes the documentation for texlive-serbian-def-cyr

%post -n texlive-serbian-def-cyr
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-serbian-def-cyr 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-serbian-def-cyr
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-serbian-def-cyr-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/serbian-def-cyr/README
%{_texmfdistdir}/doc/latex/serbian-def-cyr/proba.pdf
%{_texmfdistdir}/doc/latex/serbian-def-cyr/proba.tex
%{_texmfdistdir}/doc/latex/serbian-def-cyr/usage.pdf
%{_texmfdistdir}/doc/latex/serbian-def-cyr/usage.tex

%files -n texlive-serbian-def-cyr
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/serbian-def-cyr/serbian-def-cyr.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-serbian-def-cyr-%{texlive_version}.%{texlive_noarch}.svn23734-%{release}-zypper
%endif

%package -n texlive-serbian-lig
Version:        %{texlive_version}.%{texlive_noarch}.svn48197
Release:        0
Summary:        Control ligatures in Serbian
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-serbian-lig-doc >= %{texlive_version}
Provides:       tex(serbian-lig.sty)
Requires:       tex(xspace.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source170:      serbian-lig.tar.xz
Source171:      serbian-lig.doc.tar.xz

%description -n texlive-serbian-lig
The package suppresses fi and fl (and other ligatures) in
Serbian text written using Roman script.

date: 2018-07-14 12:14:22 +0000


%package -n texlive-serbian-lig-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn48197
Release:        0
Summary:        Documentation for texlive-serbian-lig
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-serbian-lig-doc
This package includes the documentation for texlive-serbian-lig

%post -n texlive-serbian-lig
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-serbian-lig 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-serbian-lig
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-serbian-lig-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/serbian-lig/Changes.txt
%{_texmfdistdir}/doc/latex/serbian-lig/README.txt
%{_texmfdistdir}/doc/latex/serbian-lig/lig-list.pdf
%{_texmfdistdir}/doc/latex/serbian-lig/lig-list.tex
%{_texmfdistdir}/doc/latex/serbian-lig/serbian-lig.pdf
%{_texmfdistdir}/doc/latex/serbian-lig/serbian-lig.tex

%files -n texlive-serbian-lig
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/serbian-lig/serbian-lig.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-serbian-lig-%{texlive_version}.%{texlive_noarch}.svn48197-%{release}-zypper
%endif

%package -n texlive-sesamanuel
Version:        %{texlive_version}.%{texlive_noarch}.0.0.6svn36613
Release:        0
Summary:        Class and package for sesamath books or paper
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-sesamanuel-doc >= %{texlive_version}
Provides:       tex(sesamanuel.cls)
Provides:       tex(sesamanuel.sty)
Provides:       tex(sesamanuelTIKZ.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(babel.sty)
Requires:       tex(book.cls)
Requires:       tex(colortbl.sty)
Requires:       tex(crop.sty)
Requires:       tex(esvect.sty)
Requires:       tex(etex.sty)
Requires:       tex(eurosym.sty)
Requires:       tex(fancyhdr.sty)
Requires:       tex(fancyvrb.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(helvet.sty)
Requires:       tex(ifmtarg.sty)
Requires:       tex(inputenc.sty)
Requires:       tex(longtable.sty)
Requires:       tex(mathpazo.sty)
Requires:       tex(mathrsfs.sty)
Requires:       tex(mathtools.sty)
Requires:       tex(multicol.sty)
Requires:       tex(multido.sty)
Requires:       tex(multirow.sty)
Requires:       tex(numprint.sty)
Requires:       tex(pgf.sty)
Requires:       tex(pifont.sty)
Requires:       tex(pst-all.sty)
Requires:       tex(pstricks-add.sty)
Requires:       tex(tabularx.sty)
Requires:       tex(tikz.sty)
Requires:       tex(tkz-tab.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xunicode.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source172:      sesamanuel.tar.xz
Source173:      sesamanuel.doc.tar.xz

%description -n texlive-sesamanuel
The package contains a sesamanuel class which could be used to
compose a student's classroom book with LaTeX, and also a
sesamanuelTIKZ style to be used for TikZ pictures in the
sesamath book.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-sesamanuel-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.6svn36613
Release:        0
Summary:        Documentation for texlive-sesamanuel
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Provides:       locale(texlive-sesamanuel-doc:fr)

%description -n texlive-sesamanuel-doc
This package includes the documentation for texlive-sesamanuel

%post -n texlive-sesamanuel
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-sesamanuel 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-sesamanuel
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-sesamanuel-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/sesamanuel/Lisez.moi
%{_texmfdistdir}/doc/latex/sesamanuel/logotex.eps
%{_texmfdistdir}/doc/latex/sesamanuel/read.me
%{_texmfdistdir}/doc/latex/sesamanuel/sesamanuel.pdf
%{_texmfdistdir}/doc/latex/sesamanuel/sesamath-doc-fr.pdf
%{_texmfdistdir}/doc/latex/sesamanuel/sesamath-doc-fr.tex
%{_texmfdistdir}/doc/latex/sesamanuel/tiger.eps

%files -n texlive-sesamanuel
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/sesamanuel/sesamanuel.cls
%{_texmfdistdir}/tex/latex/sesamanuel/sesamanuel.sty
%{_texmfdistdir}/tex/latex/sesamanuel/sesamanuelTIKZ.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-sesamanuel-%{texlive_version}.%{texlive_noarch}.0.0.6svn36613-%{release}-zypper
%endif

%package -n texlive-sesstime
Version:        %{texlive_version}.%{texlive_noarch}.1.12svn49750
Release:        0
Summary:        Session and timing information in lecture notes
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-sesstime-doc >= %{texlive_version}
Provides:       tex(sesstime.sty)
Requires:       tex(keyval.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source174:      sesstime.tar.xz
Source175:      sesstime.doc.tar.xz

%description -n texlive-sesstime
This LaTeX2e package makes it possible to add timing marks to
lecture notes in order to help managing the time available for
presenting a given section of the document. It also provides
tools to record and estimate the progress throughout the
course.

date: 2019-01-17 23:03:38 +0000


%package -n texlive-sesstime-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.12svn49750
Release:        0
Summary:        Documentation for texlive-sesstime
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-sesstime-doc
This package includes the documentation for texlive-sesstime

%post -n texlive-sesstime
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-sesstime 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-sesstime
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-sesstime-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/sesstime/README.txt
%{_texmfdistdir}/doc/latex/sesstime/sesstime.pdf
%{_texmfdistdir}/doc/latex/sesstime/stimsamp.tex
%{_texmfdistdir}/doc/latex/sesstime/stimsmp3.tex
%{_texmfdistdir}/doc/latex/sesstime/stimsmp4.tex

%files -n texlive-sesstime
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/sesstime/sesstime.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-sesstime-%{texlive_version}.%{texlive_noarch}.1.12svn49750-%{release}-zypper
%endif

%package -n texlive-setdeck
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn40613
Release:        0
Summary:        Typeset cards for Set
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-setdeck-doc >= %{texlive_version}
Provides:       tex(setdeck.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xcolor.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source176:      setdeck.tar.xz
Source177:      setdeck.doc.tar.xz

%description -n texlive-setdeck
The package will typeset cards for use in a game of Set.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-setdeck-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn40613
Release:        0
Summary:        Documentation for texlive-setdeck
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-setdeck-doc
This package includes the documentation for texlive-setdeck

%post -n texlive-setdeck
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-setdeck 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-setdeck
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-setdeck-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/setdeck/README
%{_texmfdistdir}/doc/latex/setdeck/setdeck.pdf
%{_texmfdistdir}/doc/latex/setdeck/setdeck.tex

%files -n texlive-setdeck
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/setdeck/setdeck.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-setdeck-%{texlive_version}.%{texlive_noarch}.0.0.1svn40613-%{release}-zypper
%endif

%package -n texlive-setspace
Version:        %{texlive_version}.%{texlive_noarch}.6.7asvn24881
Release:        0
Summary:        Set space between lines
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-setspace-doc >= %{texlive_version}
Provides:       tex(setspace.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source178:      setspace.tar.xz
Source179:      setspace.doc.tar.xz

%description -n texlive-setspace
Provides support for setting the spacing between lines in a
document. Package options include singlespacing,
onehalfspacing, and doublespacing. Alternatively the spacing
can be changed as required with the \singlespacing,
\onehalfspacing, and \doublespacing commands. Other size
spacings also available.

date: 2018-09-14 16:16:49 +0000


%package -n texlive-setspace-doc
Version:        %{texlive_version}.%{texlive_noarch}.6.7asvn24881
Release:        0
Summary:        Documentation for texlive-setspace
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-setspace-doc
This package includes the documentation for texlive-setspace

%post -n texlive-setspace
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-setspace 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-setspace
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-setspace-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/setspace/README
%{_texmfdistdir}/doc/latex/setspace/setspace-test.tex

%files -n texlive-setspace
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/setspace/setspace.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-setspace-%{texlive_version}.%{texlive_noarch}.6.7asvn24881-%{release}-zypper
%endif

%package -n texlive-seuthesis
Version:        %{texlive_version}.%{texlive_noarch}.2.1.2svn33042
Release:        0
Summary:        LaTeX template for theses at Southeastern University
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-seuthesis-doc >= %{texlive_version}
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source180:      seuthesis.tar.xz
Source181:      seuthesis.doc.tar.xz

%description -n texlive-seuthesis
This template is for theses at Southeastern University,
Nanjing, China.

date: 2018-04-05 04:13:24 +0000


%package -n texlive-seuthesis-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.1.2svn33042
Release:        0
Summary:        Documentation for texlive-seuthesis
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Provides:       locale(texlive-seuthesis-doc:zh)

%description -n texlive-seuthesis-doc
This package includes the documentation for texlive-seuthesis

%post -n texlive-seuthesis
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-seuthesis 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-seuthesis
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-seuthesis-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/seuthesis/Makefile
%{_texmfdistdir}/doc/latex/seuthesis/a3cover/A3cover.tex
%{_texmfdistdir}/doc/latex/seuthesis/a3cover/A4cover.tex
%{_texmfdistdir}/doc/latex/seuthesis/a3cover/a3cover.sh
%{_texmfdistdir}/doc/latex/seuthesis/a3cover/a4cover.sh
%{_texmfdistdir}/doc/latex/seuthesis/a3cover/bookspine_hor.tex
%{_texmfdistdir}/doc/latex/seuthesis/a3cover/bookspine_ver.tex
%{_texmfdistdir}/doc/latex/seuthesis/figures/back-cover.png
%{_texmfdistdir}/doc/latex/seuthesis/figures/doctor-hwzs.pdf
%{_texmfdistdir}/doc/latex/seuthesis/figures/doctor.png
%{_texmfdistdir}/doc/latex/seuthesis/figures/engineering.png
%{_texmfdistdir}/doc/latex/seuthesis/figures/front-cover.jpg
%{_texmfdistdir}/doc/latex/seuthesis/figures/master-hwzs.pdf
%{_texmfdistdir}/doc/latex/seuthesis/figures/master.png
%{_texmfdistdir}/doc/latex/seuthesis/figures/seu-badge-logo.eps
%{_texmfdistdir}/doc/latex/seuthesis/figures/seu-badge-logo.pdf
%{_texmfdistdir}/doc/latex/seuthesis/figures/seu-color-logo.png
%{_texmfdistdir}/doc/latex/seuthesis/figures/seu-text-logo.eps
%{_texmfdistdir}/doc/latex/seuthesis/figures/seu-text-logo.png
%{_texmfdistdir}/doc/latex/seuthesis/sample-bachelor.pdf
%{_texmfdistdir}/doc/latex/seuthesis/sample-doctor.pdf
%{_texmfdistdir}/doc/latex/seuthesis/sample-master.pdf
%{_texmfdistdir}/doc/latex/seuthesis/sample.tex
%{_texmfdistdir}/doc/latex/seuthesis/seuthesis.bib
%{_texmfdistdir}/doc/latex/seuthesis/seuthesis.pdf
%{_texmfdistdir}/doc/latex/seuthesis/zharticle/scrsize9pt.clo
%{_texmfdistdir}/doc/latex/seuthesis/zharticle/zharticle.bst
%{_texmfdistdir}/doc/latex/seuthesis/zharticle/zharticle.cfg
%{_texmfdistdir}/doc/latex/seuthesis/zharticle/zharticle.cls

%files -n texlive-seuthesis
%defattr(-,root,root,755)
%{_texmfdistdir}/bibtex/bst/seuthesis/seuthesis.bst
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-seuthesis-%{texlive_version}.%{texlive_noarch}.2.1.2svn33042-%{release}-zypper
%endif

%package -n texlive-seuthesix
Version:        %{texlive_version}.%{texlive_noarch}.1.0.1svn40088
Release:        0
Summary:        LaTeX class for theses at Southeast University, Nanjing, China
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-seuthesix-doc >= %{texlive_version}
Provides:       tex(seuthesix.cfg)
Provides:       tex(seuthesix.cls)
Requires:       tex(algorithm.sty)
Requires:       tex(algorithmic.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(amsthm.sty)
Requires:       tex(bm.sty)
Requires:       tex(caption.sty)
Requires:       tex(ctexrep.cls)
Requires:       tex(eso-pic.sty)
Requires:       tex(eucal.sty)
Requires:       tex(eufrak.sty)
Requires:       tex(fancyhdr.sty)
Requires:       tex(geometry.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(natbib.sty)
Requires:       tex(nomencl.sty)
Requires:       tex(tocloft.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source182:      seuthesix.tar.xz
Source183:      seuthesix.doc.tar.xz

%description -n texlive-seuthesix
This project provides a LaTeX document class as well as a
bibliography style file for typesetting theses at the Southeast
University, Nanjing, China. It is based on the seuthesis
package which, according to the author of seuthesix, is buggy
and has not been maintained for some time.

date: 2017-04-18 03:31:40 +0000


%package -n texlive-seuthesix-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0.1svn40088
Release:        0
Summary:        Documentation for texlive-seuthesix
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Provides:       locale(texlive-seuthesix-doc:zh)

%description -n texlive-seuthesix-doc
This package includes the documentation for texlive-seuthesix

%post -n texlive-seuthesix
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-seuthesix 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-seuthesix
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-seuthesix-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/seuthesix/LICENCE
%{_texmfdistdir}/doc/latex/seuthesix/README
%{_texmfdistdir}/doc/latex/seuthesix/figures/back-cover.png
%{_texmfdistdir}/doc/latex/seuthesix/figures/doctor-hwzs.pdf
%{_texmfdistdir}/doc/latex/seuthesix/figures/doctor.png
%{_texmfdistdir}/doc/latex/seuthesix/figures/engineering.png
%{_texmfdistdir}/doc/latex/seuthesix/figures/front-cover.jpg
%{_texmfdistdir}/doc/latex/seuthesix/figures/lxfbook.jpg
%{_texmfdistdir}/doc/latex/seuthesix/figures/master-hwzs.pdf
%{_texmfdistdir}/doc/latex/seuthesix/figures/master.png
%{_texmfdistdir}/doc/latex/seuthesix/figures/seu-badge-logo.eps
%{_texmfdistdir}/doc/latex/seuthesix/figures/seu-badge-logo.pdf
%{_texmfdistdir}/doc/latex/seuthesix/figures/seu-color-logo.png
%{_texmfdistdir}/doc/latex/seuthesix/figures/seu-text-logo.eps
%{_texmfdistdir}/doc/latex/seuthesix/figures/seu-text-logo.png
%{_texmfdistdir}/doc/latex/seuthesix/figures/seu_logo.jpg
%{_texmfdistdir}/doc/latex/seuthesix/make_pdf.sh
%{_texmfdistdir}/doc/latex/seuthesix/makefile_engineering.sh
%{_texmfdistdir}/doc/latex/seuthesix/makefile_masters.sh
%{_texmfdistdir}/doc/latex/seuthesix/makefile_phd.sh
%{_texmfdistdir}/doc/latex/seuthesix/rules.pdf
%{_texmfdistdir}/doc/latex/seuthesix/sample_engineering.pdf
%{_texmfdistdir}/doc/latex/seuthesix/sample_engineering.tex
%{_texmfdistdir}/doc/latex/seuthesix/sample_masters.pdf
%{_texmfdistdir}/doc/latex/seuthesix/sample_masters.tex
%{_texmfdistdir}/doc/latex/seuthesix/sample_phd.pdf
%{_texmfdistdir}/doc/latex/seuthesix/sample_phd.tex
%{_texmfdistdir}/doc/latex/seuthesix/seuthesix.bib
%{_texmfdistdir}/doc/latex/seuthesix/seuthesix.pdf
%{_texmfdistdir}/doc/latex/seuthesix/seuthesix.tex

%files -n texlive-seuthesix
%defattr(-,root,root,755)
%{_texmfdistdir}/bibtex/bst/seuthesix/seuthesix.bst
%{_texmfdistdir}/tex/latex/seuthesix/seuthesix.cfg
%{_texmfdistdir}/tex/latex/seuthesix/seuthesix.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-seuthesix-%{texlive_version}.%{texlive_noarch}.1.0.1svn40088-%{release}-zypper
%endif

%package -n texlive-sexam
Version:        %{texlive_version}.%{texlive_noarch}.1svn46628
Release:        0
Summary:        Package for typesetting arabic exam scripts
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-sexam-doc >= %{texlive_version}
Provides:       tex(bacex.sty)
Provides:       tex(sexam.sty)
Provides:       tex(wexam.sty)
Requires:       tex(amsfonts.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(background.sty)
Requires:       tex(bclogo.sty)
Requires:       tex(ean13isbn.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(fancybox.sty)
Requires:       tex(fmtcount.sty)
Requires:       tex(fouriernc.sty)
Requires:       tex(geometry.sty)
Requires:       tex(listings.sty)
Requires:       tex(mathpple.sty)
Requires:       tex(mathrsfs.sty)
Requires:       tex(mathtools.sty)
Requires:       tex(moreenum.sty)
Requires:       tex(multicol.sty)
Requires:       tex(pifont.sty)
Requires:       tex(polyglossia.sty)
Requires:       tex(setspace.sty)
Requires:       tex(tikz.sty)
Requires:       tex(ulem.sty)
Requires:       tex(wasysym.sty)
Requires:       tex(yagusylo.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source184:      sexam.tar.xz
Source185:      sexam.doc.tar.xz

%description -n texlive-sexam
The package provides a modified version of the exam package
made compatible with XeLaTeX/polyglossia to typesetting arabic
exams.

date: 2018-02-15 03:59:58 +0000


%package -n texlive-sexam-doc
Version:        %{texlive_version}.%{texlive_noarch}.1svn46628
Release:        0
Summary:        Documentation for texlive-sexam
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Provides:       locale(texlive-sexam-doc:ar-dz)

%description -n texlive-sexam-doc
This package includes the documentation for texlive-sexam

%post -n texlive-sexam
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-sexam 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-sexam
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-sexam-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/xelatex/sexam/01.JPG
%{_texmfdistdir}/doc/xelatex/sexam/10.png
%{_texmfdistdir}/doc/xelatex/sexam/11.png
%{_texmfdistdir}/doc/xelatex/sexam/2.JPG
%{_texmfdistdir}/doc/xelatex/sexam/3.JPG
%{_texmfdistdir}/doc/xelatex/sexam/4.JPG
%{_texmfdistdir}/doc/xelatex/sexam/6.JPG
%{_texmfdistdir}/doc/xelatex/sexam/7.JPG
%{_texmfdistdir}/doc/xelatex/sexam/8.JPG
%{_texmfdistdir}/doc/xelatex/sexam/9.JPG
%{_texmfdistdir}/doc/xelatex/sexam/README.txt
%{_texmfdistdir}/doc/xelatex/sexam/bac_template-DZ.pdf
%{_texmfdistdir}/doc/xelatex/sexam/bac_template-DZ.tex
%{_texmfdistdir}/doc/xelatex/sexam/exam_with_sexam_ar-DZ.pdf
%{_texmfdistdir}/doc/xelatex/sexam/exam_with_sexam_ar-DZ.tex
%{_texmfdistdir}/doc/xelatex/sexam/exam_with_wexam_ar-DZ.pdf
%{_texmfdistdir}/doc/xelatex/sexam/exam_with_wexam_ar-DZ.tex
%{_texmfdistdir}/doc/xelatex/sexam/sexam_wexam_doc_ar.pdf
%{_texmfdistdir}/doc/xelatex/sexam/sexam_wexam_doc_ar.tex

%files -n texlive-sexam
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/xelatex/sexam/bacex.sty
%{_texmfdistdir}/tex/xelatex/sexam/sexam.sty
%{_texmfdistdir}/tex/xelatex/sexam/wexam.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-sexam-%{texlive_version}.%{texlive_noarch}.1svn46628-%{release}-zypper
%endif

%package -n texlive-sf298
Version:        %{texlive_version}.%{texlive_noarch}.1.3svn41653
Release:        0
Summary:        Standard form 298
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-sf298-doc >= %{texlive_version}
Provides:       tex(sf298.sty)
Requires:       tex(fancyhdr.sty)
Requires:       tex(multicol.sty)
Requires:       tex(totpages.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source186:      sf298.tar.xz
Source187:      sf298.doc.tar.xz

%description -n texlive-sf298
A LaTeX package for generating a completed standard form 298
(Rev. 8-98) as prescribed by ANSI Std. Z39.18 for report
documentation as part of a document delivered, for instance, on
a U.S. government contract.

date: 2018-01-06 11:14:59 +0000


%package -n texlive-sf298-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.3svn41653
Release:        0
Summary:        Documentation for texlive-sf298
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-sf298-doc
This package includes the documentation for texlive-sf298

%post -n texlive-sf298
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-sf298 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-sf298
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-sf298-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/sf298/Makefile
%{_texmfdistdir}/doc/latex/sf298/README.txt
%{_texmfdistdir}/doc/latex/sf298/sample298.tex
%{_texmfdistdir}/doc/latex/sf298/sf298.pdf

%files -n texlive-sf298
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/sf298/sf298.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-sf298-%{texlive_version}.%{texlive_noarch}.1.3svn41653-%{release}-zypper
%endif

%package -n texlive-sffms
Version:        %{texlive_version}.%{texlive_noarch}.2.0svn15878
Release:        0
Summary:        Typesetting science fiction/fantasy manuscripts
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-sffms-doc >= %{texlive_version}
Provides:       tex(sffdumb.sty)
Provides:       tex(sffms.cls)
Provides:       tex(sffsmart.sty)
Requires:       tex(fancyhdr.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(geometry.sty)
Requires:       tex(report.cls)
Requires:       tex(setspace.sty)
Requires:       tex(ulem.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source188:      sffms.tar.xz
Source189:      sffms.doc.tar.xz

%description -n texlive-sffms
The class is designed for typesetting science fiction and
fantasy manuscripts. Sffms now includes several options for
specific publishers as well as extensive documentation aimed at
new LaTeX users.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-sffms-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.0svn15878
Release:        0
Summary:        Documentation for texlive-sffms
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-sffms-doc
This package includes the documentation for texlive-sffms

%post -n texlive-sffms
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-sffms 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-sffms
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-sffms-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/sffms/README
%{_texmfdistdir}/doc/latex/sffms/blind.tex
%{_texmfdistdir}/doc/latex/sffms/sffms_manual.pdf

%files -n texlive-sffms
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/sffms/sffdumb.sty
%{_texmfdistdir}/tex/latex/sffms/sffms.cls
%{_texmfdistdir}/tex/latex/sffms/sffsmart.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-sffms-%{texlive_version}.%{texlive_noarch}.2.0svn15878-%{release}-zypper
%endif

%package -n texlive-sfg
Version:        %{texlive_version}.%{texlive_noarch}.0.0.91svn20209
Release:        0
Summary:        Draw signal flow graphs
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-sfg-doc >= %{texlive_version}
Provides:       tex(sfg.sty)
Requires:       tex(fp.sty)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source190:      sfg.tar.xz
Source191:      sfg.doc.tar.xz

%description -n texlive-sfg
Defines some commands to draw signal flow graphs as used by
electrical and electronics engineers and graph theorists.
Requires fp and pstricks packages (and a relatively fast
machine).

date: 2018-09-15 12:02:36 +0000


%package -n texlive-sfg-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.91svn20209
Release:        0
Summary:        Documentation for texlive-sfg
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-sfg-doc
This package includes the documentation for texlive-sfg

%post -n texlive-sfg
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-sfg 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-sfg
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-sfg-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/sfg/Changes
%{_texmfdistdir}/doc/latex/sfg/README
%{_texmfdistdir}/doc/latex/sfg/sfg-doc.pdf
%{_texmfdistdir}/doc/latex/sfg/sfg-doc.tex
%{_texmfdistdir}/doc/latex/sfg/sfg_test.tex

%files -n texlive-sfg
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/sfg/sfg.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-sfg-%{texlive_version}.%{texlive_noarch}.0.0.91svn20209-%{release}-zypper
%endif

%package -n texlive-sfmath
Version:        %{texlive_version}.%{texlive_noarch}.0.0.8svn15878
Release:        0
Summary:        Sans-serif mathematics
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Provides:       tex(sfmath.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source192:      sfmath.tar.xz

%description -n texlive-sfmath
sfmath is a simple package for sans serif maths in documents.
After including the package, all maths of the current document
is displayed with sans serif fonts.

date: 2016-06-24 17:18:15 +0000

%post -n texlive-sfmath
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-sfmath 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-sfmath
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-sfmath
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/sfmath/sfmath.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-sfmath-%{texlive_version}.%{texlive_noarch}.0.0.8svn15878-%{release}-zypper
%endif

%package -n texlive-sgame
Version:        %{texlive_version}.%{texlive_noarch}.2.15svn30959
Release:        0
Summary:        LaTeX style for typesetting strategic games
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-sgame-doc >= %{texlive_version}
Provides:       tex(sgame.sty)
Provides:       tex(sgamevar.sty)
Requires:       tex(color.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source193:      sgame.tar.xz
Source194:      sgame.doc.tar.xz

%description -n texlive-sgame
Formats strategic games. For a 2x2 game, for example, the
input: \begin{game}{2}{2} &$L$ &$M$\\ $T$ &$2,2$ &$2,0$\\ $B$
&$3,0$ &$0,9$ \end{game} produces output with (a) boxes around
the payoffs, (b) payoff columns of equal width, and (c) payoffs
vertically centered within the boxes. Note that the game
environment will not work in the argument of another command.

date: 2017-04-18 03:31:40 +0000


%package -n texlive-sgame-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.15svn30959
Release:        0
Summary:        Documentation for texlive-sgame
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-sgame-doc
This package includes the documentation for texlive-sgame

%post -n texlive-sgame
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-sgame 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-sgame
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-sgame-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/sgame/README
%{_texmfdistdir}/doc/latex/sgame/sgame.pdf
%{_texmfdistdir}/doc/latex/sgame/sgame.tex

%files -n texlive-sgame
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/sgame/sgame.sty
%{_texmfdistdir}/tex/latex/sgame/sgamevar.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-sgame-%{texlive_version}.%{texlive_noarch}.2.15svn30959-%{release}-zypper
%endif

%package -n texlive-shade
Version:        %{texlive_version}.%{texlive_noarch}.1svn22212
Release:        0
Summary:        Shade pieces of text
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-shade-doc >= %{texlive_version}
Provides:       tex(shade.tex)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source195:      shade.tar.xz
Source196:      shade.doc.tar.xz

%description -n texlive-shade
The package provides a shaded backdrop to a box of text. It
uses a Metafont font (provided) which generates to appropriate
shading dependent on the resolution used in the Metafont
printer parameters.

date: 2018-01-06 11:14:59 +0000


%package -n texlive-shade-doc
Version:        %{texlive_version}.%{texlive_noarch}.1svn22212
Release:        0
Summary:        Documentation for texlive-shade
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Provides:       locale(texlive-shade-doc:en)

%description -n texlive-shade-doc
This package includes the documentation for texlive-shade

%post -n texlive-shade
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-shade 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-shade
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-shade-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/shade/README
%{_texmfdistdir}/doc/generic/shade/description.pdf
%{_texmfdistdir}/doc/generic/shade/description.tex

%files -n texlive-shade
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/source/public/shade/shade.mf
%{_texmfdistdir}/tex/generic/shade/shade.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-shade-%{texlive_version}.%{texlive_noarch}.1svn22212-%{release}-zypper
%endif

%package -n texlive-shadethm
Version:        %{texlive_version}.%{texlive_noarch}.svn20319
Release:        0
Summary:        Theorem environments that are shaded
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-shadethm-doc >= %{texlive_version}
Provides:       tex(shadethm.sty)
Requires:       tex(color.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source197:      shadethm.tar.xz
Source198:      shadethm.doc.tar.xz

%description -n texlive-shadethm
Extends the \newtheorem command. If you say
\newshadetheorem{theorem}{Theorem} in the preamble then your
regular \begin{theorem} .. \end{theorem} will produce a theorem
statement in a shaded box. It supports all the options of
\newtheorem, including forms \newshadetheorem{..}[..]{..} and
\newshadetheorem{..}{..}[..]. Environments declared using the
package require their body to remain on one page; the mdframed
package can frame and shade theorems, and its environments
break at the end of a page; users are generally recommended,
therefore, to use mdframed.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-shadethm-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn20319
Release:        0
Summary:        Documentation for texlive-shadethm
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-shadethm-doc
This package includes the documentation for texlive-shadethm

%post -n texlive-shadethm
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-shadethm 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-shadethm
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-shadethm-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/shadethm/1st_read.me
%{_texmfdistdir}/doc/latex/shadethm/shadetest.pdf
%{_texmfdistdir}/doc/latex/shadethm/shadetest.tex
%{_texmfdistdir}/doc/latex/shadethm/shadethm-doc.pdf
%{_texmfdistdir}/doc/latex/shadethm/shadethm-doc.tex

%files -n texlive-shadethm
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/shadethm/colored.sth
%{_texmfdistdir}/tex/latex/shadethm/shadein.sth
%{_texmfdistdir}/tex/latex/shadethm/shadethm.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-shadethm-%{texlive_version}.%{texlive_noarch}.svn20319-%{release}-zypper
%endif

%package -n texlive-shadow
Version:        %{texlive_version}.%{texlive_noarch}.svn20312
Release:        0
Summary:        Shadow boxes
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-shadow-doc >= %{texlive_version}
Provides:       tex(shadow.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source199:      shadow.tar.xz
Source200:      shadow.doc.tar.xz

%description -n texlive-shadow
Defines a command \shabox (analgous to \fbox), and supporting
mechanisms.

date: 2018-04-18 03:32:44 +0000


%package -n texlive-shadow-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn20312
Release:        0
Summary:        Documentation for texlive-shadow
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-shadow-doc
This package includes the documentation for texlive-shadow

%post -n texlive-shadow
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-shadow 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-shadow
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-shadow-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/shadow/shadow-doc.pdf
%{_texmfdistdir}/doc/latex/shadow/shadow-doc.tex

%files -n texlive-shadow
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/shadow/shadow.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-shadow-%{texlive_version}.%{texlive_noarch}.svn20312-%{release}-zypper
%endif

%package -n texlive-shadowtext
Version:        %{texlive_version}.%{texlive_noarch}.0.0.3svn26522
Release:        0
Summary:        Produce text with a shadow behind it
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-shadowtext-doc >= %{texlive_version}
Provides:       tex(shadowtext.sty)
Requires:       tex(color.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source201:      shadowtext.tar.xz
Source202:      shadowtext.doc.tar.xz

%description -n texlive-shadowtext
The package introduces a command \shadowtext, which adds a drop
shadow to the text that is given as its argument. The colour
and positioning of the shadow are customisable.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-shadowtext-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.3svn26522
Release:        0
Summary:        Documentation for texlive-shadowtext
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-shadowtext-doc
This package includes the documentation for texlive-shadowtext

%post -n texlive-shadowtext
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-shadowtext 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-shadowtext
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-shadowtext-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/shadowtext/README
%{_texmfdistdir}/doc/latex/shadowtext/shadowtext.pdf
%{_texmfdistdir}/doc/latex/shadowtext/shadowtext.tex

%files -n texlive-shadowtext
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/shadowtext/shadowtext.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-shadowtext-%{texlive_version}.%{texlive_noarch}.0.0.3svn26522-%{release}-zypper
%endif

%package -n texlive-shapepar
Version:        %{texlive_version}.%{texlive_noarch}.2.2svn30708
Release:        0
Summary:        A macro to typeset paragraphs in specific shapes
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-shapepar-doc >= %{texlive_version}
Provides:       tex(Canflagshape.def)
Provides:       tex(TeXshape.def)
Provides:       tex(candleshape.def)
Provides:       tex(dropshape.def)
Provides:       tex(shapepar.sty)
Provides:       tex(triangleshapes.def)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source203:      shapepar.tar.xz
Source204:      shapepar.doc.tar.xz

%description -n texlive-shapepar
\shapepar is a macro to typeset paragraphs in a specific shape.
The size is adjusted automatically so that the entire shape is
filled with text. There may not be displayed maths or
'\vadjust' material (no \vspace) in the argument of \shapepar.
The macros work for both LaTeX and plain TeX. For LaTeX,
specify \usepackage{shapepar}; for Plain, \input shapepar.sty.
\shapepar works in terms of user-defined shapes, though the
package does provide some predefined shapes: so you can form
any paragraph into the form of a heart by putting
\heartpar{sometext...} inside your document. The tedium of
creating these polygon definitions may be alleviated by using
the shapepatch extension to transfig which will convert xfig
output to \shapepar polygon form.

date: 2018-01-06 11:14:59 +0000


%package -n texlive-shapepar-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.2svn30708
Release:        0
Summary:        Documentation for texlive-shapepar
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-shapepar-doc
This package includes the documentation for texlive-shapepar

%post -n texlive-shapepar
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-shapepar 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-shapepar
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-shapepar-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/shapepar/README.shapepar
%{_texmfdistdir}/doc/generic/shapepar/proshap.py
%{_texmfdistdir}/doc/generic/shapepar/shapepar.ltx
%{_texmfdistdir}/doc/generic/shapepar/shapepar.pdf

%files -n texlive-shapepar
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/shapepar/Canflagshape.def
%{_texmfdistdir}/tex/generic/shapepar/TeXshape.def
%{_texmfdistdir}/tex/generic/shapepar/candleshape.def
%{_texmfdistdir}/tex/generic/shapepar/dropshape.def
%{_texmfdistdir}/tex/generic/shapepar/shapepar.sty
%{_texmfdistdir}/tex/generic/shapepar/triangleshapes.def
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-shapepar-%{texlive_version}.%{texlive_noarch}.2.2svn30708-%{release}-zypper
%endif

%package -n texlive-shapes
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn42428
Release:        0
Summary:        Draw polygons, reentrant stars, and fractions in circles with MetaPost
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-shapes-doc >= %{texlive_version}
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source205:      shapes.tar.xz
Source206:      shapes.doc.tar.xz

%description -n texlive-shapes
The shapes set of macros allows drawing regular polygons; their
corresponding reentrant stars in all their variations; and
fractionally filled circles (useful for visually demonstrating
the nature of fractions) in MetaPost.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-shapes-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn42428
Release:        0
Summary:        Documentation for texlive-shapes
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-shapes-doc
This package includes the documentation for texlive-shapes

%post -n texlive-shapes
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-shapes 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-shapes
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-shapes-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/metapost/shapes/CHANGES
%{_texmfdistdir}/doc/metapost/shapes/README
%{_texmfdistdir}/doc/metapost/shapes/lppl.txt
%{_texmfdistdir}/doc/metapost/shapes/shapes.pdf

%files -n texlive-shapes
%defattr(-,root,root,755)
%{_texmfdistdir}/metapost/shapes/shapes.mp
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-shapes-%{texlive_version}.%{texlive_noarch}.1.1svn42428-%{release}-zypper
%endif

%package -n texlive-shdoc
Version:        %{texlive_version}.%{texlive_noarch}.2.1bsvn41991
Release:        0
Summary:        Float environment to document the shell commands of a terminal session
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-shdoc-doc >= %{texlive_version}
Provides:       tex(shdoc.sty)
Requires:       tex(caption.sty)
Requires:       tex(float.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(mdframed.sty)
Requires:       tex(relsize.sty)
Requires:       tex(stringstrings.sty)
Requires:       tex(xcolor.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source207:      shdoc.tar.xz
Source208:      shdoc.doc.tar.xz

%description -n texlive-shdoc
The package provides a simple, though fancy float environment
to document terminal sessions -- like command executions or
shell operations. The look and feel of the package output
imitates the look of a shell prompt.

date: 2016-09-04 16:33:35 +0000


%package -n texlive-shdoc-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.1bsvn41991
Release:        0
Summary:        Documentation for texlive-shdoc
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-shdoc-doc
This package includes the documentation for texlive-shdoc

%post -n texlive-shdoc
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-shdoc 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-shdoc
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-shdoc-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/shdoc/README
%{_texmfdistdir}/doc/latex/shdoc/README.txt
%{_texmfdistdir}/doc/latex/shdoc/avrdude-log.save
%{_texmfdistdir}/doc/latex/shdoc/shdoc.pdf
%{_texmfdistdir}/doc/latex/shdoc/shreformat.sh

%files -n texlive-shdoc
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/shdoc/shdoc.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-shdoc-%{texlive_version}.%{texlive_noarch}.2.1bsvn41991-%{release}-zypper
%endif

%package -n texlive-shipunov
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn29349
Release:        0
Summary:        A collection of LaTeX packages and classes
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-shipunov-doc >= %{texlive_version}
Requires:       perl(File::Basename)
#!BuildIgnore:  perl(File::Basename)
Provides:       tex(altverse.sty)
Provides:       tex(autolist.sty)
Provides:       tex(biokey.sty)
Provides:       tex(biolist.sty)
Provides:       tex(boldline.sty)
Provides:       tex(cassete.cls)
Provides:       tex(classif2.sty)
Provides:       tex(drcaps.sty)
Provides:       tex(etiketka.cls)
Provides:       tex(flower.sty)
Provides:       tex(isyntax.sty)
Provides:       tex(numerus.sty)
Provides:       tex(punct.sty)
Provides:       tex(sltables.sty)
Provides:       tex(starfn.sty)
Requires:       tex(array.sty)
Requires:       tex(article.cls)
Requires:       tex(calc.sty)
Requires:       tex(footnpag.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(syntonly.sty)
Requires:       tex(xspace.sty)
Requires:       tex(xtab.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source209:      shipunov.tar.xz
Source210:      shipunov.doc.tar.xz

%description -n texlive-shipunov
The bundle collects packages and classes, along with one
bibliography style and examples and scripts for converting TeX
files. Many of the files in the collection are designed to
support field biologists and/or Russian writers, while others
have wider application. The collection includes (among others):
altverse, a simple verse typesetting package; autolist, which
provides various list formatting facilities; biokey, which
provides a mechanism for typesetting biological identification
lists; biolist, which typesets species lists; boldline, which
typesets heavier separating lines in tables; cassete, which
lays out audio cassette inserts; classif2, which typesets
classification lists; drcaps, which provides dropped capital
macros; etiketka, a class for typesetting business-card-sized
information (including business cards); flower, for typesetting
lists of flower formulae; isyntax; numerus; punct; sltables,
which develops on the stables package, for use in a LaTeX
context; and starfn.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-shipunov-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn29349
Release:        0
Summary:        Documentation for texlive-shipunov
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Provides:       locale(texlive-shipunov-doc:en)

%description -n texlive-shipunov-doc
This package includes the documentation for texlive-shipunov

%post -n texlive-shipunov
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-shipunov 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-shipunov
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-shipunov-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/shipunov/NEWS
%{_texmfdistdir}/doc/latex/shipunov/README
%{_texmfdistdir}/doc/latex/shipunov/altverse-ex-en.pdf
%{_texmfdistdir}/doc/latex/shipunov/altverse-ex-en.tex
%{_texmfdistdir}/doc/latex/shipunov/altverse-ex1-ru.pdf
%{_texmfdistdir}/doc/latex/shipunov/altverse-ex1-ru.tex
%{_texmfdistdir}/doc/latex/shipunov/altverse-ex2-ru.pdf
%{_texmfdistdir}/doc/latex/shipunov/altverse-ex2-ru.tex
%{_texmfdistdir}/doc/latex/shipunov/autolist-ex-en.pdf
%{_texmfdistdir}/doc/latex/shipunov/autolist-ex-en.tex
%{_texmfdistdir}/doc/latex/shipunov/autolist-ex-ru.pdf
%{_texmfdistdir}/doc/latex/shipunov/autolist-ex-ru.tex
%{_texmfdistdir}/doc/latex/shipunov/biokey-doc-en.pdf
%{_texmfdistdir}/doc/latex/shipunov/biokey-doc-en.tex
%{_texmfdistdir}/doc/latex/shipunov/biokey2html-doc-en.pdf
%{_texmfdistdir}/doc/latex/shipunov/biokey2html-doc-en.tex
%{_texmfdistdir}/doc/latex/shipunov/biokey2html-ex-en.html
%{_texmfdistdir}/doc/latex/shipunov/biokey2html-ex-en1.pdf
%{_texmfdistdir}/doc/latex/shipunov/biokey2html-ex-en2.pdf
%{_texmfdistdir}/doc/latex/shipunov/biolist-ex-en.pdf
%{_texmfdistdir}/doc/latex/shipunov/biolist-ex-en.tex
%{_texmfdistdir}/doc/latex/shipunov/boldline-ex-en.pdf
%{_texmfdistdir}/doc/latex/shipunov/boldline-ex-en.tex
%{_texmfdistdir}/doc/latex/shipunov/cassete-ex-ru.pdf
%{_texmfdistdir}/doc/latex/shipunov/cassete-ex-ru.tex
%{_texmfdistdir}/doc/latex/shipunov/classif2-ex-en.pdf
%{_texmfdistdir}/doc/latex/shipunov/classif2-ex-en.tex
%{_texmfdistdir}/doc/latex/shipunov/drcaps-ex-en.pdf
%{_texmfdistdir}/doc/latex/shipunov/drcaps-ex-en.tex
%{_texmfdistdir}/doc/latex/shipunov/etiketka-ex-ru.pdf
%{_texmfdistdir}/doc/latex/shipunov/etiketka-ex-ru.tex
%{_texmfdistdir}/doc/latex/shipunov/etiketka-ex1-en.pdf
%{_texmfdistdir}/doc/latex/shipunov/etiketka-ex1-en.tex
%{_texmfdistdir}/doc/latex/shipunov/etiketka-ex2-en.pdf
%{_texmfdistdir}/doc/latex/shipunov/etiketka-ex2-en.tex
%{_texmfdistdir}/doc/latex/shipunov/field-form-ex1-ru.pdf
%{_texmfdistdir}/doc/latex/shipunov/field-form-ex1-ru.tex
%{_texmfdistdir}/doc/latex/shipunov/field-form-ex2-ru.pdf
%{_texmfdistdir}/doc/latex/shipunov/field-form-ex2-ru.tex
%{_texmfdistdir}/doc/latex/shipunov/flower-ex-en-x.pdf
%{_texmfdistdir}/doc/latex/shipunov/flower-ex-en-x.tex
%{_texmfdistdir}/doc/latex/shipunov/flower-ex-en.pdf
%{_texmfdistdir}/doc/latex/shipunov/flower-ex-en.tex
%{_texmfdistdir}/doc/latex/shipunov/isyntax-ex-en.tex
%{_texmfdistdir}/doc/latex/shipunov/numerus-ex-ru.pdf
%{_texmfdistdir}/doc/latex/shipunov/numerus-ex-ru.tex
%{_texmfdistdir}/doc/latex/shipunov/punct-ex-en.pdf
%{_texmfdistdir}/doc/latex/shipunov/punct-ex-en.tex
%{_texmfdistdir}/doc/latex/shipunov/rusnat-doc-ru.pdf
%{_texmfdistdir}/doc/latex/shipunov/rusnat-doc-ru.tex
%{_texmfdistdir}/doc/latex/shipunov/rusnat-ex-ru.bib
%{_texmfdistdir}/doc/latex/shipunov/rusnat-ex1-ru.pdf
%{_texmfdistdir}/doc/latex/shipunov/rusnat-ex1-ru.tex
%{_texmfdistdir}/doc/latex/shipunov/rusnat-ex2-ru.pdf
%{_texmfdistdir}/doc/latex/shipunov/rusnat-ex2-ru.tex
%{_texmfdistdir}/doc/latex/shipunov/sltables-doc-en.pdf
%{_texmfdistdir}/doc/latex/shipunov/sltables-doc-en.tex
%{_texmfdistdir}/doc/latex/shipunov/starfn-ex-ru.pdf
%{_texmfdistdir}/doc/latex/shipunov/starfn-ex-ru.tex

%files -n texlive-shipunov
%defattr(-,root,root,755)
%{_texmfdistdir}/bibtex/bst/shipunov/rusnat.bst
%{_texmfdistdir}/scripts/shipunov/biokey2html.sh
%{_texmfdistdir}/scripts/shipunov/biokey2html1.pl
%{_texmfdistdir}/scripts/shipunov/biokey2html2.pl
%{_texmfdistdir}/scripts/shipunov/biokey2html3.pl
%{_texmfdistdir}/tex/latex/shipunov/altverse.sty
%{_texmfdistdir}/tex/latex/shipunov/autolist.sty
%{_texmfdistdir}/tex/latex/shipunov/biokey.sty
%{_texmfdistdir}/tex/latex/shipunov/biolist.sty
%{_texmfdistdir}/tex/latex/shipunov/boldline.sty
%{_texmfdistdir}/tex/latex/shipunov/cassete.cls
%{_texmfdistdir}/tex/latex/shipunov/classif2.sty
%{_texmfdistdir}/tex/latex/shipunov/drcaps.sty
%{_texmfdistdir}/tex/latex/shipunov/etiketka.cls
%{_texmfdistdir}/tex/latex/shipunov/flower.sty
%{_texmfdistdir}/tex/latex/shipunov/isyntax.sty
%{_texmfdistdir}/tex/latex/shipunov/numerus.sty
%{_texmfdistdir}/tex/latex/shipunov/punct.sty
%{_texmfdistdir}/tex/latex/shipunov/sltables.sty
%{_texmfdistdir}/tex/latex/shipunov/starfn.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-shipunov-%{texlive_version}.%{texlive_noarch}.1.1svn29349-%{release}-zypper
%endif

%package -n texlive-shobhika
Version:        %{texlive_version}.%{texlive_noarch}.1.05svn50555
Release:        0
Summary:        An OpenType Devanagari font designed for scholars
License:        OFL-1.1
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires:       texlive-shobhika-fonts >= %{texlive_version}
Recommends:     texlive-shobhika-doc >= %{texlive_version}
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source211:      shobhika.tar.xz
Source212:      shobhika.doc.tar.xz

%description -n texlive-shobhika
This package provides a free, open source, Unicode compliant,
OpenType font with support for Devanagari, Latin, and Cyrillic
scripts. It is available in two weights--regular and bold. The
font is designed with over 1600 Devanagari glyphs, including
support for over 1100 conjunct consonants, as well as vedic
accents. The Latin component of the font not only supports a
wide range of characters required for Roman transliteration of
Sanskrit, but also provides a subset of regularly used
mathematical symbols for scholars working with scientific and
technical documents. The project has been launched under the
auspices of the Science and Heritage Initiative (SandHI) at IIT
Bombay, and builds upon the following two fonts for its
Devanagari and Latin components respectively: (i) Yashomudra by
Rajya Marathi Vikas Samstha, and (ii) PT Serif by ParaType. We
would like to thank both these organisations for releasing
their fonts under the SIL Open Font Licence, which has enabled
us to create Shobhika.

date: 2019-03-23 10:09:58 +0000


%package -n texlive-shobhika-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.05svn50555
Release:        0
Summary:        Documentation for texlive-shobhika
License:        OFL-1.1
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-shobhika-doc
This package includes the documentation for texlive-shobhika


%package -n texlive-shobhika-fonts
Version:        %{texlive_version}.%{texlive_noarch}.1.05svn50555
Release:        0
Summary:        Severed fonts for texlive-shobhika
License:        OFL-1.1
Group:          Productivity/Publishing/TeX/Fonts
Url:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-shobhika-fonts
The  separated fonts package for texlive-shobhika
%post -n texlive-shobhika
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-shobhika 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-shobhika
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-shobhika-fonts
%files -n texlive-shobhika-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/shobhika/AUTHORS.txt
%{_texmfdistdir}/doc/fonts/shobhika/CONTRIBUTORS.txt
%{_texmfdistdir}/doc/fonts/shobhika/Copyright.txt
%{_texmfdistdir}/doc/fonts/shobhika/OFL.txt
%{_texmfdistdir}/doc/fonts/shobhika/README.md
%{_texmfdistdir}/doc/fonts/shobhika/shobhika.pdf
%{_texmfdistdir}/doc/fonts/shobhika/shobhika.tex

%files -n texlive-shobhika
%defattr(-,root,root,755)
%verify(link) %{_texmfdistdir}/fonts/opentype/public/shobhika/Shobhika-Bold.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/shobhika/Shobhika-Regular.otf

%files -n texlive-shobhika-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-shobhika
%config %{_sysconfdir}/fonts/conf.avail/58-texlive-shobhika.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-shobhika/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-shobhika/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-shobhika/fonts.scale
%{_datadir}/fonts/texlive-shobhika/Shobhika-Bold.otf
%{_datadir}/fonts/texlive-shobhika/Shobhika-Regular.otf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-shobhika-fonts-%{texlive_version}.%{texlive_noarch}.1.05svn50555-%{release}-zypper
%endif

%package -n texlive-short-math-guide
Version:        %{texlive_version}.%{texlive_noarch}.2.0svn46126
Release:        0
Summary:        Guide to using amsmath and related packages to typeset mathematical notation with LaTeX
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source213:      short-math-guide.doc.tar.xz

%description -n texlive-short-math-guide
The Short Math Guide is intended to be a concise introduction
to the use of the facilities provided by amsmath and various
other LaTeX packages for typesetting mathematical notation.
Originally created by Michael Downes of the American
Mathematical Society based only on amsmath, it has been brought
up to date with references to related packages and other useful
information.

date: 2017-12-24 16:24:22 +0000

%post -n texlive-short-math-guide
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-short-math-guide 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-short-math-guide
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-short-math-guide
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/short-math-guide/README
%{_texmfdistdir}/doc/latex/short-math-guide/short-math-guide.pdf
%{_texmfdistdir}/doc/latex/short-math-guide/short-math-guide.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-short-math-guide-%{texlive_version}.%{texlive_noarch}.2.0svn46126-%{release}-zypper
%endif

%package -n texlive-shorttoc
Version:        %{texlive_version}.%{texlive_noarch}.1.3svn15878
Release:        0
Summary:        Table of contents with different depths
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-shorttoc-doc >= %{texlive_version}
Provides:       tex(shorttoc.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source214:      shorttoc.tar.xz
Source215:      shorttoc.doc.tar.xz

%description -n texlive-shorttoc
A package to create another table of contents with a different
depth, useful in large documents where a detailed table of
contents should be accompanied by a shorter one, giving only a
general overview of the main topics in the document.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-shorttoc-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.3svn15878
Release:        0
Summary:        Documentation for texlive-shorttoc
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-shorttoc-doc
This package includes the documentation for texlive-shorttoc

%post -n texlive-shorttoc
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-shorttoc 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-shorttoc
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-shorttoc-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/shorttoc/00readme
%{_texmfdistdir}/doc/latex/shorttoc/shorttoc.pdf

%files -n texlive-shorttoc
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/shorttoc/shorttoc.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-shorttoc-%{texlive_version}.%{texlive_noarch}.1.3svn15878-%{release}-zypper
%endif

%package -n texlive-show2e
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn15878
Release:        0
Summary:        Variants of \show for LaTeX2e
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-show2e-doc >= %{texlive_version}
Provides:       tex(show2e.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source216:      show2e.tar.xz
Source217:      show2e.doc.tar.xz

%description -n texlive-show2e
This small package aims at making debugging (especially in an
interactive way) easier, by providing \show variants suited to
LaTeX2e commands (whether with optional arguments or robust)
and environments. The variant commands also display the
internal macros used by such commands, if any. The \showcs
variant helps with macros with exotic names.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-show2e-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn15878
Release:        0
Summary:        Documentation for texlive-show2e
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Provides:       locale(texlive-show2e-doc:fr;en)

%description -n texlive-show2e-doc
This package includes the documentation for texlive-show2e

%post -n texlive-show2e
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-show2e 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-show2e
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-show2e-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/show2e/README
%{_texmfdistdir}/doc/latex/show2e/show2e-fr.pdf
%{_texmfdistdir}/doc/latex/show2e/show2e.pdf

%files -n texlive-show2e
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/show2e/show2e.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-show2e-%{texlive_version}.%{texlive_noarch}.1.0svn15878-%{release}-zypper
%endif

%package -n texlive-showcharinbox
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn29803
Release:        0
Summary:        Show characters inside a box
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-showcharinbox-doc >= %{texlive_version}
Provides:       tex(showcharinbox.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source218:      showcharinbox.tar.xz
Source219:      showcharinbox.doc.tar.xz

%description -n texlive-showcharinbox
The package typesets a character inside a box, showing where
reference point is, and displaying width, height, and depth
information of the character. The output is like that on page
63 of "The TeXBook" or page 101 of "The METAFONTbook". The
package itself is motivated by Knuth's macros in the file
manmac.tex. Users should note that using a small size for the
character inside the box does not make any sense: use a large
size.

date: 2018-11-28 20:01:12 +0000


%package -n texlive-showcharinbox-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn29803
Release:        0
Summary:        Documentation for texlive-showcharinbox
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-showcharinbox-doc
This package includes the documentation for texlive-showcharinbox

%post -n texlive-showcharinbox
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-showcharinbox 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-showcharinbox
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-showcharinbox-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/showcharinbox/README
%{_texmfdistdir}/doc/latex/showcharinbox/showcharinbox.pdf

%files -n texlive-showcharinbox
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/showcharinbox/showcharinbox.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-showcharinbox-%{texlive_version}.%{texlive_noarch}.0.0.1svn29803-%{release}-zypper
%endif

%package -n texlive-showdim
Version:        %{texlive_version}.%{texlive_noarch}.1.2svn28918
Release:        0
Summary:        Variants on printing dimensions
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-showdim-doc >= %{texlive_version}
Provides:       tex(showdim.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source220:      showdim.tar.xz
Source221:      showdim.doc.tar.xz

%description -n texlive-showdim
A package for LaTeX providing a number of commands for printing
the value of a TeX dimension. For example,
\tenthpt{\baselineskip} yields the current value of
\baselineskip rounded to the nearest tenth of a point.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-showdim-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.2svn28918
Release:        0
Summary:        Documentation for texlive-showdim
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-showdim-doc
This package includes the documentation for texlive-showdim

%post -n texlive-showdim
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-showdim 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-showdim
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-showdim-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/showdim/README

%files -n texlive-showdim
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/showdim/showdim.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-showdim-%{texlive_version}.%{texlive_noarch}.1.2svn28918-%{release}-zypper
%endif

%package -n texlive-showexpl
Version:        %{texlive_version}.%{texlive_noarch}.0.0.3osvn42677
Release:        0
Summary:        Typesetting LaTeX source code
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-showexpl-doc >= %{texlive_version}
Provides:       tex(showexpl.sty)
Requires:       tex(calc.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(listings.sty)
Requires:       tex(varwidth.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source222:      showexpl.tar.xz
Source223:      showexpl.doc.tar.xz

%description -n texlive-showexpl
This package provides a way to typeset LaTeX source code and
the related result in the same document.

date: 2016-12-11 12:56:29 +0000


%package -n texlive-showexpl-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.3osvn42677
Release:        0
Summary:        Documentation for texlive-showexpl
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-showexpl-doc
This package includes the documentation for texlive-showexpl

%post -n texlive-showexpl
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-showexpl 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-showexpl
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-showexpl-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/showexpl/README
%{_texmfdistdir}/doc/latex/showexpl/result-picture.pdf
%{_texmfdistdir}/doc/latex/showexpl/showexpl-test.pdf
%{_texmfdistdir}/doc/latex/showexpl/showexpl-test.tex
%{_texmfdistdir}/doc/latex/showexpl/showexpl.pdf

%files -n texlive-showexpl
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/showexpl/showexpl.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-showexpl-%{texlive_version}.%{texlive_noarch}.0.0.3osvn42677-%{release}-zypper
%endif

%package -n texlive-showhyphens
Version:        %{texlive_version}.%{texlive_noarch}.0.0.5csvn39787
Release:        0
Summary:        Show all possible hyphenations in LuaLaTeX
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-showhyphens-doc >= %{texlive_version}
Provides:       tex(showhyphens.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(luatexbase.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source224:      showhyphens.tar.xz
Source225:      showhyphens.doc.tar.xz

%description -n texlive-showhyphens
With this package, LuaLaTeX will indicate all possible
hyphenations in the printed output.

date: 2016-12-18 07:34:28 +0000


%package -n texlive-showhyphens-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.5csvn39787
Release:        0
Summary:        Documentation for texlive-showhyphens
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-showhyphens-doc
This package includes the documentation for texlive-showhyphens

%post -n texlive-showhyphens
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-showhyphens 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-showhyphens
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-showhyphens-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/lualatex/showhyphens/README
%{_texmfdistdir}/doc/lualatex/showhyphens/showhyphens-doc.pdf
%{_texmfdistdir}/doc/lualatex/showhyphens/showhyphens-doc.tex
%{_texmfdistdir}/doc/lualatex/showhyphens/showhyphens-sample.pdf

%files -n texlive-showhyphens
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/lualatex/showhyphens/showhyphens.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-showhyphens-%{texlive_version}.%{texlive_noarch}.0.0.5csvn39787-%{release}-zypper
%endif

%package -n texlive-showlabels
Version:        %{texlive_version}.%{texlive_noarch}.1.8svn41322
Release:        0
Summary:        Show label commands in the margin
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-showlabels-doc >= %{texlive_version}
Provides:       tex(showlabels.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source226:      showlabels.tar.xz
Source227:      showlabels.doc.tar.xz

%description -n texlive-showlabels
This package helps you keep track of all the labels you define,
by putting the name of new labels into the margin whenever the
\label command is used. The package allows you to do the same
thing for other commands. The only one for which this is
obviously useful is the \cite command, but it's easy to do it
for others, such as the \ref or \begin commands.

date: 2018-01-06 11:14:59 +0000


%package -n texlive-showlabels-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.8svn41322
Release:        0
Summary:        Documentation for texlive-showlabels
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-showlabels-doc
This package includes the documentation for texlive-showlabels

%post -n texlive-showlabels
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-showlabels 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-showlabels
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-showlabels-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/showlabels/README
%{_texmfdistdir}/doc/latex/showlabels/VERSION
%{_texmfdistdir}/doc/latex/showlabels/lppl.txt
%{_texmfdistdir}/doc/latex/showlabels/showlabels.html
%{_texmfdistdir}/doc/latex/showlabels/showlabels.pdf
%{_texmfdistdir}/doc/latex/showlabels/style.css

%files -n texlive-showlabels
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/showlabels/showlabels.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-showlabels-%{texlive_version}.%{texlive_noarch}.1.8svn41322-%{release}-zypper
%endif

%package -n texlive-showtags
Version:        %{texlive_version}.%{texlive_noarch}.1.05svn20336
Release:        0
Summary:        Print the tags of bibliography entries
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-showtags-doc >= %{texlive_version}
Provides:       tex(showtags.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source228:      showtags.tar.xz
Source229:      showtags.doc.tar.xz

%description -n texlive-showtags
Prints the tag right-aligned on each line of the bibliography.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-showtags-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.05svn20336
Release:        0
Summary:        Documentation for texlive-showtags
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-showtags-doc
This package includes the documentation for texlive-showtags

%post -n texlive-showtags
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-showtags 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-showtags
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-showtags-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/showtags/showtags-doc.pdf
%{_texmfdistdir}/doc/latex/showtags/showtags-doc.tex

%files -n texlive-showtags
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/showtags/showtags.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-showtags-%{texlive_version}.%{texlive_noarch}.1.05svn20336-%{release}-zypper
%endif

%package -n texlive-shuffle
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn15878
Release:        0
Summary:        A symbol for the shuffle product
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-shuffle-doc >= %{texlive_version}
Provides:       tex(Ushuffle.fd)
Provides:       tex(shuffle.sty)
Provides:       tex(shuffle10.tfm)
Provides:       tex(shuffle7.tfm)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source230:      shuffle.tar.xz
Source231:      shuffle.doc.tar.xz

%description -n texlive-shuffle
The bundle provides a LaTeX package and a font (as Metafont
source) for the shuffle product which is used in some part of
mathematics and physics.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-shuffle-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn15878
Release:        0
Summary:        Documentation for texlive-shuffle
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-shuffle-doc
This package includes the documentation for texlive-shuffle

%post -n texlive-shuffle
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-shuffle 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-shuffle
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-shuffle-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/shuffle/README
%{_texmfdistdir}/doc/latex/shuffle/shuffle.pdf

%files -n texlive-shuffle
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/source/public/shuffle/shuffle.mf
%{_texmfdistdir}/fonts/source/public/shuffle/shuffle10.mf
%{_texmfdistdir}/fonts/source/public/shuffle/shuffle7.mf
%{_texmfdistdir}/fonts/tfm/public/shuffle/shuffle10.tfm
%{_texmfdistdir}/fonts/tfm/public/shuffle/shuffle7.tfm
%{_texmfdistdir}/tex/latex/shuffle/Ushuffle.fd
%{_texmfdistdir}/tex/latex/shuffle/shuffle.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-shuffle-%{texlive_version}.%{texlive_noarch}.1.0svn15878-%{release}-zypper
%endif

%package -n texlive-sidecap
Version:        %{texlive_version}.%{texlive_noarch}.1.6fsvn15878
Release:        0
Summary:        Typeset captions sideways
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-sidecap-doc >= %{texlive_version}
Provides:       tex(sidecap.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(ragged2e.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source232:      sidecap.tar.xz
Source233:      sidecap.doc.tar.xz

%description -n texlive-sidecap
Defines environments called SCfigure and SCtable (analogous to
figure and table) to typeset captions sideways. Options include
outercaption, innercaption, leftcaption and rightcaption.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-sidecap-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.6fsvn15878
Release:        0
Summary:        Documentation for texlive-sidecap
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-sidecap-doc
This package includes the documentation for texlive-sidecap

%post -n texlive-sidecap
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-sidecap 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-sidecap
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-sidecap-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/sidecap/README
%{_texmfdistdir}/doc/latex/sidecap/sc-test-common.tex
%{_texmfdistdir}/doc/latex/sidecap/sc-test1.tex
%{_texmfdistdir}/doc/latex/sidecap/sc-test2.tex
%{_texmfdistdir}/doc/latex/sidecap/sc-test3.tex
%{_texmfdistdir}/doc/latex/sidecap/sc-test4.tex
%{_texmfdistdir}/doc/latex/sidecap/sc-test5.tex
%{_texmfdistdir}/doc/latex/sidecap/sc-test6.tex
%{_texmfdistdir}/doc/latex/sidecap/sidecap.pdf

%files -n texlive-sidecap
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/sidecap/sidecap.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-sidecap-%{texlive_version}.%{texlive_noarch}.1.6fsvn15878-%{release}-zypper
%endif

%package -n texlive-sidenotes
Version:        %{texlive_version}.%{texlive_noarch}.1.00svn40658
Release:        0
Summary:        Typeset notes containing rich content, in the margin
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-sidenotes-doc >= %{texlive_version}
Provides:       tex(caesar_book.cls)
Provides:       tex(sidenotes.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(beramono.sty)
Requires:       tex(caption.sty)
Requires:       tex(changepage.sty)
Requires:       tex(color.sty)
Requires:       tex(enumitem.sty)
Requires:       tex(fancyhdr.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(geometry.sty)
Requires:       tex(helvet.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(l3keys2e.sty)
Requires:       tex(marginfix.sty)
Requires:       tex(marginnote.sty)
Requires:       tex(mathpazo.sty)
Requires:       tex(mhchem.sty)
Requires:       tex(microtype.sty)
Requires:       tex(morefloats.sty)
Requires:       tex(ragged2e.sty)
Requires:       tex(textcase.sty)
Requires:       tex(titlesec.sty)
Requires:       tex(titletoc.sty)
Requires:       tex(unicode-math.sty)
Requires:       tex(xparse.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source234:      sidenotes.tar.xz
Source235:      sidenotes.doc.tar.xz

%description -n texlive-sidenotes
The package allows typesetting of texts with notes, figures,
citations, captions and tables in the margin. This is common
(for example) in science text books.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-sidenotes-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.00svn40658
Release:        0
Summary:        Documentation for texlive-sidenotes
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-sidenotes-doc
This package includes the documentation for texlive-sidenotes

%post -n texlive-sidenotes
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-sidenotes 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-sidenotes
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-sidenotes-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/sidenotes/README
%{_texmfdistdir}/doc/latex/sidenotes/caesar_example.pdf
%{_texmfdistdir}/doc/latex/sidenotes/caesar_example.tex
%{_texmfdistdir}/doc/latex/sidenotes/sidenotes.pdf

%files -n texlive-sidenotes
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/sidenotes/caesar_book.cls
%{_texmfdistdir}/tex/latex/sidenotes/sidenotes.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-sidenotes-%{texlive_version}.%{texlive_noarch}.1.00svn40658-%{release}-zypper
%endif

%package -n texlive-sides
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        A LaTeX class for typesetting stage plays
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-sides-doc >= %{texlive_version}
Provides:       tex(sides.cls)
Requires:       tex(report.cls)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source236:      sides.tar.xz
Source237:      sides.doc.tar.xz

%description -n texlive-sides
This is a LaTeX class for typesetting stage plays, based on the
plari class written by Antti-Juhani Kaijanaho in 1998. It has
been updated and several formatting changes have been made to
it--most noticibly there are no longer orphans.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-sides-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Documentation for texlive-sides
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-sides-doc
This package includes the documentation for texlive-sides

%post -n texlive-sides
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-sides 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-sides
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-sides-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/sides/README
%{_texmfdistdir}/doc/latex/sides/sides-sample.pdf
%{_texmfdistdir}/doc/latex/sides/sides-sample.tex

%files -n texlive-sides
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/sides/sides.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-sides-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif

%package -n texlive-signchart
Version:        %{texlive_version}.%{texlive_noarch}.1.01svn39707
Release:        0
Summary:        Create beautifully typeset sign charts
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-signchart-doc >= %{texlive_version}
Provides:       tex(signchart.sty)
Requires:       tex(pgfplots.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xstring.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source238:      signchart.tar.xz
Source239:      signchart.doc.tar.xz

%description -n texlive-signchart
The package allows users to easily typeset beautiful looking
sign charts directly into their (La)TeX document.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-signchart-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.01svn39707
Release:        0
Summary:        Documentation for texlive-signchart
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-signchart-doc
This package includes the documentation for texlive-signchart

%post -n texlive-signchart
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-signchart 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-signchart
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-signchart-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/signchart/README.txt
%{_texmfdistdir}/doc/latex/signchart/signchart.pdf

%files -n texlive-signchart
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/signchart/signchart.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-signchart-%{texlive_version}.%{texlive_noarch}.1.01svn39707-%{release}-zypper
%endif

%package -n texlive-silence
Version:        %{texlive_version}.%{texlive_noarch}.1.5bsvn27028
Release:        0
Summary:        Selective filtering of error messages and warnings
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-silence-doc >= %{texlive_version}
Provides:       tex(silence.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source240:      silence.tar.xz
Source241:      silence.doc.tar.xz

%description -n texlive-silence
The package allows the user to filter out unwanted warnings and
error messages issued by LaTeX, packages and classes, so they
won't pop out when there's nothing one can do about them.
Filtering goes from the very broad ("avoid all messages by such
and such") to the fine-grained ("avoid messages that begin
with..."). Messages may be saved to an external file for later
reference.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-silence-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.5bsvn27028
Release:        0
Summary:        Documentation for texlive-silence
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-silence-doc
This package includes the documentation for texlive-silence

%post -n texlive-silence
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-silence 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-silence
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-silence-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/silence/README
%{_texmfdistdir}/doc/latex/silence/silence-doc.pdf

%files -n texlive-silence
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/silence/silence.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-silence-%{texlive_version}.%{texlive_noarch}.1.5bsvn27028-%{release}-zypper
%endif

%package -n texlive-simple-resume-cv
Version:        %{texlive_version}.%{texlive_noarch}.svn43057
Release:        0
Summary:        Template for a simple resume or curriculum vitae (CV), in XeLaTeX
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-simple-resume-cv-doc >= %{texlive_version}
Provides:       tex(simpleresumecv.cls)
Requires:       tex(article.cls)
Requires:       tex(color.sty)
Requires:       tex(datetime2.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(hyphenat.sty)
Requires:       tex(xltxtra.sty)
Requires:       tex(xunicode.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source242:      simple-resume-cv.tar.xz
Source243:      simple-resume-cv.doc.tar.xz

%description -n texlive-simple-resume-cv
Template for a simple resume or curriculum vitae (CV), in
XeLaTeX. Simple template that can be further customized or
extended, with numerous examples.

date: 2017-01-28 04:55:17 +0000


%package -n texlive-simple-resume-cv-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn43057
Release:        0
Summary:        Documentation for texlive-simple-resume-cv
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-simple-resume-cv-doc
This package includes the documentation for texlive-simple-resume-cv

%post -n texlive-simple-resume-cv
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-simple-resume-cv 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-simple-resume-cv
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-simple-resume-cv-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/xelatex/simple-resume-cv/CV.pdf
%{_texmfdistdir}/doc/xelatex/simple-resume-cv/CV.tex
%{_texmfdistdir}/doc/xelatex/simple-resume-cv/LICENSE
%{_texmfdistdir}/doc/xelatex/simple-resume-cv/README.md

%files -n texlive-simple-resume-cv
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/xelatex/simple-resume-cv/simpleresumecv.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-simple-resume-cv-%{texlive_version}.%{texlive_noarch}.svn43057-%{release}-zypper
%endif

%package -n texlive-simple-thesis-dissertation
Version:        %{texlive_version}.%{texlive_noarch}.svn43058
Release:        0
Summary:        Template for a simple thesis or dissertation (Ph.D. or master's degree) or technical report, in XeLaTeX
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-simple-thesis-dissertation-doc >= %{texlive_version}
Provides:       tex(simplethesisdissertation.cls)
Requires:       tex(algpseudocode.sty)
Requires:       tex(amsbsy.sty)
Requires:       tex(amsfonts.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(amsthm.sty)
Requires:       tex(array.sty)
Requires:       tex(arydshln.sty)
Requires:       tex(babel.sty)
Requires:       tex(booktabs.sty)
Requires:       tex(cite.sty)
Requires:       tex(color.sty)
Requires:       tex(datetime2.sty)
Requires:       tex(environ.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(framed.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(lipsum.sty)
Requires:       tex(lmodern.sty)
Requires:       tex(longtable.sty)
Requires:       tex(multirow.sty)
Requires:       tex(report.cls)
Requires:       tex(rotating.sty)
Requires:       tex(setspace.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(titlesec.sty)
Requires:       tex(underscore.sty)
Requires:       tex(xltxtra.sty)
Requires:       tex(xunicode.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source244:      simple-thesis-dissertation.tar.xz
Source245:      simple-thesis-dissertation.doc.tar.xz

%description -n texlive-simple-thesis-dissertation
Template for a simple thesis or dissertation (Ph.D. or master's
degree) or technical report, in XeLaTeX. Simple template that
can be further customized or extended, with numerous examples.
Consistent style for figures, tables, mathematical theorems,
definitions, lemmas, etc.

date: 2017-01-28 04:55:17 +0000


%package -n texlive-simple-thesis-dissertation-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn43058
Release:        0
Summary:        Documentation for texlive-simple-thesis-dissertation
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-simple-thesis-dissertation-doc
This package includes the documentation for texlive-simple-thesis-dissertation

%post -n texlive-simple-thesis-dissertation
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-simple-thesis-dissertation 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-simple-thesis-dissertation
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-simple-thesis-dissertation-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/xelatex/simple-thesis-dissertation/Figures/Figure-SampleVectorGraphic.odg
%{_texmfdistdir}/doc/xelatex/simple-thesis-dissertation/Figures/Figure-SampleVectorGraphic.pdf
%{_texmfdistdir}/doc/xelatex/simple-thesis-dissertation/LICENSE
%{_texmfdistdir}/doc/xelatex/simple-thesis-dissertation/README.md
%{_texmfdistdir}/doc/xelatex/simple-thesis-dissertation/Thesis-BackMatter.tex
%{_texmfdistdir}/doc/xelatex/simple-thesis-dissertation/Thesis-Chapter-ChapAbbr.tex
%{_texmfdistdir}/doc/xelatex/simple-thesis-dissertation/Thesis-Chapter-Intro.tex
%{_texmfdistdir}/doc/xelatex/simple-thesis-dissertation/Thesis-Chapter-Summary.tex
%{_texmfdistdir}/doc/xelatex/simple-thesis-dissertation/Thesis-FrontMatter.tex
%{_texmfdistdir}/doc/xelatex/simple-thesis-dissertation/Thesis.bib
%{_texmfdistdir}/doc/xelatex/simple-thesis-dissertation/Thesis.pdf
%{_texmfdistdir}/doc/xelatex/simple-thesis-dissertation/Thesis.tex

%files -n texlive-simple-thesis-dissertation
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/xelatex/simple-thesis-dissertation/simplethesisdissertation.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-simple-thesis-dissertation-%{texlive_version}.%{texlive_noarch}.svn43058-%{release}-zypper
%endif

%package -n texlive-simplecd
Version:        %{texlive_version}.%{texlive_noarch}.1.4svn29260
Release:        0
Summary:        Simple CD, DVD covers for printing
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-simplecd-doc >= %{texlive_version}
Provides:       tex(simplecd.sty)
Requires:       tex(calc.sty)
Requires:       tex(fix-cm.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(ifthen.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source246:      simplecd.tar.xz
Source247:      simplecd.doc.tar.xz

%description -n texlive-simplecd
The package provides printable cut-outs for various CD, DVD and
other disc holders. The name of the package comes from its
implementation and ease of use; it was designed just for text
content, but since the text is placed in a \parbox in a tabular
environment cell, a rather wide range of things may be placed.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-simplecd-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.4svn29260
Release:        0
Summary:        Documentation for texlive-simplecd
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-simplecd-doc
This package includes the documentation for texlive-simplecd

%post -n texlive-simplecd
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-simplecd 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-simplecd
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-simplecd-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/simplecd/README
%{_texmfdistdir}/doc/latex/simplecd/examples.pdf
%{_texmfdistdir}/doc/latex/simplecd/examples.tex
%{_texmfdistdir}/doc/latex/simplecd/simplecd.pdf

%files -n texlive-simplecd
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/simplecd/simplecd.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-simplecd-%{texlive_version}.%{texlive_noarch}.1.4svn29260-%{release}-zypper
%endif

%package -n texlive-simplecv
Version:        %{texlive_version}.%{texlive_noarch}.1.6asvn35537
Release:        0
Summary:        A simple class for writing curricula vitae
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-simplecv-doc >= %{texlive_version}
Provides:       tex(simplecv.cls)
Requires:       tex(article.cls)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source248:      simplecv.tar.xz
Source249:      simplecv.doc.tar.xz

%description -n texlive-simplecv
A derivative of the cv class available to lyx users (renamed to
avoid the existing cv package).

date: 2016-06-24 17:18:15 +0000


%package -n texlive-simplecv-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.6asvn35537
Release:        0
Summary:        Documentation for texlive-simplecv
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-simplecv-doc
This package includes the documentation for texlive-simplecv

%post -n texlive-simplecv
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-simplecv 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-simplecv
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-simplecv-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/simplecv/README
%{_texmfdistdir}/doc/latex/simplecv/simplecv.pdf
%{_texmfdistdir}/doc/latex/simplecv/testcv.pdf
%{_texmfdistdir}/doc/latex/simplecv/testcv.tex

%files -n texlive-simplecv
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/simplecv/simplecv.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-simplecv-%{texlive_version}.%{texlive_noarch}.1.6asvn35537-%{release}-zypper
%endif

%package -n texlive-simpleinvoice
Version:        %{texlive_version}.%{texlive_noarch}.svn45673
Release:        0
Summary:        Easy typesetting of invoices
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-simpleinvoice-doc >= %{texlive_version}
Provides:       tex(simpleinvoice.sty)
Requires:       tex(advdate.sty)
Requires:       tex(babel.sty)
Requires:       tex(colortbl.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(tabularx.sty)
Requires:       tex(url.sty)
Requires:       tex(xcolor.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source250:      simpleinvoice.tar.xz
Source251:      simpleinvoice.doc.tar.xz

%description -n texlive-simpleinvoice
This package lets you easily typeset professional-looking
invoices. The user specifies the content of the invoice by
different \setPROPERTY commands, and an invoice is generated
automatically with the \makeinvoice command.

date: 2017-11-04 05:13:45 +0000


%package -n texlive-simpleinvoice-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn45673
Release:        0
Summary:        Documentation for texlive-simpleinvoice
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-simpleinvoice-doc
This package includes the documentation for texlive-simpleinvoice

%post -n texlive-simpleinvoice
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-simpleinvoice 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-simpleinvoice
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-simpleinvoice-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/simpleinvoice/LICENSE
%{_texmfdistdir}/doc/latex/simpleinvoice/README.md
%{_texmfdistdir}/doc/latex/simpleinvoice/doc/examples/english.pdf
%{_texmfdistdir}/doc/latex/simpleinvoice/doc/examples/english.tex
%{_texmfdistdir}/doc/latex/simpleinvoice/doc/examples/norwegian.pdf
%{_texmfdistdir}/doc/latex/simpleinvoice/doc/examples/norwegian.tex
%{_texmfdistdir}/doc/latex/simpleinvoice/doc/simpleinvoice.pdf
%{_texmfdistdir}/doc/latex/simpleinvoice/doc/simpleinvoice.tex

%files -n texlive-simpleinvoice
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/simpleinvoice/simpleinvoice.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-simpleinvoice-%{texlive_version}.%{texlive_noarch}.svn45673-%{release}-zypper
%endif

%package -n texlive-simplekv
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn44987
Release:        0
Summary:        A simple key/value system for TeX and LaTeX
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-simplekv-doc >= %{texlive_version}
Provides:       tex(simplekv.sty)
Provides:       tex(simplekv.tex)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source252:      simplekv.tar.xz
Source253:      simplekv.doc.tar.xz

%description -n texlive-simplekv
The package provides a simple key/value system for TeX and
LaTeX.

date: 2017-08-13 03:06:52 +0000


%package -n texlive-simplekv-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn44987
Release:        0
Summary:        Documentation for texlive-simplekv
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Provides:       locale(texlive-simplekv-doc:fr)

%description -n texlive-simplekv-doc
This package includes the documentation for texlive-simplekv

%post -n texlive-simplekv
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-simplekv 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-simplekv
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-simplekv-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/simplekv/README
%{_texmfdistdir}/doc/generic/simplekv/simplekv-fr.pdf
%{_texmfdistdir}/doc/generic/simplekv/simplekv-fr.tex

%files -n texlive-simplekv
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/simplekv/simplekv.sty
%{_texmfdistdir}/tex/generic/simplekv/simplekv.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-simplekv-%{texlive_version}.%{texlive_noarch}.0.0.1svn44987-%{release}-zypper
%endif

%package -n texlive-simpler-wick
Version:        %{texlive_version}.%{texlive_noarch}.1.0.0svn39074
Release:        0
Summary:        Simpler Wick contractions
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-simpler-wick-doc >= %{texlive_version}
Provides:       tex(simpler-wick.sty)
Requires:       tex(pgfopts.sty)
Requires:       tex(tikz.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source254:      simpler-wick.tar.xz
Source255:      simpler-wick.doc.tar.xz

%description -n texlive-simpler-wick
In every quantum field theory course, there will be a chapter
about Wick's theorem and how it can be used to convert a very
large product of many creation and annihilation operators into
something more tractable and normal ordered. The contractions
are denoted with a square bracket over the operators which are
being contracted, which used to be rather annoying to typeset
in LaTeX as the only other package available was simplewick,
which is rather unwieldy. This package provides a simpler
syntax for Wick contractions.

date: 2017-04-18 03:31:40 +0000


%package -n texlive-simpler-wick-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0.0svn39074
Release:        0
Summary:        Documentation for texlive-simpler-wick
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-simpler-wick-doc
This package includes the documentation for texlive-simpler-wick

%post -n texlive-simpler-wick
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-simpler-wick 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-simpler-wick
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-simpler-wick-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/simpler-wick/LICENSE
%{_texmfdistdir}/doc/latex/simpler-wick/README.md
%{_texmfdistdir}/doc/latex/simpler-wick/simpler-wick.pdf
%{_texmfdistdir}/doc/latex/simpler-wick/simpler-wick.tex

%files -n texlive-simpler-wick
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/simpler-wick/simpler-wick.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-simpler-wick-%{texlive_version}.%{texlive_noarch}.1.0.0svn39074-%{release}-zypper
%endif

%package -n texlive-simplewick
Version:        %{texlive_version}.%{texlive_noarch}.1.2asvn15878
Release:        0
Summary:        Simple Wick contractions
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-simplewick-doc >= %{texlive_version}
Provides:       tex(simplewick.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source256:      simplewick.tar.xz
Source257:      simplewick.doc.tar.xz

%description -n texlive-simplewick
The package provides a simple means of drawing Wick
contractions above and below expressions.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-simplewick-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.2asvn15878
Release:        0
Summary:        Documentation for texlive-simplewick
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-simplewick-doc
This package includes the documentation for texlive-simplewick

%post -n texlive-simplewick
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-simplewick 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-simplewick
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-simplewick-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/simplewick/README
%{_texmfdistdir}/doc/latex/simplewick/simplewick.pdf

%files -n texlive-simplewick
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/simplewick/simplewick.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-simplewick-%{texlive_version}.%{texlive_noarch}.1.2asvn15878-%{release}-zypper
%endif

%prep
%setup -q -c -T

%build

%install
    rm -rf %{buildroot}
    mkdir -p %{buildroot}%{_texmfdistdir}
    mkdir -p %{buildroot}%{_texmfmaindir}/tlpkg/tlpostcode
    mkdir -p %{buildroot}%{_datadir}/texlive/tlpkg
    mkdir -p %{buildroot}/var/adm/update-scripts
    ln -sf ../../share/texmf        %{buildroot}%{_datadir}/texlive/texmf-dist
    ln -sf ../../share/texmf        %{buildroot}%{_datadir}/texlive/texmf
    ln -sf ../../../share/texmf/tlpkg/tlpostcode \
                                    %{buildroot}%{_datadir}/texlive/tlpkg/tlpostcode
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-robustindex-%{texlive_version}.%{texlive_noarch}.svn49877-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:1} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:2} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-roex-%{texlive_version}.%{texlive_noarch}.svn45818-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:3} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-romanbar-%{texlive_version}.%{texlive_noarch}.1.0fsvn25005-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:4} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:5} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-romanbarpagenumber-%{texlive_version}.%{texlive_noarch}.1.0svn36236-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:6} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:7} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-romande-fonts-%{texlive_version}.%{texlive_noarch}.1.008_v7_scsvn19537-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:8} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:9} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-romande
    for font in %{buildroot}/%{_texmfdistdir}/fonts/type1/arkandis/romande/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-romande
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-romande/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-romande/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-romande/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-romande/fonts.scale
    mkdir -p %{buildroot}%{_sysconfdir}/fonts/conf.avail
    (cat > %{buildroot}%{_sysconfdir}/fonts/conf.avail/58-texlive-romande.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-romande    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-romande/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-romanneg-%{texlive_version}.%{texlive_noarch}.svn20087-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:10} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:11} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-romannum-%{texlive_version}.%{texlive_noarch}.1.0bsvn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:12} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:13} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-rosario-fonts-%{texlive_version}.%{texlive_noarch}.1.0svn40843-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:14} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:15} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-rosario
    for font in %{buildroot}/%{_texmfdistdir}/fonts/opentype/public/rosario/*.{pf[ab],[ot]tf} \
		%{buildroot}/%{_texmfdistdir}/fonts/type1/public/rosario/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-rosario
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-rosario/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-rosario/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-rosario/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-rosario/fonts.scale
    mkdir -p %{buildroot}%{_sysconfdir}/fonts/conf.avail
    (cat > %{buildroot}%{_sysconfdir}/fonts/conf.avail/58-texlive-rosario.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-rosario    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-rosario/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF

    mkdir -p %{buildroot}%{_sysconfdir}/fonts/conf.d
    (cat > %{buildroot}%{_sysconfdir}/fonts/conf.d/55-texlive-rosario.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Disable plain Type1 font to let fontconfig       -->
	<!-- prefere the OpenType and TrueType fonts          -->
	<!-- ************************************************ -->

	<fontconfig>
	  <selectfont>
	    <rejectfont>
	      <glob>%{_datadir}/fonts/texlive-rosario/*.pf*</glob>
	    </rejectfont>
	  </selectfont>
	</fontconfig>
	EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-rotfloat-%{texlive_version}.%{texlive_noarch}.1.2svn18292-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:16} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:17} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-rotpages-%{texlive_version}.%{texlive_noarch}.3.0svn18740-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:18} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:19} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-roundbox-%{texlive_version}.%{texlive_noarch}.0.0.2svn29675-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:20} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:21} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-roundrect-%{texlive_version}.%{texlive_noarch}.2.2svn39796-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:22} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:23} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-rrgtrees-%{texlive_version}.%{texlive_noarch}.1.1svn27322-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:24} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:25} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-rsc-%{texlive_version}.%{texlive_noarch}.3.1fsvn41923-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:26} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:27} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-rsfs-fonts-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:28} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:29} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-rsfs
    for font in %{buildroot}/%{_texmfdistdir}/fonts/type1/public/rsfs/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-rsfs
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-rsfs/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-rsfs/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-rsfs/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-rsfs/fonts.scale
    mkdir -p %{buildroot}%{_sysconfdir}/fonts/conf.avail
    (cat > %{buildroot}%{_sysconfdir}/fonts/conf.avail/58-texlive-rsfs.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-rsfs    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-rsfs/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-rsfso-%{texlive_version}.%{texlive_noarch}.1.02svn37965-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:30} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:31} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-rterface-%{texlive_version}.%{texlive_noarch}.svn30084-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:32} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:33} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-rtkinenc-%{texlive_version}.%{texlive_noarch}.1.0svn20003-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:34} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:35} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-rtklage-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:36} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:37} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-rubik-%{texlive_version}.%{texlive_noarch}.5.0svn46791-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:38} -C %{buildroot}%{_datadir}/texlive
    tar --use-compress-program=xz -xf %{S:39} -C %{buildroot}%{_datadir}/texlive
    # Avoid /usr/bin/env <prog>
    for scr in %{_texmfdistdir}/scripts/rubik/rubikrotation.pl
    do
	test -e %{buildroot}/$scr || continue
	ed %{buildroot}/${scr} <<-'EOF'
		1
		s@/env[[:blank:]]\+@/@
		.
		w
		q
	EOF
    done
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-ruhyphen-%{texlive_version}.%{texlive_noarch}.1.6svn21081-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:40} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-rulercompass-%{texlive_version}.%{texlive_noarch}.1svn32392-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:41} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:42} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-russ-%{texlive_version}.%{texlive_noarch}.svn25209-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:43} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:44} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-rutitlepage-%{texlive_version}.%{texlive_noarch}.2.1svn49125-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:45} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:46} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-rviewport-%{texlive_version}.%{texlive_noarch}.1.0svn23739-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:47} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:48} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-rvwrite-%{texlive_version}.%{texlive_noarch}.1.2svn19614-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:49} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:50} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-ryersonsgsthesis-%{texlive_version}.%{texlive_noarch}.1.0.3svn50119-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:51} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:52} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-ryethesis-%{texlive_version}.%{texlive_noarch}.1.36svn33945-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:53} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:54} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-sa-tikz-%{texlive_version}.%{texlive_noarch}.0.0.7asvn32815-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:55} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:56} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-sageep-%{texlive_version}.%{texlive_noarch}.1.0svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:57} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:58} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-sanitize-umlaut-%{texlive_version}.%{texlive_noarch}.1.00svn41365-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:59} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:60} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-sanskrit-%{texlive_version}.%{texlive_noarch}.2.2.1svn42925-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:61} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:62} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-sanskrit-t1-fonts-%{texlive_version}.%{texlive_noarch}.svn35737-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:63} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:64} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-sanskrit-t1
    for font in %{buildroot}/%{_texmfdistdir}/fonts/type1/public/sanskrit-t1/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-sanskrit-t1
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-sanskrit-t1/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-sanskrit-t1/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-sanskrit-t1/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-sanskrit-t1/fonts.scale
    mkdir -p %{buildroot}%{_sysconfdir}/fonts/conf.avail
    (cat > %{buildroot}%{_sysconfdir}/fonts/conf.avail/58-texlive-sanskrit-t1.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-sanskrit-t1    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-sanskrit-t1/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-sansmath-%{texlive_version}.%{texlive_noarch}.1.1svn17997-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:65} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:66} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-sansmathaccent-%{texlive_version}.%{texlive_noarch}.svn30187-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:67} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:68} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-sansmathfonts-fonts-%{texlive_version}.%{texlive_noarch}.svn50756-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:69} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:70} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-sansmathfonts
    for font in %{buildroot}/%{_texmfdistdir}/fonts/type1/public/sansmathfonts/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-sansmathfonts
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-sansmathfonts/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-sansmathfonts/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-sansmathfonts/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-sansmathfonts/fonts.scale
    mkdir -p %{buildroot}%{_sysconfdir}/fonts/conf.avail
    (cat > %{buildroot}%{_sysconfdir}/fonts/conf.avail/58-texlive-sansmathfonts.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-sansmathfonts    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-sansmathfonts/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-sapthesis-%{texlive_version}.%{texlive_noarch}.4.1svn48365-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:71} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:72} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-sasnrdisplay-%{texlive_version}.%{texlive_noarch}.0.0.95svn45963-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:73} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:74} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-sauerj-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:75} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:76} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-sauter-%{texlive_version}.%{texlive_noarch}.2.4svn13293-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:77} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-sauterfonts-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:78} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:79} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-savefnmark-%{texlive_version}.%{texlive_noarch}.1.0svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:80} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:81} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-savesym-%{texlive_version}.%{texlive_noarch}.1.2svn31565-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:82} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-savetrees-%{texlive_version}.%{texlive_noarch}.2.4svn40525-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:83} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:84} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-scale-%{texlive_version}.%{texlive_noarch}.1.1.2svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:85} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:86} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-scalebar-%{texlive_version}.%{texlive_noarch}.1.0svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:87} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:88} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-scalerel-%{texlive_version}.%{texlive_noarch}.1.8svn42809-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:89} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:90} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-scanpages-fonts-%{texlive_version}.%{texlive_noarch}.1.05asvn42633-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:91} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:92} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Avoid /usr/bin/env <prog>
    for scr in %{_texmfdistdir}/doc/latex/scanpages/replicate.py
    do
	test -e %{buildroot}/$scr || continue
	ed %{buildroot}/${scr} <<-'EOF'
		1
		s@/env[[:blank:]]\+@/@
		.
		w
		q
	EOF
    done
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-scanpages
    for font in %{buildroot}/%{_texmfdistdir}/fonts/type1/public/scanpages/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-scanpages
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-scanpages/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-scanpages/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-scanpages/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-scanpages/fonts.scale
    mkdir -p %{buildroot}%{_sysconfdir}/fonts/conf.avail
    (cat > %{buildroot}%{_sysconfdir}/fonts/conf.avail/58-texlive-scanpages.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-scanpages    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-scanpages/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-schemabloc-%{texlive_version}.%{texlive_noarch}.1.5svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:93} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:94} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-schemata-%{texlive_version}.%{texlive_noarch}.0.0.8svn39510-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:95} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:96} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-schule-%{texlive_version}.%{texlive_noarch}.0.0.8.1svn48471-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:97} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:98} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-schulschriften-%{texlive_version}.%{texlive_noarch}.4svn35730-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:99} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:100} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-schwalbe-chess-%{texlive_version}.%{texlive_noarch}.2.3svn49602-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:101} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:102} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-scientific-thesis-cover-%{texlive_version}.%{texlive_noarch}.4.0.2svn47923-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:103} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:104} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-sciposter-%{texlive_version}.%{texlive_noarch}.1.18svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:105} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:106} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-sclang-prettifier-%{texlive_version}.%{texlive_noarch}.0.0.1svn35087-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:107} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:108} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-scratch-%{texlive_version}.%{texlive_noarch}.0.0.41svn50073-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:109} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:110} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-scratch3-%{texlive_version}.%{texlive_noarch}.0.0.11svn50304-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:111} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:112} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-scratchx-%{texlive_version}.%{texlive_noarch}.1.1svn44906-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:113} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:114} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-screenplay-%{texlive_version}.%{texlive_noarch}.1.6svn27223-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:115} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:116} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-screenplay-pkg-%{texlive_version}.%{texlive_noarch}.1.1svn44965-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:117} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:118} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-scrjrnl-%{texlive_version}.%{texlive_noarch}.0.0.1svn27810-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:119} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:120} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-scrlttr2copy-%{texlive_version}.%{texlive_noarch}.0.0.1dsvn39734-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:121} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:122} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-scsnowman-%{texlive_version}.%{texlive_noarch}.1.2dsvn47953-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:123} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:124} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-sdrt-%{texlive_version}.%{texlive_noarch}.1.0svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:125} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:126} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-sduthesis-%{texlive_version}.%{texlive_noarch}.1.2.1svn41401-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:127} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:128} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-secdot-%{texlive_version}.%{texlive_noarch}.1.0svn20208-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:129} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:130} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-section-%{texlive_version}.%{texlive_noarch}.svn20180-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:131} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:132} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-sectionbox-%{texlive_version}.%{texlive_noarch}.1.01svn37749-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:133} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:134} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-sectionbreak-%{texlive_version}.%{texlive_noarch}.0.0.1dsvn50339-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:135} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:136} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-sectsty-%{texlive_version}.%{texlive_noarch}.2.0.2svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:137} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:138} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-seealso-%{texlive_version}.%{texlive_noarch}.1.2svn43595-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:139} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:140} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-seetexk-%{texlive_version}.%{texlive_noarch}.svn50602-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:141} -C %{buildroot}%{_datadir}/texlive
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-selectp-%{texlive_version}.%{texlive_noarch}.1.0svn20185-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:142} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:143} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-selnolig-%{texlive_version}.%{texlive_noarch}.0.0.302svn38721-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:144} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:145} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-semantic-%{texlive_version}.%{texlive_noarch}.2.0svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:146} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:147} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-semantic-markup-%{texlive_version}.%{texlive_noarch}.svn47837-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:148} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:149} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-semaphor-fonts-%{texlive_version}.%{texlive_noarch}.svn18651-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:150} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:151} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-semaphor
    for font in %{buildroot}/%{_texmfdistdir}/fonts/opentype/public/semaphor/*.{pf[ab],[ot]tf} \
		%{buildroot}/%{_texmfdistdir}/fonts/type1/public/semaphor/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-semaphor
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-semaphor/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-semaphor/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-semaphor/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-semaphor/fonts.scale
    mkdir -p %{buildroot}%{_sysconfdir}/fonts/conf.avail
    (cat > %{buildroot}%{_sysconfdir}/fonts/conf.avail/58-texlive-semaphor.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-semaphor    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-semaphor/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF

    mkdir -p %{buildroot}%{_sysconfdir}/fonts/conf.d
    (cat > %{buildroot}%{_sysconfdir}/fonts/conf.d/55-texlive-semaphor.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Disable plain Type1 font to let fontconfig       -->
	<!-- prefere the OpenType and TrueType fonts          -->
	<!-- ************************************************ -->

	<fontconfig>
	  <selectfont>
	    <rejectfont>
	      <glob>%{_datadir}/fonts/texlive-semaphor/*.pf*</glob>
	    </rejectfont>
	  </selectfont>
	</fontconfig>
	EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-seminar-%{texlive_version}.%{texlive_noarch}.1.62svn34011-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:152} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:153} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-semioneside-%{texlive_version}.%{texlive_noarch}.0.0.41svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:154} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:155} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-semproc-%{texlive_version}.%{texlive_noarch}.0.0.1svn37568-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:156} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:157} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-sepfootnotes-%{texlive_version}.%{texlive_noarch}.0.0.3csvn41732-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:158} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:159} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-sepnum-%{texlive_version}.%{texlive_noarch}.2.0svn20186-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:160} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:161} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-seqsplit-%{texlive_version}.%{texlive_noarch}.0.0.1svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:162} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:163} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-serbian-apostrophe-%{texlive_version}.%{texlive_noarch}.svn23799-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:164} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:165} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-serbian-date-lat-%{texlive_version}.%{texlive_noarch}.svn23446-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:166} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:167} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-serbian-def-cyr-%{texlive_version}.%{texlive_noarch}.svn23734-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:168} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:169} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-serbian-lig-%{texlive_version}.%{texlive_noarch}.svn48197-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:170} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:171} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-sesamanuel-%{texlive_version}.%{texlive_noarch}.0.0.6svn36613-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:172} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:173} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-sesstime-%{texlive_version}.%{texlive_noarch}.1.12svn49750-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:174} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:175} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-setdeck-%{texlive_version}.%{texlive_noarch}.0.0.1svn40613-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:176} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:177} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-setspace-%{texlive_version}.%{texlive_noarch}.6.7asvn24881-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:178} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:179} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-seuthesis-%{texlive_version}.%{texlive_noarch}.2.1.2svn33042-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:180} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:181} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    rm -vf  %{buildroot}%{_texmfdistdir}/doc/latex/seuthesis/a3cover/a3cover.bat
    rm -vf  %{buildroot}%{_texmfdistdir}/doc/latex/seuthesis/a3cover/a4cover.bat
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-seuthesix-%{texlive_version}.%{texlive_noarch}.1.0.1svn40088-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:182} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:183} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-sexam-%{texlive_version}.%{texlive_noarch}.1svn46628-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:184} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:185} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-sf298-%{texlive_version}.%{texlive_noarch}.1.3svn41653-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:186} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:187} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-sffms-%{texlive_version}.%{texlive_noarch}.2.0svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:188} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:189} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-sfg-%{texlive_version}.%{texlive_noarch}.0.0.91svn20209-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:190} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:191} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-sfmath-%{texlive_version}.%{texlive_noarch}.0.0.8svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:192} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-sgame-%{texlive_version}.%{texlive_noarch}.2.15svn30959-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:193} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:194} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-shade-%{texlive_version}.%{texlive_noarch}.1svn22212-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:195} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:196} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-shadethm-%{texlive_version}.%{texlive_noarch}.svn20319-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:197} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:198} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-shadow-%{texlive_version}.%{texlive_noarch}.svn20312-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:199} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:200} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-shadowtext-%{texlive_version}.%{texlive_noarch}.0.0.3svn26522-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:201} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:202} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-shapepar-%{texlive_version}.%{texlive_noarch}.2.2svn30708-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:203} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:204} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-shapes-%{texlive_version}.%{texlive_noarch}.1.1svn42428-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:205} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:206} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-shdoc-%{texlive_version}.%{texlive_noarch}.2.1bsvn41991-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:207} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:208} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-shipunov-%{texlive_version}.%{texlive_noarch}.1.1svn29349-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:209} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:210} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    rm -vf  %{buildroot}%{_texmfdistdir}/scripts/shipunov/biokey2html.bat
    # Make possible scripts usable if any
    for scr in %{_texmfdistdir}/scripts/shipunov/biokey2html1.pl \
	       %{_texmfdistdir}/scripts/shipunov/biokey2html2.pl \
	       %{_texmfdistdir}/scripts/shipunov/biokey2html3.pl
    do
	test -e %{buildroot}/$scr || continue
	chmod 0755 %{buildroot}/$scr
    done
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-shobhika-fonts-%{texlive_version}.%{texlive_noarch}.1.05svn50555-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:211} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:212} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-shobhika
    for font in %{buildroot}/%{_texmfdistdir}/fonts/opentype/public/shobhika/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-shobhika
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-shobhika/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-shobhika/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-shobhika/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-shobhika/fonts.scale
    mkdir -p %{buildroot}%{_sysconfdir}/fonts/conf.avail
    (cat > %{buildroot}%{_sysconfdir}/fonts/conf.avail/58-texlive-shobhika.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-shobhika    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-shobhika/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-short-math-guide-%{texlive_version}.%{texlive_noarch}.2.0svn46126-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:213} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-shorttoc-%{texlive_version}.%{texlive_noarch}.1.3svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:214} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:215} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-show2e-%{texlive_version}.%{texlive_noarch}.1.0svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:216} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:217} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-showcharinbox-%{texlive_version}.%{texlive_noarch}.0.0.1svn29803-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:218} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:219} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-showdim-%{texlive_version}.%{texlive_noarch}.1.2svn28918-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:220} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:221} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-showexpl-%{texlive_version}.%{texlive_noarch}.0.0.3osvn42677-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:222} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:223} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-showhyphens-%{texlive_version}.%{texlive_noarch}.0.0.5csvn39787-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:224} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:225} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-showlabels-%{texlive_version}.%{texlive_noarch}.1.8svn41322-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:226} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:227} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-showtags-%{texlive_version}.%{texlive_noarch}.1.05svn20336-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:228} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:229} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-shuffle-%{texlive_version}.%{texlive_noarch}.1.0svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:230} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:231} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-sidecap-%{texlive_version}.%{texlive_noarch}.1.6fsvn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:232} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:233} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-sidenotes-%{texlive_version}.%{texlive_noarch}.1.00svn40658-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:234} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:235} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-sides-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:236} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:237} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-signchart-%{texlive_version}.%{texlive_noarch}.1.01svn39707-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:238} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:239} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-silence-%{texlive_version}.%{texlive_noarch}.1.5bsvn27028-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:240} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:241} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-simple-resume-cv-%{texlive_version}.%{texlive_noarch}.svn43057-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:242} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:243} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-simple-thesis-dissertation-%{texlive_version}.%{texlive_noarch}.svn43058-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:244} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:245} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-simplecd-%{texlive_version}.%{texlive_noarch}.1.4svn29260-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:246} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:247} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-simplecv-%{texlive_version}.%{texlive_noarch}.1.6asvn35537-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:248} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:249} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-simpleinvoice-%{texlive_version}.%{texlive_noarch}.svn45673-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:250} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:251} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-simplekv-%{texlive_version}.%{texlive_noarch}.0.0.1svn44987-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:252} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:253} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-simpler-wick-%{texlive_version}.%{texlive_noarch}.1.0.0svn39074-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:254} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:255} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-simplewick-%{texlive_version}.%{texlive_noarch}.1.2asvn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:256} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:257} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Remove this
    rm -vrf %{buildroot}%{_texmfdistdir}/tlpkg/tlpobj
    rm -vrf %{buildroot}%{_texmfmaindir}/tlpkg/tlpobj
    rm -v  %{buildroot}%{_datadir}/texlive/texmf
    rm -v  %{buildroot}%{_datadir}/texlive/texmf-dist
    rm -vr %{buildroot}%{_datadir}/texlive
    # Handle manual pages
    rm -vf %{buildroot}%{_texmfmaindir}/doc/man/Makefile
    rm -vf %{buildroot}%{_texmfmaindir}/doc/man/man*/*.pdf
    rm -vf %{buildroot}%{_texmfdistdir}/doc/man/Makefile
    rm -vf %{buildroot}%{_texmfdistdir}/doc/man/man*/*.pdf
    for path in %{buildroot}%{_texmfmaindir}/doc/man/man? \
               %{buildroot}%{_texmfdistdir}/doc/man/man?
    do
        test -d "$path" || continue
        sec=${path##*/}
        mkdir -p %{buildroot}%{_mandir}/${sec}
        for page in ${path}/*.*
        do
            test -e "$page" || continue
            mv -f $page %{buildroot}%{_mandir}/${sec}/
        done
    done
    rm -rf %{buildroot}%{_texmfmaindir}/doc/man
    rm -rf %{buildroot}%{_texmfdistdir}/doc/man
    find %{buildroot}%{_texmfmaindir}/ %{buildroot}%{_texmfdistdir}/ \
        -type f -a -perm /g+w,o+w | xargs --no-run-if-empty chmod g-w,o-w

%changelog
