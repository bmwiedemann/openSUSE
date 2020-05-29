#
# spec file for package texlive-specs-x
#
# Copyright (c) 2020 SUSE LLC
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

%define texlive_version  2020
%define texlive_previous 2019
%define texlive_release  20200327
%define texlive_noarch   176

#!BuildIgnore:          texlive
#!BuildIgnore:          texlive-scripts
#!BuildIgnore:          texlive-scripts-extra
#!BuildIgnore:          texlive-scripts-bin
#!BuildIgnore:          texlive-scripts-extra-bin
#!BuildIgnore:          texlive-gsftopk
#!BuildIgnore:          texlive-gsftopk-bin
#!BuildIgnore:          texlive-kpathsea
#!BuildIgnore:          texlive-kpathsea-bin

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

Name:           texlive-specs-x
Version:        2020
Release:        0
BuildRequires:  ed
BuildRequires:  fontconfig
BuildRequires:  fontpackages-devel
BuildRequires:  t1utils
BuildRequires:  texlive-filesystem
BuildRequires:  xz
BuildArch:      noarch
Summary:        Meta package for x
License:        Apache-1.0 and BSD-3-Clause and GPL-2.0+ and LPPL-1.0 and SUSE-Public-Domain and SUSE-TeX
Group:          Productivity/Publishing/TeX/Base
URL:            https://build.opensuse.org/package/show/Publishing:TeXLive/Meta
Source0:        texlive-specs-x-rpmlintrc

%description
Meta package to build tons of noarch texlive packages.

%package -n texlive-tikz-dimline
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn35805
Release:        0
Summary:        Technical dimension lines using PGF/TikZ
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-tikz-dimline-doc >= %{texlive_version}
Provides:       tex(tikz-dimline.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(pgfplots.sty)
Requires:       tex(tikz.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source1:        tikz-dimline.tar.xz
Source2:        tikz-dimline.doc.tar.xz

%description -n texlive-tikz-dimline
tikz-dimline helps drawing technical dimension lines in TikZ
picture environments. Its usage is similar to some
contributions posted on stackexchange.

%package -n texlive-tikz-dimline-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn35805
Release:        0
Summary:        Documentation for texlive-tikz-dimline
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-tikz-dimline-doc
This package includes the documentation for texlive-tikz-dimline

%post -n texlive-tikz-dimline
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tikz-dimline 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tikz-dimline
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikz-dimline-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/tikz-dimline/README
%{_texmfdistdir}/doc/latex/tikz-dimline/dimline1.png
%{_texmfdistdir}/doc/latex/tikz-dimline/dimline2.png
%{_texmfdistdir}/doc/latex/tikz-dimline/dimline3.png
%{_texmfdistdir}/doc/latex/tikz-dimline/tikz-dimline-doc.pdf
%{_texmfdistdir}/doc/latex/tikz-dimline/tikz-dimline-doc.tex

%files -n texlive-tikz-dimline
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/tikz-dimline/tikz-dimline.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-tikz-dimline-%{texlive_version}.%{texlive_noarch}.1.0svn35805-%{release}-zypper
%endif

%package -n texlive-tikz-feynhand
Version:        %{texlive_version}.%{texlive_noarch}.1.1.0svn51915
Release:        0
Summary:        Feynman diagrams with TikZ
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-tikz-feynhand-doc >= %{texlive_version}
Provides:       tex(tikz-feynhand.sty)
Provides:       tex(tikzfeynhand.keys.code.tex)
Provides:       tex(tikzlibraryfeynhand.code.tex)
Requires:       tex(pgfopts.sty)
Requires:       tex(tikz.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source3:        tikz-feynhand.tar.xz
Source4:        tikz-feynhand.doc.tar.xz

%description -n texlive-tikz-feynhand
This package lets you draw Feynman diagrams using TikZ. It is a
low-end modification of the TikZ-Feynman package, one of whose
principal advantages is the automatic generation of diagrams,
for which it needs LuaTex. TikZ-FeynHand only provides the
manual mode and hence runs in LaTeX without any reference to
LuaTeX. In addition it provides some new styles for vertices
and propagators, alternative shorter keywords in addition to
TikZ-Feynman's longer ones, some shortcut commands for quickly
customizing the diagrams' look, and the new feature of putting
one propagator "on top" of another. It also includes a quick
user guide for getting started, with many examples and a
5-minute introduction to TikZ.

%package -n texlive-tikz-feynhand-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1.0svn51915
Release:        0
Summary:        Documentation for texlive-tikz-feynhand
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-tikz-feynhand-doc
This package includes the documentation for texlive-tikz-feynhand

%post -n texlive-tikz-feynhand
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tikz-feynhand 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tikz-feynhand
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikz-feynhand-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/tikz-feynhand/README.md
%{_texmfdistdir}/doc/latex/tikz-feynhand/changes.txt
%{_texmfdistdir}/doc/latex/tikz-feynhand/shell_escape.jpg
%{_texmfdistdir}/doc/latex/tikz-feynhand/tikz-feynhand.userguide.pdf
%{_texmfdistdir}/doc/latex/tikz-feynhand/tikz-feynhand.userguide.tex

%files -n texlive-tikz-feynhand
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/tikz-feynhand/tikz-feynhand.sty
%{_texmfdistdir}/tex/latex/tikz-feynhand/tikzfeynhand.keys.code.tex
%{_texmfdistdir}/tex/latex/tikz-feynhand/tikzlibraryfeynhand.code.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-tikz-feynhand-%{texlive_version}.%{texlive_noarch}.1.1.0svn51915-%{release}-zypper
%endif

%package -n texlive-tikz-feynman
Version:        %{texlive_version}.%{texlive_noarch}.1.1.0svn39582
Release:        0
Summary:        Feynman diagrams with TikZ
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-tikz-feynman-doc >= %{texlive_version}
Provides:       tex(tikz-feynman.sty)
Provides:       tex(tikzfeynman.keys.code.tex)
Provides:       tex(tikzlibraryfeynman.code.tex)
Requires:       tex(ifluatex.sty)
Requires:       tex(pgfopts.sty)
Requires:       tex(tikz.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source5:        tikz-feynman.tar.xz
Source6:        tikz-feynman.doc.tar.xz

%description -n texlive-tikz-feynman
This is a LaTeX package allowing Feynman diagrams to be easily
generated within LaTeX with minimal user instructions and
without the need of external programs. It builds upon the TikZ
package and leverages the graph placement algorithms from TikZ
in order to automate the placement of many vertices.
tikz-feynman allows fine-tuned placement of vertices so that
even complex diagrams can still be generated with ease.

%package -n texlive-tikz-feynman-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1.0svn39582
Release:        0
Summary:        Documentation for texlive-tikz-feynman
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-tikz-feynman-doc
This package includes the documentation for texlive-tikz-feynman

%post -n texlive-tikz-feynman
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tikz-feynman 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tikz-feynman
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikz-feynman-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/tikz-feynman/LICENSE
%{_texmfdistdir}/doc/latex/tikz-feynman/README.md
%{_texmfdistdir}/doc/latex/tikz-feynman/references.bib
%{_texmfdistdir}/doc/latex/tikz-feynman/tikz-feynman.pdf
%{_texmfdistdir}/doc/latex/tikz-feynman/tikz-feynman.tex

%files -n texlive-tikz-feynman
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/tikz-feynman/tikz-feynman.sty
%{_texmfdistdir}/tex/latex/tikz-feynman/tikzfeynman.keys.code.tex
%{_texmfdistdir}/tex/latex/tikz-feynman/tikzfeynman.patch.3.0.0.lua
%{_texmfdistdir}/tex/latex/tikz-feynman/tikzfeynman.patch.3.0.1.lua
%{_texmfdistdir}/tex/latex/tikz-feynman/tikzlibraryfeynman.code.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-tikz-feynman-%{texlive_version}.%{texlive_noarch}.1.1.0svn39582-%{release}-zypper
%endif

%package -n texlive-tikz-imagelabels
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2svn51490
Release:        0
Summary:        Put labels on images using TikZ
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-tikz-imagelabels-doc >= %{texlive_version}
Provides:       tex(tikz-imagelabels.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xifthen.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source7:        tikz-imagelabels.tar.xz
Source8:        tikz-imagelabels.doc.tar.xz

%description -n texlive-tikz-imagelabels
This package allows to add label texts to an existing image
with the aid of TikZ. This may be used to label certain
features in an image.

%package -n texlive-tikz-imagelabels-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2svn51490
Release:        0
Summary:        Documentation for texlive-tikz-imagelabels
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-tikz-imagelabels-doc
This package includes the documentation for texlive-tikz-imagelabels

%post -n texlive-tikz-imagelabels
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tikz-imagelabels 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tikz-imagelabels
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikz-imagelabels-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/tikz-imagelabels/README.md
%{_texmfdistdir}/doc/latex/tikz-imagelabels/pleiades.jpg
%{_texmfdistdir}/doc/latex/tikz-imagelabels/tikz-imagelabels.pdf

%files -n texlive-tikz-imagelabels
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/tikz-imagelabels/tikz-imagelabels.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-tikz-imagelabels-%{texlive_version}.%{texlive_noarch}.0.0.2svn51490-%{release}-zypper
%endif

%package -n texlive-tikz-inet
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn15878
Release:        0
Summary:        Draw interaction nets with TikZ
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-tikz-inet-doc >= %{texlive_version}
Provides:       tex(tikz-inet.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(tikz.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source9:        tikz-inet.tar.xz
Source10:       tikz-inet.doc.tar.xz

%description -n texlive-tikz-inet
The package extends TikZ with macros to draw interaction nets.

%package -n texlive-tikz-inet-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn15878
Release:        0
Summary:        Documentation for texlive-tikz-inet
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-tikz-inet-doc
This package includes the documentation for texlive-tikz-inet

%post -n texlive-tikz-inet
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tikz-inet 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tikz-inet
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikz-inet-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/tikz-inet/README
%{_texmfdistdir}/doc/latex/tikz-inet/tikz-inet-doc.pdf
%{_texmfdistdir}/doc/latex/tikz-inet/tikz-inet-doc.tex

%files -n texlive-tikz-inet
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/tikz-inet/tikz-inet.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-tikz-inet-%{texlive_version}.%{texlive_noarch}.0.0.1svn15878-%{release}-zypper
%endif

%package -n texlive-tikz-kalender
Version:        %{texlive_version}.%{texlive_noarch}.0.0.4fsvn52890
Release:        0
Summary:        A LaTeX based calendar using TikZ
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-tikz-kalender-doc >= %{texlive_version}
Provides:       tex(tikz-kalender-translation.clo)
Provides:       tex(tikz-kalender.cls)
Requires:       tex(article.cls)
Requires:       tex(babel.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(geometry.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(inputenc.sty)
Requires:       tex(lmodern.sty)
Requires:       tex(pgfkeys.sty)
Requires:       tex(ragged2e.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(tgheros.sty)
Requires:       tex(tikz.sty)
Requires:       tex(translator.sty)
Requires:       tex(unicode-math.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source11:       tikz-kalender.tar.xz
Source12:       tikz-kalender.doc.tar.xz

%description -n texlive-tikz-kalender
For usage see the example files tikz-kalender-example1.tex,
tikz-kalender-example2.tex, and *.events. The Code is inspired
by this document and is subject to the >>Creative Commons
attribution license (CC-BY-SA)<<. The class tikz-kalender
requires the package TikZ and the TikZ libraries calc and
calendar.

%package -n texlive-tikz-kalender-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.4fsvn52890
Release:        0
Summary:        Documentation for texlive-tikz-kalender
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-tikz-kalender-doc
This package includes the documentation for texlive-tikz-kalender

%post -n texlive-tikz-kalender
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tikz-kalender 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tikz-kalender
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikz-kalender-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/tikz-kalender/Feiertage-2016.events
%{_texmfdistdir}/doc/latex/tikz-kalender/Geburtstage.events
%{_texmfdistdir}/doc/latex/tikz-kalender/README.md
%{_texmfdistdir}/doc/latex/tikz-kalender/Schulferien-2016.events
%{_texmfdistdir}/doc/latex/tikz-kalender/Sonstiges.events
%{_texmfdistdir}/doc/latex/tikz-kalender/Urlaub.events
%{_texmfdistdir}/doc/latex/tikz-kalender/tikz-kalender-example1.pdf
%{_texmfdistdir}/doc/latex/tikz-kalender/tikz-kalender-example1.tex
%{_texmfdistdir}/doc/latex/tikz-kalender/tikz-kalender-example2.pdf
%{_texmfdistdir}/doc/latex/tikz-kalender/tikz-kalender-example2.tex

%files -n texlive-tikz-kalender
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/tikz-kalender/tikz-kalender-translation.clo
%{_texmfdistdir}/tex/latex/tikz-kalender/tikz-kalender.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-tikz-kalender-%{texlive_version}.%{texlive_noarch}.0.0.4fsvn52890-%{release}-zypper
%endif

%package -n texlive-tikz-karnaugh
Version:        %{texlive_version}.%{texlive_noarch}.1.2svn47026
Release:        0
Summary:        Typeset Karnaugh maps using TikZ
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-tikz-karnaugh-doc >= %{texlive_version}
Provides:       tex(tikzlibrarykarnaugh.code.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source13:       tikz-karnaugh.tar.xz
Source14:       tikz-karnaugh.doc.tar.xz

%description -n texlive-tikz-karnaugh
The tikz-karnaugh package is a LaTeX package used to draw
Karnaugh maps. It uses TikZ to produce high quality graph up to
12 variables, but this limit depends on the TeX memory usage
and can be different for you. It is very good for presentation
since TikZ allows for a better control over the final
appearance of the map. You can control colour, styles and
distances. It can be considered as an upgrade of Andreas W.
Wieland's karnaugh package towards TikZ supporting. Also,
complex maps with solution (prime implicants) pointed out can
be generated with external java software. It supports both
America and traditional styles, though American style requires
a little extra effort.

%package -n texlive-tikz-karnaugh-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.2svn47026
Release:        0
Summary:        Documentation for texlive-tikz-karnaugh
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-tikz-karnaugh-doc
This package includes the documentation for texlive-tikz-karnaugh

%post -n texlive-tikz-karnaugh
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tikz-karnaugh 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tikz-karnaugh
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikz-karnaugh-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/tikz-karnaugh/README.txt
%{_texmfdistdir}/doc/latex/tikz-karnaugh/tikz-karnaugh-doc.pdf
%{_texmfdistdir}/doc/latex/tikz-karnaugh/tikz-karnaugh-doc.tex

%files -n texlive-tikz-karnaugh
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/tikz-karnaugh/tikzlibrarykarnaugh.code.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-tikz-karnaugh-%{texlive_version}.%{texlive_noarch}.1.2svn47026-%{release}-zypper
%endif

%package -n texlive-tikz-ladder
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn46555
Release:        0
Summary:        Draw ladder diagrams using TikZ
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-tikz-ladder-doc >= %{texlive_version}
Provides:       tex(tikzlibrarycircuits.plc.ladder.code.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source15:       tikz-ladder.tar.xz
Source16:       tikz-ladder.doc.tar.xz

%description -n texlive-tikz-ladder
The tikz-ladder package contains a collection of symbols for
typesetting ladder diagrams (PLC program) in agreement with the
international standard IEC-61131-3/2013. It includes blocks
(for representing functions and function blocks) besides
contacts and coils. It extends the circuit library of TikZ and
allows you to draw a ladder diagram in the same way as you
would draw any other circuit.

%package -n texlive-tikz-ladder-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn46555
Release:        0
Summary:        Documentation for texlive-tikz-ladder
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-tikz-ladder-doc
This package includes the documentation for texlive-tikz-ladder

%post -n texlive-tikz-ladder
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tikz-ladder 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tikz-ladder
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikz-ladder-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/tikz-ladder/README.txt
%{_texmfdistdir}/doc/latex/tikz-ladder/tikz-ladder-doc.pdf
%{_texmfdistdir}/doc/latex/tikz-ladder/tikz-ladder-doc.tex

%files -n texlive-tikz-ladder
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/tikz-ladder/tikzlibrarycircuits.plc.ladder.code.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-tikz-ladder-%{texlive_version}.%{texlive_noarch}.1.1svn46555-%{release}-zypper
%endif

%package -n texlive-tikz-layers
Version:        %{texlive_version}.%{texlive_noarch}.0.0.9svn46660
Release:        0
Summary:        TikZ provides graphical layers on TikZ: "behind", "above" and "glass"
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-tikz-layers-doc >= %{texlive_version}
Provides:       tex(tikz-layers.sty)
Requires:       tex(tikz.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source17:       tikz-layers.tar.xz
Source18:       tikz-layers.doc.tar.xz

%description -n texlive-tikz-layers
TikZ-layers is a tiny package that provides, along side
"background", typical graphical layers on TikZ: "behind",
"above" and "glass". The layers may be selected with one of the
styles "on behind layer", "on above layer", "on glass layer" as
an option to a {scope} environment.

%package -n texlive-tikz-layers-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.9svn46660
Release:        0
Summary:        Documentation for texlive-tikz-layers
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-tikz-layers-doc
This package includes the documentation for texlive-tikz-layers

%post -n texlive-tikz-layers
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tikz-layers 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tikz-layers
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikz-layers-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/tikz-layers/README
%{_texmfdistdir}/doc/latex/tikz-layers/README.TEXLIVE
%{_texmfdistdir}/doc/latex/tikz-layers/manifest.txt

%files -n texlive-tikz-layers
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/tikz-layers/tikz-layers.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-tikz-layers-%{texlive_version}.%{texlive_noarch}.0.0.9svn46660-%{release}-zypper
%endif

%package -n texlive-tikz-nef
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn48240
Release:        0
Summary:        Create diagrams for neural networks constructed with the methods of the Neural Engineering Framework (NEF)
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-tikz-nef-doc >= %{texlive_version}
Provides:       tex(tikzlibrarynef.code.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source19:       tikz-nef.tar.xz
Source20:       tikz-nef.doc.tar.xz

%description -n texlive-tikz-nef
The nef TikZ library provides predefined styles and shapes to
create diagrams for neural networks constructed with the
methods of the Neural Engineering Framework (NEF). The
following styles are supported: ea: ensemble array ens:
ensemble ext: external input or output inhibt: inhibitory
connection net: network pnode: pass-through node rect:
rectification ensemble recurrent: recurrent connection

%package -n texlive-tikz-nef-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn48240
Release:        0
Summary:        Documentation for texlive-tikz-nef
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-tikz-nef-doc
This package includes the documentation for texlive-tikz-nef

%post -n texlive-tikz-nef
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tikz-nef 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tikz-nef
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikz-nef-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/tikz-nef/LICENSE
%{_texmfdistdir}/doc/latex/tikz-nef/README.md
%{_texmfdistdir}/doc/latex/tikz-nef/example-net.tex
%{_texmfdistdir}/doc/latex/tikz-nef/nef.bib
%{_texmfdistdir}/doc/latex/tikz-nef/tikz-nef-doc.pdf
%{_texmfdistdir}/doc/latex/tikz-nef/tikz-nef-doc.tex

%files -n texlive-tikz-nef
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/tikz-nef/tikzlibrarynef.code.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-tikz-nef-%{texlive_version}.%{texlive_noarch}.0.0.1svn48240-%{release}-zypper
%endif

%package -n texlive-tikz-network
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn51884
Release:        0
Summary:        Draw networks with TikZ
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-tikz-network-doc >= %{texlive_version}
Provides:       tex(tikz-network.sty)
Requires:       tex(datatool.sty)
Requires:       tex(etex.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(tikz.sty)
Requires:       tex(trimspaces.sty)
Requires:       tex(xifthen.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source21:       tikz-network.tar.xz
Source22:       tikz-network.doc.tar.xz

%description -n texlive-tikz-network
This package allows the creation of images of complex networks
that are seamlessly integrated into the underlying LaTeX files.
The package requires datatool, etex, graphicx, tikz,
trimspaces, xifthen, and xkeyval.

%package -n texlive-tikz-network-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn51884
Release:        0
Summary:        Documentation for texlive-tikz-network
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-tikz-network-doc
This package includes the documentation for texlive-tikz-network

%post -n texlive-tikz-network
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tikz-network 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tikz-network
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikz-network-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/tikz-network/README.md
%{_texmfdistdir}/doc/latex/tikz-network/data/edges.csv
%{_texmfdistdir}/doc/latex/tikz-network/data/front.pdf
%{_texmfdistdir}/doc/latex/tikz-network/data/ml_edges.csv
%{_texmfdistdir}/doc/latex/tikz-network/data/ml_edges_simple.csv
%{_texmfdistdir}/doc/latex/tikz-network/data/ml_vertices.csv
%{_texmfdistdir}/doc/latex/tikz-network/data/ml_vertices_simple.csv
%{_texmfdistdir}/doc/latex/tikz-network/data/plane.png
%{_texmfdistdir}/doc/latex/tikz-network/data/vertices.csv
%{_texmfdistdir}/doc/latex/tikz-network/data/vertices_RGB.csv
%{_texmfdistdir}/doc/latex/tikz-network/tikz-network.pdf
%{_texmfdistdir}/doc/latex/tikz-network/tikz-network.tex

%files -n texlive-tikz-network
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/tikz-network/tikz-network.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-tikz-network-%{texlive_version}.%{texlive_noarch}.1.1svn51884-%{release}-zypper
%endif

%package -n texlive-tikz-opm
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1.1svn32769
Release:        0
Summary:        Typeset OPM diagrams
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-tikz-opm-doc >= %{texlive_version}
Provides:       tex(tikz-opm.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(makeshape.sty)
Requires:       tex(tikz.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source23:       tikz-opm.tar.xz
Source24:       tikz-opm.doc.tar.xz

%description -n texlive-tikz-opm
Typeset OPM (Object-Process Methodology) diagrams using LaTeX
and PGF/TikZ.

%package -n texlive-tikz-opm-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1.1svn32769
Release:        0
Summary:        Documentation for texlive-tikz-opm
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-tikz-opm-doc
This package includes the documentation for texlive-tikz-opm

%post -n texlive-tikz-opm
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tikz-opm 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tikz-opm
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikz-opm-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/tikz-opm/README
%{_texmfdistdir}/doc/latex/tikz-opm/tikz-opm.pdf

%files -n texlive-tikz-opm
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/tikz-opm/tikz-opm.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-tikz-opm-%{texlive_version}.%{texlive_noarch}.0.0.1.1svn32769-%{release}-zypper
%endif

%package -n texlive-tikz-optics
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2.3svn43466
Release:        0
Summary:        A library for drawing optical setups with TikZ
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-tikz-optics-doc >= %{texlive_version}
Provides:       tex(tikzlibraryoptics.code.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source25:       tikz-optics.tar.xz
Source26:       tikz-optics.doc.tar.xz

%description -n texlive-tikz-optics
This package provides a new TikZ library designed to easily
draw optical setups with TikZ. It provides shapes for lens,
mirror, etc. The geometrically (in)correct computation of light
rays through the setup is left to the user.

%package -n texlive-tikz-optics-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2.3svn43466
Release:        0
Summary:        Documentation for texlive-tikz-optics
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-tikz-optics-doc:fr)

%description -n texlive-tikz-optics-doc
This package includes the documentation for texlive-tikz-optics

%post -n texlive-tikz-optics
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tikz-optics 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tikz-optics
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikz-optics-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/tikz-optics/README
%{_texmfdistdir}/doc/latex/tikz-optics/tikz-optics.pdf
%{_texmfdistdir}/doc/latex/tikz-optics/tikz-optics.tex

%files -n texlive-tikz-optics
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/tikz-optics/tikzlibraryoptics.code.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-tikz-optics-%{texlive_version}.%{texlive_noarch}.0.0.2.3svn43466-%{release}-zypper
%endif

%package -n texlive-tikz-page
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn42039
Release:        0
Summary:        Small macro to help building nice and complex layout materials
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-tikz-page-doc >= %{texlive_version}
Provides:       tex(tikz-page.sty)
Requires:       tex(calc.sty)
Requires:       tex(fancyhdr.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(textpos.sty)
Requires:       tex(tikz.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source27:       tikz-page.tar.xz
Source28:       tikz-page.doc.tar.xz

%description -n texlive-tikz-page
The package provides a small macro to help building nice and
complex layout materials.

%package -n texlive-tikz-page-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn42039
Release:        0
Summary:        Documentation for texlive-tikz-page
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-tikz-page-doc
This package includes the documentation for texlive-tikz-page

%post -n texlive-tikz-page
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tikz-page 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tikz-page
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikz-page-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/tikz-page/Makefile
%{_texmfdistdir}/doc/latex/tikz-page/README
%{_texmfdistdir}/doc/latex/tikz-page/README.md
%{_texmfdistdir}/doc/latex/tikz-page/example.png
%{_texmfdistdir}/doc/latex/tikz-page/tikz-page.pdf

%files -n texlive-tikz-page
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/tikz-page/tikz-page.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-tikz-page-%{texlive_version}.%{texlive_noarch}.1.0svn42039-%{release}-zypper
%endif

%package -n texlive-tikz-palattice
Version:        %{texlive_version}.%{texlive_noarch}.2.3svn43442
Release:        0
Summary:        Draw particle accelerator lattices with TikZ
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-tikz-palattice-doc >= %{texlive_version}
Provides:       tex(tikz-palattice.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(iflang.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(siunitx.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xargs.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source29:       tikz-palattice.tar.xz
Source30:       tikz-palattice.doc.tar.xz

%description -n texlive-tikz-palattice
This package allows for drawing a map of a particle accelerator
just by giving a list of elements -- similar to lattice files
for simulation software. The package includes 12 common element
types like dipoles, quadrupoles, cavities, or screens, as well
as automatic labels with element names, a legend, a rule, and
an environment to fade out parts of the accelerator. The
coordinate of any element can be saved and used for custom TikZ
drawings or annotations. Thereby, lattices can be connected to
draw injection/extraction or even a complete accelerator
facility.

%package -n texlive-tikz-palattice-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.3svn43442
Release:        0
Summary:        Documentation for texlive-tikz-palattice
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-tikz-palattice-doc
This package includes the documentation for texlive-tikz-palattice

%post -n texlive-tikz-palattice
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tikz-palattice 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tikz-palattice
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikz-palattice-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/tikz-palattice/Makefile
%{_texmfdistdir}/doc/latex/tikz-palattice/README
%{_texmfdistdir}/doc/latex/tikz-palattice/elsa.tex
%{_texmfdistdir}/doc/latex/tikz-palattice/example1_linear.tex
%{_texmfdistdir}/doc/latex/tikz-palattice/example2_circular.tex
%{_texmfdistdir}/doc/latex/tikz-palattice/example3_coordinates.tex
%{_texmfdistdir}/doc/latex/tikz-palattice/example4_labels.tex
%{_texmfdistdir}/doc/latex/tikz-palattice/example5_legend.tex
%{_texmfdistdir}/doc/latex/tikz-palattice/tikz-palattice_documentation.pdf
%{_texmfdistdir}/doc/latex/tikz-palattice/tikz-palattice_documentation.tex

%files -n texlive-tikz-palattice
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/tikz-palattice/tikz-palattice.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-tikz-palattice-%{texlive_version}.%{texlive_noarch}.2.3svn43442-%{release}-zypper
%endif

%package -n texlive-tikz-planets
Version:        %{texlive_version}.%{texlive_noarch}.1.0.1svn54708
Release:        0
Summary:        Illustrate celestial mechanics and the solar system
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-tikz-planets-doc >= %{texlive_version}
Provides:       tex(planets.sty)
Requires:       tex(pgfkeys.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xstring.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source31:       tikz-planets.tar.xz
Source32:       tikz-planets.doc.tar.xz

%description -n texlive-tikz-planets
This TikZ-package makes it easy to illustrate celestial
mechanics and the solar system. You can use it to draw sketches
of the eclipses, the phases of the Moon, etc. The package
requires the standard packages TikZ, xcolor, xstring, and
pgfkeys.

%package -n texlive-tikz-planets-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0.1svn54708
Release:        0
Summary:        Documentation for texlive-tikz-planets
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-tikz-planets-doc
This package includes the documentation for texlive-tikz-planets

%post -n texlive-tikz-planets
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tikz-planets 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tikz-planets
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikz-planets-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/tikz-planets/README.md
%{_texmfdistdir}/doc/latex/tikz-planets/planets-doc.pdf
%{_texmfdistdir}/doc/latex/tikz-planets/planets-doc.tex

%files -n texlive-tikz-planets
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/tikz-planets/planets.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-tikz-planets-%{texlive_version}.%{texlive_noarch}.1.0.1svn54708-%{release}-zypper
%endif

%package -n texlive-tikz-qtree
Version:        %{texlive_version}.%{texlive_noarch}.1.2svn26108
Release:        0
Summary:        Use existing qtree syntax for trees in TikZ
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-tikz-qtree-doc >= %{texlive_version}
Provides:       tex(pgfsubpic.sty)
Provides:       tex(pgfsubpic.tex)
Provides:       tex(pgftree.sty)
Provides:       tex(pgftree.tex)
Provides:       tex(tikz-qtree-compat.sty)
Provides:       tex(tikz-qtree.sty)
Provides:       tex(tikz-qtree.tex)
Requires:       tex(pgf.sty)
Requires:       tex(pgffor.sty)
Requires:       tex(tikz.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source33:       tikz-qtree.tar.xz
Source34:       tikz-qtree.doc.tar.xz

%description -n texlive-tikz-qtree
The package provides a macro for drawing trees with TikZ using
the easy syntax of Alexis Dimitriadis' Qtree. It improves on
TikZ's standard tree-drawing facility by laying out tree nodes
without collisions; it improves on Qtree by adding lots of
features from TikZ (for example, edge labels, arrows between
nodes); and it improves on pst-qtree in being usable with
pdfTeX and XeTeX.

%package -n texlive-tikz-qtree-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.2svn26108
Release:        0
Summary:        Documentation for texlive-tikz-qtree
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-tikz-qtree-doc
This package includes the documentation for texlive-tikz-qtree

%post -n texlive-tikz-qtree
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tikz-qtree 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tikz-qtree
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikz-qtree-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/tikz-qtree/README
%{_texmfdistdir}/doc/latex/tikz-qtree/tikz-qtree-manual.pdf
%{_texmfdistdir}/doc/latex/tikz-qtree/tikz-qtree-manual.tex

%files -n texlive-tikz-qtree
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/tikz-qtree/pgfsubpic.sty
%{_texmfdistdir}/tex/latex/tikz-qtree/pgfsubpic.tex
%{_texmfdistdir}/tex/latex/tikz-qtree/pgftree.sty
%{_texmfdistdir}/tex/latex/tikz-qtree/pgftree.tex
%{_texmfdistdir}/tex/latex/tikz-qtree/tikz-qtree-compat.sty
%{_texmfdistdir}/tex/latex/tikz-qtree/tikz-qtree.sty
%{_texmfdistdir}/tex/latex/tikz-qtree/tikz-qtree.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-tikz-qtree-%{texlive_version}.%{texlive_noarch}.1.2svn26108-%{release}-zypper
%endif

%package -n texlive-tikz-relay
Version:        %{texlive_version}.%{texlive_noarch}.1.2svn51355
Release:        0
Summary:        TikZ library for typesetting electrical diagrams
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-tikz-relay-doc >= %{texlive_version}
Provides:       tex(tikzlibrarycircuits.ee.IEC.relay.code.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source35:       tikz-relay.tar.xz
Source36:       tikz-relay.doc.tar.xz

%description -n texlive-tikz-relay
This package contains a collection of symbols for typesetting
electrical wiring diagrams for relay control systems. The
symbols are meant to be in agreement with the international
standard IEC-60617 which has been adopted worldwide, with
perhaps the exception of the USA. It extends and modifies, when
needed, the TikZ-libray circuits.ee.IEC. A few non-standard
symbols are also included mainly to be used in presentations,
particularly with the beamer package.

%package -n texlive-tikz-relay-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.2svn51355
Release:        0
Summary:        Documentation for texlive-tikz-relay
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-tikz-relay-doc
This package includes the documentation for texlive-tikz-relay

%post -n texlive-tikz-relay
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tikz-relay 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tikz-relay
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikz-relay-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/tikz-relay/BeamerAnimation.pdf
%{_texmfdistdir}/doc/latex/tikz-relay/BeamerAnimation.tex
%{_texmfdistdir}/doc/latex/tikz-relay/README.txt
%{_texmfdistdir}/doc/latex/tikz-relay/tikz-relay-doc.pdf
%{_texmfdistdir}/doc/latex/tikz-relay/tikz-relay-doc.tex

%files -n texlive-tikz-relay
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/tikz-relay/tikzlibrarycircuits.ee.IEC.relay.code.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-tikz-relay-%{texlive_version}.%{texlive_noarch}.1.2svn51355-%{release}-zypper
%endif

%package -n texlive-tikz-sfc
Version:        %{texlive_version}.%{texlive_noarch}.1.0.1svn49424
Release:        0
Summary:        Symbols collection for typesetting Sequential Function Chart (SFC) diagrams (PLC programs)
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-tikz-sfc-doc >= %{texlive_version}
Provides:       tex(tikzlibrarycircuits.plc.sfc.code.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source37:       tikz-sfc.tar.xz
Source38:       tikz-sfc.doc.tar.xz

%description -n texlive-tikz-sfc
This package contains a collection of symbols for typesetting
Sequential Function Chart (SFC) diagrams in agreement with the
international standard IEC-61131-3/2013. It includes steps
(normal and initial), transitions, actions and actions
qualifiers (with and without time duration). It extends the
circuit library of TikZ and allows you to draw an SFC diagram
in same way you would draw any other circuit.

%package -n texlive-tikz-sfc-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0.1svn49424
Release:        0
Summary:        Documentation for texlive-tikz-sfc
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-tikz-sfc-doc
This package includes the documentation for texlive-tikz-sfc

%post -n texlive-tikz-sfc
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tikz-sfc 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tikz-sfc
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikz-sfc-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/tikz-sfc/BeamerAnimation.pdf
%{_texmfdistdir}/doc/latex/tikz-sfc/BeamerAnimation.tex
%{_texmfdistdir}/doc/latex/tikz-sfc/README.txt
%{_texmfdistdir}/doc/latex/tikz-sfc/tikz-sfc-doc.pdf
%{_texmfdistdir}/doc/latex/tikz-sfc/tikz-sfc-doc.tex

%files -n texlive-tikz-sfc
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/tikz-sfc/tikzlibrarycircuits.plc.sfc.code.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-tikz-sfc-%{texlive_version}.%{texlive_noarch}.1.0.1svn49424-%{release}-zypper
%endif

%package -n texlive-tikz-timing
Version:        %{texlive_version}.%{texlive_noarch}.0.0.7fsvn46111
Release:        0
Summary:        Easy generation of timing diagrams as TikZ pictures
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-svn-prov >= %{texlive_version}
#!BuildIgnore: texlive-svn-prov
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-tikz-timing-doc >= %{texlive_version}
Provides:       tex(tikz-timing-advnodes.sty)
Provides:       tex(tikz-timing-arrows.sty)
Provides:       tex(tikz-timing-beamer.sty)
Provides:       tex(tikz-timing-clockarrows.sty)
Provides:       tex(tikz-timing-columntype.sty)
Provides:       tex(tikz-timing-counters.sty)
Provides:       tex(tikz-timing-either.sty)
Provides:       tex(tikz-timing-ifsym.sty)
Provides:       tex(tikz-timing-interval.sty)
Provides:       tex(tikz-timing-nicetabs.sty)
Provides:       tex(tikz-timing-overlays.sty)
Provides:       tex(tikz-timing.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(array.sty)
Requires:       tex(booktabs.sty)
Requires:       tex(environ.sty)
Requires:       tex(pgfopts.sty)
Requires:       tex(tikz.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source39:       tikz-timing.tar.xz
Source40:       tikz-timing.doc.tar.xz

%description -n texlive-tikz-timing
This package provides macros and an environment to generate
timing diagrams (digital waveforms) without much effort. The
TikZ package is used to produce the graphics. The diagrams may
be inserted into text (paragraphs, \hbox, etc.) and into
tikzpictures. A tabular-like environment is provided to produce
larger timing diagrams.

%package -n texlive-tikz-timing-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.7fsvn46111
Release:        0
Summary:        Documentation for texlive-tikz-timing
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-tikz-timing-doc
This package includes the documentation for texlive-tikz-timing

%post -n texlive-tikz-timing
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tikz-timing 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tikz-timing
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikz-timing-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/tikz-timing/README
%{_texmfdistdir}/doc/latex/tikz-timing/tikz-timing.pdf

%files -n texlive-tikz-timing
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/tikz-timing/tikz-timing-advnodes.sty
%{_texmfdistdir}/tex/latex/tikz-timing/tikz-timing-arrows.sty
%{_texmfdistdir}/tex/latex/tikz-timing/tikz-timing-beamer.sty
%{_texmfdistdir}/tex/latex/tikz-timing/tikz-timing-clockarrows.sty
%{_texmfdistdir}/tex/latex/tikz-timing/tikz-timing-columntype.sty
%{_texmfdistdir}/tex/latex/tikz-timing/tikz-timing-counters.sty
%{_texmfdistdir}/tex/latex/tikz-timing/tikz-timing-either.sty
%{_texmfdistdir}/tex/latex/tikz-timing/tikz-timing-ifsym.sty
%{_texmfdistdir}/tex/latex/tikz-timing/tikz-timing-interval.sty
%{_texmfdistdir}/tex/latex/tikz-timing/tikz-timing-nicetabs.sty
%{_texmfdistdir}/tex/latex/tikz-timing/tikz-timing-overlays.sty
%{_texmfdistdir}/tex/latex/tikz-timing/tikz-timing.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-tikz-timing-%{texlive_version}.%{texlive_noarch}.0.0.7fsvn46111-%{release}-zypper
%endif

%package -n texlive-tikz-trackschematic
Version:        %{texlive_version}.%{texlive_noarch}.0.0.5.1svn53754
Release:        0
Summary:        A TikZ library for creating track diagrams in railways
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-tikz-trackschematic-doc >= %{texlive_version}
Provides:       tex(tikzlibrarytrackschematic.code.tex)
Provides:       tex(tikzlibrarytrackschematic.constructions.code.tex)
Provides:       tex(tikzlibrarytrackschematic.messures.code.tex)
Provides:       tex(tikzlibrarytrackschematic.topology.code.tex)
Provides:       tex(tikzlibrarytrackschematic.trafficcontrol.code.tex)
Provides:       tex(tikzlibrarytrackschematic.vehicles.code.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source41:       tikz-trackschematic.tar.xz
Source42:       tikz-trackschematic.doc.tar.xz

%description -n texlive-tikz-trackschematic
This TikZ library is a toolbox of symbols geared primarily
towards creating track schematic for either research or
educational purposes. It provides a TikZ frontend to some of
the symbols which may be needed to describe situations and
layouts in railway operation. The library is divided into four
sublibraries: topology, trafficcontrol, vehicles,
constructions, and messures. This project has received funding
from the European Union's Horizon 2020 research and innovation
programme under grant agreement No. 826347.

%package -n texlive-tikz-trackschematic-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.5.1svn53754
Release:        0
Summary:        Documentation for texlive-tikz-trackschematic
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-tikz-trackschematic-doc
This package includes the documentation for texlive-tikz-trackschematic

%post -n texlive-tikz-trackschematic
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tikz-trackschematic 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tikz-trackschematic
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikz-trackschematic-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/tikz-trackschematic/README.md
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-documentation.sty
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-examples/station_berg.pdf
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-examples/station_berg.tex
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-examples/station_chamstadt.pdf
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-examples/station_chamstadt.tex
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets.pdf
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets.tex
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/bend_train.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/block_clearing_point_backward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/block_clearing_point_forward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/block_signal_backward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/block_signal_forward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/braking_point_backward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/braking_point_forward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/bridge.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/bridge_track_beneath.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/bufferstop_backward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/bufferstop_forward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/clearing_point.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/combined_signal_forward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/danger_point_backward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/danger_point_forward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/derailer_left_backward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/derailer_left_forward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/derailer_right_backward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/derailer_right_forward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/diamond_crossing_left.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/diamond_crossing_right.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/distant_signal_backward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/distant_signal_forward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/distant_speed_signal_backward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/distant_speed_signal_forward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/double-slip_turnout_left.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/double-slip_turnout_right.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/end_of_movement_authority_backward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/end_of_movement_authority_forward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/friction_bufferstop_backward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/friction_bufferstop_forward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/hectometer.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/hump.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/interlocking.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/level_crossing_double.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/level_crossing_double_full_closure.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/level_crossing_single.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/loop_transmitter.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/main_line.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/main_track.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/messure_line.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/parked_vehicle.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/parked_vehicles.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/parked_vehicles_with_label.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/platform_left.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/platform_middle.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/platform_right.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/route.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/route_clearing_point_backward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/route_clearing_point_forward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/route_signal_backward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/route_signal_forward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/secondary_track.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/shunt_limit_backward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/shunt_limit_forward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/shunt_signal_backward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/shunt_signal_backward_locked.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/shunt_signal_forward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/shunt_signal_forward_locked.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/speed_signal_backward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/speed_signal_forward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/track_closure.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/track_distance.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/track_number.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/train_berth.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/train_berth_shape.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/train_berth_shape_bidirectional.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/train_berth_shape_special.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/train_berth_sign_backward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/train_berth_sign_forward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/train_direction_backward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/train_direction_forward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/train_drive_automatic.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/train_drive_human.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/train_ghost_direction_backward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/train_ghost_direction_forward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/train_moving_backward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/train_moving_fast_backward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/train_moving_fast_forward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/train_moving_forward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/train_moving_slow_backward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/train_moving_slow_forward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/train_shunt_mode_backward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/train_shunt_mode_forward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/train_shunting_backward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/train_shunting_forward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/transmitter.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/transmitter_backward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/transmitter_bidirectional.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/transmitter_forward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/transmitter_right.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/transmitter_right_bidirectional.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/transmitter_right_forward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/transmitter_right_with_signal.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/turnout_left_backward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/turnout_left_backward_left_position.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/turnout_left_backward_manually.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/turnout_left_backward_moving_points.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/turnout_left_backward_right_position.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/turnout_left_forward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/turnout_left_forward_left_position.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/turnout_left_forward_manually.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/turnout_left_forward_moving_points.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/turnout_left_forward_right_position.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/turnout_right_backward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/turnout_right_backward_left_position.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/turnout_right_backward_manually.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/turnout_right_backward_moving_points.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/turnout_right_backward_right_position.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/turnout_right_forward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/turnout_right_forward_left_position.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/turnout_right_forward_manually.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/turnout_right_forward_moving_points.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/turnout_right_forward_right_position.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/turnout_with_fouling_left_backward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/turnout_with_fouling_left_forward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/turnout_with_fouling_right_backward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/turnout_with_fouling_right_forward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/view_point_backward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/view_point_forward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic.pdf
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic.tex

%files -n texlive-tikz-trackschematic
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/tikz-trackschematic/tikzlibrarytrackschematic.code.tex
%{_texmfdistdir}/tex/latex/tikz-trackschematic/tikzlibrarytrackschematic.constructions.code.tex
%{_texmfdistdir}/tex/latex/tikz-trackschematic/tikzlibrarytrackschematic.messures.code.tex
%{_texmfdistdir}/tex/latex/tikz-trackschematic/tikzlibrarytrackschematic.topology.code.tex
%{_texmfdistdir}/tex/latex/tikz-trackschematic/tikzlibrarytrackschematic.trafficcontrol.code.tex
%{_texmfdistdir}/tex/latex/tikz-trackschematic/tikzlibrarytrackschematic.vehicles.code.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-tikz-trackschematic-%{texlive_version}.%{texlive_noarch}.0.0.5.1svn53754-%{release}-zypper
%endif

%package -n texlive-tikz-truchet
Version:        %{texlive_version}.%{texlive_noarch}.svn50020
Release:        0
Summary:        Draw Truchet tiles
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-tikz-truchet-doc >= %{texlive_version}
Provides:       tex(tikz-truchet.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(tikz.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source43:       tikz-truchet.tar.xz
Source44:       tikz-truchet.doc.tar.xz

%description -n texlive-tikz-truchet
This is a package for LaTeX that draws Truchet tiles, as used
in Colin Beveridge's article Too good to be Truchet in issue 08
of Chalkdust.

%package -n texlive-tikz-truchet-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn50020
Release:        0
Summary:        Documentation for texlive-tikz-truchet
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-tikz-truchet-doc
This package includes the documentation for texlive-tikz-truchet

%post -n texlive-tikz-truchet
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tikz-truchet 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tikz-truchet
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikz-truchet-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/tikz-truchet/README.md
%{_texmfdistdir}/doc/latex/tikz-truchet/tikz-truchet.pdf

%files -n texlive-tikz-truchet
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/tikz-truchet/tikz-truchet.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-tikz-truchet-%{texlive_version}.%{texlive_noarch}.svn50020-%{release}-zypper
%endif

%package -n texlive-tikzcodeblocks
Version:        %{texlive_version}.%{texlive_noarch}.0.0.13svn54758
Release:        0
Summary:        Helps to draw codeblocks like scratch, NEPO and PXT in TikZ
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-tikzcodeblocks-doc >= %{texlive_version}
Provides:       tex(tikzcodeblocks.sty)
Requires:       tex(adjustbox.sty)
Requires:       tex(colortbl.sty)
Requires:       tex(fontawesome.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(longtable.sty)
Requires:       tex(tikz.sty)
Requires:       tex(translations.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xspace.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source45:       tikzcodeblocks.tar.xz
Source46:       tikzcodeblocks.doc.tar.xz

%description -n texlive-tikzcodeblocks
tikzcodeblocks is a LaTeX package for typesetting blockwise
graphic programming languages like scratch, nepo or pxt.

%package -n texlive-tikzcodeblocks-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.13svn54758
Release:        0
Summary:        Documentation for texlive-tikzcodeblocks
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-tikzcodeblocks-doc:de)

%description -n texlive-tikzcodeblocks-doc
This package includes the documentation for texlive-tikzcodeblocks

%post -n texlive-tikzcodeblocks
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tikzcodeblocks 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tikzcodeblocks
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikzcodeblocks-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/tikzcodeblocks/README.md
%{_texmfdistdir}/doc/latex/tikzcodeblocks/examples/bsp-einruecken.tikz
%{_texmfdistdir}/doc/latex/tikzcodeblocks/examples/bsp-english.tikz
%{_texmfdistdir}/doc/latex/tikzcodeblocks/examples/bsp-hello-world.tikz
%{_texmfdistdir}/doc/latex/tikzcodeblocks/examples/bsp-openroberta-umgebung.tikz
%{_texmfdistdir}/doc/latex/tikzcodeblocks/examples/bsp-openroberta-zacken.tikz
%{_texmfdistdir}/doc/latex/tikzcodeblocks/examples/bsp-start-roberta.tikz
%{_texmfdistdir}/doc/latex/tikzcodeblocks/examples/bsp-start.tikz
%{_texmfdistdir}/doc/latex/tikzcodeblocks/examples/bsp-verschachtelt-zacken.tikz
%{_texmfdistdir}/doc/latex/tikzcodeblocks/examples/bsp-verzweigung.tikz
%{_texmfdistdir}/doc/latex/tikzcodeblocks/examples/smarthome.tikz
%{_texmfdistdir}/doc/latex/tikzcodeblocks/tikzcodeblocks-documentation.pdf
%{_texmfdistdir}/doc/latex/tikzcodeblocks/tikzcodeblocks-documentation.tex

%files -n texlive-tikzcodeblocks
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/tikzcodeblocks/tikzcodeblocks.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-tikzcodeblocks-%{texlive_version}.%{texlive_noarch}.0.0.13svn54758-%{release}-zypper
%endif

%package -n texlive-tikzducks
Version:        %{texlive_version}.%{texlive_noarch}.1.3svn53312
Release:        0
Summary:        A little fun package for using rubber ducks in TikZ
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-tikzducks-doc >= %{texlive_version}
Provides:       tex(tikzducks.sty)
Provides:       tex(tikzlibraryducks.code.tex)
Requires:       tex(tikz.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source47:       tikzducks.tar.xz
Source48:       tikzducks.doc.tar.xz

%description -n texlive-tikzducks
The package is a LaTeX package for ducks to be used in TikZ
pictures. This project is a continuation of an answer at
StackExchange How we can draw a duck?

%package -n texlive-tikzducks-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.3svn53312
Release:        0
Summary:        Documentation for texlive-tikzducks
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-tikzducks-doc
This package includes the documentation for texlive-tikzducks

%post -n texlive-tikzducks
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tikzducks 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tikzducks
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikzducks-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/tikzducks/README.md
%{_texmfdistdir}/doc/latex/tikzducks/tikzducks-doc.pdf
%{_texmfdistdir}/doc/latex/tikzducks/tikzducks-doc.tex

%files -n texlive-tikzducks
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/tikzducks/tikzducks.sty
%{_texmfdistdir}/tex/latex/tikzducks/tikzlibraryducks.code.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-tikzducks-%{texlive_version}.%{texlive_noarch}.1.3svn53312-%{release}-zypper
%endif

%package -n texlive-tikzinclude
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn28715
Release:        0
Summary:        Import TikZ images from colletions
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-tikzinclude-doc >= %{texlive_version}
Provides:       tex(tikzinclude.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(tikz.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source49:       tikzinclude.tar.xz
Source50:       tikzinclude.doc.tar.xz

%description -n texlive-tikzinclude
The package addresses the problem of importing only one
TikZ-image from a file holding multiple images.

%package -n texlive-tikzinclude-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn28715
Release:        0
Summary:        Documentation for texlive-tikzinclude
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-tikzinclude-doc
This package includes the documentation for texlive-tikzinclude

%post -n texlive-tikzinclude
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tikzinclude 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tikzinclude
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikzinclude-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/tikzinclude/README
%{_texmfdistdir}/doc/latex/tikzinclude/tikzinclude.pdf

%files -n texlive-tikzinclude
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/tikzinclude/tikzinclude.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-tikzinclude-%{texlive_version}.%{texlive_noarch}.1.0svn28715-%{release}-zypper
%endif

%package -n texlive-tikzlings
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2svn54080
Release:        0
Summary:        A collection of cute little animals and similar creatures
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-tikzlings-doc >= %{texlive_version}
Provides:       tex(tikzlings-addons.sty)
Provides:       tex(tikzlings-bears.sty)
Provides:       tex(tikzlings-cats.sty)
Provides:       tex(tikzlings-coatis.sty)
Provides:       tex(tikzlings-hippos.sty)
Provides:       tex(tikzlings-koalas.sty)
Provides:       tex(tikzlings-marmots.sty)
Provides:       tex(tikzlings-mice.sty)
Provides:       tex(tikzlings-moles.sty)
Provides:       tex(tikzlings-owls.sty)
Provides:       tex(tikzlings-pandas.sty)
Provides:       tex(tikzlings-penguins.sty)
Provides:       tex(tikzlings-pigs.sty)
Provides:       tex(tikzlings-rhinos.sty)
Provides:       tex(tikzlings-sloths.sty)
Provides:       tex(tikzlings-snowmans.sty)
Provides:       tex(tikzlings.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(tikz.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source51:       tikzlings.tar.xz
Source52:       tikzlings.doc.tar.xz

%description -n texlive-tikzlings
A collection of LaTeX packages for drawing cute little animals
and similar creatures using TikZ. Currently, the following
TikZlings are included: bear cat coati hippo koala marmot moles
mouse owl panda penguin pig rhino sloth snowman These little
drawings can be customized in many ways.

%package -n texlive-tikzlings-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2svn54080
Release:        0
Summary:        Documentation for texlive-tikzlings
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-tikzlings-doc
This package includes the documentation for texlive-tikzlings

%post -n texlive-tikzlings
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tikzlings 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tikzlings
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikzlings-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/tikzlings/README.md
%{_texmfdistdir}/doc/latex/tikzlings/tikzlings-doc.pdf
%{_texmfdistdir}/doc/latex/tikzlings/tikzlings-doc.tex

%files -n texlive-tikzlings
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/tikzlings/tikzlings-addons.sty
%{_texmfdistdir}/tex/latex/tikzlings/tikzlings-bears.sty
%{_texmfdistdir}/tex/latex/tikzlings/tikzlings-cats.sty
%{_texmfdistdir}/tex/latex/tikzlings/tikzlings-coatis.sty
%{_texmfdistdir}/tex/latex/tikzlings/tikzlings-hippos.sty
%{_texmfdistdir}/tex/latex/tikzlings/tikzlings-koalas.sty
%{_texmfdistdir}/tex/latex/tikzlings/tikzlings-marmots.sty
%{_texmfdistdir}/tex/latex/tikzlings/tikzlings-mice.sty
%{_texmfdistdir}/tex/latex/tikzlings/tikzlings-moles.sty
%{_texmfdistdir}/tex/latex/tikzlings/tikzlings-owls.sty
%{_texmfdistdir}/tex/latex/tikzlings/tikzlings-pandas.sty
%{_texmfdistdir}/tex/latex/tikzlings/tikzlings-penguins.sty
%{_texmfdistdir}/tex/latex/tikzlings/tikzlings-pigs.sty
%{_texmfdistdir}/tex/latex/tikzlings/tikzlings-rhinos.sty
%{_texmfdistdir}/tex/latex/tikzlings/tikzlings-sloths.sty
%{_texmfdistdir}/tex/latex/tikzlings/tikzlings-snowmans.sty
%{_texmfdistdir}/tex/latex/tikzlings/tikzlings.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-tikzlings-%{texlive_version}.%{texlive_noarch}.0.0.2svn54080-%{release}-zypper
%endif

%package -n texlive-tikzmark
Version:        %{texlive_version}.%{texlive_noarch}.1.8svn52293
Release:        0
Summary:        Use TikZ's method of remembering a position on a page
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-tikzmark-doc >= %{texlive_version}
Provides:       tex(tikzlibrarytikzmark.code.tex)
Provides:       tex(tikzmarklibrarylistings.code.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source53:       tikzmark.tar.xz
Source54:       tikzmark.doc.tar.xz

%description -n texlive-tikzmark
The tikzmark package defines a command to "remember" a position
on a page for later (or earlier) use, primarily (but not
exclusively) with TikZ.

%package -n texlive-tikzmark-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.8svn52293
Release:        0
Summary:        Documentation for texlive-tikzmark
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-tikzmark-doc
This package includes the documentation for texlive-tikzmark

%post -n texlive-tikzmark
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tikzmark 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tikzmark
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikzmark-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/tikzmark/README
%{_texmfdistdir}/doc/latex/tikzmark/README.txt
%{_texmfdistdir}/doc/latex/tikzmark/tikzmark.pdf

%files -n texlive-tikzmark
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/tikzmark/tikzlibrarytikzmark.code.tex
%{_texmfdistdir}/tex/latex/tikzmark/tikzmarklibrarylistings.code.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-tikzmark-%{texlive_version}.%{texlive_noarch}.1.8svn52293-%{release}-zypper
%endif

%package -n texlive-tikzmarmots
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn54080
Release:        0
Summary:        Drawing little marmots in TikZ
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-tikzmarmots-doc >= %{texlive_version}
Provides:       tex(tikzlibrarymarmots.code.tex)
Provides:       tex(tikzmarmots.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(tikz.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source55:       tikzmarmots.tar.xz
Source56:       tikzmarmots.doc.tar.xz

%description -n texlive-tikzmarmots
This is a LaTeX package for marmots to be used in TikZ
pictures. These little figures are constructed in such a way
that they may even "borrow" some garments and other attributes
from the TikZducks.

%package -n texlive-tikzmarmots-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn54080
Release:        0
Summary:        Documentation for texlive-tikzmarmots
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-tikzmarmots-doc
This package includes the documentation for texlive-tikzmarmots

%post -n texlive-tikzmarmots
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tikzmarmots 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tikzmarmots
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikzmarmots-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/tikzmarmots/LICENSE.txt
%{_texmfdistdir}/doc/latex/tikzmarmots/README.md
%{_texmfdistdir}/doc/latex/tikzmarmots/tikzmarmots-doc.pdf
%{_texmfdistdir}/doc/latex/tikzmarmots/tikzmarmots-doc.tex

%files -n texlive-tikzmarmots
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/tikzmarmots/tikzlibrarymarmots.code.tex
%{_texmfdistdir}/tex/latex/tikzmarmots/tikzmarmots.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-tikzmarmots-%{texlive_version}.%{texlive_noarch}.1.0svn54080-%{release}-zypper
%endif

%package -n texlive-tikzorbital
Version:        %{texlive_version}.%{texlive_noarch}.svn36439
Release:        0
Summary:        Atomic and molecular orbitals using TikZ
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-tikzorbital-doc >= %{texlive_version}
Provides:       tex(tikzorbital.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(tikz.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source57:       tikzorbital.tar.xz
Source58:       tikzorbital.doc.tar.xz

%description -n texlive-tikzorbital
Atomic s, p and d orbitals may be drawn, as well as molecular
orbital diagrams.

%package -n texlive-tikzorbital-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn36439
Release:        0
Summary:        Documentation for texlive-tikzorbital
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-tikzorbital-doc
This package includes the documentation for texlive-tikzorbital

%post -n texlive-tikzorbital
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tikzorbital 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tikzorbital
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikzorbital-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/tikzorbital/README.rst
%{_texmfdistdir}/doc/latex/tikzorbital/tikzorbital.pdf
%{_texmfdistdir}/doc/latex/tikzorbital/tikzorbital.tex

%files -n texlive-tikzorbital
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/tikzorbital/tikzorbital.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-tikzorbital-%{texlive_version}.%{texlive_noarch}.svn36439-%{release}-zypper
%endif

%package -n texlive-tikzpagenodes
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn27723
Release:        0
Summary:        A single TikZ node for the whole page
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-tikzpagenodes-doc >= %{texlive_version}
Provides:       tex(tikzpagenodes.sty)
Requires:       tex(ifoddpage.sty)
Requires:       tex(tikz.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source59:       tikzpagenodes.tar.xz
Source60:       tikzpagenodes.doc.tar.xz

%description -n texlive-tikzpagenodes
The package provides special PGF/TikZ nodes for the text,
marginpar, footer and header area of the current page. They are
inspired by the 'current page' node defined by PGF/TikZ itself.

%package -n texlive-tikzpagenodes-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn27723
Release:        0
Summary:        Documentation for texlive-tikzpagenodes
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-tikzpagenodes-doc
This package includes the documentation for texlive-tikzpagenodes

%post -n texlive-tikzpagenodes
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tikzpagenodes 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tikzpagenodes
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikzpagenodes-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/tikzpagenodes/README
%{_texmfdistdir}/doc/latex/tikzpagenodes/tikzpagenodes.pdf

%files -n texlive-tikzpagenodes
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/tikzpagenodes/tikzpagenodes.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-tikzpagenodes-%{texlive_version}.%{texlive_noarch}.1.1svn27723-%{release}-zypper
%endif

%package -n texlive-tikzpeople
Version:        %{texlive_version}.%{texlive_noarch}.0.0.4svn43978
Release:        0
Summary:        Draw people-shaped nodes in TikZ
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-tikzpeople-doc >= %{texlive_version}
Provides:       tex(tikzpeople.shape.alice.sty)
Provides:       tex(tikzpeople.shape.bob.sty)
Provides:       tex(tikzpeople.shape.bride.sty)
Provides:       tex(tikzpeople.shape.builder.sty)
Provides:       tex(tikzpeople.shape.businessman.sty)
Provides:       tex(tikzpeople.shape.charlie.sty)
Provides:       tex(tikzpeople.shape.chef.sty)
Provides:       tex(tikzpeople.shape.conductor.sty)
Provides:       tex(tikzpeople.shape.cowboy.sty)
Provides:       tex(tikzpeople.shape.criminal.sty)
Provides:       tex(tikzpeople.shape.dave.sty)
Provides:       tex(tikzpeople.shape.devil.sty)
Provides:       tex(tikzpeople.shape.duck.sty)
Provides:       tex(tikzpeople.shape.graduate.sty)
Provides:       tex(tikzpeople.shape.groom.sty)
Provides:       tex(tikzpeople.shape.guard.sty)
Provides:       tex(tikzpeople.shape.jester.sty)
Provides:       tex(tikzpeople.shape.judge.sty)
Provides:       tex(tikzpeople.shape.maninblack.sty)
Provides:       tex(tikzpeople.shape.mexican.sty)
Provides:       tex(tikzpeople.shape.nun.sty)
Provides:       tex(tikzpeople.shape.nurse.sty)
Provides:       tex(tikzpeople.shape.physician.sty)
Provides:       tex(tikzpeople.shape.pilot.sty)
Provides:       tex(tikzpeople.shape.police.sty)
Provides:       tex(tikzpeople.shape.priest.sty)
Provides:       tex(tikzpeople.shape.sailor.sty)
Provides:       tex(tikzpeople.shape.santa.sty)
Provides:       tex(tikzpeople.shape.surgeon.sty)
Provides:       tex(tikzpeople.sty)
Requires:       tex(calc.sty)
Requires:       tex(capt-of.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xifthen.sty)
Requires:       tex(xparse.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source61:       tikzpeople.tar.xz
Source62:       tikzpeople.doc.tar.xz

%description -n texlive-tikzpeople
This package provides people-shaped nodes in the style of
Microsoft Visio clip art, to be used with TikZ. The available,
highly customizable, node shapes are: alice, bob, bride,
builder, businessman, charlie, chef, conductor, cowboy,
criminal, dave, devil, duck, graduate, groom, guard, jester,
judge, maininblack, mexican, nun, nurse, physician, pilot,
police, priest, sailor, santa, surgeon.

%package -n texlive-tikzpeople-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.4svn43978
Release:        0
Summary:        Documentation for texlive-tikzpeople
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-tikzpeople-doc
This package includes the documentation for texlive-tikzpeople

%post -n texlive-tikzpeople
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tikzpeople 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tikzpeople
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikzpeople-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/tikzpeople/README.md
%{_texmfdistdir}/doc/latex/tikzpeople/tikzpeople.pdf
%{_texmfdistdir}/doc/latex/tikzpeople/tikzpeople.tex

%files -n texlive-tikzpeople
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/tikzpeople/tikzpeople.shape.alice.sty
%{_texmfdistdir}/tex/latex/tikzpeople/tikzpeople.shape.bob.sty
%{_texmfdistdir}/tex/latex/tikzpeople/tikzpeople.shape.bride.sty
%{_texmfdistdir}/tex/latex/tikzpeople/tikzpeople.shape.builder.sty
%{_texmfdistdir}/tex/latex/tikzpeople/tikzpeople.shape.businessman.sty
%{_texmfdistdir}/tex/latex/tikzpeople/tikzpeople.shape.charlie.sty
%{_texmfdistdir}/tex/latex/tikzpeople/tikzpeople.shape.chef.sty
%{_texmfdistdir}/tex/latex/tikzpeople/tikzpeople.shape.conductor.sty
%{_texmfdistdir}/tex/latex/tikzpeople/tikzpeople.shape.cowboy.sty
%{_texmfdistdir}/tex/latex/tikzpeople/tikzpeople.shape.criminal.sty
%{_texmfdistdir}/tex/latex/tikzpeople/tikzpeople.shape.dave.sty
%{_texmfdistdir}/tex/latex/tikzpeople/tikzpeople.shape.devil.sty
%{_texmfdistdir}/tex/latex/tikzpeople/tikzpeople.shape.duck.sty
%{_texmfdistdir}/tex/latex/tikzpeople/tikzpeople.shape.graduate.sty
%{_texmfdistdir}/tex/latex/tikzpeople/tikzpeople.shape.groom.sty
%{_texmfdistdir}/tex/latex/tikzpeople/tikzpeople.shape.guard.sty
%{_texmfdistdir}/tex/latex/tikzpeople/tikzpeople.shape.jester.sty
%{_texmfdistdir}/tex/latex/tikzpeople/tikzpeople.shape.judge.sty
%{_texmfdistdir}/tex/latex/tikzpeople/tikzpeople.shape.maninblack.sty
%{_texmfdistdir}/tex/latex/tikzpeople/tikzpeople.shape.mexican.sty
%{_texmfdistdir}/tex/latex/tikzpeople/tikzpeople.shape.nun.sty
%{_texmfdistdir}/tex/latex/tikzpeople/tikzpeople.shape.nurse.sty
%{_texmfdistdir}/tex/latex/tikzpeople/tikzpeople.shape.physician.sty
%{_texmfdistdir}/tex/latex/tikzpeople/tikzpeople.shape.pilot.sty
%{_texmfdistdir}/tex/latex/tikzpeople/tikzpeople.shape.police.sty
%{_texmfdistdir}/tex/latex/tikzpeople/tikzpeople.shape.priest.sty
%{_texmfdistdir}/tex/latex/tikzpeople/tikzpeople.shape.sailor.sty
%{_texmfdistdir}/tex/latex/tikzpeople/tikzpeople.shape.santa.sty
%{_texmfdistdir}/tex/latex/tikzpeople/tikzpeople.shape.surgeon.sty
%{_texmfdistdir}/tex/latex/tikzpeople/tikzpeople.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-tikzpeople-%{texlive_version}.%{texlive_noarch}.0.0.4svn43978-%{release}-zypper
%endif

%package -n texlive-tikzpfeile
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn25777
Release:        0
Summary:        Draw arrows using PGF/TikZ
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-tikzpfeile-doc >= %{texlive_version}
Provides:       tex(tikzpfeile.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(tikz.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source63:       tikzpfeile.tar.xz
Source64:       tikzpfeile.doc.tar.xz

%description -n texlive-tikzpfeile
In a document with a lot of diagrams created with PGF/TikZ,
there is a possibility of the reader being distracted by
different sorts of arrowheads in the diagrams and in the text
(as, e.g., in \rightarrow). The package defines macros to
create all arrows using PGF/TikZ, so as to avoid the problem.

%package -n texlive-tikzpfeile-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn25777
Release:        0
Summary:        Documentation for texlive-tikzpfeile
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-tikzpfeile-doc
This package includes the documentation for texlive-tikzpfeile

%post -n texlive-tikzpfeile
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tikzpfeile 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tikzpfeile
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikzpfeile-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/tikzpfeile/README
%{_texmfdistdir}/doc/latex/tikzpfeile/tikzpfeile.pdf

%files -n texlive-tikzpfeile
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/tikzpfeile/tikzpfeile.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-tikzpfeile-%{texlive_version}.%{texlive_noarch}.1.0svn25777-%{release}-zypper
%endif

%package -n texlive-tikzposter
Version:        %{texlive_version}.%{texlive_noarch}.2.0svn32732
Release:        0
Summary:        Create scientific posters using TikZ
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-tikzposter-doc >= %{texlive_version}
Provides:       tex(tikzposter.cls)
Provides:       tex(tikzposterBackgroundstyles.tex)
Provides:       tex(tikzposterBlockstyles.tex)
Provides:       tex(tikzposterColorpalettes.tex)
Provides:       tex(tikzposterColorstyles.tex)
Provides:       tex(tikzposterInnerblockstyles.tex)
Provides:       tex(tikzposterLayoutthemes.tex)
Provides:       tex(tikzposterNotestyles.tex)
Provides:       tex(tikzposterTitlestyles.tex)
Requires:       tex(a0size.sty)
Requires:       tex(ae.sty)
Requires:       tex(calc.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(extarticle.cls)
Requires:       tex(geometry.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xstring.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source65:       tikzposter.tar.xz
Source66:       tikzposter.doc.tar.xz

%description -n texlive-tikzposter
A document class provides a simple way of using TikZ for
generating posters. Several formatting options are available,
and spacing and layout of the poster is to a large extent
automated.

%package -n texlive-tikzposter-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.0svn32732
Release:        0
Summary:        Documentation for texlive-tikzposter
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-tikzposter-doc
This package includes the documentation for texlive-tikzposter

%post -n texlive-tikzposter
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tikzposter 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tikzposter
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikzposter-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/tikzposter/README
%{_texmfdistdir}/doc/latex/tikzposter/tikzposter-example.tex
%{_texmfdistdir}/doc/latex/tikzposter/tikzposter-template.tex
%{_texmfdistdir}/doc/latex/tikzposter/tikzposter.pdf

%files -n texlive-tikzposter
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/tikzposter/tikzposter.cls
%{_texmfdistdir}/tex/latex/tikzposter/tikzposterBackgroundstyles.tex
%{_texmfdistdir}/tex/latex/tikzposter/tikzposterBlockstyles.tex
%{_texmfdistdir}/tex/latex/tikzposter/tikzposterColorpalettes.tex
%{_texmfdistdir}/tex/latex/tikzposter/tikzposterColorstyles.tex
%{_texmfdistdir}/tex/latex/tikzposter/tikzposterInnerblockstyles.tex
%{_texmfdistdir}/tex/latex/tikzposter/tikzposterLayoutthemes.tex
%{_texmfdistdir}/tex/latex/tikzposter/tikzposterNotestyles.tex
%{_texmfdistdir}/tex/latex/tikzposter/tikzposterTitlestyles.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-tikzposter-%{texlive_version}.%{texlive_noarch}.2.0svn32732-%{release}-zypper
%endif

%package -n texlive-tikzscale
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2.6svn30637
Release:        0
Summary:        Resize pictures while respecting text size
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-tikzscale-doc >= %{texlive_version}
Provides:       tex(tikzscale.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(letltxmacro.sty)
Requires:       tex(pgfkeys.sty)
Requires:       tex(xparse.sty)
Requires:       tex(xstring.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source67:       tikzscale.tar.xz
Source68:       tikzscale.doc.tar.xz

%description -n texlive-tikzscale
The package extends the \includegraphics command to support
tikzpictures. It allows scaling of TikZ images and PGFPlots to
a given width or height without changing the text size.

%package -n texlive-tikzscale-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2.6svn30637
Release:        0
Summary:        Documentation for texlive-tikzscale
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-tikzscale-doc
This package includes the documentation for texlive-tikzscale

%post -n texlive-tikzscale
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tikzscale 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tikzscale
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikzscale-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/tikzscale/3Dplot.tikz
%{_texmfdistdir}/doc/latex/tikzscale/README
%{_texmfdistdir}/doc/latex/tikzscale/alt.tikz
%{_texmfdistdir}/doc/latex/tikzscale/histogramNormal.tikz
%{_texmfdistdir}/doc/latex/tikzscale/invisible.tikz
%{_texmfdistdir}/doc/latex/tikzscale/linewidth.tikz
%{_texmfdistdir}/doc/latex/tikzscale/only.tikz
%{_texmfdistdir}/doc/latex/tikzscale/onslide.tikz
%{_texmfdistdir}/doc/latex/tikzscale/pause.tikz
%{_texmfdistdir}/doc/latex/tikzscale/pgfplots-test.tikz
%{_texmfdistdir}/doc/latex/tikzscale/pgfplots.randn.dat
%{_texmfdistdir}/doc/latex/tikzscale/temporal.tikz
%{_texmfdistdir}/doc/latex/tikzscale/test-tikzscale.pdf
%{_texmfdistdir}/doc/latex/tikzscale/test-tikzscale.tex
%{_texmfdistdir}/doc/latex/tikzscale/testNode.tikz
%{_texmfdistdir}/doc/latex/tikzscale/testRectangle.tikz
%{_texmfdistdir}/doc/latex/tikzscale/testgraphic2D.tikz
%{_texmfdistdir}/doc/latex/tikzscale/tikzscale-beamer.tex
%{_texmfdistdir}/doc/latex/tikzscale/tikzscale.pdf
%{_texmfdistdir}/doc/latex/tikzscale/uncover.tikz
%{_texmfdistdir}/doc/latex/tikzscale/visible.tikz

%files -n texlive-tikzscale
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/tikzscale/tikzscale.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-tikzscale-%{texlive_version}.%{texlive_noarch}.0.0.2.6svn30637-%{release}-zypper
%endif

%package -n texlive-tikzsymbols
Version:        %{texlive_version}.%{texlive_noarch}.4.10csvn49975
Release:        0
Summary:        Some symbols created using TikZ
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-tikzsymbols-doc >= %{texlive_version}
Provides:       tex(tikzsymbols.sty)
Requires:       tex(expl3.sty)
Requires:       tex(l3keys2e.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xparse.sty)
Requires:       tex(xspace.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source69:       tikzsymbols.tar.xz
Source70:       tikzsymbols.doc.tar.xz

%description -n texlive-tikzsymbols
The package provides various emoticons, cooking symbols and
trees.

%package -n texlive-tikzsymbols-doc
Version:        %{texlive_version}.%{texlive_noarch}.4.10csvn49975
Release:        0
Summary:        Documentation for texlive-tikzsymbols
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-tikzsymbols-doc
This package includes the documentation for texlive-tikzsymbols

%post -n texlive-tikzsymbols
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tikzsymbols 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tikzsymbols
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikzsymbols-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/tikzsymbols/README.md
%{_texmfdistdir}/doc/latex/tikzsymbols/tikzsymbols.pdf

%files -n texlive-tikzsymbols
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/tikzsymbols/tikzsymbols.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-tikzsymbols-%{texlive_version}.%{texlive_noarch}.4.10csvn49975-%{release}-zypper
%endif

%package -n texlive-timbreicmc
Version:        %{texlive_version}.%{texlive_noarch}.2.0svn49740
Release:        0
Summary:        Typeset documents with ICMC/USP watermarks
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-timbreicmc-doc >= %{texlive_version}
Provides:       tex(timbreicmc.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xwatermark.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source71:       timbreicmc.tar.xz
Source72:       timbreicmc.doc.tar.xz

%description -n texlive-timbreicmc
With this package you can typeset documents with ICMC/USP Sao
Carlos watermarks. ICMC is acronym for "Instituto de Ciencias
Matematicas e de Computacao" of the "Universidade de Sao Paulo"
(USP), in the city of Sao Carlos-SP, Brazil.

%package -n texlive-timbreicmc-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.0svn49740
Release:        0
Summary:        Documentation for texlive-timbreicmc
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-timbreicmc-doc
This package includes the documentation for texlive-timbreicmc

%post -n texlive-timbreicmc
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-timbreicmc 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-timbreicmc
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-timbreicmc-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/timbreicmc/README.md
%{_texmfdistdir}/doc/latex/timbreicmc/timbreicmc.pdf

%files -n texlive-timbreicmc
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/timbreicmc/timbreicmc.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-timbreicmc-%{texlive_version}.%{texlive_noarch}.2.0svn49740-%{release}-zypper
%endif

%package -n texlive-times
Version:        %{texlive_version}.%{texlive_noarch}.svn35058
Release:        0
Summary:        URW "Base 35" font pack for LaTeX
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
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
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Requires:       texlive-times-fonts >= %{texlive_version}
Provides:       tex(8rutm.fd)
Provides:       tex(omlutm.fd)
Provides:       tex(omsutm.fd)
Provides:       tex(ot1utm.fd)
Provides:       tex(psyro.tfm)
Provides:       tex(ptmb.tfm)
Provides:       tex(ptmb.vf)
Provides:       tex(ptmb7t.tfm)
Provides:       tex(ptmb7t.vf)
Provides:       tex(ptmb8c.tfm)
Provides:       tex(ptmb8c.vf)
Provides:       tex(ptmb8r.tfm)
Provides:       tex(ptmb8t.tfm)
Provides:       tex(ptmb8t.vf)
Provides:       tex(ptmbc.tfm)
Provides:       tex(ptmbc.vf)
Provides:       tex(ptmbc7t.tfm)
Provides:       tex(ptmbc7t.vf)
Provides:       tex(ptmbc8t.tfm)
Provides:       tex(ptmbc8t.vf)
Provides:       tex(ptmbi.tfm)
Provides:       tex(ptmbi.vf)
Provides:       tex(ptmbi7t.tfm)
Provides:       tex(ptmbi7t.vf)
Provides:       tex(ptmbi8c.tfm)
Provides:       tex(ptmbi8c.vf)
Provides:       tex(ptmbi8r.tfm)
Provides:       tex(ptmbi8t.tfm)
Provides:       tex(ptmbi8t.vf)
Provides:       tex(ptmbo.tfm)
Provides:       tex(ptmbo.vf)
Provides:       tex(ptmbo7t.tfm)
Provides:       tex(ptmbo7t.vf)
Provides:       tex(ptmbo8c.tfm)
Provides:       tex(ptmbo8c.vf)
Provides:       tex(ptmbo8r.tfm)
Provides:       tex(ptmbo8t.tfm)
Provides:       tex(ptmbo8t.vf)
Provides:       tex(ptmr.tfm)
Provides:       tex(ptmr.vf)
Provides:       tex(ptmr7t.tfm)
Provides:       tex(ptmr7t.vf)
Provides:       tex(ptmr8c.tfm)
Provides:       tex(ptmr8c.vf)
Provides:       tex(ptmr8r.tfm)
Provides:       tex(ptmr8rn.tfm)
Provides:       tex(ptmr8t.tfm)
Provides:       tex(ptmr8t.vf)
Provides:       tex(ptmrc.tfm)
Provides:       tex(ptmrc.vf)
Provides:       tex(ptmrc7t.tfm)
Provides:       tex(ptmrc7t.vf)
Provides:       tex(ptmrc8t.tfm)
Provides:       tex(ptmrc8t.vf)
Provides:       tex(ptmri.tfm)
Provides:       tex(ptmri.vf)
Provides:       tex(ptmri7t.tfm)
Provides:       tex(ptmri7t.vf)
Provides:       tex(ptmri8c.tfm)
Provides:       tex(ptmri8c.vf)
Provides:       tex(ptmri8r.tfm)
Provides:       tex(ptmri8t.tfm)
Provides:       tex(ptmri8t.vf)
Provides:       tex(ptmro.tfm)
Provides:       tex(ptmro.vf)
Provides:       tex(ptmro7t.tfm)
Provides:       tex(ptmro7t.vf)
Provides:       tex(ptmro8c.tfm)
Provides:       tex(ptmro8c.vf)
Provides:       tex(ptmro8r.tfm)
Provides:       tex(ptmro8t.tfm)
Provides:       tex(ptmro8t.vf)
Provides:       tex(ptmrr8re.tfm)
Provides:       tex(ptmrre.tfm)
Provides:       tex(ptmrre.vf)
Provides:       tex(ptmrrn.tfm)
Provides:       tex(ptmrrn.vf)
Provides:       tex(t1utm.fd)
Provides:       tex(ts1utm.fd)
Provides:       tex(utm.map)
Provides:       tex(utmb7t.tfm)
Provides:       tex(utmb7t.vf)
Provides:       tex(utmb8c.tfm)
Provides:       tex(utmb8c.vf)
Provides:       tex(utmb8r.tfm)
Provides:       tex(utmb8t.tfm)
Provides:       tex(utmb8t.vf)
Provides:       tex(utmbc7t.tfm)
Provides:       tex(utmbc7t.vf)
Provides:       tex(utmbc8t.tfm)
Provides:       tex(utmbc8t.vf)
Provides:       tex(utmbi7t.tfm)
Provides:       tex(utmbi7t.vf)
Provides:       tex(utmbi8c.tfm)
Provides:       tex(utmbi8c.vf)
Provides:       tex(utmbi8r.tfm)
Provides:       tex(utmbi8t.tfm)
Provides:       tex(utmbi8t.vf)
Provides:       tex(utmbo7t.tfm)
Provides:       tex(utmbo7t.vf)
Provides:       tex(utmbo8c.tfm)
Provides:       tex(utmbo8c.vf)
Provides:       tex(utmbo8r.tfm)
Provides:       tex(utmbo8t.tfm)
Provides:       tex(utmbo8t.vf)
Provides:       tex(utmr7t.tfm)
Provides:       tex(utmr7t.vf)
Provides:       tex(utmr8c.tfm)
Provides:       tex(utmr8c.vf)
Provides:       tex(utmr8r.tfm)
Provides:       tex(utmr8t.tfm)
Provides:       tex(utmr8t.vf)
Provides:       tex(utmrc7t.tfm)
Provides:       tex(utmrc7t.vf)
Provides:       tex(utmrc8t.tfm)
Provides:       tex(utmrc8t.vf)
Provides:       tex(utmri7t.tfm)
Provides:       tex(utmri7t.vf)
Provides:       tex(utmri8c.tfm)
Provides:       tex(utmri8c.vf)
Provides:       tex(utmri8r.tfm)
Provides:       tex(utmri8t.tfm)
Provides:       tex(utmri8t.vf)
Provides:       tex(utmro7t.tfm)
Provides:       tex(utmro7t.vf)
Provides:       tex(utmro8c.tfm)
Provides:       tex(utmro8c.vf)
Provides:       tex(utmro8r.tfm)
Provides:       tex(utmro8t.tfm)
Provides:       tex(utmro8t.vf)
Provides:       tex(zpsycmrv.tfm)
Provides:       tex(zpsycmrv.vf)
Provides:       tex(zptmcm7m.tfm)
Provides:       tex(zptmcm7m.vf)
Provides:       tex(zptmcm7t.tfm)
Provides:       tex(zptmcm7t.vf)
Provides:       tex(zptmcm7v.tfm)
Provides:       tex(zptmcm7v.vf)
Provides:       tex(zptmcm7y.tfm)
Provides:       tex(zptmcm7y.vf)
Provides:       tex(zptmcmr.tfm)
Provides:       tex(zptmcmr.vf)
Provides:       tex(zptmcmrm.tfm)
Provides:       tex(zptmcmrm.vf)
Provides:       tex(zpzccmry.tfm)
Provides:       tex(zpzccmry.vf)
Requires:       tex(cmex10.tfm)
Requires:       tex(cmex9.tfm)
Requires:       tex(cmmi10.tfm)
Requires:       tex(cmr10.tfm)
Requires:       tex(cmsy10.tfm)
Requires:       tex(psyr.tfm)
Requires:       tex(pzcmi8r.tfm)
Requires:       tex(rsfs10.tfm)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source73:       times.tar.xz

%description -n texlive-times
A set of fonts for use as "drop-in" replacements for Adobe's
basic set, comprising: Century Schoolbook (substituting for
Adobe's New Century Schoolbook); Dingbats (substituting for
Adobe's Zapf Dingbats); Nimbus Mono L (substituting for Abobe's
Courier); Nimbus Roman No9 L (substituting for Adobe's Times);
Nimbus Sans L (substituting for Adobe's Helvetica); Standard
Symbols L (substituting for Adobe's Symbol); URW Bookman; URW
Chancery L Medium Italic (substituting for Adobe's Zapf
Chancery); URW Gothic L Book (substituting for Adobe's Avant
Garde); and URW Palladio L (substituting for Adobe's Palatino).

%package -n texlive-times-fonts
Version:        %{texlive_version}.%{texlive_noarch}.svn35058
Release:        0
Summary:        Severed fonts for texlive-times
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Fonts
URL:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-times-fonts
The  separated fonts package for texlive-times
%post -n texlive-times
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap utm.map' >> /var/run/texlive/run-updmap

%postun -n texlive-times 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap utm.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-times
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-times-fonts
%files -n texlive-times
%defattr(-,root,root,755)
%{_texmfdistdir}/dvips/times/config.utm
%{_texmfdistdir}/fonts/afm/adobe/times/ptmb8a.afm
%{_texmfdistdir}/fonts/afm/adobe/times/ptmbi8a.afm
%{_texmfdistdir}/fonts/afm/adobe/times/ptmr8a.afm
%{_texmfdistdir}/fonts/afm/adobe/times/ptmri8a.afm
%{_texmfdistdir}/fonts/afm/urw/times/utmb8a.afm
%{_texmfdistdir}/fonts/afm/urw/times/utmbi8a.afm
%{_texmfdistdir}/fonts/afm/urw/times/utmr8a.afm
%{_texmfdistdir}/fonts/afm/urw/times/utmri8a.afm
%{_texmfdistdir}/fonts/map/dvips/times/utm.map
%{_texmfdistdir}/fonts/tfm/adobe/times/psyro.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/ptmb.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/ptmb7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/ptmb8c.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/ptmb8r.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/ptmb8t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/ptmbc.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/ptmbc7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/ptmbc8t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/ptmbi.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/ptmbi7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/ptmbi8c.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/ptmbi8r.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/ptmbi8t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/ptmbo.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/ptmbo7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/ptmbo8c.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/ptmbo8r.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/ptmbo8t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/ptmr.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/ptmr7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/ptmr8c.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/ptmr8r.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/ptmr8rn.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/ptmr8t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/ptmrc.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/ptmrc7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/ptmrc8t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/ptmri.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/ptmri7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/ptmri8c.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/ptmri8r.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/ptmri8t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/ptmro.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/ptmro7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/ptmro8c.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/ptmro8r.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/ptmro8t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/ptmrr8re.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/ptmrre.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/ptmrrn.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/zpsycmrv.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/zptmcm7m.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/zptmcm7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/zptmcm7v.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/zptmcm7y.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/zptmcmr.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/zptmcmrm.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/zpzccmry.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/times/utmb7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/times/utmb8c.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/times/utmb8r.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/times/utmb8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/times/utmbc7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/times/utmbc8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/times/utmbi7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/times/utmbi8c.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/times/utmbi8r.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/times/utmbi8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/times/utmbo7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/times/utmbo8c.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/times/utmbo8r.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/times/utmbo8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/times/utmr7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/times/utmr8c.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/times/utmr8r.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/times/utmr8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/times/utmrc7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/times/utmrc8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/times/utmri7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/times/utmri8c.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/times/utmri8r.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/times/utmri8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/times/utmro7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/times/utmro8c.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/times/utmro8r.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/times/utmro8t.tfm
%verify(link) %{_texmfdistdir}/fonts/type1/urw/times/utmb8a.pfb
%{_texmfdistdir}/fonts/type1/urw/times/utmb8a.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/urw/times/utmbi8a.pfb
%{_texmfdistdir}/fonts/type1/urw/times/utmbi8a.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/urw/times/utmr8a.pfb
%{_texmfdistdir}/fonts/type1/urw/times/utmr8a.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/urw/times/utmri8a.pfb
%{_texmfdistdir}/fonts/type1/urw/times/utmri8a.pfm
%{_texmfdistdir}/fonts/vf/adobe/times/ptmb.vf
%{_texmfdistdir}/fonts/vf/adobe/times/ptmb7t.vf
%{_texmfdistdir}/fonts/vf/adobe/times/ptmb8c.vf
%{_texmfdistdir}/fonts/vf/adobe/times/ptmb8t.vf
%{_texmfdistdir}/fonts/vf/adobe/times/ptmbc.vf
%{_texmfdistdir}/fonts/vf/adobe/times/ptmbc7t.vf
%{_texmfdistdir}/fonts/vf/adobe/times/ptmbc8t.vf
%{_texmfdistdir}/fonts/vf/adobe/times/ptmbi.vf
%{_texmfdistdir}/fonts/vf/adobe/times/ptmbi7t.vf
%{_texmfdistdir}/fonts/vf/adobe/times/ptmbi8c.vf
%{_texmfdistdir}/fonts/vf/adobe/times/ptmbi8t.vf
%{_texmfdistdir}/fonts/vf/adobe/times/ptmbo.vf
%{_texmfdistdir}/fonts/vf/adobe/times/ptmbo7t.vf
%{_texmfdistdir}/fonts/vf/adobe/times/ptmbo8c.vf
%{_texmfdistdir}/fonts/vf/adobe/times/ptmbo8t.vf
%{_texmfdistdir}/fonts/vf/adobe/times/ptmr.vf
%{_texmfdistdir}/fonts/vf/adobe/times/ptmr7t.vf
%{_texmfdistdir}/fonts/vf/adobe/times/ptmr8c.vf
%{_texmfdistdir}/fonts/vf/adobe/times/ptmr8t.vf
%{_texmfdistdir}/fonts/vf/adobe/times/ptmrc.vf
%{_texmfdistdir}/fonts/vf/adobe/times/ptmrc7t.vf
%{_texmfdistdir}/fonts/vf/adobe/times/ptmrc8t.vf
%{_texmfdistdir}/fonts/vf/adobe/times/ptmri.vf
%{_texmfdistdir}/fonts/vf/adobe/times/ptmri7t.vf
%{_texmfdistdir}/fonts/vf/adobe/times/ptmri8c.vf
%{_texmfdistdir}/fonts/vf/adobe/times/ptmri8t.vf
%{_texmfdistdir}/fonts/vf/adobe/times/ptmro.vf
%{_texmfdistdir}/fonts/vf/adobe/times/ptmro7t.vf
%{_texmfdistdir}/fonts/vf/adobe/times/ptmro8c.vf
%{_texmfdistdir}/fonts/vf/adobe/times/ptmro8t.vf
%{_texmfdistdir}/fonts/vf/adobe/times/ptmrre.vf
%{_texmfdistdir}/fonts/vf/adobe/times/ptmrrn.vf
%{_texmfdistdir}/fonts/vf/adobe/times/zpsycmrv.vf
%{_texmfdistdir}/fonts/vf/adobe/times/zptmcm7m.vf
%{_texmfdistdir}/fonts/vf/adobe/times/zptmcm7t.vf
%{_texmfdistdir}/fonts/vf/adobe/times/zptmcm7v.vf
%{_texmfdistdir}/fonts/vf/adobe/times/zptmcm7y.vf
%{_texmfdistdir}/fonts/vf/adobe/times/zptmcmr.vf
%{_texmfdistdir}/fonts/vf/adobe/times/zptmcmrm.vf
%{_texmfdistdir}/fonts/vf/adobe/times/zpzccmry.vf
%{_texmfdistdir}/fonts/vf/urw35vf/times/utmb7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/times/utmb8c.vf
%{_texmfdistdir}/fonts/vf/urw35vf/times/utmb8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/times/utmbc7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/times/utmbc8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/times/utmbi7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/times/utmbi8c.vf
%{_texmfdistdir}/fonts/vf/urw35vf/times/utmbi8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/times/utmbo7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/times/utmbo8c.vf
%{_texmfdistdir}/fonts/vf/urw35vf/times/utmbo8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/times/utmr7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/times/utmr8c.vf
%{_texmfdistdir}/fonts/vf/urw35vf/times/utmr8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/times/utmrc7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/times/utmrc8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/times/utmri7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/times/utmri8c.vf
%{_texmfdistdir}/fonts/vf/urw35vf/times/utmri8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/times/utmro7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/times/utmro8c.vf
%{_texmfdistdir}/fonts/vf/urw35vf/times/utmro8t.vf
%{_texmfdistdir}/tex/latex/times/8rutm.fd
%{_texmfdistdir}/tex/latex/times/omlutm.fd
%{_texmfdistdir}/tex/latex/times/omsutm.fd
%{_texmfdistdir}/tex/latex/times/ot1utm.fd
%{_texmfdistdir}/tex/latex/times/t1utm.fd
%{_texmfdistdir}/tex/latex/times/ts1utm.fd

%files -n texlive-times-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-times
%{_datadir}/fontconfig/conf.avail/58-texlive-times.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-times/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-times/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-times/fonts.scale
%{_datadir}/fonts/texlive-times/utmb8a.pfb
%{_datadir}/fonts/texlive-times/utmbi8a.pfb
%{_datadir}/fonts/texlive-times/utmr8a.pfb
%{_datadir}/fonts/texlive-times/utmri8a.pfb
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-times-fonts-%{texlive_version}.%{texlive_noarch}.svn35058-%{release}-zypper
%endif

%package -n texlive-timetable
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Generate timetables
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Provides:       tex(timetable.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source74:       timetable.tar.xz

%description -n texlive-timetable
A highly-configurable package, with nice output and simple
input. The macros use a radix sort mechanism so that the order
of input is not critical.
%post -n texlive-timetable
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-timetable 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-timetable
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-timetable
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/plain/timetable/timetable.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-timetable-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif

%package -n texlive-timing-diagrams
Version:        %{texlive_version}.%{texlive_noarch}.svn31491
Release:        0
Summary:        Draw timing diagrams
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-timing-diagrams-doc >= %{texlive_version}
Provides:       tex(timing-diagrams.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(tikz.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source75:       timing-diagrams.tar.xz
Source76:       timing-diagrams.doc.tar.xz

%description -n texlive-timing-diagrams
The package provides commands to draw and annotate various
kinds of timing diagrams, using Tikz. Documentation is sparse,
but the source and the examples file should be of some use.

%package -n texlive-timing-diagrams-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn31491
Release:        0
Summary:        Documentation for texlive-timing-diagrams
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-timing-diagrams-doc
This package includes the documentation for texlive-timing-diagrams

%post -n texlive-timing-diagrams
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-timing-diagrams 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-timing-diagrams
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-timing-diagrams-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/timing-diagrams/Makefile
%{_texmfdistdir}/doc/latex/timing-diagrams/README
%{_texmfdistdir}/doc/latex/timing-diagrams/diagrams-examples.pdf
%{_texmfdistdir}/doc/latex/timing-diagrams/diagrams-examples.tex
%{_texmfdistdir}/doc/latex/timing-diagrams/version.txt

%files -n texlive-timing-diagrams
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/timing-diagrams/timing-diagrams.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-timing-diagrams-%{texlive_version}.%{texlive_noarch}.svn31491-%{release}-zypper
%endif

%package -n texlive-tinos
Version:        %{texlive_version}.%{texlive_noarch}.svn42882
Release:        0
Summary:        Tinos fonts with LaTeX support
License:        Apache-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
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
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Requires:       texlive-tinos-fonts >= %{texlive_version}
Recommends:     texlive-tinos-doc >= %{texlive_version}
Provides:       tex(LY1Tinos-TLF.fd)
Provides:       tex(OT1Tinos-TLF.fd)
Provides:       tex(T1Tinos-TLF.fd)
Provides:       tex(TS1Tinos-TLF.fd)
Provides:       tex(Tinos-Bold-tlf-ly1.tfm)
Provides:       tex(Tinos-Bold-tlf-ot1.tfm)
Provides:       tex(Tinos-Bold-tlf-t1--base.tfm)
Provides:       tex(Tinos-Bold-tlf-t1.tfm)
Provides:       tex(Tinos-Bold-tlf-t1.vf)
Provides:       tex(Tinos-Bold-tlf-ts1--base.tfm)
Provides:       tex(Tinos-Bold-tlf-ts1.tfm)
Provides:       tex(Tinos-Bold-tlf-ts1.vf)
Provides:       tex(Tinos-BoldItalic-tlf-ly1.tfm)
Provides:       tex(Tinos-BoldItalic-tlf-ot1.tfm)
Provides:       tex(Tinos-BoldItalic-tlf-t1--base.tfm)
Provides:       tex(Tinos-BoldItalic-tlf-t1.tfm)
Provides:       tex(Tinos-BoldItalic-tlf-t1.vf)
Provides:       tex(Tinos-BoldItalic-tlf-ts1--base.tfm)
Provides:       tex(Tinos-BoldItalic-tlf-ts1.tfm)
Provides:       tex(Tinos-BoldItalic-tlf-ts1.vf)
Provides:       tex(Tinos-Italic-tlf-ly1.tfm)
Provides:       tex(Tinos-Italic-tlf-ot1.tfm)
Provides:       tex(Tinos-Italic-tlf-t1--base.tfm)
Provides:       tex(Tinos-Italic-tlf-t1.tfm)
Provides:       tex(Tinos-Italic-tlf-t1.vf)
Provides:       tex(Tinos-Italic-tlf-ts1--base.tfm)
Provides:       tex(Tinos-Italic-tlf-ts1.tfm)
Provides:       tex(Tinos-Italic-tlf-ts1.vf)
Provides:       tex(Tinos-tlf-ly1.tfm)
Provides:       tex(Tinos-tlf-ot1.tfm)
Provides:       tex(Tinos-tlf-t1--base.tfm)
Provides:       tex(Tinos-tlf-t1.tfm)
Provides:       tex(Tinos-tlf-t1.vf)
Provides:       tex(Tinos-tlf-ts1--base.tfm)
Provides:       tex(Tinos-tlf-ts1.tfm)
Provides:       tex(Tinos-tlf-ts1.vf)
Provides:       tex(tinos.map)
Provides:       tex(tinos.sty)
Provides:       tex(tns_27astb.enc)
Provides:       tex(tns_s6t4vy.enc)
Provides:       tex(tns_xze2cy.enc)
Provides:       tex(tns_y6kixo.enc)
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source77:       tinos.tar.xz
Source78:       tinos.doc.tar.xz

%description -n texlive-tinos
Tinos, designed by Steve Matteson, is an innovative, refreshing
serif design that is metrically compatible with Times New
Roman.

%package -n texlive-tinos-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn42882
Release:        0
Summary:        Documentation for texlive-tinos
License:        Apache-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-tinos-doc
This package includes the documentation for texlive-tinos


%package -n texlive-tinos-fonts
Version:        %{texlive_version}.%{texlive_noarch}.svn42882
Release:        0
Summary:        Severed fonts for texlive-tinos
License:        Apache-1.0
Group:          Productivity/Publishing/TeX/Fonts
URL:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-tinos-fonts
The  separated fonts package for texlive-tinos
%post -n texlive-tinos
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap tinos.map' >> /var/run/texlive/run-updmap

%postun -n texlive-tinos 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap tinos.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-tinos
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-tinos-fonts
%files -n texlive-tinos-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/tinos/LICENSE.txt
%{_texmfdistdir}/doc/fonts/tinos/README
%{_texmfdistdir}/doc/fonts/tinos/tinos-samples.pdf
%{_texmfdistdir}/doc/fonts/tinos/tinos-samples.tex

%files -n texlive-tinos
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/enc/dvips/tinos/tns_27astb.enc
%{_texmfdistdir}/fonts/enc/dvips/tinos/tns_s6t4vy.enc
%{_texmfdistdir}/fonts/enc/dvips/tinos/tns_xze2cy.enc
%{_texmfdistdir}/fonts/enc/dvips/tinos/tns_y6kixo.enc
%{_texmfdistdir}/fonts/map/dvips/tinos/tinos.map
%{_texmfdistdir}/fonts/tfm/google/tinos/Tinos-Bold-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/tinos/Tinos-Bold-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/tinos/Tinos-Bold-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/tinos/Tinos-Bold-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/tinos/Tinos-Bold-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/tinos/Tinos-Bold-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/tinos/Tinos-BoldItalic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/tinos/Tinos-BoldItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/tinos/Tinos-BoldItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/tinos/Tinos-BoldItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/tinos/Tinos-BoldItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/tinos/Tinos-BoldItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/tinos/Tinos-Italic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/tinos/Tinos-Italic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/tinos/Tinos-Italic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/tinos/Tinos-Italic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/tinos/Tinos-Italic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/tinos/Tinos-Italic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/tinos/Tinos-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/tinos/Tinos-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/tinos/Tinos-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/tinos/Tinos-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/tinos/Tinos-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/tinos/Tinos-tlf-ts1.tfm
%verify(link) %{_texmfdistdir}/fonts/truetype/google/tinos/Tinos-Bold.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/google/tinos/Tinos-BoldItalic.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/google/tinos/Tinos-Italic.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/google/tinos/Tinos-Regular.ttf
%verify(link) %{_texmfdistdir}/fonts/type1/google/tinos/Tinos-Bold.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/google/tinos/Tinos-BoldItalic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/google/tinos/Tinos-Italic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/google/tinos/Tinos.pfb
%{_texmfdistdir}/fonts/vf/google/tinos/Tinos-Bold-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/google/tinos/Tinos-Bold-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/tinos/Tinos-BoldItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/google/tinos/Tinos-BoldItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/tinos/Tinos-Italic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/google/tinos/Tinos-Italic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/tinos/Tinos-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/google/tinos/Tinos-tlf-ts1.vf
%{_texmfdistdir}/tex/latex/tinos/LY1Tinos-TLF.fd
%{_texmfdistdir}/tex/latex/tinos/OT1Tinos-TLF.fd
%{_texmfdistdir}/tex/latex/tinos/T1Tinos-TLF.fd
%{_texmfdistdir}/tex/latex/tinos/TS1Tinos-TLF.fd
%{_texmfdistdir}/tex/latex/tinos/tinos.sty

%files -n texlive-tinos-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-tinos
%{_datadir}/fontconfig/conf.avail/58-texlive-tinos.conf
%{_datadir}/fontconfig/conf.avail/55-texlive-tinos.conf
%config %{_sysconfdir}/fonts/conf.d/55-texlive-tinos.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-tinos/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-tinos/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-tinos/fonts.scale
%{_datadir}/fonts/texlive-tinos/Tinos-Bold.ttf
%{_datadir}/fonts/texlive-tinos/Tinos-BoldItalic.ttf
%{_datadir}/fonts/texlive-tinos/Tinos-Italic.ttf
%{_datadir}/fonts/texlive-tinos/Tinos-Regular.ttf
%{_datadir}/fonts/texlive-tinos/Tinos-Bold.pfb
%{_datadir}/fonts/texlive-tinos/Tinos-BoldItalic.pfb
%{_datadir}/fonts/texlive-tinos/Tinos-Italic.pfb
%{_datadir}/fonts/texlive-tinos/Tinos.pfb
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-tinos-fonts-%{texlive_version}.%{texlive_noarch}.svn42882-%{release}-zypper
%endif

%package -n texlive-tipa
Version:        %{texlive_version}.%{texlive_noarch}.1.3svn29349
Release:        0
Summary:        Fonts and macros for IPA phonetics characters
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
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
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Requires:       texlive-tipa-fonts >= %{texlive_version}
Recommends:     texlive-tipa-doc >= %{texlive_version}
Provides:       tex(exaccent.sty)
Provides:       tex(extraipa.sty)
Provides:       tex(t3cmr.fd)
Provides:       tex(t3cmss.fd)
Provides:       tex(t3cmtt.fd)
Provides:       tex(t3enc.def)
Provides:       tex(t3phv.fd)
Provides:       tex(t3ptm.fd)
Provides:       tex(tipa.map)
Provides:       tex(tipa.sty)
Provides:       tex(tipa10.tfm)
Provides:       tex(tipa12.tfm)
Provides:       tex(tipa17.tfm)
Provides:       tex(tipa8.tfm)
Provides:       tex(tipa9.tfm)
Provides:       tex(tipab10.tfm)
Provides:       tex(tipabs10.tfm)
Provides:       tex(tipabx10.tfm)
Provides:       tex(tipabx12.tfm)
Provides:       tex(tipabx8.tfm)
Provides:       tex(tipabx9.tfm)
Provides:       tex(tipaprm.def)
Provides:       tex(tipasb10.tfm)
Provides:       tex(tipasi10.tfm)
Provides:       tex(tipasl10.tfm)
Provides:       tex(tipasl12.tfm)
Provides:       tex(tipasl8.tfm)
Provides:       tex(tipasl9.tfm)
Provides:       tex(tipass10.tfm)
Provides:       tex(tipass12.tfm)
Provides:       tex(tipass17.tfm)
Provides:       tex(tipass8.tfm)
Provides:       tex(tipass9.tfm)
Provides:       tex(tipats10.tfm)
Provides:       tex(tipatt10.tfm)
Provides:       tex(tipatt12.tfm)
Provides:       tex(tipatt8.tfm)
Provides:       tex(tipatt9.tfm)
Provides:       tex(tipx.sty)
Provides:       tex(tipx10.tfm)
Provides:       tex(tipx12.tfm)
Provides:       tex(tipx17.tfm)
Provides:       tex(tipx8.tfm)
Provides:       tex(tipx9.tfm)
Provides:       tex(tipxb10.tfm)
Provides:       tex(tipxbs10.tfm)
Provides:       tex(tipxbx10.tfm)
Provides:       tex(tipxbx12.tfm)
Provides:       tex(tipxbx8.tfm)
Provides:       tex(tipxbx9.tfm)
Provides:       tex(tipxsb10.tfm)
Provides:       tex(tipxsi10.tfm)
Provides:       tex(tipxsl10.tfm)
Provides:       tex(tipxsl12.tfm)
Provides:       tex(tipxsl8.tfm)
Provides:       tex(tipxsl9.tfm)
Provides:       tex(tipxss10.tfm)
Provides:       tex(tipxss12.tfm)
Provides:       tex(tipxss17.tfm)
Provides:       tex(tipxss8.tfm)
Provides:       tex(tipxss9.tfm)
Provides:       tex(tipxts10.tfm)
Provides:       tex(tipxtt10.tfm)
Provides:       tex(tipxtt12.tfm)
Provides:       tex(tipxtt8.tfm)
Provides:       tex(tipxtt9.tfm)
Provides:       tex(tone.sty)
Provides:       tex(ts3cmr.fd)
Provides:       tex(ts3cmss.fd)
Provides:       tex(ts3cmtt.fd)
Provides:       tex(ts3enc.def)
Provides:       tex(ts3phv.fd)
Provides:       tex(ts3ptm.fd)
Provides:       tex(utipx.fd)
Provides:       tex(utipxss.fd)
Provides:       tex(utipxtt.fd)
Provides:       tex(uxipx.fd)
Provides:       tex(uxipxss.fd)
Provides:       tex(vowel.sty)
Provides:       tex(xipa10.tfm)
Provides:       tex(xipab10.tfm)
Provides:       tex(xipabs10.tfm)
Provides:       tex(xipaprm.def)
Provides:       tex(xipasb10.tfm)
Provides:       tex(xipasi10.tfm)
Provides:       tex(xipasl10.tfm)
Provides:       tex(xipass10.tfm)
Provides:       tex(xipx10.tfm)
Provides:       tex(xipxb10.tfm)
Provides:       tex(xipxbs10.tfm)
Provides:       tex(xipxsb10.tfm)
Provides:       tex(xipxsi10.tfm)
Provides:       tex(xipxsl10.tfm)
Provides:       tex(xipxss10.tfm)
Requires:       tex(fontenc.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source79:       tipa.tar.xz
Source80:       tipa.doc.tar.xz

%description -n texlive-tipa
These fonts are considered the 'ultimate answer' to IPA
typesetting. The encoding of these 8-bit fonts has been
registered as LaTeX standard encoding T3, and the set of
addendum symbols as encoding TS3. 'Times-like' Adobe Type 1
versions are provided for both the T3 and the TS3 fonts.

%package -n texlive-tipa-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.3svn29349
Release:        0
Summary:        Documentation for texlive-tipa
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-tipa-doc:en)

%description -n texlive-tipa-doc
This package includes the documentation for texlive-tipa


%package -n texlive-tipa-fonts
Version:        %{texlive_version}.%{texlive_noarch}.1.3svn29349
Release:        0
Summary:        Severed fonts for texlive-tipa
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Fonts
URL:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-tipa-fonts
The  separated fonts package for texlive-tipa
%post -n texlive-tipa
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMixedMap tipa.map' >> /var/run/texlive/run-updmap

%postun -n texlive-tipa 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMixedMap tipa.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-tipa
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-tipa-fonts
%files -n texlive-tipa-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/tipa/00README
%{_texmfdistdir}/doc/fonts/tipa/00README.doc
%{_texmfdistdir}/doc/fonts/tipa/Makefile
%{_texmfdistdir}/doc/fonts/tipa/Makefile.doc
%{_texmfdistdir}/doc/fonts/tipa/Manifest.txt
%{_texmfdistdir}/doc/fonts/tipa/boxchar.sty
%{_texmfdistdir}/doc/fonts/tipa/codelist.sty
%{_texmfdistdir}/doc/fonts/tipa/gentfm.sh
%{_texmfdistdir}/doc/fonts/tipa/gentipa.sh
%{_texmfdistdir}/doc/fonts/tipa/gentipx.sh
%{_texmfdistdir}/doc/fonts/tipa/genxipa.sh
%{_texmfdistdir}/doc/fonts/tipa/genxipx.sh
%{_texmfdistdir}/doc/fonts/tipa/mktipapk.sh
%{_texmfdistdir}/doc/fonts/tipa/mkxipapk.sh
%{_texmfdistdir}/doc/fonts/tipa/tipa.bib
%{_texmfdistdir}/doc/fonts/tipa/tipaman.pdf
%{_texmfdistdir}/doc/fonts/tipa/tipaman.sty
%{_texmfdistdir}/doc/fonts/tipa/tipaman.tex
%{_texmfdistdir}/doc/fonts/tipa/tipaman0.tex
%{_texmfdistdir}/doc/fonts/tipa/tipaman1.tex
%{_texmfdistdir}/doc/fonts/tipa/tipaman2.tex
%{_texmfdistdir}/doc/fonts/tipa/tipaman3.tex
%{_texmfdistdir}/doc/fonts/tipa/tipaman4.tex
%{_texmfdistdir}/doc/fonts/tipa/vowel.pdf
%{_texmfdistdir}/doc/fonts/tipa/vowel.tex

%files -n texlive-tipa
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/map/dvips/tipa/tipa.map
%{_texmfdistdir}/fonts/source/public/tipa/tipa.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipa10.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipa12.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipa17.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipa8.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipa9.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipab10.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipabase.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipabs10.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipabx10.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipabx12.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipabx8.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipabx9.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipadiac.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipaextr.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipagerm.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipanew.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipapnct.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipaprm.def
%{_texmfdistdir}/fonts/source/public/tipa/tiparoml.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipasb10.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipasc.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipasi10.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipasl10.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipasl12.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipasl8.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipasl9.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipass10.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipass12.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipass17.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipass8.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipass9.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipasym1.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipasym2.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipasym3.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipasym4.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipatone.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipatr.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipats10.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipatt10.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipatt12.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipatt8.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipatt9.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipx.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipx10.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipx12.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipx17.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipx8.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipx9.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipxb10.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipxbs10.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipxbx10.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipxbx12.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipxbx8.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipxbx9.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipxsb10.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipxsi10.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipxsl10.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipxsl12.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipxsl8.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipxsl9.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipxss10.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipxss12.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipxss17.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipxss8.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipxss9.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipxts10.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipxtt10.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipxtt12.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipxtt8.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipxtt9.mf
%{_texmfdistdir}/fonts/source/public/tipa/xipa10.mf
%{_texmfdistdir}/fonts/source/public/tipa/xipab10.mf
%{_texmfdistdir}/fonts/source/public/tipa/xipabs10.mf
%{_texmfdistdir}/fonts/source/public/tipa/xipaprm.def
%{_texmfdistdir}/fonts/source/public/tipa/xipasb10.mf
%{_texmfdistdir}/fonts/source/public/tipa/xipasi10.mf
%{_texmfdistdir}/fonts/source/public/tipa/xipasl10.mf
%{_texmfdistdir}/fonts/source/public/tipa/xipass10.mf
%{_texmfdistdir}/fonts/source/public/tipa/xipx10.mf
%{_texmfdistdir}/fonts/source/public/tipa/xipxb10.mf
%{_texmfdistdir}/fonts/source/public/tipa/xipxbs10.mf
%{_texmfdistdir}/fonts/source/public/tipa/xipxsb10.mf
%{_texmfdistdir}/fonts/source/public/tipa/xipxsi10.mf
%{_texmfdistdir}/fonts/source/public/tipa/xipxsl10.mf
%{_texmfdistdir}/fonts/source/public/tipa/xipxss10.mf
%{_texmfdistdir}/fonts/tfm/public/tipa/tipa10.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipa12.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipa17.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipa8.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipa9.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipab10.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipabs10.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipabx10.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipabx12.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipabx8.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipabx9.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipasb10.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipasi10.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipasl10.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipasl12.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipasl8.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipasl9.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipass10.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipass12.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipass17.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipass8.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipass9.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipats10.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipatt10.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipatt12.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipatt8.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipatt9.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipx10.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipx12.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipx17.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipx8.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipx9.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipxb10.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipxbs10.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipxbx10.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipxbx12.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipxbx8.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipxbx9.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipxsb10.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipxsi10.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipxsl10.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipxsl12.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipxsl8.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipxsl9.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipxss10.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipxss12.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipxss17.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipxss8.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipxss9.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipxts10.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipxtt10.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipxtt12.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipxtt8.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipxtt9.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/xipa10.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/xipab10.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/xipabs10.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/xipasb10.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/xipasi10.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/xipasl10.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/xipass10.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/xipx10.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/xipxb10.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/xipxbs10.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/xipxsb10.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/xipxsi10.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/xipxsl10.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/xipxss10.tfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/tipa/tipa10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/tipa/tipa12.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/tipa/tipa17.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/tipa/tipa8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/tipa/tipa9.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/tipa/tipab10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/tipa/tipabs10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/tipa/tipabx10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/tipa/tipabx12.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/tipa/tipabx8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/tipa/tipabx9.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/tipa/tipasb10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/tipa/tipasi10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/tipa/tipasl10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/tipa/tipasl12.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/tipa/tipasl8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/tipa/tipasl9.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/tipa/tipass10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/tipa/tipass12.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/tipa/tipass17.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/tipa/tipass8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/tipa/tipass9.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/tipa/tipats10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/tipa/tipatt10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/tipa/tipatt12.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/tipa/tipatt8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/tipa/tipatt9.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/tipa/tipx10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/tipa/tipx12.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/tipa/tipx17.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/tipa/tipx8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/tipa/tipx9.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/tipa/tipxb10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/tipa/tipxbs10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/tipa/tipxbx10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/tipa/tipxbx12.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/tipa/tipxbx8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/tipa/tipxbx9.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/tipa/tipxsb10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/tipa/tipxsi10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/tipa/tipxsl10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/tipa/tipxsl12.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/tipa/tipxsl8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/tipa/tipxsl9.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/tipa/tipxss10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/tipa/tipxss12.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/tipa/tipxss17.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/tipa/tipxss8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/tipa/tipxss9.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/tipa/tipxts10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/tipa/tipxtt10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/tipa/tipxtt12.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/tipa/tipxtt8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/tipa/tipxtt9.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/tipa/xipa10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/tipa/xipab10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/tipa/xipabs10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/tipa/xipasb10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/tipa/xipasi10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/tipa/xipasl10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/tipa/xipass10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/tipa/xipx10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/tipa/xipxb10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/tipa/xipxbs10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/tipa/xipxsb10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/tipa/xipxsi10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/tipa/xipxsl10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/tipa/xipxss10.pfb
%{_texmfdistdir}/tex/latex/tipa/exaccent.sty
%{_texmfdistdir}/tex/latex/tipa/extraipa.sty
%{_texmfdistdir}/tex/latex/tipa/t3cmr.fd
%{_texmfdistdir}/tex/latex/tipa/t3cmss.fd
%{_texmfdistdir}/tex/latex/tipa/t3cmtt.fd
%{_texmfdistdir}/tex/latex/tipa/t3enc.def
%{_texmfdistdir}/tex/latex/tipa/t3phv.fd
%{_texmfdistdir}/tex/latex/tipa/t3ptm.fd
%{_texmfdistdir}/tex/latex/tipa/tipa.sty
%{_texmfdistdir}/tex/latex/tipa/tipx.sty
%{_texmfdistdir}/tex/latex/tipa/tone.sty
%{_texmfdistdir}/tex/latex/tipa/ts3cmr.fd
%{_texmfdistdir}/tex/latex/tipa/ts3cmss.fd
%{_texmfdistdir}/tex/latex/tipa/ts3cmtt.fd
%{_texmfdistdir}/tex/latex/tipa/ts3enc.def
%{_texmfdistdir}/tex/latex/tipa/ts3phv.fd
%{_texmfdistdir}/tex/latex/tipa/ts3ptm.fd
%{_texmfdistdir}/tex/latex/tipa/utipx.fd
%{_texmfdistdir}/tex/latex/tipa/utipxss.fd
%{_texmfdistdir}/tex/latex/tipa/utipxtt.fd
%{_texmfdistdir}/tex/latex/tipa/uxipx.fd
%{_texmfdistdir}/tex/latex/tipa/uxipxss.fd
%{_texmfdistdir}/tex/latex/tipa/vowel.sty

%files -n texlive-tipa-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-tipa
%{_datadir}/fontconfig/conf.avail/58-texlive-tipa.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-tipa/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-tipa/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-tipa/fonts.scale
%{_datadir}/fonts/texlive-tipa/tipa10.pfb
%{_datadir}/fonts/texlive-tipa/tipa12.pfb
%{_datadir}/fonts/texlive-tipa/tipa17.pfb
%{_datadir}/fonts/texlive-tipa/tipa8.pfb
%{_datadir}/fonts/texlive-tipa/tipa9.pfb
%{_datadir}/fonts/texlive-tipa/tipab10.pfb
%{_datadir}/fonts/texlive-tipa/tipabs10.pfb
%{_datadir}/fonts/texlive-tipa/tipabx10.pfb
%{_datadir}/fonts/texlive-tipa/tipabx12.pfb
%{_datadir}/fonts/texlive-tipa/tipabx8.pfb
%{_datadir}/fonts/texlive-tipa/tipabx9.pfb
%{_datadir}/fonts/texlive-tipa/tipasb10.pfb
%{_datadir}/fonts/texlive-tipa/tipasi10.pfb
%{_datadir}/fonts/texlive-tipa/tipasl10.pfb
%{_datadir}/fonts/texlive-tipa/tipasl12.pfb
%{_datadir}/fonts/texlive-tipa/tipasl8.pfb
%{_datadir}/fonts/texlive-tipa/tipasl9.pfb
%{_datadir}/fonts/texlive-tipa/tipass10.pfb
%{_datadir}/fonts/texlive-tipa/tipass12.pfb
%{_datadir}/fonts/texlive-tipa/tipass17.pfb
%{_datadir}/fonts/texlive-tipa/tipass8.pfb
%{_datadir}/fonts/texlive-tipa/tipass9.pfb
%{_datadir}/fonts/texlive-tipa/tipats10.pfb
%{_datadir}/fonts/texlive-tipa/tipatt10.pfb
%{_datadir}/fonts/texlive-tipa/tipatt12.pfb
%{_datadir}/fonts/texlive-tipa/tipatt8.pfb
%{_datadir}/fonts/texlive-tipa/tipatt9.pfb
%{_datadir}/fonts/texlive-tipa/tipx10.pfb
%{_datadir}/fonts/texlive-tipa/tipx12.pfb
%{_datadir}/fonts/texlive-tipa/tipx17.pfb
%{_datadir}/fonts/texlive-tipa/tipx8.pfb
%{_datadir}/fonts/texlive-tipa/tipx9.pfb
%{_datadir}/fonts/texlive-tipa/tipxb10.pfb
%{_datadir}/fonts/texlive-tipa/tipxbs10.pfb
%{_datadir}/fonts/texlive-tipa/tipxbx10.pfb
%{_datadir}/fonts/texlive-tipa/tipxbx12.pfb
%{_datadir}/fonts/texlive-tipa/tipxbx8.pfb
%{_datadir}/fonts/texlive-tipa/tipxbx9.pfb
%{_datadir}/fonts/texlive-tipa/tipxsb10.pfb
%{_datadir}/fonts/texlive-tipa/tipxsi10.pfb
%{_datadir}/fonts/texlive-tipa/tipxsl10.pfb
%{_datadir}/fonts/texlive-tipa/tipxsl12.pfb
%{_datadir}/fonts/texlive-tipa/tipxsl8.pfb
%{_datadir}/fonts/texlive-tipa/tipxsl9.pfb
%{_datadir}/fonts/texlive-tipa/tipxss10.pfb
%{_datadir}/fonts/texlive-tipa/tipxss12.pfb
%{_datadir}/fonts/texlive-tipa/tipxss17.pfb
%{_datadir}/fonts/texlive-tipa/tipxss8.pfb
%{_datadir}/fonts/texlive-tipa/tipxss9.pfb
%{_datadir}/fonts/texlive-tipa/tipxts10.pfb
%{_datadir}/fonts/texlive-tipa/tipxtt10.pfb
%{_datadir}/fonts/texlive-tipa/tipxtt12.pfb
%{_datadir}/fonts/texlive-tipa/tipxtt8.pfb
%{_datadir}/fonts/texlive-tipa/tipxtt9.pfb
%{_datadir}/fonts/texlive-tipa/xipa10.pfb
%{_datadir}/fonts/texlive-tipa/xipab10.pfb
%{_datadir}/fonts/texlive-tipa/xipabs10.pfb
%{_datadir}/fonts/texlive-tipa/xipasb10.pfb
%{_datadir}/fonts/texlive-tipa/xipasi10.pfb
%{_datadir}/fonts/texlive-tipa/xipasl10.pfb
%{_datadir}/fonts/texlive-tipa/xipass10.pfb
%{_datadir}/fonts/texlive-tipa/xipx10.pfb
%{_datadir}/fonts/texlive-tipa/xipxb10.pfb
%{_datadir}/fonts/texlive-tipa/xipxbs10.pfb
%{_datadir}/fonts/texlive-tipa/xipxsb10.pfb
%{_datadir}/fonts/texlive-tipa/xipxsi10.pfb
%{_datadir}/fonts/texlive-tipa/xipxsl10.pfb
%{_datadir}/fonts/texlive-tipa/xipxss10.pfb
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-tipa-fonts-%{texlive_version}.%{texlive_noarch}.1.3svn29349-%{release}-zypper
%endif

%package -n texlive-tipa-de
Version:        %{texlive_version}.%{texlive_noarch}.1.3svn22005
Release:        0
Summary:        German translation of tipa documentation
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source81:       tipa-de.doc.tar.xz

%description -n texlive-tipa-de
This is a translation of Fukui Rei's tipaman from the tipa
bundle.
%post -n texlive-tipa-de
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tipa-de 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tipa-de
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tipa-de
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/tipa-de/LIESMICH
%{_texmfdistdir}/doc/latex/tipa-de/tipa.bib
%{_texmfdistdir}/doc/latex/tipa-de/tipaman-de.pdf
%{_texmfdistdir}/doc/latex/tipa-de/tipaman-de.tex
%{_texmfdistdir}/doc/latex/tipa-de/tipaman0-de.tex
%{_texmfdistdir}/doc/latex/tipa-de/tipaman1-de.tex
%{_texmfdistdir}/doc/latex/tipa-de/tipaman2-de.tex
%{_texmfdistdir}/doc/latex/tipa-de/tipaman3-de.tex
%{_texmfdistdir}/doc/latex/tipa-de/tipaman4-de.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-tipa-de-%{texlive_version}.%{texlive_noarch}.1.3svn22005-%{release}-zypper
%endif

%package -n texlive-tipfr
Version:        %{texlive_version}.%{texlive_noarch}.1.5svn38646
Release:        0
Summary:        Produces calculator's keys with the help of TikZ
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-tipfr-doc >= %{texlive_version}
Provides:       tex(tipfr.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(mathtools.sty)
Requires:       tex(multido.sty)
Requires:       tex(newtxtt.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source82:       tipfr.tar.xz
Source83:       tipfr.doc.tar.xz

%description -n texlive-tipfr
The package provides commands to draw calculator keys with the
help of TikZ. It also provides commands to draw the content of
screens and of menu items.

%package -n texlive-tipfr-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.5svn38646
Release:        0
Summary:        Documentation for texlive-tipfr
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-tipfr-doc:fr)

%description -n texlive-tipfr-doc
This package includes the documentation for texlive-tipfr

%post -n texlive-tipfr
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tipfr 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tipfr
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tipfr-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/tipfr/IndexHead.ist
%{_texmfdistdir}/doc/latex/tipfr/README
%{_texmfdistdir}/doc/latex/tipfr/tipfr-doc.pdf
%{_texmfdistdir}/doc/latex/tipfr/tipfr-doc.tex

%files -n texlive-tipfr
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/tipfr/tipfr.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-tipfr-%{texlive_version}.%{texlive_noarch}.1.5svn38646-%{release}-zypper
%endif

%package -n texlive-titlecaps
Version:        %{texlive_version}.%{texlive_noarch}.1.2svn36170
Release:        0
Summary:        Setting rich-text input into Titling Caps
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-titlecaps-doc >= %{texlive_version}
Provides:       tex(titlecaps.sty)
Requires:       tex(ifnextok.sty)
Requires:       tex(ifthen.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source84:       titlecaps.tar.xz
Source85:       titlecaps.doc.tar.xz

%description -n texlive-titlecaps
The package is intended for setting rich text into titling
capitals (in which the first character of words are
capitalized). It automatically accounts for diacritical marks
(like umlauts), national symbols (like "ae"), punctuation, and
font changing commands that alter the appearance or size of the
text. It allows a list of predesignated words to be protected
as lower-cased, and also allows for titling exceptions of
various sorts.

%package -n texlive-titlecaps-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.2svn36170
Release:        0
Summary:        Documentation for texlive-titlecaps
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-titlecaps-doc
This package includes the documentation for texlive-titlecaps

%post -n texlive-titlecaps
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-titlecaps 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-titlecaps
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-titlecaps-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/titlecaps/README
%{_texmfdistdir}/doc/latex/titlecaps/titlecaps.pdf
%{_texmfdistdir}/doc/latex/titlecaps/titlecaps.tex

%files -n texlive-titlecaps
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/titlecaps/titlecaps.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-titlecaps-%{texlive_version}.%{texlive_noarch}.1.2svn36170-%{release}-zypper
%endif

%package -n texlive-titlefoot
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Add special material to footer of title page
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Provides:       tex(titlefoot.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source86:       titlefoot.tar.xz

%description -n texlive-titlefoot
Provides the capability of adding keywords (with a \keywords
command), a running title (\runningtitle), AMS subject
classifications (\amssubj), and an 'author's footnote' as
footnotes to the title or first page of a document. Works with
any class for which the \thanks macro works (e.g., article).
%post -n texlive-titlefoot
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-titlefoot 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-titlefoot
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-titlefoot
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/titlefoot/titlefoot.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-titlefoot-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif

%package -n texlive-titlepages
Version:        %{texlive_version}.%{texlive_noarch}.svn19457
Release:        0
Summary:        Sample titlepages, and how to code them
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source87:       titlepages.doc.tar.xz

%description -n texlive-titlepages
The document provides examples of over two dozen title page
designs based on a range of published books and theses,
together with the LaTeX code used to create them.
%post -n texlive-titlepages
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-titlepages 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-titlepages
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-titlepages
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/titlepages/README
%{_texmfdistdir}/doc/latex/titlepages/titlepages.pdf
%{_texmfdistdir}/doc/latex/titlepages/titlepages.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-titlepages-%{texlive_version}.%{texlive_noarch}.svn19457-%{release}-zypper
%endif

%package -n texlive-titlepic
Version:        %{texlive_version}.%{texlive_noarch}.1.2svn43497
Release:        0
Summary:        Add picture to title page of a document
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-titlepic-doc >= %{texlive_version}
Provides:       tex(titlepic.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source88:       titlepic.tar.xz
Source89:       titlepic.doc.tar.xz

%description -n texlive-titlepic
The package allows you to place a picture on the title page
(cover page) of a LaTeX document. Example of usage:
\usepackage[cc]{titlepic} \usepackage{graphicx}
\titlepic{\includegraphics[width=\textwidth]{picture.png}} The
package currently only works with the document classes article,
report and book.

%package -n texlive-titlepic-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.2svn43497
Release:        0
Summary:        Documentation for texlive-titlepic
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-titlepic-doc
This package includes the documentation for texlive-titlepic

%post -n texlive-titlepic
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-titlepic 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-titlepic
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-titlepic-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/titlepic/README.md
%{_texmfdistdir}/doc/latex/titlepic/titlepic-manual.pdf
%{_texmfdistdir}/doc/latex/titlepic/titlepic-manual.tex

%files -n texlive-titlepic
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/titlepic/titlepic.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-titlepic-%{texlive_version}.%{texlive_noarch}.1.2svn43497-%{release}-zypper
%endif

%package -n texlive-titleref
Version:        %{texlive_version}.%{texlive_noarch}.3.1svn18729
Release:        0
Summary:        A "\titleref" command to cross-reference section titles
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-titleref-doc >= %{texlive_version}
Provides:       tex(titleref.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source90:       titleref.tar.xz
Source91:       titleref.doc.tar.xz

%description -n texlive-titleref
Defines a command \titleref that allows you to cross-reference
section (and chapter, etc) titles and captions just like \ref
and \pageref. The package does not interwork with hyperref; if
you need hypertext capabilities, use nameref instead.

%package -n texlive-titleref-doc
Version:        %{texlive_version}.%{texlive_noarch}.3.1svn18729
Release:        0
Summary:        Documentation for texlive-titleref
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-titleref-doc
This package includes the documentation for texlive-titleref

%post -n texlive-titleref
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-titleref 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-titleref
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-titleref-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/titleref/miscdoc.sty
%{_texmfdistdir}/doc/latex/titleref/titleref.pdf
%{_texmfdistdir}/doc/latex/titleref/titleref.tex

%files -n texlive-titleref
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/titleref/titleref.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-titleref-%{texlive_version}.%{texlive_noarch}.3.1svn18729-%{release}-zypper
%endif

%package -n texlive-titlesec
Version:        %{texlive_version}.%{texlive_noarch}.2.13svn52413
Release:        0
Summary:        Select alternative section titles
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-titlesec-doc >= %{texlive_version}
Provides:       tex(titleps.sty)
Provides:       tex(titlesec.sty)
Provides:       tex(titletoc.sty)
Requires:       tex(etex.sty)
Requires:       tex(keyval.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source92:       titlesec.tar.xz
Source93:       titlesec.doc.tar.xz

%description -n texlive-titlesec
A package providing an interface to sectioning commands for
selection from various title styles. E.g., marginal titles and
to change the font of all headings with a single command, also
providing simple one-step page styles. Also includes a package
to change the page styles when there are floats in a page. You
may assign headers/footers to individual floats, too.

%package -n texlive-titlesec-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.13svn52413
Release:        0
Summary:        Documentation for texlive-titlesec
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-titlesec-doc
This package includes the documentation for texlive-titlesec

%post -n texlive-titlesec
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-titlesec 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-titlesec
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-titlesec-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/titlesec/CHANGES.old
%{_texmfdistdir}/doc/latex/titlesec/README.md
%{_texmfdistdir}/doc/latex/titlesec/titleps.pdf
%{_texmfdistdir}/doc/latex/titlesec/titleps.tex
%{_texmfdistdir}/doc/latex/titlesec/titlesec.pdf
%{_texmfdistdir}/doc/latex/titlesec/titlesec.tex

%files -n texlive-titlesec
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/titlesec/titleps.sty
%{_texmfdistdir}/tex/latex/titlesec/titlesec.sty
%{_texmfdistdir}/tex/latex/titlesec/titletoc.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-titlesec-%{texlive_version}.%{texlive_noarch}.2.13svn52413-%{release}-zypper
%endif

%package -n texlive-titling
Version:        %{texlive_version}.%{texlive_noarch}.2.1dsvn15878
Release:        0
Summary:        Control over the typesetting of the \maketitle command
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-titling-doc >= %{texlive_version}
Provides:       tex(titling.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source94:       titling.tar.xz
Source95:       titling.doc.tar.xz

%description -n texlive-titling
The titling package provides control over the typesetting of
the \maketitle command and \thanks commands, and makes the
\title, \author and \date information permanently available.
Multiple titles are allowed in a single document. New titling
elements can be added and a titlepage title can be centered on
a physical page.

%package -n texlive-titling-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.1dsvn15878
Release:        0
Summary:        Documentation for texlive-titling
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-titling-doc
This package includes the documentation for texlive-titling

%post -n texlive-titling
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-titling 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-titling
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-titling-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/titling/README
%{_texmfdistdir}/doc/latex/titling/titling.pdf

%files -n texlive-titling
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/titling/titling.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-titling-%{texlive_version}.%{texlive_noarch}.2.1dsvn15878-%{release}-zypper
%endif

%package -n texlive-tkz-base
Version:        %{texlive_version}.%{texlive_noarch}.3.06csvn54758
Release:        0
Summary:        Tools for drawing with a cartesian coordinate system
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-tkz-base-doc >= %{texlive_version}
Provides:       tex(tkz-base.cfg)
Provides:       tex(tkz-base.sty)
Provides:       tex(tkz-lib-marks.tex)
Provides:       tex(tkz-obj-axes.tex)
Provides:       tex(tkz-obj-grids.tex)
Provides:       tex(tkz-obj-marks.tex)
Provides:       tex(tkz-obj-points.tex)
Provides:       tex(tkz-obj-rep.tex)
Provides:       tex(tkz-tools-BB.tex)
Provides:       tex(tkz-tools-arith.tex)
Provides:       tex(tkz-tools-base.tex)
Provides:       tex(tkz-tools-misc.tex)
Provides:       tex(tkz-tools-modules.tex)
Provides:       tex(tkz-tools-print.tex)
Provides:       tex(tkz-tools-text.tex)
Provides:       tex(tkz-tools-utilities.tex)
Requires:       tex(etex.sty)
Requires:       tex(fp.sty)
Requires:       tex(numprint.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xfp.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source96:       tkz-base.tar.xz
Source97:       tkz-base.doc.tar.xz

%description -n texlive-tkz-base
The bundle is a set of packages, designed to give mathematics
teachers (and students) easy access to programming of drawings
with TikZ.

%package -n texlive-tkz-base-doc
Version:        %{texlive_version}.%{texlive_noarch}.3.06csvn54758
Release:        0
Summary:        Documentation for texlive-tkz-base
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-tkz-base-doc:fr)

%description -n texlive-tkz-base-doc
This package includes the documentation for texlive-tkz-base

%post -n texlive-tkz-base
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tkz-base 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tkz-base
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tkz-base-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/tkz-base/README.md
%{_texmfdistdir}/doc/latex/tkz-base/TKZdoc-base-BB.tex
%{_texmfdistdir}/doc/latex/tkz-base/TKZdoc-base-axes.tex
%{_texmfdistdir}/doc/latex/tkz-base/TKZdoc-base-compilation.tex
%{_texmfdistdir}/doc/latex/tkz-base/TKZdoc-base-divers.tex
%{_texmfdistdir}/doc/latex/tkz-base/TKZdoc-base-faq.tex
%{_texmfdistdir}/doc/latex/tkz-base/TKZdoc-base-grid.tex
%{_texmfdistdir}/doc/latex/tkz-base/TKZdoc-base-initialisation.tex
%{_texmfdistdir}/doc/latex/tkz-base/TKZdoc-base-installation.tex
%{_texmfdistdir}/doc/latex/tkz-base/TKZdoc-base-main.tex
%{_texmfdistdir}/doc/latex/tkz-base/TKZdoc-base-marks.tex
%{_texmfdistdir}/doc/latex/tkz-base/TKZdoc-base-news.tex
%{_texmfdistdir}/doc/latex/tkz-base/TKZdoc-base-obj.tex
%{_texmfdistdir}/doc/latex/tkz-base/TKZdoc-base-point.tex
%{_texmfdistdir}/doc/latex/tkz-base/TKZdoc-base-rep.tex
%{_texmfdistdir}/doc/latex/tkz-base/TKZdoc-base-style.tex
%{_texmfdistdir}/doc/latex/tkz-base/TKZdoc-base-texte.tex
%{_texmfdistdir}/doc/latex/tkz-base/TKZdoc-base.pdf
%{_texmfdistdir}/doc/latex/tkz-base/examples/preamble-standalone.ltx
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-10.1.1.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-10.2.1.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-10.3.1.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-10.4.0.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-10.5.1.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-10.6.1.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-10.6.2.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-10.6.3.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-10.7.1.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-10.9.0.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-12.1.2.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-13.1.1.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-13.1.2.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-13.2.1.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-13.3.1.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-13.3.2.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-13.4.1.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-14.1.1.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-15.1.1.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-15.2.1.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-15.2.2.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-15.3.1.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-15.4.1.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-15.5.1.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-16.1.1.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-16.1.2.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-16.1.3.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-16.1.4.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-16.2.1.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-3.1.0.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-4.1.0.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-4.2.0.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-5.1.1.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-5.1.2.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-5.2.0.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-5.2.1.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-5.2.2.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-5.2.3.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-6.1.0.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-6.1.1.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-6.1.2.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-6.1.3.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-6.1.4.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-6.1.5.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-6.1.6.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-6.10.1.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-6.2.1.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-6.2.10.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-6.2.11.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-6.2.2.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-6.2.3.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-6.2.4.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-6.2.5.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-6.2.6.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-6.2.7.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-6.2.8.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-6.2.9.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-6.3.1.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-6.3.2.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-6.3.3.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-6.7.1.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-6.7.2.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-6.7.3.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-6.8.1.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-6.8.2.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-6.9.1.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-7.0.1.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-7.0.10.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-7.0.11.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-7.0.2.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-7.0.3.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-7.0.4.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-7.0.5.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-7.0.6.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-7.0.7.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-7.0.8.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-7.0.9.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-8.1.1.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-8.10.1.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-8.10.2.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-8.11.1.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-8.11.2.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-8.11.3.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-8.12.2.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-8.12.3.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-8.13.1.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-8.2.0.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-8.2.1.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-8.2.2.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-8.2.3.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-8.3.1.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-8.4.1.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-8.5.1.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-8.5.2.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-8.6.1.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-8.6.2.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-8.6.3.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-8.7.1.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-8.7.2.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-8.8.1.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-8.8.2.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-8.9.1.tex
%{_texmfdistdir}/doc/latex/tkz-base/examples/tkzBase-9.2.0.tex
%{_texmfdistdir}/doc/latex/tkz-base/tiger.pdf

%files -n texlive-tkz-base
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/tkz-base/tkz-base.cfg
%{_texmfdistdir}/tex/latex/tkz-base/tkz-base.sty
%{_texmfdistdir}/tex/latex/tkz-base/tkz-lib-marks.tex
%{_texmfdistdir}/tex/latex/tkz-base/tkz-obj-axes.tex
%{_texmfdistdir}/tex/latex/tkz-base/tkz-obj-grids.tex
%{_texmfdistdir}/tex/latex/tkz-base/tkz-obj-marks.tex
%{_texmfdistdir}/tex/latex/tkz-base/tkz-obj-points.tex
%{_texmfdistdir}/tex/latex/tkz-base/tkz-obj-rep.tex
%{_texmfdistdir}/tex/latex/tkz-base/tkz-tools-BB.tex
%{_texmfdistdir}/tex/latex/tkz-base/tkz-tools-arith.tex
%{_texmfdistdir}/tex/latex/tkz-base/tkz-tools-base.tex
%{_texmfdistdir}/tex/latex/tkz-base/tkz-tools-misc.tex
%{_texmfdistdir}/tex/latex/tkz-base/tkz-tools-modules.tex
%{_texmfdistdir}/tex/latex/tkz-base/tkz-tools-print.tex
%{_texmfdistdir}/tex/latex/tkz-base/tkz-tools-text.tex
%{_texmfdistdir}/tex/latex/tkz-base/tkz-tools-utilities.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-tkz-base-%{texlive_version}.%{texlive_noarch}.3.06csvn54758-%{release}-zypper
%endif

%package -n texlive-tkz-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.43csvn54758
Release:        0
Summary:        Documentation macros for the TKZ series of packages
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source98:       tkz-doc.doc.tar.xz

%description -n texlive-tkz-doc
This bundle offers a documentation class (tkz-doc) and a
package (tkzexample). These files are used in the documentation
of the author's packages tkz-base, tkz-euclide, tkz-fct,
tkz-linknodes, and tkz-tab.
%post -n texlive-tkz-doc
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tkz-doc 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tkz-doc
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tkz-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/tkz-doc/README.md
%{_texmfdistdir}/doc/latex/tkz-doc/latex/couverture.tex
%{_texmfdistdir}/doc/latex/tkz-doc/latex/tkz-doc.cfg
%{_texmfdistdir}/doc/latex/tkz-doc/latex/tkz-doc.cls
%{_texmfdistdir}/doc/latex/tkz-doc/latex/tkzexample.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-tkz-doc-%{texlive_version}.%{texlive_noarch}.1.43csvn54758-%{release}-zypper
%endif

%package -n texlive-tkz-euclide
Version:        %{texlive_version}.%{texlive_noarch}.3.06csvn54758
Release:        0
Summary:        Tools for drawing Euclidean geometry
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-tkz-euclide-doc >= %{texlive_version}
Provides:       tex(tkz-euclide.sty)
Provides:       tex(tkz-obj-eu-angles.tex)
Provides:       tex(tkz-obj-eu-arcs.tex)
Provides:       tex(tkz-obj-eu-circles.tex)
Provides:       tex(tkz-obj-eu-compass.tex)
Provides:       tex(tkz-obj-eu-draw-circles.tex)
Provides:       tex(tkz-obj-eu-draw-lines.tex)
Provides:       tex(tkz-obj-eu-draw-polygons.tex)
Provides:       tex(tkz-obj-eu-draw-triangles.tex)
Provides:       tex(tkz-obj-eu-lines.tex)
Provides:       tex(tkz-obj-eu-points-by.tex)
Provides:       tex(tkz-obj-eu-points-rnd.tex)
Provides:       tex(tkz-obj-eu-points-with.tex)
Provides:       tex(tkz-obj-eu-points.tex)
Provides:       tex(tkz-obj-eu-polygons.tex)
Provides:       tex(tkz-obj-eu-protractor.tex)
Provides:       tex(tkz-obj-eu-sectors.tex)
Provides:       tex(tkz-obj-eu-show.tex)
Provides:       tex(tkz-obj-eu-triangles.tex)
Provides:       tex(tkz-tools-angles.tex)
Provides:       tex(tkz-tools-intersections.tex)
Provides:       tex(tkz-tools-math.tex)
Requires:       tex(tkz-base.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source99:       tkz-euclide.tar.xz
Source100:      tkz-euclide.doc.tar.xz

%description -n texlive-tkz-euclide
The tkz-euclide package is a set of files designed to give math
teachers and students easy access to the programming of
Euclidean geometry with TikZ.

%package -n texlive-tkz-euclide-doc
Version:        %{texlive_version}.%{texlive_noarch}.3.06csvn54758
Release:        0
Summary:        Documentation for texlive-tkz-euclide
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-tkz-euclide-doc:en)

%description -n texlive-tkz-euclide-doc
This package includes the documentation for texlive-tkz-euclide

%post -n texlive-tkz-euclide
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tkz-euclide 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tkz-euclide
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tkz-euclide-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/tkz-euclide/Euclidean_geometry.pdf
%{_texmfdistdir}/doc/latex/tkz-euclide/README.md
%{_texmfdistdir}/doc/latex/tkz-euclide/TKZdoc-euclide-FAQ.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/TKZdoc-euclide-angles.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/TKZdoc-euclide-arcs.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/TKZdoc-euclide-base.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/TKZdoc-euclide-circles.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/TKZdoc-euclide-compass.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/TKZdoc-euclide-config.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/TKZdoc-euclide-exemples.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/TKZdoc-euclide-installation.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/TKZdoc-euclide-intersec.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/TKZdoc-euclide-lines.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/TKZdoc-euclide-main.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/TKZdoc-euclide-news.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/TKZdoc-euclide-pointby.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/TKZdoc-euclide-points.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/TKZdoc-euclide-pointsSpc.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/TKZdoc-euclide-pointwith.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/TKZdoc-euclide-polygons.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/TKZdoc-euclide-presentation.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/TKZdoc-euclide-rapporteur.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/TKZdoc-euclide-rnd.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/TKZdoc-euclide-sectors.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/TKZdoc-euclide-show.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/TKZdoc-euclide-tools.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/TKZdoc-euclide-triangles.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/TKZdoc-euclide.pdf
%{_texmfdistdir}/doc/latex/tkz-euclide/cheatsheet_euclide_1.pdf
%{_texmfdistdir}/doc/latex/tkz-euclide/cheatsheet_euclide_2.pdf
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/preamble-standalone.ltx
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-1.0.0.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-1.3.1.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-1.3.2.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-1.3.3.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-1.4.0.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-1.5.0.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-1.6.1.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-10.1.1.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-10.1.10.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-10.1.11.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-10.1.2.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-10.1.3.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-10.1.4.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-10.1.5.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-10.1.6.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-10.1.7.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-10.1.8.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-10.1.9.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-10.2.1.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-11.2.0.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-11.3.0.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-11.4.0.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-11.4.1.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-11.5.0.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-11.5.1.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-11.6.0.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-12.1.1.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-12.1.2.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-12.1.3.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-12.1.4.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-12.1.5.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-12.2.1.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-12.2.2.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-12.2.3.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-12.2.4.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-12.2.5.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-13.1.1.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-13.1.2.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-13.1.3.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-13.1.4.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-13.1.5.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-13.1.6.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-13.2.1.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-14.1.1.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-14.1.2.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-14.1.3.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-14.2.0.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-14.2.1.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-14.3.1.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-14.3.2.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-14.4.1.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-14.5.0.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-14.5.1.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-14.5.2.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-14.5.3.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-15.1.1.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-15.1.2.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-15.1.3.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-15.2.1.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-15.2.2.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-15.2.3.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-15.2.4.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-15.2.5.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-16.0.1.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-16.0.2.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-16.0.3.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-16.0.4.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-16.0.5.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-16.0.6.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-16.0.7.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-16.0.8.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-17.1.1.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-17.1.2.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-17.1.3.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-17.10.1.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-17.10.2.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-17.3.1.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-17.3.2.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-17.3.3.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-17.4.1.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-17.5.1.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-17.6.1.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-17.7.1.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-17.7.2.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-17.8.1.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-17.8.2.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-17.9.1.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-18.1.1.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-18.1.10.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-18.1.2.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-18.1.3.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-18.1.4.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-18.1.5.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-18.1.6.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-18.1.7.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-18.1.8.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-18.1.9.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-19.1.1.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-19.2.1.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-19.2.2.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-19.2.3.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-19.2.4.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-19.3.1.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-19.4.1.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-19.5.1.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-19.6.1.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-20.1.1.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-20.2.1.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-20.2.2.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-20.2.3.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-20.2.4.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-20.2.6.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-20.2.7.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-20.2.8.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-20.2.9.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-20.3.1.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-20.3.2.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-20.3.3.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-20.3.4.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-20.3.5.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-21.1.1.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-21.1.2.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-21.1.3.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-21.2.1.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-21.2.2.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-21.3.1.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-21.4.1.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-21.4.2.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-21.4.3.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-21.4.4.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-22.2.0.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-22.3.1.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-22.4.0.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-22.4.1.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-22.5.0.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-22.6.1.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-22.6.2.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-23.1.1.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-23.1.2.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-23.1.3.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-23.1.4.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-23.1.5.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-23.2.1.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-23.2.2.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-23.3.1.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-24.1.0.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-24.2.0.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-24.3.0.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-24.4.0.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-24.5.0.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-24.6.0.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-24.7.0.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-24.8.0.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-25.1.0.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-25.1.1.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-25.2.1.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-25.4.1.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-25.5.1.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-25.5.2.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-26.1.1.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-26.1.2.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-26.2.0.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-26.3.1.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-27.1.1.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-27.1.2.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-27.1.3.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-27.1.4.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-27.2.1.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-27.2.2.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-28.1.1.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-29.1.0.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-29.2.0.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-30.1.2.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-30.1.3.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-30.1.4.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-30.1.5.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-30.2.1.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-30.2.10.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-30.2.11.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-30.2.12.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-30.2.2.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-30.2.3.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-30.2.4.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-30.2.5.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-30.2.6.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-30.2.7.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-30.2.8.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-30.2.9.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-31.1.1.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-31.1.2.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-31.1.3.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-31.2.1.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-31.2.2.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-31.3.1.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-31.3.2.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-31.4.0.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-32.2.0.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-32.3.0.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-32.4.0.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-4.0.0.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-4.1.1.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-4.1.2.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-4.1.3.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-4.1.4.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-4.1.5.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-4.2.1.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-4.2.2.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-4.2.3.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-4.4.0.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-4.5.0.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-5.1.1.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-5.2.1.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-5.2.2.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-5.3.0.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-6.1.1.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-6.1.2.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-6.1.3.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-6.1.4.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-6.1.5.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-6.1.6.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-6.1.7.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-6.1.8.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-6.1.9.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-7.0.2.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-7.0.3.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-7.0.4.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-8.1.1.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-8.2.0.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-9.2.0.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-9.2.1.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-9.2.2.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-9.2.3.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-9.2.4.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-9.2.5.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-9.2.6.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-9.2.7.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-9.2.8.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzEuclide-9.3.1.tex

%files -n texlive-tkz-euclide
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/tkz-euclide/tkz-euclide.sty
%{_texmfdistdir}/tex/latex/tkz-euclide/tkz-obj-eu-angles.tex
%{_texmfdistdir}/tex/latex/tkz-euclide/tkz-obj-eu-arcs.tex
%{_texmfdistdir}/tex/latex/tkz-euclide/tkz-obj-eu-circles.tex
%{_texmfdistdir}/tex/latex/tkz-euclide/tkz-obj-eu-compass.tex
%{_texmfdistdir}/tex/latex/tkz-euclide/tkz-obj-eu-draw-circles.tex
%{_texmfdistdir}/tex/latex/tkz-euclide/tkz-obj-eu-draw-lines.tex
%{_texmfdistdir}/tex/latex/tkz-euclide/tkz-obj-eu-draw-polygons.tex
%{_texmfdistdir}/tex/latex/tkz-euclide/tkz-obj-eu-draw-triangles.tex
%{_texmfdistdir}/tex/latex/tkz-euclide/tkz-obj-eu-lines.tex
%{_texmfdistdir}/tex/latex/tkz-euclide/tkz-obj-eu-points-by.tex
%{_texmfdistdir}/tex/latex/tkz-euclide/tkz-obj-eu-points-rnd.tex
%{_texmfdistdir}/tex/latex/tkz-euclide/tkz-obj-eu-points-with.tex
%{_texmfdistdir}/tex/latex/tkz-euclide/tkz-obj-eu-points.tex
%{_texmfdistdir}/tex/latex/tkz-euclide/tkz-obj-eu-polygons.tex
%{_texmfdistdir}/tex/latex/tkz-euclide/tkz-obj-eu-protractor.tex
%{_texmfdistdir}/tex/latex/tkz-euclide/tkz-obj-eu-sectors.tex
%{_texmfdistdir}/tex/latex/tkz-euclide/tkz-obj-eu-show.tex
%{_texmfdistdir}/tex/latex/tkz-euclide/tkz-obj-eu-triangles.tex
%{_texmfdistdir}/tex/latex/tkz-euclide/tkz-tools-angles.tex
%{_texmfdistdir}/tex/latex/tkz-euclide/tkz-tools-intersections.tex
%{_texmfdistdir}/tex/latex/tkz-euclide/tkz-tools-math.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-tkz-euclide-%{texlive_version}.%{texlive_noarch}.3.06csvn54758-%{release}-zypper
%endif

%package -n texlive-tkz-fct
Version:        %{texlive_version}.%{texlive_noarch}.1.3csvn54703
Release:        0
Summary:        Tools for drawing graphs of functions
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-tkz-fct-doc >= %{texlive_version}
Provides:       tex(tkz-fct.sty)
Requires:       tex(fp.sty)
Requires:       tex(tkz-base.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source101:      tkz-fct.tar.xz
Source102:      tkz-fct.doc.tar.xz

%description -n texlive-tkz-fct
The tkz-fct package is designed to give math teachers (and
students) easy access to programming graphs of functions with
TikZ and gnuplot.

%package -n texlive-tkz-fct-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.3csvn54703
Release:        0
Summary:        Documentation for texlive-tkz-fct
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-tkz-fct-doc:fr)

%description -n texlive-tkz-fct-doc
This package includes the documentation for texlive-tkz-fct

%post -n texlive-tkz-fct
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tkz-fct 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tkz-fct
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tkz-fct-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/tkz-fct/README.md
%{_texmfdistdir}/doc/latex/tkz-fct/TKZdoc-fct-VDW.tex
%{_texmfdistdir}/doc/latex/tkz-fct/TKZdoc-fct-area.tex
%{_texmfdistdir}/doc/latex/tkz-fct/TKZdoc-fct-asymptote.tex
%{_texmfdistdir}/doc/latex/tkz-fct/TKZdoc-fct-bac.tex
%{_texmfdistdir}/doc/latex/tkz-fct/TKZdoc-fct-compilation.tex
%{_texmfdistdir}/doc/latex/tkz-fct/TKZdoc-fct-example.tex
%{_texmfdistdir}/doc/latex/tkz-fct/TKZdoc-fct-faq.tex
%{_texmfdistdir}/doc/latex/tkz-fct/TKZdoc-fct-fonctions.tex
%{_texmfdistdir}/doc/latex/tkz-fct/TKZdoc-fct-fppgf.tex
%{_texmfdistdir}/doc/latex/tkz-fct/TKZdoc-fct-interpolation.tex
%{_texmfdistdir}/doc/latex/tkz-fct/TKZdoc-fct-label.tex
%{_texmfdistdir}/doc/latex/tkz-fct/TKZdoc-fct-liste.tex
%{_texmfdistdir}/doc/latex/tkz-fct/TKZdoc-fct-main.tex
%{_texmfdistdir}/doc/latex/tkz-fct/TKZdoc-fct-param.tex
%{_texmfdistdir}/doc/latex/tkz-fct/TKZdoc-fct-point.tex
%{_texmfdistdir}/doc/latex/tkz-fct/TKZdoc-fct-polar.tex
%{_texmfdistdir}/doc/latex/tkz-fct/TKZdoc-fct-riemann.tex
%{_texmfdistdir}/doc/latex/tkz-fct/TKZdoc-fct-symbol.tex
%{_texmfdistdir}/doc/latex/tkz-fct/TKZdoc-fct-tangent.tex
%{_texmfdistdir}/doc/latex/tkz-fct/TKZdoc-fct-why.tex
%{_texmfdistdir}/doc/latex/tkz-fct/TKZdoc-fct.pdf

%files -n texlive-tkz-fct
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/tkz-fct/tkz-fct.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-tkz-fct-%{texlive_version}.%{texlive_noarch}.1.3csvn54703-%{release}-zypper
%endif

%package -n texlive-tkz-orm
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1.4svn54512
Release:        0
Summary:        Create Object-Role Model (ORM) diagrams
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-tkz-orm-doc >= %{texlive_version}
Provides:       tex(tkz-orm.sty)
Requires:       tex(tikz.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source103:      tkz-orm.tar.xz
Source104:      tkz-orm.doc.tar.xz

%description -n texlive-tkz-orm
The package provides styles for drawing Object-Role Model (ORM)
diagrams in TeX based on the PGF and TikZ picture environment.

%package -n texlive-tkz-orm-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1.4svn54512
Release:        0
Summary:        Documentation for texlive-tkz-orm
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-tkz-orm-doc
This package includes the documentation for texlive-tkz-orm

%post -n texlive-tkz-orm
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tkz-orm 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tkz-orm
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tkz-orm-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/tkz-orm/LICENSE
%{_texmfdistdir}/doc/latex/tkz-orm/Makefile
%{_texmfdistdir}/doc/latex/tkz-orm/README
%{_texmfdistdir}/doc/latex/tkz-orm/pgfmanualstyle.sty
%{_texmfdistdir}/doc/latex/tkz-orm/tkz-orm.bib
%{_texmfdistdir}/doc/latex/tkz-orm/tkz-orm.pdf
%{_texmfdistdir}/doc/latex/tkz-orm/tkz-orm.tex

%files -n texlive-tkz-orm
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/tkz-orm/tkz-orm.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-tkz-orm-%{texlive_version}.%{texlive_noarch}.0.0.1.4svn54512-%{release}-zypper
%endif

%package -n texlive-tkz-tab
Version:        %{texlive_version}.%{texlive_noarch}.2.1csvn54662
Release:        0
Summary:        Tables of signs and variations using PGF/TikZ
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-tkz-tab-doc >= %{texlive_version}
Provides:       tex(tkz-tab.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source105:      tkz-tab.tar.xz
Source106:      tkz-tab.doc.tar.xz

%description -n texlive-tkz-tab
The package provides comprehensive facilities for preparing
lists of signs and variations, using PGF. The package
documentation requires the tkz-doc bundle. This package has
been taken temporarily out of circulation to give the author
time to investigate some problems.

%package -n texlive-tkz-tab-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.1csvn54662
Release:        0
Summary:        Documentation for texlive-tkz-tab
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-tkz-tab-doc:fr)

%description -n texlive-tkz-tab-doc
This package includes the documentation for texlive-tkz-tab

%post -n texlive-tkz-tab
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tkz-tab 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tkz-tab
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tkz-tab-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/tkz-tab/README.md
%{_texmfdistdir}/doc/latex/tkz-tab/TKZdoc-tab-adapt.tex
%{_texmfdistdir}/doc/latex/tkz-tab/TKZdoc-tab-bac.tex
%{_texmfdistdir}/doc/latex/tkz-tab/TKZdoc-tab-examples.tex
%{_texmfdistdir}/doc/latex/tkz-tab/TKZdoc-tab-image.tex
%{_texmfdistdir}/doc/latex/tkz-tab/TKZdoc-tab-init.tex
%{_texmfdistdir}/doc/latex/tkz-tab/TKZdoc-tab-main.tex
%{_texmfdistdir}/doc/latex/tkz-tab/TKZdoc-tab-sign.tex
%{_texmfdistdir}/doc/latex/tkz-tab/TKZdoc-tab-slope.tex
%{_texmfdistdir}/doc/latex/tkz-tab/TKZdoc-tab-style.tex
%{_texmfdistdir}/doc/latex/tkz-tab/TKZdoc-tab-tangente.tex
%{_texmfdistdir}/doc/latex/tkz-tab/TKZdoc-tab-tv.tex
%{_texmfdistdir}/doc/latex/tkz-tab/TKZdoc-tab-valeurs.tex
%{_texmfdistdir}/doc/latex/tkz-tab/TKZdoc-tab-variation.tex
%{_texmfdistdir}/doc/latex/tkz-tab/TKZdoc-tab.pdf

%files -n texlive-tkz-tab
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/tkz-tab/tkz-tab.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-tkz-tab-%{texlive_version}.%{texlive_noarch}.2.1csvn54662-%{release}-zypper
%endif

%package -n texlive-tlc-article
Version:        %{texlive_version}.%{texlive_noarch}.1.0.17svn51431
Release:        0
Summary:        A LaTeX document class for formal documents
License:        BSD-3-Clause
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-tlc-article-doc >= %{texlive_version}
Provides:       tex(tlc-article.cls)
Requires:       tex(appendix.sty)
Requires:       tex(array.sty)
Requires:       tex(article.cls)
Requires:       tex(bookmark.sty)
Requires:       tex(csvsimple.sty)
Requires:       tex(enumitem.sty)
Requires:       tex(fancyhdr.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(geometry.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(inputenc.sty)
Requires:       tex(lastpage.sty)
Requires:       tex(listings.sty)
Requires:       tex(lmodern.sty)
Requires:       tex(longtable.sty)
Requires:       tex(makecell.sty)
Requires:       tex(multicol.sty)
Requires:       tex(pdflscape.sty)
Requires:       tex(pdfpages.sty)
Requires:       tex(spverbatim.sty)
Requires:       tex(tabularx.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(titling.sty)
Requires:       tex(tocloft.sty)
Requires:       tex(todonotes.sty)
Requires:       tex(xcolor.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source107:      tlc-article.tar.xz
Source108:      tlc-article.doc.tar.xz

%description -n texlive-tlc-article
The package provides a LaTeX document class that orchestrates a
logical arrangement for document header, footer, author,
abstract, table of contents, and margins. It standardizes a
document layout intended for formal documents. The tlc_article
GitHub repository uses a SCRUM framework adapted to standard
GitHub tooling. tlc_article is integrated with Travis-ci.org
for continuous integration and AllanConsulting.slack.com for
centralized notification.

%package -n texlive-tlc-article-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0.17svn51431
Release:        0
Summary:        Documentation for texlive-tlc-article
License:        BSD-3-Clause
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-tlc-article-doc
This package includes the documentation for texlive-tlc-article

%post -n texlive-tlc-article
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tlc-article 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tlc-article
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tlc-article-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/tlc-article/LICENSE
%{_texmfdistdir}/doc/latex/tlc-article/README.md
%{_texmfdistdir}/doc/latex/tlc-article/bin/deploy
%{_texmfdistdir}/doc/latex/tlc-article/data/additional-layout.tex
%{_texmfdistdir}/doc/latex/tlc-article/data/logo.png
%{_texmfdistdir}/doc/latex/tlc-article/data/required-packages.csv
%{_texmfdistdir}/doc/latex/tlc-article/data/version.csv
%{_texmfdistdir}/doc/latex/tlc-article/doc/tlc-article.pdf
%{_texmfdistdir}/doc/latex/tlc-article/images/titlepage.png
%{_texmfdistdir}/doc/latex/tlc-article/tlc-article.tex
%{_texmfdistdir}/doc/latex/tlc-article/tlc-article.texx

%files -n texlive-tlc-article
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/tlc-article/tlc-article.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-tlc-article-%{texlive_version}.%{texlive_noarch}.1.0.17svn51431-%{release}-zypper
%endif

%package -n texlive-tlc2
Version:        %{texlive_version}.%{texlive_noarch}.svn26096
Release:        0
Summary:        Examples from "The LaTeX Companion", second edition
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source109:      tlc2.doc.tar.xz

%description -n texlive-tlc2
The source of the examples printed in the book, together with
necessary supporting files. The book was published by
Addison-Wesley, 2004, ISBN 0-201-36299-6.
%post -n texlive-tlc2
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tlc2 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tlc2
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tlc2
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/tlc2/1-3-1.ltx
%{_texmfdistdir}/doc/latex/tlc2/1-3-2.ltx2
%{_texmfdistdir}/doc/latex/tlc2/1-3-3.ltx
%{_texmfdistdir}/doc/latex/tlc2/1-3-4.ltx
%{_texmfdistdir}/doc/latex/tlc2/1-3-5.ltx
%{_texmfdistdir}/doc/latex/tlc2/10-1-1.ltx
%{_texmfdistdir}/doc/latex/tlc2/10-1-10.ltx
%{_texmfdistdir}/doc/latex/tlc2/10-1-11.ltx
%{_texmfdistdir}/doc/latex/tlc2/10-1-12.ltx
%{_texmfdistdir}/doc/latex/tlc2/10-1-13.ltx
%{_texmfdistdir}/doc/latex/tlc2/10-1-14.ltx
%{_texmfdistdir}/doc/latex/tlc2/10-1-15.ltx
%{_texmfdistdir}/doc/latex/tlc2/10-1-16.ltx
%{_texmfdistdir}/doc/latex/tlc2/10-1-17.ltx
%{_texmfdistdir}/doc/latex/tlc2/10-1-18.ltx
%{_texmfdistdir}/doc/latex/tlc2/10-1-19.ltx
%{_texmfdistdir}/doc/latex/tlc2/10-1-2.ltx
%{_texmfdistdir}/doc/latex/tlc2/10-1-20.ltx
%{_texmfdistdir}/doc/latex/tlc2/10-1-21.ltx
%{_texmfdistdir}/doc/latex/tlc2/10-1-22.ltx
%{_texmfdistdir}/doc/latex/tlc2/10-1-23.ltx
%{_texmfdistdir}/doc/latex/tlc2/10-1-24.ltx
%{_texmfdistdir}/doc/latex/tlc2/10-1-25.ltx
%{_texmfdistdir}/doc/latex/tlc2/10-1-26.ltx
%{_texmfdistdir}/doc/latex/tlc2/10-1-27.ltx
%{_texmfdistdir}/doc/latex/tlc2/10-1-3.ltx
%{_texmfdistdir}/doc/latex/tlc2/10-1-4.ltx
%{_texmfdistdir}/doc/latex/tlc2/10-1-5.ltx
%{_texmfdistdir}/doc/latex/tlc2/10-1-6.ltx
%{_texmfdistdir}/doc/latex/tlc2/10-1-7.ltx
%{_texmfdistdir}/doc/latex/tlc2/10-1-8.ltx
%{_texmfdistdir}/doc/latex/tlc2/10-1-9.ltx2
%{_texmfdistdir}/doc/latex/tlc2/10-2-1.ltx
%{_texmfdistdir}/doc/latex/tlc2/10-2-10.ltx
%{_texmfdistdir}/doc/latex/tlc2/10-2-11.ltx
%{_texmfdistdir}/doc/latex/tlc2/10-2-12.ltx
%{_texmfdistdir}/doc/latex/tlc2/10-2-13.ltx
%{_texmfdistdir}/doc/latex/tlc2/10-2-14.ltx
%{_texmfdistdir}/doc/latex/tlc2/10-2-15.ltx
%{_texmfdistdir}/doc/latex/tlc2/10-2-2.ltx
%{_texmfdistdir}/doc/latex/tlc2/10-2-3.ltx
%{_texmfdistdir}/doc/latex/tlc2/10-2-4.ltx
%{_texmfdistdir}/doc/latex/tlc2/10-2-5.ltx
%{_texmfdistdir}/doc/latex/tlc2/10-2-6.ltx
%{_texmfdistdir}/doc/latex/tlc2/10-2-7.ltx
%{_texmfdistdir}/doc/latex/tlc2/10-2-8.ltx
%{_texmfdistdir}/doc/latex/tlc2/10-2-9.ltx
%{_texmfdistdir}/doc/latex/tlc2/10-3-1.ltx
%{_texmfdistdir}/doc/latex/tlc2/10-3-10.ltx
%{_texmfdistdir}/doc/latex/tlc2/10-3-11.ltx
%{_texmfdistdir}/doc/latex/tlc2/10-3-12.ltx
%{_texmfdistdir}/doc/latex/tlc2/10-3-2.ltx
%{_texmfdistdir}/doc/latex/tlc2/10-3-3.ltx
%{_texmfdistdir}/doc/latex/tlc2/10-3-4.ltx
%{_texmfdistdir}/doc/latex/tlc2/10-3-5.ltx
%{_texmfdistdir}/doc/latex/tlc2/10-3-6.ltx
%{_texmfdistdir}/doc/latex/tlc2/10-3-7.ltx
%{_texmfdistdir}/doc/latex/tlc2/10-3-8.ltx
%{_texmfdistdir}/doc/latex/tlc2/10-3-9.ltx
%{_texmfdistdir}/doc/latex/tlc2/10-4-1.ltx
%{_texmfdistdir}/doc/latex/tlc2/10-4-2.ltx
%{_texmfdistdir}/doc/latex/tlc2/10-4-3.ltx
%{_texmfdistdir}/doc/latex/tlc2/10-4-4.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-1-1.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-1-2.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-1-3.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-2-1.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-2-10.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-2-11.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-2-12.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-2-13.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-2-14.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-2-2.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-2-3.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-2-4.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-2-5.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-2-6.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-2-7.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-2-8.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-2-9.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-3-1.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-3-10.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-3-11.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-3-12.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-3-13.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-3-14.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-3-15.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-3-16.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-3-17.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-3-18.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-3-19.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-3-2.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-3-20.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-3-21.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-3-22.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-3-23.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-3-24.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-3-25.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-3-26.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-3-27.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-3-3.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-3-4.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-3-5.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-3-6.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-3-7.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-3-8.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-3-9.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-4-1.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-4-2.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-4-3.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-4-4.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-4-5.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-4-6.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-4-7.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-4-8.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-5-1.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-5-10.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-5-11.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-5-12.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-5-13.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-5-14.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-5-15.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-5-16.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-5-17.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-5-18.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-5-19.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-5-2.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-5-20.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-5-21.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-5-22.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-5-23.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-5-24.ltx2
%{_texmfdistdir}/doc/latex/tlc2/12-5-25.ltx2
%{_texmfdistdir}/doc/latex/tlc2/12-5-26.ltx2
%{_texmfdistdir}/doc/latex/tlc2/12-5-27.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-5-28.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-5-29.ltx2
%{_texmfdistdir}/doc/latex/tlc2/12-5-3.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-5-30.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-5-31.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-5-32.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-5-33.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-5-34.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-5-35.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-5-36.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-5-37.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-5-38.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-5-39.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-5-4.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-5-40.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-5-41.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-5-42.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-5-43.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-5-44.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-5-45.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-5-46.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-5-47.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-5-48.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-5-49.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-5-5.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-5-6.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-5-7.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-5-8.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-5-9.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-6-1.ltx2
%{_texmfdistdir}/doc/latex/tlc2/12-6-10.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-6-2.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-6-3.ltx2
%{_texmfdistdir}/doc/latex/tlc2/12-6-4.ltx2
%{_texmfdistdir}/doc/latex/tlc2/12-6-5.ltx2
%{_texmfdistdir}/doc/latex/tlc2/12-6-6.ltx2
%{_texmfdistdir}/doc/latex/tlc2/12-6-7.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-6-8.ltx
%{_texmfdistdir}/doc/latex/tlc2/12-6-9.ltx
%{_texmfdistdir}/doc/latex/tlc2/13-4-1.ltx
%{_texmfdistdir}/doc/latex/tlc2/13-4-2.ltx
%{_texmfdistdir}/doc/latex/tlc2/13-5-1.ltx
%{_texmfdistdir}/doc/latex/tlc2/13-5-2.ltx
%{_texmfdistdir}/doc/latex/tlc2/13-5-3.ltx
%{_texmfdistdir}/doc/latex/tlc2/13-5-4.ltx
%{_texmfdistdir}/doc/latex/tlc2/13-5-5.ltx
%{_texmfdistdir}/doc/latex/tlc2/13-5-6.ltx
%{_texmfdistdir}/doc/latex/tlc2/13-5-7.ltx
%{_texmfdistdir}/doc/latex/tlc2/14-4-1.ltx
%{_texmfdistdir}/doc/latex/tlc2/14-4-2.ltx
%{_texmfdistdir}/doc/latex/tlc2/2-1-1.ltx
%{_texmfdistdir}/doc/latex/tlc2/2-2-1.ltx
%{_texmfdistdir}/doc/latex/tlc2/2-2-10.ltx
%{_texmfdistdir}/doc/latex/tlc2/2-2-11.ltx
%{_texmfdistdir}/doc/latex/tlc2/2-2-12.ltx
%{_texmfdistdir}/doc/latex/tlc2/2-2-13.ltx
%{_texmfdistdir}/doc/latex/tlc2/2-2-14.ltx
%{_texmfdistdir}/doc/latex/tlc2/2-2-15.ltx
%{_texmfdistdir}/doc/latex/tlc2/2-2-16.ltx
%{_texmfdistdir}/doc/latex/tlc2/2-2-17.ltx
%{_texmfdistdir}/doc/latex/tlc2/2-2-18.ltx
%{_texmfdistdir}/doc/latex/tlc2/2-2-19.ltx
%{_texmfdistdir}/doc/latex/tlc2/2-2-2.ltx
%{_texmfdistdir}/doc/latex/tlc2/2-2-20.ltx
%{_texmfdistdir}/doc/latex/tlc2/2-2-21.ltx2
%{_texmfdistdir}/doc/latex/tlc2/2-2-22.ltx
%{_texmfdistdir}/doc/latex/tlc2/2-2-3.ltx
%{_texmfdistdir}/doc/latex/tlc2/2-2-4.ltx
%{_texmfdistdir}/doc/latex/tlc2/2-2-5.ltx
%{_texmfdistdir}/doc/latex/tlc2/2-2-6.ltx
%{_texmfdistdir}/doc/latex/tlc2/2-2-7.ltx
%{_texmfdistdir}/doc/latex/tlc2/2-2-8.ltx
%{_texmfdistdir}/doc/latex/tlc2/2-2-9.ltx
%{_texmfdistdir}/doc/latex/tlc2/2-3-1.ltx2
%{_texmfdistdir}/doc/latex/tlc2/2-3-10.ltx
%{_texmfdistdir}/doc/latex/tlc2/2-3-11.ltx
%{_texmfdistdir}/doc/latex/tlc2/2-3-12.ltx
%{_texmfdistdir}/doc/latex/tlc2/2-3-13.ltx
%{_texmfdistdir}/doc/latex/tlc2/2-3-14.ltx
%{_texmfdistdir}/doc/latex/tlc2/2-3-2.ltx
%{_texmfdistdir}/doc/latex/tlc2/2-3-3.ltx
%{_texmfdistdir}/doc/latex/tlc2/2-3-4.ltx
%{_texmfdistdir}/doc/latex/tlc2/2-3-5.ltx
%{_texmfdistdir}/doc/latex/tlc2/2-3-6.ltx
%{_texmfdistdir}/doc/latex/tlc2/2-3-7.ltx
%{_texmfdistdir}/doc/latex/tlc2/2-3-8.ltx2
%{_texmfdistdir}/doc/latex/tlc2/2-3-9.ltx
%{_texmfdistdir}/doc/latex/tlc2/2-4-1.ltx
%{_texmfdistdir}/doc/latex/tlc2/2-4-2.ltx
%{_texmfdistdir}/doc/latex/tlc2/2-4-3.ltx
%{_texmfdistdir}/doc/latex/tlc2/2-4-4.ltx2
%{_texmfdistdir}/doc/latex/tlc2/2-4-5.ltx
%{_texmfdistdir}/doc/latex/tlc2/2-4-6.ltx2
%{_texmfdistdir}/doc/latex/tlc2/2-4-7.ltx
%{_texmfdistdir}/doc/latex/tlc2/2-4-8.ltx
%{_texmfdistdir}/doc/latex/tlc2/2-4-9.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-1-1.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-1-10.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-1-11.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-1-12.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-1-13.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-1-14.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-1-15.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-1-16.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-1-17.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-1-18.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-1-19.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-1-2.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-1-20.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-1-21.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-1-22.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-1-23.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-1-24.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-1-25.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-1-26.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-1-27.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-1-28.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-1-29.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-1-3.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-1-30.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-1-31.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-1-32.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-1-33.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-1-34.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-1-35.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-1-36.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-1-37.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-1-38.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-1-39.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-1-4.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-1-40.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-1-41.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-1-42.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-1-43.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-1-44.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-1-45.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-1-46.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-1-47.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-1-48.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-1-49.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-1-5.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-1-50.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-1-51.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-1-52.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-1-53.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-1-6.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-1-7.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-1-8.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-1-9.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-2-1.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-2-10.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-2-11.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-2-12.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-2-13.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-2-14.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-2-15.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-2-16.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-2-17.ltx2
%{_texmfdistdir}/doc/latex/tlc2/3-2-18.ltx2
%{_texmfdistdir}/doc/latex/tlc2/3-2-19.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-2-2.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-2-20.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-2-21.ltx2
%{_texmfdistdir}/doc/latex/tlc2/3-2-22.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-2-23.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-2-24.ltx2
%{_texmfdistdir}/doc/latex/tlc2/3-2-25.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-2-26.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-2-27.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-2-28.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-2-3.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-2-4.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-2-5.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-2-6.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-2-7.ltx2
%{_texmfdistdir}/doc/latex/tlc2/3-2-8.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-2-9.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-3-1.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-3-10.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-3-11.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-3-12.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-3-13.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-3-14.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-3-15.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-3-16.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-3-17.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-3-18.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-3-19.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-3-2.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-3-20.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-3-21.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-3-22.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-3-23.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-3-24.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-3-25.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-3-26.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-3-27.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-3-28.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-3-29.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-3-3.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-3-30.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-3-4.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-3-5.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-3-6.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-3-7.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-3-8.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-3-9.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-4-1.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-4-10.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-4-11.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-4-12.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-4-13.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-4-14.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-4-15.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-4-16.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-4-17.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-4-18.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-4-19.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-4-2.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-4-20.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-4-21.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-4-22.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-4-23.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-4-24.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-4-25.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-4-26.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-4-27.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-4-28.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-4-29.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-4-3.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-4-30.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-4-31.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-4-32.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-4-33.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-4-34.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-4-35.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-4-36.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-4-37.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-4-38.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-4-39.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-4-4.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-4-40.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-4-41.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-4-42.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-4-5.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-4-6.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-4-7.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-4-8.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-4-9.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-5-1.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-5-10.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-5-11.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-5-12.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-5-13.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-5-14.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-5-15.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-5-16.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-5-17.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-5-18.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-5-19.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-5-2.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-5-20.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-5-3.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-5-4.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-5-5.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-5-6.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-5-7.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-5-8.ltx
%{_texmfdistdir}/doc/latex/tlc2/3-5-9.ltx
%{_texmfdistdir}/doc/latex/tlc2/4-1-1.ltx
%{_texmfdistdir}/doc/latex/tlc2/4-2-1.ltx
%{_texmfdistdir}/doc/latex/tlc2/4-2-10.ltx
%{_texmfdistdir}/doc/latex/tlc2/4-2-11.ltx
%{_texmfdistdir}/doc/latex/tlc2/4-2-12.ltx
%{_texmfdistdir}/doc/latex/tlc2/4-2-13.ltx
%{_texmfdistdir}/doc/latex/tlc2/4-2-2.ltx
%{_texmfdistdir}/doc/latex/tlc2/4-2-3.ltx
%{_texmfdistdir}/doc/latex/tlc2/4-2-4.ltx
%{_texmfdistdir}/doc/latex/tlc2/4-2-5.ltx
%{_texmfdistdir}/doc/latex/tlc2/4-2-6.ltx
%{_texmfdistdir}/doc/latex/tlc2/4-2-7.ltx
%{_texmfdistdir}/doc/latex/tlc2/4-2-8.ltx2
%{_texmfdistdir}/doc/latex/tlc2/4-2-9.ltx2
%{_texmfdistdir}/doc/latex/tlc2/4-3-1.ltx2
%{_texmfdistdir}/doc/latex/tlc2/4-3-2.ltx2
%{_texmfdistdir}/doc/latex/tlc2/4-3-3.ltx2
%{_texmfdistdir}/doc/latex/tlc2/4-4-1.ltx
%{_texmfdistdir}/doc/latex/tlc2/4-4-10.ltx2
%{_texmfdistdir}/doc/latex/tlc2/4-4-11.ltx2
%{_texmfdistdir}/doc/latex/tlc2/4-4-12.ltx2
%{_texmfdistdir}/doc/latex/tlc2/4-4-13.ltx2
%{_texmfdistdir}/doc/latex/tlc2/4-4-14.ltx
%{_texmfdistdir}/doc/latex/tlc2/4-4-15.ltx2
%{_texmfdistdir}/doc/latex/tlc2/4-4-2.ltx
%{_texmfdistdir}/doc/latex/tlc2/4-4-3.ltx
%{_texmfdistdir}/doc/latex/tlc2/4-4-4.ltx2
%{_texmfdistdir}/doc/latex/tlc2/4-4-5.ltx2
%{_texmfdistdir}/doc/latex/tlc2/4-4-6.ltx2
%{_texmfdistdir}/doc/latex/tlc2/4-4-7.ltx2
%{_texmfdistdir}/doc/latex/tlc2/4-4-8.ltx2
%{_texmfdistdir}/doc/latex/tlc2/4-4-9.ltx2
%{_texmfdistdir}/doc/latex/tlc2/4-5-1.ltx2
%{_texmfdistdir}/doc/latex/tlc2/4-5-2.ltx2
%{_texmfdistdir}/doc/latex/tlc2/5-1-1.ltx
%{_texmfdistdir}/doc/latex/tlc2/5-1-2.ltx
%{_texmfdistdir}/doc/latex/tlc2/5-1-3.ltx
%{_texmfdistdir}/doc/latex/tlc2/5-1-4.ltx
%{_texmfdistdir}/doc/latex/tlc2/5-2-1.ltx
%{_texmfdistdir}/doc/latex/tlc2/5-2-10.ltx
%{_texmfdistdir}/doc/latex/tlc2/5-2-11.ltx
%{_texmfdistdir}/doc/latex/tlc2/5-2-12.ltx
%{_texmfdistdir}/doc/latex/tlc2/5-2-13.ltx
%{_texmfdistdir}/doc/latex/tlc2/5-2-2.ltx
%{_texmfdistdir}/doc/latex/tlc2/5-2-3.ltx
%{_texmfdistdir}/doc/latex/tlc2/5-2-4.ltx
%{_texmfdistdir}/doc/latex/tlc2/5-2-5.ltx
%{_texmfdistdir}/doc/latex/tlc2/5-2-6.ltx
%{_texmfdistdir}/doc/latex/tlc2/5-2-7.ltx
%{_texmfdistdir}/doc/latex/tlc2/5-2-8.ltx
%{_texmfdistdir}/doc/latex/tlc2/5-2-9.ltx
%{_texmfdistdir}/doc/latex/tlc2/5-3-1.ltx
%{_texmfdistdir}/doc/latex/tlc2/5-3-2.ltx
%{_texmfdistdir}/doc/latex/tlc2/5-3-3.ltx
%{_texmfdistdir}/doc/latex/tlc2/5-3-4.ltx
%{_texmfdistdir}/doc/latex/tlc2/5-3-5.ltx
%{_texmfdistdir}/doc/latex/tlc2/5-3-6.ltx
%{_texmfdistdir}/doc/latex/tlc2/5-4-1.ltx2
%{_texmfdistdir}/doc/latex/tlc2/5-4-2.ltx2
%{_texmfdistdir}/doc/latex/tlc2/5-4-3.ltx2
%{_texmfdistdir}/doc/latex/tlc2/5-4-4.ltx
%{_texmfdistdir}/doc/latex/tlc2/5-4-5.ltx2
%{_texmfdistdir}/doc/latex/tlc2/5-4-6.ltx2
%{_texmfdistdir}/doc/latex/tlc2/5-5-1.ltx
%{_texmfdistdir}/doc/latex/tlc2/5-5-2.ltx
%{_texmfdistdir}/doc/latex/tlc2/5-6-1.ltx
%{_texmfdistdir}/doc/latex/tlc2/5-6-2.ltx
%{_texmfdistdir}/doc/latex/tlc2/5-6-3.ltx
%{_texmfdistdir}/doc/latex/tlc2/5-6-4.ltx
%{_texmfdistdir}/doc/latex/tlc2/5-6-5.ltx
%{_texmfdistdir}/doc/latex/tlc2/5-6-6.ltx
%{_texmfdistdir}/doc/latex/tlc2/5-6-7.ltx
%{_texmfdistdir}/doc/latex/tlc2/5-6-8.ltx
%{_texmfdistdir}/doc/latex/tlc2/5-7-1.ltx
%{_texmfdistdir}/doc/latex/tlc2/5-7-2.ltx
%{_texmfdistdir}/doc/latex/tlc2/5-7-3.ltx
%{_texmfdistdir}/doc/latex/tlc2/5-7-4.ltx
%{_texmfdistdir}/doc/latex/tlc2/5-7-5.ltx
%{_texmfdistdir}/doc/latex/tlc2/5-7-6.ltx
%{_texmfdistdir}/doc/latex/tlc2/5-7-7.ltx
%{_texmfdistdir}/doc/latex/tlc2/5-7-8.ltx
%{_texmfdistdir}/doc/latex/tlc2/5-8-1.ltx
%{_texmfdistdir}/doc/latex/tlc2/5-8-2.ltx
%{_texmfdistdir}/doc/latex/tlc2/5-9-1.ltx
%{_texmfdistdir}/doc/latex/tlc2/5-9-2.ltx
%{_texmfdistdir}/doc/latex/tlc2/5-9-3.ltx
%{_texmfdistdir}/doc/latex/tlc2/5-9-4.ltx
%{_texmfdistdir}/doc/latex/tlc2/5-9-5.ltx
%{_texmfdistdir}/doc/latex/tlc2/5-9-6.ltx
%{_texmfdistdir}/doc/latex/tlc2/6-3-1.ltx
%{_texmfdistdir}/doc/latex/tlc2/6-3-2.ltx
%{_texmfdistdir}/doc/latex/tlc2/6-3-3.ltx
%{_texmfdistdir}/doc/latex/tlc2/6-3-4.ltx2
%{_texmfdistdir}/doc/latex/tlc2/6-3-5.ltx
%{_texmfdistdir}/doc/latex/tlc2/6-3-6.ltx2
%{_texmfdistdir}/doc/latex/tlc2/6-3-7.ltx2
%{_texmfdistdir}/doc/latex/tlc2/6-4-1.ltx
%{_texmfdistdir}/doc/latex/tlc2/6-4-2.ltx
%{_texmfdistdir}/doc/latex/tlc2/6-4-3.ltx
%{_texmfdistdir}/doc/latex/tlc2/6-4-4.ltx
%{_texmfdistdir}/doc/latex/tlc2/6-4-5.ltx2
%{_texmfdistdir}/doc/latex/tlc2/6-4-6.ltx2
%{_texmfdistdir}/doc/latex/tlc2/6-4-7.ltx
%{_texmfdistdir}/doc/latex/tlc2/6-4-8.ltx
%{_texmfdistdir}/doc/latex/tlc2/6-5-1.ltx
%{_texmfdistdir}/doc/latex/tlc2/6-5-10.ltx
%{_texmfdistdir}/doc/latex/tlc2/6-5-11.ltx
%{_texmfdistdir}/doc/latex/tlc2/6-5-12.ltx
%{_texmfdistdir}/doc/latex/tlc2/6-5-13.ltx
%{_texmfdistdir}/doc/latex/tlc2/6-5-14.ltx2
%{_texmfdistdir}/doc/latex/tlc2/6-5-15.ltx
%{_texmfdistdir}/doc/latex/tlc2/6-5-16.ltx
%{_texmfdistdir}/doc/latex/tlc2/6-5-17.ltx
%{_texmfdistdir}/doc/latex/tlc2/6-5-18.ltx2
%{_texmfdistdir}/doc/latex/tlc2/6-5-2.ltx
%{_texmfdistdir}/doc/latex/tlc2/6-5-3.ltx
%{_texmfdistdir}/doc/latex/tlc2/6-5-4.ltx
%{_texmfdistdir}/doc/latex/tlc2/6-5-5.ltx
%{_texmfdistdir}/doc/latex/tlc2/6-5-6.ltx
%{_texmfdistdir}/doc/latex/tlc2/6-5-7.ltx2
%{_texmfdistdir}/doc/latex/tlc2/6-5-8.ltx
%{_texmfdistdir}/doc/latex/tlc2/6-5-9.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-10-1.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-12-1.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-3-1.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-3-2.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-3-3.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-3-4.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-3-5.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-3-6.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-3-7.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-3-8.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-4-1.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-4-2.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-4-3.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-4-4.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-4-5.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-5-1.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-5-10.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-5-11.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-5-12.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-5-13.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-5-14.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-5-15.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-5-16.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-5-17.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-5-2.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-5-3.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-5-4.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-5-5.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-5-6.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-5-7.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-5-8.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-5-9.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-6-1.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-6-10.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-6-11.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-6-12.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-6-2.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-6-3.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-6-4.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-6-5.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-6-6.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-6-7.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-6-8.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-6-9.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-7-1.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-7-10.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-7-11.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-7-12.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-7-13.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-7-14.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-7-15.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-7-16.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-7-17.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-7-18.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-7-19.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-7-2.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-7-20.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-7-21.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-7-22.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-7-23.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-7-24.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-7-25.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-7-26.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-7-27.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-7-28.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-7-29.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-7-3.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-7-4.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-7-5.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-7-6.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-7-7.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-7-8.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-7-9.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-8-1.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-8-10.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-8-11.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-8-12.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-8-13.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-8-14.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-8-15.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-8-16.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-8-17.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-8-18.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-8-19.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-8-2.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-8-20.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-8-21.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-8-22.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-8-3.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-8-4.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-8-5.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-8-6.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-8-7.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-8-8.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-8-9.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-9-1.ltx
%{_texmfdistdir}/doc/latex/tlc2/7-9-2.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-2-1.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-2-10.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-2-11.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-2-12.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-2-13.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-2-14.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-2-15.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-2-16.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-2-17.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-2-18.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-2-19.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-2-2.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-2-20.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-2-21.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-2-22.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-2-23.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-2-24.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-2-25.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-2-26.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-2-27.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-2-28.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-2-29.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-2-3.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-2-4.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-2-5.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-2-6.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-2-7.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-2-8.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-2-9.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-3-1.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-3-10.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-3-11.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-3-12.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-3-13.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-3-14.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-3-15.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-3-16.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-3-17.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-3-18.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-3-19.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-3-2.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-3-20.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-3-21.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-3-22.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-3-23.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-3-24.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-3-25.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-3-26.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-3-27.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-3-28.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-3-29.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-3-3.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-3-30.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-3-31.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-3-32.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-3-33.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-3-34.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-3-35.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-3-36.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-3-37.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-3-38.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-3-39.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-3-4.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-3-5.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-3-6.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-3-7.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-3-8.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-3-9.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-4-1.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-4-10.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-4-11.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-4-12.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-4-13.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-4-14.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-4-2.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-4-3.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-4-4.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-4-5.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-4-6.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-4-7.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-4-8.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-4-9.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-5-1.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-5-2.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-5-3.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-5-4.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-6-1.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-6-2.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-6-3.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-6-4.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-7-1.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-7-2.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-7-3.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-7-4.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-7-5.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-7-6.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-7-7.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-8-1.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-8-10.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-8-11.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-8-12.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-8-13.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-8-14.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-8-15.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-8-16.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-8-17.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-8-18.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-8-19.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-8-2.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-8-20.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-8-21.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-8-22.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-8-23.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-8-24.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-8-25.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-8-3.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-8-4.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-8-5.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-8-6.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-8-7.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-8-8.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-8-9.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-9-1.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-9-2.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-9-3.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-9-4.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-9-5.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-9-6.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-9-7.ltx
%{_texmfdistdir}/doc/latex/tlc2/8-9-8.ltx
%{_texmfdistdir}/doc/latex/tlc2/9-2-1.ltx
%{_texmfdistdir}/doc/latex/tlc2/9-2-2.ltx
%{_texmfdistdir}/doc/latex/tlc2/9-2-3.ltx
%{_texmfdistdir}/doc/latex/tlc2/9-2-4.ltx
%{_texmfdistdir}/doc/latex/tlc2/9-2-5.ltx
%{_texmfdistdir}/doc/latex/tlc2/9-2-6.ltx
%{_texmfdistdir}/doc/latex/tlc2/9-2-7.ltx
%{_texmfdistdir}/doc/latex/tlc2/9-2-8.ltx
%{_texmfdistdir}/doc/latex/tlc2/9-3-1.ltx
%{_texmfdistdir}/doc/latex/tlc2/9-3-10.ltx
%{_texmfdistdir}/doc/latex/tlc2/9-3-11.ltx
%{_texmfdistdir}/doc/latex/tlc2/9-3-12.ltx
%{_texmfdistdir}/doc/latex/tlc2/9-3-13.ltx
%{_texmfdistdir}/doc/latex/tlc2/9-3-14.ltx
%{_texmfdistdir}/doc/latex/tlc2/9-3-15.ltx
%{_texmfdistdir}/doc/latex/tlc2/9-3-16.ltx
%{_texmfdistdir}/doc/latex/tlc2/9-3-17.ltx
%{_texmfdistdir}/doc/latex/tlc2/9-3-18.ltx
%{_texmfdistdir}/doc/latex/tlc2/9-3-19.ltx
%{_texmfdistdir}/doc/latex/tlc2/9-3-2.ltx
%{_texmfdistdir}/doc/latex/tlc2/9-3-20.ltx
%{_texmfdistdir}/doc/latex/tlc2/9-3-21.ltx
%{_texmfdistdir}/doc/latex/tlc2/9-3-22.ltx
%{_texmfdistdir}/doc/latex/tlc2/9-3-23.ltx
%{_texmfdistdir}/doc/latex/tlc2/9-3-24.ltx
%{_texmfdistdir}/doc/latex/tlc2/9-3-25.ltx
%{_texmfdistdir}/doc/latex/tlc2/9-3-26.ltx
%{_texmfdistdir}/doc/latex/tlc2/9-3-27.ltx
%{_texmfdistdir}/doc/latex/tlc2/9-3-28.ltx
%{_texmfdistdir}/doc/latex/tlc2/9-3-29.ltx
%{_texmfdistdir}/doc/latex/tlc2/9-3-3.ltx
%{_texmfdistdir}/doc/latex/tlc2/9-3-30.ltx
%{_texmfdistdir}/doc/latex/tlc2/9-3-31.ltx
%{_texmfdistdir}/doc/latex/tlc2/9-3-32.ltx
%{_texmfdistdir}/doc/latex/tlc2/9-3-33.ltx
%{_texmfdistdir}/doc/latex/tlc2/9-3-34.ltx
%{_texmfdistdir}/doc/latex/tlc2/9-3-35.ltx
%{_texmfdistdir}/doc/latex/tlc2/9-3-36.ltx
%{_texmfdistdir}/doc/latex/tlc2/9-3-37.ltx
%{_texmfdistdir}/doc/latex/tlc2/9-3-38.ltx
%{_texmfdistdir}/doc/latex/tlc2/9-3-39.ltx
%{_texmfdistdir}/doc/latex/tlc2/9-3-4.ltx
%{_texmfdistdir}/doc/latex/tlc2/9-3-5.ltx
%{_texmfdistdir}/doc/latex/tlc2/9-3-6.ltx
%{_texmfdistdir}/doc/latex/tlc2/9-3-7.ltx
%{_texmfdistdir}/doc/latex/tlc2/9-3-8.ltx
%{_texmfdistdir}/doc/latex/tlc2/9-3-9.ltx
%{_texmfdistdir}/doc/latex/tlc2/9-4-1.ltx
%{_texmfdistdir}/doc/latex/tlc2/9-4-2.ltx
%{_texmfdistdir}/doc/latex/tlc2/9-4-3.ltx
%{_texmfdistdir}/doc/latex/tlc2/9-4-4.ltx
%{_texmfdistdir}/doc/latex/tlc2/9-4-5.ltx
%{_texmfdistdir}/doc/latex/tlc2/9-5-1.ltx
%{_texmfdistdir}/doc/latex/tlc2/A-1-1.ltx
%{_texmfdistdir}/doc/latex/tlc2/A-1-10.ltx
%{_texmfdistdir}/doc/latex/tlc2/A-1-11.ltx
%{_texmfdistdir}/doc/latex/tlc2/A-1-12.ltx
%{_texmfdistdir}/doc/latex/tlc2/A-1-13.ltx
%{_texmfdistdir}/doc/latex/tlc2/A-1-14.ltx
%{_texmfdistdir}/doc/latex/tlc2/A-1-15.ltx
%{_texmfdistdir}/doc/latex/tlc2/A-1-16.ltx
%{_texmfdistdir}/doc/latex/tlc2/A-1-17.ltx
%{_texmfdistdir}/doc/latex/tlc2/A-1-2.ltx
%{_texmfdistdir}/doc/latex/tlc2/A-1-3.ltx
%{_texmfdistdir}/doc/latex/tlc2/A-1-4.ltx
%{_texmfdistdir}/doc/latex/tlc2/A-1-5.ltx
%{_texmfdistdir}/doc/latex/tlc2/A-1-6.ltx
%{_texmfdistdir}/doc/latex/tlc2/A-1-7.ltx
%{_texmfdistdir}/doc/latex/tlc2/A-1-8.ltx
%{_texmfdistdir}/doc/latex/tlc2/A-1-9.ltx
%{_texmfdistdir}/doc/latex/tlc2/A-2-1.ltx
%{_texmfdistdir}/doc/latex/tlc2/A-2-10.ltx
%{_texmfdistdir}/doc/latex/tlc2/A-2-11.ltx
%{_texmfdistdir}/doc/latex/tlc2/A-2-12.ltx
%{_texmfdistdir}/doc/latex/tlc2/A-2-13.ltx
%{_texmfdistdir}/doc/latex/tlc2/A-2-14.ltx
%{_texmfdistdir}/doc/latex/tlc2/A-2-15.ltx
%{_texmfdistdir}/doc/latex/tlc2/A-2-16.ltx
%{_texmfdistdir}/doc/latex/tlc2/A-2-17.ltx
%{_texmfdistdir}/doc/latex/tlc2/A-2-18.ltx
%{_texmfdistdir}/doc/latex/tlc2/A-2-19.ltx
%{_texmfdistdir}/doc/latex/tlc2/A-2-2.ltx
%{_texmfdistdir}/doc/latex/tlc2/A-2-20.ltx
%{_texmfdistdir}/doc/latex/tlc2/A-2-21.ltx
%{_texmfdistdir}/doc/latex/tlc2/A-2-3.ltx
%{_texmfdistdir}/doc/latex/tlc2/A-2-4.ltx
%{_texmfdistdir}/doc/latex/tlc2/A-2-5.ltx
%{_texmfdistdir}/doc/latex/tlc2/A-2-6.ltx
%{_texmfdistdir}/doc/latex/tlc2/A-2-7.ltx
%{_texmfdistdir}/doc/latex/tlc2/A-2-8.ltx
%{_texmfdistdir}/doc/latex/tlc2/A-2-9.ltx
%{_texmfdistdir}/doc/latex/tlc2/A-3-1.ltx
%{_texmfdistdir}/doc/latex/tlc2/A-3-10.ltx
%{_texmfdistdir}/doc/latex/tlc2/A-3-11.ltx
%{_texmfdistdir}/doc/latex/tlc2/A-3-2.ltx
%{_texmfdistdir}/doc/latex/tlc2/A-3-3.ltx
%{_texmfdistdir}/doc/latex/tlc2/A-3-4.ltx
%{_texmfdistdir}/doc/latex/tlc2/A-3-5.ltx
%{_texmfdistdir}/doc/latex/tlc2/A-3-6.ltx
%{_texmfdistdir}/doc/latex/tlc2/A-3-7.ltx
%{_texmfdistdir}/doc/latex/tlc2/A-3-8.ltx
%{_texmfdistdir}/doc/latex/tlc2/A-3-9.ltx2
%{_texmfdistdir}/doc/latex/tlc2/B-3-1.ltx
%{_texmfdistdir}/doc/latex/tlc2/Escher.ps
%{_texmfdistdir}/doc/latex/tlc2/cat.ps
%{_texmfdistdir}/doc/latex/tlc2/elephant.ps
%{_texmfdistdir}/doc/latex/tlc2/indexexa.ltx
%{_texmfdistdir}/doc/latex/tlc2/jura.bib
%{_texmfdistdir}/doc/latex/tlc2/partial.toc
%{_texmfdistdir}/doc/latex/tlc2/rosette.ps
%{_texmfdistdir}/doc/latex/tlc2/tex.bib
%{_texmfdistdir}/doc/latex/tlc2/ttctexa.cls
%{_texmfdistdir}/doc/latex/tlc2/ttctexamargin.cls
%{_texmfdistdir}/doc/latex/tlc2/ttctexareport.cls
%{_texmfdistdir}/doc/latex/tlc2/w.eps
%{_texmfdistdir}/doc/latex/tlc2/w.ps
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-tlc2-%{texlive_version}.%{texlive_noarch}.svn26096-%{release}-zypper
%endif

%package -n texlive-tocbibind
Version:        %{texlive_version}.%{texlive_noarch}.1.5ksvn20085
Release:        0
Summary:        Add bibliography/index/contents to Table of Contents
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-tocbibind-doc >= %{texlive_version}
Provides:       tex(tocbibind.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source110:      tocbibind.tar.xz
Source111:      tocbibind.doc.tar.xz

%description -n texlive-tocbibind
Automatically adds the bibliography and/or the index and/or the
contents, etc., to the Table of Contents listing.

%package -n texlive-tocbibind-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.5ksvn20085
Release:        0
Summary:        Documentation for texlive-tocbibind
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-tocbibind-doc
This package includes the documentation for texlive-tocbibind

%post -n texlive-tocbibind
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tocbibind 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tocbibind
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tocbibind-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/tocbibind/README
%{_texmfdistdir}/doc/latex/tocbibind/tocbibind.pdf

%files -n texlive-tocbibind
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/tocbibind/tocbibind.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-tocbibind-%{texlive_version}.%{texlive_noarch}.1.5ksvn20085-%{release}-zypper
%endif

%package -n texlive-tocdata
Version:        %{texlive_version}.%{texlive_noarch}.2.03svn51654
Release:        0
Summary:        Adds names to chapters, sections, figures in the TOC and LOF
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-tocdata-doc >= %{texlive_version}
Provides:       tex(tocdata.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(titletoc.sty)
Requires:       tex(tocloft.sty)
Requires:       tex(xparse.sty)
Requires:       tex(xpatch.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source112:      tocdata.tar.xz
Source113:      tocdata.doc.tar.xz

%description -n texlive-tocdata
The tocdata package may be used to add a small amount of data
to an entry in the table of contents or list of figures,
between the section or caption name and the page number. The
typical use would be to add the name of an author or artist of
a chapter or section, such as in an anthology or a collection
of papers. Additionally, user-level macros are provided which
add the author's name to a chapter or section, along with an
optional prefix and/or suffix, and add to a figure the artist's
name, prefix, and suffix, plus optional additional text. Author
and artist names are also added to the index. Additional
user-level macros control formatting. tocdata works with the
TOC/LOF formatting of the default LaTeX classes, memoir,
koma-script, and with titletoc, tocloft, tocbasic, and
tocstyle.

%package -n texlive-tocdata-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.03svn51654
Release:        0
Summary:        Documentation for texlive-tocdata
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-tocdata-doc
This package includes the documentation for texlive-tocdata

%post -n texlive-tocdata
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tocdata 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tocdata
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tocdata-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/tocdata/README.txt
%{_texmfdistdir}/doc/latex/tocdata/tocdata.pdf

%files -n texlive-tocdata
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/tocdata/tocdata.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-tocdata-%{texlive_version}.%{texlive_noarch}.2.03svn51654-%{release}-zypper
%endif

%package -n texlive-tocloft
Version:        %{texlive_version}.%{texlive_noarch}.2.3jsvn53364
Release:        0
Summary:        Control table of contents, figures, etcetera
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-tocloft-doc >= %{texlive_version}
Provides:       tex(tocloft.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source114:      tocloft.tar.xz
Source115:      tocloft.doc.tar.xz

%description -n texlive-tocloft
Provides control over the typography of the Table of Contents,
List of Figures and List of Tables, and the ability to create
new 'List of ...'. The ToC \parskip may be changed.

%package -n texlive-tocloft-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.3jsvn53364
Release:        0
Summary:        Documentation for texlive-tocloft
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-tocloft-doc
This package includes the documentation for texlive-tocloft

%post -n texlive-tocloft
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tocloft 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tocloft
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tocloft-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/tocloft/README
%{_texmfdistdir}/doc/latex/tocloft/tocloft.pdf

%files -n texlive-tocloft
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/tocloft/tocloft.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-tocloft-%{texlive_version}.%{texlive_noarch}.2.3jsvn53364-%{release}-zypper
%endif

%package -n texlive-tocvsec2
Version:        %{texlive_version}.%{texlive_noarch}.1.3asvn33146
Release:        0
Summary:        Section numbering and table of contents control
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-tocvsec2-doc >= %{texlive_version}
Provides:       tex(tocvsec2.sty)
Requires:       tex(ifthen.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source116:      tocvsec2.tar.xz
Source117:      tocvsec2.doc.tar.xz

%description -n texlive-tocvsec2
Provides control over section numbering (without recourse to
starred sectional commands) and/or the entries in the Table of
Contents on a section by section basis.

%package -n texlive-tocvsec2-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.3asvn33146
Release:        0
Summary:        Documentation for texlive-tocvsec2
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-tocvsec2-doc
This package includes the documentation for texlive-tocvsec2

%post -n texlive-tocvsec2
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tocvsec2 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tocvsec2
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tocvsec2-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/tocvsec2/README
%{_texmfdistdir}/doc/latex/tocvsec2/tocvsec2-example.tex
%{_texmfdistdir}/doc/latex/tocvsec2/tocvsec2.pdf

%files -n texlive-tocvsec2
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/tocvsec2/tocvsec2.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-tocvsec2-%{texlive_version}.%{texlive_noarch}.1.3asvn33146-%{release}-zypper
%endif

%package -n texlive-todo
Version:        %{texlive_version}.%{texlive_noarch}.2.142svn17746
Release:        0
Summary:        Make a to-do list for a document
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-todo-doc >= %{texlive_version}
Provides:       tex(todo.sty)
Requires:       tex(amssymb.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source118:      todo.tar.xz
Source119:      todo.doc.tar.xz

%description -n texlive-todo
The package allows you to insert "to do" marks in your
document, to make lists of such items, and to cross-reference
to them.

%package -n texlive-todo-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.142svn17746
Release:        0
Summary:        Documentation for texlive-todo
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-todo-doc
This package includes the documentation for texlive-todo

%post -n texlive-todo
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-todo 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-todo
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-todo-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/todo/README
%{_texmfdistdir}/doc/latex/todo/todo-spl.pdf
%{_texmfdistdir}/doc/latex/todo/todo-spl.tex
%{_texmfdistdir}/doc/latex/todo/todo.pdf

%files -n texlive-todo
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/todo/todo.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-todo-%{texlive_version}.%{texlive_noarch}.2.142svn17746-%{release}-zypper
%endif

%package -n texlive-todonotes
Version:        %{texlive_version}.%{texlive_noarch}.1.1.2svn52662
Release:        0
Summary:        Marking things to do in a LaTeX document
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-pgf >= %{texlive_version}
#!BuildIgnore: texlive-pgf
Requires:       texlive-tools >= %{texlive_version}
#!BuildIgnore: texlive-tools
Requires:       texlive-xcolor >= %{texlive_version}
#!BuildIgnore: texlive-xcolor
Requires:       texlive-xkeyval >= %{texlive_version}
#!BuildIgnore: texlive-xkeyval
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-todonotes-doc >= %{texlive_version}
Provides:       tex(todonotes.sty)
Requires:       tex(calc.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source120:      todonotes.tar.xz
Source121:      todonotes.doc.tar.xz

%description -n texlive-todonotes
The package lets the user mark things to do later, in a simple
and visually appealing way. The package takes several options
to enable customization/finetuning of the visual appearance.

%package -n texlive-todonotes-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1.2svn52662
Release:        0
Summary:        Documentation for texlive-todonotes
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-todonotes-doc
This package includes the documentation for texlive-todonotes

%post -n texlive-todonotes
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-todonotes 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-todonotes
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-todonotes-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/todonotes/README
%{_texmfdistdir}/doc/latex/todonotes/examples/alterAppearenceOfListOfTodos.pdf
%{_texmfdistdir}/doc/latex/todonotes/examples/alterAppearenceOfListOfTodos.tex
%{_texmfdistdir}/doc/latex/todonotes/examples/externalize.pdf
%{_texmfdistdir}/doc/latex/todonotes/examples/externalize.tex
%{_texmfdistdir}/doc/latex/todonotes/examples/saveColorByUsingLayers.pdf
%{_texmfdistdir}/doc/latex/todonotes/examples/saveColorByUsingLayers.tex
%{_texmfdistdir}/doc/latex/todonotes/todonotes.pdf

%files -n texlive-todonotes
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/todonotes/todonotes.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-todonotes-%{texlive_version}.%{texlive_noarch}.1.1.2svn52662-%{release}-zypper
%endif

%package -n texlive-tokcycle
Version:        %{texlive_version}.%{texlive_noarch}.1.12svn53755
Release:        0
Summary:        The tokcycle package helps one to build tools to process tokens from an input stream, on a token-by-token basis
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-tokcycle-doc >= %{texlive_version}
Provides:       tex(tokcycle.sty)
Provides:       tex(tokcycle.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source122:      tokcycle.tar.xz
Source123:      tokcycle.doc.tar.xz

%description -n texlive-tokcycle
The tokcycle package helps one to build tools to process tokens
from an input stream. If a macro to process an arbitrary single
token can be built, then tokcycle can provide a wrapper for
cycling through an input stream (including macros, spaces, and
groups) on a token-by-token basis, using the provided macro on
each successive character. tokcycle characterizes each
successive token in the input stream as a Character, a Group, a
Macro, or a Space. Each of these token categories are processed
with a unique directive, to bring about the desired effect of
the token cycle. If condition flags are provided to identify
active, implicit, and catcode-6 tokens as they are digested.
The package provides a number of options for handling groups.

%package -n texlive-tokcycle-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.12svn53755
Release:        0
Summary:        Documentation for texlive-tokcycle
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-tokcycle-doc
This package includes the documentation for texlive-tokcycle

%post -n texlive-tokcycle
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tokcycle 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tokcycle
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tokcycle-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/tokcycle/README
%{_texmfdistdir}/doc/generic/tokcycle/tokcycle-doc.pdf
%{_texmfdistdir}/doc/generic/tokcycle/tokcycle-doc.tex
%{_texmfdistdir}/doc/generic/tokcycle/tokcycle-examples.pdf
%{_texmfdistdir}/doc/generic/tokcycle/tokcycle-examples.tex

%files -n texlive-tokcycle
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/tokcycle/tokcycle.sty
%{_texmfdistdir}/tex/generic/tokcycle/tokcycle.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-tokcycle-%{texlive_version}.%{texlive_noarch}.1.12svn53755-%{release}-zypper
%endif

%package -n texlive-tokenizer
Version:        %{texlive_version}.%{texlive_noarch}.1.1.0svn15878
Release:        0
Summary:        A tokenizer
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-tokenizer-doc >= %{texlive_version}
Provides:       tex(tokenizer.sty)
Requires:       tex(ifthen.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source124:      tokenizer.tar.xz
Source125:      tokenizer.doc.tar.xz

%description -n texlive-tokenizer
A tokenizer for LaTeX. \GetTokens{Target1}{Target2}{Source}
splits source into two tokens at the first encounter of a
comma. The first token is saved in a newly created command with
the name passed as <Target1> and the second token likewise. A
package option 'trim' causes leading and trailing space to be
removed from each token; with this option, the \TrimSpaces
command is defined, which removes leading and trailing spaces
from its argument.

%package -n texlive-tokenizer-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1.0svn15878
Release:        0
Summary:        Documentation for texlive-tokenizer
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-tokenizer-doc
This package includes the documentation for texlive-tokenizer

%post -n texlive-tokenizer
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tokenizer 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tokenizer
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tokenizer-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/tokenizer/tokenizer.pdf
%{_texmfdistdir}/doc/latex/tokenizer/tokenizer.tex

%files -n texlive-tokenizer
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/tokenizer/tokenizer.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-tokenizer-%{texlive_version}.%{texlive_noarch}.1.1.0svn15878-%{release}-zypper
%endif

%package -n texlive-toolbox
Version:        %{texlive_version}.%{texlive_noarch}.5.1svn32260
Release:        0
Summary:        Tool macros
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-toolbox-doc >= %{texlive_version}
Provides:       tex(toolbox.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source126:      toolbox.tar.xz
Source127:      toolbox.doc.tar.xz

%description -n texlive-toolbox
A package for (La)TeX which provides some macros which are
convenient for writing indexes, glossaries, or other macros. It
contains macros which support: implicit macros; fancy optional
arguments; loops over tokenlists and itemlists; searching and
splitting; controlled expansion; redefinition of macros; and
concatenated macro names; macros for text replacement.

%package -n texlive-toolbox-doc
Version:        %{texlive_version}.%{texlive_noarch}.5.1svn32260
Release:        0
Summary:        Documentation for texlive-toolbox
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-toolbox-doc
This package includes the documentation for texlive-toolbox

%post -n texlive-toolbox
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-toolbox 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-toolbox
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-toolbox-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/toolbox/README
%{_texmfdistdir}/doc/latex/toolbox/toolbox.pdf
%{_texmfdistdir}/doc/latex/toolbox/toolbox.tex
%{_texmfdistdir}/doc/latex/toolbox/toolbox.txt

%files -n texlive-toolbox
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/toolbox/toolbox.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-toolbox-%{texlive_version}.%{texlive_noarch}.5.1svn32260-%{release}-zypper
%endif

%package -n texlive-tools
Version:        %{texlive_version}.%{texlive_noarch}.svn53640
Release:        0
Summary:        The LaTeX standard tools bundle
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-extratools >= %{texlive_version}
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-tools-doc >= %{texlive_version}
Provides:       tex(afterpage.sty)
Provides:       tex(array-2016-10-06.sty)
Provides:       tex(array.sty)
Provides:       tex(bm.sty)
Provides:       tex(calc.sty)
Provides:       tex(dcolumn.sty)
Provides:       tex(delarray.sty)
Provides:       tex(e.tex)
Provides:       tex(enumerate.sty)
Provides:       tex(fontsmpl.sty)
Provides:       tex(fontsmpl.tex)
Provides:       tex(ftnright.sty)
Provides:       tex(h.tex)
Provides:       tex(hhline.sty)
Provides:       tex(indentfirst.sty)
Provides:       tex(layout.sty)
Provides:       tex(longtable.sty)
Provides:       tex(multicol-2017-04-11.sty)
Provides:       tex(multicol.sty)
Provides:       tex(q.tex)
Provides:       tex(r.tex)
Provides:       tex(rawfonts.sty)
Provides:       tex(s.tex)
Provides:       tex(shellesc.sty)
Provides:       tex(showkeys.sty)
Provides:       tex(somedefs.sty)
Provides:       tex(tabularx.sty)
Provides:       tex(thb.sty)
Provides:       tex(thc.sty)
Provides:       tex(thcb.sty)
Provides:       tex(theorem.sty)
Provides:       tex(thm.sty)
Provides:       tex(thmb.sty)
Provides:       tex(thp.sty)
Provides:       tex(trace.sty)
Provides:       tex(varioref-2016-02-16.sty)
Provides:       tex(varioref.sty)
Provides:       tex(verbatim.sty)
Provides:       tex(verbtest.tex)
Provides:       tex(x.tex)
Provides:       tex(xr.sty)
Provides:       tex(xspace.sty)
Requires:       tex(color.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source128:      tools.tar.xz
Source129:      tools.doc.tar.xz

%description -n texlive-tools
A collection of (variously) simple tools provided as part of
the LaTeX required tools distribution, comprising the packages:
afterpage, array, bm, calc, dcolumn, delarray, enumerate,
fileerr, fontsmpl, ftnright, hhline, indentfirst, layout,
longtable, multicol, rawfonts, showkeys, somedefs, tabularx,
theorem, trace, varioref, verbatim, xr, and xspace.

%package -n texlive-tools-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn53640
Release:        0
Summary:        Documentation for texlive-tools
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-tools-doc
This package includes the documentation for texlive-tools

%post -n texlive-tools
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tools 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tools
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tools-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/tools/README.md
%{_texmfdistdir}/doc/latex/tools/afterpage.pdf
%{_texmfdistdir}/doc/latex/tools/array.pdf
%{_texmfdistdir}/doc/latex/tools/bm.pdf
%{_texmfdistdir}/doc/latex/tools/calc.pdf
%{_texmfdistdir}/doc/latex/tools/changes.txt
%{_texmfdistdir}/doc/latex/tools/dcolumn.pdf
%{_texmfdistdir}/doc/latex/tools/delarray.pdf
%{_texmfdistdir}/doc/latex/tools/enumerate.pdf
%{_texmfdistdir}/doc/latex/tools/fileerr.pdf
%{_texmfdistdir}/doc/latex/tools/fontsmpl.pdf
%{_texmfdistdir}/doc/latex/tools/ftnright.pdf
%{_texmfdistdir}/doc/latex/tools/hhline.pdf
%{_texmfdistdir}/doc/latex/tools/indentfirst.pdf
%{_texmfdistdir}/doc/latex/tools/layout.pdf
%{_texmfdistdir}/doc/latex/tools/longtable.pdf
%{_texmfdistdir}/doc/latex/tools/manifest.txt
%{_texmfdistdir}/doc/latex/tools/multicol.pdf
%{_texmfdistdir}/doc/latex/tools/rawfonts.pdf
%{_texmfdistdir}/doc/latex/tools/shellesc.pdf
%{_texmfdistdir}/doc/latex/tools/showkeys.pdf
%{_texmfdistdir}/doc/latex/tools/somedefs.pdf
%{_texmfdistdir}/doc/latex/tools/tabularx.pdf
%{_texmfdistdir}/doc/latex/tools/theorem.pdf
%{_texmfdistdir}/doc/latex/tools/tools-overview.pdf
%{_texmfdistdir}/doc/latex/tools/tools-overview.tex
%{_texmfdistdir}/doc/latex/tools/trace.pdf
%{_texmfdistdir}/doc/latex/tools/varioref.pdf
%{_texmfdistdir}/doc/latex/tools/verbatim.pdf
%{_texmfdistdir}/doc/latex/tools/xr.pdf
%{_texmfdistdir}/doc/latex/tools/xspace.pdf

%files -n texlive-tools
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/tools/.tex
%{_texmfdistdir}/tex/latex/tools/afterpage.sty
%{_texmfdistdir}/tex/latex/tools/array-2016-10-06.sty
%{_texmfdistdir}/tex/latex/tools/array.sty
%{_texmfdistdir}/tex/latex/tools/bm.sty
%{_texmfdistdir}/tex/latex/tools/calc.sty
%{_texmfdistdir}/tex/latex/tools/dcolumn.sty
%{_texmfdistdir}/tex/latex/tools/delarray.sty
%{_texmfdistdir}/tex/latex/tools/e.tex
%{_texmfdistdir}/tex/latex/tools/enumerate.sty
%{_texmfdistdir}/tex/latex/tools/fontsmpl.sty
%{_texmfdistdir}/tex/latex/tools/fontsmpl.tex
%{_texmfdistdir}/tex/latex/tools/ftnright.sty
%{_texmfdistdir}/tex/latex/tools/h.tex
%{_texmfdistdir}/tex/latex/tools/hhline.sty
%{_texmfdistdir}/tex/latex/tools/indentfirst.sty
%{_texmfdistdir}/tex/latex/tools/layout.sty
%{_texmfdistdir}/tex/latex/tools/longtable.sty
%{_texmfdistdir}/tex/latex/tools/multicol-2017-04-11.sty
%{_texmfdistdir}/tex/latex/tools/multicol.sty
%{_texmfdistdir}/tex/latex/tools/q.tex
%{_texmfdistdir}/tex/latex/tools/r.tex
%{_texmfdistdir}/tex/latex/tools/rawfonts.sty
%{_texmfdistdir}/tex/latex/tools/s.tex
%{_texmfdistdir}/tex/latex/tools/shellesc.sty
%{_texmfdistdir}/tex/latex/tools/showkeys.sty
%{_texmfdistdir}/tex/latex/tools/somedefs.sty
%{_texmfdistdir}/tex/latex/tools/tabularx.sty
%{_texmfdistdir}/tex/latex/tools/thb.sty
%{_texmfdistdir}/tex/latex/tools/thc.sty
%{_texmfdistdir}/tex/latex/tools/thcb.sty
%{_texmfdistdir}/tex/latex/tools/theorem.sty
%{_texmfdistdir}/tex/latex/tools/thm.sty
%{_texmfdistdir}/tex/latex/tools/thmb.sty
%{_texmfdistdir}/tex/latex/tools/thp.sty
%{_texmfdistdir}/tex/latex/tools/trace.sty
%{_texmfdistdir}/tex/latex/tools/varioref-2016-02-16.sty
%{_texmfdistdir}/tex/latex/tools/varioref.sty
%{_texmfdistdir}/tex/latex/tools/verbatim.sty
%{_texmfdistdir}/tex/latex/tools/verbtest.tex
%{_texmfdistdir}/tex/latex/tools/x.tex
%{_texmfdistdir}/tex/latex/tools/xr.sty
%{_texmfdistdir}/tex/latex/tools/xspace.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-tools-%{texlive_version}.%{texlive_noarch}.svn53640-%{release}-zypper
%endif

%package -n texlive-topfloat
Version:        %{texlive_version}.%{texlive_noarch}.svn19084
Release:        0
Summary:        Move floats to the top of the page
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-topfloat-doc >= %{texlive_version}
Provides:       tex(topfloat.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source130:      topfloat.tar.xz
Source131:      topfloat.doc.tar.xz

%description -n texlive-topfloat
The topfloat package

%package -n texlive-topfloat-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn19084
Release:        0
Summary:        Documentation for texlive-topfloat
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-topfloat-doc:it)

%description -n texlive-topfloat-doc
This package includes the documentation for texlive-topfloat

%post -n texlive-topfloat
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-topfloat 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-topfloat
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-topfloat-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/topfloat/topfloat.pdf
%{_texmfdistdir}/doc/latex/topfloat/topfloat.tex

%files -n texlive-topfloat
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/topfloat/topfloat.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-topfloat-%{texlive_version}.%{texlive_noarch}.svn19084-%{release}-zypper
%endif

%package -n texlive-topiclongtable
Version:        %{texlive_version}.%{texlive_noarch}.1.3.2svn54758
Release:        0
Summary:        Extend longtable with cells that merge hierarchically
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-topiclongtable-doc >= %{texlive_version}
Provides:       tex(topiclongtable.sty)
Requires:       tex(array.sty)
Requires:       tex(expl3.sty)
Requires:       tex(longtable.sty)
Requires:       tex(multirow.sty)
Requires:       tex(xparse.sty)
Requires:       tex(zref-abspage.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source132:      topiclongtable.tar.xz
Source133:      topiclongtable.doc.tar.xz

%description -n texlive-topiclongtable
This LaTeX package extends longtable implementing cells that:
merge with the one above if it has the same content, do not
merge with the one above unless the ones on the left are
merged, are well behaved with respect to longtable chunking on
page breaks, and automatically draw the correct separation
lines. The typical use case is a table spanning multiple pages
that contains a list of hierarchically organized topics (hence
the package name). The package depends on array, expl3,
longtable, multirow, xparse, and zref-abspage.

%package -n texlive-topiclongtable-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.3.2svn54758
Release:        0
Summary:        Documentation for texlive-topiclongtable
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-topiclongtable-doc
This package includes the documentation for texlive-topiclongtable

%post -n texlive-topiclongtable
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-topiclongtable 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-topiclongtable
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-topiclongtable-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/topiclongtable/README.md
%{_texmfdistdir}/doc/latex/topiclongtable/topiclongtable-doc.pdf
%{_texmfdistdir}/doc/latex/topiclongtable/topiclongtable-doc.tex

%files -n texlive-topiclongtable
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/topiclongtable/topiclongtable.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-topiclongtable-%{texlive_version}.%{texlive_noarch}.1.3.2svn54758-%{release}-zypper
%endif

%package -n texlive-topletter
Version:        %{texlive_version}.%{texlive_noarch}.0.0.3.0svn48182
Release:        0
Summary:        Letter class for the Politecnico di Torino
License:        Apache-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-topletter-doc >= %{texlive_version}
Provides:       tex(TOPletter.cls)
Requires:       tex(article.cls)
Requires:       tex(babel.sty)
Requires:       tex(changepage.sty)
Requires:       tex(color.sty)
Requires:       tex(fancyhdr.sty)
Requires:       tex(geometry.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(helvet.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(iflang.sty)
Requires:       tex(inputenc.sty)
Requires:       tex(setspace.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source134:      topletter.tar.xz
Source135:      topletter.doc.tar.xz

%description -n texlive-topletter
This package provides a LaTeX class for typesetting letters
conforming to the official Corporate Image guidelines for the
Politecnico di Torino. The class can be used for letters
written in Italian and in English.

%package -n texlive-topletter-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.3.0svn48182
Release:        0
Summary:        Documentation for texlive-topletter
License:        Apache-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-topletter-doc:it)

%description -n texlive-topletter-doc
This package includes the documentation for texlive-topletter

%post -n texlive-topletter
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-topletter 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-topletter
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-topletter-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/topletter/EsempioLettera.pdf
%{_texmfdistdir}/doc/latex/topletter/EsempioLettera.tex
%{_texmfdistdir}/doc/latex/topletter/ExampleLetter.pdf
%{_texmfdistdir}/doc/latex/topletter/ExampleLetter.tex
%{_texmfdistdir}/doc/latex/topletter/LICENSE
%{_texmfdistdir}/doc/latex/topletter/LogoPolitoBlu.pdf
%{_texmfdistdir}/doc/latex/topletter/README.md
%{_texmfdistdir}/doc/latex/topletter/TOPletter.pdf
%{_texmfdistdir}/doc/latex/topletter/Walt_Disney_1942_signature.pdf

%files -n texlive-topletter
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/topletter/TOPletter.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-topletter-%{texlive_version}.%{texlive_noarch}.0.0.3.0svn48182-%{release}-zypper
%endif

%package -n texlive-toptesi
Version:        %{texlive_version}.%{texlive_noarch}.6.3.06svn51743
Release:        0
Summary:        Bundle for typesetting multilanguage theses
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-toptesi-doc >= %{texlive_version}
Provides:       tex(topcoman.sty)
Provides:       tex(topfront.sty)
Provides:       tex(toptesi-dottorale.sty)
Provides:       tex(toptesi-magistrale.sty)
Provides:       tex(toptesi-monografia.sty)
Provides:       tex(toptesi-scudo.sty)
Provides:       tex(toptesi-sss.sty)
Provides:       tex(toptesi.cfg)
Provides:       tex(toptesi.cls)
Provides:       tex(toptesi.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(amsthm.sty)
Requires:       tex(babel.sty)
Requires:       tex(booktabs.sty)
Requires:       tex(calc.sty)
Requires:       tex(caption.sty)
Requires:       tex(csquotes.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(fancyvrb.sty)
Requires:       tex(filecontents.sty)
Requires:       tex(float.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(frontespizio.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(iftex.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(imakeidx.sty)
Requires:       tex(indentfirst.sty)
Requires:       tex(lscape.sty)
Requires:       tex(multirow.sty)
Requires:       tex(nomencl.sty)
Requires:       tex(polyglossia.sty)
Requires:       tex(report.cls)
Requires:       tex(scrextend.sty)
Requires:       tex(setspace.sty)
Requires:       tex(siunitx.sty)
Requires:       tex(subcaption.sty)
Requires:       tex(tabularx.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(trace.sty)
Requires:       tex(unicode-math.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xparse.sty)
Requires:       tex(xspace.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source136:      toptesi.tar.xz
Source137:      toptesi.doc.tar.xz

%description -n texlive-toptesi
This bundle contains everything needed for typesetting a
bachelor, master, or PhD thesis in Italian (or in any other
language supported by LaTeX: the bundle is constructed to
support multilingual use). The infix strings may be selected
and specified at will by means of a configuration file, so as
to customize the layout of the front page to the requirements
of a specific university. Thanks to its language management,
the bundle is suited for multilanguage theses that are becoming
more and more frequent thanks to the double degree programs of
the European Community Socrates programs. Toptesi is designed
to save the PDF version of a thesis in PDF/A-1b compliant mode
and with all the necessary metadata.

%package -n texlive-toptesi-doc
Version:        %{texlive_version}.%{texlive_noarch}.6.3.06svn51743
Release:        0
Summary:        Documentation for texlive-toptesi
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-toptesi-doc:en;it)

%description -n texlive-toptesi-doc
This package includes the documentation for texlive-toptesi

%post -n texlive-toptesi
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-toptesi 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-toptesi
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-toptesi-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/toptesi/FrontespiziAssemblati.pdf
%{_texmfdistdir}/doc/latex/toptesi/FrontespiziAssemblati1.pdf
%{_texmfdistdir}/doc/latex/toptesi/FrontespiziAssemblati2.pdf
%{_texmfdistdir}/doc/latex/toptesi/Frontespizio-sss.pdf
%{_texmfdistdir}/doc/latex/toptesi/FrontespizioLandscape.pdf
%{_texmfdistdir}/doc/latex/toptesi/FrontespizioScudo.pdf
%{_texmfdistdir}/doc/latex/toptesi/GuITlogo.pdf
%{_texmfdistdir}/doc/latex/toptesi/MPlogo.pdf
%{_texmfdistdir}/doc/latex/toptesi/README.txt
%{_texmfdistdir}/doc/latex/toptesi/TITDocScCropped.pdf
%{_texmfdistdir}/doc/latex/toptesi/TITlogoCropped.pdf
%{_texmfdistdir}/doc/latex/toptesi/Toptesi-con-topfront.pdf
%{_texmfdistdir}/doc/latex/toptesi/Toptesi-con-topfront.tex
%{_texmfdistdir}/doc/latex/toptesi/Toptesi-example-topfront.pdf
%{_texmfdistdir}/doc/latex/toptesi/Toptesi-example-topfront.tex
%{_texmfdistdir}/doc/latex/toptesi/VeraPDFiniziale.jpg
%{_texmfdistdir}/doc/latex/toptesi/logodue.pdf
%{_texmfdistdir}/doc/latex/toptesi/logoquattro.pdf
%{_texmfdistdir}/doc/latex/toptesi/logotre.pdf
%{_texmfdistdir}/doc/latex/toptesi/logouno.pdf
%{_texmfdistdir}/doc/latex/toptesi/lppl.tex
%{_texmfdistdir}/doc/latex/toptesi/topfront-example.pdf
%{_texmfdistdir}/doc/latex/toptesi/topfront-example.tex
%{_texmfdistdir}/doc/latex/toptesi/toptesi-example-con-frontespizio.pdf
%{_texmfdistdir}/doc/latex/toptesi/toptesi-example-con-frontespizio.tex
%{_texmfdistdir}/doc/latex/toptesi/toptesi-example-dottorale.pdf
%{_texmfdistdir}/doc/latex/toptesi/toptesi-example-dottorale.tex
%{_texmfdistdir}/doc/latex/toptesi/toptesi-example-luatex.pdf
%{_texmfdistdir}/doc/latex/toptesi/toptesi-example-luatex.tex
%{_texmfdistdir}/doc/latex/toptesi/toptesi-example-magistrale.pdf
%{_texmfdistdir}/doc/latex/toptesi/toptesi-example-magistrale.tex
%{_texmfdistdir}/doc/latex/toptesi/toptesi-example-sss.pdf
%{_texmfdistdir}/doc/latex/toptesi/toptesi-example-sss.tex
%{_texmfdistdir}/doc/latex/toptesi/toptesi-example-triennale.pdf
%{_texmfdistdir}/doc/latex/toptesi/toptesi-example-triennale.tex
%{_texmfdistdir}/doc/latex/toptesi/toptesi-example-xetex.pdf
%{_texmfdistdir}/doc/latex/toptesi/toptesi-example-xetex.tex
%{_texmfdistdir}/doc/latex/toptesi/toptesi-example.cfg
%{_texmfdistdir}/doc/latex/toptesi/toptesi-example.pdf
%{_texmfdistdir}/doc/latex/toptesi/toptesi-example.tex
%{_texmfdistdir}/doc/latex/toptesi/toptesi-it.pdf
%{_texmfdistdir}/doc/latex/toptesi/toptesi-it.tex
%{_texmfdistdir}/doc/latex/toptesi/toptesi-scudo-example.zip
%{_texmfdistdir}/doc/latex/toptesi/toptesi.pdf
%{_texmfdistdir}/doc/latex/toptesi/veraPDFconformance.jpg
%{_texmfdistdir}/doc/latex/toptesi/veraPDFnoconformance.jpg

%files -n texlive-toptesi
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/toptesi/topcoman.sty
%{_texmfdistdir}/tex/latex/toptesi/topfront.sty
%{_texmfdistdir}/tex/latex/toptesi/toptesi-dottorale.sty
%{_texmfdistdir}/tex/latex/toptesi/toptesi-magistrale.sty
%{_texmfdistdir}/tex/latex/toptesi/toptesi-monografia.sty
%{_texmfdistdir}/tex/latex/toptesi/toptesi-scudo.sty
%{_texmfdistdir}/tex/latex/toptesi/toptesi-sss.sty
%{_texmfdistdir}/tex/latex/toptesi/toptesi.cfg
%{_texmfdistdir}/tex/latex/toptesi/toptesi.cls
%{_texmfdistdir}/tex/latex/toptesi/toptesi.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-toptesi-%{texlive_version}.%{texlive_noarch}.6.3.06svn51743-%{release}-zypper
%endif

%package -n texlive-totcount
Version:        %{texlive_version}.%{texlive_noarch}.1.2svn21178
Release:        0
Summary:        Find the last value of a counter
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-totcount-doc >= %{texlive_version}
Provides:       tex(totcount.sty)
Requires:       tex(keyval.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source138:      totcount.tar.xz
Source139:      totcount.doc.tar.xz

%description -n texlive-totcount
The package records the value that was last set, for any
counter of interest; since most such counters are simply
incremented when they are changed, the recorded value will
usually be the maximum value.

%package -n texlive-totcount-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.2svn21178
Release:        0
Summary:        Documentation for texlive-totcount
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-totcount-doc
This package includes the documentation for texlive-totcount

%post -n texlive-totcount
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-totcount 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-totcount
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-totcount-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/totcount/README
%{_texmfdistdir}/doc/latex/totcount/totcount-ex.tex
%{_texmfdistdir}/doc/latex/totcount/totcount.pdf

%files -n texlive-totcount
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/totcount/totcount.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-totcount-%{texlive_version}.%{texlive_noarch}.1.2svn21178-%{release}-zypper
%endif

%package -n texlive-totpages
Version:        %{texlive_version}.%{texlive_noarch}.2.00svn15878
Release:        0
Summary:        Count pages in a document, and report last page number
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-totpages-doc >= %{texlive_version}
Provides:       tex(totpages.sty)
Requires:       tex(everyshi.sty)
Requires:       tex(keyval.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source140:      totpages.tar.xz
Source141:      totpages.doc.tar.xz

%description -n texlive-totpages
The package counts the actual pages in the document (as opposed
to reporting the number of the last page, as does lastpage).
The counter itself may be shipped out to the DVI file. The
package uses the everyshi package for its task.

%package -n texlive-totpages-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.00svn15878
Release:        0
Summary:        Documentation for texlive-totpages
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-totpages-doc
This package includes the documentation for texlive-totpages

%post -n texlive-totpages
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-totpages 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-totpages
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-totpages-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/totpages/README
%{_texmfdistdir}/doc/latex/totpages/totexmpl.tex
%{_texmfdistdir}/doc/latex/totpages/totpages.pdf

%files -n texlive-totpages
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/totpages/totpages.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-totpages-%{texlive_version}.%{texlive_noarch}.2.00svn15878-%{release}-zypper
%endif

%package -n texlive-tpic2pdftex
Version:        %{texlive_version}.%{texlive_noarch}.svn52851
Release:        0
Summary:        Use tpic commands in pdfTeX
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-tpic2pdftex-bin >= %{texlive_version}
#!BuildIgnore: texlive-tpic2pdftex-bin
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Provides:       man(tpic2pdftex.1)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source142:      tpic2pdftex.doc.tar.xz

%description -n texlive-tpic2pdftex
The AWK script converts pic language, embedded inline
(delimited by .PS and .PE markers), to \pdfliteral commands.
%post -n texlive-tpic2pdftex
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tpic2pdftex 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tpic2pdftex
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tpic2pdftex
%defattr(-,root,root,755)
%{_mandir}/man1/tpic2pdftex.1*
%{_texmfdistdir}/doc/tpic2pdftex/Makefile
%{_texmfdistdir}/doc/tpic2pdftex/beamerexample.pdf
%{_texmfdistdir}/doc/tpic2pdftex/beamerexample.pic
%{_texmfdistdir}/doc/tpic2pdftex/example.pdf
%{_texmfdistdir}/doc/tpic2pdftex/example.pic
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-tpic2pdftex-%{texlive_version}.%{texlive_noarch}.svn52851-%{release}-zypper
%endif

%package -n texlive-tpslifonts
Version:        %{texlive_version}.%{texlive_noarch}.0.0.6svn42428
Release:        0
Summary:        A LaTeX package for configuring presentation fonts
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-tpslifonts-doc >= %{texlive_version}
Provides:       tex(tpslifonts.sty)
Requires:       tex(cmbright.sty)
Requires:       tex(eulervm.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(t1cmdh.fd)
Requires:       tex(t1cmfib.fd)
Requires:       tex(t1cmfr.fd)
Requires:       tex(t1cmr.fd)
Requires:       tex(t1cmss.fd)
Requires:       tex(t1cmtt.fd)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source143:      tpslifonts.tar.xz
Source144:      tpslifonts.doc.tar.xz

%description -n texlive-tpslifonts
This package aims to improve of font readability in
presentations, especially with maths. The standard cm maths
fonts at large design sizes are difficult to read from far
away, especially at low resolutions and low contrast color
choice. Using this package leads to much better overall
readability of some font combinations. The package offers a
couple of 'harmonising' combinations of text and maths fonts
from the (distant) relatives of computer modern fonts, with a
couple of extras for optimising readability. Text fonts from
computer modern roman, computer modern sans serif, SliTeX
computer modern sans serif, computer modern bright, or concrete
roman are available, in addition to maths fonts from computer
modern maths, computer modern bright maths, or Euler fonts. The
package is part of the TeXPower bundle.

%package -n texlive-tpslifonts-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.6svn42428
Release:        0
Summary:        Documentation for texlive-tpslifonts
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-tpslifonts-doc
This package includes the documentation for texlive-tpslifonts

%post -n texlive-tpslifonts
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tpslifonts 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tpslifonts
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tpslifonts-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/tpslifonts/00readme.txt
%{_texmfdistdir}/doc/latex/tpslifonts/01install.txt
%{_texmfdistdir}/doc/latex/tpslifonts/Makefile
%{_texmfdistdir}/doc/latex/tpslifonts/slifontsexample.tex

%files -n texlive-tpslifonts
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/tpslifonts/tpslifonts.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-tpslifonts-%{texlive_version}.%{texlive_noarch}.0.0.6svn42428-%{release}-zypper
%endif

%package -n texlive-tqft
Version:        %{texlive_version}.%{texlive_noarch}.2.1svn44455
Release:        0
Summary:        Drawing TQFT diagrams with TikZ/PGF
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-tqft-doc >= %{texlive_version}
Provides:       tex(tikzlibrarytqft.code.tex)
Provides:       tex(tqft.sty)
Requires:       tex(pgf.sty)
Requires:       tex(pgfkeys.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source145:      tqft.tar.xz
Source146:      tqft.doc.tar.xz

%description -n texlive-tqft
The package defines some node shapes useful for drawing TQFT
diagrams with TikZ/PGF. That is, it defines highly customisable
shapes that look like cobordisms between circles, such as those
used in TQFT and other mathematical diagrams.

%package -n texlive-tqft-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.1svn44455
Release:        0
Summary:        Documentation for texlive-tqft
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-tqft-doc
This package includes the documentation for texlive-tqft

%post -n texlive-tqft
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tqft 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tqft
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tqft-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/tqft/README
%{_texmfdistdir}/doc/latex/tqft/tqft.pdf
%{_texmfdistdir}/doc/latex/tqft/tqft_code.pdf
%{_texmfdistdir}/doc/latex/tqft/tqft_doc.tex

%files -n texlive-tqft
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/tqft/tikzlibrarytqft.code.tex
%{_texmfdistdir}/tex/latex/tqft/tqft.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-tqft-%{texlive_version}.%{texlive_noarch}.2.1svn44455-%{release}-zypper
%endif

%package -n texlive-tracklang
Version:        %{texlive_version}.%{texlive_noarch}.1.4svn52991
Release:        0
Summary:        Language and dialect tracker
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-tracklang-doc >= %{texlive_version}
Provides:       tex(tracklang-region-codes.tex)
Provides:       tex(tracklang-scripts.sty)
Provides:       tex(tracklang-scripts.tex)
Provides:       tex(tracklang.sty)
Provides:       tex(tracklang.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source147:      tracklang.tar.xz
Source148:      tracklang.doc.tar.xz

%description -n texlive-tracklang
The tracklang package is provided for package developers who
want a simple interface to find out which languages the user
has requested through packages such as babel or polyglossia.
This package does not provide any translations! Its purpose is
simply to track which languages have been requested by the
user. Generic TeX code is in tracklang.tex for non-LaTeX users.

%package -n texlive-tracklang-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.4svn52991
Release:        0
Summary:        Documentation for texlive-tracklang
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-tracklang-doc
This package includes the documentation for texlive-tracklang

%post -n texlive-tracklang
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tracklang 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tracklang
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tracklang-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/tracklang/CHANGES
%{_texmfdistdir}/doc/generic/tracklang/README
%{_texmfdistdir}/doc/generic/tracklang/samples/animals/animals-en-GB.ldf
%{_texmfdistdir}/doc/generic/tracklang/samples/animals/animals-en-US.ldf
%{_texmfdistdir}/doc/generic/tracklang/samples/animals/animals-english.ldf
%{_texmfdistdir}/doc/generic/tracklang/samples/animals/animals-german.ldf
%{_texmfdistdir}/doc/generic/tracklang/samples/animals/animals.sty
%{_texmfdistdir}/doc/generic/tracklang/samples/animals/animals2-en-GB.ldf
%{_texmfdistdir}/doc/generic/tracklang/samples/animals/animals2-en-US.ldf
%{_texmfdistdir}/doc/generic/tracklang/samples/animals/animals2-english.ldf
%{_texmfdistdir}/doc/generic/tracklang/samples/animals/animals2-german.ldf
%{_texmfdistdir}/doc/generic/tracklang/samples/animals/animals2.sty
%{_texmfdistdir}/doc/generic/tracklang/samples/animals/sample-animals-babel.pdf
%{_texmfdistdir}/doc/generic/tracklang/samples/animals/sample-animals-babel.tex
%{_texmfdistdir}/doc/generic/tracklang/samples/animals/sample-animals-de-poly.pdf
%{_texmfdistdir}/doc/generic/tracklang/samples/animals/sample-animals-de-poly.tex
%{_texmfdistdir}/doc/generic/tracklang/samples/animals/sample-animals-de.pdf
%{_texmfdistdir}/doc/generic/tracklang/samples/animals/sample-animals-de.tex
%{_texmfdistdir}/doc/generic/tracklang/samples/animals/sample-animals-poly.pdf
%{_texmfdistdir}/doc/generic/tracklang/samples/animals/sample-animals-poly.tex
%{_texmfdistdir}/doc/generic/tracklang/samples/animals/sample-animals.pdf
%{_texmfdistdir}/doc/generic/tracklang/samples/animals/sample-animals.tex
%{_texmfdistdir}/doc/generic/tracklang/samples/animals/sample-animals2-de.pdf
%{_texmfdistdir}/doc/generic/tracklang/samples/animals/sample-animals2-de.tex
%{_texmfdistdir}/doc/generic/tracklang/samples/animals/sample-animals2-de2.pdf
%{_texmfdistdir}/doc/generic/tracklang/samples/animals/sample-animals2-de2.tex
%{_texmfdistdir}/doc/generic/tracklang/samples/animals/sample-animals2-de3.pdf
%{_texmfdistdir}/doc/generic/tracklang/samples/animals/sample-animals2-de3.tex
%{_texmfdistdir}/doc/generic/tracklang/samples/animals/sample-animals2-de4.pdf
%{_texmfdistdir}/doc/generic/tracklang/samples/animals/sample-animals2-de4.tex
%{_texmfdistdir}/doc/generic/tracklang/samples/animals/sample-animals2-poly.pdf
%{_texmfdistdir}/doc/generic/tracklang/samples/animals/sample-animals2-poly.tex
%{_texmfdistdir}/doc/generic/tracklang/samples/animals/sample-animals2.pdf
%{_texmfdistdir}/doc/generic/tracklang/samples/animals/sample-animals2.tex
%{_texmfdistdir}/doc/generic/tracklang/samples/regions/regions-BE.ldf
%{_texmfdistdir}/doc/generic/tracklang/samples/regions/regions-CA.ldf
%{_texmfdistdir}/doc/generic/tracklang/samples/regions/regions-GB.ldf
%{_texmfdistdir}/doc/generic/tracklang/samples/regions/regions-IM.ldf
%{_texmfdistdir}/doc/generic/tracklang/samples/regions/regions-US.ldf
%{_texmfdistdir}/doc/generic/tracklang/samples/regions/regions-dutch.ldf
%{_texmfdistdir}/doc/generic/tracklang/samples/regions/regions-english.ldf
%{_texmfdistdir}/doc/generic/tracklang/samples/regions/regions-french.ldf
%{_texmfdistdir}/doc/generic/tracklang/samples/regions/regions-german.ldf
%{_texmfdistdir}/doc/generic/tracklang/samples/regions/regions-italian.ldf
%{_texmfdistdir}/doc/generic/tracklang/samples/regions/regions-manx.ldf
%{_texmfdistdir}/doc/generic/tracklang/samples/regions/regions.sty
%{_texmfdistdir}/doc/generic/tracklang/samples/regions/regions2.sty
%{_texmfdistdir}/doc/generic/tracklang/samples/regions/sample-regions.pdf
%{_texmfdistdir}/doc/generic/tracklang/samples/regions/sample-regions.tex
%{_texmfdistdir}/doc/generic/tracklang/samples/regions/sample-regions2-manx.pdf
%{_texmfdistdir}/doc/generic/tracklang/samples/regions/sample-regions2-manx.tex
%{_texmfdistdir}/doc/generic/tracklang/samples/regions/sample-regions2-map.pdf
%{_texmfdistdir}/doc/generic/tracklang/samples/regions/sample-regions2-map.tex
%{_texmfdistdir}/doc/generic/tracklang/samples/regions/sample-regions2-map2.pdf
%{_texmfdistdir}/doc/generic/tracklang/samples/regions/sample-regions2-map2.tex
%{_texmfdistdir}/doc/generic/tracklang/samples/regions/sample-regions2-map3.pdf
%{_texmfdistdir}/doc/generic/tracklang/samples/regions/sample-regions2-map3.tex
%{_texmfdistdir}/doc/generic/tracklang/samples/regions/sample-regions2-nomap.pdf
%{_texmfdistdir}/doc/generic/tracklang/samples/regions/sample-regions2-nomap.tex
%{_texmfdistdir}/doc/generic/tracklang/samples/regions/sample-regions2.pdf
%{_texmfdistdir}/doc/generic/tracklang/samples/regions/sample-regions2.tex
%{_texmfdistdir}/doc/generic/tracklang/samples/sample-tracklang.pdf
%{_texmfdistdir}/doc/generic/tracklang/samples/sample-tracklang.tex
%{_texmfdistdir}/doc/generic/tracklang/samples/sample-tracklang2.pdf
%{_texmfdistdir}/doc/generic/tracklang/samples/sample-tracklang2.tex
%{_texmfdistdir}/doc/generic/tracklang/samples/sample-tracklang3.pdf
%{_texmfdistdir}/doc/generic/tracklang/samples/sample-tracklang3.tex
%{_texmfdistdir}/doc/generic/tracklang/samples/sample-tracklang4.pdf
%{_texmfdistdir}/doc/generic/tracklang/samples/sample-tracklang4.tex
%{_texmfdistdir}/doc/generic/tracklang/samples/sample-tracklang5.pdf
%{_texmfdistdir}/doc/generic/tracklang/samples/sample-tracklang5.tex
%{_texmfdistdir}/doc/generic/tracklang/samples/sample-tracklang6.pdf
%{_texmfdistdir}/doc/generic/tracklang/samples/sample-tracklang6.tex
%{_texmfdistdir}/doc/generic/tracklang/tracklang.pdf

%files -n texlive-tracklang
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/tracklang/tracklang-region-codes.tex
%{_texmfdistdir}/tex/generic/tracklang/tracklang-scripts.tex
%{_texmfdistdir}/tex/generic/tracklang/tracklang.tex
%{_texmfdistdir}/tex/latex/tracklang/tracklang-scripts.sty
%{_texmfdistdir}/tex/latex/tracklang/tracklang.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-tracklang-%{texlive_version}.%{texlive_noarch}.1.4svn52991-%{release}-zypper
%endif

%package -n texlive-trajan
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn15878
Release:        0
Summary:        Fonts from the Trajan column in Rome
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
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
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Requires:       texlive-trajan-fonts >= %{texlive_version}
Recommends:     texlive-trajan-doc >= %{texlive_version}
Provides:       tex(t1trjn.fd)
Provides:       tex(trajan.map)
Provides:       tex(trajan.sty)
Provides:       tex(trjnr10.tfm)
Provides:       tex(trjnsl10.tfm)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source149:      trajan.tar.xz
Source150:      trajan.doc.tar.xz

%description -n texlive-trajan
Provides fonts (both as Metafont source and in Adobe Type 1
format) based on the capitals carved on the Trajan column in
Rome in 114 AD, together with macros to access the fonts. Many
typographers think these rank first among the Roman's artistic
legacy. The font is uppercase letters together with some
punctuation and analphabetics; no lowercase or digits.

%package -n texlive-trajan-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn15878
Release:        0
Summary:        Documentation for texlive-trajan
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-trajan-doc
This package includes the documentation for texlive-trajan


%package -n texlive-trajan-fonts
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn15878
Release:        0
Summary:        Severed fonts for texlive-trajan
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Fonts
URL:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-trajan-fonts
The  separated fonts package for texlive-trajan
%post -n texlive-trajan
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMixedMap trajan.map' >> /var/run/texlive/run-updmap

%postun -n texlive-trajan 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMixedMap trajan.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-trajan
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-trajan-fonts
%files -n texlive-trajan-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/trajan/README
%{_texmfdistdir}/doc/latex/trajan/trajan.pdf
%{_texmfdistdir}/doc/latex/trajan/trytrajan.pdf
%{_texmfdistdir}/doc/latex/trajan/trytrajan.tex

%files -n texlive-trajan
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/afm/public/trajan/trjnr10.afm
%{_texmfdistdir}/fonts/afm/public/trajan/trjnsl10.afm
%{_texmfdistdir}/fonts/map/dvips/trajan/trajan.map
%{_texmfdistdir}/fonts/tfm/public/trajan/trjnr10.tfm
%{_texmfdistdir}/fonts/tfm/public/trajan/trjnsl10.tfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/trajan/trjnr10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/trajan/trjnsl10.pfb
%{_texmfdistdir}/tex/latex/trajan/t1trjn.fd
%{_texmfdistdir}/tex/latex/trajan/trajan.sty

%files -n texlive-trajan-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-trajan
%{_datadir}/fontconfig/conf.avail/58-texlive-trajan.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-trajan/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-trajan/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-trajan/fonts.scale
%{_datadir}/fonts/texlive-trajan/trjnr10.pfb
%{_datadir}/fonts/texlive-trajan/trjnsl10.pfb
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-trajan-fonts-%{texlive_version}.%{texlive_noarch}.1.1svn15878-%{release}-zypper
%endif

%package -n texlive-tram
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2svn29803
Release:        0
Summary:        Typeset tram boxes in LaTeX
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-tram-doc >= %{texlive_version}
Provides:       tex(tram.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source151:      tram.tar.xz
Source152:      tram.doc.tar.xz

%description -n texlive-tram
Tram boxes are highlighted with patterns of dots; the package
defines an environment tram that typesets its content into a
tram box. The pattern used may be selected in an optional
argument to the environment.

%package -n texlive-tram-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2svn29803
Release:        0
Summary:        Documentation for texlive-tram
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-tram-doc
This package includes the documentation for texlive-tram

%post -n texlive-tram
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tram 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tram
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tram-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/tram/README
%{_texmfdistdir}/doc/latex/tram/tram-doc.pdf
%{_texmfdistdir}/doc/latex/tram/tram-doc.tex

%files -n texlive-tram
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/source/public/tram/tram.mf
%{_texmfdistdir}/tex/latex/tram/tram.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-tram-%{texlive_version}.%{texlive_noarch}.0.0.2svn29803-%{release}-zypper
%endif

%package -n texlive-translation-array-fr
Version:        %{texlive_version}.%{texlive_noarch}.svn24344
Release:        0
Summary:        French translation of the documentation of array
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source153:      translation-array-fr.doc.tar.xz

%description -n texlive-translation-array-fr
A French translation of the documentation of array.
%post -n texlive-translation-array-fr
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-translation-array-fr 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-translation-array-fr
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-translation-array-fr
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/translation-array-fr/Copyright
%{_texmfdistdir}/doc/latex/translation-array-fr/README
%{_texmfdistdir}/doc/latex/translation-array-fr/f-array.dtx
%{_texmfdistdir}/doc/latex/translation-array-fr/f-array.pdf
%{_texmfdistdir}/doc/latex/translation-array-fr/ltxdoc.cfg
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-translation-array-fr-%{texlive_version}.%{texlive_noarch}.svn24344-%{release}-zypper
%endif

%package -n texlive-translation-arsclassica-de
Version:        %{texlive_version}.%{texlive_noarch}.svn23803
Release:        0
Summary:        German version of arsclassica
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source154:      translation-arsclassica-de.doc.tar.xz

%description -n texlive-translation-arsclassica-de
This is a "translation" of the arsclassica documentation.
%post -n texlive-translation-arsclassica-de
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-translation-arsclassica-de 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-translation-arsclassica-de
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-translation-arsclassica-de
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/translation-arsclassica-de/ArsClassica-de.pdf
%{_texmfdistdir}/doc/latex/translation-arsclassica-de/ArsClassica-de.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-translation-arsclassica-de-%{texlive_version}.%{texlive_noarch}.svn23803-%{release}-zypper
%endif

%package -n texlive-translation-biblatex-de
Version:        %{texlive_version}.%{texlive_noarch}.3.0svn45592
Release:        0
Summary:        German translation of the User Guide of BibLaTeX
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source155:      translation-biblatex-de.doc.tar.xz

%description -n texlive-translation-biblatex-de
A German translation of the User Guide of BibLaTeX.
%post -n texlive-translation-biblatex-de
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-translation-biblatex-de 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-translation-biblatex-de
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-translation-biblatex-de
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/translation-biblatex-de/README
%{_texmfdistdir}/doc/latex/translation-biblatex-de/biblatex-de-Benutzerhandbuch.pdf
%{_texmfdistdir}/doc/latex/translation-biblatex-de/biblatex-de-Benutzerhandbuch.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-translation-biblatex-de-%{texlive_version}.%{texlive_noarch}.3.0svn45592-%{release}-zypper
%endif

%package -n texlive-translation-chemsym-de
Version:        %{texlive_version}.%{texlive_noarch}.svn23804
Release:        0
Summary:        German version of chemsym
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source156:      translation-chemsym-de.doc.tar.xz

%description -n texlive-translation-chemsym-de
This is a "translation" of the chemsym documentation.
%post -n texlive-translation-chemsym-de
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-translation-chemsym-de 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-translation-chemsym-de
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-translation-chemsym-de
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/translation-chemsym-de/00Liesmich.chs
%{_texmfdistdir}/doc/latex/translation-chemsym-de/chemsym-de.dtx
%{_texmfdistdir}/doc/latex/translation-chemsym-de/chemsym-de.pdf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-translation-chemsym-de-%{texlive_version}.%{texlive_noarch}.svn23804-%{release}-zypper
%endif

%package -n texlive-translation-dcolumn-fr
Version:        %{texlive_version}.%{texlive_noarch}.svn24345
Release:        0
Summary:        French translation of the documentation of dcolumn
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source157:      translation-dcolumn-fr.doc.tar.xz

%description -n texlive-translation-dcolumn-fr
A French translation of the documentation of dcolumn.
%post -n texlive-translation-dcolumn-fr
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-translation-dcolumn-fr 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-translation-dcolumn-fr
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-translation-dcolumn-fr
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/translation-dcolumn-fr/Copyright
%{_texmfdistdir}/doc/latex/translation-dcolumn-fr/README
%{_texmfdistdir}/doc/latex/translation-dcolumn-fr/f-dcolumn.dtx
%{_texmfdistdir}/doc/latex/translation-dcolumn-fr/f-dcolumn.pdf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-translation-dcolumn-fr-%{texlive_version}.%{texlive_noarch}.svn24345-%{release}-zypper
%endif

%package -n texlive-translation-ecv-de
Version:        %{texlive_version}.%{texlive_noarch}.svn24754
Release:        0
Summary:        Ecv documentation, in German
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source158:      translation-ecv-de.doc.tar.xz

%description -n texlive-translation-ecv-de
This is a "translation" of the ecv documentation.
%post -n texlive-translation-ecv-de
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-translation-ecv-de 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-translation-ecv-de
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-translation-ecv-de
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/translation-ecv-de/ecvde.dtx.pdf
%{_texmfdistdir}/doc/latex/translation-ecv-de/ecvde.dtx.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-translation-ecv-de-%{texlive_version}.%{texlive_noarch}.svn24754-%{release}-zypper
%endif

%package -n texlive-translation-enumitem-de
Version:        %{texlive_version}.%{texlive_noarch}.svn24196
Release:        0
Summary:        Enumitem documentation, in German
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source159:      translation-enumitem-de.doc.tar.xz

%description -n texlive-translation-enumitem-de
This is a translation of the manual for enumitem.
%post -n texlive-translation-enumitem-de
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-translation-enumitem-de 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-translation-enumitem-de
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-translation-enumitem-de
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/translation-enumitem-de/enumitem-de.pdf
%{_texmfdistdir}/doc/latex/translation-enumitem-de/enumitem-de.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-translation-enumitem-de-%{texlive_version}.%{texlive_noarch}.svn24196-%{release}-zypper
%endif

%package -n texlive-translation-europecv-de
Version:        %{texlive_version}.%{texlive_noarch}.svn23840
Release:        0
Summary:        German version of europecv
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source160:      translation-europecv-de.doc.tar.xz

%description -n texlive-translation-europecv-de
This is a "translation" of the europecv documentation.
%post -n texlive-translation-europecv-de
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-translation-europecv-de 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-translation-europecv-de
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-translation-europecv-de
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/translation-europecv-de/Beispiele/at.pdf
%{_texmfdistdir}/doc/latex/translation-europecv-de/Beispiele/bulgarian-koi8-r.tex
%{_texmfdistdir}/doc/latex/translation-europecv-de/Beispiele/bulgarian-utf8.tex
%{_texmfdistdir}/doc/latex/translation-europecv-de/Beispiele/greek-utf8.pdf
%{_texmfdistdir}/doc/latex/translation-europecv-de/Beispiele/greek-utf8.tex
%{_texmfdistdir}/doc/latex/translation-europecv-de/Beispiele/maltese-maltese.tex
%{_texmfdistdir}/doc/latex/translation-europecv-de/Beispiele/maltese-utf8.tex
%{_texmfdistdir}/doc/latex/translation-europecv-de/Beispiele/minimal.pdf
%{_texmfdistdir}/doc/latex/translation-europecv-de/Beispiele/minimal.tex
%{_texmfdistdir}/doc/latex/translation-europecv-de/europecv-de.pdf
%{_texmfdistdir}/doc/latex/translation-europecv-de/europecv-de.tex
%{_texmfdistdir}/doc/latex/translation-europecv-de/templates/cv_template_de.pdf
%{_texmfdistdir}/doc/latex/translation-europecv-de/templates/cv_template_de.tex
%{_texmfdistdir}/doc/latex/translation-europecv-de/templates/cv_template_en.pdf
%{_texmfdistdir}/doc/latex/translation-europecv-de/templates/cv_template_en.tex
%{_texmfdistdir}/doc/latex/translation-europecv-de/templates/cv_template_it.pdf
%{_texmfdistdir}/doc/latex/translation-europecv-de/templates/cv_template_it.tex
%{_texmfdistdir}/doc/latex/translation-europecv-de/templates/cv_template_pl.pdf
%{_texmfdistdir}/doc/latex/translation-europecv-de/templates/cv_template_pl.tex
%{_texmfdistdir}/doc/latex/translation-europecv-de/templates/publications.bib
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-translation-europecv-de-%{texlive_version}.%{texlive_noarch}.svn23840-%{release}-zypper
%endif

%package -n texlive-translation-filecontents-de
Version:        %{texlive_version}.%{texlive_noarch}.svn24010
Release:        0
Summary:        German version of filecontents
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source161:      translation-filecontents-de.doc.tar.xz

%description -n texlive-translation-filecontents-de
This is a "translation" of the filecontents documentation.
%post -n texlive-translation-filecontents-de
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-translation-filecontents-de 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-translation-filecontents-de
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-translation-filecontents-de
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/translation-filecontents-de/filecontents-de.dtx
%{_texmfdistdir}/doc/latex/translation-filecontents-de/filecontents-de.ins
%{_texmfdistdir}/doc/latex/translation-filecontents-de/filecontents-de.pdf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-translation-filecontents-de-%{texlive_version}.%{texlive_noarch}.svn24010-%{release}-zypper
%endif

%package -n texlive-translation-moreverb-de
Version:        %{texlive_version}.%{texlive_noarch}.svn23957
Release:        0
Summary:        German version of moreverb
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source162:      translation-moreverb-de.doc.tar.xz

%description -n texlive-translation-moreverb-de
This is a "translation" of the moreverb documentation.
%post -n texlive-translation-moreverb-de
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-translation-moreverb-de 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-translation-moreverb-de
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-translation-moreverb-de
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/translation-moreverb-de/filecontens-de.ins.txt
%{_texmfdistdir}/doc/latex/translation-moreverb-de/moreverb-de.dtx.pdf
%{_texmfdistdir}/doc/latex/translation-moreverb-de/moreverb-de.dtx.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-translation-moreverb-de-%{texlive_version}.%{texlive_noarch}.svn23957-%{release}-zypper
%endif

%package -n texlive-translation-natbib-fr
Version:        %{texlive_version}.%{texlive_noarch}.svn25105
Release:        0
Summary:        French translation of the documentation of natbib
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source163:      translation-natbib-fr.doc.tar.xz

%description -n texlive-translation-natbib-fr
A French translation of the documentation of natbib.
%post -n texlive-translation-natbib-fr
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-translation-natbib-fr 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-translation-natbib-fr
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-translation-natbib-fr
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/translation-natbib-fr/f-natbib.dtx
%{_texmfdistdir}/doc/latex/translation-natbib-fr/f-natbib.pdf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-translation-natbib-fr-%{texlive_version}.%{texlive_noarch}.svn25105-%{release}-zypper
%endif

%package -n texlive-translation-tabbing-fr
Version:        %{texlive_version}.%{texlive_noarch}.svn24228
Release:        0
Summary:        French translation of the documentation of Tabbing
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source164:      translation-tabbing-fr.doc.tar.xz

%description -n texlive-translation-tabbing-fr
A translation to French (by the author) of the documentation of
the Tabbing package.
%post -n texlive-translation-tabbing-fr
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-translation-tabbing-fr 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-translation-tabbing-fr
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-translation-tabbing-fr
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/translation-tabbing-fr/f-Tabbing.dtx
%{_texmfdistdir}/doc/latex/translation-tabbing-fr/f-Tabbing.pdf
%{_texmfdistdir}/doc/latex/translation-tabbing-fr/ltxdoc.cfg
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-translation-tabbing-fr-%{texlive_version}.%{texlive_noarch}.svn24228-%{release}-zypper
%endif

%package -n texlive-translations
Version:        %{texlive_version}.%{texlive_noarch}.1.8svn53962
Release:        0
Summary:        Internationalisation of LaTeX2e packages
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-translations-doc >= %{texlive_version}
Provides:       tex(translations.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(pdftexcmds.sty)
Requires:       tex(scrlfile.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source165:      translations.tar.xz
Source166:      translations.doc.tar.xz

%description -n texlive-translations
This package (once part of the exsheets package), provides a
framework for providing multilingual features to a LaTeX
package. The package has its own basic dictionaries for
English, Dutch, French, German and Spanish; it aims to use
translation material for English, Dutch, French, German,
Italian, Spanish, Catalan, Turkish, Croatian, Hungarian, Danish
and Portuguese from babel or polyglossia if either is in use in
the document. (Additional languages from the multilingual
packages may be possible: ask the author.)

%package -n texlive-translations-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.8svn53962
Release:        0
Summary:        Documentation for texlive-translations
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-translations-doc:en)

%description -n texlive-translations-doc
This package includes the documentation for texlive-translations

%post -n texlive-translations
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-translations 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-translations
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-translations-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/translations/README
%{_texmfdistdir}/doc/latex/translations/translations_en.pdf
%{_texmfdistdir}/doc/latex/translations/translations_en.tex

%files -n texlive-translations
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/translations/translations-basic-dictionary-catalan.trsl
%{_texmfdistdir}/tex/latex/translations/translations-basic-dictionary-dutch.trsl
%{_texmfdistdir}/tex/latex/translations/translations-basic-dictionary-english.trsl
%{_texmfdistdir}/tex/latex/translations/translations-basic-dictionary-french.trsl
%{_texmfdistdir}/tex/latex/translations/translations-basic-dictionary-german.trsl
%{_texmfdistdir}/tex/latex/translations/translations-basic-dictionary-spanish.trsl
%{_texmfdistdir}/tex/latex/translations/translations.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-translations-%{texlive_version}.%{texlive_noarch}.1.8svn53962-%{release}-zypper
%endif

%package -n texlive-translator
Version:        %{texlive_version}.%{texlive_noarch}.1.12asvn54512
Release:        0
Summary:        Easy translation of strings in LaTeX
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-translator-doc >= %{texlive_version}
Provides:       tex(translator.sty)
Requires:       tex(keyval.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source167:      translator.tar.xz
Source168:      translator.doc.tar.xz

%description -n texlive-translator
This LaTeX package provides a flexible mechanism for
translating individual words into different languages. For
example, it can be used to translate a word like "figure" into,
say, the German word "Abbildung". Such a translation mechanism
is useful when the author of some package would like to
localize the package such that texts are correctly translated
into the language preferred by the user. This package is not
intended to be used to automatically translate more than a few
words.

%package -n texlive-translator-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.12asvn54512
Release:        0
Summary:        Documentation for texlive-translator
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-translator-doc
This package includes the documentation for texlive-translator

%post -n texlive-translator
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-translator 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-translator
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-translator-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/translator/README.md
%{_texmfdistdir}/doc/latex/translator/translator.pdf
%{_texmfdistdir}/doc/latex/translator/translator.tex

%files -n texlive-translator
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/translator/translator-basic-dictionary-Bulgarian.dict
%{_texmfdistdir}/tex/latex/translator/translator-basic-dictionary-Catalan.dict
%{_texmfdistdir}/tex/latex/translator/translator-basic-dictionary-Croatian.dict
%{_texmfdistdir}/tex/latex/translator/translator-basic-dictionary-Danish.dict
%{_texmfdistdir}/tex/latex/translator/translator-basic-dictionary-English.dict
%{_texmfdistdir}/tex/latex/translator/translator-basic-dictionary-French.dict
%{_texmfdistdir}/tex/latex/translator/translator-basic-dictionary-German.dict
%{_texmfdistdir}/tex/latex/translator/translator-basic-dictionary-Greek.dict
%{_texmfdistdir}/tex/latex/translator/translator-basic-dictionary-Italian.dict
%{_texmfdistdir}/tex/latex/translator/translator-basic-dictionary-Norsk.dict
%{_texmfdistdir}/tex/latex/translator/translator-basic-dictionary-Nynorsk.dict
%{_texmfdistdir}/tex/latex/translator/translator-basic-dictionary-Polish.dict
%{_texmfdistdir}/tex/latex/translator/translator-basic-dictionary-Portuguese.dict
%{_texmfdistdir}/tex/latex/translator/translator-basic-dictionary-Russian.dict
%{_texmfdistdir}/tex/latex/translator/translator-basic-dictionary-Serbian.dict
%{_texmfdistdir}/tex/latex/translator/translator-basic-dictionary-Spanish.dict
%{_texmfdistdir}/tex/latex/translator/translator-basic-dictionary-Swedish.dict
%{_texmfdistdir}/tex/latex/translator/translator-basic-dictionary-Turkish.dict
%{_texmfdistdir}/tex/latex/translator/translator-bibliography-dictionary-Bulgarian.dict
%{_texmfdistdir}/tex/latex/translator/translator-bibliography-dictionary-Catalan.dict
%{_texmfdistdir}/tex/latex/translator/translator-bibliography-dictionary-Croatian.dict
%{_texmfdistdir}/tex/latex/translator/translator-bibliography-dictionary-Danish.dict
%{_texmfdistdir}/tex/latex/translator/translator-bibliography-dictionary-English.dict
%{_texmfdistdir}/tex/latex/translator/translator-bibliography-dictionary-French.dict
%{_texmfdistdir}/tex/latex/translator/translator-bibliography-dictionary-German.dict
%{_texmfdistdir}/tex/latex/translator/translator-bibliography-dictionary-Greek.dict
%{_texmfdistdir}/tex/latex/translator/translator-bibliography-dictionary-Italian.dict
%{_texmfdistdir}/tex/latex/translator/translator-bibliography-dictionary-Polish.dict
%{_texmfdistdir}/tex/latex/translator/translator-bibliography-dictionary-Portuguese.dict
%{_texmfdistdir}/tex/latex/translator/translator-bibliography-dictionary-Russian.dict
%{_texmfdistdir}/tex/latex/translator/translator-bibliography-dictionary-Serbian.dict
%{_texmfdistdir}/tex/latex/translator/translator-bibliography-dictionary-Spanish.dict
%{_texmfdistdir}/tex/latex/translator/translator-bibliography-dictionary-Swedish.dict
%{_texmfdistdir}/tex/latex/translator/translator-bibliography-dictionary-Turkish.dict
%{_texmfdistdir}/tex/latex/translator/translator-environment-dictionary-Bulgarian.dict
%{_texmfdistdir}/tex/latex/translator/translator-environment-dictionary-Catalan.dict
%{_texmfdistdir}/tex/latex/translator/translator-environment-dictionary-Croatian.dict
%{_texmfdistdir}/tex/latex/translator/translator-environment-dictionary-Danish.dict
%{_texmfdistdir}/tex/latex/translator/translator-environment-dictionary-English.dict
%{_texmfdistdir}/tex/latex/translator/translator-environment-dictionary-French.dict
%{_texmfdistdir}/tex/latex/translator/translator-environment-dictionary-German.dict
%{_texmfdistdir}/tex/latex/translator/translator-environment-dictionary-Greek.dict
%{_texmfdistdir}/tex/latex/translator/translator-environment-dictionary-Italian.dict
%{_texmfdistdir}/tex/latex/translator/translator-environment-dictionary-Polish.dict
%{_texmfdistdir}/tex/latex/translator/translator-environment-dictionary-Portuguese.dict
%{_texmfdistdir}/tex/latex/translator/translator-environment-dictionary-Russian.dict
%{_texmfdistdir}/tex/latex/translator/translator-environment-dictionary-Serbian.dict
%{_texmfdistdir}/tex/latex/translator/translator-environment-dictionary-Spanish.dict
%{_texmfdistdir}/tex/latex/translator/translator-environment-dictionary-Swedish.dict
%{_texmfdistdir}/tex/latex/translator/translator-environment-dictionary-Turkish.dict
%{_texmfdistdir}/tex/latex/translator/translator-months-dictionary-Bulgarian.dict
%{_texmfdistdir}/tex/latex/translator/translator-months-dictionary-Catalan.dict
%{_texmfdistdir}/tex/latex/translator/translator-months-dictionary-Croatian.dict
%{_texmfdistdir}/tex/latex/translator/translator-months-dictionary-Danish.dict
%{_texmfdistdir}/tex/latex/translator/translator-months-dictionary-English.dict
%{_texmfdistdir}/tex/latex/translator/translator-months-dictionary-French.dict
%{_texmfdistdir}/tex/latex/translator/translator-months-dictionary-German.dict
%{_texmfdistdir}/tex/latex/translator/translator-months-dictionary-Greek.dict
%{_texmfdistdir}/tex/latex/translator/translator-months-dictionary-Italian.dict
%{_texmfdistdir}/tex/latex/translator/translator-months-dictionary-Norsk.dict
%{_texmfdistdir}/tex/latex/translator/translator-months-dictionary-Nynorsk.dict
%{_texmfdistdir}/tex/latex/translator/translator-months-dictionary-Polish.dict
%{_texmfdistdir}/tex/latex/translator/translator-months-dictionary-Portuguese.dict
%{_texmfdistdir}/tex/latex/translator/translator-months-dictionary-Russian.dict
%{_texmfdistdir}/tex/latex/translator/translator-months-dictionary-Serbian.dict
%{_texmfdistdir}/tex/latex/translator/translator-months-dictionary-Spanish.dict
%{_texmfdistdir}/tex/latex/translator/translator-months-dictionary-Swedish.dict
%{_texmfdistdir}/tex/latex/translator/translator-months-dictionary-Turkish.dict
%{_texmfdistdir}/tex/latex/translator/translator-numbers-dictionary-Bulgarian.dict
%{_texmfdistdir}/tex/latex/translator/translator-numbers-dictionary-Catalan.dict
%{_texmfdistdir}/tex/latex/translator/translator-numbers-dictionary-Croatian.dict
%{_texmfdistdir}/tex/latex/translator/translator-numbers-dictionary-Danish.dict
%{_texmfdistdir}/tex/latex/translator/translator-numbers-dictionary-English.dict
%{_texmfdistdir}/tex/latex/translator/translator-numbers-dictionary-French.dict
%{_texmfdistdir}/tex/latex/translator/translator-numbers-dictionary-German.dict
%{_texmfdistdir}/tex/latex/translator/translator-numbers-dictionary-Greek.dict
%{_texmfdistdir}/tex/latex/translator/translator-numbers-dictionary-Italian.dict
%{_texmfdistdir}/tex/latex/translator/translator-numbers-dictionary-Norsk.dict
%{_texmfdistdir}/tex/latex/translator/translator-numbers-dictionary-Nynorsk.dict
%{_texmfdistdir}/tex/latex/translator/translator-numbers-dictionary-Polish.dict
%{_texmfdistdir}/tex/latex/translator/translator-numbers-dictionary-Portuguese.dict
%{_texmfdistdir}/tex/latex/translator/translator-numbers-dictionary-Russian.dict
%{_texmfdistdir}/tex/latex/translator/translator-numbers-dictionary-Serbian.dict
%{_texmfdistdir}/tex/latex/translator/translator-numbers-dictionary-Spanish.dict
%{_texmfdistdir}/tex/latex/translator/translator-numbers-dictionary-Swedish.dict
%{_texmfdistdir}/tex/latex/translator/translator-numbers-dictionary-Turkish.dict
%{_texmfdistdir}/tex/latex/translator/translator-theorem-dictionary-Bulgarian.dict
%{_texmfdistdir}/tex/latex/translator/translator-theorem-dictionary-Catalan.dict
%{_texmfdistdir}/tex/latex/translator/translator-theorem-dictionary-Croatian.dict
%{_texmfdistdir}/tex/latex/translator/translator-theorem-dictionary-Danish.dict
%{_texmfdistdir}/tex/latex/translator/translator-theorem-dictionary-English.dict
%{_texmfdistdir}/tex/latex/translator/translator-theorem-dictionary-French.dict
%{_texmfdistdir}/tex/latex/translator/translator-theorem-dictionary-German.dict
%{_texmfdistdir}/tex/latex/translator/translator-theorem-dictionary-Greek.dict
%{_texmfdistdir}/tex/latex/translator/translator-theorem-dictionary-Italian.dict
%{_texmfdistdir}/tex/latex/translator/translator-theorem-dictionary-Norsk.dict
%{_texmfdistdir}/tex/latex/translator/translator-theorem-dictionary-Polish.dict
%{_texmfdistdir}/tex/latex/translator/translator-theorem-dictionary-Portuguese.dict
%{_texmfdistdir}/tex/latex/translator/translator-theorem-dictionary-Russian.dict
%{_texmfdistdir}/tex/latex/translator/translator-theorem-dictionary-Serbian.dict
%{_texmfdistdir}/tex/latex/translator/translator-theorem-dictionary-Spanish.dict
%{_texmfdistdir}/tex/latex/translator/translator-theorem-dictionary-Swedish.dict
%{_texmfdistdir}/tex/latex/translator/translator-theorem-dictionary-Turkish.dict
%{_texmfdistdir}/tex/latex/translator/translator.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-translator-%{texlive_version}.%{texlive_noarch}.1.12asvn54512-%{release}-zypper
%endif

%package -n texlive-transparent
Version:        %{texlive_version}.%{texlive_noarch}.1.4svn52981
Release:        0
Summary:        Using a color stack for transparency with pdfTeX
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-transparent-doc >= %{texlive_version}
Provides:       tex(transparent.sty)
Requires:       tex(auxhook.sty)
Requires:       tex(iftex.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source169:      transparent.tar.xz
Source170:      transparent.doc.tar.xz

%description -n texlive-transparent
Since version 1.40 pdfTeX supports several color stacks; the
package uses a separate colour stack for control of
transparency (which is not, of course, a colour).

%package -n texlive-transparent-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.4svn52981
Release:        0
Summary:        Documentation for texlive-transparent
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-transparent-doc
This package includes the documentation for texlive-transparent

%post -n texlive-transparent
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-transparent 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-transparent
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-transparent-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/transparent/README.md
%{_texmfdistdir}/doc/latex/transparent/transparent-example.tex
%{_texmfdistdir}/doc/latex/transparent/transparent.pdf

%files -n texlive-transparent
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/transparent/transparent.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-transparent-%{texlive_version}.%{texlive_noarch}.1.4svn52981-%{release}-zypper
%endif

%package -n texlive-tree-dvips
Version:        %{texlive_version}.%{texlive_noarch}.0.0.91svn21751
Release:        0
Summary:        Trees and other linguists' macros
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-tree-dvips-doc >= %{texlive_version}
Provides:       tex(lingmacros.sty)
Provides:       tex(tree-dvips.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source171:      tree-dvips.tar.xz
Source172:      tree-dvips.doc.tar.xz

%description -n texlive-tree-dvips
The package defines a mechanism for specifying connected trees
that uses a tabular environment to generate node positions. The
package uses PostScript code, loaded by dvips, so output can
only be generated by use of dvips. The package lingmacros.sty
defines a few macros for linguists: \enumsentence for
enumerating sentence examples, simple tabular-based
non-connected tree macros, and gloss macros.

%package -n texlive-tree-dvips-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.91svn21751
Release:        0
Summary:        Documentation for texlive-tree-dvips
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-tree-dvips-doc
This package includes the documentation for texlive-tree-dvips

%post -n texlive-tree-dvips
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tree-dvips 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tree-dvips
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tree-dvips-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/tree-dvips/Makefile
%{_texmfdistdir}/doc/latex/tree-dvips/README
%{_texmfdistdir}/doc/latex/tree-dvips/README.TEXLIVE
%{_texmfdistdir}/doc/latex/tree-dvips/lingmacros-manual.pdf
%{_texmfdistdir}/doc/latex/tree-dvips/lingmacros-manual.tex
%{_texmfdistdir}/doc/latex/tree-dvips/tree-dvips91.script
%{_texmfdistdir}/doc/latex/tree-dvips/tree-manual.pdf
%{_texmfdistdir}/doc/latex/tree-dvips/tree-manual.tex

%files -n texlive-tree-dvips
%defattr(-,root,root,755)
%{_texmfdistdir}/dvips/tree-dvips/tree-dvips91.pro
%{_texmfdistdir}/tex/latex/tree-dvips/lingmacros.sty
%{_texmfdistdir}/tex/latex/tree-dvips/tree-dvips.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-tree-dvips-%{texlive_version}.%{texlive_noarch}.0.0.91svn21751-%{release}-zypper
%endif

%package -n texlive-treetex
Version:        %{texlive_version}.%{texlive_noarch}.svn28176
Release:        0
Summary:        Draw trees
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-treetex-doc >= %{texlive_version}
Provides:       tex(classes.tex)
Provides:       tex(l_pic.tex)
Provides:       tex(treetex.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source173:      treetex.tar.xz
Source174:      treetex.doc.tar.xz

%description -n texlive-treetex
Macros to draw trees, within TeX (or LaTeX). The algorithm used
is discussed in an accompanying paper (written using LaTeX
2.09).

%package -n texlive-treetex-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn28176
Release:        0
Summary:        Documentation for texlive-treetex
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-treetex-doc
This package includes the documentation for texlive-treetex

%post -n texlive-treetex
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-treetex 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-treetex
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-treetex-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/plain/treetex/epodd.tex
%{_texmfdistdir}/doc/plain/treetex/readme
%{_texmfdistdir}/doc/plain/treetex/tree_doc.tex

%files -n texlive-treetex
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/plain/treetex/classes.tex
%{_texmfdistdir}/tex/plain/treetex/l_pic.tex
%{_texmfdistdir}/tex/plain/treetex/treetex.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-treetex-%{texlive_version}.%{texlive_noarch}.svn28176-%{release}-zypper
%endif

%package -n texlive-trfsigns
Version:        %{texlive_version}.%{texlive_noarch}.1.01svn15878
Release:        0
Summary:        Typeset transform signs
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-trfsigns-doc >= %{texlive_version}
Provides:       tex(trfsigns.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source175:      trfsigns.tar.xz
Source176:      trfsigns.doc.tar.xz

%description -n texlive-trfsigns
A package for typesetting various transformation signs for
Laplace transforms, Fourier transforms and others.

%package -n texlive-trfsigns-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.01svn15878
Release:        0
Summary:        Documentation for texlive-trfsigns
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-trfsigns-doc:de)

%description -n texlive-trfsigns-doc
This package includes the documentation for texlive-trfsigns

%post -n texlive-trfsigns
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-trfsigns 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-trfsigns
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-trfsigns-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/trfsigns/COPYING
%{_texmfdistdir}/doc/latex/trfsigns/README
%{_texmfdistdir}/doc/latex/trfsigns/trfexamp.tex
%{_texmfdistdir}/doc/latex/trfsigns/trfsigns.pdf

%files -n texlive-trfsigns
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/trfsigns/trfsigns.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-trfsigns-%{texlive_version}.%{texlive_noarch}.1.01svn15878-%{release}-zypper
%endif

%package -n texlive-trigonometry
Version:        %{texlive_version}.%{texlive_noarch}.svn43006
Release:        0
Summary:        Demonstration code for cos and sin in TeX macros
License:        SUSE-TeX
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-trigonometry-doc >= %{texlive_version}
Provides:       tex(trigonometry.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source177:      trigonometry.tar.xz
Source178:      trigonometry.doc.tar.xz

%description -n texlive-trigonometry
A document that both provides macros that are usable elsewhere,
and demonstrates the macros. The code uses the "classical"
analytical expansion of sin and cos (the more recent trig uses
a "numerical analyst's" expansion).

%package -n texlive-trigonometry-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn43006
Release:        0
Summary:        Documentation for texlive-trigonometry
License:        SUSE-TeX
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-trigonometry-doc
This package includes the documentation for texlive-trigonometry

%post -n texlive-trigonometry
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-trigonometry 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-trigonometry
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-trigonometry-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/trigonometry/README.txt

%files -n texlive-trigonometry
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/trigonometry/trigonometry.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-trigonometry-%{texlive_version}.%{texlive_noarch}.svn43006-%{release}-zypper
%endif

%package -n texlive-trimspaces
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn15878
Release:        0
Summary:        Trim spaces around an argument or within a macro
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-trimspaces-doc >= %{texlive_version}
Provides:       tex(trimspaces.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source179:      trimspaces.tar.xz
Source180:      trimspaces.doc.tar.xz

%description -n texlive-trimspaces
A very short package that allows you to expandably remove
spaces around a token list (commands are provided to remove
spaces before, spaces after, or both); or to remove surrounding
spaces within a macro definition, or to define space-stripped
macros.

%package -n texlive-trimspaces-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn15878
Release:        0
Summary:        Documentation for texlive-trimspaces
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-trimspaces-doc
This package includes the documentation for texlive-trimspaces

%post -n texlive-trimspaces
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-trimspaces 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-trimspaces
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-trimspaces-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/trimspaces/README
%{_texmfdistdir}/doc/latex/trimspaces/trimspaces.pdf

%files -n texlive-trimspaces
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/trimspaces/trimspaces.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-trimspaces-%{texlive_version}.%{texlive_noarch}.1.1svn15878-%{release}-zypper
%endif

%package -n texlive-trivfloat
Version:        %{texlive_version}.%{texlive_noarch}.1.3bsvn15878
Release:        0
Summary:        Quick float definitions in LaTeX
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-trivfloat-doc >= %{texlive_version}
Provides:       tex(trivfloat.sty)
Requires:       tex(float.sty)
Requires:       tex(floatrow.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source181:      trivfloat.tar.xz
Source182:      trivfloat.doc.tar.xz

%description -n texlive-trivfloat
The trivfloat package provides a quick method for defining new
float types in LaTeX. A single command sets up a new float in
the same style as the LaTeX kernel figure and table float
types. The package works with memoir as well as the standard
classes.

%package -n texlive-trivfloat-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.3bsvn15878
Release:        0
Summary:        Documentation for texlive-trivfloat
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-trivfloat-doc
This package includes the documentation for texlive-trivfloat

%post -n texlive-trivfloat
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-trivfloat 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-trivfloat
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-trivfloat-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/trivfloat/README
%{_texmfdistdir}/doc/latex/trivfloat/trivfloat.pdf

%files -n texlive-trivfloat
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/trivfloat/trivfloat.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-trivfloat-%{texlive_version}.%{texlive_noarch}.1.3bsvn15878-%{release}-zypper
%endif

%package -n texlive-trsym
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn18732
Release:        0
Summary:        Symbols for transformations
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-trsym-doc >= %{texlive_version}
Provides:       tex(trsy10.tfm)
Provides:       tex(trsy12.tfm)
Provides:       tex(trsym.sty)
Provides:       tex(utrsy.fd)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source183:      trsym.tar.xz
Source184:      trsym.doc.tar.xz

%description -n texlive-trsym
The bundle provides Metafont source for a small font used for
(e.g.) Laplace transformations, together with a LaTeX .fd file
and a package providing commands for the symbols' use in
mathematics.

%package -n texlive-trsym-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn18732
Release:        0
Summary:        Documentation for texlive-trsym
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-trsym-doc
This package includes the documentation for texlive-trsym

%post -n texlive-trsym
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-trsym 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-trsym
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-trsym-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/trsym/README
%{_texmfdistdir}/doc/latex/trsym/manifest.txt
%{_texmfdistdir}/doc/latex/trsym/trsym.pdf

%files -n texlive-trsym
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/source/public/trsym/trsy.mf
%{_texmfdistdir}/fonts/source/public/trsym/trsy10.mf
%{_texmfdistdir}/fonts/source/public/trsym/trsy12.mf
%{_texmfdistdir}/fonts/tfm/public/trsym/trsy10.tfm
%{_texmfdistdir}/fonts/tfm/public/trsym/trsy12.tfm
%{_texmfdistdir}/tex/latex/trsym/trsym.sty
%{_texmfdistdir}/tex/latex/trsym/utrsy.fd
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-trsym-%{texlive_version}.%{texlive_noarch}.1.0svn18732-%{release}-zypper
%endif

%package -n texlive-truncate
Version:        %{texlive_version}.%{texlive_noarch}.3.6svn18921
Release:        0
Summary:        Truncate text to a specified width
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-truncate-doc >= %{texlive_version}
Provides:       tex(truncate.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source185:      truncate.tar.xz
Source186:      truncate.doc.tar.xz

%description -n texlive-truncate
The package will by default break at word boundaries, but
package options are offered to permit breaks within words.

%package -n texlive-truncate-doc
Version:        %{texlive_version}.%{texlive_noarch}.3.6svn18921
Release:        0
Summary:        Documentation for texlive-truncate
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-truncate-doc
This package includes the documentation for texlive-truncate

%post -n texlive-truncate
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-truncate 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-truncate
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-truncate-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/truncate/miscdoc.sty
%{_texmfdistdir}/doc/latex/truncate/truncate.pdf
%{_texmfdistdir}/doc/latex/truncate/truncate.tex

%files -n texlive-truncate
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/truncate/truncate.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-truncate-%{texlive_version}.%{texlive_noarch}.3.6svn18921-%{release}-zypper
%endif

%package -n texlive-tsemlines
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn23440
Release:        0
Summary:        Support for the ancient \emline macro
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Provides:       tex(tsemlines.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source187:      tsemlines.tar.xz

%description -n texlive-tsemlines
Occasional Documents appear, that use graphics generated by
texcad from the emtex distribution. These documents often use
the \emline macro, which produced lines at an arbitrary
orientation. The present package emulates the macro, using
TikZ.
%post -n texlive-tsemlines
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tsemlines 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tsemlines
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tsemlines
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/tsemlines/tsemlines.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-tsemlines-%{texlive_version}.%{texlive_noarch}.1.0svn23440-%{release}-zypper
%endif

%package -n texlive-ttfutils
Version:        %{texlive_version}.%{texlive_noarch}.svn54074
Release:        0
Summary:        Convert TrueType to TFM and PK fonts
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-ttfutils-bin >= %{texlive_version}
#!BuildIgnore: texlive-ttfutils-bin
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-ttfutils-doc >= %{texlive_version}
Provides:       tex(T1-WGL4.enc)
Provides:       tex(ttf2pk.cfg)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source188:      ttfutils.tar.xz
Source189:      ttfutils.doc.tar.xz

%description -n texlive-ttfutils
Utilities: ttf2afm ttf2pk ttf2tfm ttfdump. FreeType is the
underlying library.

%package -n texlive-ttfutils-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn54074
Release:        0
Summary:        Documentation for texlive-ttfutils
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       man(ttf2afm.1)
Provides:       man(ttf2pk.1)
Provides:       man(ttf2tfm.1)
Provides:       man(ttfdump.1)

%description -n texlive-ttfutils-doc
This package includes the documentation for texlive-ttfutils

%post -n texlive-ttfutils
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-ttfutils 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-ttfutils
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-ttfutils-doc
%defattr(-,root,root,755)
%{_mandir}/man1/ttf2afm.1*
%{_mandir}/man1/ttf2pk.1*
%{_mandir}/man1/ttf2tfm.1*
%{_mandir}/man1/ttfdump.1*
%{_texmfdistdir}/doc/ttf2pk/ttf2pk.doc
%{_texmfdistdir}/doc/ttf2pk/ttf2pk.txt
%{_texmfdistdir}/doc/ttf2pk/ttf2tfm.txt

%files -n texlive-ttfutils
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/enc/ttf2pk/base/T1-WGL4.enc
%{_texmfdistdir}/fonts/sfd/ttf2pk/Big5.sfd
%{_texmfdistdir}/fonts/sfd/ttf2pk/EUC.sfd
%{_texmfdistdir}/fonts/sfd/ttf2pk/HKSCS.sfd
%{_texmfdistdir}/fonts/sfd/ttf2pk/KS-HLaTeX.sfd
%{_texmfdistdir}/fonts/sfd/ttf2pk/SJIS.sfd
%{_texmfdistdir}/fonts/sfd/ttf2pk/UBg5plus.sfd
%{_texmfdistdir}/fonts/sfd/ttf2pk/UBig5.sfd
%{_texmfdistdir}/fonts/sfd/ttf2pk/UGB.sfd
%{_texmfdistdir}/fonts/sfd/ttf2pk/UGBK.sfd
%{_texmfdistdir}/fonts/sfd/ttf2pk/UJIS.sfd
%{_texmfdistdir}/fonts/sfd/ttf2pk/UKS-HLaTeX.sfd
%{_texmfdistdir}/fonts/sfd/ttf2pk/UKS.sfd
%{_texmfdistdir}/fonts/sfd/ttf2pk/Unicode.sfd
%{_texmfdistdir}/ttf2pk/VPS.rpl
%{_texmfdistdir}/ttf2pk/ttf2pk.cfg
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-ttfutils-%{texlive_version}.%{texlive_noarch}.svn54074-%{release}-zypper
%endif

%package -n texlive-tucv
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn20680
Release:        0
Summary:        Support for typesetting a CV or resumee
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-tucv-doc >= %{texlive_version}
Provides:       tex(tucv.sty)
Requires:       tex(array.sty)
Requires:       tex(calc.sty)
Requires:       tex(color.sty)
Requires:       tex(fancyhdr.sty)
Requires:       tex(xparse.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source190:      tucv.tar.xz
Source191:      tucv.doc.tar.xz

%description -n texlive-tucv
The package provides commands for typesetting a CV or resume.
It provides commands for general-purpose headings, entries, and
item/description pairs, as well as more specific commands for
formatting sections, with explicit inclusion of school, degree,
employer, job, conference, and publications entries. It tends
to produce a somewhat long and quite detailed document but may
also be suitable to support a shorter resume. The package
relies on a 'sufficiently recent' copy of the l3kernel and
l3packages bundles.

%package -n texlive-tucv-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn20680
Release:        0
Summary:        Documentation for texlive-tucv
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-tucv-doc
This package includes the documentation for texlive-tucv

%post -n texlive-tucv
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tucv 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tucv
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tucv-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/tucv/README
%{_texmfdistdir}/doc/latex/tucv/tucv.pdf
%{_texmfdistdir}/doc/latex/tucv/tucv_ex.pdf
%{_texmfdistdir}/doc/latex/tucv/tucv_ex.tex

%files -n texlive-tucv
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/tucv/tucv.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-tucv-%{texlive_version}.%{texlive_noarch}.1.0svn20680-%{release}-zypper
%endif

%package -n texlive-tuda-ci
Version:        %{texlive_version}.%{texlive_noarch}.2.09svn54230
Release:        0
Summary:        LaTeX templates of Technische Universitat Darmstadt
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-tuda-ci-doc >= %{texlive_version}
Provides:       tex(beamercolorthemeTUDa.sty)
Provides:       tex(beamerfontthemeTUDa.sty)
Provides:       tex(beamerinnerthemeTUDa.sty)
Provides:       tex(beamerouterthemeTUDa.sty)
Provides:       tex(beamerthemeTUDa.sty)
Provides:       tex(tuda-a0paper.clo)
Provides:       tex(tuda-a1paper.clo)
Provides:       tex(tuda-a2paper.clo)
Provides:       tex(tuda-a3paper.clo)
Provides:       tex(tuda-a4paper.clo)
Provides:       tex(tuda-a5paper.clo)
Provides:       tex(tuda-pgfplots.sty)
Provides:       tex(tudabeamer.cls)
Provides:       tex(tudacolors.def)
Provides:       tex(tudacolors.sty)
Provides:       tex(tudaexercise.cls)
Provides:       tex(tudafonts.sty)
Provides:       tex(tudaleaflet.cls)
Provides:       tex(tudaletter.cls)
Provides:       tex(tudalettersize10pt.clo)
Provides:       tex(tudaposter.cls)
Provides:       tex(tudapub.cls)
Provides:       tex(tudarules.sty)
Provides:       tex(tudasciposter.cls)
Provides:       tex(tudasize9pt.clo)
Provides:       tex(tudathesis.cfg)
Requires:       tex(URspecialopts.sty)
Requires:       tex(XCharter.sty)
Requires:       tex(afterpage.sty)
Requires:       tex(anyfontsize.sty)
Requires:       tex(beamer.cls)
Requires:       tex(environ.sty)
Requires:       tex(expl3.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(geometry.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(iftex.sty)
Requires:       tex(inputenc.sty)
Requires:       tex(l3keys2e.sty)
Requires:       tex(leaflet.cls)
Requires:       tex(luainputenc.sty)
Requires:       tex(microtype.sty)
Requires:       tex(pdfx.sty)
Requires:       tex(pgfplots.sty)
Requires:       tex(qrcode.sty)
Requires:       tex(ragged2e.sty)
Requires:       tex(roboto-mono.sty)
Requires:       tex(roboto.sty)
Requires:       tex(scrartcl.cls)
Requires:       tex(scrextend.sty)
Requires:       tex(scrlayer-notecolumn.sty)
Requires:       tex(scrlayer-scrpage.sty)
Requires:       tex(scrlayer.sty)
Requires:       tex(scrlfile.sty)
Requires:       tex(scrlttr2.cls)
Requires:       tex(tcolorbox.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(tikz.sty)
Requires:       tex(trimclip.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xparse.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source192:      tuda-ci.tar.xz
Source193:      tuda-ci.doc.tar.xz

%description -n texlive-tuda-ci
The TUDa-CI-Bundle provides a possibility to use the Corporate
Design of TU Darmstadt in LaTeX. It contains documentclasses as
well as some helper packages and config files together with
some templates for user documentation, which currently are only
available in German.

%package -n texlive-tuda-ci-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.09svn54230
Release:        0
Summary:        Documentation for texlive-tuda-ci
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-tuda-ci-doc:de)

%description -n texlive-tuda-ci-doc
This package includes the documentation for texlive-tuda-ci

%post -n texlive-tuda-ci
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tuda-ci 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tuda-ci
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tuda-ci-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/tuda-ci/DEMO-TUDaAnnouncement.pdf
%{_texmfdistdir}/doc/latex/tuda-ci/DEMO-TUDaAnnouncement.tex
%{_texmfdistdir}/doc/latex/tuda-ci/DEMO-TUDaBeamer.pdf
%{_texmfdistdir}/doc/latex/tuda-ci/DEMO-TUDaBeamer.tex
%{_texmfdistdir}/doc/latex/tuda-ci/DEMO-TUDaBibliography.bib
%{_texmfdistdir}/doc/latex/tuda-ci/DEMO-TUDaExercise.pdf
%{_texmfdistdir}/doc/latex/tuda-ci/DEMO-TUDaExercise.tex
%{_texmfdistdir}/doc/latex/tuda-ci/DEMO-TUDaFromaddress.lco
%{_texmfdistdir}/doc/latex/tuda-ci/DEMO-TUDaLeaflet.pdf
%{_texmfdistdir}/doc/latex/tuda-ci/DEMO-TUDaLeaflet.tex
%{_texmfdistdir}/doc/latex/tuda-ci/DEMO-TUDaLetter.pdf
%{_texmfdistdir}/doc/latex/tuda-ci/DEMO-TUDaLetter.tex
%{_texmfdistdir}/doc/latex/tuda-ci/DEMO-TUDaPhD.pdf
%{_texmfdistdir}/doc/latex/tuda-ci/DEMO-TUDaPhD.tex
%{_texmfdistdir}/doc/latex/tuda-ci/DEMO-TUDaPoster.pdf
%{_texmfdistdir}/doc/latex/tuda-ci/DEMO-TUDaPoster.tex
%{_texmfdistdir}/doc/latex/tuda-ci/DEMO-TUDaPub.pdf
%{_texmfdistdir}/doc/latex/tuda-ci/DEMO-TUDaPub.tex
%{_texmfdistdir}/doc/latex/tuda-ci/DEMO-TUDaReport.pdf
%{_texmfdistdir}/doc/latex/tuda-ci/DEMO-TUDaReport.tex
%{_texmfdistdir}/doc/latex/tuda-ci/DEMO-TUDaSciPoster.pdf
%{_texmfdistdir}/doc/latex/tuda-ci/DEMO-TUDaSciPoster.tex
%{_texmfdistdir}/doc/latex/tuda-ci/DEMO-TUDaThesis.pdf
%{_texmfdistdir}/doc/latex/tuda-ci/DEMO-TUDaThesis.tex
%{_texmfdistdir}/doc/latex/tuda-ci/README.md

%files -n texlive-tuda-ci
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/tuda-ci/beamercolorthemeTUDa.sty
%{_texmfdistdir}/tex/latex/tuda-ci/beamerfontthemeTUDa.sty
%{_texmfdistdir}/tex/latex/tuda-ci/beamerinnerthemeTUDa.sty
%{_texmfdistdir}/tex/latex/tuda-ci/beamerouterthemeTUDa.sty
%{_texmfdistdir}/tex/latex/tuda-ci/beamerthemeTUDa.sty
%{_texmfdistdir}/tex/latex/tuda-ci/tuda-a0paper.clo
%{_texmfdistdir}/tex/latex/tuda-ci/tuda-a1paper.clo
%{_texmfdistdir}/tex/latex/tuda-ci/tuda-a2paper.clo
%{_texmfdistdir}/tex/latex/tuda-ci/tuda-a3paper.clo
%{_texmfdistdir}/tex/latex/tuda-ci/tuda-a4paper.clo
%{_texmfdistdir}/tex/latex/tuda-ci/tuda-a5paper.clo
%{_texmfdistdir}/tex/latex/tuda-ci/tuda-pgfplots.sty
%{_texmfdistdir}/tex/latex/tuda-ci/tudabeamer.cls
%{_texmfdistdir}/tex/latex/tuda-ci/tudacolors.def
%{_texmfdistdir}/tex/latex/tuda-ci/tudacolors.sty
%{_texmfdistdir}/tex/latex/tuda-ci/tudaexercise.cls
%{_texmfdistdir}/tex/latex/tuda-ci/tudafonts.sty
%{_texmfdistdir}/tex/latex/tuda-ci/tudaleaflet.cls
%{_texmfdistdir}/tex/latex/tuda-ci/tudaletter.cls
%{_texmfdistdir}/tex/latex/tuda-ci/tudalettersize10pt.clo
%{_texmfdistdir}/tex/latex/tuda-ci/tudaposter.cls
%{_texmfdistdir}/tex/latex/tuda-ci/tudapub.cls
%{_texmfdistdir}/tex/latex/tuda-ci/tudarules.sty
%{_texmfdistdir}/tex/latex/tuda-ci/tudasciposter.cls
%{_texmfdistdir}/tex/latex/tuda-ci/tudasize9pt.clo
%{_texmfdistdir}/tex/latex/tuda-ci/tudathesis.cfg
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-tuda-ci-%{texlive_version}.%{texlive_noarch}.2.09svn54230-%{release}-zypper
%endif

%package -n texlive-tudscr
Version:        %{texlive_version}.%{texlive_noarch}.2.06fsvn54744
Release:        0
Summary:        Corporate Design of Technische Universitat Dresden
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-cbfonts >= %{texlive_version}
#!BuildIgnore: texlive-cbfonts
Requires:       texlive-environ >= %{texlive_version}
#!BuildIgnore: texlive-environ
Requires:       texlive-etoolbox >= %{texlive_version}
#!BuildIgnore: texlive-etoolbox
Requires:       texlive-geometry >= %{texlive_version}
#!BuildIgnore: texlive-geometry
Requires:       texlive-graphics >= %{texlive_version}
#!BuildIgnore: texlive-graphics
Requires:       texlive-greek-inputenc >= %{texlive_version}
#!BuildIgnore: texlive-greek-inputenc
Requires:       texlive-iwona >= %{texlive_version}
#!BuildIgnore: texlive-iwona
Requires:       texlive-koma-script >= %{texlive_version}
#!BuildIgnore: texlive-koma-script
Requires:       texlive-mathastext >= %{texlive_version}
#!BuildIgnore: texlive-mathastext
Requires:       texlive-mweights >= %{texlive_version}
#!BuildIgnore: texlive-mweights
Requires:       texlive-oberdiek >= %{texlive_version}
#!BuildIgnore: texlive-oberdiek
Requires:       texlive-opensans >= %{texlive_version}
#!BuildIgnore: texlive-opensans
Requires:       texlive-trimspaces >= %{texlive_version}
#!BuildIgnore: texlive-trimspaces
Requires:       texlive-xcolor >= %{texlive_version}
#!BuildIgnore: texlive-xcolor
Requires:       texlive-xpatch >= %{texlive_version}
#!BuildIgnore: texlive-xpatch
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-tudscr-doc >= %{texlive_version}
Provides:       tex(fix-tudscrfonts.sty)
Provides:       tex(mathswap.sty)
Provides:       tex(tudscrartcl.cls)
Provides:       tex(tudscrbase.sty)
Provides:       tex(tudscrbook.cls)
Provides:       tex(tudscrcolor.sty)
Provides:       tex(tudscrcomp-book.sty)
Provides:       tex(tudscrcomp-poster.sty)
Provides:       tex(tudscrcomp.sty)
Provides:       tex(tudscrdoc.cls)
Provides:       tex(tudscrfonts.sty)
Provides:       tex(tudscrmanual.cls)
Provides:       tex(tudscrposter.cls)
Provides:       tex(tudscrreprt.cls)
Provides:       tex(tudscrsupervisor.sty)
Provides:       tex(tudscrtutorial.sty)
Provides:       tex(twocolfix.sty)
Requires:       tex(amsfonts.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(auto-pst-pdf.sty)
Requires:       tex(babel.sty)
Requires:       tex(bm.sty)
Requires:       tex(booktabs.sty)
Requires:       tex(calc.sty)
Requires:       tex(caption.sty)
Requires:       tex(csquotes.sty)
Requires:       tex(dox.sty)
Requires:       tex(ellipsis.sty)
Requires:       tex(enumitem.sty)
Requires:       tex(environ.sty)
Requires:       tex(etexcmds.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(filemod.sty)
Requires:       tex(floatrow.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(geometry.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hologo.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(hyphsubst.sty)
Requires:       tex(ifplatform.sty)
Requires:       tex(iftex.sty)
Requires:       tex(imakeidx.sty)
Requires:       tex(isodate.sty)
Requires:       tex(kvsetkeys.sty)
Requires:       tex(letltxmacro.sty)
Requires:       tex(listings.sty)
Requires:       tex(lmodern.sty)
Requires:       tex(marginnote.sty)
Requires:       tex(mathastext.sty)
Requires:       tex(microtype.sty)
Requires:       tex(newunicodechar.sty)
Requires:       tex(omliwona.fd)
Requires:       tex(omsiwona.fd)
Requires:       tex(pdfpages.sty)
Requires:       tex(pdftexcmds.sty)
Requires:       tex(quoting.sty)
Requires:       tex(ragged2e.sty)
Requires:       tex(scrbase.sty)
Requires:       tex(scrextend.sty)
Requires:       tex(scrhack.sty)
Requires:       tex(scrlayer-scrpage.sty)
Requires:       tex(scrwfile.sty)
Requires:       tex(setspace.sty)
Requires:       tex(shellesc.sty)
Requires:       tex(tabularx.sty)
Requires:       tex(textcase.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(tikz.sty)
Requires:       tex(todonotes.sty)
Requires:       tex(trimspaces.sty)
Requires:       tex(units.sty)
Requires:       tex(url.sty)
Requires:       tex(varioref.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xparse.sty)
Requires:       tex(xpatch.sty)
Requires:       tex(xspace.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source194:      tudscr.tar.xz
Source195:      tudscr.doc.tar.xz

%description -n texlive-tudscr
The TUD-Script bundle provides both classes and packages in
order to create LaTeX documents in the corporate design of the
Technische Universitat Dresden. It bases on the KOMA-Script
bundle, which must necessarily be present. For questions,
problems and comments, please refer to either the LaTeX forum
of the Dresden University of Technology or the GitHub "tudscr"
repository. The bundle offers: the three document classes
tudscrartcl, tudscrreprt, and tudscrbook which serve as wrapper
classes for scrartcl, scrreprt, and scrbook, the class
tudscrposter for creating posters, the package tudscrsupervisor
providing environments and macros to create tasks, evaluations
and notices for scientific theses, the package tudscrfonts,
which makes the corporate design fonts of the Technische
Universitat Dresden available for LaTeX standard classes and
KOMA-Script classes, the package fix-tudscrfonts, which
provides the same fonts to additional corporate design classes
not related to TUD-Script, the package tudscrcomp, which
simplifies the switch to TUD-Script from external corporate
design classes, the package mathswap for swapping math
delimiters within numbers (similar to ionumbers), the package
twocolfix for fixing the positioning bug of headings in
twocolumn layout, and a comprehensive user documentation as
well as several tutorials.

%package -n texlive-tudscr-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.06fsvn54744
Release:        0
Summary:        Documentation for texlive-tudscr
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-tudscr-doc:de)

%description -n texlive-tudscr-doc
This package includes the documentation for texlive-tudscr

%post -n texlive-tudscr
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tudscr 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tudscr
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tudscr-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/tudscr/LICENSE.md
%{_texmfdistdir}/doc/latex/tudscr/README.md
%{_texmfdistdir}/doc/latex/tudscr/tudscr.pdf
%{_texmfdistdir}/doc/latex/tudscr/tudscr_print.pdf
%{_texmfdistdir}/doc/latex/tudscr/tudscrsource.pdf
%{_texmfdistdir}/doc/latex/tudscr/tutorials/mathswap.pdf
%{_texmfdistdir}/doc/latex/tudscr/tutorials/mathtype.pdf
%{_texmfdistdir}/doc/latex/tudscr/tutorials/treatise.pdf

%files -n texlive-tudscr
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/tudscr/fix-tudscrfonts.sty
%{_texmfdistdir}/tex/latex/tudscr/logo/DDC-01.eps
%{_texmfdistdir}/tex/latex/tudscr/logo/DDC-01.pdf
%{_texmfdistdir}/tex/latex/tudscr/logo/DDC-03.eps
%{_texmfdistdir}/tex/latex/tudscr/logo/DDC-03.pdf
%{_texmfdistdir}/tex/latex/tudscr/logo/DDC-07.eps
%{_texmfdistdir}/tex/latex/tudscr/logo/DDC-07.pdf
%{_texmfdistdir}/tex/latex/tudscr/logo/DDC-09.eps
%{_texmfdistdir}/tex/latex/tudscr/logo/DDC-09.pdf
%{_texmfdistdir}/tex/latex/tudscr/logo/DDC-19.eps
%{_texmfdistdir}/tex/latex/tudscr/logo/DDC-19.pdf
%{_texmfdistdir}/tex/latex/tudscr/logo/DDC-21.eps
%{_texmfdistdir}/tex/latex/tudscr/logo/DDC-21.pdf
%{_texmfdistdir}/tex/latex/tudscr/logo/DDC-22.eps
%{_texmfdistdir}/tex/latex/tudscr/logo/DDC-22.pdf
%{_texmfdistdir}/tex/latex/tudscr/logo/DDC-24.eps
%{_texmfdistdir}/tex/latex/tudscr/logo/DDC-24.pdf
%{_texmfdistdir}/tex/latex/tudscr/logo/DDC-25.eps
%{_texmfdistdir}/tex/latex/tudscr/logo/DDC-25.pdf
%{_texmfdistdir}/tex/latex/tudscr/logo/DDC-27.eps
%{_texmfdistdir}/tex/latex/tudscr/logo/DDC-27.pdf
%{_texmfdistdir}/tex/latex/tudscr/logo/DDC-28.eps
%{_texmfdistdir}/tex/latex/tudscr/logo/DDC-28.pdf
%{_texmfdistdir}/tex/latex/tudscr/logo/DDC-30.eps
%{_texmfdistdir}/tex/latex/tudscr/logo/DDC-30.pdf
%{_texmfdistdir}/tex/latex/tudscr/logo/TUD-black.eps
%{_texmfdistdir}/tex/latex/tudscr/logo/TUD-black.pdf
%{_texmfdistdir}/tex/latex/tudscr/logo/TUD-blue.eps
%{_texmfdistdir}/tex/latex/tudscr/logo/TUD-blue.pdf
%{_texmfdistdir}/tex/latex/tudscr/logo/TUD-white.eps
%{_texmfdistdir}/tex/latex/tudscr/logo/TUD-white.pdf
%{_texmfdistdir}/tex/latex/tudscr/mathswap.sty
%{_texmfdistdir}/tex/latex/tudscr/tudscrartcl.cls
%{_texmfdistdir}/tex/latex/tudscr/tudscrbase.sty
%{_texmfdistdir}/tex/latex/tudscr/tudscrbook.cls
%{_texmfdistdir}/tex/latex/tudscr/tudscrcolor.sty
%{_texmfdistdir}/tex/latex/tudscr/tudscrcomp-book.sty
%{_texmfdistdir}/tex/latex/tudscr/tudscrcomp-poster.sty
%{_texmfdistdir}/tex/latex/tudscr/tudscrcomp.sty
%{_texmfdistdir}/tex/latex/tudscr/tudscrdoc.cls
%{_texmfdistdir}/tex/latex/tudscr/tudscrfonts.sty
%{_texmfdistdir}/tex/latex/tudscr/tudscrmanual.cls
%{_texmfdistdir}/tex/latex/tudscr/tudscrposter.cls
%{_texmfdistdir}/tex/latex/tudscr/tudscrreprt.cls
%{_texmfdistdir}/tex/latex/tudscr/tudscrsupervisor.sty
%{_texmfdistdir}/tex/latex/tudscr/tudscrtutorial.sty
%{_texmfdistdir}/tex/latex/tudscr/twocolfix.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-tudscr-%{texlive_version}.%{texlive_noarch}.2.06fsvn54744-%{release}-zypper
%endif

%package -n texlive-tufte-latex
Version:        %{texlive_version}.%{texlive_noarch}.3.5.2svn37649
Release:        0
Summary:        Document classes inspired by the work of Edward Tufte
License:        Apache-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-changepage >= %{texlive_version}
#!BuildIgnore: texlive-changepage
Requires:       texlive-ifmtarg >= %{texlive_version}
#!BuildIgnore: texlive-ifmtarg
Requires:       texlive-paralist >= %{texlive_version}
#!BuildIgnore: texlive-paralist
Requires:       texlive-placeins >= %{texlive_version}
#!BuildIgnore: texlive-placeins
Requires:       texlive-sauerj >= %{texlive_version}
#!BuildIgnore: texlive-sauerj
Requires:       texlive-xifthen >= %{texlive_version}
#!BuildIgnore: texlive-xifthen
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-tufte-latex-doc >= %{texlive_version}
Provides:       tex(tufte-book.cls)
Provides:       tex(tufte-common.def)
Provides:       tex(tufte-handout.cls)
Requires:       tex(beramono.sty)
Requires:       tex(bibentry.sty)
Requires:       tex(bidi.sty)
Requires:       tex(changepage.sty)
Requires:       tex(chngpage.sty)
Requires:       tex(fancyhdr.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(geometry.sty)
Requires:       tex(hardwrap.sty)
Requires:       tex(helvet.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(letterspace.sty)
Requires:       tex(mathpazo.sty)
Requires:       tex(multicol.sty)
Requires:       tex(natbib.sty)
Requires:       tex(optparams.sty)
Requires:       tex(paralist.sty)
Requires:       tex(placeins.sty)
Requires:       tex(ragged2e.sty)
Requires:       tex(setspace.sty)
Requires:       tex(soul.sty)
Requires:       tex(textcase.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(titlesec.sty)
Requires:       tex(titletoc.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xifthen.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xltxtra.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source196:      tufte-latex.tar.xz
Source197:      tufte-latex.doc.tar.xz

%description -n texlive-tufte-latex
Provided are two classes inspired, respectively, by handouts
and books created by Edward Tufte.

%package -n texlive-tufte-latex-doc
Version:        %{texlive_version}.%{texlive_noarch}.3.5.2svn37649
Release:        0
Summary:        Documentation for texlive-tufte-latex
License:        Apache-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-tufte-latex-doc
This package includes the documentation for texlive-tufte-latex

%post -n texlive-tufte-latex
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tufte-latex 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tufte-latex
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tufte-latex-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/tufte-latex/History.txt
%{_texmfdistdir}/doc/latex/tufte-latex/Manifest.txt
%{_texmfdistdir}/doc/latex/tufte-latex/README.txt
%{_texmfdistdir}/doc/latex/tufte-latex/graphics/be-contents.pdf
%{_texmfdistdir}/doc/latex/tufte-latex/graphics/be-title.pdf
%{_texmfdistdir}/doc/latex/tufte-latex/graphics/ei-contents.pdf
%{_texmfdistdir}/doc/latex/tufte-latex/graphics/ei-title.pdf
%{_texmfdistdir}/doc/latex/tufte-latex/graphics/helix.asy
%{_texmfdistdir}/doc/latex/tufte-latex/graphics/helix.pdf
%{_texmfdistdir}/doc/latex/tufte-latex/graphics/hilbertcurves.pdf
%{_texmfdistdir}/doc/latex/tufte-latex/graphics/nasa_vision_sm.png
%{_texmfdistdir}/doc/latex/tufte-latex/graphics/satir_graph.png
%{_texmfdistdir}/doc/latex/tufte-latex/graphics/sine.asy
%{_texmfdistdir}/doc/latex/tufte-latex/graphics/sine.pdf
%{_texmfdistdir}/doc/latex/tufte-latex/graphics/vdqi-contents.pdf
%{_texmfdistdir}/doc/latex/tufte-latex/graphics/vdqi-title.pdf
%{_texmfdistdir}/doc/latex/tufte-latex/graphics/ve-contents.pdf
%{_texmfdistdir}/doc/latex/tufte-latex/graphics/ve-title.pdf
%{_texmfdistdir}/doc/latex/tufte-latex/sample-book.pdf
%{_texmfdistdir}/doc/latex/tufte-latex/sample-book.tex
%{_texmfdistdir}/doc/latex/tufte-latex/sample-handout.bib
%{_texmfdistdir}/doc/latex/tufte-latex/sample-handout.pdf
%{_texmfdistdir}/doc/latex/tufte-latex/sample-handout.tex

%files -n texlive-tufte-latex
%defattr(-,root,root,755)
%{_texmfdistdir}/bibtex/bst/tufte-latex/tufte.bst
%{_texmfdistdir}/tex/latex/tufte-latex/tufte-book.cls
%{_texmfdistdir}/tex/latex/tufte-latex/tufte-common.def
%{_texmfdistdir}/tex/latex/tufte-latex/tufte-handout.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-tufte-latex-%{texlive_version}.%{texlive_noarch}.3.5.2svn37649-%{release}-zypper
%endif

%package -n texlive-tugboat
Version:        %{texlive_version}.%{texlive_noarch}.2.23svn54261
Release:        0
Summary:        LaTeX macros for TUGboat articles
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-tugboat-doc >= %{texlive_version}
Provides:       tex(ltugboat.cls)
Provides:       tex(ltugboat.sty)
Provides:       tex(ltugcomn.sty)
Provides:       tex(ltugproc.cls)
Provides:       tex(ltugproc.sty)
Requires:       tex(article.cls)
Requires:       tex(mflogo.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source198:      tugboat.tar.xz
Source199:      tugboat.doc.tar.xz

%description -n texlive-tugboat
Provides ltugboat.cls for both regular and proceedings issues
of the TUGboat journal. Also provides a BibTeX style,
tugboat.bst.

%package -n texlive-tugboat-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.23svn54261
Release:        0
Summary:        Documentation for texlive-tugboat
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-tugboat-doc:en)

%description -n texlive-tugboat-doc
This package includes the documentation for texlive-tugboat

%post -n texlive-tugboat
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tugboat 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tugboat
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tugboat-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/tugboat/README
%{_texmfdistdir}/doc/latex/tugboat/ltubguid.ltx
%{_texmfdistdir}/doc/latex/tugboat/ltubguid.pdf
%{_texmfdistdir}/doc/latex/tugboat/manifest.txt
%{_texmfdistdir}/doc/latex/tugboat/tugboat.pdf

%files -n texlive-tugboat
%defattr(-,root,root,755)
%{_texmfdistdir}/bibtex/bst/tugboat/ltugbib.bst
%{_texmfdistdir}/bibtex/bst/tugboat/tugboat.bst
%{_texmfdistdir}/tex/latex/tugboat/ltugboat.cls
%{_texmfdistdir}/tex/latex/tugboat/ltugboat.sty
%{_texmfdistdir}/tex/latex/tugboat/ltugcomn.sty
%{_texmfdistdir}/tex/latex/tugboat/ltugproc.cls
%{_texmfdistdir}/tex/latex/tugboat/ltugproc.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-tugboat-%{texlive_version}.%{texlive_noarch}.2.23svn54261-%{release}-zypper
%endif

%package -n texlive-tugboat-plain
Version:        %{texlive_version}.%{texlive_noarch}.1.25svn51373
Release:        0
Summary:        Plain TeX macros for TUGboat
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-tugboat-plain-doc >= %{texlive_version}
Provides:       tex(tugboat.sty)
Provides:       tex(tugproc.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source200:      tugboat-plain.tar.xz
Source201:      tugboat-plain.doc.tar.xz

%description -n texlive-tugboat-plain
The macros defined in this directory (in files tugboat.sty and
tugboat.cmn) are used in papers written in Plain TeX for
publication in TUGboat.

%package -n texlive-tugboat-plain-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.25svn51373
Release:        0
Summary:        Documentation for texlive-tugboat-plain
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-tugboat-plain-doc
This package includes the documentation for texlive-tugboat-plain

%post -n texlive-tugboat-plain
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tugboat-plain 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tugboat-plain
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tugboat-plain-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/plain/tugboat-plain/README
%{_texmfdistdir}/doc/plain/tugboat-plain/tubguide.pdf
%{_texmfdistdir}/doc/plain/tugboat-plain/tubguide.tex

%files -n texlive-tugboat-plain
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/plain/tugboat-plain/tugboat.cmn
%{_texmfdistdir}/tex/plain/tugboat-plain/tugboat.sty
%{_texmfdistdir}/tex/plain/tugboat-plain/tugproc.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-tugboat-plain-%{texlive_version}.%{texlive_noarch}.1.25svn51373-%{release}-zypper
%endif

%package -n texlive-tui
Version:        %{texlive_version}.%{texlive_noarch}.1.9svn27253
Release:        0
Summary:        Thesis style for the University of the Andes, Colombia
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-tui-doc >= %{texlive_version}
Provides:       tex(tui.cls)
Requires:       tex(MnSymbol.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(amsthm.sty)
Requires:       tex(babel.sty)
Requires:       tex(breakurl.sty)
Requires:       tex(courier.sty)
Requires:       tex(csquotes.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(inputenc.sty)
Requires:       tex(kpfonts.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(makeidx.sty)
Requires:       tex(mathptmx.sty)
Requires:       tex(memoir.cls)
Requires:       tex(xcolor.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source202:      tui.tar.xz
Source203:      tui.doc.tar.xz

%description -n texlive-tui
Doctoral Dissertations from the Faculty of Engineering at the
Universidad de los Andes, Bogota, Colombia. The class is
implemented as an extension of the memoir class. Clase de Tesis
doctorales para ingenieria, Universidad de los Andes, Bogota.

%package -n texlive-tui-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.9svn27253
Release:        0
Summary:        Documentation for texlive-tui
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-tui-doc:en;es)

%description -n texlive-tui-doc
This package includes the documentation for texlive-tui

%post -n texlive-tui
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tui 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tui
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tui-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/tui/README
%{_texmfdistdir}/doc/latex/tui/TUIdoc.pdf
%{_texmfdistdir}/doc/latex/tui/TUIdoc.tex
%{_texmfdistdir}/doc/latex/tui/example/abstract.tex
%{_texmfdistdir}/doc/latex/tui/example/agradec.tex
%{_texmfdistdir}/doc/latex/tui/example/ap01.tex
%{_texmfdistdir}/doc/latex/tui/example/bibliotesis.bib
%{_texmfdistdir}/doc/latex/tui/example/ch01.tex
%{_texmfdistdir}/doc/latex/tui/example/ch02.tex
%{_texmfdistdir}/doc/latex/tui/example/ch03.tex
%{_texmfdistdir}/doc/latex/tui/example/coleccion.tex
%{_texmfdistdir}/doc/latex/tui/example/dedicat.tex
%{_texmfdistdir}/doc/latex/tui/example/hyphenation.tex
%{_texmfdistdir}/doc/latex/tui/example/imagen.pdf
%{_texmfdistdir}/doc/latex/tui/example/intro.tex
%{_texmfdistdir}/doc/latex/tui/example/lipsum.tex
%{_texmfdistdir}/doc/latex/tui/example/listofsymbols.tex
%{_texmfdistdir}/doc/latex/tui/example/main.tex
%{_texmfdistdir}/doc/latex/tui/example/plegal.tex
%{_texmfdistdir}/doc/latex/tui/example/portada.tex
%{_texmfdistdir}/doc/latex/tui/example/resumen.tex
%{_texmfdistdir}/doc/latex/tui/template/abstract.tex
%{_texmfdistdir}/doc/latex/tui/template/agradec.tex
%{_texmfdistdir}/doc/latex/tui/template/ap01.tex
%{_texmfdistdir}/doc/latex/tui/template/bibliotesis.bib
%{_texmfdistdir}/doc/latex/tui/template/ch01.tex
%{_texmfdistdir}/doc/latex/tui/template/ch02.tex
%{_texmfdistdir}/doc/latex/tui/template/ch03.tex
%{_texmfdistdir}/doc/latex/tui/template/coleccion.tex
%{_texmfdistdir}/doc/latex/tui/template/dedicat.tex
%{_texmfdistdir}/doc/latex/tui/template/hyphenation.tex
%{_texmfdistdir}/doc/latex/tui/template/intro.tex
%{_texmfdistdir}/doc/latex/tui/template/listofsymbols.tex
%{_texmfdistdir}/doc/latex/tui/template/main.tex
%{_texmfdistdir}/doc/latex/tui/template/plegal.tex
%{_texmfdistdir}/doc/latex/tui/template/portada.tex
%{_texmfdistdir}/doc/latex/tui/template/resumen.tex

%files -n texlive-tui
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/tui/tui.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-tui-%{texlive_version}.%{texlive_noarch}.1.9svn27253-%{release}-zypper
%endif

%package -n texlive-turabian
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1.0svn36298
Release:        0
Summary:        Create Turabian-formatted material using LaTeX
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-turabian-doc >= %{texlive_version}
Provides:       tex(turabian.cls)
Requires:       tex(babel.sty)
Requires:       tex(cjhebrew.sty)
Requires:       tex(fancyhdr.sty)
Requires:       tex(geometry.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hyphenat.sty)
Requires:       tex(indentfirst.sty)
Requires:       tex(lipsum.sty)
Requires:       tex(report.cls)
Requires:       tex(scrextend.sty)
Requires:       tex(setspace.sty)
Requires:       tex(times.sty)
Requires:       tex(titlesec.sty)
Requires:       tex(tocloft.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source204:      turabian.tar.xz
Source205:      turabian.doc.tar.xz

%description -n texlive-turabian
The bundle provides a class file and a template for creating
Turabian-formatted projects. The class file supports citation
formatting conforming to the Turabian 8th Edition style guide.

%package -n texlive-turabian-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1.0svn36298
Release:        0
Summary:        Documentation for texlive-turabian
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-turabian-doc
This package includes the documentation for texlive-turabian

%post -n texlive-turabian
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-turabian 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-turabian
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-turabian-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/turabian/README
%{_texmfdistdir}/doc/latex/turabian/turabian.tex
%{_texmfdistdir}/doc/latex/turabian/userguide.txt

%files -n texlive-turabian
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/turabian/turabian.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-turabian-%{texlive_version}.%{texlive_noarch}.0.0.1.0svn36298-%{release}-zypper
%endif

%package -n texlive-turabian-formatting
Version:        %{texlive_version}.%{texlive_noarch}.svn54436
Release:        0
Summary:        Formatting based on Turabian's Manual
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-turabian-formatting-doc >= %{texlive_version}
Provides:       tex(turabian-formatting.sty)
Provides:       tex(turabian-researchpaper.cls)
Provides:       tex(turabian-thesis.cls)
Requires:       tex(article.cls)
Requires:       tex(book.cls)
Requires:       tex(endnotes.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(footmisc.sty)
Requires:       tex(nowidow.sty)
Requires:       tex(setspace.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source206:      turabian-formatting.tar.xz
Source207:      turabian-formatting.doc.tar.xz

%description -n texlive-turabian-formatting
The turabian-formatting package provides Chicago-style
formatting based on Kate L. Turabian's "A Manual for Writers of
Research Papers, Theses, and Dissertations: Chicago Style for
Students and Researchers" (9th edition).

%package -n texlive-turabian-formatting-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn54436
Release:        0
Summary:        Documentation for texlive-turabian-formatting
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-turabian-formatting-doc
This package includes the documentation for texlive-turabian-formatting

%post -n texlive-turabian-formatting
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-turabian-formatting 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-turabian-formatting
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-turabian-formatting-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/turabian-formatting/README
%{_texmfdistdir}/doc/latex/turabian-formatting/turabian-formatting-doc.pdf
%{_texmfdistdir}/doc/latex/turabian-formatting/turabian-formatting-doc.tex

%files -n texlive-turabian-formatting
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/turabian-formatting/turabian-formatting.sty
%{_texmfdistdir}/tex/latex/turabian-formatting/turabian-researchpaper.cls
%{_texmfdistdir}/tex/latex/turabian-formatting/turabian-thesis.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-turabian-formatting-%{texlive_version}.%{texlive_noarch}.svn54436-%{release}-zypper
%endif

%package -n texlive-turkmen
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2svn17748
Release:        0
Summary:        Babel support for Turkmen
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-turkmen-doc >= %{texlive_version}
Provides:       tex(turkmen.ldf)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source208:      turkmen.tar.xz
Source209:      turkmen.doc.tar.xz

%description -n texlive-turkmen
The package provides support for Turkmen in babel, but
integration with babel is not available.

%package -n texlive-turkmen-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2svn17748
Release:        0
Summary:        Documentation for texlive-turkmen
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-turkmen-doc
This package includes the documentation for texlive-turkmen

%post -n texlive-turkmen
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-turkmen 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-turkmen
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-turkmen-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/turkmen/README
%{_texmfdistdir}/doc/latex/turkmen/turkmen.pdf

%files -n texlive-turkmen
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/turkmen/turkmen.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-turkmen-%{texlive_version}.%{texlive_noarch}.0.0.2svn17748-%{release}-zypper
%endif

%package -n texlive-turnstile
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn15878
Release:        0
Summary:        Typeset the (logic) turnstile notation
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-turnstile-doc >= %{texlive_version}
Provides:       tex(turnstile.sty)
Requires:       tex(ifthen.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source210:      turnstile.tar.xz
Source211:      turnstile.doc.tar.xz

%description -n texlive-turnstile
Among other uses, the turnstile sign is used by logicians for
denoting a consequence relation, related to a given logic,
between a collection of formulas and a derived formula.

%package -n texlive-turnstile-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn15878
Release:        0
Summary:        Documentation for texlive-turnstile
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-turnstile-doc:pt)

%description -n texlive-turnstile-doc
This package includes the documentation for texlive-turnstile

%post -n texlive-turnstile
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-turnstile 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-turnstile
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-turnstile-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/turnstile/README
%{_texmfdistdir}/doc/latex/turnstile/README.en
%{_texmfdistdir}/doc/latex/turnstile/README.pt
%{_texmfdistdir}/doc/latex/turnstile/turnstile-en.pdf
%{_texmfdistdir}/doc/latex/turnstile/turnstile-pt.pdf
%{_texmfdistdir}/doc/latex/turnstile/turnstile_article.pdf
%{_texmfdistdir}/doc/latex/turnstile/turnstile_article.tex
%{_texmfdistdir}/doc/latex/turnstile/turnstile_artigo.pdf
%{_texmfdistdir}/doc/latex/turnstile/turnstile_artigo.tex

%files -n texlive-turnstile
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/turnstile/turnstile.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-turnstile-%{texlive_version}.%{texlive_noarch}.1.0svn15878-%{release}-zypper
%endif

%package -n texlive-turnthepage
Version:        %{texlive_version}.%{texlive_noarch}.1.3asvn29803
Release:        0
Summary:        Provide "turn page" instructions
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-turnthepage-doc >= %{texlive_version}
Provides:       tex(turnpageetex.sty)
Provides:       tex(turnpagewoetex.sty)
Provides:       tex(turnthepage.sty)
Requires:       tex(alphalph.sty)
Requires:       tex(atbegshi.sty)
Requires:       tex(pageslts.sty)
Requires:       tex(picture.sty)
Requires:       tex(zref-abspage.sty)
Requires:       tex(zref-lastpage.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source212:      turnthepage.tar.xz
Source213:      turnthepage.doc.tar.xz

%description -n texlive-turnthepage
The package prints a 'turn' instruction at the bottom of
odd-numbered pages (except the last). This is a common
convention for examination papers and the like.

%package -n texlive-turnthepage-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.3asvn29803
Release:        0
Summary:        Documentation for texlive-turnthepage
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-turnthepage-doc
This package includes the documentation for texlive-turnthepage

%post -n texlive-turnthepage
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-turnthepage 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-turnthepage
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-turnthepage-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/turnthepage/Makefile
%{_texmfdistdir}/doc/latex/turnthepage/README
%{_texmfdistdir}/doc/latex/turnthepage/perso.ist
%{_texmfdistdir}/doc/latex/turnthepage/turnthepage-bib.bib
%{_texmfdistdir}/doc/latex/turnthepage/turnthepage.pdf
%{_texmfdistdir}/doc/latex/turnthepage/turnthepage.tex

%files -n texlive-turnthepage
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/turnthepage/turnpageetex.sty
%{_texmfdistdir}/tex/latex/turnthepage/turnpagewoetex.sty
%{_texmfdistdir}/tex/latex/turnthepage/turnthepage.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-turnthepage-%{texlive_version}.%{texlive_noarch}.1.3asvn29803-%{release}-zypper
%endif

%package -n texlive-twemoji-colr
Version:        %{texlive_version}.%{texlive_noarch}.0.0.5.0svn54512
Release:        0
Summary:        Twemoji font in COLR/CPAL layered format
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Requires:       texlive-twemoji-colr-fonts >= %{texlive_version}
Recommends:     texlive-twemoji-colr-doc >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source214:      twemoji-colr.tar.xz
Source215:      twemoji-colr.doc.tar.xz

%description -n texlive-twemoji-colr
This is a COLR/CPAL-based color OpenType font from the Twemoji
collection of emoji images.

%package -n texlive-twemoji-colr-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.5.0svn54512
Release:        0
Summary:        Documentation for texlive-twemoji-colr
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-twemoji-colr-doc
This package includes the documentation for texlive-twemoji-colr


%package -n texlive-twemoji-colr-fonts
Version:        %{texlive_version}.%{texlive_noarch}.0.0.5.0svn54512
Release:        0
Summary:        Severed fonts for texlive-twemoji-colr
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Fonts
URL:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-twemoji-colr-fonts
The  separated fonts package for texlive-twemoji-colr
%post -n texlive-twemoji-colr
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-twemoji-colr 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-twemoji-colr
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-twemoji-colr-fonts
%files -n texlive-twemoji-colr-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/twemoji-colr/README.md

%files -n texlive-twemoji-colr
%defattr(-,root,root,755)
%verify(link) %{_texmfdistdir}/fonts/truetype/public/twemoji-colr/TwemojiMozilla.ttf

%files -n texlive-twemoji-colr-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-twemoji-colr
%{_datadir}/fontconfig/conf.avail/58-texlive-twemoji-colr.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-twemoji-colr/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-twemoji-colr/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-twemoji-colr/fonts.scale
%{_datadir}/fonts/texlive-twemoji-colr/TwemojiMozilla.ttf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-twemoji-colr-fonts-%{texlive_version}.%{texlive_noarch}.0.0.5.0svn54512-%{release}-zypper
%endif

%package -n texlive-twoinone
Version:        %{texlive_version}.%{texlive_noarch}.svn17024
Release:        0
Summary:        Print two pages on a single page
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-twoinone-doc >= %{texlive_version}
Provides:       tex(2in1.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source216:      twoinone.tar.xz
Source217:      twoinone.doc.tar.xz

%description -n texlive-twoinone
The package is for printing two pages on a single (landscape)
A4 page. Page numbers appear on the included pages, and not on
the landscape 'container' page.

%package -n texlive-twoinone-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn17024
Release:        0
Summary:        Documentation for texlive-twoinone
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-twoinone-doc
This package includes the documentation for texlive-twoinone

%post -n texlive-twoinone
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-twoinone 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-twoinone
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-twoinone-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/twoinone/twoinone.pdf
%{_texmfdistdir}/doc/latex/twoinone/twoinone.tex

%files -n texlive-twoinone
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/twoinone/2in1.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-twoinone-%{texlive_version}.%{texlive_noarch}.svn17024-%{release}-zypper
%endif

%package -n texlive-twoup
Version:        %{texlive_version}.%{texlive_noarch}.1.3svn15878
Release:        0
Summary:        Print two virtual pages on each physical page
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-twoup-doc >= %{texlive_version}
Provides:       tex(twoup.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source218:      twoup.tar.xz
Source219:      twoup.doc.tar.xz

%description -n texlive-twoup
MiKTeX and many other TeX implementations include tools for
massaging PostScript into booklet and two-up printing -- that
is, printing two logical pages side by side on one side of one
sheet of paper. However, some LaTeX preliminaries are necessary
to use those tools. The twoup package provides such
preliminaries and gives advice on how to use the PostScript
tools.

%package -n texlive-twoup-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.3svn15878
Release:        0
Summary:        Documentation for texlive-twoup
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-twoup-doc
This package includes the documentation for texlive-twoup

%post -n texlive-twoup
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-twoup 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-twoup
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-twoup-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/twoup/README
%{_texmfdistdir}/doc/latex/twoup/twoup.pdf

%files -n texlive-twoup
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/twoup/twoup.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-twoup-%{texlive_version}.%{texlive_noarch}.1.3svn15878-%{release}-zypper
%endif

%package -n texlive-txfonts
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Times-like fonts in support of mathematics
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
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
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Requires:       texlive-txfonts-fonts >= %{texlive_version}
Recommends:     texlive-txfonts-doc >= %{texlive_version}
Provides:       tex(ly1txr.fd)
Provides:       tex(ly1txss.fd)
Provides:       tex(ly1txtt.fd)
Provides:       tex(omltxmi.fd)
Provides:       tex(omltxr.fd)
Provides:       tex(omstxr.fd)
Provides:       tex(omstxsy.fd)
Provides:       tex(omxtxex.fd)
Provides:       tex(ot1txr.fd)
Provides:       tex(ot1txss.fd)
Provides:       tex(ot1txtt.fd)
Provides:       tex(rtcxb.tfm)
Provides:       tex(rtcxbi.tfm)
Provides:       tex(rtcxbsl.tfm)
Provides:       tex(rtcxbss.tfm)
Provides:       tex(rtcxbsso.tfm)
Provides:       tex(rtcxi.tfm)
Provides:       tex(rtcxr.tfm)
Provides:       tex(rtcxsl.tfm)
Provides:       tex(rtcxss.tfm)
Provides:       tex(rtcxsssl.tfm)
Provides:       tex(rtxb.tfm)
Provides:       tex(rtxbi.tfm)
Provides:       tex(rtxbmi.tfm)
Provides:       tex(rtxbsc.tfm)
Provides:       tex(rtxbsl.tfm)
Provides:       tex(rtxbss.tfm)
Provides:       tex(rtxbsssc.tfm)
Provides:       tex(rtxbsssl.tfm)
Provides:       tex(rtxi.tfm)
Provides:       tex(rtxmi.tfm)
Provides:       tex(rtxphvb.tfm)
Provides:       tex(rtxphvbo.tfm)
Provides:       tex(rtxphvr.tfm)
Provides:       tex(rtxphvro.tfm)
Provides:       tex(rtxptmb.tfm)
Provides:       tex(rtxptmbi.tfm)
Provides:       tex(rtxptmbo.tfm)
Provides:       tex(rtxptmr.tfm)
Provides:       tex(rtxptmri.tfm)
Provides:       tex(rtxptmro.tfm)
Provides:       tex(rtxr.tfm)
Provides:       tex(rtxsc.tfm)
Provides:       tex(rtxsl.tfm)
Provides:       tex(rtxss.tfm)
Provides:       tex(rtxsssc.tfm)
Provides:       tex(rtxsssl.tfm)
Provides:       tex(t1txr.fd)
Provides:       tex(t1txss.fd)
Provides:       tex(t1txtt.fd)
Provides:       tex(t1xb.tfm)
Provides:       tex(t1xb.vf)
Provides:       tex(t1xbi.tfm)
Provides:       tex(t1xbi.vf)
Provides:       tex(t1xbsc.tfm)
Provides:       tex(t1xbsc.vf)
Provides:       tex(t1xbsl.tfm)
Provides:       tex(t1xbsl.vf)
Provides:       tex(t1xbss.tfm)
Provides:       tex(t1xbss.vf)
Provides:       tex(t1xbsssc.tfm)
Provides:       tex(t1xbsssc.vf)
Provides:       tex(t1xbsssl.tfm)
Provides:       tex(t1xbsssl.vf)
Provides:       tex(t1xbtt.tfm)
Provides:       tex(t1xbttsc.tfm)
Provides:       tex(t1xbttsl.tfm)
Provides:       tex(t1xi.tfm)
Provides:       tex(t1xi.vf)
Provides:       tex(t1xr.tfm)
Provides:       tex(t1xr.vf)
Provides:       tex(t1xsc.tfm)
Provides:       tex(t1xsc.vf)
Provides:       tex(t1xsl.tfm)
Provides:       tex(t1xsl.vf)
Provides:       tex(t1xss.tfm)
Provides:       tex(t1xss.vf)
Provides:       tex(t1xsssc.tfm)
Provides:       tex(t1xsssc.vf)
Provides:       tex(t1xsssl.tfm)
Provides:       tex(t1xsssl.vf)
Provides:       tex(t1xtt.tfm)
Provides:       tex(t1xttsc.tfm)
Provides:       tex(t1xttsl.tfm)
Provides:       tex(tcxb.tfm)
Provides:       tex(tcxb.vf)
Provides:       tex(tcxbi.tfm)
Provides:       tex(tcxbi.vf)
Provides:       tex(tcxbsl.tfm)
Provides:       tex(tcxbsl.vf)
Provides:       tex(tcxbss.tfm)
Provides:       tex(tcxbss.vf)
Provides:       tex(tcxbsssl.tfm)
Provides:       tex(tcxbsssl.vf)
Provides:       tex(tcxbtt.tfm)
Provides:       tex(tcxbttsl.tfm)
Provides:       tex(tcxi.tfm)
Provides:       tex(tcxi.vf)
Provides:       tex(tcxr.tfm)
Provides:       tex(tcxr.vf)
Provides:       tex(tcxsl.tfm)
Provides:       tex(tcxsl.vf)
Provides:       tex(tcxss.tfm)
Provides:       tex(tcxss.vf)
Provides:       tex(tcxsssl.tfm)
Provides:       tex(tcxsssl.vf)
Provides:       tex(tcxtt.tfm)
Provides:       tex(tcxttsl.tfm)
Provides:       tex(ts1txr.fd)
Provides:       tex(ts1txss.fd)
Provides:       tex(ts1txtt.fd)
Provides:       tex(tx8r.enc)
Provides:       tex(txb.tfm)
Provides:       tex(txb.vf)
Provides:       tex(txbex.tfm)
Provides:       tex(txbexa.tfm)
Provides:       tex(txbi.tfm)
Provides:       tex(txbi.vf)
Provides:       tex(txbmi.tfm)
Provides:       tex(txbmi.vf)
Provides:       tex(txbmi1.tfm)
Provides:       tex(txbmi1.vf)
Provides:       tex(txbmia.tfm)
Provides:       tex(txbsc.tfm)
Provides:       tex(txbsc.vf)
Provides:       tex(txbsl.tfm)
Provides:       tex(txbsl.vf)
Provides:       tex(txbss.tfm)
Provides:       tex(txbss.vf)
Provides:       tex(txbsssc.tfm)
Provides:       tex(txbsssc.vf)
Provides:       tex(txbsssl.tfm)
Provides:       tex(txbsssl.vf)
Provides:       tex(txbsy.tfm)
Provides:       tex(txbsya.tfm)
Provides:       tex(txbsyb.tfm)
Provides:       tex(txbsyc.tfm)
Provides:       tex(txbtt.tfm)
Provides:       tex(txbttsc.tfm)
Provides:       tex(txbttsl.tfm)
Provides:       tex(txex.tfm)
Provides:       tex(txexa.tfm)
Provides:       tex(txfonts.map)
Provides:       tex(txfonts.sty)
Provides:       tex(txi.tfm)
Provides:       tex(txi.vf)
Provides:       tex(txmi.tfm)
Provides:       tex(txmi.vf)
Provides:       tex(txmi1.tfm)
Provides:       tex(txmi1.vf)
Provides:       tex(txmia.tfm)
Provides:       tex(txr.map)
Provides:       tex(txr.tfm)
Provides:       tex(txr.vf)
Provides:       tex(txr1.map)
Provides:       tex(txr2.map)
Provides:       tex(txr3.map)
Provides:       tex(txsc.tfm)
Provides:       tex(txsc.vf)
Provides:       tex(txsl.tfm)
Provides:       tex(txsl.vf)
Provides:       tex(txss.tfm)
Provides:       tex(txss.vf)
Provides:       tex(txsssc.tfm)
Provides:       tex(txsssc.vf)
Provides:       tex(txsssl.tfm)
Provides:       tex(txsssl.vf)
Provides:       tex(txsy.tfm)
Provides:       tex(txsya.tfm)
Provides:       tex(txsyb.tfm)
Provides:       tex(txsyc.tfm)
Provides:       tex(txtt.tfm)
Provides:       tex(txttsc.tfm)
Provides:       tex(txttsl.tfm)
Provides:       tex(tyxb.tfm)
Provides:       tex(tyxb.vf)
Provides:       tex(tyxbi.tfm)
Provides:       tex(tyxbi.vf)
Provides:       tex(tyxbsc.tfm)
Provides:       tex(tyxbsc.vf)
Provides:       tex(tyxbsl.tfm)
Provides:       tex(tyxbsl.vf)
Provides:       tex(tyxbss.tfm)
Provides:       tex(tyxbss.vf)
Provides:       tex(tyxbsssc.tfm)
Provides:       tex(tyxbsssc.vf)
Provides:       tex(tyxbsssl.tfm)
Provides:       tex(tyxbsssl.vf)
Provides:       tex(tyxbtt.tfm)
Provides:       tex(tyxbtt.vf)
Provides:       tex(tyxbttsc.tfm)
Provides:       tex(tyxbttsc.vf)
Provides:       tex(tyxbttsl.tfm)
Provides:       tex(tyxbttsl.vf)
Provides:       tex(tyxi.tfm)
Provides:       tex(tyxi.vf)
Provides:       tex(tyxr.tfm)
Provides:       tex(tyxr.vf)
Provides:       tex(tyxsc.tfm)
Provides:       tex(tyxsc.vf)
Provides:       tex(tyxsl.tfm)
Provides:       tex(tyxsl.vf)
Provides:       tex(tyxss.tfm)
Provides:       tex(tyxss.vf)
Provides:       tex(tyxsssc.tfm)
Provides:       tex(tyxsssc.vf)
Provides:       tex(tyxsssl.tfm)
Provides:       tex(tyxsssl.vf)
Provides:       tex(tyxtt.tfm)
Provides:       tex(tyxtt.vf)
Provides:       tex(tyxttsc.tfm)
Provides:       tex(tyxttsc.vf)
Provides:       tex(tyxttsl.tfm)
Provides:       tex(tyxttsl.vf)
Provides:       tex(utxexa.fd)
Provides:       tex(utxmia.fd)
Provides:       tex(utxr.fd)
Provides:       tex(utxss.fd)
Provides:       tex(utxsya.fd)
Provides:       tex(utxsyb.fd)
Provides:       tex(utxsyc.fd)
Provides:       tex(utxtt.fd)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source220:      txfonts.tar.xz
Source221:      txfonts.doc.tar.xz

%description -n texlive-txfonts
Txfonts supplies virtual text roman fonts using Adobe Times (or
URW NimbusRomNo9L) with some modified and additional text
symbols in the OT1, T1, and TS1 encodings; maths alphabets
using Times/URW Nimbus; maths fonts providing all the symbols
of the Computer Modern and AMS fonts, including all the Greek
capital letters from CMR; and additional maths fonts of various
other symbols. The set is complemented by a sans-serif set of
text fonts, based on Helvetica/NimbusSanL, and a monospace set.
All the fonts are in Type 1 format (AFM and PFB files), and are
supported by TeX metrics (VF and TFM files) and macros for use
with LaTeX.

%package -n texlive-txfonts-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Documentation for texlive-txfonts
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-txfonts-doc
This package includes the documentation for texlive-txfonts


%package -n texlive-txfonts-fonts
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Severed fonts for texlive-txfonts
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Fonts
URL:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-txfonts-fonts
The  separated fonts package for texlive-txfonts
%post -n texlive-txfonts
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap txfonts.map' >> /var/run/texlive/run-updmap

%postun -n texlive-txfonts 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap txfonts.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-txfonts
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-txfonts-fonts
%files -n texlive-txfonts-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/txfonts/00bug_fix.txt
%{_texmfdistdir}/doc/fonts/txfonts/COPYRIGHT
%{_texmfdistdir}/doc/fonts/txfonts/README
%{_texmfdistdir}/doc/fonts/txfonts/txfontsdoc.pdf
%{_texmfdistdir}/doc/fonts/txfonts/txfontsdoc.tex
%{_texmfdistdir}/doc/fonts/txfonts/txfontsdocA4.pdf
%{_texmfdistdir}/doc/fonts/txfonts/txfontsdocA4.tex
%{_texmfdistdir}/doc/fonts/txfonts/txmi.vpl

%files -n texlive-txfonts
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/afm/public/txfonts/rtcxb.afm
%{_texmfdistdir}/fonts/afm/public/txfonts/rtcxbi.afm
%{_texmfdistdir}/fonts/afm/public/txfonts/rtcxbss.afm
%{_texmfdistdir}/fonts/afm/public/txfonts/rtcxi.afm
%{_texmfdistdir}/fonts/afm/public/txfonts/rtcxr.afm
%{_texmfdistdir}/fonts/afm/public/txfonts/rtcxss.afm
%{_texmfdistdir}/fonts/afm/public/txfonts/rtxb.afm
%{_texmfdistdir}/fonts/afm/public/txfonts/rtxbi.afm
%{_texmfdistdir}/fonts/afm/public/txfonts/rtxbmi.afm
%{_texmfdistdir}/fonts/afm/public/txfonts/rtxbsc.afm
%{_texmfdistdir}/fonts/afm/public/txfonts/rtxbss.afm
%{_texmfdistdir}/fonts/afm/public/txfonts/rtxbsssc.afm
%{_texmfdistdir}/fonts/afm/public/txfonts/rtxi.afm
%{_texmfdistdir}/fonts/afm/public/txfonts/rtxmi.afm
%{_texmfdistdir}/fonts/afm/public/txfonts/rtxr.afm
%{_texmfdistdir}/fonts/afm/public/txfonts/rtxsc.afm
%{_texmfdistdir}/fonts/afm/public/txfonts/rtxss.afm
%{_texmfdistdir}/fonts/afm/public/txfonts/rtxsssc.afm
%{_texmfdistdir}/fonts/afm/public/txfonts/t1xbtt.afm
%{_texmfdistdir}/fonts/afm/public/txfonts/t1xbttsc.afm
%{_texmfdistdir}/fonts/afm/public/txfonts/t1xtt.afm
%{_texmfdistdir}/fonts/afm/public/txfonts/t1xttsc.afm
%{_texmfdistdir}/fonts/afm/public/txfonts/tcxbtt.afm
%{_texmfdistdir}/fonts/afm/public/txfonts/tcxtt.afm
%{_texmfdistdir}/fonts/afm/public/txfonts/txbex.afm
%{_texmfdistdir}/fonts/afm/public/txfonts/txbexa.afm
%{_texmfdistdir}/fonts/afm/public/txfonts/txbmia.afm
%{_texmfdistdir}/fonts/afm/public/txfonts/txbsy.afm
%{_texmfdistdir}/fonts/afm/public/txfonts/txbsya.afm
%{_texmfdistdir}/fonts/afm/public/txfonts/txbsyb.afm
%{_texmfdistdir}/fonts/afm/public/txfonts/txbsyc.afm
%{_texmfdistdir}/fonts/afm/public/txfonts/txbtt.afm
%{_texmfdistdir}/fonts/afm/public/txfonts/txbttsc.afm
%{_texmfdistdir}/fonts/afm/public/txfonts/txex.afm
%{_texmfdistdir}/fonts/afm/public/txfonts/txexa.afm
%{_texmfdistdir}/fonts/afm/public/txfonts/txmia.afm
%{_texmfdistdir}/fonts/afm/public/txfonts/txsy.afm
%{_texmfdistdir}/fonts/afm/public/txfonts/txsya.afm
%{_texmfdistdir}/fonts/afm/public/txfonts/txsyb.afm
%{_texmfdistdir}/fonts/afm/public/txfonts/txsyc.afm
%{_texmfdistdir}/fonts/afm/public/txfonts/txtt.afm
%{_texmfdistdir}/fonts/afm/public/txfonts/txttsc.afm
%{_texmfdistdir}/fonts/enc/dvips/txfonts/tx8r.enc
%{_texmfdistdir}/fonts/map/dvips/txfonts/txfonts.map
%{_texmfdistdir}/fonts/map/dvips/txfonts/txr.map
%{_texmfdistdir}/fonts/map/dvips/txfonts/txr1.map
%{_texmfdistdir}/fonts/map/dvips/txfonts/txr2.map
%{_texmfdistdir}/fonts/map/dvips/txfonts/txr3.map
%{_texmfdistdir}/fonts/tfm/public/txfonts/rtcxb.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/rtcxbi.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/rtcxbsl.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/rtcxbss.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/rtcxbsso.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/rtcxi.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/rtcxr.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/rtcxsl.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/rtcxss.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/rtcxsssl.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/rtxb.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/rtxbi.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/rtxbmi.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/rtxbsc.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/rtxbsl.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/rtxbss.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/rtxbsssc.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/rtxbsssl.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/rtxi.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/rtxmi.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/rtxphvb.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/rtxphvbo.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/rtxphvr.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/rtxphvro.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/rtxptmb.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/rtxptmbi.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/rtxptmbo.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/rtxptmr.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/rtxptmri.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/rtxptmro.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/rtxr.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/rtxsc.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/rtxsl.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/rtxss.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/rtxsssc.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/rtxsssl.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/t1xb.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/t1xbi.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/t1xbsc.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/t1xbsl.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/t1xbss.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/t1xbsssc.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/t1xbsssl.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/t1xbtt.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/t1xbttsc.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/t1xbttsl.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/t1xi.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/t1xr.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/t1xsc.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/t1xsl.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/t1xss.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/t1xsssc.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/t1xsssl.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/t1xtt.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/t1xttsc.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/t1xttsl.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/tcxb.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/tcxbi.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/tcxbsl.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/tcxbss.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/tcxbsssl.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/tcxbtt.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/tcxbttsl.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/tcxi.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/tcxr.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/tcxsl.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/tcxss.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/tcxsssl.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/tcxtt.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/tcxttsl.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/txb.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/txbex.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/txbexa.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/txbi.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/txbmi.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/txbmi1.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/txbmia.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/txbsc.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/txbsl.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/txbss.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/txbsssc.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/txbsssl.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/txbsy.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/txbsya.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/txbsyb.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/txbsyc.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/txbtt.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/txbttsc.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/txbttsl.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/txex.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/txexa.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/txi.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/txmi.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/txmi1.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/txmia.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/txr.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/txsc.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/txsl.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/txss.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/txsssc.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/txsssl.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/txsy.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/txsya.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/txsyb.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/txsyc.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/txtt.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/txttsc.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/txttsl.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/tyxb.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/tyxbi.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/tyxbsc.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/tyxbsl.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/tyxbss.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/tyxbsssc.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/tyxbsssl.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/tyxbtt.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/tyxbttsc.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/tyxbttsl.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/tyxi.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/tyxr.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/tyxsc.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/tyxsl.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/tyxss.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/tyxsssc.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/tyxsssl.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/tyxtt.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/tyxttsc.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/tyxttsl.tfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/txfonts/rtcxb.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/txfonts/rtcxbi.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/txfonts/rtcxbss.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/txfonts/rtcxi.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/txfonts/rtcxr.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/txfonts/rtcxss.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/txfonts/rtxb.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/txfonts/rtxbi.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/txfonts/rtxbmi.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/txfonts/rtxbsc.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/txfonts/rtxbss.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/txfonts/rtxbsssc.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/txfonts/rtxi.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/txfonts/rtxmi.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/txfonts/rtxr.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/txfonts/rtxsc.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/txfonts/rtxss.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/txfonts/rtxsssc.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/txfonts/t1xbtt.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/txfonts/t1xbttsc.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/txfonts/t1xtt.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/txfonts/t1xttsc.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/txfonts/tcxbtt.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/txfonts/tcxtt.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/txfonts/txbex.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/txfonts/txbexa.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/txfonts/txbmia.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/txfonts/txbsy.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/txfonts/txbsya.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/txfonts/txbsyb.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/txfonts/txbsyc.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/txfonts/txbtt.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/txfonts/txbttsc.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/txfonts/txex.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/txfonts/txexa.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/txfonts/txmia.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/txfonts/txsy.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/txfonts/txsya.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/txfonts/txsyb.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/txfonts/txsyc.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/txfonts/txtt.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/txfonts/txttsc.pfb
%{_texmfdistdir}/fonts/vf/public/txfonts/t1xb.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/t1xbi.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/t1xbsc.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/t1xbsl.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/t1xbss.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/t1xbsssc.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/t1xbsssl.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/t1xi.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/t1xr.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/t1xsc.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/t1xsl.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/t1xss.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/t1xsssc.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/t1xsssl.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/tcxb.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/tcxbi.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/tcxbsl.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/tcxbss.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/tcxbsssl.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/tcxi.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/tcxr.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/tcxsl.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/tcxss.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/tcxsssl.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/txb.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/txbi.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/txbmi.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/txbmi1.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/txbsc.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/txbsl.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/txbss.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/txbsssc.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/txbsssl.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/txi.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/txmi.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/txmi1.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/txr.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/txsc.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/txsl.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/txss.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/txsssc.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/txsssl.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/tyxb.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/tyxbi.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/tyxbsc.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/tyxbsl.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/tyxbss.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/tyxbsssc.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/tyxbsssl.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/tyxbtt.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/tyxbttsc.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/tyxbttsl.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/tyxi.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/tyxr.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/tyxsc.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/tyxsl.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/tyxss.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/tyxsssc.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/tyxsssl.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/tyxtt.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/tyxttsc.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/tyxttsl.vf
%{_texmfdistdir}/tex/latex/txfonts/ly1txr.fd
%{_texmfdistdir}/tex/latex/txfonts/ly1txss.fd
%{_texmfdistdir}/tex/latex/txfonts/ly1txtt.fd
%{_texmfdistdir}/tex/latex/txfonts/omltxmi.fd
%{_texmfdistdir}/tex/latex/txfonts/omltxr.fd
%{_texmfdistdir}/tex/latex/txfonts/omstxr.fd
%{_texmfdistdir}/tex/latex/txfonts/omstxsy.fd
%{_texmfdistdir}/tex/latex/txfonts/omxtxex.fd
%{_texmfdistdir}/tex/latex/txfonts/ot1txr.fd
%{_texmfdistdir}/tex/latex/txfonts/ot1txss.fd
%{_texmfdistdir}/tex/latex/txfonts/ot1txtt.fd
%{_texmfdistdir}/tex/latex/txfonts/t1txr.fd
%{_texmfdistdir}/tex/latex/txfonts/t1txss.fd
%{_texmfdistdir}/tex/latex/txfonts/t1txtt.fd
%{_texmfdistdir}/tex/latex/txfonts/ts1txr.fd
%{_texmfdistdir}/tex/latex/txfonts/ts1txss.fd
%{_texmfdistdir}/tex/latex/txfonts/ts1txtt.fd
%{_texmfdistdir}/tex/latex/txfonts/txfonts.sty
%{_texmfdistdir}/tex/latex/txfonts/utxexa.fd
%{_texmfdistdir}/tex/latex/txfonts/utxmia.fd
%{_texmfdistdir}/tex/latex/txfonts/utxr.fd
%{_texmfdistdir}/tex/latex/txfonts/utxss.fd
%{_texmfdistdir}/tex/latex/txfonts/utxsya.fd
%{_texmfdistdir}/tex/latex/txfonts/utxsyb.fd
%{_texmfdistdir}/tex/latex/txfonts/utxsyc.fd
%{_texmfdistdir}/tex/latex/txfonts/utxtt.fd

%files -n texlive-txfonts-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-txfonts
%{_datadir}/fontconfig/conf.avail/58-texlive-txfonts.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-txfonts/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-txfonts/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-txfonts/fonts.scale
%{_datadir}/fonts/texlive-txfonts/rtcxb.pfb
%{_datadir}/fonts/texlive-txfonts/rtcxbi.pfb
%{_datadir}/fonts/texlive-txfonts/rtcxbss.pfb
%{_datadir}/fonts/texlive-txfonts/rtcxi.pfb
%{_datadir}/fonts/texlive-txfonts/rtcxr.pfb
%{_datadir}/fonts/texlive-txfonts/rtcxss.pfb
%{_datadir}/fonts/texlive-txfonts/rtxb.pfb
%{_datadir}/fonts/texlive-txfonts/rtxbi.pfb
%{_datadir}/fonts/texlive-txfonts/rtxbmi.pfb
%{_datadir}/fonts/texlive-txfonts/rtxbsc.pfb
%{_datadir}/fonts/texlive-txfonts/rtxbss.pfb
%{_datadir}/fonts/texlive-txfonts/rtxbsssc.pfb
%{_datadir}/fonts/texlive-txfonts/rtxi.pfb
%{_datadir}/fonts/texlive-txfonts/rtxmi.pfb
%{_datadir}/fonts/texlive-txfonts/rtxr.pfb
%{_datadir}/fonts/texlive-txfonts/rtxsc.pfb
%{_datadir}/fonts/texlive-txfonts/rtxss.pfb
%{_datadir}/fonts/texlive-txfonts/rtxsssc.pfb
%{_datadir}/fonts/texlive-txfonts/t1xbtt.pfb
%{_datadir}/fonts/texlive-txfonts/t1xbttsc.pfb
%{_datadir}/fonts/texlive-txfonts/t1xtt.pfb
%{_datadir}/fonts/texlive-txfonts/t1xttsc.pfb
%{_datadir}/fonts/texlive-txfonts/tcxbtt.pfb
%{_datadir}/fonts/texlive-txfonts/tcxtt.pfb
%{_datadir}/fonts/texlive-txfonts/txbex.pfb
%{_datadir}/fonts/texlive-txfonts/txbexa.pfb
%{_datadir}/fonts/texlive-txfonts/txbmia.pfb
%{_datadir}/fonts/texlive-txfonts/txbsy.pfb
%{_datadir}/fonts/texlive-txfonts/txbsya.pfb
%{_datadir}/fonts/texlive-txfonts/txbsyb.pfb
%{_datadir}/fonts/texlive-txfonts/txbsyc.pfb
%{_datadir}/fonts/texlive-txfonts/txbtt.pfb
%{_datadir}/fonts/texlive-txfonts/txbttsc.pfb
%{_datadir}/fonts/texlive-txfonts/txex.pfb
%{_datadir}/fonts/texlive-txfonts/txexa.pfb
%{_datadir}/fonts/texlive-txfonts/txmia.pfb
%{_datadir}/fonts/texlive-txfonts/txsy.pfb
%{_datadir}/fonts/texlive-txfonts/txsya.pfb
%{_datadir}/fonts/texlive-txfonts/txsyb.pfb
%{_datadir}/fonts/texlive-txfonts/txsyc.pfb
%{_datadir}/fonts/texlive-txfonts/txtt.pfb
%{_datadir}/fonts/texlive-txfonts/txttsc.pfb
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-txfonts-fonts-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif

%package -n texlive-txfontsb
Version:        %{texlive_version}.%{texlive_noarch}.1.1.1svn54512
Release:        0
Summary:        Extensions to txfonts, using GNU Freefont
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
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
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Requires:       texlive-txfontsb-fonts >= %{texlive_version}
Recommends:     texlive-txfontsb-doc >= %{texlive_version}
Provides:       tex(gptimes.enc)
Provides:       tex(gptimes.map)
Provides:       tex(gptimesy.enc)
Provides:       tex(gtimesb6a.tfm)
Provides:       tex(gtimesb6a.vf)
Provides:       tex(gtimesb6r.tfm)
Provides:       tex(gtimesbi6a.tfm)
Provides:       tex(gtimesbi6a.vf)
Provides:       tex(gtimesbi6r.tfm)
Provides:       tex(gtimesg6r.tfm)
Provides:       tex(gtimesi6a.tfm)
Provides:       tex(gtimesi6a.vf)
Provides:       tex(gtimesi6r.tfm)
Provides:       tex(gtimesrg6a.tfm)
Provides:       tex(gtimesrg6a.vf)
Provides:       tex(gtimessc6a.tfm)
Provides:       tex(gtimessc6a.vf)
Provides:       tex(gtimessc6r.tfm)
Provides:       tex(gtimessco6a.tfm)
Provides:       tex(gtimessco6a.vf)
Provides:       tex(gtimessco6r.tfm)
Provides:       tex(gtimesyb6a.tfm)
Provides:       tex(gtimesyb6a.vf)
Provides:       tex(gtimesyb6r.tfm)
Provides:       tex(gtimesybi6a.tfm)
Provides:       tex(gtimesybi6a.vf)
Provides:       tex(gtimesybi6r.tfm)
Provides:       tex(gtimesyg6r.tfm)
Provides:       tex(gtimesyi6a.tfm)
Provides:       tex(gtimesyi6a.vf)
Provides:       tex(gtimesyi6r.tfm)
Provides:       tex(gtimesyrg6a.tfm)
Provides:       tex(gtimesyrg6a.vf)
Provides:       tex(gtimesysc6a.tfm)
Provides:       tex(gtimesysc6a.vf)
Provides:       tex(gtimesysc6r.tfm)
Provides:       tex(gtimesysco6a.tfm)
Provides:       tex(gtimesysco6a.vf)
Provides:       tex(gtimesysco6r.tfm)
Provides:       tex(lgrtxr.fd)
Provides:       tex(lgrtxrc.fd)
Provides:       tex(lgrtxry.fd)
Provides:       tex(lgrtxryc.fd)
Provides:       tex(ot1txrc.fd)
Provides:       tex(ot1txryc.fd)
Provides:       tex(timessc6a.tfm)
Provides:       tex(timessc6a.vf)
Provides:       tex(timessc6r.tfm)
Provides:       tex(timessco6a.tfm)
Provides:       tex(timessco6a.vf)
Provides:       tex(timessco6r.tfm)
Provides:       tex(txfontsb.sty)
Requires:       tex(txfonts.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source222:      txfontsb.tar.xz
Source223:      txfontsb.doc.tar.xz

%description -n texlive-txfontsb
A set of fonts that extend the txfonts bundle with small caps
and old style numbers, together with Greek support. The
extensions are made with modifications of the GNU Freefont.

%package -n texlive-txfontsb-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1.1svn54512
Release:        0
Summary:        Documentation for texlive-txfontsb
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-txfontsb-doc
This package includes the documentation for texlive-txfontsb


%package -n texlive-txfontsb-fonts
Version:        %{texlive_version}.%{texlive_noarch}.1.1.1svn54512
Release:        0
Summary:        Severed fonts for texlive-txfontsb
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Fonts
URL:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-txfontsb-fonts
The  separated fonts package for texlive-txfontsb
%post -n texlive-txfontsb
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap gptimes.map' >> /var/run/texlive/run-updmap

%postun -n texlive-txfontsb 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap gptimes.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-txfontsb
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-txfontsb-fonts
%files -n texlive-txfontsb-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/txfontsb/README
%{_texmfdistdir}/doc/fonts/txfontsb/txfontsb.pdf
%{_texmfdistdir}/doc/fonts/txfontsb/txfontsb.tex

%files -n texlive-txfontsb
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/afm/public/txfontsb/FreeSerifb-SmallCaps.afm
%{_texmfdistdir}/fonts/afm/public/txfontsb/FreeSerifb-SmallCapsAlt.afm
%{_texmfdistdir}/fonts/afm/public/txfontsb/FreeSerifb.afm
%{_texmfdistdir}/fonts/afm/public/txfontsb/FreeSerifbBold.afm
%{_texmfdistdir}/fonts/afm/public/txfontsb/FreeSerifbBoldItalic.afm
%{_texmfdistdir}/fonts/afm/public/txfontsb/FreeSerifbItalic.afm
%{_texmfdistdir}/fonts/enc/dvips/txfontsb/gptimes.enc
%{_texmfdistdir}/fonts/enc/dvips/txfontsb/gptimesy.enc
%{_texmfdistdir}/fonts/map/dvips/txfontsb/gptimes.map
%verify(link) %{_texmfdistdir}/fonts/opentype/public/txfontsb/FreeSerifb-SmallCaps.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/txfontsb/FreeSerifb-SmallCapsAlt.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/txfontsb/FreeSerifb.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/txfontsb/FreeSerifbBold.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/txfontsb/FreeSerifbBoldItalic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/txfontsb/FreeSerifbItalic.otf
%{_texmfdistdir}/fonts/tfm/public/txfontsb/gtimesb6a.tfm
%{_texmfdistdir}/fonts/tfm/public/txfontsb/gtimesb6r.tfm
%{_texmfdistdir}/fonts/tfm/public/txfontsb/gtimesbi6a.tfm
%{_texmfdistdir}/fonts/tfm/public/txfontsb/gtimesbi6r.tfm
%{_texmfdistdir}/fonts/tfm/public/txfontsb/gtimesg6r.tfm
%{_texmfdistdir}/fonts/tfm/public/txfontsb/gtimesi6a.tfm
%{_texmfdistdir}/fonts/tfm/public/txfontsb/gtimesi6r.tfm
%{_texmfdistdir}/fonts/tfm/public/txfontsb/gtimesrg6a.tfm
%{_texmfdistdir}/fonts/tfm/public/txfontsb/gtimessc6a.tfm
%{_texmfdistdir}/fonts/tfm/public/txfontsb/gtimessc6r.tfm
%{_texmfdistdir}/fonts/tfm/public/txfontsb/gtimessco6a.tfm
%{_texmfdistdir}/fonts/tfm/public/txfontsb/gtimessco6r.tfm
%{_texmfdistdir}/fonts/tfm/public/txfontsb/gtimesyb6a.tfm
%{_texmfdistdir}/fonts/tfm/public/txfontsb/gtimesyb6r.tfm
%{_texmfdistdir}/fonts/tfm/public/txfontsb/gtimesybi6a.tfm
%{_texmfdistdir}/fonts/tfm/public/txfontsb/gtimesybi6r.tfm
%{_texmfdistdir}/fonts/tfm/public/txfontsb/gtimesyg6r.tfm
%{_texmfdistdir}/fonts/tfm/public/txfontsb/gtimesyi6a.tfm
%{_texmfdistdir}/fonts/tfm/public/txfontsb/gtimesyi6r.tfm
%{_texmfdistdir}/fonts/tfm/public/txfontsb/gtimesyrg6a.tfm
%{_texmfdistdir}/fonts/tfm/public/txfontsb/gtimesysc6a.tfm
%{_texmfdistdir}/fonts/tfm/public/txfontsb/gtimesysc6r.tfm
%{_texmfdistdir}/fonts/tfm/public/txfontsb/gtimesysco6a.tfm
%{_texmfdistdir}/fonts/tfm/public/txfontsb/gtimesysco6r.tfm
%{_texmfdistdir}/fonts/tfm/public/txfontsb/timessc6a.tfm
%{_texmfdistdir}/fonts/tfm/public/txfontsb/timessc6r.tfm
%{_texmfdistdir}/fonts/tfm/public/txfontsb/timessco6a.tfm
%{_texmfdistdir}/fonts/tfm/public/txfontsb/timessco6r.tfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/txfontsb/FreeSerifb-SmallCaps.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/txfontsb/FreeSerifb-SmallCapsAlt.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/txfontsb/FreeSerifb.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/txfontsb/FreeSerifbBold.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/txfontsb/FreeSerifbBoldItalic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/txfontsb/FreeSerifbItalic.pfb
%{_texmfdistdir}/fonts/vf/public/txfontsb/gtimesb6a.vf
%{_texmfdistdir}/fonts/vf/public/txfontsb/gtimesbi6a.vf
%{_texmfdistdir}/fonts/vf/public/txfontsb/gtimesi6a.vf
%{_texmfdistdir}/fonts/vf/public/txfontsb/gtimesrg6a.vf
%{_texmfdistdir}/fonts/vf/public/txfontsb/gtimessc6a.vf
%{_texmfdistdir}/fonts/vf/public/txfontsb/gtimessco6a.vf
%{_texmfdistdir}/fonts/vf/public/txfontsb/gtimesyb6a.vf
%{_texmfdistdir}/fonts/vf/public/txfontsb/gtimesybi6a.vf
%{_texmfdistdir}/fonts/vf/public/txfontsb/gtimesyi6a.vf
%{_texmfdistdir}/fonts/vf/public/txfontsb/gtimesyrg6a.vf
%{_texmfdistdir}/fonts/vf/public/txfontsb/gtimesysc6a.vf
%{_texmfdistdir}/fonts/vf/public/txfontsb/gtimesysco6a.vf
%{_texmfdistdir}/fonts/vf/public/txfontsb/timessc6a.vf
%{_texmfdistdir}/fonts/vf/public/txfontsb/timessco6a.vf
%{_texmfdistdir}/tex/latex/txfontsb/lgrtxr.fd
%{_texmfdistdir}/tex/latex/txfontsb/lgrtxrc.fd
%{_texmfdistdir}/tex/latex/txfontsb/lgrtxry.fd
%{_texmfdistdir}/tex/latex/txfontsb/lgrtxryc.fd
%{_texmfdistdir}/tex/latex/txfontsb/ot1txrc.fd
%{_texmfdistdir}/tex/latex/txfontsb/ot1txryc.fd
%{_texmfdistdir}/tex/latex/txfontsb/txfontsb.sty

%files -n texlive-txfontsb-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-txfontsb
%{_datadir}/fontconfig/conf.avail/58-texlive-txfontsb.conf
%{_datadir}/fontconfig/conf.avail/55-texlive-txfontsb.conf
%config %{_sysconfdir}/fonts/conf.d/55-texlive-txfontsb.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-txfontsb/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-txfontsb/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-txfontsb/fonts.scale
%{_datadir}/fonts/texlive-txfontsb/FreeSerifb-SmallCaps.otf
%{_datadir}/fonts/texlive-txfontsb/FreeSerifb-SmallCapsAlt.otf
%{_datadir}/fonts/texlive-txfontsb/FreeSerifb.otf
%{_datadir}/fonts/texlive-txfontsb/FreeSerifbBold.otf
%{_datadir}/fonts/texlive-txfontsb/FreeSerifbBoldItalic.otf
%{_datadir}/fonts/texlive-txfontsb/FreeSerifbItalic.otf
%{_datadir}/fonts/texlive-txfontsb/FreeSerifb-SmallCaps.pfb
%{_datadir}/fonts/texlive-txfontsb/FreeSerifb-SmallCapsAlt.pfb
%{_datadir}/fonts/texlive-txfontsb/FreeSerifb.pfb
%{_datadir}/fonts/texlive-txfontsb/FreeSerifbBold.pfb
%{_datadir}/fonts/texlive-txfontsb/FreeSerifbBoldItalic.pfb
%{_datadir}/fonts/texlive-txfontsb/FreeSerifbItalic.pfb
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-txfontsb-fonts-%{texlive_version}.%{texlive_noarch}.1.1.1svn54512-%{release}-zypper
%endif

%package -n texlive-txgreeks
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn21839
Release:        0
Summary:        Shape selection for TX fonts Greek letters
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-txgreeks-doc >= %{texlive_version}
Provides:       tex(txgreeks.sty)
Requires:       tex(txfonts.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source224:      txgreeks.tar.xz
Source225:      txgreeks.doc.tar.xz

%description -n texlive-txgreeks
The package allows LaTeX users who use the TX fonts to select
the shapes (italic or upright) for the Greek lowercase and
uppercase letters. Once the shapes for lowercase and uppercase
have been selected via a package option, the \other prefix
(e.g., \otheralpha) allows using the alternate glyph (as in the
fourier package). The txgreeks package does not constrain the
text font that may be used in the document.

%package -n texlive-txgreeks-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn21839
Release:        0
Summary:        Documentation for texlive-txgreeks
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-txgreeks-doc
This package includes the documentation for texlive-txgreeks

%post -n texlive-txgreeks
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-txgreeks 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-txgreeks
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-txgreeks-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/txgreeks/README
%{_texmfdistdir}/doc/latex/txgreeks/txgreeks.pdf

%files -n texlive-txgreeks
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/txgreeks/txgreeks.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-txgreeks-%{texlive_version}.%{texlive_noarch}.1.0svn21839-%{release}-zypper
%endif

%package -n texlive-txuprcal
Version:        %{texlive_version}.%{texlive_noarch}.1.00svn43327
Release:        0
Summary:        Upright calligraphic font based on TX calligraphic
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
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
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Requires:       texlive-txuprcal-fonts >= %{texlive_version}
Recommends:     texlive-txuprcal-doc >= %{texlive_version}
Provides:       tex(TXUprCal.map)
Provides:       tex(txUprCal-Bold.tfm)
Provides:       tex(txUprCal-Regular.tfm)
Provides:       tex(txuprcal.sty)
Provides:       tex(utxuprcal.fd)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source226:      txuprcal.tar.xz
Source227:      txuprcal.doc.tar.xz

%description -n texlive-txuprcal
This small package provides a means of loading as \mathcal an
uprighted version of the calligraphic fonts from the TX font
package. A scaled option to provided to allow arbitrary
scaling.

%package -n texlive-txuprcal-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.00svn43327
Release:        0
Summary:        Documentation for texlive-txuprcal
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-txuprcal-doc
This package includes the documentation for texlive-txuprcal


%package -n texlive-txuprcal-fonts
Version:        %{texlive_version}.%{texlive_noarch}.1.00svn43327
Release:        0
Summary:        Severed fonts for texlive-txuprcal
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Fonts
URL:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-txuprcal-fonts
The  separated fonts package for texlive-txuprcal
%post -n texlive-txuprcal
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap TXUprCal.map' >> /var/run/texlive/run-updmap

%postun -n texlive-txuprcal 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap TXUprCal.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-txuprcal
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-txuprcal-fonts
%files -n texlive-txuprcal-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/txuprcal/README
%{_texmfdistdir}/doc/fonts/txuprcal/txuprcal-doc.pdf
%{_texmfdistdir}/doc/fonts/txuprcal/txuprcal-doc.tex

%files -n texlive-txuprcal
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/map/dvips/txuprcal/TXUprCal.map
%{_texmfdistdir}/fonts/tfm/public/txuprcal/txUprCal-Bold.tfm
%{_texmfdistdir}/fonts/tfm/public/txuprcal/txUprCal-Regular.tfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/txuprcal/txuprcal-bold.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/txuprcal/txuprcal-reg.pfb
%{_texmfdistdir}/tex/latex/txuprcal/txuprcal.sty
%{_texmfdistdir}/tex/latex/txuprcal/utxuprcal.fd

%files -n texlive-txuprcal-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-txuprcal
%{_datadir}/fontconfig/conf.avail/58-texlive-txuprcal.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-txuprcal/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-txuprcal/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-txuprcal/fonts.scale
%{_datadir}/fonts/texlive-txuprcal/txuprcal-bold.pfb
%{_datadir}/fonts/texlive-txuprcal/txuprcal-reg.pfb
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-txuprcal-fonts-%{texlive_version}.%{texlive_noarch}.1.00svn43327-%{release}-zypper
%endif

%package -n texlive-type1cm
Version:        %{texlive_version}.%{texlive_noarch}.svn21820
Release:        0
Summary:        Arbitrary size font selection in LaTeX
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-type1cm-doc >= %{texlive_version}
Provides:       tex(type1cm.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source228:      type1cm.tar.xz
Source229:      type1cm.doc.tar.xz

%description -n texlive-type1cm
LaTeX, by default, restricts the sizes at which you can use its
default computer modern fonts, to a fixed set of discrete sizes
(effectively, a set specified by Knuth). The type1cm package
removes this restriction; this is particularly useful when
using scalable versions of the cm fonts (Bakoma, or the
versions from BSR/Y&Y, or True Type versions from Kinch, PCTeX,
etc.). In fact, since modern distributions will automatically
generate any bitmap font you might need, type1cm has wider
application than just those using scaleable versions of the
fonts. Note that the LaTeX distribution now contains a package
fix-cm, which performs the task of type1cm, as well as doing
the same job for T1- and TS1-encoded ec fonts.

%package -n texlive-type1cm-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn21820
Release:        0
Summary:        Documentation for texlive-type1cm
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-type1cm-doc
This package includes the documentation for texlive-type1cm

%post -n texlive-type1cm
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-type1cm 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-type1cm
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-type1cm-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/type1cm/type1cm-doc.pdf
%{_texmfdistdir}/doc/latex/type1cm/type1cm-doc.tex
%{_texmfdistdir}/doc/latex/type1cm/type1cm.txt

%files -n texlive-type1cm
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/type1cm/type1cm.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-type1cm-%{texlive_version}.%{texlive_noarch}.svn21820-%{release}-zypper
%endif

%package -n texlive-typed-checklist
Version:        %{texlive_version}.%{texlive_noarch}.2.0svn49731
Release:        0
Summary:        Typesetting tasks, goals, milestones, artifacts, and more in LaTeX
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-typed-checklist-doc >= %{texlive_version}
Provides:       tex(typed-checklist.sty)
Requires:       tex(array.sty)
Requires:       tex(asciilist.sty)
Requires:       tex(bbding.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(longtable.sty)
Requires:       tex(marginnote.sty)
Requires:       tex(tabu.sty)
Requires:       tex(tabularx.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xltabular.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source230:      typed-checklist.tar.xz
Source231:      typed-checklist.doc.tar.xz

%description -n texlive-typed-checklist
The main goal of this package is to provide means for
typesetting checklists in a way that stipulates users to
explicitly distinguish checklists for goals, for tasks, for
artifacts, and for milestones -- i.e., the type of checklist
entries. The intention behind this is that a user of the
package is coerced to think about what kind of entries he/she
adds to the checklist. This shall yield a clearer result and,
in the long run, help with training to distinguish entries of
different types.

%package -n texlive-typed-checklist-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.0svn49731
Release:        0
Summary:        Documentation for texlive-typed-checklist
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-typed-checklist-doc
This package includes the documentation for texlive-typed-checklist

%post -n texlive-typed-checklist
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-typed-checklist 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-typed-checklist
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-typed-checklist-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/typed-checklist/README.md
%{_texmfdistdir}/doc/latex/typed-checklist/typed-checklist.pdf

%files -n texlive-typed-checklist
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/typed-checklist/typed-checklist.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-typed-checklist-%{texlive_version}.%{texlive_noarch}.2.0svn49731-%{release}-zypper
%endif

%package -n texlive-typeface
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn27046
Release:        0
Summary:        Select a balanced set of fonts
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-typeface-doc >= %{texlive_version}
Provides:       tex(typeface.cfg)
Provides:       tex(typeface.sty)
Requires:       tex(anyfontsize.sty)
Requires:       tex(array.sty)
Requires:       tex(etexcmds.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(fix-cm.sty)
Requires:       tex(fixmath.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(ifetex.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(iftex.sty)
Requires:       tex(ifthenx.sty)
Requires:       tex(mathtools.sty)
Requires:       tex(nfssext-cfr.sty)
Requires:       tex(scalefnt.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source232:      typeface.tar.xz
Source233:      typeface.doc.tar.xz

%description -n texlive-typeface
The package provides the means of establishing a consistent set
of fonts for use in a LaTeX document. It allows mixing and
matching the Type 1 font sets available on the archive (and it
may be extended, via its configuration file, to support other
fonts). Font-set definition takes the form of a set of options
that are read when the package is loaded: for each typographic
category (main body font, sans-serif font, monospace font,
mathematics fonts, text figures, and so on), a font or a
transformation is given in those options. The approach enables
the user to remember their own configurations (as a single
command) and to borrow configurations that other users have
developed. The present release is designated "for review".

%package -n texlive-typeface-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn27046
Release:        0
Summary:        Documentation for texlive-typeface
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-typeface-doc
This package includes the documentation for texlive-typeface

%post -n texlive-typeface
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-typeface 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-typeface
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-typeface-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/typeface/README
%{_texmfdistdir}/doc/latex/typeface/typeface-all-rm.pdf
%{_texmfdistdir}/doc/latex/typeface/typeface-test.tex
%{_texmfdistdir}/doc/latex/typeface/typeface.pdf
%{_texmfdistdir}/doc/latex/typeface/typeface.tex

%files -n texlive-typeface
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/typeface/typeface.cfg
%{_texmfdistdir}/tex/latex/typeface/typeface.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-typeface-%{texlive_version}.%{texlive_noarch}.0.0.1svn27046-%{release}-zypper
%endif

%package -n texlive-typehtml
Version:        %{texlive_version}.%{texlive_noarch}.svn17134
Release:        0
Summary:        Typeset HTML directly from LaTeX
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-typehtml-doc >= %{texlive_version}
Provides:       tex(typehtml.sty)
Requires:       tex(exscale.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source234:      typehtml.tar.xz
Source235:      typehtml.doc.tar.xz

%description -n texlive-typehtml
Can handle almost all of HTML2, and most of the math fragment
of the draft HTML3.

%package -n texlive-typehtml-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn17134
Release:        0
Summary:        Documentation for texlive-typehtml
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-typehtml-doc
This package includes the documentation for texlive-typehtml

%post -n texlive-typehtml
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-typehtml 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-typehtml
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-typehtml-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/typehtml/README
%{_texmfdistdir}/doc/latex/typehtml/typehtml.pdf

%files -n texlive-typehtml
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/typehtml/typehtml.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-typehtml-%{texlive_version}.%{texlive_noarch}.svn17134-%{release}-zypper
%endif

%package -n texlive-typeoutfileinfo
Version:        %{texlive_version}.%{texlive_noarch}.0.0.31svn29349
Release:        0
Summary:        Display class/package/file information
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-typeoutfileinfo-bin >= %{texlive_version}
#!BuildIgnore: texlive-typeoutfileinfo-bin
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-typeoutfileinfo-doc >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source236:      typeoutfileinfo.tar.xz
Source237:      typeoutfileinfo.doc.tar.xz

%description -n texlive-typeoutfileinfo
The package provides a minimalist shell script, for Unix
systems, that displays the information content in a
\ProvidesFile, \ProvidesPackage or \ProvidesClass command in a
LaTeX source file. The package requires that the readprov
package is available.

%package -n texlive-typeoutfileinfo-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.31svn29349
Release:        0
Summary:        Documentation for texlive-typeoutfileinfo
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-typeoutfileinfo-doc
This package includes the documentation for texlive-typeoutfileinfo

%post -n texlive-typeoutfileinfo
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-typeoutfileinfo 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-typeoutfileinfo
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-typeoutfileinfo-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/support/typeoutfileinfo/README

%files -n texlive-typeoutfileinfo
%defattr(-,root,root,755)
%{_texmfdistdir}/scripts/typeoutfileinfo/typeoutfileinfo.sh
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-typeoutfileinfo-%{texlive_version}.%{texlive_noarch}.0.0.31svn29349-%{release}-zypper
%endif

%package -n texlive-typewriter
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn46641
Release:        0
Summary:        Typeset with a randomly variable monospace font
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-typewriter-doc >= %{texlive_version}
Provides:       tex(typewriter.sty)
Requires:       tex(luaotfload.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source238:      typewriter.tar.xz
Source239:      typewriter.doc.tar.xz

%description -n texlive-typewriter
The typewriter package uses the OpenType Computer Modern
Unicode Typewriter font, together with a LuaTeX virtual font
setup that introduces random variability in grey level and
angle of each character. It was originally an answer to a
question on stackexchange.

%package -n texlive-typewriter-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn46641
Release:        0
Summary:        Documentation for texlive-typewriter
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-typewriter-doc
This package includes the documentation for texlive-typewriter

%post -n texlive-typewriter
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-typewriter 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-typewriter
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-typewriter-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/lualatex/typewriter/README.md
%{_texmfdistdir}/doc/lualatex/typewriter/typewriter-guide.pdf
%{_texmfdistdir}/doc/lualatex/typewriter/typewriter-guide.tex

%files -n texlive-typewriter
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/lualatex/typewriter/typewriter.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-typewriter-%{texlive_version}.%{texlive_noarch}.1.1svn46641-%{release}-zypper
%endif

%package -n texlive-typicons
Version:        %{texlive_version}.%{texlive_noarch}.2.0.7svn37623
Release:        0
Summary:        Font containing a set of web-related icons
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Requires:       texlive-typicons-fonts >= %{texlive_version}
Recommends:     texlive-typicons-doc >= %{texlive_version}
Provides:       tex(typicons.sty)
Requires:       tex(fontspec.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source240:      typicons.tar.xz
Source241:      typicons.doc.tar.xz

%description -n texlive-typicons
This package grants access to 336 web-related icons provided by
the included "Typicons" free font, designed by Stephen
Hutchings and released under the SIL Open Font License. See
http://www.typicons.com for more details about the font itself.
This package requires the fontspec package and either the
Xe(La)TeX or Lua(La)TeX engine to load the included ttf font.
Once the package is loaded, icons can be accessed through the
general \ticon command, which takes as argument the name of the
desired icon, or through direct commands specific to each icon.
The full list of icon designs, names and direct commands is
showcased in the manual.

%package -n texlive-typicons-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.0.7svn37623
Release:        0
Summary:        Documentation for texlive-typicons
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-typicons-doc
This package includes the documentation for texlive-typicons


%package -n texlive-typicons-fonts
Version:        %{texlive_version}.%{texlive_noarch}.2.0.7svn37623
Release:        0
Summary:        Severed fonts for texlive-typicons
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Fonts
URL:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-typicons-fonts
The  separated fonts package for texlive-typicons
%post -n texlive-typicons
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-typicons 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-typicons
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-typicons-fonts
%files -n texlive-typicons-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/typicons/README
%{_texmfdistdir}/doc/fonts/typicons/typicons.pdf
%{_texmfdistdir}/doc/fonts/typicons/typicons.tex

%files -n texlive-typicons
%defattr(-,root,root,755)
%verify(link) %{_texmfdistdir}/fonts/truetype/public/typicons/typicons.ttf
%{_texmfdistdir}/tex/latex/typicons/typicons.sty

%files -n texlive-typicons-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-typicons
%{_datadir}/fontconfig/conf.avail/58-texlive-typicons.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-typicons/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-typicons/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-typicons/fonts.scale
%{_datadir}/fonts/texlive-typicons/typicons.ttf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-typicons-fonts-%{texlive_version}.%{texlive_noarch}.2.0.7svn37623-%{release}-zypper
%endif

%package -n texlive-typoaid
Version:        %{texlive_version}.%{texlive_noarch}.0.0.4.7svn44238
Release:        0
Summary:        Macros for font diagnostics
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-typoaid-doc >= %{texlive_version}
Provides:       tex(typoaid.sty)
Requires:       tex(array.sty)
Requires:       tex(booktabs.sty)
Requires:       tex(expl3.sty)
Requires:       tex(siunitx.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source242:      typoaid.tar.xz
Source243:      typoaid.doc.tar.xz

%description -n texlive-typoaid
This package provides macros for measuring alphabet lengths
(i.e. the length occupied by the characters "abcd...xyz"),
em-widths and ex-heights, which may help in making typesetting
decisions. The package is compatible with pdfLaTeX, LuaLaTeX,
and XeLaTeX, and will accept font family switches defined via
the fontspec package. The plan is that future versions shall be
able to provide even more diagnostic tools, and some
LuaTeX-specific special commands, too. The package relies on
the following other LaTeX packages: expl3, array, booktabs, and
siunitx.

%package -n texlive-typoaid-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.4.7svn44238
Release:        0
Summary:        Documentation for texlive-typoaid
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-typoaid-doc
This package includes the documentation for texlive-typoaid

%post -n texlive-typoaid
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-typoaid 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-typoaid
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-typoaid-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/typoaid/README.md
%{_texmfdistdir}/doc/latex/typoaid/typoaid.pdf
%{_texmfdistdir}/doc/latex/typoaid/typoaid.tex

%files -n texlive-typoaid
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/typoaid/typoaid.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-typoaid-%{texlive_version}.%{texlive_noarch}.0.0.4.7svn44238-%{release}-zypper
%endif

%package -n texlive-typogrid
Version:        %{texlive_version}.%{texlive_noarch}.0.0.21svn24994
Release:        0
Summary:        Print a typographic grid
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-typogrid-doc >= %{texlive_version}
Provides:       tex(typogrid.sty)
Requires:       tex(calc.sty)
Requires:       tex(eso-pic.sty)
Requires:       tex(keyval.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source244:      typogrid.tar.xz
Source245:      typogrid.doc.tar.xz

%description -n texlive-typogrid
Draws a grid on every page of the document; the grid divides
the page into columns, and may be used for fixing measurements
of layout.

%package -n texlive-typogrid-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.21svn24994
Release:        0
Summary:        Documentation for texlive-typogrid
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-typogrid-doc
This package includes the documentation for texlive-typogrid

%post -n texlive-typogrid
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-typogrid 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-typogrid
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-typogrid-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/typogrid/ChangeLog
%{_texmfdistdir}/doc/latex/typogrid/Makefile
%{_texmfdistdir}/doc/latex/typogrid/README
%{_texmfdistdir}/doc/latex/typogrid/getversion.tex
%{_texmfdistdir}/doc/latex/typogrid/testtypogrid.tex
%{_texmfdistdir}/doc/latex/typogrid/typogrid.pdf

%files -n texlive-typogrid
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/typogrid/typogrid.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-typogrid-%{texlive_version}.%{texlive_noarch}.0.0.21svn24994-%{release}-zypper
%endif

%package -n texlive-uaclasses
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        University of Arizona thesis and dissertation format
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-uaclasses-doc >= %{texlive_version}
Provides:       tex(my-thesis.cls)
Provides:       tex(my-title.sty)
Provides:       tex(ua-thesis.cls)
Provides:       tex(ua-title.sty)
Requires:       tex(amsbook.cls)
Requires:       tex(amsfonts.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(amsthm.sty)
Requires:       tex(report.cls)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source246:      uaclasses.tar.xz
Source247:      uaclasses.doc.tar.xz

%description -n texlive-uaclasses
This package provides a LaTeX2e document class named
'ua-thesis' for typesetting theses and dissertations in the
official format required by the University of Arizona.
Moreover, there is a fully compatible alternative document
class 'my-thesis' for private 'nice' copies of the
dissertation, and the respective title pages are available as
separate packages to work with any document class.

%package -n texlive-uaclasses-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Documentation for texlive-uaclasses
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-uaclasses-doc
This package includes the documentation for texlive-uaclasses

%post -n texlive-uaclasses
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-uaclasses 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-uaclasses
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-uaclasses-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/uaclasses/README
%{_texmfdistdir}/doc/latex/uaclasses/my-example.pdf
%{_texmfdistdir}/doc/latex/uaclasses/ua-example.pdf
%{_texmfdistdir}/doc/latex/uaclasses/ua-example.tex

%files -n texlive-uaclasses
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/uaclasses/my-thesis.cls
%{_texmfdistdir}/tex/latex/uaclasses/my-title.sty
%{_texmfdistdir}/tex/latex/uaclasses/ua-thesis.cls
%{_texmfdistdir}/tex/latex/uaclasses/ua-title.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-uaclasses-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif

%package -n texlive-uafthesis
Version:        %{texlive_version}.%{texlive_noarch}.12.12svn29349
Release:        0
Summary:        Document class for theses at University of Alaska Fairbanks
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-uafthesis-doc >= %{texlive_version}
Provides:       tex(uafthesis.cls)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source248:      uafthesis.tar.xz
Source249:      uafthesis.doc.tar.xz

%description -n texlive-uafthesis
This is an "unofficial" official class.

%package -n texlive-uafthesis-doc
Version:        %{texlive_version}.%{texlive_noarch}.12.12svn29349
Release:        0
Summary:        Documentation for texlive-uafthesis
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-uafthesis-doc
This package includes the documentation for texlive-uafthesis

%post -n texlive-uafthesis
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-uafthesis 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-uafthesis
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-uafthesis-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/uafthesis/Makefile
%{_texmfdistdir}/doc/latex/uafthesis/README.md
%{_texmfdistdir}/doc/latex/uafthesis/bib_styles/agufull08.bst
%{_texmfdistdir}/doc/latex/uafthesis/bib_styles/unsrtabbrv3.bst
%{_texmfdistdir}/doc/latex/uafthesis/example/abstract.tex
%{_texmfdistdir}/doc/latex/uafthesis/example/acknowledgements.tex
%{_texmfdistdir}/doc/latex/uafthesis/example/apx1.tex
%{_texmfdistdir}/doc/latex/uafthesis/example/build.sh
%{_texmfdistdir}/doc/latex/uafthesis/example/ch1.tex
%{_texmfdistdir}/doc/latex/uafthesis/example/ch2.tex
%{_texmfdistdir}/doc/latex/uafthesis/example/ch3.tex
%{_texmfdistdir}/doc/latex/uafthesis/example/custom-macros.tex
%{_texmfdistdir}/doc/latex/uafthesis/example/example.loa.bk
%{_texmfdistdir}/doc/latex/uafthesis/example/example.tex
%{_texmfdistdir}/doc/latex/uafthesis/example/example.toc.bk
%{_texmfdistdir}/doc/latex/uafthesis/example/fig/fivebatteries.png
%{_texmfdistdir}/doc/latex/uafthesis/example/fig/onebattery.png
%{_texmfdistdir}/doc/latex/uafthesis/example/quotepage.tex

%files -n texlive-uafthesis
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/uafthesis/uafthesis.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-uafthesis-%{texlive_version}.%{texlive_noarch}.12.12svn29349-%{release}-zypper
%endif

%package -n texlive-uantwerpendocs
Version:        %{texlive_version}.%{texlive_noarch}.2.4svn51007
Release:        0
Summary:        Course texts, master theses, and exams in University of Antwerp style
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-uantwerpendocs-doc >= %{texlive_version}
Provides:       tex(uantwerpenbamathesis.cls)
Provides:       tex(uantwerpencoursetext.cls)
Provides:       tex(uantwerpenexam.cls)
Provides:       tex(uantwerpenletter.cls)
Provides:       tex(uantwerpenmasterthesis.cls)
Provides:       tex(uantwerpenphdthesis.cls)
Requires:       tex(atbegshi.sty)
Requires:       tex(auto-pst-pdf.sty)
Requires:       tex(background.sty)
Requires:       tex(color.sty)
Requires:       tex(ean13isbn.sty)
Requires:       tex(eso-pic.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(fancyhdr.sty)
Requires:       tex(geometry.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(pst-barcode.sty)
Requires:       tex(shellesc.sty)
Requires:       tex(tikz.sty)
Requires:       tex(ulem.sty)
Requires:       tex(varioref.sty)
Requires:       tex(xstring.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source250:      uantwerpendocs.tar.xz
Source251:      uantwerpendocs.doc.tar.xz

%description -n texlive-uantwerpendocs
These class files implement the house style of the University
of Antwerp. This package originated from the Faculty of Applied
Engineering. Using these class files will make it easy for you
to make and keep your documents compliant to this version and
future versions of the house style of the University of
Antwerp.

%package -n texlive-uantwerpendocs-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.4svn51007
Release:        0
Summary:        Documentation for texlive-uantwerpendocs
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-uantwerpendocs-doc
This package includes the documentation for texlive-uantwerpendocs

%post -n texlive-uantwerpendocs
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-uantwerpendocs 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-uantwerpendocs
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-uantwerpendocs-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/uantwerpendocs/LICENSE
%{_texmfdistdir}/doc/latex/uantwerpendocs/README
%{_texmfdistdir}/doc/latex/uantwerpendocs/uantwerpenbamathesis-example.pdf
%{_texmfdistdir}/doc/latex/uantwerpendocs/uantwerpenbamathesis-example.tex
%{_texmfdistdir}/doc/latex/uantwerpendocs/uantwerpencoursetext-example.pdf
%{_texmfdistdir}/doc/latex/uantwerpendocs/uantwerpencoursetext-example.tex
%{_texmfdistdir}/doc/latex/uantwerpendocs/uantwerpendocs.pdf
%{_texmfdistdir}/doc/latex/uantwerpendocs/uantwerpenexam-example1.pdf
%{_texmfdistdir}/doc/latex/uantwerpendocs/uantwerpenexam-example1.tex
%{_texmfdistdir}/doc/latex/uantwerpendocs/uantwerpenexam-example2.pdf
%{_texmfdistdir}/doc/latex/uantwerpendocs/uantwerpenexam-example2.tex
%{_texmfdistdir}/doc/latex/uantwerpendocs/uantwerpenletter-example.pdf
%{_texmfdistdir}/doc/latex/uantwerpendocs/uantwerpenletter-example.tex
%{_texmfdistdir}/doc/latex/uantwerpendocs/uantwerpenmasterthesis-example.pdf
%{_texmfdistdir}/doc/latex/uantwerpendocs/uantwerpenmasterthesis-example.tex
%{_texmfdistdir}/doc/latex/uantwerpendocs/uantwerpenphdthesis-example1.pdf
%{_texmfdistdir}/doc/latex/uantwerpendocs/uantwerpenphdthesis-example1.tex
%{_texmfdistdir}/doc/latex/uantwerpendocs/uantwerpenphdthesis-example2.pdf
%{_texmfdistdir}/doc/latex/uantwerpendocs/uantwerpenphdthesis-example2.tex

%files -n texlive-uantwerpendocs
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/uantwerpendocs/4E_PMS302_BR_ENG_RGB.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/4E_PMS302_BR_ENG_RGB.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/4E_PMS302_BR_NED_RGB.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/4E_PMS302_BR_NED_RGB.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/UA_HOR_DUI_CMYK.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/UA_HOR_DUI_CMYK.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/UA_HOR_ENG_CMYK.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/UA_HOR_ENG_CMYK.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/UA_HOR_FRA_CMYK.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/UA_HOR_FRA_CMYK.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/UA_HOR_NED_CMYK.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/UA_HOR_NED_CMYK.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/UA_HOR_SPA_CMYK.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/UA_HOR_SPA_CMYK.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/keyboard.jpg
%{_texmfdistdir}/tex/latex/uantwerpendocs/uantwerpenbamathesis.cls
%{_texmfdistdir}/tex/latex/uantwerpendocs/uantwerpencoursetext.cls
%{_texmfdistdir}/tex/latex/uantwerpendocs/uantwerpenexam.cls
%{_texmfdistdir}/tex/latex/uantwerpendocs/uantwerpenletter.cls
%{_texmfdistdir}/tex/latex/uantwerpendocs/uantwerpenmasterthesis.cls
%{_texmfdistdir}/tex/latex/uantwerpendocs/uantwerpenphdthesis.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-uantwerpendocs-%{texlive_version}.%{texlive_noarch}.2.4svn51007-%{release}-zypper
%endif

%package -n texlive-uassign
Version:        %{texlive_version}.%{texlive_noarch}.1.01svn38459
Release:        0
Summary:        Environments and options for typesetting university assignments
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-uassign-doc >= %{texlive_version}
Provides:       tex(uassign.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(amsthm.sty)
Requires:       tex(bookmark.sty)
Requires:       tex(color.sty)
Requires:       tex(enumerate.sty)
Requires:       tex(fancyhdr.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(titlesec.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source252:      uassign.tar.xz
Source253:      uassign.doc.tar.xz

%description -n texlive-uassign
The purpose of this package is to provide simple question and
solution style environments for typesetting university
assignments.

%package -n texlive-uassign-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.01svn38459
Release:        0
Summary:        Documentation for texlive-uassign
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-uassign-doc
This package includes the documentation for texlive-uassign

%post -n texlive-uassign
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-uassign 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-uassign
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-uassign-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/uassign/README.md
%{_texmfdistdir}/doc/latex/uassign/uassign.pdf
%{_texmfdistdir}/doc/latex/uassign/uassign.tex

%files -n texlive-uassign
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/uassign/uassign.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-uassign-%{texlive_version}.%{texlive_noarch}.1.01svn38459-%{release}-zypper
%endif

%package -n texlive-ucalgmthesis
Version:        %{texlive_version}.%{texlive_noarch}.svn52527
Release:        0
Summary:        LaTeX thesis class for University of Calgary Faculty of Graduate Studies
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-ucalgmthesis-doc >= %{texlive_version}
Provides:       tex(ucalgmthesis.cls)
Requires:       tex(amsthm.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(libertine.sty)
Requires:       tex(mathdesign.sty)
Requires:       tex(memoir.cls)
Requires:       tex(newpxmath.sty)
Requires:       tex(newpxtext.sty)
Requires:       tex(newtxmath.sty)
Requires:       tex(newtxtext.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source254:      ucalgmthesis.tar.xz
Source255:      ucalgmthesis.doc.tar.xz

%description -n texlive-ucalgmthesis
ucalgmthesis.cls is a LaTeX class file that produces documents
according to the thesis guidelines of the University of Calgary
Faculty of Graduate Studies. It uses the memoir class, which
provides very powerful and flexible mechanisms for book design
and layout. All memoir commands for changing chapter and
section headings, page layout, fancy foot- and endnotes,
typesetting poems, etc., can be used. (Memoir is meant as a
replacement for the standard LaTeX classes, so all standard
LaTeX commands such as \chapter, \section, etc., still work.)
Likewise, any of memoir's class options can be passed as
options to ucalgmthesis, in particular 12pt to select 12 point
type (11 point is the default).

%package -n texlive-ucalgmthesis-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn52527
Release:        0
Summary:        Documentation for texlive-ucalgmthesis
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-ucalgmthesis-doc
This package includes the documentation for texlive-ucalgmthesis

%post -n texlive-ucalgmthesis
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-ucalgmthesis 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-ucalgmthesis
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-ucalgmthesis-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/ucalgmthesis/LICENSE
%{_texmfdistdir}/doc/latex/ucalgmthesis/README.md
%{_texmfdistdir}/doc/latex/ucalgmthesis/appendix.tex
%{_texmfdistdir}/doc/latex/ucalgmthesis/backmatter.tex
%{_texmfdistdir}/doc/latex/ucalgmthesis/chapter1.tex
%{_texmfdistdir}/doc/latex/ucalgmthesis/chapter2.tex
%{_texmfdistdir}/doc/latex/ucalgmthesis/frontmatter.tex
%{_texmfdistdir}/doc/latex/ucalgmthesis/sample-thesis.bib
%{_texmfdistdir}/doc/latex/ucalgmthesis/sample-thesis.pdf
%{_texmfdistdir}/doc/latex/ucalgmthesis/sample-thesis.tex
%{_texmfdistdir}/doc/latex/ucalgmthesis/titlepage.tex

%files -n texlive-ucalgmthesis
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/ucalgmthesis/ucalgmthesis.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-ucalgmthesis-%{texlive_version}.%{texlive_noarch}.svn52527-%{release}-zypper
%endif

%package -n texlive-ucbthesis
Version:        %{texlive_version}.%{texlive_noarch}.3.6svn51690
Release:        0
Summary:        Thesis and dissertation class supporting UCB requirements
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-ucbthesis-doc >= %{texlive_version}
Provides:       tex(ucbthesis.cls)
Requires:       tex(memoir.cls)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source256:      ucbthesis.tar.xz
Source257:      ucbthesis.doc.tar.xz

%description -n texlive-ucbthesis
The class provides the necessary framework for electronic
submission of Masters theses and Ph.D. dissertations at the
University of California, Berkeley. It is based on the memoir
class.

%package -n texlive-ucbthesis-doc
Version:        %{texlive_version}.%{texlive_noarch}.3.6svn51690
Release:        0
Summary:        Documentation for texlive-ucbthesis
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-ucbthesis-doc
This package includes the documentation for texlive-ucbthesis

%post -n texlive-ucbthesis
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-ucbthesis 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-ucbthesis
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-ucbthesis-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/ucbthesis/README
%{_texmfdistdir}/doc/latex/ucbthesis/example/abstract.tex
%{_texmfdistdir}/doc/latex/ucbthesis/example/chap1.tex
%{_texmfdistdir}/doc/latex/ucbthesis/example/chap2.tex
%{_texmfdistdir}/doc/latex/ucbthesis/example/references.bib
%{_texmfdistdir}/doc/latex/ucbthesis/example/thesis.tex
%{_texmfdistdir}/doc/latex/ucbthesis/ucbthesis.pdf
%{_texmfdistdir}/doc/latex/ucbthesis/ucbthesis.tex

%files -n texlive-ucbthesis
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/ucbthesis/ucbthesis.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-ucbthesis-%{texlive_version}.%{texlive_noarch}.3.6svn51690-%{release}-zypper
%endif

%package -n texlive-ucdavisthesis
Version:        %{texlive_version}.%{texlive_noarch}.1.3svn40772
Release:        0
Summary:        A thesis/dissertation class for University of California at Davis
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-ucdavisthesis-doc >= %{texlive_version}
Provides:       tex(ucdavisthesis.cls)
Provides:       tex(ucdthesis10.clo)
Provides:       tex(ucdthesis11.clo)
Provides:       tex(ucdthesis12.clo)
Provides:       tex(ucdthesis13.clo)
Requires:       tex(ifthen.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source258:      ucdavisthesis.tar.xz
Source259:      ucdavisthesis.doc.tar.xz

%description -n texlive-ucdavisthesis
The ucdavisthesis class is a LaTeX class that allows you to
create a dissertation or thesis conforming to UC Davis
formatting requirements as of April 2016.

%package -n texlive-ucdavisthesis-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.3svn40772
Release:        0
Summary:        Documentation for texlive-ucdavisthesis
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-ucdavisthesis-doc
This package includes the documentation for texlive-ucdavisthesis

%post -n texlive-ucdavisthesis
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-ucdavisthesis 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-ucdavisthesis
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-ucdavisthesis-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/ucdavisthesis/README
%{_texmfdistdir}/doc/latex/ucdavisthesis/example/ucdavisthesis_example.bib
%{_texmfdistdir}/doc/latex/ucdavisthesis/example/ucdavisthesis_example_Chap1.tex
%{_texmfdistdir}/doc/latex/ucdavisthesis/example/ucdavisthesis_example_Chap2.tex
%{_texmfdistdir}/doc/latex/ucdavisthesis/example/ucdavisthesis_example_Chap3.tex
%{_texmfdistdir}/doc/latex/ucdavisthesis/example/ucdavisthesis_example_figure.eps
%{_texmfdistdir}/doc/latex/ucdavisthesis/example/ucdavisthesis_example_figure.pdf
%{_texmfdistdir}/doc/latex/ucdavisthesis/example/ucdavisthesis_example_main.pdf
%{_texmfdistdir}/doc/latex/ucdavisthesis/example/ucdavisthesis_example_main.tex
%{_texmfdistdir}/doc/latex/ucdavisthesis/ucdavisthesis.pdf

%files -n texlive-ucdavisthesis
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/ucdavisthesis/ucdavisthesis.cls
%{_texmfdistdir}/tex/latex/ucdavisthesis/ucdthesis10.clo
%{_texmfdistdir}/tex/latex/ucdavisthesis/ucdthesis11.clo
%{_texmfdistdir}/tex/latex/ucdavisthesis/ucdthesis12.clo
%{_texmfdistdir}/tex/latex/ucdavisthesis/ucdthesis13.clo
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-ucdavisthesis-%{texlive_version}.%{texlive_noarch}.1.3svn40772-%{release}-zypper
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
    ln -sf tlpkg/tlpostcode         %{buildroot}%{_texmfmaindir}/tlpostcode
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-tikz-dimline-%{texlive_version}.%{texlive_noarch}.1.0svn35805-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:1} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:2} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-tikz-feynhand-%{texlive_version}.%{texlive_noarch}.1.1.0svn51915-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:3} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:4} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-tikz-feynman-%{texlive_version}.%{texlive_noarch}.1.1.0svn39582-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:5} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:6} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-tikz-imagelabels-%{texlive_version}.%{texlive_noarch}.0.0.2svn51490-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:7} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:8} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-tikz-inet-%{texlive_version}.%{texlive_noarch}.0.0.1svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:9} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:10} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-tikz-kalender-%{texlive_version}.%{texlive_noarch}.0.0.4fsvn52890-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:11} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:12} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-tikz-karnaugh-%{texlive_version}.%{texlive_noarch}.1.2svn47026-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:13} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:14} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-tikz-ladder-%{texlive_version}.%{texlive_noarch}.1.1svn46555-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:15} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:16} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-tikz-layers-%{texlive_version}.%{texlive_noarch}.0.0.9svn46660-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:17} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:18} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-tikz-nef-%{texlive_version}.%{texlive_noarch}.0.0.1svn48240-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:19} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:20} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-tikz-network-%{texlive_version}.%{texlive_noarch}.1.1svn51884-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:21} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:22} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-tikz-opm-%{texlive_version}.%{texlive_noarch}.0.0.1.1svn32769-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:23} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:24} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-tikz-optics-%{texlive_version}.%{texlive_noarch}.0.0.2.3svn43466-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:25} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:26} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-tikz-page-%{texlive_version}.%{texlive_noarch}.1.0svn42039-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:27} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:28} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-tikz-palattice-%{texlive_version}.%{texlive_noarch}.2.3svn43442-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:29} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:30} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-tikz-planets-%{texlive_version}.%{texlive_noarch}.1.0.1svn54708-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:31} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:32} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-tikz-qtree-%{texlive_version}.%{texlive_noarch}.1.2svn26108-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:33} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:34} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-tikz-relay-%{texlive_version}.%{texlive_noarch}.1.2svn51355-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:35} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:36} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-tikz-sfc-%{texlive_version}.%{texlive_noarch}.1.0.1svn49424-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:37} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:38} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-tikz-timing-%{texlive_version}.%{texlive_noarch}.0.0.7fsvn46111-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:39} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:40} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-tikz-trackschematic-%{texlive_version}.%{texlive_noarch}.0.0.5.1svn53754-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:41} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:42} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-tikz-truchet-%{texlive_version}.%{texlive_noarch}.svn50020-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:43} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:44} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-tikzcodeblocks-%{texlive_version}.%{texlive_noarch}.0.0.13svn54758-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:45} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:46} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-tikzducks-%{texlive_version}.%{texlive_noarch}.1.3svn53312-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:47} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:48} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-tikzinclude-%{texlive_version}.%{texlive_noarch}.1.0svn28715-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:49} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:50} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-tikzlings-%{texlive_version}.%{texlive_noarch}.0.0.2svn54080-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:51} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:52} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-tikzmark-%{texlive_version}.%{texlive_noarch}.1.8svn52293-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:53} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:54} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-tikzmarmots-%{texlive_version}.%{texlive_noarch}.1.0svn54080-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:55} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:56} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-tikzorbital-%{texlive_version}.%{texlive_noarch}.svn36439-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:57} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:58} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-tikzpagenodes-%{texlive_version}.%{texlive_noarch}.1.1svn27723-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:59} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:60} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-tikzpeople-%{texlive_version}.%{texlive_noarch}.0.0.4svn43978-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:61} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:62} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-tikzpfeile-%{texlive_version}.%{texlive_noarch}.1.0svn25777-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:63} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:64} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-tikzposter-%{texlive_version}.%{texlive_noarch}.2.0svn32732-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:65} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:66} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-tikzscale-%{texlive_version}.%{texlive_noarch}.0.0.2.6svn30637-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:67} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:68} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-tikzsymbols-%{texlive_version}.%{texlive_noarch}.4.10csvn49975-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:69} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:70} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-timbreicmc-%{texlive_version}.%{texlive_noarch}.2.0svn49740-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:71} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:72} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-times-fonts-%{texlive_version}.%{texlive_noarch}.svn35058-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:73} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-times
    for font in %{buildroot}/%{_texmfdistdir}/fonts/type1/urw/times/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-times
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-times/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-times/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-times/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-times/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-times.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-times    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-times/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-timetable-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:74} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-timing-diagrams-%{texlive_version}.%{texlive_noarch}.svn31491-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:75} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:76} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-tinos-fonts-%{texlive_version}.%{texlive_noarch}.svn42882-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:77} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:78} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-tinos
    for font in %{buildroot}/%{_texmfdistdir}/fonts/truetype/google/tinos/*.{pf[ab],[ot]tf} \
		%{buildroot}/%{_texmfdistdir}/fonts/type1/google/tinos/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-tinos
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-tinos/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-tinos/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-tinos/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-tinos/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-tinos.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-tinos    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-tinos/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF

    mkdir -p %{buildroot}%{_sysconfdir}/fonts/conf.d
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/55-texlive-tinos.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Disable plain Type1 font to let fontconfig       -->
	<!-- prefere the OpenType and TrueType fonts          -->
	<!-- ************************************************ -->

	<fontconfig>
	  <selectfont>
	    <rejectfont>
	      <glob>%{_datadir}/fonts/texlive-tinos/*.pf*</glob>
	    </rejectfont>
	  </selectfont>
	</fontconfig>
	EOF
    ln -sf %{_datadir}/fontconfig/conf.avail/55-texlive-tinos.conf %{buildroot}%{_sysconfdir}/fonts/conf.d/55-texlive-tinos.conf
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-tipa-fonts-%{texlive_version}.%{texlive_noarch}.1.3svn29349-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:79} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:80} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Make possible scripts usable if any
    for scr in %{_texmfdistdir}/doc/fonts/tipa/gentfm.sh \
	       %{_texmfdistdir}/doc/fonts/tipa/gentipa.sh \
	       %{_texmfdistdir}/doc/fonts/tipa/gentipx.sh \
	       %{_texmfdistdir}/doc/fonts/tipa/genxipa.sh \
	       %{_texmfdistdir}/doc/fonts/tipa/genxipx.sh \
	       %{_texmfdistdir}/doc/fonts/tipa/mktipapk.sh \
	       %{_texmfdistdir}/doc/fonts/tipa/mkxipapk.sh
    do
	test -e %{buildroot}/$scr || continue
	chmod 0755 %{buildroot}/$scr
    done
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-tipa
    for font in %{buildroot}/%{_texmfdistdir}/fonts/type1/public/tipa/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-tipa
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-tipa/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-tipa/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-tipa/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-tipa/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-tipa.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-tipa    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-tipa/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-tipa-de-%{texlive_version}.%{texlive_noarch}.1.3svn22005-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:81} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-tipfr-%{texlive_version}.%{texlive_noarch}.1.5svn38646-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:82} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:83} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-titlecaps-%{texlive_version}.%{texlive_noarch}.1.2svn36170-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:84} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:85} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-titlefoot-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:86} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-titlepages-%{texlive_version}.%{texlive_noarch}.svn19457-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:87} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-titlepic-%{texlive_version}.%{texlive_noarch}.1.2svn43497-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:88} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:89} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-titleref-%{texlive_version}.%{texlive_noarch}.3.1svn18729-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:90} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:91} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-titlesec-%{texlive_version}.%{texlive_noarch}.2.13svn52413-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:92} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:93} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-titling-%{texlive_version}.%{texlive_noarch}.2.1dsvn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:94} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:95} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-tkz-base-%{texlive_version}.%{texlive_noarch}.3.06csvn54758-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:96} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:97} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-tkz-doc-%{texlive_version}.%{texlive_noarch}.1.43csvn54758-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:98} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-tkz-euclide-%{texlive_version}.%{texlive_noarch}.3.06csvn54758-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:99} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:100} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-tkz-fct-%{texlive_version}.%{texlive_noarch}.1.3csvn54703-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:101} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:102} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-tkz-orm-%{texlive_version}.%{texlive_noarch}.0.0.1.4svn54512-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:103} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:104} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-tkz-tab-%{texlive_version}.%{texlive_noarch}.2.1csvn54662-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:105} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:106} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-tlc-article-%{texlive_version}.%{texlive_noarch}.1.0.17svn51431-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:107} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:108} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-tlc2-%{texlive_version}.%{texlive_noarch}.svn26096-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:109} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-tocbibind-%{texlive_version}.%{texlive_noarch}.1.5ksvn20085-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:110} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:111} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-tocdata-%{texlive_version}.%{texlive_noarch}.2.03svn51654-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:112} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:113} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-tocloft-%{texlive_version}.%{texlive_noarch}.2.3jsvn53364-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:114} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:115} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-tocvsec2-%{texlive_version}.%{texlive_noarch}.1.3asvn33146-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:116} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:117} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-todo-%{texlive_version}.%{texlive_noarch}.2.142svn17746-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:118} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:119} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-todonotes-%{texlive_version}.%{texlive_noarch}.1.1.2svn52662-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:120} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:121} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-tokcycle-%{texlive_version}.%{texlive_noarch}.1.12svn53755-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:122} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:123} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-tokenizer-%{texlive_version}.%{texlive_noarch}.1.1.0svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:124} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:125} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-toolbox-%{texlive_version}.%{texlive_noarch}.5.1svn32260-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:126} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:127} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-tools-%{texlive_version}.%{texlive_noarch}.svn53640-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:128} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:129} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-topfloat-%{texlive_version}.%{texlive_noarch}.svn19084-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:130} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:131} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-topiclongtable-%{texlive_version}.%{texlive_noarch}.1.3.2svn54758-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:132} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:133} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-topletter-%{texlive_version}.%{texlive_noarch}.0.0.3.0svn48182-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:134} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:135} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-toptesi-%{texlive_version}.%{texlive_noarch}.6.3.06svn51743-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:136} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:137} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-totcount-%{texlive_version}.%{texlive_noarch}.1.2svn21178-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:138} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:139} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-totpages-%{texlive_version}.%{texlive_noarch}.2.00svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:140} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:141} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-tpic2pdftex-%{texlive_version}.%{texlive_noarch}.svn52851-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:142} -C %{buildroot}%{_datadir}/texlive
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-tpslifonts-%{texlive_version}.%{texlive_noarch}.0.0.6svn42428-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:143} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:144} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-tqft-%{texlive_version}.%{texlive_noarch}.2.1svn44455-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:145} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:146} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-tracklang-%{texlive_version}.%{texlive_noarch}.1.4svn52991-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:147} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:148} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-trajan-fonts-%{texlive_version}.%{texlive_noarch}.1.1svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:149} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:150} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-trajan
    for font in %{buildroot}/%{_texmfdistdir}/fonts/type1/public/trajan/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-trajan
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-trajan/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-trajan/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-trajan/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-trajan/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-trajan.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-trajan    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-trajan/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-tram-%{texlive_version}.%{texlive_noarch}.0.0.2svn29803-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:151} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:152} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-translation-array-fr-%{texlive_version}.%{texlive_noarch}.svn24344-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:153} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-translation-arsclassica-de-%{texlive_version}.%{texlive_noarch}.svn23803-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:154} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-translation-biblatex-de-%{texlive_version}.%{texlive_noarch}.3.0svn45592-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:155} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-translation-chemsym-de-%{texlive_version}.%{texlive_noarch}.svn23804-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:156} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-translation-dcolumn-fr-%{texlive_version}.%{texlive_noarch}.svn24345-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:157} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-translation-ecv-de-%{texlive_version}.%{texlive_noarch}.svn24754-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:158} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-translation-enumitem-de-%{texlive_version}.%{texlive_noarch}.svn24196-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:159} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-translation-europecv-de-%{texlive_version}.%{texlive_noarch}.svn23840-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:160} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-translation-filecontents-de-%{texlive_version}.%{texlive_noarch}.svn24010-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:161} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-translation-moreverb-de-%{texlive_version}.%{texlive_noarch}.svn23957-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:162} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-translation-natbib-fr-%{texlive_version}.%{texlive_noarch}.svn25105-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:163} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-translation-tabbing-fr-%{texlive_version}.%{texlive_noarch}.svn24228-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:164} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-translations-%{texlive_version}.%{texlive_noarch}.1.8svn53962-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:165} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:166} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-translator-%{texlive_version}.%{texlive_noarch}.1.12asvn54512-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:167} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:168} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-transparent-%{texlive_version}.%{texlive_noarch}.1.4svn52981-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:169} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:170} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-tree-dvips-%{texlive_version}.%{texlive_noarch}.0.0.91svn21751-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:171} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:172} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-treetex-%{texlive_version}.%{texlive_noarch}.svn28176-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:173} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:174} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-trfsigns-%{texlive_version}.%{texlive_noarch}.1.01svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:175} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:176} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-trigonometry-%{texlive_version}.%{texlive_noarch}.svn43006-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:177} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:178} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-trimspaces-%{texlive_version}.%{texlive_noarch}.1.1svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:179} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:180} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-trivfloat-%{texlive_version}.%{texlive_noarch}.1.3bsvn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:181} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:182} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-trsym-%{texlive_version}.%{texlive_noarch}.1.0svn18732-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:183} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:184} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-truncate-%{texlive_version}.%{texlive_noarch}.3.6svn18921-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:185} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:186} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-tsemlines-%{texlive_version}.%{texlive_noarch}.1.0svn23440-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:187} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-ttfutils-%{texlive_version}.%{texlive_noarch}.svn54074-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:188} -C %{buildroot}%{_datadir}/texlive
    tar --use-compress-program=xz -xf %{S:189} -C %{buildroot}%{_datadir}/texlive
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-tucv-%{texlive_version}.%{texlive_noarch}.1.0svn20680-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:190} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:191} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-tuda-ci-%{texlive_version}.%{texlive_noarch}.2.09svn54230-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:192} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:193} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-tudscr-%{texlive_version}.%{texlive_noarch}.2.06fsvn54744-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:194} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:195} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-tufte-latex-%{texlive_version}.%{texlive_noarch}.3.5.2svn37649-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:196} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:197} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-tugboat-%{texlive_version}.%{texlive_noarch}.2.23svn54261-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:198} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:199} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-tugboat-plain-%{texlive_version}.%{texlive_noarch}.1.25svn51373-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:200} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:201} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-tui-%{texlive_version}.%{texlive_noarch}.1.9svn27253-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:202} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:203} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-turabian-%{texlive_version}.%{texlive_noarch}.0.0.1.0svn36298-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:204} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:205} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-turabian-formatting-%{texlive_version}.%{texlive_noarch}.svn54436-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:206} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:207} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-turkmen-%{texlive_version}.%{texlive_noarch}.0.0.2svn17748-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:208} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:209} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-turnstile-%{texlive_version}.%{texlive_noarch}.1.0svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:210} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:211} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-turnthepage-%{texlive_version}.%{texlive_noarch}.1.3asvn29803-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:212} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:213} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-twemoji-colr-fonts-%{texlive_version}.%{texlive_noarch}.0.0.5.0svn54512-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:214} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:215} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-twemoji-colr
    for font in %{buildroot}/%{_texmfdistdir}/fonts/truetype/public/twemoji-colr/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-twemoji-colr
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-twemoji-colr/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-twemoji-colr/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-twemoji-colr/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-twemoji-colr/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-twemoji-colr.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-twemoji-colr    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-twemoji-colr/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-twoinone-%{texlive_version}.%{texlive_noarch}.svn17024-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:216} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:217} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-twoup-%{texlive_version}.%{texlive_noarch}.1.3svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:218} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:219} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-txfonts-fonts-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:220} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:221} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-txfonts
    for font in %{buildroot}/%{_texmfdistdir}/fonts/type1/public/txfonts/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-txfonts
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-txfonts/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-txfonts/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-txfonts/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-txfonts/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-txfonts.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-txfonts    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-txfonts/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-txfontsb-fonts-%{texlive_version}.%{texlive_noarch}.1.1.1svn54512-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:222} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:223} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-txfontsb
    for font in %{buildroot}/%{_texmfdistdir}/fonts/opentype/public/txfontsb/*.{pf[ab],[ot]tf} \
		%{buildroot}/%{_texmfdistdir}/fonts/type1/public/txfontsb/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-txfontsb
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-txfontsb/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-txfontsb/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-txfontsb/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-txfontsb/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-txfontsb.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-txfontsb    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-txfontsb/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF

    mkdir -p %{buildroot}%{_sysconfdir}/fonts/conf.d
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/55-texlive-txfontsb.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Disable plain Type1 font to let fontconfig       -->
	<!-- prefere the OpenType and TrueType fonts          -->
	<!-- ************************************************ -->

	<fontconfig>
	  <selectfont>
	    <rejectfont>
	      <glob>%{_datadir}/fonts/texlive-txfontsb/*.pf*</glob>
	    </rejectfont>
	  </selectfont>
	</fontconfig>
	EOF
    ln -sf %{_datadir}/fontconfig/conf.avail/55-texlive-txfontsb.conf %{buildroot}%{_sysconfdir}/fonts/conf.d/55-texlive-txfontsb.conf
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-txgreeks-%{texlive_version}.%{texlive_noarch}.1.0svn21839-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:224} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:225} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-txuprcal-fonts-%{texlive_version}.%{texlive_noarch}.1.00svn43327-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:226} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:227} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-txuprcal
    for font in %{buildroot}/%{_texmfdistdir}/fonts/type1/public/txuprcal/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-txuprcal
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-txuprcal/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-txuprcal/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-txuprcal/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-txuprcal/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-txuprcal.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-txuprcal    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-txuprcal/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-type1cm-%{texlive_version}.%{texlive_noarch}.svn21820-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:228} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:229} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-typed-checklist-%{texlive_version}.%{texlive_noarch}.2.0svn49731-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:230} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:231} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-typeface-%{texlive_version}.%{texlive_noarch}.0.0.1svn27046-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:232} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:233} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-typehtml-%{texlive_version}.%{texlive_noarch}.svn17134-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:234} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:235} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-typeoutfileinfo-%{texlive_version}.%{texlive_noarch}.0.0.31svn29349-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:236} -C %{buildroot}%{_datadir}/texlive
    tar --use-compress-program=xz -xf %{S:237} -C %{buildroot}%{_datadir}/texlive
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-typewriter-%{texlive_version}.%{texlive_noarch}.1.1svn46641-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:238} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:239} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-typicons-fonts-%{texlive_version}.%{texlive_noarch}.2.0.7svn37623-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:240} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:241} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-typicons
    for font in %{buildroot}/%{_texmfdistdir}/fonts/truetype/public/typicons/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-typicons
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-typicons/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-typicons/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-typicons/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-typicons/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-typicons.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-typicons    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-typicons/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-typoaid-%{texlive_version}.%{texlive_noarch}.0.0.4.7svn44238-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:242} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:243} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-typogrid-%{texlive_version}.%{texlive_noarch}.0.0.21svn24994-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:244} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:245} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-uaclasses-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:246} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:247} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-uafthesis-%{texlive_version}.%{texlive_noarch}.12.12svn29349-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:248} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:249} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-uantwerpendocs-%{texlive_version}.%{texlive_noarch}.2.4svn51007-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:250} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:251} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-uassign-%{texlive_version}.%{texlive_noarch}.1.01svn38459-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:252} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:253} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-ucalgmthesis-%{texlive_version}.%{texlive_noarch}.svn52527-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:254} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:255} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-ucbthesis-%{texlive_version}.%{texlive_noarch}.3.6svn51690-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:256} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:257} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-ucdavisthesis-%{texlive_version}.%{texlive_noarch}.1.3svn40772-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:258} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:259} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Remove this
    rm -vrf %{buildroot}%{_texmfdistdir}/tlpkg/tlpobj
    rm -vrf %{buildroot}%{_texmfmaindir}/tlpkg/tlpobj
    rm -v  %{buildroot}%{_datadir}/texlive/texmf
    rm -v  %{buildroot}%{_datadir}/texlive/texmf-dist
    rm -v  %{buildroot}%{_texmfmaindir}/tlpostcode
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
