#
# spec file for package texlive-specs-x.spec
#
# Copyright (c) 2024 SUSE LLC
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
##### WARNING: Please do not edit this auto generated spec file.
#


%define texlive_version  2024
%define texlive_previous 2022
%define texlive_release  20240311
%define texlive_noarch   216
%define biber_version    2.19

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

%if ! %{defined python3_bin_suffix}
%global python3_bin_suffix 3
%endif

Name:           texlive-specs-x
Version:        2024
Release:        0
BuildRequires:  ed
BuildRequires:  fontconfig
BuildRequires:  fontpackages-devel
BuildRequires:  mkfontdir
BuildRequires:  mkfontscale
BuildRequires:  t1utils
BuildRequires:  texlive-filesystem
BuildRequires:  xorg-x11-fonts-core
BuildRequires:  xz
BuildArch:      noarch
Summary:        Meta package for x
License:        Apache-1.0 and BSD-3-Clause and GFDL-1.3-or-later and GPL-2.0-or-later and LPPL-1.0 and SUSE-Public-Domain and SUSE-TeX
URL:            https://build.opensuse.org/package/show/Publishing:TeXLive/Meta
Group:          Productivity/Publishing/TeX/Base
Source0:        texlive-specs-x-rpmlintrc

%description
Meta package to build tons of noarch texlive packages.

%package -n texlive-tikz-dimline
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn35805
Release:        0
License:        LPPL-1.0
Summary:        Technical dimension lines using PGF/TikZ
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tikz-dimline-doc >= %{texlive_version}
Provides:       tex(tikz-dimline.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(pgfplots.sty)
Requires:       tex(tikz.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
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
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tikz-dimline and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikz-dimline-doc
%{_texmfdistdir}/doc/latex/tikz-dimline/README
%{_texmfdistdir}/doc/latex/tikz-dimline/dimline1.png
%{_texmfdistdir}/doc/latex/tikz-dimline/dimline2.png
%{_texmfdistdir}/doc/latex/tikz-dimline/dimline3.png
%{_texmfdistdir}/doc/latex/tikz-dimline/tikz-dimline-doc.pdf
%{_texmfdistdir}/doc/latex/tikz-dimline/tikz-dimline-doc.tex

%files -n texlive-tikz-dimline
%{_texmfdistdir}/tex/latex/tikz-dimline/tikz-dimline.sty

%package -n texlive-tikz-ext
Version:        %{texlive_version}.%{texlive_noarch}.0.0.5.1svn66737
Release:        0
License:        GFDL-1.3-or-later
Summary:        A collection of libraries for PGF/TikZ
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tikz-ext-doc >= %{texlive_version}
Provides:       tex(pgfcalendar-ext.code.tex)
Provides:       tex(pgfcalendar-ext.sty)
Provides:       tex(pgfcalendar-ext.tex)
Provides:       tex(pgffor-ext.code.tex)
Provides:       tex(pgffor-ext.sty)
Provides:       tex(pgffor-ext.tex)
Provides:       tex(pgfkeyslibraryext.pgfkeys-plus.code.tex)
Provides:       tex(pgflibraryext.arrows.code.tex)
Provides:       tex(pgflibraryext.shapes.circlearrow.code.tex)
Provides:       tex(pgflibraryext.shapes.circlecrosssplit.code.tex)
Provides:       tex(pgflibraryext.shapes.heatmark.code.tex)
Provides:       tex(pgflibraryext.shapes.rectangleroundedcorners.code.tex)
Provides:       tex(pgflibraryext.shapes.superellipse.code.tex)
Provides:       tex(pgflibraryext.shapes.uncenteredrectangle.code.tex)
Provides:       tex(pgflibraryext.transformations.mirror.code.tex)
Provides:       tex(tikzlibraryext.calendar-plus.code.tex)
Provides:       tex(tikzlibraryext.layers.code.tex)
Provides:       tex(tikzlibraryext.misc.code.tex)
Provides:       tex(tikzlibraryext.node-families.code.tex)
Provides:       tex(tikzlibraryext.node-families.shapes.geometric.code.tex)
Provides:       tex(tikzlibraryext.nodes.code.tex)
Provides:       tex(tikzlibraryext.paths.arcto.code.tex)
Provides:       tex(tikzlibraryext.paths.ortho.code.tex)
Provides:       tex(tikzlibraryext.paths.timer.code.tex)
Provides:       tex(tikzlibraryext.patterns.images.code.tex)
Provides:       tex(tikzlibraryext.positioning-plus.code.tex)
Provides:       tex(tikzlibraryext.scalepicture.code.tex)
Provides:       tex(tikzlibraryext.shapes.uncenteredrectangle.code.tex)
Provides:       tex(tikzlibraryext.topaths.arcthrough.code.tex)
Provides:       tex(tikzlibraryext.transformations.mirror.code.tex)
Requires:       tex(pgfcalendar.sty)
Requires:       tex(pgffor.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source3:        tikz-ext.tar.xz
Source4:        tikz-ext.doc.tar.xz

%description -n texlive-tikz-ext
This is a collection of libraries for PGF/TikZ. Currently these
are transformations.mirror, paths.arcto, paths.ortho,
paths.timer, patterns.images, topaths.arcthrough and misc. Most
of these libraries were developed in response to questions on
TeX.stackexchange.com.

%package -n texlive-tikz-ext-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.5.1svn66737
Release:        0
Summary:        Documentation for texlive-tikz-ext
License:        GFDL-1.3-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tikz-ext and texlive-alldocumentation)

%description -n texlive-tikz-ext-doc
This package includes the documentation for texlive-tikz-ext

%post -n texlive-tikz-ext
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tikz-ext
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tikz-ext
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikz-ext-doc
%{_texmfdistdir}/doc/latex/tikz-ext/README.md
%{_texmfdistdir}/doc/latex/tikz-ext/tikz-ext-manual-en-calendar.tex
%{_texmfdistdir}/doc/latex/tikz-ext/tikz-ext-manual-en-intro.tex
%{_texmfdistdir}/doc/latex/tikz-ext/tikz-ext-manual-en-library-calendar-plus.tex
%{_texmfdistdir}/doc/latex/tikz-ext/tikz-ext-manual-en-library-layers.tex
%{_texmfdistdir}/doc/latex/tikz-ext/tikz-ext-manual-en-library-misc.tex
%{_texmfdistdir}/doc/latex/tikz-ext/tikz-ext-manual-en-library-node-families.tex
%{_texmfdistdir}/doc/latex/tikz-ext/tikz-ext-manual-en-library-nodes.tex
%{_texmfdistdir}/doc/latex/tikz-ext/tikz-ext-manual-en-library-paths.arcto.tex
%{_texmfdistdir}/doc/latex/tikz-ext/tikz-ext-manual-en-library-paths.ortho.tex
%{_texmfdistdir}/doc/latex/tikz-ext/tikz-ext-manual-en-library-paths.timer.tex
%{_texmfdistdir}/doc/latex/tikz-ext/tikz-ext-manual-en-library-patterns.images.tex
%{_texmfdistdir}/doc/latex/tikz-ext/tikz-ext-manual-en-library-pgffor.tex
%{_texmfdistdir}/doc/latex/tikz-ext/tikz-ext-manual-en-library-positioning-plus.tex
%{_texmfdistdir}/doc/latex/tikz-ext/tikz-ext-manual-en-library-scalepicture.tex
%{_texmfdistdir}/doc/latex/tikz-ext/tikz-ext-manual-en-library-topaths.arcthrough.tex
%{_texmfdistdir}/doc/latex/tikz-ext/tikz-ext-manual-en-library-trans.tex
%{_texmfdistdir}/doc/latex/tikz-ext/tikz-ext-manual-en-main-body.tex
%{_texmfdistdir}/doc/latex/tikz-ext/tikz-ext-manual-en-main-preamble.tex
%{_texmfdistdir}/doc/latex/tikz-ext/tikz-ext-manual-en-pgf-arrows.tex
%{_texmfdistdir}/doc/latex/tikz-ext/tikz-ext-manual-en-pgf-shapes-circlearrow.tex
%{_texmfdistdir}/doc/latex/tikz-ext/tikz-ext-manual-en-pgf-shapes-circlecrosssplit.tex
%{_texmfdistdir}/doc/latex/tikz-ext/tikz-ext-manual-en-pgf-shapes-heatmark.tex
%{_texmfdistdir}/doc/latex/tikz-ext/tikz-ext-manual-en-pgf-shapes-rectround.tex
%{_texmfdistdir}/doc/latex/tikz-ext/tikz-ext-manual-en-pgf-shapes-superellipse.tex
%{_texmfdistdir}/doc/latex/tikz-ext/tikz-ext-manual-en-pgf-shapes-uncentered.tex
%{_texmfdistdir}/doc/latex/tikz-ext/tikz-ext-manual-en-pgf-trans.tex
%{_texmfdistdir}/doc/latex/tikz-ext/tikz-ext-manual.bib
%{_texmfdistdir}/doc/latex/tikz-ext/tikz-ext-manual.pdf
%{_texmfdistdir}/doc/latex/tikz-ext/tikz-ext-manual.tex

%files -n texlive-tikz-ext
%{_texmfdistdir}/tex/generic/tikz-ext/pgfcalendar-ext.code.tex
%{_texmfdistdir}/tex/generic/tikz-ext/pgffor-ext.code.tex
%{_texmfdistdir}/tex/generic/tikz-ext/pgfkeyslibraryext.pgfkeys-plus.code.tex
%{_texmfdistdir}/tex/generic/tikz-ext/pgflibraryext.arrows.code.tex
%{_texmfdistdir}/tex/generic/tikz-ext/pgflibraryext.shapes.circlearrow.code.tex
%{_texmfdistdir}/tex/generic/tikz-ext/pgflibraryext.shapes.circlecrosssplit.code.tex
%{_texmfdistdir}/tex/generic/tikz-ext/pgflibraryext.shapes.heatmark.code.tex
%{_texmfdistdir}/tex/generic/tikz-ext/pgflibraryext.shapes.rectangleroundedcorners.code.tex
%{_texmfdistdir}/tex/generic/tikz-ext/pgflibraryext.shapes.superellipse.code.tex
%{_texmfdistdir}/tex/generic/tikz-ext/pgflibraryext.shapes.uncenteredrectangle.code.tex
%{_texmfdistdir}/tex/generic/tikz-ext/pgflibraryext.transformations.mirror.code.tex
%{_texmfdistdir}/tex/generic/tikz-ext/tikzlibraryext.calendar-plus.code.tex
%{_texmfdistdir}/tex/generic/tikz-ext/tikzlibraryext.layers.code.tex
%{_texmfdistdir}/tex/generic/tikz-ext/tikzlibraryext.misc.code.tex
%{_texmfdistdir}/tex/generic/tikz-ext/tikzlibraryext.node-families.code.tex
%{_texmfdistdir}/tex/generic/tikz-ext/tikzlibraryext.node-families.shapes.geometric.code.tex
%{_texmfdistdir}/tex/generic/tikz-ext/tikzlibraryext.nodes.code.tex
%{_texmfdistdir}/tex/generic/tikz-ext/tikzlibraryext.paths.arcto.code.tex
%{_texmfdistdir}/tex/generic/tikz-ext/tikzlibraryext.paths.ortho.code.tex
%{_texmfdistdir}/tex/generic/tikz-ext/tikzlibraryext.paths.timer.code.tex
%{_texmfdistdir}/tex/generic/tikz-ext/tikzlibraryext.patterns.images.code.tex
%{_texmfdistdir}/tex/generic/tikz-ext/tikzlibraryext.positioning-plus.code.tex
%{_texmfdistdir}/tex/generic/tikz-ext/tikzlibraryext.scalepicture.code.tex
%{_texmfdistdir}/tex/generic/tikz-ext/tikzlibraryext.shapes.uncenteredrectangle.code.tex
%{_texmfdistdir}/tex/generic/tikz-ext/tikzlibraryext.topaths.arcthrough.code.tex
%{_texmfdistdir}/tex/generic/tikz-ext/tikzlibraryext.transformations.mirror.code.tex
%{_texmfdistdir}/tex/latex/tikz-ext/pgfcalendar-ext.sty
%{_texmfdistdir}/tex/latex/tikz-ext/pgffor-ext.sty
%{_texmfdistdir}/tex/plain/tikz-ext/pgfcalendar-ext.tex
%{_texmfdistdir}/tex/plain/tikz-ext/pgffor-ext.tex

%package -n texlive-tikz-feynhand
Version:        %{texlive_version}.%{texlive_noarch}.1.1.0svn51915
Release:        0
License:        GPL-2.0-or-later
Summary:        Feynman diagrams with TikZ
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tikz-feynhand-doc >= %{texlive_version}
Provides:       tex(tikz-feynhand.sty)
Provides:       tex(tikzfeynhand.keys.code.tex)
Provides:       tex(tikzlibraryfeynhand.code.tex)
Requires:       tex(pgfopts.sty)
Requires:       tex(tikz.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source5:        tikz-feynhand.tar.xz
Source6:        tikz-feynhand.doc.tar.xz

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
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tikz-feynhand and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikz-feynhand-doc
%{_texmfdistdir}/doc/latex/tikz-feynhand/README.md
%{_texmfdistdir}/doc/latex/tikz-feynhand/changes.txt
%{_texmfdistdir}/doc/latex/tikz-feynhand/shell_escape.jpg
%{_texmfdistdir}/doc/latex/tikz-feynhand/tikz-feynhand.userguide.pdf
%{_texmfdistdir}/doc/latex/tikz-feynhand/tikz-feynhand.userguide.tex

%files -n texlive-tikz-feynhand
%{_texmfdistdir}/tex/latex/tikz-feynhand/tikz-feynhand.sty
%{_texmfdistdir}/tex/latex/tikz-feynhand/tikzfeynhand.keys.code.tex
%{_texmfdistdir}/tex/latex/tikz-feynhand/tikzlibraryfeynhand.code.tex

%package -n texlive-tikz-feynman
Version:        %{texlive_version}.%{texlive_noarch}.1.1.0svn56615
Release:        0
License:        LPPL-1.0
Summary:        Feynman diagrams with TikZ
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires:       texlive-iftex >= %{texlive_version}
#!BuildIgnore: texlive-iftex
Requires:       texlive-pgfopts >= %{texlive_version}
#!BuildIgnore: texlive-pgfopts
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tikz-feynman-doc >= %{texlive_version}
Provides:       tex(tikz-feynman.sty)
Provides:       tex(tikzfeynman.keys.code.tex)
Provides:       tex(tikzlibraryfeynman.code.tex)
Requires:       tex(ifluatex.sty)
Requires:       tex(pgfopts.sty)
Requires:       tex(tikz.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source7:        tikz-feynman.tar.xz
Source8:        tikz-feynman.doc.tar.xz

%description -n texlive-tikz-feynman
This is a LaTeX package allowing Feynman diagrams to be easily
generated within LaTeX with minimal user instructions and
without the need of external programs. It builds upon the TikZ
package and leverages the graph placement algorithms from TikZ
in order to automate the placement of many vertices.
tikz-feynman allows fine-tuned placement of vertices so that
even complex diagrams can still be generated with ease.

%package -n texlive-tikz-feynman-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1.0svn56615
Release:        0
Summary:        Documentation for texlive-tikz-feynman
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tikz-feynman and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikz-feynman-doc
%{_texmfdistdir}/doc/latex/tikz-feynman/LICENSE
%{_texmfdistdir}/doc/latex/tikz-feynman/README.md
%{_texmfdistdir}/doc/latex/tikz-feynman/references.bib
%{_texmfdistdir}/doc/latex/tikz-feynman/tikz-feynman.pdf
%{_texmfdistdir}/doc/latex/tikz-feynman/tikz-feynman.tex

%files -n texlive-tikz-feynman
%{_texmfdistdir}/tex/latex/tikz-feynman/tikz-feynman.sty
%{_texmfdistdir}/tex/latex/tikz-feynman/tikzfeynman.keys.code.tex
%{_texmfdistdir}/tex/latex/tikz-feynman/tikzfeynman.patch.3.0.0.lua
%{_texmfdistdir}/tex/latex/tikz-feynman/tikzfeynman.patch.3.0.1.lua
%{_texmfdistdir}/tex/latex/tikz-feynman/tikzlibraryfeynman.code.tex

%package -n texlive-tikz-imagelabels
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2svn51490
Release:        0
License:        LPPL-1.0
Summary:        Put labels on images using TikZ
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tikz-imagelabels-doc >= %{texlive_version}
Provides:       tex(tikz-imagelabels.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xifthen.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source9:        tikz-imagelabels.tar.xz
Source10:       tikz-imagelabels.doc.tar.xz

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
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tikz-imagelabels and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikz-imagelabels-doc
%{_texmfdistdir}/doc/latex/tikz-imagelabels/README.md
%{_texmfdistdir}/doc/latex/tikz-imagelabels/pleiades.jpg
%{_texmfdistdir}/doc/latex/tikz-imagelabels/tikz-imagelabels.pdf

%files -n texlive-tikz-imagelabels
%{_texmfdistdir}/tex/latex/tikz-imagelabels/tikz-imagelabels.sty

%package -n texlive-tikz-inet
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn15878
Release:        0
License:        LPPL-1.0
Summary:        Draw interaction nets with TikZ
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tikz-inet-doc >= %{texlive_version}
Provides:       tex(tikz-inet.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(tikz.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source11:       tikz-inet.tar.xz
Source12:       tikz-inet.doc.tar.xz

%description -n texlive-tikz-inet
The package extends TikZ with macros to draw interaction nets.

%package -n texlive-tikz-inet-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn15878
Release:        0
Summary:        Documentation for texlive-tikz-inet
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tikz-inet and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikz-inet-doc
%{_texmfdistdir}/doc/latex/tikz-inet/README
%{_texmfdistdir}/doc/latex/tikz-inet/tikz-inet-doc.pdf
%{_texmfdistdir}/doc/latex/tikz-inet/tikz-inet-doc.tex

%files -n texlive-tikz-inet
%{_texmfdistdir}/tex/latex/tikz-inet/tikz-inet.sty

%package -n texlive-tikz-kalender
Version:        %{texlive_version}.%{texlive_noarch}.0.0.4fsvn52890
Release:        0
License:        LPPL-1.0
Summary:        A LaTeX based calendar using TikZ
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tikz-kalender-doc >= %{texlive_version}
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
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source13:       tikz-kalender.tar.xz
Source14:       tikz-kalender.doc.tar.xz

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
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tikz-kalender and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikz-kalender-doc
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
%{_texmfdistdir}/tex/latex/tikz-kalender/tikz-kalender-translation.clo
%{_texmfdistdir}/tex/latex/tikz-kalender/tikz-kalender.cls

%package -n texlive-tikz-karnaugh
Version:        %{texlive_version}.%{texlive_noarch}.1.5svn62040
Release:        0
License:        LPPL-1.0
Summary:        Typeset Karnaugh maps using TikZ
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tikz-karnaugh-doc >= %{texlive_version}
Provides:       tex(tikzlibrarykarnaugh.code.tex)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source15:       tikz-karnaugh.tar.xz
Source16:       tikz-karnaugh.doc.tar.xz

%description -n texlive-tikz-karnaugh
The tikz-karnaugh package is a LaTeX package used to draw
Karnaugh maps. It uses TikZ to produce high quality graph from
1 to 12 variables, but this upper limit depends on the TeX
memory usage and can be different for you. It is very good for
presentation since TikZ allows for a better control over the
final appearance of the map. You can control colour, styles and
distances. It can be considered as an upgrade and extension of
Andreas W. Wieland's karnaugh package towards TikZ supporting.
Upgrade because uses TikZ for more option on typesetting and
overall higher quality. Extension because it also supports
American style and inputting the values as they would appear in
the map or in the truth table. Complex maps with solution
(implicants) pointed out can be generated with external java
software (see documentation for details). It supports both
American and traditional (simplified labels) styles and from
version 1.3 on American style is natively supported, therefore,
no more addition work is required to typeset Gray coded labels,
variable names etc. From version 1.4, two new macros allow
typesetting a map much more similarly as it should appear.
Original order, as the values appear in the truth table, still
being supported.

%package -n texlive-tikz-karnaugh-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.5svn62040
Release:        0
Summary:        Documentation for texlive-tikz-karnaugh
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tikz-karnaugh and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikz-karnaugh-doc
%{_texmfdistdir}/doc/latex/tikz-karnaugh/README.txt
%{_texmfdistdir}/doc/latex/tikz-karnaugh/tikz-karnaugh-doc.pdf
%{_texmfdistdir}/doc/latex/tikz-karnaugh/tikz-karnaugh-doc.tex

%files -n texlive-tikz-karnaugh
%{_texmfdistdir}/tex/latex/tikz-karnaugh/tikzlibrarykarnaugh.code.tex

%package -n texlive-tikz-ladder
Version:        %{texlive_version}.%{texlive_noarch}.1.3svn62992
Release:        0
License:        LPPL-1.0
Summary:        Draw ladder diagrams using TikZ
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tikz-ladder-doc >= %{texlive_version}
Provides:       tex(tikzlibrarycircuits.plc.ladder.code.tex)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source17:       tikz-ladder.tar.xz
Source18:       tikz-ladder.doc.tar.xz

%description -n texlive-tikz-ladder
The tikz-ladder package contains a collection of symbols for
typesetting ladder diagrams (PLC program) in agreement with the
international standard IEC-61131-3/2013. It includes blocks
(for representing functions and function blocks) besides
contacts and coils. It extends the circuit library of TikZ and
allows you to draw a ladder diagram in the same way as you
would draw any other circuit.

%package -n texlive-tikz-ladder-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.3svn62992
Release:        0
Summary:        Documentation for texlive-tikz-ladder
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tikz-ladder and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikz-ladder-doc
%{_texmfdistdir}/doc/latex/tikz-ladder/README.txt
%{_texmfdistdir}/doc/latex/tikz-ladder/tikz-ladder-doc.pdf
%{_texmfdistdir}/doc/latex/tikz-ladder/tikz-ladder-doc.tex

%files -n texlive-tikz-ladder
%{_texmfdistdir}/tex/latex/tikz-ladder/tikzlibrarycircuits.plc.ladder.code.tex

%package -n texlive-tikz-lake-fig
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn55288
Release:        0
License:        LPPL-1.0
Summary:        Schematic diagrams of lakes
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tikz-lake-fig-doc >= %{texlive_version}
Provides:       tex(tikz-lake-fig.sty)
Requires:       tex(array.sty)
Requires:       tex(colortbl.sty)
Requires:       tex(multirow.sty)
Requires:       tex(pbox.sty)
Requires:       tex(relsize.sty)
Requires:       tex(subfiles.sty)
Requires:       tex(tabularx.sty)
Requires:       tex(tikz.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source19:       tikz-lake-fig.tar.xz
Source20:       tikz-lake-fig.doc.tar.xz

%description -n texlive-tikz-lake-fig
This package contains a collection of schematic diagrams of
lakes for use in LaTeX documents. Diagrams include
representations of material budgets, fluxes, and connectivity
arrangements.

%package -n texlive-tikz-lake-fig-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn55288
Release:        0
Summary:        Documentation for texlive-tikz-lake-fig
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tikz-lake-fig and texlive-alldocumentation)

%description -n texlive-tikz-lake-fig-doc
This package includes the documentation for texlive-tikz-lake-fig

%post -n texlive-tikz-lake-fig
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tikz-lake-fig
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tikz-lake-fig
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikz-lake-fig-doc
%{_texmfdistdir}/doc/latex/tikz-lake-fig/README.md
%{_texmfdistdir}/doc/latex/tikz-lake-fig/tikz-lake-fig-doc.pdf
%{_texmfdistdir}/doc/latex/tikz-lake-fig/tikz-lake-fig-doc.tex

%files -n texlive-tikz-lake-fig
%{_texmfdistdir}/tex/latex/tikz-lake-fig/tikz-lake-fig.sty

%package -n texlive-tikz-layers
Version:        %{texlive_version}.%{texlive_noarch}.0.0.9svn46660
Release:        0
License:        LPPL-1.0
Summary:        TikZ provides graphical layers on TikZ: "behind", "above" and "glass"
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tikz-layers-doc >= %{texlive_version}
Provides:       tex(tikz-layers.sty)
Requires:       tex(tikz.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source21:       tikz-layers.tar.xz
Source22:       tikz-layers.doc.tar.xz

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
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tikz-layers and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikz-layers-doc
%{_texmfdistdir}/doc/latex/tikz-layers/README
%{_texmfdistdir}/doc/latex/tikz-layers/README.TEXLIVE
%{_texmfdistdir}/doc/latex/tikz-layers/manifest.txt

%files -n texlive-tikz-layers
%{_texmfdistdir}/tex/latex/tikz-layers/tikz-layers.sty

%package -n texlive-tikz-mirror-lens
Version:        %{texlive_version}.%{texlive_noarch}.1.0.2svn65500
Release:        0
License:        LPPL-1.0
Summary:        Spherical mirrors and lenses in TikZ
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tikz-mirror-lens-doc >= %{texlive_version}
Provides:       tex(tikz-mirror-lens.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(tikz.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source23:       tikz-mirror-lens.tar.xz
Source24:       tikz-mirror-lens.doc.tar.xz

%description -n texlive-tikz-mirror-lens
This package allows the automatic drawing of the image of
objects in spherical mirrors and lenses from the data of the
focus, from the position and height of the object. It
calculates the position and height of the image, and also
displays the notable rays.

%package -n texlive-tikz-mirror-lens-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0.2svn65500
Release:        0
Summary:        Documentation for texlive-tikz-mirror-lens
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tikz-mirror-lens and texlive-alldocumentation)
Provides:       locale(texlive-tikz-mirror-lens-doc:pt_BR)

%description -n texlive-tikz-mirror-lens-doc
This package includes the documentation for texlive-tikz-mirror-lens

%post -n texlive-tikz-mirror-lens
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tikz-mirror-lens
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tikz-mirror-lens
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikz-mirror-lens-doc
%{_texmfdistdir}/doc/latex/tikz-mirror-lens/README.md
%{_texmfdistdir}/doc/latex/tikz-mirror-lens/input_pacotes.tex
%{_texmfdistdir}/doc/latex/tikz-mirror-lens/input_tab_configuracoes_espelhos.tex
%{_texmfdistdir}/doc/latex/tikz-mirror-lens/input_tab_configuracoes_lentes.tex
%{_texmfdistdir}/doc/latex/tikz-mirror-lens/input_tab_configuracoes_lentesL.tex
%{_texmfdistdir}/doc/latex/tikz-mirror-lens/tikz-mirror-lens-PT.pdf
%{_texmfdistdir}/doc/latex/tikz-mirror-lens/tikz-mirror-lens-PT.tex
%{_texmfdistdir}/doc/latex/tikz-mirror-lens/tikz-mirror-lens.pdf
%{_texmfdistdir}/doc/latex/tikz-mirror-lens/tikz-mirror-lens.tex

%files -n texlive-tikz-mirror-lens
%{_texmfdistdir}/tex/latex/tikz-mirror-lens/tikz-mirror-lens.cwl
%{_texmfdistdir}/tex/latex/tikz-mirror-lens/tikz-mirror-lens.sty

%package -n texlive-tikz-nef
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn55920
Release:        0
License:        LPPL-1.0
Summary:        Create diagrams for neural networks constructed with the methods of the Neural Engineering Framework (NEF)
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tikz-nef-doc >= %{texlive_version}
Provides:       tex(tikzlibrarynef.code.tex)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source25:       tikz-nef.tar.xz
Source26:       tikz-nef.doc.tar.xz

%description -n texlive-tikz-nef
The nef TikZ library provides predefined styles and shapes to
create diagrams for neural networks constructed with the
methods of the Neural Engineering Framework (NEF). The
following styles are supported: ea: ensemble array ens:
ensemble ext: external input or output inhibt: inhibitory
connection net: network pnode: pass-through node rect:
rectification ensemble recurrent: recurrent connection

%package -n texlive-tikz-nef-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn55920
Release:        0
Summary:        Documentation for texlive-tikz-nef
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tikz-nef and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikz-nef-doc
%{_texmfdistdir}/doc/latex/tikz-nef/LICENSE
%{_texmfdistdir}/doc/latex/tikz-nef/README.md
%{_texmfdistdir}/doc/latex/tikz-nef/example-net.tex
%{_texmfdistdir}/doc/latex/tikz-nef/nef.bib
%{_texmfdistdir}/doc/latex/tikz-nef/tikz-nef-doc.pdf
%{_texmfdistdir}/doc/latex/tikz-nef/tikz-nef-doc.tex

%files -n texlive-tikz-nef
%{_texmfdistdir}/tex/latex/tikz-nef/tikzlibrarynef.code.tex

%package -n texlive-tikz-network
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn51884
Release:        0
License:        GPL-2.0-or-later
Summary:        Draw networks with TikZ
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tikz-network-doc >= %{texlive_version}
Provides:       tex(tikz-network.sty)
Requires:       tex(datatool.sty)
Requires:       tex(etex.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(tikz.sty)
Requires:       tex(trimspaces.sty)
Requires:       tex(xifthen.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source27:       tikz-network.tar.xz
Source28:       tikz-network.doc.tar.xz

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
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tikz-network and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikz-network-doc
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
%{_texmfdistdir}/tex/latex/tikz-network/tikz-network.sty

%package -n texlive-tikz-nfold
Version:        %{texlive_version}.%{texlive_noarch}.1.0.0svn67718
Release:        0
License:        LPPL-1.0
Summary:        Triple, quadruple, and n-fold paths with TikZ
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tikz-nfold-doc >= %{texlive_version}
Provides:       tex(pgflibrarybezieroffset.code.tex)
Provides:       tex(pgflibrarynfold.code.tex)
Provides:       tex(pgflibraryoffsetpath.code.tex)
Provides:       tex(tikzlibrarynfold.code.tex)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source29:       tikz-nfold.tar.xz
Source30:       tikz-nfold.doc.tar.xz

%description -n texlive-tikz-nfold
This library adds higher-order paths to TikZ and also fixes
some graphical issues with TikZ' double paths, used e.g. in
arrows with an Implies tip. It is also compatible with tikz-cd,
adding support for triple and higher arrows. Macros to offset
arbitrary paths are included as well.

%package -n texlive-tikz-nfold-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0.0svn67718
Release:        0
Summary:        Documentation for texlive-tikz-nfold
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tikz-nfold and texlive-alldocumentation)

%description -n texlive-tikz-nfold-doc
This package includes the documentation for texlive-tikz-nfold

%post -n texlive-tikz-nfold
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tikz-nfold
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tikz-nfold
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikz-nfold-doc
%{_texmfdistdir}/doc/latex/tikz-nfold/README.md
%{_texmfdistdir}/doc/latex/tikz-nfold/tikz-nfold-doc.pdf
%{_texmfdistdir}/doc/latex/tikz-nfold/tikz-nfold-doc.tex

%files -n texlive-tikz-nfold
%{_texmfdistdir}/tex/latex/tikz-nfold/pgflibrarybezieroffset.code.tex
%{_texmfdistdir}/tex/latex/tikz-nfold/pgflibrarynfold.code.tex
%{_texmfdistdir}/tex/latex/tikz-nfold/pgflibraryoffsetpath.code.tex
%{_texmfdistdir}/tex/latex/tikz-nfold/tikzlibrarynfold.code.tex

%package -n texlive-tikz-opm
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1.1svn32769
Release:        0
License:        LPPL-1.0
Summary:        Typeset OPM diagrams
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tikz-opm-doc >= %{texlive_version}
Provides:       tex(tikz-opm.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(makeshape.sty)
Requires:       tex(tikz.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source31:       tikz-opm.tar.xz
Source32:       tikz-opm.doc.tar.xz

%description -n texlive-tikz-opm
Typeset OPM (Object-Process Methodology) diagrams using LaTeX
and PGF/TikZ.

%package -n texlive-tikz-opm-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1.1svn32769
Release:        0
Summary:        Documentation for texlive-tikz-opm
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tikz-opm and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikz-opm-doc
%{_texmfdistdir}/doc/latex/tikz-opm/README
%{_texmfdistdir}/doc/latex/tikz-opm/tikz-opm.pdf

%files -n texlive-tikz-opm
%{_texmfdistdir}/tex/latex/tikz-opm/tikz-opm.sty

%package -n texlive-tikz-optics
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2.3svn62977
Release:        0
License:        LPPL-1.0
Summary:        A library for drawing optical setups with TikZ
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tikz-optics-doc >= %{texlive_version}
Provides:       tex(tikzlibraryoptics.code.tex)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source33:       tikz-optics.tar.xz
Source34:       tikz-optics.doc.tar.xz

%description -n texlive-tikz-optics
This package provides a new TikZ library designed to easily
draw optical setups with TikZ. It provides shapes for lens,
mirror, etc. The geometrically (in)correct computation of light
rays through the setup is left to the user.

%package -n texlive-tikz-optics-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2.3svn62977
Release:        0
Summary:        Documentation for texlive-tikz-optics
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tikz-optics and texlive-alldocumentation)
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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikz-optics-doc
%{_texmfdistdir}/doc/latex/tikz-optics/README
%{_texmfdistdir}/doc/latex/tikz-optics/tikz-optics.pdf
%{_texmfdistdir}/doc/latex/tikz-optics/tikz-optics.tex

%files -n texlive-tikz-optics
%{_texmfdistdir}/tex/latex/tikz-optics/tikzlibraryoptics.code.tex

%package -n texlive-tikz-osci
Version:        %{texlive_version}.%{texlive_noarch}.0.0.4.0svn68636
Release:        0
License:        LPPL-1.0
Summary:        Produce oscilloscope "screen shots"
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tikz-osci-doc >= %{texlive_version}
Provides:       tex(tikz-osci.sty)
Requires:       tex(pgfkeys.sty)
Requires:       tex(pgfplots.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xcolor.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source35:       tikz-osci.tar.xz
Source36:       tikz-osci.doc.tar.xz

%description -n texlive-tikz-osci
This package enables you to produce oscilloscope "screen
shots".

%package -n texlive-tikz-osci-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.4.0svn68636
Release:        0
Summary:        Documentation for texlive-tikz-osci
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tikz-osci and texlive-alldocumentation)

%description -n texlive-tikz-osci-doc
This package includes the documentation for texlive-tikz-osci

%post -n texlive-tikz-osci
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tikz-osci
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tikz-osci
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikz-osci-doc
%{_texmfdistdir}/doc/latex/tikz-osci/README.md
%{_texmfdistdir}/doc/latex/tikz-osci/tikz-osci-doc.pdf
%{_texmfdistdir}/doc/latex/tikz-osci/tikz-osci-doc.tex
%{_texmfdistdir}/doc/latex/tikz-osci/tikz-osci-example.pdf
%{_texmfdistdir}/doc/latex/tikz-osci/tikz-osci-example.tex

%files -n texlive-tikz-osci
%{_texmfdistdir}/tex/latex/tikz-osci/tikz-osci.sty

%package -n texlive-tikz-page
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn42039
Release:        0
License:        LPPL-1.0
Summary:        Small macro to help building nice and complex layout materials
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tikz-page-doc >= %{texlive_version}
Provides:       tex(tikz-page.sty)
Requires:       tex(calc.sty)
Requires:       tex(fancyhdr.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(textpos.sty)
Requires:       tex(tikz.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source37:       tikz-page.tar.xz
Source38:       tikz-page.doc.tar.xz

%description -n texlive-tikz-page
The package provides a small macro to help building nice and
complex layout materials.

%package -n texlive-tikz-page-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn42039
Release:        0
Summary:        Documentation for texlive-tikz-page
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tikz-page and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikz-page-doc
%{_texmfdistdir}/doc/latex/tikz-page/Makefile
%{_texmfdistdir}/doc/latex/tikz-page/README
%{_texmfdistdir}/doc/latex/tikz-page/README.md
%{_texmfdistdir}/doc/latex/tikz-page/example.png
%{_texmfdistdir}/doc/latex/tikz-page/tikz-page.pdf

%files -n texlive-tikz-page
%{_texmfdistdir}/tex/latex/tikz-page/tikz-page.sty

%package -n texlive-tikz-palattice
Version:        %{texlive_version}.%{texlive_noarch}.2.3svn43442
Release:        0
License:        LPPL-1.0
Summary:        Draw particle accelerator lattices with TikZ
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tikz-palattice-doc >= %{texlive_version}
Provides:       tex(tikz-palattice.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(iflang.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(siunitx.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xargs.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source39:       tikz-palattice.tar.xz
Source40:       tikz-palattice.doc.tar.xz

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
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tikz-palattice and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikz-palattice-doc
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
%{_texmfdistdir}/tex/latex/tikz-palattice/tikz-palattice.sty

%package -n texlive-tikz-planets
Version:        %{texlive_version}.%{texlive_noarch}.1.0.2svn55002
Release:        0
License:        LPPL-1.0
Summary:        Illustrate celestial mechanics and the solar system
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tikz-planets-doc >= %{texlive_version}
Provides:       tex(planets.sty)
Requires:       tex(pgfkeys.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xstring.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source41:       tikz-planets.tar.xz
Source42:       tikz-planets.doc.tar.xz

%description -n texlive-tikz-planets
This TikZ-package makes it easy to illustrate celestial
mechanics and the solar system. You can use it to draw sketches
of the eclipses, the phases of the Moon, etc. The package
requires the standard packages TikZ, xcolor, xstring, and
pgfkeys.

%package -n texlive-tikz-planets-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0.2svn55002
Release:        0
Summary:        Documentation for texlive-tikz-planets
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tikz-planets and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikz-planets-doc
%{_texmfdistdir}/doc/latex/tikz-planets/README.md
%{_texmfdistdir}/doc/latex/tikz-planets/planets-doc.pdf
%{_texmfdistdir}/doc/latex/tikz-planets/planets-doc.tex

%files -n texlive-tikz-planets
%{_texmfdistdir}/tex/latex/tikz-planets/planets.sty

%package -n texlive-tikz-qtree
Version:        %{texlive_version}.%{texlive_noarch}.1.2svn26108
Release:        0
License:        GPL-2.0-or-later
Summary:        Use existing qtree syntax for trees in TikZ
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tikz-qtree-doc >= %{texlive_version}
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
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source43:       tikz-qtree.tar.xz
Source44:       tikz-qtree.doc.tar.xz

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
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tikz-qtree and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikz-qtree-doc
%{_texmfdistdir}/doc/latex/tikz-qtree/README
%{_texmfdistdir}/doc/latex/tikz-qtree/tikz-qtree-manual.pdf
%{_texmfdistdir}/doc/latex/tikz-qtree/tikz-qtree-manual.tex

%files -n texlive-tikz-qtree
%{_texmfdistdir}/tex/latex/tikz-qtree/pgfsubpic.sty
%{_texmfdistdir}/tex/latex/tikz-qtree/pgfsubpic.tex
%{_texmfdistdir}/tex/latex/tikz-qtree/pgftree.sty
%{_texmfdistdir}/tex/latex/tikz-qtree/pgftree.tex
%{_texmfdistdir}/tex/latex/tikz-qtree/tikz-qtree-compat.sty
%{_texmfdistdir}/tex/latex/tikz-qtree/tikz-qtree.sty
%{_texmfdistdir}/tex/latex/tikz-qtree/tikz-qtree.tex

%package -n texlive-tikz-relay
Version:        %{texlive_version}.%{texlive_noarch}.1.3svn64072
Release:        0
License:        LPPL-1.0
Summary:        TikZ library for typesetting electrical diagrams
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tikz-relay-doc >= %{texlive_version}
Provides:       tex(tikzlibrarycircuits.ee.IEC.relay.code.tex)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source45:       tikz-relay.tar.xz
Source46:       tikz-relay.doc.tar.xz

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
Version:        %{texlive_version}.%{texlive_noarch}.1.3svn64072
Release:        0
Summary:        Documentation for texlive-tikz-relay
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tikz-relay and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikz-relay-doc
%{_texmfdistdir}/doc/latex/tikz-relay/BeamerAnimation.pdf
%{_texmfdistdir}/doc/latex/tikz-relay/BeamerAnimation.tex
%{_texmfdistdir}/doc/latex/tikz-relay/README.txt
%{_texmfdistdir}/doc/latex/tikz-relay/tikz-relay-doc.pdf
%{_texmfdistdir}/doc/latex/tikz-relay/tikz-relay-doc.tex

%files -n texlive-tikz-relay
%{_texmfdistdir}/tex/latex/tikz-relay/tikzlibrarycircuits.ee.IEC.relay.code.tex

%package -n texlive-tikz-sfc
Version:        %{texlive_version}.%{texlive_noarch}.1.0.1svn49424
Release:        0
License:        LPPL-1.0
Summary:        Symbols collection for typesetting Sequential Function Chart (SFC) diagrams (PLC programs)
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tikz-sfc-doc >= %{texlive_version}
Provides:       tex(tikzlibrarycircuits.plc.sfc.code.tex)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source47:       tikz-sfc.tar.xz
Source48:       tikz-sfc.doc.tar.xz

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
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tikz-sfc and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikz-sfc-doc
%{_texmfdistdir}/doc/latex/tikz-sfc/BeamerAnimation.pdf
%{_texmfdistdir}/doc/latex/tikz-sfc/BeamerAnimation.tex
%{_texmfdistdir}/doc/latex/tikz-sfc/README.txt
%{_texmfdistdir}/doc/latex/tikz-sfc/tikz-sfc-doc.pdf
%{_texmfdistdir}/doc/latex/tikz-sfc/tikz-sfc-doc.tex

%files -n texlive-tikz-sfc
%{_texmfdistdir}/tex/latex/tikz-sfc/tikzlibrarycircuits.plc.sfc.code.tex

%package -n texlive-tikz-swigs
Version:        %{texlive_version}.%{texlive_noarch}.svn59889
Release:        0
License:        LPPL-1.0
Summary:        Horizontally and vertically split elliptical nodes
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tikz-swigs-doc >= %{texlive_version}
Provides:       tex(tikzlibraryswigs.code.tex)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source49:       tikz-swigs.tar.xz
Source50:       tikz-swigs.doc.tar.xz

%description -n texlive-tikz-swigs
This package provides horizontally and vertically split
elliptical (pairs of) nodes in TikZ. The package name derives
from the fact that split ellipses of this type are used to
represent Single-World Intervention Graph (SWIG) models which
are used in counterfactual causal inference.

%package -n texlive-tikz-swigs-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn59889
Release:        0
Summary:        Documentation for texlive-tikz-swigs
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tikz-swigs and texlive-alldocumentation)

%description -n texlive-tikz-swigs-doc
This package includes the documentation for texlive-tikz-swigs

%post -n texlive-tikz-swigs
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tikz-swigs
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tikz-swigs
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikz-swigs-doc
%{_texmfdistdir}/doc/latex/tikz-swigs/LICENSE
%{_texmfdistdir}/doc/latex/tikz-swigs/README.md
%{_texmfdistdir}/doc/latex/tikz-swigs/tikz-swigs.pdf
%{_texmfdistdir}/doc/latex/tikz-swigs/tikz-swigs.tex

%files -n texlive-tikz-swigs
%{_texmfdistdir}/tex/latex/tikz-swigs/tikzlibraryswigs.code.tex

%package -n texlive-tikz-timing
Version:        %{texlive_version}.%{texlive_noarch}.0.0.7fsvn64967
Release:        0
License:        LPPL-1.0
Summary:        Easy generation of timing diagrams as TikZ pictures
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires:       texlive-svn-prov >= %{texlive_version}
#!BuildIgnore: texlive-svn-prov
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tikz-timing-doc >= %{texlive_version}
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
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source51:       tikz-timing.tar.xz
Source52:       tikz-timing.doc.tar.xz

%description -n texlive-tikz-timing
This package provides macros and an environment to generate
timing diagrams (digital waveforms) without much effort. The
TikZ package is used to produce the graphics. The diagrams may
be inserted into text (paragraphs, \hbox, etc.) and into
tikzpictures. A tabular-like environment is provided to produce
larger timing diagrams.

%package -n texlive-tikz-timing-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.7fsvn64967
Release:        0
Summary:        Documentation for texlive-tikz-timing
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tikz-timing and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikz-timing-doc
%{_texmfdistdir}/doc/latex/tikz-timing/README
%{_texmfdistdir}/doc/latex/tikz-timing/tikz-timing.pdf

%files -n texlive-tikz-timing
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

%package -n texlive-tikz-trackschematic
Version:        %{texlive_version}.%{texlive_noarch}.0.0.7.1svn63480
Release:        0
License:        LPPL-1.0
Summary:        A TikZ library for creating track diagrams in railways
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tikz-trackschematic-doc >= %{texlive_version}
Provides:       tex(tikz-trackschematic.sty)
Provides:       tex(tikzlibrarytrackschematic.code.tex)
Provides:       tex(tikzlibrarytrackschematic.constructions.code.tex)
Provides:       tex(tikzlibrarytrackschematic.electrics.code.tex)
Provides:       tex(tikzlibrarytrackschematic.measures.code.tex)
Provides:       tex(tikzlibrarytrackschematic.symbology.code.tex)
Provides:       tex(tikzlibrarytrackschematic.topology.code.tex)
Provides:       tex(tikzlibrarytrackschematic.trafficcontrol.code.tex)
Provides:       tex(tikzlibrarytrackschematic.vehicles.code.tex)
Requires:       tex(etoolbox.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source53:       tikz-trackschematic.tar.xz
Source54:       tikz-trackschematic.doc.tar.xz

%description -n texlive-tikz-trackschematic
This TikZ library is a toolbox of symbols geared primarily
towards creating track schematic for either research or
educational purposes. It provides a TikZ frontend to some of
the symbols which may be needed to describe situations and
layouts in railway operation. The library is divided into
sublibraries: topology, trafficcontrol, vehicles,
constructions, electrics, symbology, and measures.

%package -n texlive-tikz-trackschematic-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.7.1svn63480
Release:        0
Summary:        Documentation for texlive-tikz-trackschematic
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tikz-trackschematic and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikz-trackschematic-doc
%{_texmfdistdir}/doc/latex/tikz-trackschematic/CHANGELOG.md
%{_texmfdistdir}/doc/latex/tikz-trackschematic/CITATION.cff
%{_texmfdistdir}/doc/latex/tikz-trackschematic/LICENSE
%{_texmfdistdir}/doc/latex/tikz-trackschematic/README.md
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-documentation.sty
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-examples/minimal_working_example.pdf
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-examples/minimal_working_example.png
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-examples/minimal_working_example.tex
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-examples/station_berg.pdf
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-examples/station_berg.png
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-examples/station_berg.tex
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-examples/station_chamstadt.pdf
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-examples/station_chamstadt.png
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-examples/station_chamstadt.tex
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets.pdf
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets.tex
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/balise_forward_with_signal.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/balise_switched.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/balises.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/bend_train.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/block_clearing_point_backward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/block_clearing_point_forward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/block_signal_backward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/block_signal_forward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/block_signal_with_shunt_signal_backward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/block_signal_with_shunt_signal_forward.tikz
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
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/direction_control.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/direction_control_backward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/direction_control_forward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/distant_pantograph_down_backward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/distant_pantograph_down_forward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/distant_power_off_backward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/distant_power_off_forward.tikz
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
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/individual_balises.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/individual_balises_mixed.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/interlocking.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/level_crossing_double.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/level_crossing_double_full_closure.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/level_crossing_single.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/level_crossing_without_barrier.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/main_line.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/main_track.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/measure_line.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/measure_line_with_hectometer.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/pantograph_down_backward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/pantograph_down_forward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/pantograph_up_backward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/pantograph_up_forward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/parked_vehicle.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/parked_vehicles.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/parked_vehicles_with_label.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/platform_left.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/platform_middle.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/platform_right.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/power_off_backward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/power_off_forward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/power_on_backward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/power_on_forward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/pylons_both.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/pylons_left.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/pylons_middle.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/pylons_right.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/route.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/route_clearing_point_backward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/route_clearing_point_forward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/route_signal_backward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/route_signal_forward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/route_signal_with_shunt_signal_backward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/route_signal_with_shunt_signal_forward.tikz
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
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/track_marking.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/track_marking_with_turnout.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/track_number.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/trackloop.tikz
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
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/wire_limit_backward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-snippets/wire_limit_forward.tikz
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-symbology-table.pdf
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic-symbology-table.tex
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic.pdf
%{_texmfdistdir}/doc/latex/tikz-trackschematic/tikz-trackschematic.tex

%files -n texlive-tikz-trackschematic
%{_texmfdistdir}/tex/latex/tikz-trackschematic/tikz-trackschematic.sty
%{_texmfdistdir}/tex/latex/tikz-trackschematic/tikzlibrarytrackschematic.code.tex
%{_texmfdistdir}/tex/latex/tikz-trackschematic/tikzlibrarytrackschematic.constructions.code.tex
%{_texmfdistdir}/tex/latex/tikz-trackschematic/tikzlibrarytrackschematic.electrics.code.tex
%{_texmfdistdir}/tex/latex/tikz-trackschematic/tikzlibrarytrackschematic.measures.code.tex
%{_texmfdistdir}/tex/latex/tikz-trackschematic/tikzlibrarytrackschematic.symbology.code.tex
%{_texmfdistdir}/tex/latex/tikz-trackschematic/tikzlibrarytrackschematic.topology.code.tex
%{_texmfdistdir}/tex/latex/tikz-trackschematic/tikzlibrarytrackschematic.trafficcontrol.code.tex
%{_texmfdistdir}/tex/latex/tikz-trackschematic/tikzlibrarytrackschematic.vehicles.code.tex

%package -n texlive-tikz-truchet
Version:        %{texlive_version}.%{texlive_noarch}.svn50020
Release:        0
License:        LPPL-1.0
Summary:        Draw Truchet tiles
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tikz-truchet-doc >= %{texlive_version}
Provides:       tex(tikz-truchet.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(tikz.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source55:       tikz-truchet.tar.xz
Source56:       tikz-truchet.doc.tar.xz

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
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tikz-truchet and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikz-truchet-doc
%{_texmfdistdir}/doc/latex/tikz-truchet/README.md
%{_texmfdistdir}/doc/latex/tikz-truchet/tikz-truchet.pdf

%files -n texlive-tikz-truchet
%{_texmfdistdir}/tex/latex/tikz-truchet/tikz-truchet.sty

%package -n texlive-tikz2d-fr
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1.1svn67239
Release:        0
License:        LPPL-1.0
Summary:        Work with some 2D TikZ commands (French)
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tikz2d-fr-doc >= %{texlive_version}
Provides:       tex(tikz2d-fr.sty)
Requires:       tex(listofitems.sty)
Requires:       tex(pgffor.sty)
Requires:       tex(simplekv.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xintexpr.sty)
Requires:       tex(xstring.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source57:       tikz2d-fr.tar.xz
Source58:       tikz2d-fr.doc.tar.xz

%description -n texlive-tikz2d-fr
This is a small package to work with some (French) 2D commands
for TikZ: "freehand style" mainlevee define and mark points
\DefinirPoints, \MarquerPoints draw colored segments
\TracerSegments

%package -n texlive-tikz2d-fr-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1.1svn67239
Release:        0
Summary:        Documentation for texlive-tikz2d-fr
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tikz2d-fr and texlive-alldocumentation)

%description -n texlive-tikz2d-fr-doc
This package includes the documentation for texlive-tikz2d-fr

%post -n texlive-tikz2d-fr
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tikz2d-fr
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tikz2d-fr
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikz2d-fr-doc
%{_texmfdistdir}/doc/latex/tikz2d-fr/README.md
%{_texmfdistdir}/doc/latex/tikz2d-fr/tikz2d-fr-doc.pdf
%{_texmfdistdir}/doc/latex/tikz2d-fr/tikz2d-fr-doc.tex

%files -n texlive-tikz2d-fr
%{_texmfdistdir}/tex/latex/tikz2d-fr/tikz2d-fr.sty

%package -n texlive-tikz3d-fr
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1.2svn67774
Release:        0
License:        LPPL-1.0
Summary:        Work with some 3D figures
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tikz3d-fr-doc >= %{texlive_version}
Provides:       tex(tikz3d-fr.sty)
Requires:       tex(listofitems.sty)
Requires:       tex(simplekv.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xintexpr.sty)
Requires:       tex(xinttools.sty)
Requires:       tex(xstring.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source59:       tikz3d-fr.tar.xz
Source60:       tikz3d-fr.doc.tar.xz

%description -n texlive-tikz3d-fr
This is a package for working with some 3D figures.

%package -n texlive-tikz3d-fr-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1.2svn67774
Release:        0
Summary:        Documentation for texlive-tikz3d-fr
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tikz3d-fr and texlive-alldocumentation)

%description -n texlive-tikz3d-fr-doc
This package includes the documentation for texlive-tikz3d-fr

%post -n texlive-tikz3d-fr
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tikz3d-fr
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tikz3d-fr
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikz3d-fr-doc
%{_texmfdistdir}/doc/latex/tikz3d-fr/README.md
%{_texmfdistdir}/doc/latex/tikz3d-fr/tikz3d-fr-doc.pdf
%{_texmfdistdir}/doc/latex/tikz3d-fr/tikz3d-fr-doc.tex

%files -n texlive-tikz3d-fr
%{_texmfdistdir}/tex/latex/tikz3d-fr/tikz3d-fr.sty

%package -n texlive-tikzbricks
Version:        %{texlive_version}.%{texlive_noarch}.0.0.4svn63952
Release:        0
License:        LPPL-1.0
Summary:        Drawing bricks with TikZ
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tikzbricks-doc >= %{texlive_version}
Provides:       tex(tikzbricks.sty)
Requires:       tex(tikz-3dplot.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source61:       tikzbricks.tar.xz
Source62:       tikzbricks.doc.tar.xz

%description -n texlive-tikzbricks
A small LaTeX package to draw bricks with TikZ. The user can
modify color, shape, and viewpoint.

%package -n texlive-tikzbricks-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.4svn63952
Release:        0
Summary:        Documentation for texlive-tikzbricks
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tikzbricks and texlive-alldocumentation)

%description -n texlive-tikzbricks-doc
This package includes the documentation for texlive-tikzbricks

%post -n texlive-tikzbricks
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tikzbricks
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tikzbricks
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikzbricks-doc
%{_texmfdistdir}/doc/latex/tikzbricks/README.md
%{_texmfdistdir}/doc/latex/tikzbricks/tikzbricks-doc.pdf
%{_texmfdistdir}/doc/latex/tikzbricks/tikzbricks-doc.tex

%files -n texlive-tikzbricks
%{_texmfdistdir}/tex/latex/tikzbricks/tikzbricks.sty

%package -n texlive-tikzcodeblocks
Version:        %{texlive_version}.%{texlive_noarch}.0.0.13svn54758
Release:        0
License:        LPPL-1.0
Summary:        Helps to draw codeblocks like scratch, NEPO and PXT in TikZ
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tikzcodeblocks-doc >= %{texlive_version}
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
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source63:       tikzcodeblocks.tar.xz
Source64:       tikzcodeblocks.doc.tar.xz

%description -n texlive-tikzcodeblocks
tikzcodeblocks is a LaTeX package for typesetting blockwise
graphic programming languages like scratch, nepo or pxt.

%package -n texlive-tikzcodeblocks-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.13svn54758
Release:        0
Summary:        Documentation for texlive-tikzcodeblocks
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tikzcodeblocks and texlive-alldocumentation)
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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikzcodeblocks-doc
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
%{_texmfdistdir}/tex/latex/tikzcodeblocks/tikzcodeblocks.sty

%package -n texlive-tikzdotncross
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn69382
Release:        0
License:        LPPL-1.0
Summary:        Small set of macros for defining/marking coordinates and crossing (jumps) paths
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tikzdotncross-doc >= %{texlive_version}
Provides:       tex(tikzdotncross.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source65:       tikzdotncross.tar.xz
Source66:       tikzdotncross.doc.tar.xz

%description -n texlive-tikzdotncross
This package offers a few alternative ways for declaring and
marking coordinates and drawing a line with "jumps" over an
already existent path, which is a quite common issue when
drawing, for instace, Electronic Circuits (like with
CircuiTikZ).

%package -n texlive-tikzdotncross-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn69382
Release:        0
Summary:        Documentation for texlive-tikzdotncross
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tikzdotncross and texlive-alldocumentation)

%description -n texlive-tikzdotncross-doc
This package includes the documentation for texlive-tikzdotncross

%post -n texlive-tikzdotncross
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tikzdotncross
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tikzdotncross
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikzdotncross-doc
%{_texmfdistdir}/doc/latex/tikzdotncross/README.md
%{_texmfdistdir}/doc/latex/tikzdotncross/tikzdotncross.pdf
%{_texmfdistdir}/doc/latex/tikzdotncross/tikzdotncross.tex

%files -n texlive-tikzdotncross
%{_texmfdistdir}/tex/latex/tikzdotncross/tikzdotncross.sty

%package -n texlive-tikzducks
Version:        %{texlive_version}.%{texlive_noarch}.1.6svn66773
Release:        0
License:        LPPL-1.0
Summary:        A little fun package for using rubber ducks in TikZ
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tikzducks-doc >= %{texlive_version}
Provides:       tex(tikzducks-generic.tex)
Provides:       tex(tikzducks-plain.tex)
Provides:       tex(tikzducks.sty)
Provides:       tex(tikzlibraryducks.code.tex)
Requires:       tex(expl3.sty)
Requires:       tex(tikz.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source67:       tikzducks.tar.xz
Source68:       tikzducks.doc.tar.xz

%description -n texlive-tikzducks
The package is a LaTeX package for ducks to be used in TikZ
pictures. This project is a continuation of an answer at
StackExchange How we can draw a duck?

%package -n texlive-tikzducks-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.6svn66773
Release:        0
Summary:        Documentation for texlive-tikzducks
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tikzducks and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikzducks-doc
%{_texmfdistdir}/doc/generic/tikzducks/README.md
%{_texmfdistdir}/doc/generic/tikzducks/tikzducks-doc.pdf
%{_texmfdistdir}/doc/generic/tikzducks/tikzducks-doc.tex

%files -n texlive-tikzducks
%{_texmfdistdir}/tex/generic/tikzducks/t-tikzducks.mkiv
%{_texmfdistdir}/tex/generic/tikzducks/tikzducks-generic.tex
%{_texmfdistdir}/tex/generic/tikzducks/tikzducks-plain.tex
%{_texmfdistdir}/tex/generic/tikzducks/tikzducks.sty
%{_texmfdistdir}/tex/generic/tikzducks/tikzlibraryducks.code.tex

%package -n texlive-tikzfill
Version:        %{texlive_version}.%{texlive_noarch}.1.0.1svn67847
Release:        0
License:        LPPL-1.0
Summary:        TikZ libraries for filling with images and patterns
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tikzfill-doc >= %{texlive_version}
Provides:       tex(tikzfill-common.sty)
Provides:       tex(tikzfill.hexagon.sty)
Provides:       tex(tikzfill.image.sty)
Provides:       tex(tikzfill.rhombus.sty)
Provides:       tex(tikzfill.sty)
Provides:       tex(tikzlibraryfill.hexagon.code.tex)
Provides:       tex(tikzlibraryfill.image.code.tex)
Provides:       tex(tikzlibraryfill.rhombus.code.tex)
Requires:       tex(tikz.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source69:       tikzfill.tar.xz
Source70:       tikzfill.doc.tar.xz

%description -n texlive-tikzfill
This is a collection of TikZ libraries which add further
options to fill TikZ paths with images and patterns. The
libraries comprise fillings with images from files and from
TikZ pictures. Also, patterns of hexagons and of rhombi are
provided.

%package -n texlive-tikzfill-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0.1svn67847
Release:        0
Summary:        Documentation for texlive-tikzfill
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tikzfill and texlive-alldocumentation)

%description -n texlive-tikzfill-doc
This package includes the documentation for texlive-tikzfill

%post -n texlive-tikzfill
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tikzfill
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tikzfill
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikzfill-doc
%{_texmfdistdir}/doc/latex/tikzfill/CHANGES.md
%{_texmfdistdir}/doc/latex/tikzfill/README.md
%{_texmfdistdir}/doc/latex/tikzfill/tikzfill-doc.sty
%{_texmfdistdir}/doc/latex/tikzfill/tikzfill.pdf
%{_texmfdistdir}/doc/latex/tikzfill/tikzfill.tex

%files -n texlive-tikzfill
%{_texmfdistdir}/tex/latex/tikzfill/tikzfill-common.sty
%{_texmfdistdir}/tex/latex/tikzfill/tikzfill.hexagon.sty
%{_texmfdistdir}/tex/latex/tikzfill/tikzfill.image.sty
%{_texmfdistdir}/tex/latex/tikzfill/tikzfill.rhombus.sty
%{_texmfdistdir}/tex/latex/tikzfill/tikzfill.sty
%{_texmfdistdir}/tex/latex/tikzfill/tikzlibraryfill.hexagon.code.tex
%{_texmfdistdir}/tex/latex/tikzfill/tikzlibraryfill.image.code.tex
%{_texmfdistdir}/tex/latex/tikzfill/tikzlibraryfill.rhombus.code.tex

%package -n texlive-tikzinclude
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn28715
Release:        0
License:        LPPL-1.0
Summary:        Import TikZ images from colletions
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tikzinclude-doc >= %{texlive_version}
Provides:       tex(tikzinclude.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(tikz.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source71:       tikzinclude.tar.xz
Source72:       tikzinclude.doc.tar.xz

%description -n texlive-tikzinclude
The package addresses the problem of importing only one
TikZ-image from a file holding multiple images.

%package -n texlive-tikzinclude-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn28715
Release:        0
Summary:        Documentation for texlive-tikzinclude
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tikzinclude and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikzinclude-doc
%{_texmfdistdir}/doc/latex/tikzinclude/README
%{_texmfdistdir}/doc/latex/tikzinclude/tikzinclude.pdf

%files -n texlive-tikzinclude
%{_texmfdistdir}/tex/latex/tikzinclude/tikzinclude.sty

%package -n texlive-tikzlings
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn63628
Release:        0
License:        LPPL-1.0
Summary:        A collection of cute little animals and similar creatures
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tikzlings-doc >= %{texlive_version}
Provides:       tex(tikzlibrarytikzlings.code.tex)
Provides:       tex(tikzlings-addons.sty)
Provides:       tex(tikzlings-anteaters.sty)
Provides:       tex(tikzlings-bats.sty)
Provides:       tex(tikzlings-bears.sty)
Provides:       tex(tikzlings-bees.sty)
Provides:       tex(tikzlings-bugs.sty)
Provides:       tex(tikzlings-cats.sty)
Provides:       tex(tikzlings-chickens.sty)
Provides:       tex(tikzlings-coatis.sty)
Provides:       tex(tikzlings-elephants.sty)
Provides:       tex(tikzlings-hippos.sty)
Provides:       tex(tikzlings-koalas.sty)
Provides:       tex(tikzlings-list.sty)
Provides:       tex(tikzlings-marmots.sty)
Provides:       tex(tikzlings-mice.sty)
Provides:       tex(tikzlings-moles.sty)
Provides:       tex(tikzlings-owls.sty)
Provides:       tex(tikzlings-pandas.sty)
Provides:       tex(tikzlings-penguins.sty)
Provides:       tex(tikzlings-pigs.sty)
Provides:       tex(tikzlings-rhinos.sty)
Provides:       tex(tikzlings-sheep.sty)
Provides:       tex(tikzlings-sloths.sty)
Provides:       tex(tikzlings-snowmen.sty)
Provides:       tex(tikzlings-squirrels.sty)
Provides:       tex(tikzlings-wolves.sty)
Provides:       tex(tikzlings.sty)
Requires:       tex(expl3.sty)
Requires:       tex(tikz.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source73:       tikzlings.tar.xz
Source74:       tikzlings.doc.tar.xz

%description -n texlive-tikzlings
A collection of LaTeX packages for drawing cute little animals
and similar creatures using TikZ. Currently, the following
TikZlings are included: anteater bat bear bee bug cat chicken
coati elephant hippo koala marmot mole mouse owl panda penguin
pig rhino sheep sloth snowman squirrel wolf These little
drawings can be customized in many ways.

%package -n texlive-tikzlings-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn63628
Release:        0
Summary:        Documentation for texlive-tikzlings
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tikzlings and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikzlings-doc
%{_texmfdistdir}/doc/latex/tikzlings/README.md
%{_texmfdistdir}/doc/latex/tikzlings/tikzlings-doc.pdf
%{_texmfdistdir}/doc/latex/tikzlings/tikzlings-doc.tex

%files -n texlive-tikzlings
%{_texmfdistdir}/tex/latex/tikzlings/tikzlibrarytikzlings.code.tex
%{_texmfdistdir}/tex/latex/tikzlings/tikzlings-addons.sty
%{_texmfdistdir}/tex/latex/tikzlings/tikzlings-anteaters.sty
%{_texmfdistdir}/tex/latex/tikzlings/tikzlings-bats.sty
%{_texmfdistdir}/tex/latex/tikzlings/tikzlings-bears.sty
%{_texmfdistdir}/tex/latex/tikzlings/tikzlings-bees.sty
%{_texmfdistdir}/tex/latex/tikzlings/tikzlings-bugs.sty
%{_texmfdistdir}/tex/latex/tikzlings/tikzlings-cats.sty
%{_texmfdistdir}/tex/latex/tikzlings/tikzlings-chickens.sty
%{_texmfdistdir}/tex/latex/tikzlings/tikzlings-coatis.sty
%{_texmfdistdir}/tex/latex/tikzlings/tikzlings-elephants.sty
%{_texmfdistdir}/tex/latex/tikzlings/tikzlings-hippos.sty
%{_texmfdistdir}/tex/latex/tikzlings/tikzlings-koalas.sty
%{_texmfdistdir}/tex/latex/tikzlings/tikzlings-list.sty
%{_texmfdistdir}/tex/latex/tikzlings/tikzlings-marmots.sty
%{_texmfdistdir}/tex/latex/tikzlings/tikzlings-mice.sty
%{_texmfdistdir}/tex/latex/tikzlings/tikzlings-moles.sty
%{_texmfdistdir}/tex/latex/tikzlings/tikzlings-owls.sty
%{_texmfdistdir}/tex/latex/tikzlings/tikzlings-pandas.sty
%{_texmfdistdir}/tex/latex/tikzlings/tikzlings-penguins.sty
%{_texmfdistdir}/tex/latex/tikzlings/tikzlings-pigs.sty
%{_texmfdistdir}/tex/latex/tikzlings/tikzlings-rhinos.sty
%{_texmfdistdir}/tex/latex/tikzlings/tikzlings-sheep.sty
%{_texmfdistdir}/tex/latex/tikzlings/tikzlings-sloths.sty
%{_texmfdistdir}/tex/latex/tikzlings/tikzlings-snowmen.sty
%{_texmfdistdir}/tex/latex/tikzlings/tikzlings-squirrels.sty
%{_texmfdistdir}/tex/latex/tikzlings/tikzlings-wolves.sty
%{_texmfdistdir}/tex/latex/tikzlings/tikzlings.sty

%package -n texlive-tikzmark
Version:        %{texlive_version}.%{texlive_noarch}.1.15svn64819
Release:        0
License:        LPPL-1.0
Summary:        Use TikZ's method of remembering a position on a page
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tikzmark-doc >= %{texlive_version}
Provides:       tex(tikzlibrarytikzmark.code.tex)
Provides:       tex(tikzmarklibraryams.code.tex)
Provides:       tex(tikzmarklibraryhighlighting.code.tex)
Provides:       tex(tikzmarklibrarylistings.code.tex)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source75:       tikzmark.tar.xz
Source76:       tikzmark.doc.tar.xz

%description -n texlive-tikzmark
The tikzmark package defines a command to "remember" a position
on a page for later (or earlier) use, primarily (but not
exclusively) with TikZ.

%package -n texlive-tikzmark-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.15svn64819
Release:        0
Summary:        Documentation for texlive-tikzmark
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tikzmark and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikzmark-doc
%{_texmfdistdir}/doc/latex/tikzmark/README
%{_texmfdistdir}/doc/latex/tikzmark/README.txt
%{_texmfdistdir}/doc/latex/tikzmark/tikzmark.pdf

%files -n texlive-tikzmark
%{_texmfdistdir}/tex/latex/tikzmark/tikzlibrarytikzmark.code.tex
%{_texmfdistdir}/tex/latex/tikzmark/tikzmarklibraryams.code.tex
%{_texmfdistdir}/tex/latex/tikzmark/tikzmarklibraryhighlighting.code.tex
%{_texmfdistdir}/tex/latex/tikzmark/tikzmarklibrarylistings.code.tex

%package -n texlive-tikzmarmots
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn54080
Release:        0
License:        LPPL-1.0
Summary:        Drawing little marmots in TikZ
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tikzmarmots-doc >= %{texlive_version}
Provides:       tex(tikzlibrarymarmots.code.tex)
Provides:       tex(tikzmarmots.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(tikz.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source77:       tikzmarmots.tar.xz
Source78:       tikzmarmots.doc.tar.xz

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
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tikzmarmots and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikzmarmots-doc
%{_texmfdistdir}/doc/latex/tikzmarmots/LICENSE.txt
%{_texmfdistdir}/doc/latex/tikzmarmots/README.md
%{_texmfdistdir}/doc/latex/tikzmarmots/tikzmarmots-doc.pdf
%{_texmfdistdir}/doc/latex/tikzmarmots/tikzmarmots-doc.tex

%files -n texlive-tikzmarmots
%{_texmfdistdir}/tex/latex/tikzmarmots/tikzlibrarymarmots.code.tex
%{_texmfdistdir}/tex/latex/tikzmarmots/tikzmarmots.sty

%package -n texlive-tikzorbital
Version:        %{texlive_version}.%{texlive_noarch}.svn36439
Release:        0
License:        LPPL-1.0
Summary:        Atomic and molecular orbitals using TikZ
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tikzorbital-doc >= %{texlive_version}
Provides:       tex(tikzorbital.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(tikz.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source79:       tikzorbital.tar.xz
Source80:       tikzorbital.doc.tar.xz

%description -n texlive-tikzorbital
Atomic s, p and d orbitals may be drawn, as well as molecular
orbital diagrams.

%package -n texlive-tikzorbital-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn36439
Release:        0
Summary:        Documentation for texlive-tikzorbital
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tikzorbital and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikzorbital-doc
%{_texmfdistdir}/doc/latex/tikzorbital/README.rst
%{_texmfdistdir}/doc/latex/tikzorbital/tikzorbital.pdf
%{_texmfdistdir}/doc/latex/tikzorbital/tikzorbital.tex

%files -n texlive-tikzorbital
%{_texmfdistdir}/tex/latex/tikzorbital/tikzorbital.sty

%package -n texlive-tikzpackets
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn55827
Release:        0
License:        LPPL-1.0
Summary:        Display network packets
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tikzpackets-doc >= %{texlive_version}
Provides:       tex(tikzPackets.sty)
Requires:       tex(pbox.sty)
Requires:       tex(tcolorbox.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xparse.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source81:       tikzpackets.tar.xz
Source82:       tikzpackets.doc.tar.xz

%description -n texlive-tikzpackets
This package allows you to easily display network packets
graphically.

%package -n texlive-tikzpackets-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn55827
Release:        0
Summary:        Documentation for texlive-tikzpackets
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tikzpackets and texlive-alldocumentation)

%description -n texlive-tikzpackets-doc
This package includes the documentation for texlive-tikzpackets

%post -n texlive-tikzpackets
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tikzpackets
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tikzpackets
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikzpackets-doc
%{_texmfdistdir}/doc/latex/tikzpackets/README
%{_texmfdistdir}/doc/latex/tikzpackets/tikzPackets.pdf
%{_texmfdistdir}/doc/latex/tikzpackets/tikzPackets.tex

%files -n texlive-tikzpackets
%{_texmfdistdir}/tex/latex/tikzpackets/tikzPackets.sty

%package -n texlive-tikzpagenodes
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn64967
Release:        0
License:        LPPL-1.0
Summary:        A single TikZ node for the whole page
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tikzpagenodes-doc >= %{texlive_version}
Provides:       tex(tikzpagenodes.sty)
Requires:       tex(ifoddpage.sty)
Requires:       tex(tikz.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source83:       tikzpagenodes.tar.xz
Source84:       tikzpagenodes.doc.tar.xz

%description -n texlive-tikzpagenodes
The package provides special PGF/TikZ nodes for the text,
marginpar, footer and header area of the current page. They are
inspired by the 'current page' node defined by PGF/TikZ itself.

%package -n texlive-tikzpagenodes-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn64967
Release:        0
Summary:        Documentation for texlive-tikzpagenodes
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tikzpagenodes and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikzpagenodes-doc
%{_texmfdistdir}/doc/latex/tikzpagenodes/README
%{_texmfdistdir}/doc/latex/tikzpagenodes/tikzpagenodes.pdf

%files -n texlive-tikzpagenodes
%{_texmfdistdir}/tex/latex/tikzpagenodes/tikzpagenodes.sty

%package -n texlive-tikzpeople
Version:        %{texlive_version}.%{texlive_noarch}.0.0.4svn67840
Release:        0
License:        LPPL-1.0
Summary:        Draw people-shaped nodes in TikZ
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tikzpeople-doc >= %{texlive_version}
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
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source85:       tikzpeople.tar.xz
Source86:       tikzpeople.doc.tar.xz

%description -n texlive-tikzpeople
This package provides people-shaped nodes in the style of
Microsoft Visio clip art, to be used with TikZ. The available,
highly customizable, node shapes are: alice, bob, bride,
builder, businessman, charlie, chef, conductor, cowboy,
criminal, dave, devil, duck, graduate, groom, guard, jester,
judge, maininblack, mexican, nun, nurse, physician, pilot,
police, priest, sailor, santa, surgeon.

%package -n texlive-tikzpeople-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.4svn67840
Release:        0
Summary:        Documentation for texlive-tikzpeople
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tikzpeople and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikzpeople-doc
%{_texmfdistdir}/doc/latex/tikzpeople/README.md
%{_texmfdistdir}/doc/latex/tikzpeople/tikzpeople.pdf
%{_texmfdistdir}/doc/latex/tikzpeople/tikzpeople.tex

%files -n texlive-tikzpeople
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

%package -n texlive-tikzpfeile
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn25777
Release:        0
License:        LPPL-1.0
Summary:        Draw arrows using PGF/TikZ
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tikzpfeile-doc >= %{texlive_version}
Provides:       tex(tikzpfeile.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(tikz.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source87:       tikzpfeile.tar.xz
Source88:       tikzpfeile.doc.tar.xz

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
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tikzpfeile and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikzpfeile-doc
%{_texmfdistdir}/doc/latex/tikzpfeile/README
%{_texmfdistdir}/doc/latex/tikzpfeile/tikzpfeile.pdf

%files -n texlive-tikzpfeile
%{_texmfdistdir}/tex/latex/tikzpfeile/tikzpfeile.sty

%package -n texlive-tikzpingus
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn68310
Release:        0
License:        GPL-2.0-or-later
Summary:        Penguins with TikZ
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tikzpingus-doc >= %{texlive_version}
Provides:       tex(tikzpingus-bee.lib.tex)
Provides:       tex(tikzpingus-christmas.lib.tex)
Provides:       tex(tikzpingus-cloak.lib.tex)
Provides:       tex(tikzpingus-devil.lib.tex)
Provides:       tex(tikzpingus-emotions.lib.tex)
Provides:       tex(tikzpingus-flags.lib.tex)
Provides:       tex(tikzpingus-formal.lib.tex)
Provides:       tex(tikzpingus-fun.lib.tex)
Provides:       tex(tikzpingus-glasses.lib.tex)
Provides:       tex(tikzpingus-hats.lib.tex)
Provides:       tex(tikzpingus-horse.lib.tex)
Provides:       tex(tikzpingus-magic.lib.tex)
Provides:       tex(tikzpingus-medieval.lib.tex)
Provides:       tex(tikzpingus-movement.lib.tex)
Provides:       tex(tikzpingus-safe.lib.tex)
Provides:       tex(tikzpingus-science-fiction.lib.tex)
Provides:       tex(tikzpingus-shirts.lib.tex)
Provides:       tex(tikzpingus-signs.lib.tex)
Provides:       tex(tikzpingus-sport.lib.tex)
Provides:       tex(tikzpingus-technology.lib.tex)
Provides:       tex(tikzpingus.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(tikz.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source89:       tikzpingus.tar.xz
Source90:       tikzpingus.doc.tar.xz

%description -n texlive-tikzpingus
tikzpingus is a package similar to tikzducks but with penguins
and a vast set of gadgets and extras (capable of changing the
wing-positions, body-types, and more).

%package -n texlive-tikzpingus-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn68310
Release:        0
Summary:        Documentation for texlive-tikzpingus
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tikzpingus and texlive-alldocumentation)

%description -n texlive-tikzpingus-doc
This package includes the documentation for texlive-tikzpingus

%post -n texlive-tikzpingus
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tikzpingus
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tikzpingus
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikzpingus-doc
%{_texmfdistdir}/doc/latex/tikzpingus/README.md
%{_texmfdistdir}/doc/latex/tikzpingus/tikzpingus-doc.pdf
%{_texmfdistdir}/doc/latex/tikzpingus/tikzpingus-doc.tex

%files -n texlive-tikzpingus
%{_texmfdistdir}/makeindex/tikzpingus/indexstyle.ist
%{_texmfdistdir}/tex/latex/tikzpingus/tikzpingus-bee.lib.tex
%{_texmfdistdir}/tex/latex/tikzpingus/tikzpingus-christmas.lib.tex
%{_texmfdistdir}/tex/latex/tikzpingus/tikzpingus-cloak.lib.tex
%{_texmfdistdir}/tex/latex/tikzpingus/tikzpingus-devil.lib.tex
%{_texmfdistdir}/tex/latex/tikzpingus/tikzpingus-emotions.lib.tex
%{_texmfdistdir}/tex/latex/tikzpingus/tikzpingus-flags.lib.tex
%{_texmfdistdir}/tex/latex/tikzpingus/tikzpingus-formal.lib.tex
%{_texmfdistdir}/tex/latex/tikzpingus/tikzpingus-fun.lib.tex
%{_texmfdistdir}/tex/latex/tikzpingus/tikzpingus-glasses.lib.tex
%{_texmfdistdir}/tex/latex/tikzpingus/tikzpingus-hats.lib.tex
%{_texmfdistdir}/tex/latex/tikzpingus/tikzpingus-horse.lib.tex
%{_texmfdistdir}/tex/latex/tikzpingus/tikzpingus-magic.lib.tex
%{_texmfdistdir}/tex/latex/tikzpingus/tikzpingus-medieval.lib.tex
%{_texmfdistdir}/tex/latex/tikzpingus/tikzpingus-movement.lib.tex
%{_texmfdistdir}/tex/latex/tikzpingus/tikzpingus-safe.lib.tex
%{_texmfdistdir}/tex/latex/tikzpingus/tikzpingus-science-fiction.lib.tex
%{_texmfdistdir}/tex/latex/tikzpingus/tikzpingus-shirts.lib.tex
%{_texmfdistdir}/tex/latex/tikzpingus/tikzpingus-signs.lib.tex
%{_texmfdistdir}/tex/latex/tikzpingus/tikzpingus-sport.lib.tex
%{_texmfdistdir}/tex/latex/tikzpingus/tikzpingus-technology.lib.tex
%{_texmfdistdir}/tex/latex/tikzpingus/tikzpingus.sty

%package -n texlive-tikzposter
Version:        %{texlive_version}.%{texlive_noarch}.2.0svn32732
Release:        0
License:        LPPL-1.0
Summary:        Create scientific posters using TikZ
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tikzposter-doc >= %{texlive_version}
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
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source91:       tikzposter.tar.xz
Source92:       tikzposter.doc.tar.xz

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
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tikzposter and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikzposter-doc
%{_texmfdistdir}/doc/latex/tikzposter/README
%{_texmfdistdir}/doc/latex/tikzposter/tikzposter-example.tex
%{_texmfdistdir}/doc/latex/tikzposter/tikzposter-template.tex
%{_texmfdistdir}/doc/latex/tikzposter/tikzposter.pdf

%files -n texlive-tikzposter
%{_texmfdistdir}/tex/latex/tikzposter/tikzposter.cls
%{_texmfdistdir}/tex/latex/tikzposter/tikzposterBackgroundstyles.tex
%{_texmfdistdir}/tex/latex/tikzposter/tikzposterBlockstyles.tex
%{_texmfdistdir}/tex/latex/tikzposter/tikzposterColorpalettes.tex
%{_texmfdistdir}/tex/latex/tikzposter/tikzposterColorstyles.tex
%{_texmfdistdir}/tex/latex/tikzposter/tikzposterInnerblockstyles.tex
%{_texmfdistdir}/tex/latex/tikzposter/tikzposterLayoutthemes.tex
%{_texmfdistdir}/tex/latex/tikzposter/tikzposterNotestyles.tex
%{_texmfdistdir}/tex/latex/tikzposter/tikzposterTitlestyles.tex

%package -n texlive-tikzquads
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn69409
Release:        0
License:        LPPL-1.0
Summary:        A few shapes designed to be used with CircuiTikZ
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tikzquads-doc >= %{texlive_version}
Provides:       tex(tikzquads.sty)
Requires:       tex(pgfkeysearch.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source93:       tikzquads.tar.xz
Source94:       tikzquads.doc.tar.xz

%description -n texlive-tikzquads
This package defines a few extra shapes, Quadripoles and single
port, which can be used 'standalone', but are mainly meant to
be used with CircuiTikZ.

%package -n texlive-tikzquads-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn69409
Release:        0
Summary:        Documentation for texlive-tikzquads
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tikzquads and texlive-alldocumentation)

%description -n texlive-tikzquads-doc
This package includes the documentation for texlive-tikzquads

%post -n texlive-tikzquads
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tikzquads
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tikzquads
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikzquads-doc
%{_texmfdistdir}/doc/latex/tikzquads/README.md
%{_texmfdistdir}/doc/latex/tikzquads/tikzquads.pdf
%{_texmfdistdir}/doc/latex/tikzquads/tikzquads.tex

%files -n texlive-tikzquads
%{_texmfdistdir}/tex/latex/tikzquads/tikzquads.sty

%package -n texlive-tikzquests
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn69388
Release:        0
License:        LPPL-1.0
Summary:        A parametric questions' repositories framework
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tikzquests-doc >= %{texlive_version}
Provides:       tex(tikzquests.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source95:       tikzquests.tar.xz
Source96:       tikzquests.doc.tar.xz

%description -n texlive-tikzquests
This is a framework for building parametric questions'
repositories, which can be further used to construct parametric
questions for exams. Unlike other packages of the kind this
does not try to enforce any pre-defined presentation format,
focusing only on how to set a repository of questions and use
them.

%package -n texlive-tikzquests-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn69388
Release:        0
Summary:        Documentation for texlive-tikzquests
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tikzquests and texlive-alldocumentation)

%description -n texlive-tikzquests-doc
This package includes the documentation for texlive-tikzquests

%post -n texlive-tikzquests
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tikzquests
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tikzquests
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikzquests-doc
%{_texmfdistdir}/doc/latex/tikzquests/README.md
%{_texmfdistdir}/doc/latex/tikzquests/tikzquests.pdf
%{_texmfdistdir}/doc/latex/tikzquests/tikzquests.tex

%files -n texlive-tikzquests
%{_texmfdistdir}/tex/latex/tikzquests/tikzquests.sty

%package -n texlive-tikzscale
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2.6svn30637
Release:        0
License:        LPPL-1.0
Summary:        Resize pictures while respecting text size
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tikzscale-doc >= %{texlive_version}
Provides:       tex(tikzscale.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(letltxmacro.sty)
Requires:       tex(pgfkeys.sty)
Requires:       tex(xparse.sty)
Requires:       tex(xstring.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source97:       tikzscale.tar.xz
Source98:       tikzscale.doc.tar.xz

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
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tikzscale and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikzscale-doc
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
%{_texmfdistdir}/tex/latex/tikzscale/tikzscale.sty

%package -n texlive-tikzsymbols
Version:        %{texlive_version}.%{texlive_noarch}.4.12asvn61300
Release:        0
License:        LPPL-1.0
Summary:        Some symbols created using TikZ
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tikzsymbols-doc >= %{texlive_version}
Provides:       tex(tikzsymbols.sty)
Requires:       tex(expl3.sty)
Requires:       tex(l3keys2e.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xparse.sty)
Requires:       tex(xspace.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source99:       tikzsymbols.tar.xz
Source100:      tikzsymbols.doc.tar.xz

%description -n texlive-tikzsymbols
The package provides various emoticons, cooking symbols and
trees.

%package -n texlive-tikzsymbols-doc
Version:        %{texlive_version}.%{texlive_noarch}.4.12asvn61300
Release:        0
Summary:        Documentation for texlive-tikzsymbols
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tikzsymbols and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikzsymbols-doc
%{_texmfdistdir}/doc/latex/tikzsymbols/README.md
%{_texmfdistdir}/doc/latex/tikzsymbols/tikzsymbols.pdf

%files -n texlive-tikzsymbols
%{_texmfdistdir}/tex/latex/tikzsymbols/tikzsymbols.sty

%package -n texlive-tikztosvg
Version:        %{texlive_version}.%{texlive_noarch}.0.0.3.0svn60289
Release:        0
License:        GPL-2.0-or-later
Summary:        A utility for rendering TikZ diagrams to SVG
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-tikztosvg-bin >= %{texlive_version}
#!BuildIgnore: texlive-tikztosvg-bin
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tikztosvg-doc >= %{texlive_version}
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source101:      tikztosvg.tar.xz
Source102:      tikztosvg.doc.tar.xz

%description -n texlive-tikztosvg
This package provides a shell script that calls XeTeX and
pdf2svg to convert TikZ environments to SVG files.

%package -n texlive-tikztosvg-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.3.0svn60289
Release:        0
Summary:        Documentation for texlive-tikztosvg
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tikztosvg and texlive-alldocumentation)
Provides:       man(tikztosvg.1)

%description -n texlive-tikztosvg-doc
This package includes the documentation for texlive-tikztosvg

%post -n texlive-tikztosvg
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tikztosvg
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tikztosvg
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikztosvg-doc
%{_mandir}/man1/tikztosvg.1*
%{_texmfdistdir}/doc/support/tikztosvg/CHANGELOG.md
%{_texmfdistdir}/doc/support/tikztosvg/LICENSE
%{_texmfdistdir}/doc/support/tikztosvg/Makefile
%{_texmfdistdir}/doc/support/tikztosvg/README.md
%{_texmfdistdir}/doc/support/tikztosvg/example.svg
%{_texmfdistdir}/doc/support/tikztosvg/example.tikz
%{_texmfdistdir}/doc/support/tikztosvg/man.adoc
%{_texmfdistdir}/doc/support/tikztosvg/tikztosvg.pdf

%files -n texlive-tikztosvg
%{_texmfdistdir}/scripts/tikztosvg/tikztosvg

%package -n texlive-tikzviolinplots
Version:        %{texlive_version}.%{texlive_noarch}.0.0.7.2svn66659
Release:        0
License:        LPPL-1.0
Summary:        Draws violin plots from data
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tikzviolinplots-doc >= %{texlive_version}
Provides:       tex(tikzviolinplots.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(pgfkeys.sty)
Requires:       tex(pgfplots.sty)
Requires:       tex(pgfplotstable.sty)
Requires:       tex(stringstrings.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source103:      tikzviolinplots.tar.xz
Source104:      tikzviolinplots.doc.tar.xz

%description -n texlive-tikzviolinplots
This package enables the user to draw violin plots, calculating
the kernel density estimation from the data and plotting the
resulting curve inside a tikzpicture environment. It supports
different kernels, and allows the user to either set the
bandwidth value for each plot or use a default value.

%package -n texlive-tikzviolinplots-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.7.2svn66659
Release:        0
Summary:        Documentation for texlive-tikzviolinplots
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tikzviolinplots and texlive-alldocumentation)

%description -n texlive-tikzviolinplots-doc
This package includes the documentation for texlive-tikzviolinplots

%post -n texlive-tikzviolinplots
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tikzviolinplots
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tikzviolinplots
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tikzviolinplots-doc
%{_texmfdistdir}/doc/latex/tikzviolinplots/AFR.csv
%{_texmfdistdir}/doc/latex/tikzviolinplots/AMR.csv
%{_texmfdistdir}/doc/latex/tikzviolinplots/EMR.csv
%{_texmfdistdir}/doc/latex/tikzviolinplots/EUR.csv
%{_texmfdistdir}/doc/latex/tikzviolinplots/LICENSE
%{_texmfdistdir}/doc/latex/tikzviolinplots/README.md
%{_texmfdistdir}/doc/latex/tikzviolinplots/SEAR.csv
%{_texmfdistdir}/doc/latex/tikzviolinplots/WPR.csv
%{_texmfdistdir}/doc/latex/tikzviolinplots/tikzviolinplots.pdf
%{_texmfdistdir}/doc/latex/tikzviolinplots/tikzviolinplots.tex

%files -n texlive-tikzviolinplots
%{_texmfdistdir}/tex/latex/tikzviolinplots/tikzviolinplots.sty

%package -n texlive-tile-graphic
Version:        %{texlive_version}.%{texlive_noarch}.svn55325
Release:        0
License:        LPPL-1.0
Summary:        Create tiles of a graphical file
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tile-graphic-doc >= %{texlive_version}
Provides:       tex(tile-graphic.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(multido.sty)
Requires:       tex(shellesc.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source105:      tile-graphic.tar.xz
Source106:      tile-graphic.doc.tar.xz

%description -n texlive-tile-graphic
This package breaks a given graphical file into n rows and m
columns of subgraphics, which are called tiles. The tiles can
be written separately to individual PDF files, or packaged into
a single PDF file.

%package -n texlive-tile-graphic-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn55325
Release:        0
Summary:        Documentation for texlive-tile-graphic
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tile-graphic and texlive-alldocumentation)

%description -n texlive-tile-graphic-doc
This package includes the documentation for texlive-tile-graphic

%post -n texlive-tile-graphic
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tile-graphic
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tile-graphic
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tile-graphic-doc
%{_texmfdistdir}/doc/latex/tile-graphic/README.md
%{_texmfdistdir}/doc/latex/tile-graphic/docs/tile-graphic.pdf
%{_texmfdistdir}/doc/latex/tile-graphic/examples/choo/choo.pdf
%{_texmfdistdir}/doc/latex/tile-graphic/examples/create-tg.tex
%{_texmfdistdir}/doc/latex/tile-graphic/examples/flowers.pdf
%{_texmfdistdir}/doc/latex/tile-graphic/examples/postscript/flowers.eps
%{_texmfdistdir}/doc/latex/tile-graphic/examples/postscript/flowers.pdf
%{_texmfdistdir}/doc/latex/tile-graphic/tg.cfg.txt

%files -n texlive-tile-graphic
%{_texmfdistdir}/tex/latex/tile-graphic/tile-graphic.sty

%package -n texlive-tilings
Version:        %{texlive_version}.%{texlive_noarch}.2.0svn67292
Release:        0
License:        LPPL-1.0
Summary:        A TikZ library for drawing tiles and tilings
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tilings-doc >= %{texlive_version}
Provides:       tex(tikzlibrarypenrose.code.tex)
Provides:       tex(tikzlibrarytilings.code.tex)
Provides:       tex(tikzlibrarytilings.penrose.code.tex)
Provides:       tex(tikzlibrarytilings.polykite.code.tex)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source107:      tilings.tar.xz
Source108:      tilings.doc.tar.xz

%description -n texlive-tilings
This package provides a TikZ library for working with tiles,
tilings, and tessellations. Using it, one can define tiles,
place tiles, deform tiles, and -- in some cases -- apply
replacement rules to generate tessellations. It has pre-defined
tiles for most of the Penrose tile sets and the aperiodical
polykite tiles. This is a replacement for the penrose package,
renamed as it now deals with more extensive tiles than just the
Penrose tile sets.

%package -n texlive-tilings-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.0svn67292
Release:        0
Summary:        Documentation for texlive-tilings
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tilings and texlive-alldocumentation)

%description -n texlive-tilings-doc
This package includes the documentation for texlive-tilings

%post -n texlive-tilings
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tilings
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tilings
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tilings-doc
%{_texmfdistdir}/doc/latex/tilings/README
%{_texmfdistdir}/doc/latex/tilings/README.txt
%{_texmfdistdir}/doc/latex/tilings/tilings.pdf
%{_texmfdistdir}/doc/latex/tilings/tilings.tex
%{_texmfdistdir}/doc/latex/tilings/tilings_code.pdf

%files -n texlive-tilings
%{_texmfdistdir}/tex/latex/tilings/tikzlibrarypenrose.code.tex
%{_texmfdistdir}/tex/latex/tilings/tikzlibrarytilings.code.tex
%{_texmfdistdir}/tex/latex/tilings/tikzlibrarytilings.penrose.code.tex
%{_texmfdistdir}/tex/latex/tilings/tikzlibrarytilings.polykite.code.tex

%package -n texlive-timbreicmc
Version:        %{texlive_version}.%{texlive_noarch}.2.0svn49740
Release:        0
License:        LPPL-1.0
Summary:        Typeset documents with ICMC/USP watermarks
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-timbreicmc-doc >= %{texlive_version}
Provides:       tex(timbreicmc.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xwatermark.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source109:      timbreicmc.tar.xz
Source110:      timbreicmc.doc.tar.xz

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
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-timbreicmc and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-timbreicmc-doc
%{_texmfdistdir}/doc/latex/timbreicmc/README.md
%{_texmfdistdir}/doc/latex/timbreicmc/timbreicmc.pdf

%files -n texlive-timbreicmc
%{_texmfdistdir}/tex/latex/timbreicmc/timbreicmc.sty

%package -n texlive-times
Version:        %{texlive_version}.%{texlive_noarch}.svn61719
Release:        0
License:        GPL-2.0-or-later
Summary:        URW 'Base 35' font pack for LaTeX
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source111:      times.tar.xz

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
Version:        %{texlive_version}.%{texlive_noarch}.svn61719
Release:        0
Summary:        Severed fonts for texlive-times
License:        GPL-2.0-or-later
URL:            https://www.tug.org/texlive/
Group:          Productivity/Publishing/TeX/Fonts
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Suggests:       xorg-x11-fonts-core

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-times-fonts

%files -n texlive-times
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
%dir %{_datadir}/fonts/texlive-times
%{_datadir}/fontconfig/conf.avail/58-texlive-times.conf
%verify(not md5 size mtime) %{_datadir}/fonts/texlive-times/encodings.dir
%verify(not md5 size mtime) %{_datadir}/fonts/texlive-times/fonts.dir
%verify(not md5 size mtime) %{_datadir}/fonts/texlive-times/fonts.scale
%{_datadir}/fonts/texlive-times/utmb8a.pfb
%{_datadir}/fonts/texlive-times/utmbi8a.pfb
%{_datadir}/fonts/texlive-times/utmr8a.pfb
%{_datadir}/fonts/texlive-times/utmri8a.pfb

%package -n texlive-timetable
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
License:        LPPL-1.0
Summary:        Generate timetables
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source112:      timetable.tar.xz

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-timetable
%{_texmfdistdir}/tex/plain/timetable/timetable.tex

%package -n texlive-timing-diagrams
Version:        %{texlive_version}.%{texlive_noarch}.svn31491
Release:        0
License:        LPPL-1.0
Summary:        Draw timing diagrams
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-timing-diagrams-doc >= %{texlive_version}
Provides:       tex(timing-diagrams.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(tikz.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source113:      timing-diagrams.tar.xz
Source114:      timing-diagrams.doc.tar.xz

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
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-timing-diagrams and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-timing-diagrams-doc
%{_texmfdistdir}/doc/latex/timing-diagrams/Makefile
%{_texmfdistdir}/doc/latex/timing-diagrams/README
%{_texmfdistdir}/doc/latex/timing-diagrams/diagrams-examples.pdf
%{_texmfdistdir}/doc/latex/timing-diagrams/diagrams-examples.tex
%{_texmfdistdir}/doc/latex/timing-diagrams/version.txt

%files -n texlive-timing-diagrams
%{_texmfdistdir}/tex/latex/timing-diagrams/timing-diagrams.sty

%package -n texlive-tinos
Version:        %{texlive_version}.%{texlive_noarch}.svn68950
Release:        0
License:        Apache-1.0
Summary:        Tinos fonts with LaTeX support
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tinos-doc >= %{texlive_version}
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
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source115:      tinos.tar.xz
Source116:      tinos.doc.tar.xz

%description -n texlive-tinos
Tinos, designed by Steve Matteson, is an innovative, refreshing
serif design that is metrically compatible with Times New
Roman.

%package -n texlive-tinos-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn68950
Release:        0
Summary:        Documentation for texlive-tinos
License:        Apache-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tinos and texlive-alldocumentation)

%description -n texlive-tinos-doc
This package includes the documentation for texlive-tinos

%package -n texlive-tinos-fonts
Version:        %{texlive_version}.%{texlive_noarch}.svn68950
Release:        0
Summary:        Severed fonts for texlive-tinos
License:        Apache-1.0
URL:            https://www.tug.org/texlive/
Group:          Productivity/Publishing/TeX/Fonts
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Suggests:       xorg-x11-fonts-core

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-tinos-fonts

%files -n texlive-tinos-doc
%{_texmfdistdir}/doc/fonts/tinos/LICENSE.txt
%{_texmfdistdir}/doc/fonts/tinos/README
%{_texmfdistdir}/doc/fonts/tinos/tinos-samples.pdf
%{_texmfdistdir}/doc/fonts/tinos/tinos-samples.tex

%files -n texlive-tinos
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
%dir %{_datadir}/fonts/texlive-tinos
%{_datadir}/fontconfig/conf.avail/58-texlive-tinos.conf
%{_datadir}/fontconfig/conf.avail/55-texlive-tinos.conf
%config %{_sysconfdir}/fonts/conf.d/55-texlive-tinos.conf
%verify(not md5 size mtime) %{_datadir}/fonts/texlive-tinos/encodings.dir
%verify(not md5 size mtime) %{_datadir}/fonts/texlive-tinos/fonts.dir
%verify(not md5 size mtime) %{_datadir}/fonts/texlive-tinos/fonts.scale
%{_datadir}/fonts/texlive-tinos/Tinos-Bold.ttf
%{_datadir}/fonts/texlive-tinos/Tinos-BoldItalic.ttf
%{_datadir}/fonts/texlive-tinos/Tinos-Italic.ttf
%{_datadir}/fonts/texlive-tinos/Tinos-Regular.ttf
%{_datadir}/fonts/texlive-tinos/Tinos-Bold.pfb
%{_datadir}/fonts/texlive-tinos/Tinos-BoldItalic.pfb
%{_datadir}/fonts/texlive-tinos/Tinos-Italic.pfb
%{_datadir}/fonts/texlive-tinos/Tinos.pfb

%package -n texlive-tipa
Version:        %{texlive_version}.%{texlive_noarch}.1.3svn29349
Release:        0
License:        LPPL-1.0
Summary:        Fonts and macros for IPA phonetics characters
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tipa-doc >= %{texlive_version}
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
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source117:      tipa.tar.xz
Source118:      tipa.doc.tar.xz

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
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tipa and texlive-alldocumentation)
Provides:       locale(texlive-tipa-doc:en)

%description -n texlive-tipa-doc
This package includes the documentation for texlive-tipa

%package -n texlive-tipa-fonts
Version:        %{texlive_version}.%{texlive_noarch}.1.3svn29349
Release:        0
Summary:        Severed fonts for texlive-tipa
License:        LPPL-1.0
URL:            https://www.tug.org/texlive/
Group:          Productivity/Publishing/TeX/Fonts
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Suggests:       xorg-x11-fonts-core

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-tipa-fonts

%files -n texlive-tipa-doc
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
%dir %{_datadir}/fonts/texlive-tipa
%{_datadir}/fontconfig/conf.avail/58-texlive-tipa.conf
%verify(not md5 size mtime) %{_datadir}/fonts/texlive-tipa/encodings.dir
%verify(not md5 size mtime) %{_datadir}/fonts/texlive-tipa/fonts.dir
%verify(not md5 size mtime) %{_datadir}/fonts/texlive-tipa/fonts.scale
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

%package -n texlive-tipa-de
Version:        %{texlive_version}.%{texlive_noarch}.1.3svn22005
Release:        0
License:        LPPL-1.0
Summary:        German translation of tipa documentation
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source119:      tipa-de.doc.tar.xz

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tipa-de
%{_texmfdistdir}/doc/latex/tipa-de/LIESMICH
%{_texmfdistdir}/doc/latex/tipa-de/tipa.bib
%{_texmfdistdir}/doc/latex/tipa-de/tipaman-de.pdf
%{_texmfdistdir}/doc/latex/tipa-de/tipaman-de.tex
%{_texmfdistdir}/doc/latex/tipa-de/tipaman0-de.tex
%{_texmfdistdir}/doc/latex/tipa-de/tipaman1-de.tex
%{_texmfdistdir}/doc/latex/tipa-de/tipaman2-de.tex
%{_texmfdistdir}/doc/latex/tipa-de/tipaman3-de.tex
%{_texmfdistdir}/doc/latex/tipa-de/tipaman4-de.tex

%package -n texlive-tipauni
Version:        %{texlive_version}.%{texlive_noarch}.0.0.7asvn65817
Release:        0
License:        GPL-2.0-or-later
Summary:        Producing Unicode characters with TIPA commands
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Obsoletes:      texlive-unitipa < 2022
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
Suggests:       texlive-tipauni-doc >= %{texlive_version}
Provides:       tex(tipauni.sty)
Requires:       tex(expkv-def.sty)
Requires:       tex(expkv-opt.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(xparse.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source120:      tipauni.tar.xz
Source121:      tipauni.doc.tar.xz

%description -n texlive-tipauni
Package TIPA uses the T3 encoding for producing IPA characters.
The package is widely used in the field of linguistics, but
because of the old encoding, the output documents are less
productive than Unicode-based documents. This package redefines
most of the TIPA-commands for outputting Unicode characters.
Users can now use their beloved TIPA shortcuts with the
benefits of Unicode, i.e. searchability, copy-pasting, changing
the font and many more. As this package needs the fontspec
package for loading an IPA font, it needs to be compiled with
XeLaTeX or LuaLaTeX. This package can also be viewed as an
ASCII-based input method for producing IPA characters in
Unicode. It needs the New Computer Modern font for printing IPA
characters.

%package -n texlive-tipauni-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.7asvn65817
Release:        0
Summary:        Documentation for texlive-tipauni
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Obsoletes:      texlive-unitipa-doc < 2022
Supplements:    (texlive-tipauni and texlive-alldocumentation)

%description -n texlive-tipauni-doc
This package includes the documentation for texlive-tipauni

%post -n texlive-tipauni
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tipauni
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tipauni
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tipauni-doc
%{_texmfdistdir}/doc/latex/tipauni/README.txt
%{_texmfdistdir}/doc/latex/tipauni/tipauni-commands.pdf
%{_texmfdistdir}/doc/latex/tipauni/tipauni-commands.tex
%{_texmfdistdir}/doc/latex/tipauni/tipauni-example.pdf
%{_texmfdistdir}/doc/latex/tipauni/tipauni-example.tex
%{_texmfdistdir}/doc/latex/tipauni/tipauni.pdf

%files -n texlive-tipauni
%{_texmfdistdir}/tex/latex/tipauni/tipauni-newcm-book.fontspec
%{_texmfdistdir}/tex/latex/tipauni/tipauni-newcm-regular.fontspec
%{_texmfdistdir}/tex/latex/tipauni/tipauni.sty

%package -n texlive-tipfr
Version:        %{texlive_version}.%{texlive_noarch}.1.5svn38646
Release:        0
License:        LPPL-1.0
Summary:        Produces calculator's keys with the help of TikZ
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tipfr-doc >= %{texlive_version}
Provides:       tex(tipfr.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(mathtools.sty)
Requires:       tex(multido.sty)
Requires:       tex(newtxtt.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source122:      tipfr.tar.xz
Source123:      tipfr.doc.tar.xz

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
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tipfr and texlive-alldocumentation)
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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tipfr-doc
%{_texmfdistdir}/doc/latex/tipfr/IndexHead.ist
%{_texmfdistdir}/doc/latex/tipfr/README
%{_texmfdistdir}/doc/latex/tipfr/tipfr-doc.pdf
%{_texmfdistdir}/doc/latex/tipfr/tipfr-doc.tex

%files -n texlive-tipfr
%{_texmfdistdir}/tex/latex/tipfr/tipfr.sty

%package -n texlive-tiscreen
Version:        %{texlive_version}.%{texlive_noarch}.svn62602
Release:        0
License:        LPPL-1.0
Summary:        Mimic the screen of older Texas Instruments calculators
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tiscreen-doc >= %{texlive_version}
Provides:       tex(tiscreen.sty)
Requires:       tex(array.sty)
Requires:       tex(lcd.sty)
Requires:       tex(tcolorbox.sty)
Requires:       tex(textgreek.sty)
Requires:       tex(tikz.sty)
Requires:       tex(tipa.sty)
Requires:       tex(wasysym.sty)
Requires:       tex(xcolor.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source124:      tiscreen.tar.xz
Source125:      tiscreen.doc.tar.xz

%description -n texlive-tiscreen
This package mimics the screen of older Texas Instruments dot
matrix display calculators, specifically the TI-82 STATS. It
relies on the lcd and xcolor packages.

%package -n texlive-tiscreen-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn62602
Release:        0
Summary:        Documentation for texlive-tiscreen
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tiscreen and texlive-alldocumentation)

%description -n texlive-tiscreen-doc
This package includes the documentation for texlive-tiscreen

%post -n texlive-tiscreen
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tiscreen
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tiscreen
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tiscreen-doc
%{_texmfdistdir}/doc/latex/tiscreen/README
%{_texmfdistdir}/doc/latex/tiscreen/tiscreen-doc.pdf
%{_texmfdistdir}/doc/latex/tiscreen/tiscreen-doc.tex

%files -n texlive-tiscreen
%{_texmfdistdir}/tex/latex/tiscreen/tiscreen.sty

%package -n texlive-titlecaps
Version:        %{texlive_version}.%{texlive_noarch}.1.3svn63020
Release:        0
License:        LPPL-1.0
Summary:        Setting rich-text input into Titling Caps
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-titlecaps-doc >= %{texlive_version}
Provides:       tex(titlecaps.sty)
Requires:       tex(ifnextok.sty)
Requires:       tex(ifthen.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source126:      titlecaps.tar.xz
Source127:      titlecaps.doc.tar.xz

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
Version:        %{texlive_version}.%{texlive_noarch}.1.3svn63020
Release:        0
Summary:        Documentation for texlive-titlecaps
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-titlecaps and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-titlecaps-doc
%{_texmfdistdir}/doc/latex/titlecaps/README
%{_texmfdistdir}/doc/latex/titlecaps/titlecaps.pdf
%{_texmfdistdir}/doc/latex/titlecaps/titlecaps.tex

%files -n texlive-titlecaps
%{_texmfdistdir}/tex/latex/titlecaps/titlecaps.sty

%package -n texlive-titlefoot
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
License:        LPPL-1.0
Summary:        Add special material to footer of title page
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source128:      titlefoot.tar.xz

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-titlefoot
%{_texmfdistdir}/tex/latex/titlefoot/titlefoot.sty

%package -n texlive-titlepages
Version:        %{texlive_version}.%{texlive_noarch}.svn19457
Release:        0
License:        LPPL-1.0
Summary:        Sample titlepages, and how to code them
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source129:      titlepages.doc.tar.xz

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-titlepages
%{_texmfdistdir}/doc/latex/titlepages/README
%{_texmfdistdir}/doc/latex/titlepages/titlepages.pdf
%{_texmfdistdir}/doc/latex/titlepages/titlepages.tex

%package -n texlive-titlepic
Version:        %{texlive_version}.%{texlive_noarch}.1.2svn43497
Release:        0
License:        SUSE-Public-Domain
Summary:        Add picture to title page of a document
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-titlepic-doc >= %{texlive_version}
Provides:       tex(titlepic.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source130:      titlepic.tar.xz
Source131:      titlepic.doc.tar.xz

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
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-titlepic and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-titlepic-doc
%{_texmfdistdir}/doc/latex/titlepic/README.md
%{_texmfdistdir}/doc/latex/titlepic/titlepic-manual.pdf
%{_texmfdistdir}/doc/latex/titlepic/titlepic-manual.tex

%files -n texlive-titlepic
%{_texmfdistdir}/tex/latex/titlepic/titlepic.sty

%package -n texlive-titleref
Version:        %{texlive_version}.%{texlive_noarch}.3.1svn18729
Release:        0
License:        SUSE-Public-Domain
Summary:        A "\titleref" command to cross-reference section titles
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-titleref-doc >= %{texlive_version}
Provides:       tex(titleref.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source132:      titleref.tar.xz
Source133:      titleref.doc.tar.xz

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
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-titleref and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-titleref-doc
%{_texmfdistdir}/doc/latex/titleref/miscdoc.sty
%{_texmfdistdir}/doc/latex/titleref/titleref.pdf
%{_texmfdistdir}/doc/latex/titleref/titleref.tex

%files -n texlive-titleref
%{_texmfdistdir}/tex/latex/titleref/titleref.sty

%package -n texlive-titlesec
Version:        %{texlive_version}.%{texlive_noarch}.2.16svn68677
Release:        0
License:        LPPL-1.0
Summary:        Select alternative section titles
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-titlesec-doc >= %{texlive_version}
Provides:       tex(titleps.sty)
Provides:       tex(titlesec.sty)
Provides:       tex(titletoc.sty)
Requires:       tex(etex.sty)
Requires:       tex(keyval.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source134:      titlesec.tar.xz
Source135:      titlesec.doc.tar.xz

%description -n texlive-titlesec
A package providing an interface to sectioning commands for
selection from various title styles. E.g., marginal titles and
to change the font of all headings with a single command, also
providing simple one-step page styles. Also includes a package
to change the page styles when there are floats in a page. You
may assign headers/footers to individual floats, too.

%package -n texlive-titlesec-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.16svn68677
Release:        0
Summary:        Documentation for texlive-titlesec
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-titlesec and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-titlesec-doc
%{_texmfdistdir}/doc/latex/titlesec/CHANGES.old
%{_texmfdistdir}/doc/latex/titlesec/README.md
%{_texmfdistdir}/doc/latex/titlesec/titleps.pdf
%{_texmfdistdir}/doc/latex/titlesec/titleps.tex
%{_texmfdistdir}/doc/latex/titlesec/titlesec.pdf
%{_texmfdistdir}/doc/latex/titlesec/titlesec.tex

%files -n texlive-titlesec
%{_texmfdistdir}/tex/latex/titlesec/titleps.sty
%{_texmfdistdir}/tex/latex/titlesec/titlesec.sty
%{_texmfdistdir}/tex/latex/titlesec/titletoc.sty

%package -n texlive-titling
Version:        %{texlive_version}.%{texlive_noarch}.2.1dsvn15878
Release:        0
License:        LPPL-1.0
Summary:        Control over the typesetting of the \maketitle command
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-titling-doc >= %{texlive_version}
Provides:       tex(titling.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source136:      titling.tar.xz
Source137:      titling.doc.tar.xz

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
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-titling and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-titling-doc
%{_texmfdistdir}/doc/latex/titling/README
%{_texmfdistdir}/doc/latex/titling/titling.pdf

%files -n texlive-titling
%{_texmfdistdir}/tex/latex/titling/titling.sty

%package -n texlive-tkz-base
Version:        %{texlive_version}.%{texlive_noarch}.4.21csvn69460
Release:        0
License:        LPPL-1.0
Summary:        Tools for drawing with a cartesian coordinate system
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tkz-base-doc >= %{texlive_version}
Provides:       tex(tkz-base.cfg)
Provides:       tex(tkz-base.sty)
Provides:       tex(tkz-lib-marks.tex)
Provides:       tex(tkz-lib-shape.tex)
Provides:       tex(tkz-obj-axes.tex)
Provides:       tex(tkz-obj-grids.tex)
Provides:       tex(tkz-obj-marks.tex)
Provides:       tex(tkz-obj-points.tex)
Provides:       tex(tkz-obj-rep.tex)
Provides:       tex(tkz-tools-BB.tex)
Provides:       tex(tkz-tools-arith.tex)
Provides:       tex(tkz-tools-base.tex)
Provides:       tex(tkz-tools-colors.tex)
Provides:       tex(tkz-tools-misc.tex)
Provides:       tex(tkz-tools-modules.tex)
Provides:       tex(tkz-tools-print.tex)
Provides:       tex(tkz-tools-text.tex)
Provides:       tex(tkz-tools-utilities.tex)
Requires:       tex(fp.sty)
Requires:       tex(numprint.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xfp.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source138:      tkz-base.tar.xz
Source139:      tkz-base.doc.tar.xz

%description -n texlive-tkz-base
The bundle is a set of packages, designed to give mathematics
teachers (and students) easy access to programming of drawings
with TikZ.

%package -n texlive-tkz-base-doc
Version:        %{texlive_version}.%{texlive_noarch}.4.21csvn69460
Release:        0
Summary:        Documentation for texlive-tkz-base
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tkz-base and texlive-alldocumentation)
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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tkz-base-doc
%{_texmfdistdir}/doc/latex/tkz-base/README.md
%{_texmfdistdir}/doc/latex/tkz-base/TKZdoc-base-BB.tex
%{_texmfdistdir}/doc/latex/tkz-base/TKZdoc-base-axes.tex
%{_texmfdistdir}/doc/latex/tkz-base/TKZdoc-base-compilation.tex
%{_texmfdistdir}/doc/latex/tkz-base/TKZdoc-base-divers.tex
%{_texmfdistdir}/doc/latex/tkz-base/TKZdoc-base-example.tex
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
%{_texmfdistdir}/doc/latex/tkz-base/tiger.pdf
%{_texmfdistdir}/doc/latex/tkz-base/tkz-base.pdf

%files -n texlive-tkz-base
%{_texmfdistdir}/tex/latex/tkz-base/tkz-base.cfg
%{_texmfdistdir}/tex/latex/tkz-base/tkz-base.sty
%{_texmfdistdir}/tex/latex/tkz-base/tkz-lib-marks.tex
%{_texmfdistdir}/tex/latex/tkz-base/tkz-lib-shape.tex
%{_texmfdistdir}/tex/latex/tkz-base/tkz-obj-axes.tex
%{_texmfdistdir}/tex/latex/tkz-base/tkz-obj-grids.tex
%{_texmfdistdir}/tex/latex/tkz-base/tkz-obj-marks.tex
%{_texmfdistdir}/tex/latex/tkz-base/tkz-obj-points.tex
%{_texmfdistdir}/tex/latex/tkz-base/tkz-obj-rep.tex
%{_texmfdistdir}/tex/latex/tkz-base/tkz-tools-BB.tex
%{_texmfdistdir}/tex/latex/tkz-base/tkz-tools-arith.tex
%{_texmfdistdir}/tex/latex/tkz-base/tkz-tools-base.tex
%{_texmfdistdir}/tex/latex/tkz-base/tkz-tools-colors.tex
%{_texmfdistdir}/tex/latex/tkz-base/tkz-tools-misc.tex
%{_texmfdistdir}/tex/latex/tkz-base/tkz-tools-modules.tex
%{_texmfdistdir}/tex/latex/tkz-base/tkz-tools-print.tex
%{_texmfdistdir}/tex/latex/tkz-base/tkz-tools-text.tex
%{_texmfdistdir}/tex/latex/tkz-base/tkz-tools-utilities.tex

%package -n texlive-tkz-berge
Version:        %{texlive_version}.%{texlive_noarch}.2.0svn57485
Release:        0
License:        LPPL-1.0
Summary:        Macros for drawing graphs of graph theory
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tkz-berge-doc >= %{texlive_version}
Provides:       tex(tkz-berge.sty)
Requires:       tex(tkz-graph.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source140:      tkz-berge.tar.xz
Source141:      tkz-berge.doc.tar.xz

%description -n texlive-tkz-berge
The package provides a collection of useful macros for drawing
classic graphs of graph theory, or to make other graphs. This
package has been taken temporarily out of circulation to give
the author time to investigate some problems.

%package -n texlive-tkz-berge-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.0svn57485
Release:        0
Summary:        Documentation for texlive-tkz-berge
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tkz-berge and texlive-alldocumentation)

%description -n texlive-tkz-berge-doc
This package includes the documentation for texlive-tkz-berge

%post -n texlive-tkz-berge
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tkz-berge
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tkz-berge
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tkz-berge-doc
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/doc/NamedGraphs.pdf
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/doc/latex/NamedGraphs-Andrasfai.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/doc/latex/NamedGraphs-Balaban.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/doc/latex/NamedGraphs-Bipartite.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/doc/latex/NamedGraphs-Bull.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/doc/latex/NamedGraphs-Cage.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/doc/latex/NamedGraphs-Chvatal.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/doc/latex/NamedGraphs-Cocktail_Party.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/doc/latex/NamedGraphs-Coxeter.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/doc/latex/NamedGraphs-Crown.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/doc/latex/NamedGraphs-CubicSymmetric.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/doc/latex/NamedGraphs-Desargues.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/doc/latex/NamedGraphs-Doyle.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/doc/latex/NamedGraphs-Dyck.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/doc/latex/NamedGraphs-Folkman.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/doc/latex/NamedGraphs-Foster.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/doc/latex/NamedGraphs-Franklin.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/doc/latex/NamedGraphs-Gray.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/doc/latex/NamedGraphs-Groetzsch.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/doc/latex/NamedGraphs-Harries.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/doc/latex/NamedGraphs-Heawood.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/doc/latex/NamedGraphs-Hypercube.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/doc/latex/NamedGraphs-Koenisberg.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/doc/latex/NamedGraphs-Levi.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/doc/latex/NamedGraphs-McGee.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/doc/latex/NamedGraphs-Moebius.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/doc/latex/NamedGraphs-Nauru.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/doc/latex/NamedGraphs-Pappus.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/doc/latex/NamedGraphs-Petersen.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/doc/latex/NamedGraphs-Platonic.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/doc/latex/NamedGraphs-Robertson.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/doc/latex/NamedGraphs-Tutte.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/doc/latex/NamedGraphs-Wong.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/doc/latex/NamedGraphs-couverture.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/doc/latex/NamedGraphs-main.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-1-1-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-1-2-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-1-3-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-10-1-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-10-2-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-11-1-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-11-2-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-11-3-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-11-4-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-12-1-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-12-2-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-12-3-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-12-4-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-13-1-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-13-2-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-13-3-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-13-4-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-14-1-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-15-1-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-15-2-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-15-3-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-16-0-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-17-1-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-17-2-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-17-3-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-18-1-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-18-2-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-19-1-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-2-1-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-2-2-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-2-3-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-2-4-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-20-1-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-20-2-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-21-0-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-21-1-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-21-2-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-22-1-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-22-2-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-22-3-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-23-1-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-23-2-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-23-3-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-23-4-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-23-5-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-23-6-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-23-7-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-24-1-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-24-2-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-24-3-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-25-1-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-25-2-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-25-3-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-25-4-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-25-5-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-25-6-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-25-7-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-25-8-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-25-9-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-26-1-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-26-10-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-26-11-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-26-12-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-26-13-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-26-14-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-26-2-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-26-3-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-26-4-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-26-5-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-26-6-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-26-7-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-26-8-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-26-9-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-27-1-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-27-2-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-27-3-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-27-4-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-28-1-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-29-1-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-3-1-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-3-2-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-3-3-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-4-0-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-6-1-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-6-2-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-7-1-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-7-2-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-7-3-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-7-4-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-7-5-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-8-1-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-8-2-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-8-3-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-9-1-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-9-2-0.tex
%{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/tkzpreamblenamed.ltx
%{_texmfdistdir}/doc/latex/tkz-berge/README.md
%{_texmfdistdir}/doc/latex/tkz-berge/doc/latex/TKZdoc-berge-classic.tex
%{_texmfdistdir}/doc/latex/tkz-berge/doc/latex/TKZdoc-berge-macros-e.tex
%{_texmfdistdir}/doc/latex/tkz-berge/doc/latex/TKZdoc-berge-macros.tex
%{_texmfdistdir}/doc/latex/tkz-berge/doc/latex/TKZdoc-berge-main.tex
%{_texmfdistdir}/doc/latex/tkz-berge/doc/latex/TKZdoc-berge-style.tex
%{_texmfdistdir}/doc/latex/tkz-berge/doc/latex/TKZdoc-gr-installation.tex
%{_texmfdistdir}/doc/latex/tkz-berge/doc/tkz-berge-screen.pdf
%{_texmfdistdir}/doc/latex/tkz-berge/examples/Grid.pdf
%{_texmfdistdir}/doc/latex/tkz-berge/examples/gr-Circulant.pdf
%{_texmfdistdir}/doc/latex/tkz-berge/examples/gr-Complet-16.pdf
%{_texmfdistdir}/doc/latex/tkz-berge/examples/gr-edgeingraphmodloop.pdf
%{_texmfdistdir}/doc/latex/tkz-berge/examples/grCLadder.pdf
%{_texmfdistdir}/doc/latex/tkz-berge/examples/grDoubleMod.pdf
%{_texmfdistdir}/doc/latex/tkz-berge/examples/grExtraChords.pdf
%{_texmfdistdir}/doc/latex/tkz-berge/examples/grLadder.pdf
%{_texmfdistdir}/doc/latex/tkz-berge/examples/grSQCycle.pdf
%{_texmfdistdir}/doc/latex/tkz-berge/examples/grStar.pdf
%{_texmfdistdir}/doc/latex/tkz-berge/examples/grWheel.pdf
%{_texmfdistdir}/doc/latex/tkz-berge/examples/hypercube.pdf
%{_texmfdistdir}/doc/latex/tkz-berge/examples/hypercube_simple.pdf
%{_texmfdistdir}/doc/latex/tkz-berge/examples/hypercubed.pdf
%{_texmfdistdir}/doc/latex/tkz-berge/examples/latex/Grid.tex
%{_texmfdistdir}/doc/latex/tkz-berge/examples/latex/gr-Circulant.tex
%{_texmfdistdir}/doc/latex/tkz-berge/examples/latex/gr-Complet-16.tex
%{_texmfdistdir}/doc/latex/tkz-berge/examples/latex/gr-edgeingraphmodloop.tex
%{_texmfdistdir}/doc/latex/tkz-berge/examples/latex/grCLadder.tex
%{_texmfdistdir}/doc/latex/tkz-berge/examples/latex/grDoubleMod.tex
%{_texmfdistdir}/doc/latex/tkz-berge/examples/latex/grExtraChords.tex
%{_texmfdistdir}/doc/latex/tkz-berge/examples/latex/grLadder.tex
%{_texmfdistdir}/doc/latex/tkz-berge/examples/latex/grSQCycle.tex
%{_texmfdistdir}/doc/latex/tkz-berge/examples/latex/grStar.tex
%{_texmfdistdir}/doc/latex/tkz-berge/examples/latex/grWheel.tex
%{_texmfdistdir}/doc/latex/tkz-berge/examples/latex/hypercube_simple.tex
%{_texmfdistdir}/doc/latex/tkz-berge/examples/latex/hypercubed.tex

%files -n texlive-tkz-berge
%{_texmfdistdir}/tex/latex/tkz-berge/tkz-berge.sty

%package -n texlive-tkz-bernoulli
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1.3svn68780
Release:        0
License:        LPPL-1.0
Summary:        Draw Bernoulli trees with TikZ
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tkz-bernoulli-doc >= %{texlive_version}
Provides:       tex(tkz-bernoulli.sty)
Requires:       tex(pgffor.sty)
Requires:       tex(simplekv.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xintbinhex.sty)
Requires:       tex(xintexpr.sty)
Requires:       tex(xstring.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source142:      tkz-bernoulli.tar.xz
Source143:      tkz-bernoulli.doc.tar.xz

%description -n texlive-tkz-bernoulli
This is a package for representing Bernoulli trees with
PGF/TikZ.

%package -n texlive-tkz-bernoulli-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1.3svn68780
Release:        0
Summary:        Documentation for texlive-tkz-bernoulli
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tkz-bernoulli and texlive-alldocumentation)

%description -n texlive-tkz-bernoulli-doc
This package includes the documentation for texlive-tkz-bernoulli

%post -n texlive-tkz-bernoulli
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tkz-bernoulli
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tkz-bernoulli
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tkz-bernoulli-doc
%{_texmfdistdir}/doc/latex/tkz-bernoulli/README.md
%{_texmfdistdir}/doc/latex/tkz-bernoulli/tkz-bernoulli-doc.pdf
%{_texmfdistdir}/doc/latex/tkz-bernoulli/tkz-bernoulli-doc.tex

%files -n texlive-tkz-bernoulli
%{_texmfdistdir}/tex/latex/tkz-bernoulli/tkz-bernoulli.sty

%package -n texlive-tkz-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.45csvn68665
Release:        0
License:        LPPL-1.0
Summary:        Documentation macros for the TKZ series of packages
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tkz-doc-doc >= %{texlive_version}
Provides:       tex(tkz-doc.cfg)
Provides:       tex(tkz-doc.cls)
Requires:       tex(booktabs.sty)
Requires:       tex(cellspace.sty)
Requires:       tex(datetime.sty)
Requires:       tex(eso-pic.sty)
Requires:       tex(footmisc.sty)
Requires:       tex(framed.sty)
Requires:       tex(multicol.sty)
Requires:       tex(ragged2e.sty)
Requires:       tex(scrartcl.cls)
Requires:       tex(scrlayer-scrpage.sty)
Requires:       tex(tikz.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source144:      tkz-doc.tar.xz
Source145:      tkz-doc.doc.tar.xz

%description -n texlive-tkz-doc
This bundle offers a documentation class (tkz-doc) and a
package (tkzexample). These files are used in the documentation
of the author's packages tkz-base, tkz-euclide, tkz-fct,
tkz-linknodes, and tkz-tab.

%package -n texlive-tkz-doc-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.45csvn68665
Release:        0
Summary:        Documentation for texlive-tkz-doc
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tkz-doc and texlive-alldocumentation)

%description -n texlive-tkz-doc-doc
This package includes the documentation for texlive-tkz-doc

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tkz-doc-doc
%{_texmfdistdir}/doc/latex/tkz-doc/README.md
%{_texmfdistdir}/doc/latex/tkz-doc/tkz-doc.pdf
%{_texmfdistdir}/doc/latex/tkz-doc/tkz-doc.tex

%files -n texlive-tkz-doc
%{_texmfdistdir}/tex/latex/tkz-doc/tkz-doc.cfg
%{_texmfdistdir}/tex/latex/tkz-doc/tkz-doc.cls

%package -n texlive-tkz-elements
Version:        %{texlive_version}.%{texlive_noarch}.2.00csvn69715
Release:        0
License:        LPPL-1.0
Summary:        A Lua library for drawing Euclidean geometry with TikZ or tkz-euclide
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tkz-elements-doc >= %{texlive_version}
Provides:       tex(tkz-elements.sty)
Requires:       tex(luacode.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source146:      tkz-elements.tar.xz
Source147:      tkz-elements.doc.tar.xz

%description -n texlive-tkz-elements
This package provides a library written in Lua, allowing to
make all the necessary calculations to define the objects of a
Euclidean geometry figure. You need to compile with LuaLaTeX.
The definitions and calculations are only done with Lua. The
main possibility of programmation proposed is oriented "object
programming" with object classes like point, line, triangle,
circle and ellipse. For the moment, once the calculations are
done, it is tkz-euclide or TikZ which allows the drawings.

%package -n texlive-tkz-elements-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.00csvn69715
Release:        0
Summary:        Documentation for texlive-tkz-elements
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tkz-elements and texlive-alldocumentation)

%description -n texlive-tkz-elements-doc
This package includes the documentation for texlive-tkz-elements

%post -n texlive-tkz-elements
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tkz-elements
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tkz-elements
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tkz-elements-doc
%{_texmfdistdir}/doc/latex/tkz-elements/README.md
%{_texmfdistdir}/doc/latex/tkz-elements/TKZdoc-elements-classes-circle.tex
%{_texmfdistdir}/doc/latex/tkz-elements/TKZdoc-elements-classes-ellipse.tex
%{_texmfdistdir}/doc/latex/tkz-elements/TKZdoc-elements-classes-line.tex
%{_texmfdistdir}/doc/latex/tkz-elements/TKZdoc-elements-classes-misc.tex
%{_texmfdistdir}/doc/latex/tkz-elements/TKZdoc-elements-classes-parallelogram.tex
%{_texmfdistdir}/doc/latex/tkz-elements/TKZdoc-elements-classes-point.tex
%{_texmfdistdir}/doc/latex/tkz-elements/TKZdoc-elements-classes-quadrilateral.tex
%{_texmfdistdir}/doc/latex/tkz-elements/TKZdoc-elements-classes-rectangle.tex
%{_texmfdistdir}/doc/latex/tkz-elements/TKZdoc-elements-classes-regular.tex
%{_texmfdistdir}/doc/latex/tkz-elements/TKZdoc-elements-classes-square.tex
%{_texmfdistdir}/doc/latex/tkz-elements/TKZdoc-elements-classes-triangle.tex
%{_texmfdistdir}/doc/latex/tkz-elements/TKZdoc-elements-classes-vectors.tex
%{_texmfdistdir}/doc/latex/tkz-elements/TKZdoc-elements-classes.tex
%{_texmfdistdir}/doc/latex/tkz-elements/TKZdoc-elements-convention.tex
%{_texmfdistdir}/doc/latex/tkz-elements/TKZdoc-elements-examples.tex
%{_texmfdistdir}/doc/latex/tkz-elements/TKZdoc-elements-indepthstudy.tex
%{_texmfdistdir}/doc/latex/tkz-elements/TKZdoc-elements-intersection.tex
%{_texmfdistdir}/doc/latex/tkz-elements/TKZdoc-elements-inversion.tex
%{_texmfdistdir}/doc/latex/tkz-elements/TKZdoc-elements-main.tex
%{_texmfdistdir}/doc/latex/tkz-elements/TKZdoc-elements-organization.tex
%{_texmfdistdir}/doc/latex/tkz-elements/TKZdoc-elements-presentation.tex
%{_texmfdistdir}/doc/latex/tkz-elements/TKZdoc-elements-structure.tex
%{_texmfdistdir}/doc/latex/tkz-elements/TKZdoc-elements-tests.tex
%{_texmfdistdir}/doc/latex/tkz-elements/TKZdoc-elements-transferts.tex
%{_texmfdistdir}/doc/latex/tkz-elements/TKZdoc-elements-why.tex
%{_texmfdistdir}/doc/latex/tkz-elements/examples/tkz-elements-demo_1.pdf
%{_texmfdistdir}/doc/latex/tkz-elements/examples/tkz-elements-demo_1.tex
%{_texmfdistdir}/doc/latex/tkz-elements/examples/tkz-elements-demo_2.pdf
%{_texmfdistdir}/doc/latex/tkz-elements/examples/tkz-elements-demo_2.tex
%{_texmfdistdir}/doc/latex/tkz-elements/examples/tkz-elements-demo_3.pdf
%{_texmfdistdir}/doc/latex/tkz-elements/examples/tkz-elements-demo_3.tex
%{_texmfdistdir}/doc/latex/tkz-elements/examples/tkz-elements-demo_4.pdf
%{_texmfdistdir}/doc/latex/tkz-elements/examples/tkz-elements-demo_4.tex
%{_texmfdistdir}/doc/latex/tkz-elements/gold_preamble.lua
%{_texmfdistdir}/doc/latex/tkz-elements/sangaku.lua
%{_texmfdistdir}/doc/latex/tkz-elements/tkz-elements.pdf

%files -n texlive-tkz-elements
%{_texmfdistdir}/tex/latex/tkz-elements/tkz-elements.sty
%{_texmfdistdir}/tex/latex/tkz-elements/tkz_elements_circle.lua
%{_texmfdistdir}/tex/latex/tkz-elements/tkz_elements_class.lua
%{_texmfdistdir}/tex/latex/tkz-elements/tkz_elements_ellipse.lua
%{_texmfdistdir}/tex/latex/tkz-elements/tkz_elements_functions_circles.lua
%{_texmfdistdir}/tex/latex/tkz-elements/tkz_elements_functions_intersections.lua
%{_texmfdistdir}/tex/latex/tkz-elements/tkz_elements_functions_lines.lua
%{_texmfdistdir}/tex/latex/tkz-elements/tkz_elements_functions_maths.lua
%{_texmfdistdir}/tex/latex/tkz-elements/tkz_elements_functions_points.lua
%{_texmfdistdir}/tex/latex/tkz-elements/tkz_elements_functions_regular.lua
%{_texmfdistdir}/tex/latex/tkz-elements/tkz_elements_functions_triangles.lua
%{_texmfdistdir}/tex/latex/tkz-elements/tkz_elements_line.lua
%{_texmfdistdir}/tex/latex/tkz-elements/tkz_elements_main.lua
%{_texmfdistdir}/tex/latex/tkz-elements/tkz_elements_misc.lua
%{_texmfdistdir}/tex/latex/tkz-elements/tkz_elements_parallelogram.lua
%{_texmfdistdir}/tex/latex/tkz-elements/tkz_elements_point.lua
%{_texmfdistdir}/tex/latex/tkz-elements/tkz_elements_quadrilateral.lua
%{_texmfdistdir}/tex/latex/tkz-elements/tkz_elements_rectangle.lua
%{_texmfdistdir}/tex/latex/tkz-elements/tkz_elements_regular.lua
%{_texmfdistdir}/tex/latex/tkz-elements/tkz_elements_square.lua
%{_texmfdistdir}/tex/latex/tkz-elements/tkz_elements_triangle.lua
%{_texmfdistdir}/tex/latex/tkz-elements/tkz_elements_vector.lua

%package -n texlive-tkz-euclide
Version:        %{texlive_version}.%{texlive_noarch}.5.06csvn69702
Release:        0
License:        LPPL-1.0
Summary:        Tools for drawing Euclidean geometry
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tkz-euclide-doc >= %{texlive_version}
Provides:       tex(tkz-draw-eu-angles.tex)
Provides:       tex(tkz-draw-eu-circles.tex)
Provides:       tex(tkz-draw-eu-compass.tex)
Provides:       tex(tkz-draw-eu-ellipses.tex)
Provides:       tex(tkz-draw-eu-lines.tex)
Provides:       tex(tkz-draw-eu-points.tex)
Provides:       tex(tkz-draw-eu-polygons.tex)
Provides:       tex(tkz-draw-eu-protractor.tex)
Provides:       tex(tkz-draw-eu-sectors.tex)
Provides:       tex(tkz-draw-eu-show.tex)
Provides:       tex(tkz-euclide.cfg)
Provides:       tex(tkz-euclide.sty)
Provides:       tex(tkz-lib-eu-marks.tex)
Provides:       tex(tkz-lib-eu-shape.tex)
Provides:       tex(tkz-obj-eu-axesmin.tex)
Provides:       tex(tkz-obj-eu-circles-by.tex)
Provides:       tex(tkz-obj-eu-circles.tex)
Provides:       tex(tkz-obj-eu-grids.tex)
Provides:       tex(tkz-obj-eu-lines.tex)
Provides:       tex(tkz-obj-eu-lua-circles-by.tex)
Provides:       tex(tkz-obj-eu-lua-circles.tex)
Provides:       tex(tkz-obj-eu-lua-points-by.tex)
Provides:       tex(tkz-obj-eu-lua-points-spc.tex)
Provides:       tex(tkz-obj-eu-lua-points-with.tex)
Provides:       tex(tkz-obj-eu-lua-points.tex)
Provides:       tex(tkz-obj-eu-points-by.tex)
Provides:       tex(tkz-obj-eu-points-rnd.tex)
Provides:       tex(tkz-obj-eu-points-spc.tex)
Provides:       tex(tkz-obj-eu-points-with.tex)
Provides:       tex(tkz-obj-eu-points.tex)
Provides:       tex(tkz-obj-eu-polygons.tex)
Provides:       tex(tkz-obj-eu-triangles.tex)
Provides:       tex(tkz-tools-eu-BB.tex)
Provides:       tex(tkz-tools-eu-angles.tex)
Provides:       tex(tkz-tools-eu-base.tex)
Provides:       tex(tkz-tools-eu-colors.tex)
Provides:       tex(tkz-tools-eu-intersections.tex)
Provides:       tex(tkz-tools-eu-lua-angles.tex)
Provides:       tex(tkz-tools-eu-lua-base.tex)
Provides:       tex(tkz-tools-eu-lua-intersections.tex)
Provides:       tex(tkz-tools-eu-lua-math.tex)
Provides:       tex(tkz-tools-eu-math.tex)
Provides:       tex(tkz-tools-eu-modules.tex)
Provides:       tex(tkz-tools-eu-text.tex)
Provides:       tex(tkz-tools-eu-utilities.tex)
Requires:       tex(luacode.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xfp.sty)
Requires:       tex(xpatch.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source148:      tkz-euclide.tar.xz
Source149:      tkz-euclide.doc.tar.xz

%description -n texlive-tkz-euclide
The tkz-euclide package is a set of files designed to give math
teachers and students easy access to the programming of
Euclidean geometry with TikZ.

%package -n texlive-tkz-euclide-doc
Version:        %{texlive_version}.%{texlive_noarch}.5.06csvn69702
Release:        0
Summary:        Documentation for texlive-tkz-euclide
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tkz-euclide and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tkz-euclide-doc
%{_texmfdistdir}/doc/latex/tkz-euclide/README.md
%{_texmfdistdir}/doc/latex/tkz-euclide/TKZdoc-euclide-FAQ.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/TKZdoc-euclide-angles.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/TKZdoc-euclide-circleby.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/TKZdoc-euclide-circles.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/TKZdoc-euclide-clipping.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/TKZdoc-euclide-compass.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/TKZdoc-euclide-documentation.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/TKZdoc-euclide-drawing.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/TKZdoc-euclide-elements.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/TKZdoc-euclide-examples.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/TKZdoc-euclide-filling.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/TKZdoc-euclide-installation.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/TKZdoc-euclide-intersection.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/TKZdoc-euclide-labelling.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/TKZdoc-euclide-lines.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/TKZdoc-euclide-lua.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/TKZdoc-euclide-main.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/TKZdoc-euclide-marking.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/TKZdoc-euclide-news.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/TKZdoc-euclide-others.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/TKZdoc-euclide-pointby.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/TKZdoc-euclide-points.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/TKZdoc-euclide-pointsSpc.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/TKZdoc-euclide-pointwith.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/TKZdoc-euclide-polygons.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/TKZdoc-euclide-presentation.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/TKZdoc-euclide-rapporteur.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/TKZdoc-euclide-rnd.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/TKZdoc-euclide-show.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/TKZdoc-euclide-styles.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/TKZdoc-euclide-tools.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/TKZdoc-euclide-triangles.tex
%{_texmfdistdir}/doc/latex/tkz-euclide/tkz-euclide.pdf

%files -n texlive-tkz-euclide
%{_texmfdistdir}/tex/latex/tkz-euclide/tkz-draw-eu-angles.tex
%{_texmfdistdir}/tex/latex/tkz-euclide/tkz-draw-eu-circles.tex
%{_texmfdistdir}/tex/latex/tkz-euclide/tkz-draw-eu-compass.tex
%{_texmfdistdir}/tex/latex/tkz-euclide/tkz-draw-eu-ellipses.tex
%{_texmfdistdir}/tex/latex/tkz-euclide/tkz-draw-eu-lines.tex
%{_texmfdistdir}/tex/latex/tkz-euclide/tkz-draw-eu-points.tex
%{_texmfdistdir}/tex/latex/tkz-euclide/tkz-draw-eu-polygons.tex
%{_texmfdistdir}/tex/latex/tkz-euclide/tkz-draw-eu-protractor.tex
%{_texmfdistdir}/tex/latex/tkz-euclide/tkz-draw-eu-sectors.tex
%{_texmfdistdir}/tex/latex/tkz-euclide/tkz-draw-eu-show.tex
%{_texmfdistdir}/tex/latex/tkz-euclide/tkz-euclide.cfg
%{_texmfdistdir}/tex/latex/tkz-euclide/tkz-euclide.sty
%{_texmfdistdir}/tex/latex/tkz-euclide/tkz-lib-eu-marks.tex
%{_texmfdistdir}/tex/latex/tkz-euclide/tkz-lib-eu-shape.tex
%{_texmfdistdir}/tex/latex/tkz-euclide/tkz-obj-eu-axesmin.tex
%{_texmfdistdir}/tex/latex/tkz-euclide/tkz-obj-eu-circles-by.tex
%{_texmfdistdir}/tex/latex/tkz-euclide/tkz-obj-eu-circles.tex
%{_texmfdistdir}/tex/latex/tkz-euclide/tkz-obj-eu-grids.tex
%{_texmfdistdir}/tex/latex/tkz-euclide/tkz-obj-eu-lines.tex
%{_texmfdistdir}/tex/latex/tkz-euclide/tkz-obj-eu-lua-circles-by.tex
%{_texmfdistdir}/tex/latex/tkz-euclide/tkz-obj-eu-lua-circles.tex
%{_texmfdistdir}/tex/latex/tkz-euclide/tkz-obj-eu-lua-points-by.tex
%{_texmfdistdir}/tex/latex/tkz-euclide/tkz-obj-eu-lua-points-spc.tex
%{_texmfdistdir}/tex/latex/tkz-euclide/tkz-obj-eu-lua-points-with.tex
%{_texmfdistdir}/tex/latex/tkz-euclide/tkz-obj-eu-lua-points.tex
%{_texmfdistdir}/tex/latex/tkz-euclide/tkz-obj-eu-points-by.tex
%{_texmfdistdir}/tex/latex/tkz-euclide/tkz-obj-eu-points-rnd.tex
%{_texmfdistdir}/tex/latex/tkz-euclide/tkz-obj-eu-points-spc.tex
%{_texmfdistdir}/tex/latex/tkz-euclide/tkz-obj-eu-points-with.tex
%{_texmfdistdir}/tex/latex/tkz-euclide/tkz-obj-eu-points.tex
%{_texmfdistdir}/tex/latex/tkz-euclide/tkz-obj-eu-polygons.tex
%{_texmfdistdir}/tex/latex/tkz-euclide/tkz-obj-eu-triangles.tex
%{_texmfdistdir}/tex/latex/tkz-euclide/tkz-tools-eu-BB.tex
%{_texmfdistdir}/tex/latex/tkz-euclide/tkz-tools-eu-angles.tex
%{_texmfdistdir}/tex/latex/tkz-euclide/tkz-tools-eu-base.tex
%{_texmfdistdir}/tex/latex/tkz-euclide/tkz-tools-eu-colors.tex
%{_texmfdistdir}/tex/latex/tkz-euclide/tkz-tools-eu-intersections.tex
%{_texmfdistdir}/tex/latex/tkz-euclide/tkz-tools-eu-lua-angles.tex
%{_texmfdistdir}/tex/latex/tkz-euclide/tkz-tools-eu-lua-base.tex
%{_texmfdistdir}/tex/latex/tkz-euclide/tkz-tools-eu-lua-intersections.tex
%{_texmfdistdir}/tex/latex/tkz-euclide/tkz-tools-eu-lua-math.tex
%{_texmfdistdir}/tex/latex/tkz-euclide/tkz-tools-eu-math.tex
%{_texmfdistdir}/tex/latex/tkz-euclide/tkz-tools-eu-modules.tex
%{_texmfdistdir}/tex/latex/tkz-euclide/tkz-tools-eu-text.tex
%{_texmfdistdir}/tex/latex/tkz-euclide/tkz-tools-eu-utilities.tex

%package -n texlive-tkz-fct
Version:        %{texlive_version}.%{texlive_noarch}.1.7csvn61949
Release:        0
License:        LPPL-1.0
Summary:        Tools for drawing graphs of functions
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tkz-fct-doc >= %{texlive_version}
Provides:       tex(tkz-fct.sty)
Requires:       tex(fp.sty)
Requires:       tex(tkz-base.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source150:      tkz-fct.tar.xz
Source151:      tkz-fct.doc.tar.xz

%description -n texlive-tkz-fct
The tkz-fct package is designed to give math teachers (and
students) easy access to programming graphs of functions with
TikZ and gnuplot.

%package -n texlive-tkz-fct-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.7csvn61949
Release:        0
Summary:        Documentation for texlive-tkz-fct
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tkz-fct and texlive-alldocumentation)
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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tkz-fct-doc
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
%{_texmfdistdir}/doc/latex/tkz-fct/TKZdoc-fct-installation.tex
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
%{_texmfdistdir}/doc/latex/tkz-fct/tkz-fct.pdf

%files -n texlive-tkz-fct
%{_texmfdistdir}/tex/latex/tkz-fct/tkz-fct.sty

%package -n texlive-tkz-graph
Version:        %{texlive_version}.%{texlive_noarch}.2.0svn57484
Release:        0
License:        LPPL-1.0
Summary:        Draw graph-theory graphs
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tkz-graph-doc >= %{texlive_version}
Provides:       tex(tkz-graph.sty)
Requires:       tex(etex.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source152:      tkz-graph.tar.xz
Source153:      tkz-graph.doc.tar.xz

%description -n texlive-tkz-graph
The package is designed to create graph diagrams as simply as
possible, using TikZ.

%package -n texlive-tkz-graph-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.0svn57484
Release:        0
Summary:        Documentation for texlive-tkz-graph
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tkz-graph and texlive-alldocumentation)
Provides:       locale(texlive-tkz-graph-doc:fr)

%description -n texlive-tkz-graph-doc
This package includes the documentation for texlive-tkz-graph

%post -n texlive-tkz-graph
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tkz-graph
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tkz-graph
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tkz-graph-doc
%{_texmfdistdir}/doc/latex/tkz-graph/README.md
%{_texmfdistdir}/doc/latex/tkz-graph/doc/latex/TKZdoc-gr-Dijkstra.tex
%{_texmfdistdir}/doc/latex/tkz-graph/doc/latex/TKZdoc-gr-Welsh.tex
%{_texmfdistdir}/doc/latex/tkz-graph/doc/latex/TKZdoc-gr-annales.tex
%{_texmfdistdir}/doc/latex/tkz-graph/doc/latex/TKZdoc-gr-couverture.tex
%{_texmfdistdir}/doc/latex/tkz-graph/doc/latex/TKZdoc-gr-edge.tex
%{_texmfdistdir}/doc/latex/tkz-graph/doc/latex/TKZdoc-gr-label.tex
%{_texmfdistdir}/doc/latex/tkz-graph/doc/latex/TKZdoc-gr-main.tex
%{_texmfdistdir}/doc/latex/tkz-graph/doc/latex/TKZdoc-gr-presentation.tex
%{_texmfdistdir}/doc/latex/tkz-graph/doc/latex/TKZdoc-gr-prob.tex
%{_texmfdistdir}/doc/latex/tkz-graph/doc/latex/TKZdoc-gr-style.tex
%{_texmfdistdir}/doc/latex/tkz-graph/doc/latex/TKZdoc-gr-vertex.tex
%{_texmfdistdir}/doc/latex/tkz-graph/doc/latex/TKZdoc-gr-vertices.tex
%{_texmfdistdir}/doc/latex/tkz-graph/test-graph.pdf
%{_texmfdistdir}/doc/latex/tkz-graph/test-graph.tex
%{_texmfdistdir}/doc/latex/tkz-graph/tkz-graph-screen.pdf

%files -n texlive-tkz-graph
%{_texmfdistdir}/tex/latex/tkz-graph/tkz-graph.sty

%package -n texlive-tkz-orm
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1.4svn61719
Release:        0
License:        GPL-2.0-or-later
Summary:        Create Object-Role Model (ORM) diagrams
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tkz-orm-doc >= %{texlive_version}
Provides:       tex(tkz-orm.sty)
Requires:       tex(tikz.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source154:      tkz-orm.tar.xz
Source155:      tkz-orm.doc.tar.xz

%description -n texlive-tkz-orm
The package provides styles for drawing Object-Role Model (ORM)
diagrams in TeX based on the PGF and TikZ picture environment.

%package -n texlive-tkz-orm-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1.4svn61719
Release:        0
Summary:        Documentation for texlive-tkz-orm
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tkz-orm and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tkz-orm-doc
%{_texmfdistdir}/doc/latex/tkz-orm/LICENSE
%{_texmfdistdir}/doc/latex/tkz-orm/Makefile
%{_texmfdistdir}/doc/latex/tkz-orm/README
%{_texmfdistdir}/doc/latex/tkz-orm/pgfmanualstyle.sty
%{_texmfdistdir}/doc/latex/tkz-orm/tkz-orm.bib
%{_texmfdistdir}/doc/latex/tkz-orm/tkz-orm.pdf
%{_texmfdistdir}/doc/latex/tkz-orm/tkz-orm.tex

%files -n texlive-tkz-orm
%{_texmfdistdir}/tex/latex/tkz-orm/tkz-orm.sty

%package -n texlive-tkz-tab
Version:        %{texlive_version}.%{texlive_noarch}.2.12csvn66115
Release:        0
License:        LPPL-1.0
Summary:        Tables of signs and variations using PGF/TikZ
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tkz-tab-doc >= %{texlive_version}
Provides:       tex(tkz-tab.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source156:      tkz-tab.tar.xz
Source157:      tkz-tab.doc.tar.xz

%description -n texlive-tkz-tab
The package provides comprehensive facilities for preparing
lists of signs and variations, using PGF. The package
documentation requires the tkz-doc bundle. This package has
been taken temporarily out of circulation to give the author
time to investigate some problems.

%package -n texlive-tkz-tab-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.12csvn66115
Release:        0
Summary:        Documentation for texlive-tkz-tab
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tkz-tab and texlive-alldocumentation)
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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tkz-tab-doc
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
%{_texmfdistdir}/tex/latex/tkz-tab/tkz-tab.sty

%package -n texlive-tkzexample
Version:        %{texlive_version}.%{texlive_noarch}.1.45csvn63908
Release:        0
License:        LPPL-1.0
Summary:        Package for the documentation of all tkz-* packages
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tkzexample-doc >= %{texlive_version}
Provides:       tex(tkzexample.sty)
Requires:       tex(calc.sty)
Requires:       tex(fancyvrb.sty)
Requires:       tex(mdframed.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source158:      tkzexample.tar.xz
Source159:      tkzexample.doc.tar.xz

%description -n texlive-tkzexample
This package is needed to compile the documentation of all
tkz-* packages (like tkz-euclide).

%package -n texlive-tkzexample-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.45csvn63908
Release:        0
Summary:        Documentation for texlive-tkzexample
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tkzexample and texlive-alldocumentation)

%description -n texlive-tkzexample-doc
This package includes the documentation for texlive-tkzexample

%post -n texlive-tkzexample
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tkzexample
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tkzexample
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tkzexample-doc
%{_texmfdistdir}/doc/latex/tkzexample/README.md
%{_texmfdistdir}/doc/latex/tkzexample/tkzexample.pdf
%{_texmfdistdir}/doc/latex/tkzexample/tkzexample.tex

%files -n texlive-tkzexample
%{_texmfdistdir}/tex/latex/tkzexample/tkzexample.sty

%package -n texlive-tlc-article
Version:        %{texlive_version}.%{texlive_noarch}.1.0.17svn51431
Release:        0
License:        BSD-3-Clause
Summary:        A LaTeX document class for formal documents
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tlc-article-doc >= %{texlive_version}
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
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source160:      tlc-article.tar.xz
Source161:      tlc-article.doc.tar.xz

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
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tlc-article and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tlc-article-doc
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
%{_texmfdistdir}/tex/latex/tlc-article/tlc-article.cls

%package -n texlive-tlc2
Version:        %{texlive_version}.%{texlive_noarch}.svn26096
Release:        0
License:        LPPL-1.0
Summary:        Examples from "The LaTeX Companion", second edition
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source162:      tlc2.doc.tar.xz

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tlc2
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

%package -n texlive-tlc3-examples
Version:        %{texlive_version}.%{texlive_noarch}.svn65496
Release:        0
License:        LPPL-1.0
Summary:        All examples from "The LaTeX Companion", third edition
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source163:      tlc3-examples.doc.tar.xz

%description -n texlive-tlc3-examples
The PDFs (as used with spotcolor and trimming) and sources for
all examples from the third edition (Parts I+II), together with
necessary supporting files. The edition is published by
Addison-Wesley, 2023, ISBN-13: 978-0-13-816648-9, ISBN-10:
0-13-816648-X (bundle of Part I & II).

%post -n texlive-tlc3-examples
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tlc3-examples
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tlc3-examples
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tlc3-examples
%{_texmfdistdir}/doc/latex/tlc3-examples/README.TEXLIVE
%{_texmfdistdir}/doc/latex/tlc3-examples/README.md
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/1-3-1.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/1-3-2.ltx2
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/1-3-3.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/1-3-4.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/1-3-5.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/1-3-6.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/10-1-1.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/10-1-2.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/10-10-1.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/10-10-2.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/10-10-3.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/10-10-4.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/10-10-5.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/10-10-6.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/10-11-1.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/10-12-1.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/10-12-2.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/10-12-3.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/10-13-1.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/10-13-10.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/10-13-11.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/10-13-12.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/10-13-13.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/10-13-14.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/10-13-15.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/10-13-16.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/10-13-2.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/10-13-3.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/10-13-4.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/10-13-5.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/10-13-6.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/10-13-7.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/10-13-8.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/10-13-9.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/10-2-1.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/10-2-2.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/10-2-3.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/10-2-4.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/10-2-5.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/10-5-1.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/10-5-2.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/10-8-1.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/10-8-2.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/10-9-1.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/10-9-2.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/10-9-3.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/10-9-4.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-2-1.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-2-10.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-2-11.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-2-12.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-2-13.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-2-14.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-2-15.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-2-16.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-2-17.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-2-18.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-2-19.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-2-2.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-2-20.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-2-21.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-2-22.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-2-23.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-2-24.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-2-25.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-2-26.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-2-27.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-2-28.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-2-29.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-2-3.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-2-30.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-2-31.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-2-32.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-2-33.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-2-34.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-2-35.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-2-36.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-2-37.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-2-38.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-2-39.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-2-4.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-2-40.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-2-5.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-2-6.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-2-7.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-2-8.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-2-9.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-3-1.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-3-10.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-3-11.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-3-12.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-3-13.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-3-14.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-3-15.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-3-2.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-3-3.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-3-4.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-3-5.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-3-6.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-3-7.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-3-8.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-3-9.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-4-1.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-4-10.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-4-11.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-4-12.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-4-13.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-4-14.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-4-15.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-4-16.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-4-17.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-4-18.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-4-19.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-4-2.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-4-20.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-4-21.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-4-22.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-4-23.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-4-24.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-4-25.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-4-26.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-4-27.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-4-28.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-4-29.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-4-3.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-4-30.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-4-31.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-4-32.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-4-33.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-4-34.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-4-35.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-4-36.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-4-37.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-4-38.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-4-39.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-4-4.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-4-40.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-4-41.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-4-42.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-4-5.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-4-6.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-4-7.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-4-8.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-4-9.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-5-1.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-5-10.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-5-11.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-5-12.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-5-13.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-5-14.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-5-15.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-5-16.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-5-17.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-5-18.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-5-19.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-5-2.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-5-3.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-5-4.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-5-5.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-5-6.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-5-7.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-5-8.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-5-9.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-6-1.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-6-2.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-6-3.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-6-4.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-7-1.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-7-10.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-7-11.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-7-12.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-7-13.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-7-14.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-7-15.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-7-16.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-7-17.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-7-18.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-7-19.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-7-2.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-7-20.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-7-21.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-7-22.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-7-23.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-7-24.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-7-25.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-7-3.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-7-4.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-7-5.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-7-6.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-7-7.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-7-8.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-7-9.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-8-1.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-8-10.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-8-11.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-8-2.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-8-3.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-8-4.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-8-5.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-8-6.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-8-7.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-8-8.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/11-8-9.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-1-1.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-1-10.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-1-11.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-1-12.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-1-13.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-1-2.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-1-3.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-1-4.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-1-5.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-1-6.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-1-7.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-1-8.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-1-9.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-1-fig.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-10-fig.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-11-fig.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-12-fig.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-13-fig.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-14-fig.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-15-fig.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-16-fig.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-17-fig.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-18-fig.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-19-fig.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-2-1.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-2-2.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-2-3.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-2-4.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-2-5.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-2-6.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-2-fig.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-20-fig.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-21-fig.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-22-fig.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-23-fig.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-24-fig.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-25-fig.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-26-fig.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-27-fig.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-28-fig.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-29-fig.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-3-1.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-3-10.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-3-11.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-3-12.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-3-13.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-3-14.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-3-15.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-3-16.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-3-17.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-3-18.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-3-19.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-3-2.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-3-20.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-3-21.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-3-22.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-3-23.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-3-24.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-3-25.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-3-26.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-3-27.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-3-28.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-3-29.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-3-3.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-3-30.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-3-31.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-3-32.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-3-33.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-3-34.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-3-35.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-3-36.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-3-37.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-3-38.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-3-39.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-3-4.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-3-40.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-3-5.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-3-6.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-3-7.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-3-8.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-3-9.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-3-fig.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-30-fig.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-31-fig.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-32-fig.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-33-fig.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-34-fig.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-35-fig.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-36-fig.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-37-fig.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-38-fig.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-39-fig.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-4-1.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-4-2.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-4-3.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-4-4.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-4-5.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-4-6.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-4-fig.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-40-fig.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-41-fig.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-42-fig.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-43-fig.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-44-fig.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-45-fig.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-46-fig.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-47-fig.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-48-fig.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-49-fig.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-5-fig.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-50-fig.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-51-fig.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-52-fig.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-6-fig.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-7-fig.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-8-fig.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/12-9-fig.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/13-2-1.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/13-2-2.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/13-2-3.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/13-2-4.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/13-2-5.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/13-2-6.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/13-2-7.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/13-3-1.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/13-3-10.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/13-3-11.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/13-3-12.ltx2
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/13-3-13.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/13-3-14.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/13-3-15.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/13-3-16.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/13-3-17.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/13-3-18.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/13-3-19.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/13-3-2.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/13-3-20.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/13-3-21.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/13-3-22.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/13-3-23.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/13-3-24.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/13-3-25.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/13-3-26.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/13-3-27.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/13-3-28.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/13-3-29.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/13-3-3.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/13-3-30.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/13-3-4.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/13-3-5.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/13-3-6.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/13-3-7.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/13-3-8.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/13-3-9.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/13-4-1.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/13-4-2.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/13-4-3.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/13-5-1.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/13-5-2.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/13-5-3.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/13-6-1.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-1-1.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-3-1.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-3-2.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-3-3.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-3-4.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-3-5.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-6-1.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-6-2.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-1.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-10.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-100.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-101.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-102.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-103.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-104.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-105.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-106.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-107.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-108.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-109.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-11.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-110.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-111.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-112.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-113.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-114.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-115.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-116.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-117.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-118.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-119.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-12.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-120.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-121.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-122.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-123.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-124.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-125.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-126.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-127.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-128.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-129.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-13.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-130.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-131.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-132.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-133.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-134.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-135.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-136.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-137.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-138.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-139.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-14.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-140.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-141.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-15.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-16.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-17.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-18.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-19.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-2.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-20.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-21.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-22.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-23.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-24.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-25.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-26.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-27.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-28.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-29.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-3.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-30.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-31.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-32.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-33.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-34.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-35.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-36.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-37.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-38.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-39.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-4.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-40.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-41.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-42.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-43.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-44.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-45.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-46.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-47.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-48.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-49.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-5.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-50.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-51.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-52.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-53.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-54.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-55.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-56.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-57.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-58.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-59.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-6.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-60.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-61.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-62.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-63.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-64.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-65.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-66.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-67.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-68.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-69.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-7.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-70.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-71.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-72.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-73.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-74.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-75.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-76.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-77.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-78.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-79.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-8.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-80.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-81.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-82.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-83.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-84.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-85.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-86.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-87.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-88.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-89.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-9.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-90.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-91.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-92.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-93.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-94.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-95.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-96.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-97.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-98.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/15-7-99.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-1-1.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-1-2.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-1-3.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-1-4.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-2-1.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-2-10.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-2-11.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-2-12.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-2-13.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-2-14.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-2-15.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-2-16.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-2-17.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-2-18.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-2-19.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-2-2.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-2-20.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-2-21.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-2-22.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-2-23.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-2-24.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-2-25.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-2-26.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-2-27.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-2-28.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-2-29.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-2-3.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-2-30.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-2-4.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-2-5.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-2-6.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-2-7.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-2-8.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-2-9.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-3-1.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-3-10.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-3-11.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-3-12.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-3-13.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-3-14.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-3-15.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-3-16.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-3-17.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-3-18.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-3-19.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-3-2.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-3-20.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-3-21.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-3-22.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-3-23.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-3-24.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-3-25.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-3-26.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-3-27.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-3-28.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-3-29.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-3-3.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-3-30.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-3-31.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-3-32.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-3-33.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-3-4.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-3-5.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-3-6.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-3-7.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-3-8.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-3-9.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-4-1.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-4-10.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-4-2.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-4-3.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-4-4.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-4-5.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-4-6.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-4-7.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-4-8.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-4-9.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-5-1.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-5-10.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-5-11.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-5-12.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-5-13.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-5-14.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-5-15.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-5-16.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-5-17.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-5-18.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-5-19.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-5-2.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-5-20.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-5-21.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-5-22.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-5-23.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-5-24.ltx2
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-5-25.ltx2
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-5-26.ltx2
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-5-27.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-5-28.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-5-29.ltx2
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-5-3.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-5-30.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-5-31.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-5-32.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-5-33.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-5-34.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-5-35.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-5-36.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-5-37.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-5-38.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-5-39.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-5-4.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-5-40.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-5-41.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-5-42.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-5-43.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-5-44.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-5-45.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-5-46.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-5-47.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-5-48.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-5-49.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-5-5.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-5-50.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-5-51.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-5-52.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-5-53.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-5-54.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-5-6.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-5-7.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-5-8.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-5-9.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-6-1.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-6-2.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-6-3.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-6-4.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-6-5.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-6-6.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-6-7.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-6-8.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-7-1.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-7-10.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-7-11.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-7-12.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-7-13.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-7-14.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-7-15.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-7-16.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-7-17.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-7-18.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-7-19.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-7-2.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-7-20.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-7-21.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-7-22.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-7-23.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-7-24.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-7-25.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-7-26.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-7-27.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-7-28.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-7-29.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-7-3.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-7-30.ltx2
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-7-31.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-7-32.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-7-33.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-7-34.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-7-35.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-7-36.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-7-37.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-7-38.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-7-39.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-7-4.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-7-40.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-7-41.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-7-42.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-7-5.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-7-6.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-7-7.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-7-8.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-7-9.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-8-1.ltx2
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-8-10.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-8-11.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-8-2.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-8-3.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-8-4.ltx2
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-8-5.ltx2
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-8-6.ltx2
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-8-7.ltx2
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-8-8.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/16-8-9.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/17-4-1.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/17-4-2.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/2-1-1.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/2-1-2.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/2-1-3.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/2-2-1.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/2-2-10.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/2-2-11.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/2-2-12.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/2-2-13.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/2-2-14.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/2-2-15.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/2-2-16.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/2-2-17.ltx2
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/2-2-18.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/2-2-19.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/2-2-2.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/2-2-20.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/2-2-21.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/2-2-22.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/2-2-3.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/2-2-4.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/2-2-5.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/2-2-6.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/2-2-7.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/2-2-8.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/2-2-9.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/2-3-1.ltx2
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/2-3-10.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/2-3-11.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/2-3-12.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/2-3-13.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/2-3-14.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/2-3-15.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/2-3-16.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/2-3-2.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/2-3-3.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/2-3-4.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/2-3-5.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/2-3-6.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/2-3-7.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/2-3-8.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/2-3-9.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/2-4-1.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/2-4-10.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/2-4-11.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/2-4-12.ltx2
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/2-4-13.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/2-4-14.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/2-4-15.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/2-4-16.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/2-4-17.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/2-4-18.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/2-4-19.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/2-4-2.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/2-4-20.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/2-4-21.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/2-4-3.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/2-4-4.ltx2
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/2-4-5.ltx2
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/2-4-6.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/2-4-7.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/2-4-8.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/2-4-9.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-1-1.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-1-10.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-1-11.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-1-12.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-1-13.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-1-14.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-1-15.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-1-16.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-1-17.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-1-18.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-1-19.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-1-2.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-1-20.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-1-21.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-1-22.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-1-23.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-1-3.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-1-4.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-1-5.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-1-6.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-1-7.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-1-8.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-1-9.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-2-1.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-2-2.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-2-3.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-2-4.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-2-5.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-2-6.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-2-7.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-2-8.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-2-9.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-3-1.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-3-10.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-3-11.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-3-12.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-3-13.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-3-14.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-3-15.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-3-16.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-3-17.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-3-18.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-3-19.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-3-2.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-3-20.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-3-21.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-3-22.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-3-23.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-3-24.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-3-25.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-3-26.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-3-27.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-3-28.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-3-29.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-3-3.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-3-30.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-3-31.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-3-32.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-3-33.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-3-34.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-3-35.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-3-36.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-3-37.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-3-38.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-3-39.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-3-4.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-3-5.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-3-6.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-3-7.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-3-8.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-3-9.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-4-1.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-4-10.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-4-11.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-4-12.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-4-13.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-4-14.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-4-15.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-4-16.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-4-17.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-4-18.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-4-19.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-4-2.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-4-20.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-4-21.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-4-22.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-4-23.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-4-24.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-4-25.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-4-26.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-4-27.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-4-28.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-4-29.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-4-3.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-4-30.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-4-31.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-4-32.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-4-33.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-4-34.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-4-35.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-4-36.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-4-37.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-4-38.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-4-39.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-4-4.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-4-40.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-4-41.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-4-42.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-4-43.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-4-44.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-4-45.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-4-46.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-4-47.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-4-5.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-4-6.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-4-7.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-4-8.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-4-9.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-5-1.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-5-10.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-5-11.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-5-12.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-5-13.ltx2
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-5-14.ltx2
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-5-15.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-5-16.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-5-17.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-5-18.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-5-19.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-5-2.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-5-20.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-5-21.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-5-22.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-5-23.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-5-24.ltx2
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-5-25.ltx2
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-5-26.ltx2
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-5-27.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-5-28.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-5-29.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-5-3.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-5-30.ltx2
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-5-31.ltx2
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-5-32.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-5-33.ltx2
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-5-34.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-5-35.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-5-36.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-5-37.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-5-38.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-5-39.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-5-4.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-5-40.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-5-41.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-5-42.ltx2
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-5-43.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-5-44.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-5-45.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-5-46.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-5-47.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-5-48.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-5-5.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-5-6.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-5-7.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-5-8.ltx2
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-5-9.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-6-1.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-6-10.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-6-11.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-6-12.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-6-13.ltx2
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-6-14.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-6-15.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-6-16.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-6-17.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-6-18.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-6-19.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-6-2.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-6-3.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-6-4.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-6-5.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-6-6.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-6-7.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-6-8.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/3-6-9.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-1-1.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-1-10.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-1-11.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-1-12.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-1-13.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-1-14.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-1-15.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-1-16.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-1-17.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-1-18.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-1-19.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-1-2.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-1-20.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-1-21.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-1-22.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-1-23.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-1-24.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-1-25.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-1-26.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-1-27.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-1-28.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-1-29.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-1-3.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-1-30.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-1-31.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-1-32.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-1-33.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-1-34.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-1-35.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-1-36.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-1-37.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-1-38.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-1-39.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-1-4.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-1-40.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-1-41.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-1-42.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-1-43.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-1-44.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-1-45.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-1-46.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-1-47.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-1-48.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-1-49.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-1-5.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-1-50.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-1-51.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-1-52.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-1-53.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-1-54.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-1-55.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-1-6.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-1-7.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-1-8.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-1-9.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-2-1.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-2-10.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-2-11.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-2-12.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-2-13.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-2-14.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-2-15.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-2-16.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-2-17.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-2-18.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-2-19.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-2-2.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-2-20.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-2-21.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-2-22.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-2-23.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-2-24.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-2-25.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-2-26.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-2-27.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-2-28.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-2-29.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-2-3.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-2-30.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-2-31.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-2-32.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-2-33.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-2-34.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-2-35.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-2-36.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-2-37.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-2-38.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-2-39.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-2-4.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-2-40.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-2-41.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-2-42.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-2-43.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-2-44.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-2-45.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-2-46.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-2-47.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-2-48.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-2-49.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-2-5.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-2-50.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-2-51.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-2-52.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-2-53.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-2-54.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-2-55.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-2-56.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-2-57.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-2-58.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-2-59.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-2-6.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-2-60.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-2-61.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-2-7.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-2-8.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-2-9.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-3-1.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-3-10.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-3-11.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-3-12.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-3-13.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-3-14.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-3-15.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-3-16.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-3-17.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-3-18.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-3-19.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-3-2.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-3-20.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-3-21.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-3-22.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-3-23.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-3-24.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-3-25.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-3-26.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-3-27.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-3-28.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-3-29.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-3-3.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-3-30.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-3-31.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-3-32.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-3-33.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-3-34.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-3-35.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-3-36.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-3-4.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-3-5.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-3-6.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-3-7.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-3-8.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-3-9.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-4-1.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-4-2.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-4-3.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-4-4.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/4-4-5.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/5-1-1.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/5-2-1.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/5-2-10.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/5-2-2.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/5-2-3.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/5-2-4.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/5-2-5.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/5-2-6.ltx2
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/5-2-7.ltx2
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/5-2-8.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/5-2-9.ltx2
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/5-3-1.ltx2
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/5-3-2.ltx2
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/5-3-3.ltx2
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/5-3-4.ltx2
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/5-3-5.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/5-4-1.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/5-4-10.ltx2
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/5-4-11.ltx2
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/5-4-12.ltx2
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/5-4-13.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/5-4-14.ltx2
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/5-4-15.ltx2
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/5-4-16.ltx2
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/5-4-17.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/5-4-2.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/5-4-3.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/5-4-4.ltx2
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/5-4-5.ltx2
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/5-4-6.ltx2
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/5-4-7.ltx2
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/5-4-8.ltx2
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/5-4-9.ltx2
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/5-5-1.ltx2
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/5-5-2.ltx2
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/5-5-3.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/5-5-4.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/5-5-5.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/5-6-1.ltx2
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/5-6-2.ltx2
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/5-6-3.ltx2
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/5-6-4.ltx2
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/5-6-5.ltx2
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/5-6-6.ltx2
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/5-6-7.ltx2
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/5-6-8.ltx2
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/5-6-9.ltx2
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-1-1.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-1-2.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-1-3.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-1-4.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-1-5.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-1-6.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-2-1.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-2-10.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-2-11.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-2-12.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-2-13.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-2-14.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-2-15.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-2-16.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-2-17.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-2-18.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-2-2.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-2-3.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-2-4.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-2-5.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-2-6.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-2-7.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-2-8.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-2-9.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-3-1.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-3-10.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-3-11.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-3-2.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-3-3.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-3-4.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-3-5.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-3-6.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-3-7.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-3-8.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-3-9.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-4-1.ltx2
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-4-2.ltx2
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-4-3.ltx2
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-4-4.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-4-5.ltx2
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-4-6.ltx2
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-4-7.ltx2
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-4-8.ltx2
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-5-1.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-5-2.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-6-1.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-6-10.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-6-2.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-6-3.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-6-4.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-6-5.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-6-6.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-6-7.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-6-8.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-6-9.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-7-1.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-7-10.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-7-11.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-7-12.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-7-13.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-7-14.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-7-15.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-7-16.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-7-17.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-7-18.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-7-19.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-7-2.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-7-20.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-7-21.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-7-22.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-7-3.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-7-4.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-7-5.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-7-6.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-7-7.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-7-8.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-7-9.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-8-1.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-8-2.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-9-1.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-9-2.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-9-3.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-9-4.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-9-5.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-9-6.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-9-7.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-9-8.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/6-9-9.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/7-3-1.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/7-3-2.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/7-3-3.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/7-3-4.ltx2
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/7-3-5.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/7-3-6.ltx2
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/7-3-7.ltx2
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/7-3-8.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/7-3-9.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/7-4-1.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/7-4-10.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/7-4-11.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/7-4-12.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/7-4-13.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/7-4-14.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/7-4-15.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/7-4-16.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/7-4-17.ltx2
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/7-4-2.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/7-4-3.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/7-4-4.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/7-4-5.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/7-4-6.ltx2
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/7-4-7.ltx2
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/7-4-8.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/7-4-9.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/7-5-1.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/7-5-10.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/7-5-11.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/7-5-12.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/7-5-13.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/7-5-14.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/7-5-15.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/7-5-16.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/7-5-2.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/7-5-3.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/7-5-4.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/7-5-5.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/7-5-6.ltx2
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/7-5-7.ltx2
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/7-5-8.ltx2
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/7-5-9.ltx2
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-1-1.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-1-10.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-1-11.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-1-12.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-1-13.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-1-14.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-1-15.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-1-2.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-1-3.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-1-4.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-1-5.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-1-6.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-1-7.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-1-8.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-1-9.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-2-1.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-2-10.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-2-11.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-2-12.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-2-13.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-2-14.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-2-15.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-2-16.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-2-17.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-2-18.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-2-19.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-2-2.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-2-20.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-2-21.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-2-22.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-2-23.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-2-3.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-2-4.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-2-5.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-2-6.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-2-7.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-2-8.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-2-9.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-3-1.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-3-10.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-3-11.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-3-12.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-3-13.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-3-14.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-3-15.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-3-16.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-3-17.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-3-18.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-3-2.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-3-3.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-3-4.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-3-5.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-3-6.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-3-7.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-3-8.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-3-9.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-4-1.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-4-10.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-4-11.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-4-12.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-4-13.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-4-14.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-4-15.ltx2
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-4-16.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-4-17.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-4-18.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-4-19.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-4-2.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-4-20.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-4-21.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-4-22.ltx2
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-4-23.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-4-24.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-4-25.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-4-26.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-4-27.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-4-28.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-4-29.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-4-3.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-4-4.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-4-5.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-4-6.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-4-7.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-4-8.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-4-9.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-5-1.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-5-10.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-5-11.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-5-12.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-5-13.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-5-14.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-5-15.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-5-16.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-5-17.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-5-18.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-5-19.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-5-2.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-5-20.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-5-21.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-5-22.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-5-23.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-5-24.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-5-25.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-5-26.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-5-3.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-5-4.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-5-5.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-5-6.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-5-7.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-5-8.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/8-5-9.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/9-3-1.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/9-3-10.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/9-3-11.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/9-3-12.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/9-3-13.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/9-3-14.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/9-3-15.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/9-3-16.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/9-3-2.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/9-3-3.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/9-3-4.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/9-3-5.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/9-3-6.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/9-3-7.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/9-3-8.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/9-3-9.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/9-4-1.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/9-4-2.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/9-4-3.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/9-4-4.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/9-4-5.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/9-4-6.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/9-4-7.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/9-4-8.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/9-5-1.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/9-5-10.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/9-5-11.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/9-5-12.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/9-5-13.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/9-5-14.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/9-5-15.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/9-5-2.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/9-5-3.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/9-5-4.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/9-5-5.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/9-5-6.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/9-5-7.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/9-5-8.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/9-5-9.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/9-6-1.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/9-6-10.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/9-6-11.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/9-6-12.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/9-6-13.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/9-6-14.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/9-6-15.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/9-6-16.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/9-6-17.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/9-6-18.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/9-6-19.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/9-6-2.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/9-6-20.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/9-6-21.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/9-6-22.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/9-6-23.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/9-6-24.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/9-6-25.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/9-6-26.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/9-6-27.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/9-6-28.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/9-6-3.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/9-6-4.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/9-6-5.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/9-6-6.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/9-6-7.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/9-6-8.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/9-6-9.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/9-7-1.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/9-7-2.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/9-7-3.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/A-1-1.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/A-1-10.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/A-1-11.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/A-1-12.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/A-1-13.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/A-1-14.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/A-1-15.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/A-1-16.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/A-1-17.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/A-1-2.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/A-1-3.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/A-1-4.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/A-1-5.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/A-1-6.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/A-1-7.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/A-1-8.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/A-1-9.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/A-2-1.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/A-2-10.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/A-2-11.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/A-2-12.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/A-2-2.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/A-2-3.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/A-2-4.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/A-2-5.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/A-2-6.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/A-2-7.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/A-2-8.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/A-2-9.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/A-3-1.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/A-3-10.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/A-3-11.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/A-3-12.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/A-3-13.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/A-3-14.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/A-3-15.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/A-3-16.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/A-3-17.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/A-3-18.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/A-3-19.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/A-3-2.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/A-3-20.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/A-3-21.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/A-3-3.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/A-3-4.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/A-3-5.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/A-3-6.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/A-3-7.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/A-3-8.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/A-3-9.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/A-4-1.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/A-4-2.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/A-4-3.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/A-4-4.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/A-4-5.ltx2
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/A-4-6.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/A-5-1.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/A-5-2.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/A-5-3.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/A-5-4.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/A-5-5.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/A-5-6.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/A-5-7.ltx2
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/A-5-8.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/A-5-9.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/B-4-1.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/B-4-2.ltx
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/Escher.pdf
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/I.pdf
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/cat.pdf
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/elephant.pdf
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/latex-logo.pdf
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/layout-tlc3-special.sty
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/locale.bib
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/longlife-grayscale.jpg
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/longlife.jpg
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/partial.toc
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/phaip.bst
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/rosette.pdf
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/showhyphenation-tlc3-spotcolor.lua
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/tlc-biblatex-special.bib
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/tlc-ex.bib
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/tlc-jura.bib
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/tlc-tex.bib
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/tlc.bib
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/tlc3exa.cls
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/tlc3examargin.cls
%{_texmfdistdir}/doc/latex/tlc3-examples/example-sources/tlc3exareport.cls

%package -n texlive-tlmgr-intro-zh-cn
Version:        %{texlive_version}.%{texlive_noarch}.svn59100
Release:        0
License:        GPL-2.0-or-later
Summary:        A short tutorial on using tlmgr in Chinese
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source164:      tlmgr-intro-zh-cn.doc.tar.xz

%description -n texlive-tlmgr-intro-zh-cn
This is a Chinese translation of the tlmgr documentation. It
introduces some of the common usage of the TeX Live Manager.
The original can be found in the tlmgrbasics package.

%post -n texlive-tlmgr-intro-zh-cn
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tlmgr-intro-zh-cn
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tlmgr-intro-zh-cn
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tlmgr-intro-zh-cn
%{_texmfdistdir}/doc/support/tlmgr-intro-zh-cn/LICENSE
%{_texmfdistdir}/doc/support/tlmgr-intro-zh-cn/README.md
%{_texmfdistdir}/doc/support/tlmgr-intro-zh-cn/body/actions.tex
%{_texmfdistdir}/doc/support/tlmgr-intro-zh-cn/body/examples.tex
%{_texmfdistdir}/doc/support/tlmgr-intro-zh-cn/body/mirrors.tex
%{_texmfdistdir}/doc/support/tlmgr-intro-zh-cn/body/options.tex
%{_texmfdistdir}/doc/support/tlmgr-intro-zh-cn/body/preface.tex
%{_texmfdistdir}/doc/support/tlmgr-intro-zh-cn/body/schemes_and_collections.tex
%{_texmfdistdir}/doc/support/tlmgr-intro-zh-cn/body/syntex.tex
%{_texmfdistdir}/doc/support/tlmgr-intro-zh-cn/fig/collection.png
%{_texmfdistdir}/doc/support/tlmgr-intro-zh-cn/fig/scheme.png
%{_texmfdistdir}/doc/support/tlmgr-intro-zh-cn/latexmkrc
%{_texmfdistdir}/doc/support/tlmgr-intro-zh-cn/tlmgr-intro-zh-cn.pdf
%{_texmfdistdir}/doc/support/tlmgr-intro-zh-cn/tlmgr-intro-zh-cn.sty
%{_texmfdistdir}/doc/support/tlmgr-intro-zh-cn/tlmgr-intro-zh-cn.tex

%package -n texlive-tlmgrbasics
Version:        %{texlive_version}.%{texlive_noarch}.svn70175
Release:        0
License:        GPL-2.0-or-later
Summary:        A simplified documentation for tlmgr
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source165:      tlmgrbasics.doc.tar.xz

%description -n texlive-tlmgrbasics
This package provides simplified documentation for tlmgr, the
TeX Live Manager. It describes the most commonly-used actions
and options in a convenient format.

%post -n texlive-tlmgrbasics
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tlmgrbasics
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tlmgrbasics
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tlmgrbasics
%{_texmfdistdir}/doc/support/tlmgrbasics/README
%{_texmfdistdir}/doc/support/tlmgrbasics/tlmgr.pdf
%{_texmfdistdir}/doc/support/tlmgrbasics/tlmgr.tex

%package -n texlive-to-be-determined
Version:        %{texlive_version}.%{texlive_noarch}.0.0.3.0svn64882
Release:        0
License:        LPPL-1.0
Summary:        Highlight text passages that need further work
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires:       texlive-soul >= %{texlive_version}
#!BuildIgnore: texlive-soul
Requires:       texlive-xcolor >= %{texlive_version}
#!BuildIgnore: texlive-xcolor
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-to-be-determined-doc >= %{texlive_version}
Provides:       tex(to-be-determined.sty)
Requires:       tex(soul.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source166:      to-be-determined.tar.xz
Source167:      to-be-determined.doc.tar.xz

%description -n texlive-to-be-determined
This package provides a single command \tbd which highlights
the pieces of text that need to be rewritten later. You can
hide them all with a single package option hide, or just make
them disappear entirely with the option off.

%package -n texlive-to-be-determined-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.3.0svn64882
Release:        0
Summary:        Documentation for texlive-to-be-determined
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-to-be-determined and texlive-alldocumentation)

%description -n texlive-to-be-determined-doc
This package includes the documentation for texlive-to-be-determined

%post -n texlive-to-be-determined
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-to-be-determined
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-to-be-determined
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-to-be-determined-doc
%{_texmfdistdir}/doc/latex/to-be-determined/DEPENDS.txt
%{_texmfdistdir}/doc/latex/to-be-determined/LICENSE.txt
%{_texmfdistdir}/doc/latex/to-be-determined/README.md
%{_texmfdistdir}/doc/latex/to-be-determined/to-be-determined.pdf

%files -n texlive-to-be-determined
%{_texmfdistdir}/tex/latex/to-be-determined/to-be-determined.sty

%package -n texlive-tocbibind
Version:        %{texlive_version}.%{texlive_noarch}.1.5ksvn20085
Release:        0
License:        LPPL-1.0
Summary:        Add bibliography/index/contents to Table of Contents
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tocbibind-doc >= %{texlive_version}
Provides:       tex(tocbibind.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source168:      tocbibind.tar.xz
Source169:      tocbibind.doc.tar.xz

%description -n texlive-tocbibind
Automatically adds the bibliography and/or the index and/or the
contents, etc., to the Table of Contents listing.

%package -n texlive-tocbibind-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.5ksvn20085
Release:        0
Summary:        Documentation for texlive-tocbibind
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tocbibind and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tocbibind-doc
%{_texmfdistdir}/doc/latex/tocbibind/README
%{_texmfdistdir}/doc/latex/tocbibind/tocbibind.pdf

%files -n texlive-tocbibind
%{_texmfdistdir}/tex/latex/tocbibind/tocbibind.sty

%package -n texlive-tocdata
Version:        %{texlive_version}.%{texlive_noarch}.2.07svn69512
Release:        0
License:        LPPL-1.0
Summary:        Adds names to chapters, sections, figures in the TOC and LOF
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tocdata-doc >= %{texlive_version}
Provides:       tex(tocdata.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(titletoc.sty)
Requires:       tex(tocloft.sty)
Requires:       tex(xparse.sty)
Requires:       tex(xpatch.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source170:      tocdata.tar.xz
Source171:      tocdata.doc.tar.xz

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
Version:        %{texlive_version}.%{texlive_noarch}.2.07svn69512
Release:        0
Summary:        Documentation for texlive-tocdata
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tocdata and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tocdata-doc
%{_texmfdistdir}/doc/latex/tocdata/README.txt
%{_texmfdistdir}/doc/latex/tocdata/tocdata.pdf

%files -n texlive-tocdata
%{_texmfdistdir}/tex/latex/tocdata/tocdata.sty

%package -n texlive-tocloft
Version:        %{texlive_version}.%{texlive_noarch}.2.3jsvn53364
Release:        0
License:        LPPL-1.0
Summary:        Control table of contents, figures, etcetera
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tocloft-doc >= %{texlive_version}
Provides:       tex(tocloft.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source172:      tocloft.tar.xz
Source173:      tocloft.doc.tar.xz

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
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tocloft and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tocloft-doc
%{_texmfdistdir}/doc/latex/tocloft/README
%{_texmfdistdir}/doc/latex/tocloft/tocloft.pdf

%files -n texlive-tocloft
%{_texmfdistdir}/tex/latex/tocloft/tocloft.sty

%package -n texlive-tocvsec2
Version:        %{texlive_version}.%{texlive_noarch}.1.3asvn33146
Release:        0
License:        LPPL-1.0
Summary:        Section numbering and table of contents control
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tocvsec2-doc >= %{texlive_version}
Provides:       tex(tocvsec2.sty)
Requires:       tex(ifthen.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source174:      tocvsec2.tar.xz
Source175:      tocvsec2.doc.tar.xz

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
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tocvsec2 and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tocvsec2-doc
%{_texmfdistdir}/doc/latex/tocvsec2/README
%{_texmfdistdir}/doc/latex/tocvsec2/tocvsec2-example.tex
%{_texmfdistdir}/doc/latex/tocvsec2/tocvsec2.pdf

%files -n texlive-tocvsec2
%{_texmfdistdir}/tex/latex/tocvsec2/tocvsec2.sty

%package -n texlive-todo
Version:        %{texlive_version}.%{texlive_noarch}.2.142svn17746
Release:        0
License:        LPPL-1.0
Summary:        Make a to-do list for a document
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-todo-doc >= %{texlive_version}
Provides:       tex(todo.sty)
Requires:       tex(amssymb.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source176:      todo.tar.xz
Source177:      todo.doc.tar.xz

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
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-todo and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-todo-doc
%{_texmfdistdir}/doc/latex/todo/README
%{_texmfdistdir}/doc/latex/todo/todo-spl.pdf
%{_texmfdistdir}/doc/latex/todo/todo-spl.tex
%{_texmfdistdir}/doc/latex/todo/todo.pdf

%files -n texlive-todo
%{_texmfdistdir}/tex/latex/todo/todo.sty

%package -n texlive-todonotes
Version:        %{texlive_version}.%{texlive_noarch}.1.1.7svn69319
Release:        0
License:        LPPL-1.0
Summary:        Marking things to do in a LaTeX document
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires:       texlive-pgf >= %{texlive_version}
#!BuildIgnore: texlive-pgf
Requires:       texlive-tools >= %{texlive_version}
#!BuildIgnore: texlive-tools
Requires:       texlive-xcolor >= %{texlive_version}
#!BuildIgnore: texlive-xcolor
Requires:       texlive-xkeyval >= %{texlive_version}
#!BuildIgnore: texlive-xkeyval
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-todonotes-doc >= %{texlive_version}
Provides:       tex(todonotes.sty)
Requires:       tex(calc.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source178:      todonotes.tar.xz
Source179:      todonotes.doc.tar.xz

%description -n texlive-todonotes
The package lets the user mark things to do later, in a simple
and visually appealing way. The package takes several options
to enable customization/finetuning of the visual appearance.

%package -n texlive-todonotes-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1.7svn69319
Release:        0
Summary:        Documentation for texlive-todonotes
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-todonotes and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-todonotes-doc
%{_texmfdistdir}/doc/latex/todonotes/README
%{_texmfdistdir}/doc/latex/todonotes/examples/alterAppearenceOfListOfTodos.pdf
%{_texmfdistdir}/doc/latex/todonotes/examples/alterAppearenceOfListOfTodos.tex
%{_texmfdistdir}/doc/latex/todonotes/examples/externalize.pdf
%{_texmfdistdir}/doc/latex/todonotes/examples/externalize.tex
%{_texmfdistdir}/doc/latex/todonotes/examples/saveColorByUsingLayers.pdf
%{_texmfdistdir}/doc/latex/todonotes/examples/saveColorByUsingLayers.tex
%{_texmfdistdir}/doc/latex/todonotes/img/AlteredAppearenceOfListOfTodos.png
%{_texmfdistdir}/doc/latex/todonotes/todonotes.pdf

%files -n texlive-todonotes
%{_texmfdistdir}/tex/latex/todonotes/todonotes.sty

%package -n texlive-tokcycle
Version:        %{texlive_version}.%{texlive_noarch}.1.42svn60320
Release:        0
License:        LPPL-1.0
Summary:        Build tools to process tokens from an input stream
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tokcycle-doc >= %{texlive_version}
Provides:       tex(tokcycle.sty)
Provides:       tex(tokcycle.tex)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source180:      tokcycle.tar.xz
Source181:      tokcycle.doc.tar.xz

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
Version:        %{texlive_version}.%{texlive_noarch}.1.42svn60320
Release:        0
Summary:        Documentation for texlive-tokcycle
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tokcycle and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tokcycle-doc
%{_texmfdistdir}/doc/generic/tokcycle/README
%{_texmfdistdir}/doc/generic/tokcycle/tokcycle-doc.pdf
%{_texmfdistdir}/doc/generic/tokcycle/tokcycle-doc.tex
%{_texmfdistdir}/doc/generic/tokcycle/tokcycle-examples.pdf
%{_texmfdistdir}/doc/generic/tokcycle/tokcycle-examples.tex

%files -n texlive-tokcycle
%{_texmfdistdir}/tex/generic/tokcycle/tokcycle.sty
%{_texmfdistdir}/tex/generic/tokcycle/tokcycle.tex

%package -n texlive-tokenizer
Version:        %{texlive_version}.%{texlive_noarch}.1.1.0svn15878
Release:        0
License:        LPPL-1.0
Summary:        A tokenizer
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tokenizer-doc >= %{texlive_version}
Provides:       tex(tokenizer.sty)
Requires:       tex(ifthen.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source182:      tokenizer.tar.xz
Source183:      tokenizer.doc.tar.xz

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
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tokenizer and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tokenizer-doc
%{_texmfdistdir}/doc/latex/tokenizer/tokenizer.pdf
%{_texmfdistdir}/doc/latex/tokenizer/tokenizer.tex

%files -n texlive-tokenizer
%{_texmfdistdir}/tex/latex/tokenizer/tokenizer.sty

%package -n texlive-tonevalue
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn60058
Release:        0
License:        Apache-1.0
Summary:        Tool for linguists and phoneticians to visualize tone value patterns
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tonevalue-doc >= %{texlive_version}
Provides:       tex(tonevalue.sty)
Requires:       tex(contour.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(listofitems.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xstring.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source184:      tonevalue.tar.xz
Source185:      tonevalue.doc.tar.xz

%description -n texlive-tonevalue
This package provides a TikZ-based solution to typeset
visualisations of tone values. Currently, unt's model is
implemented. Support for more models is planned.

%package -n texlive-tonevalue-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn60058
Release:        0
Summary:        Documentation for texlive-tonevalue
License:        Apache-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tonevalue and texlive-alldocumentation)

%description -n texlive-tonevalue-doc
This package includes the documentation for texlive-tonevalue

%post -n texlive-tonevalue
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tonevalue
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tonevalue
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tonevalue-doc
%{_texmfdistdir}/doc/latex/tonevalue/LICENSE
%{_texmfdistdir}/doc/latex/tonevalue/README
%{_texmfdistdir}/doc/latex/tonevalue/tonevalue.pdf
%{_texmfdistdir}/doc/latex/tonevalue/tonevalue.tex

%files -n texlive-tonevalue
%{_texmfdistdir}/tex/latex/tonevalue/tonevalue.sty

%package -n texlive-toolbox
Version:        %{texlive_version}.%{texlive_noarch}.5.1svn32260
Release:        0
License:        LPPL-1.0
Summary:        Tool macros
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-toolbox-doc >= %{texlive_version}
Provides:       tex(toolbox.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source186:      toolbox.tar.xz
Source187:      toolbox.doc.tar.xz

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
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-toolbox and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-toolbox-doc
%{_texmfdistdir}/doc/latex/toolbox/README
%{_texmfdistdir}/doc/latex/toolbox/toolbox.pdf
%{_texmfdistdir}/doc/latex/toolbox/toolbox.tex
%{_texmfdistdir}/doc/latex/toolbox/toolbox.txt

%files -n texlive-toolbox
%{_texmfdistdir}/tex/latex/toolbox/toolbox.sty

%package -n texlive-tools
Version:        %{texlive_version}.%{texlive_noarch}.20231101csvn68941
Release:        0
License:        LPPL-1.0
Summary:        The LaTeX standard tools bundle
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires:       texlive-extratools >= %{texlive_version}
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tools-doc >= %{texlive_version}
Provides:       tex(afterpage.sty)
Provides:       tex(array-2016-10-06.sty)
Provides:       tex(array-2020-02-10.sty)
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
Provides:       tex(longtable-2020-01-07.sty)
Provides:       tex(longtable.sty)
Provides:       tex(multicol-2017-04-11.sty)
Provides:       tex(multicol-2019-10-01.sty)
Provides:       tex(multicol.sty)
Provides:       tex(q.tex)
Provides:       tex(r.tex)
Provides:       tex(rawfonts.sty)
Provides:       tex(s.tex)
Provides:       tex(shellesc.sty)
Provides:       tex(showkeys-2014-10-28.sty)
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
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source188:      tools.tar.xz
Source189:      tools.doc.tar.xz

%description -n texlive-tools
A collection of (variously) simple tools provided as part of
the LaTeX required tools distribution, comprising the packages:
afterpage, array, bm, calc, dcolumn, delarray, enumerate,
fileerr, fontsmpl, ftnright, hhline, indentfirst, layout,
longtable, multicol, rawfonts, shellesc, showkeys, somedefs,
tabularx, theorem, trace, varioref, verbatim, xr, and xspace.

%package -n texlive-tools-doc
Version:        %{texlive_version}.%{texlive_noarch}.20231101csvn68941
Release:        0
Summary:        Documentation for texlive-tools
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tools and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tools-doc
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
%{_texmfdistdir}/tex/latex/tools/.tex
%{_texmfdistdir}/tex/latex/tools/afterpage.sty
%{_texmfdistdir}/tex/latex/tools/array-2016-10-06.sty
%{_texmfdistdir}/tex/latex/tools/array-2020-02-10.sty
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
%{_texmfdistdir}/tex/latex/tools/longtable-2020-01-07.sty
%{_texmfdistdir}/tex/latex/tools/longtable.sty
%{_texmfdistdir}/tex/latex/tools/multicol-2017-04-11.sty
%{_texmfdistdir}/tex/latex/tools/multicol-2019-10-01.sty
%{_texmfdistdir}/tex/latex/tools/multicol.sty
%{_texmfdistdir}/tex/latex/tools/q.tex
%{_texmfdistdir}/tex/latex/tools/r.tex
%{_texmfdistdir}/tex/latex/tools/rawfonts.sty
%{_texmfdistdir}/tex/latex/tools/s.tex
%{_texmfdistdir}/tex/latex/tools/shellesc.sty
%{_texmfdistdir}/tex/latex/tools/showkeys-2014-10-28.sty
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

%package -n texlive-topfloat
Version:        %{texlive_version}.%{texlive_noarch}.svn19084
Release:        0
License:        GPL-2.0-or-later
Summary:        Move floats to the top of the page
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-topfloat-doc >= %{texlive_version}
Provides:       tex(topfloat.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source190:      topfloat.tar.xz
Source191:      topfloat.doc.tar.xz

%description -n texlive-topfloat
The topfloat package

%package -n texlive-topfloat-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn19084
Release:        0
Summary:        Documentation for texlive-topfloat
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-topfloat and texlive-alldocumentation)
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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-topfloat-doc
%{_texmfdistdir}/doc/latex/topfloat/topfloat.pdf
%{_texmfdistdir}/doc/latex/topfloat/topfloat.tex

%files -n texlive-topfloat
%{_texmfdistdir}/tex/latex/topfloat/topfloat.sty

%package -n texlive-topiclongtable
Version:        %{texlive_version}.%{texlive_noarch}.1.3.2svn54758
Release:        0
License:        LPPL-1.0
Summary:        Extend longtable with cells that merge hierarchically
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-topiclongtable-doc >= %{texlive_version}
Provides:       tex(topiclongtable.sty)
Requires:       tex(array.sty)
Requires:       tex(expl3.sty)
Requires:       tex(longtable.sty)
Requires:       tex(multirow.sty)
Requires:       tex(xparse.sty)
Requires:       tex(zref-abspage.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source192:      topiclongtable.tar.xz
Source193:      topiclongtable.doc.tar.xz

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
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-topiclongtable and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-topiclongtable-doc
%{_texmfdistdir}/doc/latex/topiclongtable/README.md
%{_texmfdistdir}/doc/latex/topiclongtable/topiclongtable-doc.pdf
%{_texmfdistdir}/doc/latex/topiclongtable/topiclongtable-doc.tex

%files -n texlive-topiclongtable
%{_texmfdistdir}/tex/latex/topiclongtable/topiclongtable.sty

%package -n texlive-topletter
Version:        %{texlive_version}.%{texlive_noarch}.0.0.3.0svn48182
Release:        0
License:        Apache-1.0
Summary:        Letter class for the Politecnico di Torino
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-topletter-doc >= %{texlive_version}
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
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source194:      topletter.tar.xz
Source195:      topletter.doc.tar.xz

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
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-topletter and texlive-alldocumentation)
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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-topletter-doc
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
%{_texmfdistdir}/tex/latex/topletter/TOPletter.cls

%package -n texlive-toptesi
Version:        %{texlive_version}.%{texlive_noarch}.6.4.06svn56276
Release:        0
License:        LPPL-1.0
Summary:        Bundle for typesetting multilanguage theses
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-toptesi-doc >= %{texlive_version}
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
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source196:      toptesi.tar.xz
Source197:      toptesi.doc.tar.xz

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
Version:        %{texlive_version}.%{texlive_noarch}.6.4.06svn56276
Release:        0
Summary:        Documentation for texlive-toptesi
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-toptesi and texlive-alldocumentation)
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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-toptesi-doc
%{_texmfdistdir}/doc/latex/toptesi/FrontespiziAssemblati.pdf
%{_texmfdistdir}/doc/latex/toptesi/FrontespiziAssemblati1.pdf
%{_texmfdistdir}/doc/latex/toptesi/FrontespiziAssemblati2.pdf
%{_texmfdistdir}/doc/latex/toptesi/Frontespizio-sss.pdf
%{_texmfdistdir}/doc/latex/toptesi/FrontespizioLandscape.pdf
%{_texmfdistdir}/doc/latex/toptesi/FrontespizioScudo.pdf
%{_texmfdistdir}/doc/latex/toptesi/FrontespizioScudo.tex
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
%{_texmfdistdir}/doc/latex/toptesi/logoguittondo.pdf
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
%{_texmfdistdir}/doc/latex/toptesi/veraPDFnoconformance.pdf

%files -n texlive-toptesi
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

%package -n texlive-totalcount
Version:        %{texlive_version}.%{texlive_noarch}.1.0asvn67201
Release:        0
License:        LPPL-1.0
Summary:        Commands for typesetting total values of counters
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-totalcount-doc >= %{texlive_version}
Provides:       tex(totalcount.sty)
Requires:       tex(xspace.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source198:      totalcount.tar.xz
Source199:      totalcount.doc.tar.xz

%description -n texlive-totalcount
This LaTeX package offers commands for typesetting total values
of counters.

%package -n texlive-totalcount-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0asvn67201
Release:        0
Summary:        Documentation for texlive-totalcount
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-totalcount and texlive-alldocumentation)

%description -n texlive-totalcount-doc
This package includes the documentation for texlive-totalcount

%post -n texlive-totalcount
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-totalcount
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-totalcount
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-totalcount-doc
%{_texmfdistdir}/doc/latex/totalcount/CHANGELOG
%{_texmfdistdir}/doc/latex/totalcount/README
%{_texmfdistdir}/doc/latex/totalcount/SUMMARY
%{_texmfdistdir}/doc/latex/totalcount/totalcount.pdf

%files -n texlive-totalcount
%{_texmfdistdir}/tex/latex/totalcount/totalcount.sty

%package -n texlive-totcount
Version:        %{texlive_version}.%{texlive_noarch}.1.2svn21178
Release:        0
License:        LPPL-1.0
Summary:        Find the last value of a counter
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-totcount-doc >= %{texlive_version}
Provides:       tex(totcount.sty)
Requires:       tex(keyval.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source200:      totcount.tar.xz
Source201:      totcount.doc.tar.xz

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
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-totcount and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-totcount-doc
%{_texmfdistdir}/doc/latex/totcount/README
%{_texmfdistdir}/doc/latex/totcount/totcount-ex.tex
%{_texmfdistdir}/doc/latex/totcount/totcount.pdf

%files -n texlive-totcount
%{_texmfdistdir}/tex/latex/totcount/totcount.sty

%package -n texlive-totpages
Version:        %{texlive_version}.%{texlive_noarch}.2.00svn15878
Release:        0
License:        LPPL-1.0
Summary:        Count pages in a document, and report last page number
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-totpages-doc >= %{texlive_version}
Provides:       tex(totpages.sty)
Requires:       tex(everyshi.sty)
Requires:       tex(keyval.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source202:      totpages.tar.xz
Source203:      totpages.doc.tar.xz

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
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-totpages and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-totpages-doc
%{_texmfdistdir}/doc/latex/totpages/README
%{_texmfdistdir}/doc/latex/totpages/totexmpl.tex
%{_texmfdistdir}/doc/latex/totpages/totpages.pdf

%files -n texlive-totpages
%{_texmfdistdir}/tex/latex/totpages/totpages.sty

%package -n texlive-tpic2pdftex
Version:        %{texlive_version}.%{texlive_noarch}.svn52851
Release:        0
License:        GPL-2.0-or-later
Summary:        Use tpic commands in pdfTeX
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-tpic2pdftex-bin >= %{texlive_version}
#!BuildIgnore: texlive-tpic2pdftex-bin
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source204:      tpic2pdftex.doc.tar.xz

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tpic2pdftex
%{_mandir}/man1/tpic2pdftex.1*
%{_texmfdistdir}/doc/tpic2pdftex/Makefile
%{_texmfdistdir}/doc/tpic2pdftex/beamerexample.pdf
%{_texmfdistdir}/doc/tpic2pdftex/beamerexample.pic
%{_texmfdistdir}/doc/tpic2pdftex/example.pdf
%{_texmfdistdir}/doc/tpic2pdftex/example.pic

%package -n texlive-tpslifonts
Version:        %{texlive_version}.%{texlive_noarch}.0.0.6svn42428
Release:        0
License:        GPL-2.0-or-later
Summary:        A LaTeX package for configuring presentation fonts
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tpslifonts-doc >= %{texlive_version}
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
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source205:      tpslifonts.tar.xz
Source206:      tpslifonts.doc.tar.xz

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
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tpslifonts and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tpslifonts-doc
%{_texmfdistdir}/doc/latex/tpslifonts/00readme.txt
%{_texmfdistdir}/doc/latex/tpslifonts/01install.txt
%{_texmfdistdir}/doc/latex/tpslifonts/Makefile
%{_texmfdistdir}/doc/latex/tpslifonts/slifontsexample.tex

%files -n texlive-tpslifonts
%{_texmfdistdir}/tex/latex/tpslifonts/tpslifonts.sty

%package -n texlive-tqft
Version:        %{texlive_version}.%{texlive_noarch}.2.1svn44455
Release:        0
License:        LPPL-1.0
Summary:        Drawing TQFT diagrams with TikZ/PGF
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tqft-doc >= %{texlive_version}
Provides:       tex(tikzlibrarytqft.code.tex)
Provides:       tex(tqft.sty)
Requires:       tex(pgf.sty)
Requires:       tex(pgfkeys.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source207:      tqft.tar.xz
Source208:      tqft.doc.tar.xz

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
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tqft and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tqft-doc
%{_texmfdistdir}/doc/latex/tqft/README
%{_texmfdistdir}/doc/latex/tqft/tqft.pdf
%{_texmfdistdir}/doc/latex/tqft/tqft_code.pdf
%{_texmfdistdir}/doc/latex/tqft/tqft_doc.tex

%files -n texlive-tqft
%{_texmfdistdir}/tex/latex/tqft/tikzlibrarytqft.code.tex
%{_texmfdistdir}/tex/latex/tqft/tqft.sty

%package -n texlive-tracklang
Version:        %{texlive_version}.%{texlive_noarch}.1.6.1svn65263
Release:        0
License:        LPPL-1.0
Summary:        Language and dialect tracker
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tracklang-doc >= %{texlive_version}
Provides:       tex(tracklang-region-codes.tex)
Provides:       tex(tracklang-scripts.sty)
Provides:       tex(tracklang-scripts.tex)
Provides:       tex(tracklang.sty)
Provides:       tex(tracklang.tex)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source209:      tracklang.tar.xz
Source210:      tracklang.doc.tar.xz

%description -n texlive-tracklang
The tracklang package is provided for package developers who
want a simple interface to find out which languages the user
has requested through packages such as babel or polyglossia.
This package does not provide any translations! Its purpose is
simply to track which languages have been requested by the
user. Generic TeX code is in tracklang.tex for non-LaTeX users.

%package -n texlive-tracklang-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.6.1svn65263
Release:        0
Summary:        Documentation for texlive-tracklang
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tracklang and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tracklang-doc
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
%{_texmfdistdir}/doc/generic/tracklang/tracklang-code.pdf
%{_texmfdistdir}/doc/generic/tracklang/tracklang-manual.html
%{_texmfdistdir}/doc/generic/tracklang/tracklang-manual.pdf
%{_texmfdistdir}/doc/generic/tracklang/tracklang-manual.tex

%files -n texlive-tracklang
%{_texmfdistdir}/tex/generic/tracklang/tracklang-region-codes.tex
%{_texmfdistdir}/tex/generic/tracklang/tracklang-scripts.tex
%{_texmfdistdir}/tex/generic/tracklang/tracklang.tex
%{_texmfdistdir}/tex/latex/tracklang/tracklang-scripts.sty
%{_texmfdistdir}/tex/latex/tracklang/tracklang.sty

%package -n texlive-trajan
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn15878
Release:        0
License:        LPPL-1.0
Summary:        Fonts from the Trajan column in Rome
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-trajan-doc >= %{texlive_version}
Provides:       tex(t1trjn.fd)
Provides:       tex(trajan.map)
Provides:       tex(trajan.sty)
Provides:       tex(trjnr10.tfm)
Provides:       tex(trjnsl10.tfm)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source211:      trajan.tar.xz
Source212:      trajan.doc.tar.xz

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
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-trajan and texlive-alldocumentation)

%description -n texlive-trajan-doc
This package includes the documentation for texlive-trajan

%package -n texlive-trajan-fonts
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn15878
Release:        0
Summary:        Severed fonts for texlive-trajan
License:        LPPL-1.0
URL:            https://www.tug.org/texlive/
Group:          Productivity/Publishing/TeX/Fonts
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Suggests:       xorg-x11-fonts-core

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-trajan-fonts

%files -n texlive-trajan-doc
%{_texmfdistdir}/doc/latex/trajan/README
%{_texmfdistdir}/doc/latex/trajan/trajan.pdf
%{_texmfdistdir}/doc/latex/trajan/trytrajan.pdf
%{_texmfdistdir}/doc/latex/trajan/trytrajan.tex

%files -n texlive-trajan
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
%dir %{_datadir}/fonts/texlive-trajan
%{_datadir}/fontconfig/conf.avail/58-texlive-trajan.conf
%verify(not md5 size mtime) %{_datadir}/fonts/texlive-trajan/encodings.dir
%verify(not md5 size mtime) %{_datadir}/fonts/texlive-trajan/fonts.dir
%verify(not md5 size mtime) %{_datadir}/fonts/texlive-trajan/fonts.scale
%{_datadir}/fonts/texlive-trajan/trjnr10.pfb
%{_datadir}/fonts/texlive-trajan/trjnsl10.pfb

%package -n texlive-tram
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2svn29803
Release:        0
License:        LPPL-1.0
Summary:        Typeset tram boxes in LaTeX
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tram-doc >= %{texlive_version}
Provides:       tex(tram.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source213:      tram.tar.xz
Source214:      tram.doc.tar.xz

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
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tram and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tram-doc
%{_texmfdistdir}/doc/latex/tram/README
%{_texmfdistdir}/doc/latex/tram/tram-doc.pdf
%{_texmfdistdir}/doc/latex/tram/tram-doc.tex

%files -n texlive-tram
%{_texmfdistdir}/fonts/source/public/tram/tram.mf
%{_texmfdistdir}/tex/latex/tram/tram.sty

%package -n texlive-tramlines
Version:        %{texlive_version}.%{texlive_noarch}.1.1.0svn65692
Release:        0
License:        LPPL-1.0
Summary:        A package for creating tramlines (lines above and below a title used by lawyers in the UK)
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tramlines-doc >= %{texlive_version}
Provides:       tex(tramlines.sty)
Requires:       tex(booktabs.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source215:      tramlines.tar.xz
Source216:      tramlines.doc.tar.xz

%description -n texlive-tramlines
This package automatically creates tramlines (lines above and
below a title used by lawyers in the UK and the Commonwealth).

%package -n texlive-tramlines-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1.0svn65692
Release:        0
Summary:        Documentation for texlive-tramlines
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tramlines and texlive-alldocumentation)

%description -n texlive-tramlines-doc
This package includes the documentation for texlive-tramlines

%post -n texlive-tramlines
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tramlines
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tramlines
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tramlines-doc
%{_texmfdistdir}/doc/latex/tramlines/README
%{_texmfdistdir}/doc/latex/tramlines/tramlines-documentation.pdf
%{_texmfdistdir}/doc/latex/tramlines/tramlines-documentation.tex

%files -n texlive-tramlines
%{_texmfdistdir}/tex/latex/tramlines/tramlines.sty

%package -n texlive-translation-array-fr
Version:        %{texlive_version}.%{texlive_noarch}.svn24344
Release:        0
License:        LPPL-1.0
Summary:        French translation of the documentation of array
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source217:      translation-array-fr.doc.tar.xz

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-translation-array-fr
%{_texmfdistdir}/doc/latex/translation-array-fr/Copyright
%{_texmfdistdir}/doc/latex/translation-array-fr/README
%{_texmfdistdir}/doc/latex/translation-array-fr/f-array.dtx
%{_texmfdistdir}/doc/latex/translation-array-fr/f-array.pdf
%{_texmfdistdir}/doc/latex/translation-array-fr/ltxdoc.cfg

%package -n texlive-translation-arsclassica-de
Version:        %{texlive_version}.%{texlive_noarch}.svn23803
Release:        0
License:        LPPL-1.0
Summary:        German version of arsclassica
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source218:      translation-arsclassica-de.doc.tar.xz

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-translation-arsclassica-de
%{_texmfdistdir}/doc/latex/translation-arsclassica-de/ArsClassica-de.pdf
%{_texmfdistdir}/doc/latex/translation-arsclassica-de/ArsClassica-de.tex

%package -n texlive-translation-biblatex-de
Version:        %{texlive_version}.%{texlive_noarch}.3.15bsvn59382
Release:        0
License:        LPPL-1.0
Summary:        German translation of the User Guide for BibLaTeX
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source219:      translation-biblatex-de.doc.tar.xz

%description -n texlive-translation-biblatex-de
A German translation of the User Guide for BibLaTeX.

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-translation-biblatex-de
%{_texmfdistdir}/doc/latex/translation-biblatex-de/README
%{_texmfdistdir}/doc/latex/translation-biblatex-de/biblatex-de-Benutzerhandbuch.pdf
%{_texmfdistdir}/doc/latex/translation-biblatex-de/biblatex-de-Benutzerhandbuch.tex

%package -n texlive-translation-chemsym-de
Version:        %{texlive_version}.%{texlive_noarch}.svn23804
Release:        0
License:        LPPL-1.0
Summary:        German version of chemsym
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source220:      translation-chemsym-de.doc.tar.xz

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-translation-chemsym-de
%{_texmfdistdir}/doc/latex/translation-chemsym-de/00Liesmich.chs
%{_texmfdistdir}/doc/latex/translation-chemsym-de/chemsym-de.dtx
%{_texmfdistdir}/doc/latex/translation-chemsym-de/chemsym-de.pdf

%package -n texlive-translation-dcolumn-fr
Version:        %{texlive_version}.%{texlive_noarch}.svn24345
Release:        0
License:        LPPL-1.0
Summary:        French translation of the documentation of dcolumn
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source221:      translation-dcolumn-fr.doc.tar.xz

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-translation-dcolumn-fr
%{_texmfdistdir}/doc/latex/translation-dcolumn-fr/Copyright
%{_texmfdistdir}/doc/latex/translation-dcolumn-fr/README
%{_texmfdistdir}/doc/latex/translation-dcolumn-fr/f-dcolumn.dtx
%{_texmfdistdir}/doc/latex/translation-dcolumn-fr/f-dcolumn.pdf

%package -n texlive-translation-ecv-de
Version:        %{texlive_version}.%{texlive_noarch}.svn24754
Release:        0
License:        LPPL-1.0
Summary:        Ecv documentation, in German
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source222:      translation-ecv-de.doc.tar.xz

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-translation-ecv-de
%{_texmfdistdir}/doc/latex/translation-ecv-de/ecvde.dtx.pdf
%{_texmfdistdir}/doc/latex/translation-ecv-de/ecvde.dtx.tex

%package -n texlive-translation-enumitem-de
Version:        %{texlive_version}.%{texlive_noarch}.svn24196
Release:        0
License:        LPPL-1.0
Summary:        Enumitem documentation, in German
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source223:      translation-enumitem-de.doc.tar.xz

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-translation-enumitem-de
%{_texmfdistdir}/doc/latex/translation-enumitem-de/enumitem-de.pdf
%{_texmfdistdir}/doc/latex/translation-enumitem-de/enumitem-de.tex

%package -n texlive-translation-europecv-de
Version:        %{texlive_version}.%{texlive_noarch}.svn23840
Release:        0
License:        LPPL-1.0
Summary:        German version of europecv
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source224:      translation-europecv-de.doc.tar.xz

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-translation-europecv-de
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

%package -n texlive-translation-filecontents-de
Version:        %{texlive_version}.%{texlive_noarch}.svn24010
Release:        0
License:        LPPL-1.0
Summary:        German version of filecontents
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source225:      translation-filecontents-de.doc.tar.xz

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-translation-filecontents-de
%{_texmfdistdir}/doc/latex/translation-filecontents-de/filecontents-de.dtx
%{_texmfdistdir}/doc/latex/translation-filecontents-de/filecontents-de.ins
%{_texmfdistdir}/doc/latex/translation-filecontents-de/filecontents-de.pdf

%package -n texlive-translation-moreverb-de
Version:        %{texlive_version}.%{texlive_noarch}.svn23957
Release:        0
License:        LPPL-1.0
Summary:        German version of moreverb
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source226:      translation-moreverb-de.doc.tar.xz

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-translation-moreverb-de
%{_texmfdistdir}/doc/latex/translation-moreverb-de/filecontens-de.ins.txt
%{_texmfdistdir}/doc/latex/translation-moreverb-de/moreverb-de.dtx.pdf
%{_texmfdistdir}/doc/latex/translation-moreverb-de/moreverb-de.dtx.tex

%package -n texlive-translation-natbib-fr
Version:        %{texlive_version}.%{texlive_noarch}.svn25105
Release:        0
License:        LPPL-1.0
Summary:        French translation of the documentation of natbib
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source227:      translation-natbib-fr.doc.tar.xz

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-translation-natbib-fr
%{_texmfdistdir}/doc/latex/translation-natbib-fr/f-natbib.dtx
%{_texmfdistdir}/doc/latex/translation-natbib-fr/f-natbib.pdf

%package -n texlive-translation-tabbing-fr
Version:        %{texlive_version}.%{texlive_noarch}.svn24228
Release:        0
License:        LPPL-1.0
Summary:        French translation of the documentation of Tabbing
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source228:      translation-tabbing-fr.doc.tar.xz

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-translation-tabbing-fr
%{_texmfdistdir}/doc/latex/translation-tabbing-fr/f-Tabbing.dtx
%{_texmfdistdir}/doc/latex/translation-tabbing-fr/f-Tabbing.pdf
%{_texmfdistdir}/doc/latex/translation-tabbing-fr/ltxdoc.cfg

%package -n texlive-translations
Version:        %{texlive_version}.%{texlive_noarch}.1.12svn61896
Release:        0
License:        LPPL-1.0
Summary:        Internationalisation of LaTeX2e packages
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-translations-doc >= %{texlive_version}
Provides:       tex(translations.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(pdftexcmds.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source229:      translations.tar.xz
Source230:      translations.doc.tar.xz

%description -n texlive-translations
This package (once part of the exsheets package), provides a
framework for providing multilingual features to a LaTeX
package. The package has its own basic dictionaries for
English, Brazilian, Catalan, Dutch, French, German and Spanish;
it aims to use translation material for English, Dutch, French,
German, Italian, Spanish, Catalan, Turkish, Croatian,
Hungarian, Danish and Portuguese from babel or polyglossia if
either is in use in the document. (Additional languages from
the multilingual packages may be possible: ask the author.)

%package -n texlive-translations-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.12svn61896
Release:        0
Summary:        Documentation for texlive-translations
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-translations and texlive-alldocumentation)
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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-translations-doc
%{_texmfdistdir}/doc/latex/translations/README
%{_texmfdistdir}/doc/latex/translations/translations-manual.pdf
%{_texmfdistdir}/doc/latex/translations/translations-manual.tex

%files -n texlive-translations
%{_texmfdistdir}/tex/latex/translations/translations-basic-dictionary-brazil.trsl
%{_texmfdistdir}/tex/latex/translations/translations-basic-dictionary-catalan.trsl
%{_texmfdistdir}/tex/latex/translations/translations-basic-dictionary-dutch.trsl
%{_texmfdistdir}/tex/latex/translations/translations-basic-dictionary-english.trsl
%{_texmfdistdir}/tex/latex/translations/translations-basic-dictionary-french.trsl
%{_texmfdistdir}/tex/latex/translations/translations-basic-dictionary-german.trsl
%{_texmfdistdir}/tex/latex/translations/translations-basic-dictionary-polish.trsl
%{_texmfdistdir}/tex/latex/translations/translations-basic-dictionary-spanish.trsl
%{_texmfdistdir}/tex/latex/translations/translations.sty

%package -n texlive-translator
Version:        %{texlive_version}.%{texlive_noarch}.1.12dsvn59412
Release:        0
License:        LPPL-1.0
Summary:        Easy translation of strings in LaTeX
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-translator-doc >= %{texlive_version}
Provides:       tex(translator.sty)
Requires:       tex(keyval.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source231:      translator.tar.xz
Source232:      translator.doc.tar.xz

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
Version:        %{texlive_version}.%{texlive_noarch}.1.12dsvn59412
Release:        0
Summary:        Documentation for texlive-translator
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-translator and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-translator-doc
%{_texmfdistdir}/doc/latex/translator/README.md
%{_texmfdistdir}/doc/latex/translator/translator.pdf
%{_texmfdistdir}/doc/latex/translator/translator.tex

%files -n texlive-translator
%{_texmfdistdir}/tex/latex/translator/translator-basic-dictionary-Bulgarian.dict
%{_texmfdistdir}/tex/latex/translator/translator-basic-dictionary-Catalan.dict
%{_texmfdistdir}/tex/latex/translator/translator-basic-dictionary-Croatian.dict
%{_texmfdistdir}/tex/latex/translator/translator-basic-dictionary-Czech.dict
%{_texmfdistdir}/tex/latex/translator/translator-basic-dictionary-Danish.dict
%{_texmfdistdir}/tex/latex/translator/translator-basic-dictionary-Dutch.dict
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
%{_texmfdistdir}/tex/latex/translator/translator-bibliography-dictionary-Czech.dict
%{_texmfdistdir}/tex/latex/translator/translator-bibliography-dictionary-Danish.dict
%{_texmfdistdir}/tex/latex/translator/translator-bibliography-dictionary-Dutch.dict
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
%{_texmfdistdir}/tex/latex/translator/translator-environment-dictionary-Czech.dict
%{_texmfdistdir}/tex/latex/translator/translator-environment-dictionary-Danish.dict
%{_texmfdistdir}/tex/latex/translator/translator-environment-dictionary-Dutch.dict
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
%{_texmfdistdir}/tex/latex/translator/translator-months-dictionary-Czech.dict
%{_texmfdistdir}/tex/latex/translator/translator-months-dictionary-Danish.dict
%{_texmfdistdir}/tex/latex/translator/translator-months-dictionary-Dutch.dict
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
%{_texmfdistdir}/tex/latex/translator/translator-numbers-dictionary-Czech.dict
%{_texmfdistdir}/tex/latex/translator/translator-numbers-dictionary-Danish.dict
%{_texmfdistdir}/tex/latex/translator/translator-numbers-dictionary-Dutch.dict
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
%{_texmfdistdir}/tex/latex/translator/translator-theorem-dictionary-Czech.dict
%{_texmfdistdir}/tex/latex/translator/translator-theorem-dictionary-Danish.dict
%{_texmfdistdir}/tex/latex/translator/translator-theorem-dictionary-Dutch.dict
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

%package -n texlive-transparent
Version:        %{texlive_version}.%{texlive_noarch}.1.5svn64852
Release:        0
License:        LPPL-1.0
Summary:        Using a color stack for transparency with pdfTeX
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-transparent-doc >= %{texlive_version}
Provides:       tex(transparent-nometadata.sty)
Provides:       tex(transparent.sty)
Requires:       tex(auxhook.sty)
Requires:       tex(iftex.sty)
Requires:       tex(l3opacity.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source233:      transparent.tar.xz
Source234:      transparent.doc.tar.xz

%description -n texlive-transparent
pdfTeX and LuaTeX support several color stacks. This package
shows how a separate color stack can be used for transparency,
a property besides color that works across page breaks. If the
PDF management is used it can also be used with other engines,
but without support for page breaks.

%package -n texlive-transparent-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.5svn64852
Release:        0
Summary:        Documentation for texlive-transparent
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-transparent and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-transparent-doc
%{_texmfdistdir}/doc/latex/transparent/README.md
%{_texmfdistdir}/doc/latex/transparent/transparent-example.tex
%{_texmfdistdir}/doc/latex/transparent/transparent.pdf

%files -n texlive-transparent
%{_texmfdistdir}/tex/latex/transparent/transparent-nometadata.sty
%{_texmfdistdir}/tex/latex/transparent/transparent.sty

%package -n texlive-transparent-io
Version:        %{texlive_version}.%{texlive_noarch}.svn64113
Release:        0
License:        GPL-2.0-or-later
Summary:        Show for approval the filenames used in \input, \openin, or \openout
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source235:      transparent-io.doc.tar.xz

%description -n texlive-transparent-io
This package provides macros to make the file I/O in plain TeX
more transparent. That is, every \input, \openin, and \openout
operation by TeX is presented to the user who must check
carefully if the file name of the source is acceptable. The
user must sometimes enter additional text and has to specify
the file name that the TeX operation should use. The macros
require a complex installation procedure; the package contains
sed and bash scripts to do this on a UNIX-like operating
system. Every installation is different from any other as
password-protected macro names and private messages have to be
chosen by the installer. Therefore, the files in the package
cannot be used directly. The files carry the extension .org,
and only after the user has performed an individual
customization for a private installation the changed files are
renamed and have the extension .tex. For details see the
manual.

%post -n texlive-transparent-io
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-transparent-io
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-transparent-io
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-transparent-io
%{_texmfdistdir}/doc/plain/transparent-io/README
%{_texmfdistdir}/doc/plain/transparent-io/TrIO.org
%{_texmfdistdir}/doc/plain/transparent-io/TrIOauto.org
%{_texmfdistdir}/doc/plain/transparent-io/TrIOextract.org
%{_texmfdistdir}/doc/plain/transparent-io/TrIOinput.org
%{_texmfdistdir}/doc/plain/transparent-io/TrIOinstall.org
%{_texmfdistdir}/doc/plain/transparent-io/TrIOlineno.org
%{_texmfdistdir}/doc/plain/transparent-io/TrIOmacros.org
%{_texmfdistdir}/doc/plain/transparent-io/TrIOopen.org
%{_texmfdistdir}/doc/plain/transparent-io/TrIOopenin.org
%{_texmfdistdir}/doc/plain/transparent-io/TrIOopenout.org
%{_texmfdistdir}/doc/plain/transparent-io/TrIOprivate.org
%{_texmfdistdir}/doc/plain/transparent-io/TrIOsupport.org
%{_texmfdistdir}/doc/plain/transparent-io/Transparent-IO-TUGboat-danger.tex
%{_texmfdistdir}/doc/plain/transparent-io/Transparent-IO-doc.pdf
%{_texmfdistdir}/doc/plain/transparent-io/Transparent-IO-doc.tex
%{_texmfdistdir}/doc/plain/transparent-io/Transparent-IO-eccentric.tex
%{_texmfdistdir}/doc/plain/transparent-io/Transparent-IO-example.tex
%{_texmfdistdir}/doc/plain/transparent-io/Transparent-IO-hello.tex

%package -n texlive-tree-dvips
Version:        %{texlive_version}.%{texlive_noarch}.0.0.91svn21751
Release:        0
License:        LPPL-1.0
Summary:        Trees and other linguists' macros
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tree-dvips-doc >= %{texlive_version}
Provides:       tex(lingmacros.sty)
Provides:       tex(tree-dvips.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source236:      tree-dvips.tar.xz
Source237:      tree-dvips.doc.tar.xz

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
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tree-dvips and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tree-dvips-doc
%{_texmfdistdir}/doc/latex/tree-dvips/Makefile
%{_texmfdistdir}/doc/latex/tree-dvips/README
%{_texmfdistdir}/doc/latex/tree-dvips/README.TEXLIVE
%{_texmfdistdir}/doc/latex/tree-dvips/lingmacros-manual.pdf
%{_texmfdistdir}/doc/latex/tree-dvips/lingmacros-manual.tex
%{_texmfdistdir}/doc/latex/tree-dvips/tree-dvips91.script
%{_texmfdistdir}/doc/latex/tree-dvips/tree-manual.pdf
%{_texmfdistdir}/doc/latex/tree-dvips/tree-manual.tex

%files -n texlive-tree-dvips
%{_texmfdistdir}/dvips/tree-dvips/tree-dvips91.pro
%{_texmfdistdir}/tex/latex/tree-dvips/lingmacros.sty
%{_texmfdistdir}/tex/latex/tree-dvips/tree-dvips.sty

%package -n texlive-treetex
Version:        %{texlive_version}.%{texlive_noarch}.svn28176
Release:        0
License:        SUSE-Public-Domain
Summary:        Draw trees
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-treetex-doc >= %{texlive_version}
Provides:       tex(classes.tex)
Provides:       tex(l_pic.tex)
Provides:       tex(treetex.tex)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source238:      treetex.tar.xz
Source239:      treetex.doc.tar.xz

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
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-treetex and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-treetex-doc
%{_texmfdistdir}/doc/plain/treetex/epodd.tex
%{_texmfdistdir}/doc/plain/treetex/readme
%{_texmfdistdir}/doc/plain/treetex/tree_doc.tex

%files -n texlive-treetex
%{_texmfdistdir}/tex/plain/treetex/classes.tex
%{_texmfdistdir}/tex/plain/treetex/l_pic.tex
%{_texmfdistdir}/tex/plain/treetex/treetex.tex

%package -n texlive-trfsigns
Version:        %{texlive_version}.%{texlive_noarch}.1.01svn15878
Release:        0
License:        GPL-2.0-or-later
Summary:        Typeset transform signs
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-trfsigns-doc >= %{texlive_version}
Provides:       tex(trfsigns.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source240:      trfsigns.tar.xz
Source241:      trfsigns.doc.tar.xz

%description -n texlive-trfsigns
A package for typesetting various transformation signs for
Laplace transforms, Fourier transforms and others.

%package -n texlive-trfsigns-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.01svn15878
Release:        0
Summary:        Documentation for texlive-trfsigns
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-trfsigns and texlive-alldocumentation)
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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-trfsigns-doc
%{_texmfdistdir}/doc/latex/trfsigns/COPYING
%{_texmfdistdir}/doc/latex/trfsigns/README
%{_texmfdistdir}/doc/latex/trfsigns/trfexamp.tex
%{_texmfdistdir}/doc/latex/trfsigns/trfsigns.pdf

%files -n texlive-trfsigns
%{_texmfdistdir}/tex/latex/trfsigns/trfsigns.sty

%package -n texlive-trigonometry
Version:        %{texlive_version}.%{texlive_noarch}.svn43006
Release:        0
License:        SUSE-TeX
Summary:        Demonstration code for cos and sin in TeX macros
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-trigonometry-doc >= %{texlive_version}
Provides:       tex(trigonometry.tex)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source242:      trigonometry.tar.xz
Source243:      trigonometry.doc.tar.xz

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
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-trigonometry and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-trigonometry-doc
%{_texmfdistdir}/doc/generic/trigonometry/README.txt

%files -n texlive-trigonometry
%{_texmfdistdir}/tex/generic/trigonometry/trigonometry.tex

%package -n texlive-trimspaces
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn15878
Release:        0
License:        LPPL-1.0
Summary:        Trim spaces around an argument or within a macro
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-trimspaces-doc >= %{texlive_version}
Provides:       tex(trimspaces.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source244:      trimspaces.tar.xz
Source245:      trimspaces.doc.tar.xz

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
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-trimspaces and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-trimspaces-doc
%{_texmfdistdir}/doc/latex/trimspaces/README
%{_texmfdistdir}/doc/latex/trimspaces/trimspaces.pdf

%files -n texlive-trimspaces
%{_texmfdistdir}/tex/latex/trimspaces/trimspaces.sty

%package -n texlive-trivfloat
Version:        %{texlive_version}.%{texlive_noarch}.1.3bsvn15878
Release:        0
License:        LPPL-1.0
Summary:        Quick float definitions in LaTeX
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-trivfloat-doc >= %{texlive_version}
Provides:       tex(trivfloat.sty)
Requires:       tex(float.sty)
Requires:       tex(floatrow.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source246:      trivfloat.tar.xz
Source247:      trivfloat.doc.tar.xz

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
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-trivfloat and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-trivfloat-doc
%{_texmfdistdir}/doc/latex/trivfloat/README
%{_texmfdistdir}/doc/latex/trivfloat/trivfloat.pdf

%files -n texlive-trivfloat
%{_texmfdistdir}/tex/latex/trivfloat/trivfloat.sty

%package -n texlive-trivialpursuit
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1.1svn68971
Release:        0
License:        LPPL-1.0
Summary:        Insert Trivial Pursuit boarding game
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-trivialpursuit-doc >= %{texlive_version}
Provides:       tex(TrivialPursuit.sty)
Requires:       tex(calc.sty)
Requires:       tex(fontawesome5.sty)
Requires:       tex(listofitems.sty)
Requires:       tex(simplekv.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xintexpr.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source248:      trivialpursuit.tar.xz
Source249:      trivialpursuit.doc.tar.xz

%description -n texlive-trivialpursuit
This is a package to display a Trivial Pursuit board game, with
customization.

%package -n texlive-trivialpursuit-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1.1svn68971
Release:        0
Summary:        Documentation for texlive-trivialpursuit
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-trivialpursuit and texlive-alldocumentation)
Provides:       locale(texlive-trivialpursuit-doc:fr)

%description -n texlive-trivialpursuit-doc
This package includes the documentation for texlive-trivialpursuit

%post -n texlive-trivialpursuit
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-trivialpursuit
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-trivialpursuit
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-trivialpursuit-doc
%{_texmfdistdir}/doc/latex/trivialpursuit/README.md
%{_texmfdistdir}/doc/latex/trivialpursuit/TrivialPursuit-doc-en.pdf
%{_texmfdistdir}/doc/latex/trivialpursuit/TrivialPursuit-doc-en.tex
%{_texmfdistdir}/doc/latex/trivialpursuit/TrivialPursuit-doc-fr.pdf
%{_texmfdistdir}/doc/latex/trivialpursuit/TrivialPursuit-doc-fr.tex

%files -n texlive-trivialpursuit
%{_texmfdistdir}/tex/latex/trivialpursuit/TrivialPursuit.sty

%package -n texlive-trsym
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn18732
Release:        0
License:        LPPL-1.0
Summary:        Symbols for transformations
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-trsym-doc >= %{texlive_version}
Provides:       tex(trsy10.tfm)
Provides:       tex(trsy12.tfm)
Provides:       tex(trsym.sty)
Provides:       tex(utrsy.fd)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source250:      trsym.tar.xz
Source251:      trsym.doc.tar.xz

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
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-trsym and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-trsym-doc
%{_texmfdistdir}/doc/latex/trsym/README
%{_texmfdistdir}/doc/latex/trsym/manifest.txt
%{_texmfdistdir}/doc/latex/trsym/trsym.pdf

%files -n texlive-trsym
%{_texmfdistdir}/fonts/source/public/trsym/trsy.mf
%{_texmfdistdir}/fonts/source/public/trsym/trsy10.mf
%{_texmfdistdir}/fonts/source/public/trsym/trsy12.mf
%{_texmfdistdir}/fonts/tfm/public/trsym/trsy10.tfm
%{_texmfdistdir}/fonts/tfm/public/trsym/trsy12.tfm
%{_texmfdistdir}/tex/latex/trsym/trsym.sty
%{_texmfdistdir}/tex/latex/trsym/utrsy.fd

%package -n texlive-truncate
Version:        %{texlive_version}.%{texlive_noarch}.3.6svn18921
Release:        0
License:        SUSE-Public-Domain
Summary:        Truncate text to a specified width
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-truncate-doc >= %{texlive_version}
Provides:       tex(truncate.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source252:      truncate.tar.xz
Source253:      truncate.doc.tar.xz

%description -n texlive-truncate
The package will by default break at word boundaries, but
package options are offered to permit breaks within words.

%package -n texlive-truncate-doc
Version:        %{texlive_version}.%{texlive_noarch}.3.6svn18921
Release:        0
Summary:        Documentation for texlive-truncate
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-truncate and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-truncate-doc
%{_texmfdistdir}/doc/latex/truncate/miscdoc.sty
%{_texmfdistdir}/doc/latex/truncate/truncate.pdf
%{_texmfdistdir}/doc/latex/truncate/truncate.tex

%files -n texlive-truncate
%{_texmfdistdir}/tex/latex/truncate/truncate.sty

%package -n texlive-truthtable
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1.0svn68300
Release:        0
License:        LPPL-1.0
Summary:        Automatically generate truth tables for given variables and statements
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-truthtable-doc >= %{texlive_version}
Provides:       tex(truthtable.sty)
Requires:       tex(luacode.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source254:      truthtable.tar.xz
Source255:      truthtable.doc.tar.xz

%description -n texlive-truthtable
This LuaLaTeX package permits to automatically generate truth
tables given a table header. It supports a number of logical
operations which can be combined as needed. It is built upon
the luacode package.

%package -n texlive-truthtable-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1.0svn68300
Release:        0
Summary:        Documentation for texlive-truthtable
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-truthtable and texlive-alldocumentation)

%description -n texlive-truthtable-doc
This package includes the documentation for texlive-truthtable

%post -n texlive-truthtable
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-truthtable
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-truthtable
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-truthtable-doc
%{_texmfdistdir}/doc/lualatex/truthtable/README.md
%{_texmfdistdir}/doc/lualatex/truthtable/res/exampletable.tex
%{_texmfdistdir}/doc/lualatex/truthtable/res/exampletableoutput.tex
%{_texmfdistdir}/doc/lualatex/truthtable/truthtable.pdf
%{_texmfdistdir}/doc/lualatex/truthtable/truthtable.tex

%files -n texlive-truthtable
%{_texmfdistdir}/tex/lualatex/truthtable/truthtable.sty

%package -n texlive-tsemlines
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn23440
Release:        0
License:        SUSE-Public-Domain
Summary:        Support for the ancient \emline macro
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source256:      tsemlines.tar.xz

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tsemlines
%{_texmfdistdir}/tex/latex/tsemlines/tsemlines.sty

%package -n texlive-tsvtemplate
Version:        %{texlive_version}.%{texlive_noarch}.2022_1.0svn65333
Release:        0
License:        LPPL-1.0
Summary:        Apply a template to a tsv file
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tsvtemplate-doc >= %{texlive_version}
Provides:       tex(tsvtemplate.sty)
Provides:       tex(tsvtemplate.tex)
Requires:       tex(environ.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source257:      tsvtemplate.tar.xz
Source258:      tsvtemplate.doc.tar.xz

%description -n texlive-tsvtemplate
This is a simple tsv (tab-separated values) reader for LuaLaTeX
and plain LuaTeX. It also supports (non-quoted) comma-separated
values, or indeed values separated by any character.

%package -n texlive-tsvtemplate-doc
Version:        %{texlive_version}.%{texlive_noarch}.2022_1.0svn65333
Release:        0
Summary:        Documentation for texlive-tsvtemplate
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tsvtemplate and texlive-alldocumentation)

%description -n texlive-tsvtemplate-doc
This package includes the documentation for texlive-tsvtemplate

%post -n texlive-tsvtemplate
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tsvtemplate
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tsvtemplate
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tsvtemplate-doc
%{_texmfdistdir}/doc/luatex/tsvtemplate/LICENSE
%{_texmfdistdir}/doc/luatex/tsvtemplate/README
%{_texmfdistdir}/doc/luatex/tsvtemplate/tsvtemplate.doc
%{_texmfdistdir}/doc/luatex/tsvtemplate/tsvtemplate.pdf

%files -n texlive-tsvtemplate
%{_texmfdistdir}/tex/luatex/tsvtemplate/tsvtemplate.sty
%{_texmfdistdir}/tex/luatex/tsvtemplate/tsvtemplate.tex

%package -n texlive-ttfutils
Version:        %{texlive_version}.%{texlive_noarch}.svn70015
Release:        0
License:        LPPL-1.0
Summary:        Convert TrueType to TFM and PK fonts
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-ttfutils-bin >= %{texlive_version}
#!BuildIgnore: texlive-ttfutils-bin
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-ttfutils-doc >= %{texlive_version}
Provides:       tex(T1-WGL4.enc)
Provides:       tex(ttf2pk.cfg)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source259:      ttfutils.tar.xz
Source260:      ttfutils.doc.tar.xz

%description -n texlive-ttfutils
Utilities: ttf2afm ttf2pk ttf2tfm ttfdump. FreeType is the
underlying library.

%package -n texlive-ttfutils-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn70015
Release:        0
Summary:        Documentation for texlive-ttfutils
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-ttfutils and texlive-alldocumentation)
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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-ttfutils-doc
%{_mandir}/man1/ttf2afm.1*
%{_mandir}/man1/ttf2pk.1*
%{_mandir}/man1/ttf2tfm.1*
%{_mandir}/man1/ttfdump.1*
%{_texmfdistdir}/doc/ttf2pk/ttf2pk.doc
%{_texmfdistdir}/doc/ttf2pk/ttf2pk.txt
%{_texmfdistdir}/doc/ttf2pk/ttf2tfm.txt

%files -n texlive-ttfutils
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

%package -n texlive-tucv
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn20680
Release:        0
License:        LPPL-1.0
Summary:        Support for typesetting a CV or resumee
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tucv-doc >= %{texlive_version}
Provides:       tex(tucv.sty)
Requires:       tex(array.sty)
Requires:       tex(calc.sty)
Requires:       tex(color.sty)
Requires:       tex(fancyhdr.sty)
Requires:       tex(xparse.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source261:      tucv.tar.xz
Source262:      tucv.doc.tar.xz

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
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tucv and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tucv-doc
%{_texmfdistdir}/doc/latex/tucv/README
%{_texmfdistdir}/doc/latex/tucv/tucv.pdf
%{_texmfdistdir}/doc/latex/tucv/tucv_ex.pdf
%{_texmfdistdir}/doc/latex/tucv/tucv_ex.tex

%files -n texlive-tucv
%{_texmfdistdir}/tex/latex/tucv/tucv.sty

%package -n texlive-tuda-ci
Version:        %{texlive_version}.%{texlive_noarch}.3.36svn69351
Release:        0
License:        LPPL-1.0
Summary:        LaTeX templates of Technische Universitat Darmstadt
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tuda-ci-doc >= %{texlive_version}
Provides:       tex(beamercolorthemeTUDa.sty)
Provides:       tex(beamercolorthemeTUDa2023.sty)
Provides:       tex(beamerfontthemeTUDa.sty)
Provides:       tex(beamerfontthemeTUDa2023.sty)
Provides:       tex(beamerinnerthemeTUDa.sty)
Provides:       tex(beamerinnerthemeTUDa2008.sty)
Provides:       tex(beamerinnerthemeTUDa2023.sty)
Provides:       tex(beamerouterthemeTUDa.sty)
Provides:       tex(beamerouterthemeTUDa2023.sty)
Provides:       tex(beamerthemeTUDa-mecheng.sty)
Provides:       tex(beamerthemeTUDa.sty)
Provides:       tex(beamerthemeTUDa2008.sty)
Provides:       tex(beamerthemeTUDa2023.sty)
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
Provides:       tex(tudamecheng.cfg)
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
Requires:       tex(fontspec.sty)
Requires:       tex(geometry.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(iftex.sty)
Requires:       tex(inputenc.sty)
Requires:       tex(leaflet.cls)
Requires:       tex(luainputenc.sty)
Requires:       tex(microtype.sty)
Requires:       tex(multicol.sty)
Requires:       tex(pdfx.sty)
Requires:       tex(pgf.sty)
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
Requires:       tex(scrletter.cls)
Requires:       tex(scrlfile.sty)
Requires:       tex(tcolorbox.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(tikz.sty)
Requires:       tex(trimclip.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xparse.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source263:      tuda-ci.tar.xz
Source264:      tuda-ci.doc.tar.xz

%description -n texlive-tuda-ci
The TUDa-CI-Bundle provides a possibility to use the Corporate
Design of TU Darmstadt in LaTeX. It contains documentclasses as
well as some helper packages and config files together with
some templates for user documentation, which currently are only
available in German.

%package -n texlive-tuda-ci-doc
Version:        %{texlive_version}.%{texlive_noarch}.3.36svn69351
Release:        0
Summary:        Documentation for texlive-tuda-ci
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tuda-ci and texlive-alldocumentation)
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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tuda-ci-doc
%{_texmfdistdir}/doc/latex/tuda-ci/DEMO-TUDaAnnouncement.pdf
%{_texmfdistdir}/doc/latex/tuda-ci/DEMO-TUDaAnnouncement.tex
%{_texmfdistdir}/doc/latex/tuda-ci/DEMO-TUDaBeamer.pdf
%{_texmfdistdir}/doc/latex/tuda-ci/DEMO-TUDaBeamer.tex
%{_texmfdistdir}/doc/latex/tuda-ci/DEMO-TUDaBeamer2023.pdf
%{_texmfdistdir}/doc/latex/tuda-ci/DEMO-TUDaBeamer2023.tex
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
%{_texmfdistdir}/tex/latex/tuda-ci/beamercolorthemeTUDa.sty
%{_texmfdistdir}/tex/latex/tuda-ci/beamercolorthemeTUDa2023.sty
%{_texmfdistdir}/tex/latex/tuda-ci/beamerfontthemeTUDa.sty
%{_texmfdistdir}/tex/latex/tuda-ci/beamerfontthemeTUDa2023.sty
%{_texmfdistdir}/tex/latex/tuda-ci/beamerinnerthemeTUDa.sty
%{_texmfdistdir}/tex/latex/tuda-ci/beamerinnerthemeTUDa2008.sty
%{_texmfdistdir}/tex/latex/tuda-ci/beamerinnerthemeTUDa2023.sty
%{_texmfdistdir}/tex/latex/tuda-ci/beamerouterthemeTUDa.sty
%{_texmfdistdir}/tex/latex/tuda-ci/beamerouterthemeTUDa2023.sty
%{_texmfdistdir}/tex/latex/tuda-ci/beamerthemeTUDa-mecheng.sty
%{_texmfdistdir}/tex/latex/tuda-ci/beamerthemeTUDa.sty
%{_texmfdistdir}/tex/latex/tuda-ci/beamerthemeTUDa2008.sty
%{_texmfdistdir}/tex/latex/tuda-ci/beamerthemeTUDa2023.sty
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
%{_texmfdistdir}/tex/latex/tuda-ci/tudamecheng.cfg
%{_texmfdistdir}/tex/latex/tuda-ci/tudaposter.cls
%{_texmfdistdir}/tex/latex/tuda-ci/tudapub.cls
%{_texmfdistdir}/tex/latex/tuda-ci/tudarules.sty
%{_texmfdistdir}/tex/latex/tuda-ci/tudasciposter.cls
%{_texmfdistdir}/tex/latex/tuda-ci/tudasize9pt.clo
%{_texmfdistdir}/tex/latex/tuda-ci/tudathesis.cfg

%package -n texlive-tudscr
Version:        %{texlive_version}.%{texlive_noarch}.2.06osvn64085
Release:        0
License:        LPPL-1.0
Summary:        Corporate Design of Technische Universitat Dresden
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
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
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tudscr-doc >= %{texlive_version}
Provides:       tex(fix-tudscrfonts.sty)
Provides:       tex(mathswap.sty)
Provides:       tex(tudscr-gitinfo.sty)
Provides:       tex(tudscrartcl.cls)
Provides:       tex(tudscrbase.sty)
Provides:       tex(tudscrbook.cls)
Provides:       tex(tudscrcolor.sty)
Provides:       tex(tudscrcomp.sty)
Provides:       tex(tudscrdoc.cls)
Provides:       tex(tudscrfonts.sty)
Provides:       tex(tudscrmanual.cls)
Provides:       tex(tudscrmanual.sty)
Provides:       tex(tudscrposter.cls)
Provides:       tex(tudscrreprt.cls)
Provides:       tex(tudscrsupervisor.sty)
Provides:       tex(twocolfix.sty)
Requires:       tex(auto-pst-pdf.sty)
Requires:       tex(babel.sty)
Requires:       tex(bm.sty)
Requires:       tex(bookmark.sty)
Requires:       tex(booktabs.sty)
Requires:       tex(calc.sty)
Requires:       tex(caption.sty)
Requires:       tex(csquotes.sty)
Requires:       tex(ellipsis.sty)
Requires:       tex(enumitem.sty)
Requires:       tex(environ.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(filemod.sty)
Requires:       tex(floatrow.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(geometry.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hologo.sty)
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
Requires:       tex(scrlfile.sty)
Requires:       tex(scrwfile.sty)
Requires:       tex(setspace.sty)
Requires:       tex(shellesc.sty)
Requires:       tex(tabularx.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(tikz.sty)
Requires:       tex(todonotes.sty)
Requires:       tex(trimspaces.sty)
Requires:       tex(units.sty)
Requires:       tex(url.sty)
Requires:       tex(varioref.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xpatch.sty)
Requires:       tex(xspace.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source265:      tudscr.tar.xz
Source266:      tudscr.doc.tar.xz

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
Version:        %{texlive_version}.%{texlive_noarch}.2.06osvn64085
Release:        0
Summary:        Documentation for texlive-tudscr
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tudscr and texlive-alldocumentation)
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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tudscr-doc
%{_texmfdistdir}/doc/latex/tudscr/LICENSE.md
%{_texmfdistdir}/doc/latex/tudscr/README.md
%{_texmfdistdir}/doc/latex/tudscr/tudscr.pdf
%{_texmfdistdir}/doc/latex/tudscr/tudscr_print.pdf
%{_texmfdistdir}/doc/latex/tudscr/tudscrsource.pdf
%{_texmfdistdir}/doc/latex/tudscr/tutorials/mathswap.pdf
%{_texmfdistdir}/doc/latex/tudscr/tutorials/mathtype.pdf
%{_texmfdistdir}/doc/latex/tudscr/tutorials/treatise.pdf

%files -n texlive-tudscr
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
%{_texmfdistdir}/tex/latex/tudscr/tudscr-gitinfo.sty
%{_texmfdistdir}/tex/latex/tudscr/tudscrartcl.cls
%{_texmfdistdir}/tex/latex/tudscr/tudscrbase.sty
%{_texmfdistdir}/tex/latex/tudscr/tudscrbook.cls
%{_texmfdistdir}/tex/latex/tudscr/tudscrcolor.sty
%{_texmfdistdir}/tex/latex/tudscr/tudscrcomp.sty
%{_texmfdistdir}/tex/latex/tudscr/tudscrdoc.cls
%{_texmfdistdir}/tex/latex/tudscr/tudscrfonts.sty
%{_texmfdistdir}/tex/latex/tudscr/tudscrmanual.cls
%{_texmfdistdir}/tex/latex/tudscr/tudscrmanual.sty
%{_texmfdistdir}/tex/latex/tudscr/tudscrposter.cls
%{_texmfdistdir}/tex/latex/tudscr/tudscrreprt.cls
%{_texmfdistdir}/tex/latex/tudscr/tudscrsupervisor.sty
%{_texmfdistdir}/tex/latex/tudscr/twocolfix.sty

%package -n texlive-tufte-latex
Version:        %{texlive_version}.%{texlive_noarch}.3.5.2svn37649
Release:        0
License:        Apache-1.0
Summary:        Document classes inspired by the work of Edward Tufte
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
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
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tufte-latex-doc >= %{texlive_version}
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
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source267:      tufte-latex.tar.xz
Source268:      tufte-latex.doc.tar.xz

%description -n texlive-tufte-latex
Provided are two classes inspired, respectively, by handouts
and books created by Edward Tufte.

%package -n texlive-tufte-latex-doc
Version:        %{texlive_version}.%{texlive_noarch}.3.5.2svn37649
Release:        0
Summary:        Documentation for texlive-tufte-latex
License:        Apache-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tufte-latex and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tufte-latex-doc
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
%{_texmfdistdir}/bibtex/bst/tufte-latex/tufte.bst
%{_texmfdistdir}/tex/latex/tufte-latex/tufte-book.cls
%{_texmfdistdir}/tex/latex/tufte-latex/tufte-common.def
%{_texmfdistdir}/tex/latex/tufte-latex/tufte-handout.cls

%package -n texlive-tugboat
Version:        %{texlive_version}.%{texlive_noarch}.2.31svn68694
Release:        0
License:        LPPL-1.0
Summary:        LaTeX macros for TUGboat articles
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tugboat-doc >= %{texlive_version}
Provides:       tex(ltugboat.cls)
Provides:       tex(ltugboat.sty)
Provides:       tex(ltugcomn.sty)
Provides:       tex(ltugproc.cls)
Provides:       tex(ltugproc.sty)
Requires:       tex(article.cls)
Requires:       tex(gettitlestring.sty)
Requires:       tex(mflogo.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source269:      tugboat.tar.xz
Source270:      tugboat.doc.tar.xz

%description -n texlive-tugboat
Provides ltugboat.cls for both regular and proceedings issues
of the TUGboat journal. Also provides a BibTeX style,
tugboat.bst.

%package -n texlive-tugboat-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.31svn68694
Release:        0
Summary:        Documentation for texlive-tugboat
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tugboat and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tugboat-doc
%{_texmfdistdir}/doc/latex/tugboat/NEWS
%{_texmfdistdir}/doc/latex/tugboat/README
%{_texmfdistdir}/doc/latex/tugboat/ltubguid.ltx
%{_texmfdistdir}/doc/latex/tugboat/ltubguid.pdf
%{_texmfdistdir}/doc/latex/tugboat/manifest.txt
%{_texmfdistdir}/doc/latex/tugboat/tugboat-code.pdf

%files -n texlive-tugboat
%{_texmfdistdir}/bibtex/bst/tugboat/ltugbib.bst
%{_texmfdistdir}/bibtex/bst/tugboat/tugboat.bst
%{_texmfdistdir}/tex/latex/tugboat/ltugboat.cls
%{_texmfdistdir}/tex/latex/tugboat/ltugboat.sty
%{_texmfdistdir}/tex/latex/tugboat/ltugcomn.sty
%{_texmfdistdir}/tex/latex/tugboat/ltugproc.cls
%{_texmfdistdir}/tex/latex/tugboat/ltugproc.sty

%package -n texlive-tugboat-plain
Version:        %{texlive_version}.%{texlive_noarch}.1.29svn68695
Release:        0
License:        LPPL-1.0
Summary:        Plain TeX macros for TUGboat
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tugboat-plain-doc >= %{texlive_version}
Provides:       tex(tugboat.sty)
Provides:       tex(tugproc.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source271:      tugboat-plain.tar.xz
Source272:      tugboat-plain.doc.tar.xz

%description -n texlive-tugboat-plain
The macros defined in this directory (in files tugboat.sty and
tugboat.cmn) are used in papers written in Plain TeX for
publication in TUGboat.

%package -n texlive-tugboat-plain-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.29svn68695
Release:        0
Summary:        Documentation for texlive-tugboat-plain
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tugboat-plain and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tugboat-plain-doc
%{_texmfdistdir}/doc/plain/tugboat-plain/README
%{_texmfdistdir}/doc/plain/tugboat-plain/tubguide.pdf
%{_texmfdistdir}/doc/plain/tugboat-plain/tubguide.tex

%files -n texlive-tugboat-plain
%{_texmfdistdir}/tex/plain/tugboat-plain/tugboat.cmn
%{_texmfdistdir}/tex/plain/tugboat-plain/tugboat.sty
%{_texmfdistdir}/tex/plain/tugboat-plain/tugproc.sty

%package -n texlive-tui
Version:        %{texlive_version}.%{texlive_noarch}.1.9svn27253
Release:        0
License:        LPPL-1.0
Summary:        Thesis style for the University of the Andes, Colombia
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tui-doc >= %{texlive_version}
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
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source273:      tui.tar.xz
Source274:      tui.doc.tar.xz

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
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tui and texlive-alldocumentation)
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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tui-doc
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
%{_texmfdistdir}/tex/latex/tui/tui.cls

%package -n texlive-turabian
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1.0svn36298
Release:        0
License:        LPPL-1.0
Summary:        Create Turabian-formatted material using LaTeX
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-turabian-doc >= %{texlive_version}
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
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source275:      turabian.tar.xz
Source276:      turabian.doc.tar.xz

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
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-turabian and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-turabian-doc
%{_texmfdistdir}/doc/latex/turabian/README
%{_texmfdistdir}/doc/latex/turabian/turabian.tex
%{_texmfdistdir}/doc/latex/turabian/userguide.txt

%files -n texlive-turabian
%{_texmfdistdir}/tex/latex/turabian/turabian.cls

%package -n texlive-turabian-formatting
Version:        %{texlive_version}.%{texlive_noarch}.svn58561
Release:        0
License:        LPPL-1.0
Summary:        Formatting based on Turabian's Manual
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-turabian-formatting-doc >= %{texlive_version}
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
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source277:      turabian-formatting.tar.xz
Source278:      turabian-formatting.doc.tar.xz

%description -n texlive-turabian-formatting
The turabian-formatting package provides Chicago-style
formatting based on Kate L. Turabian's "A Manual for Writers of
Research Papers, Theses, and Dissertations: Chicago Style for
Students and Researchers" (9th edition).

%package -n texlive-turabian-formatting-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn58561
Release:        0
Summary:        Documentation for texlive-turabian-formatting
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-turabian-formatting and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-turabian-formatting-doc
%{_texmfdistdir}/doc/latex/turabian-formatting/README
%{_texmfdistdir}/doc/latex/turabian-formatting/turabian-formatting-doc.pdf
%{_texmfdistdir}/doc/latex/turabian-formatting/turabian-formatting-doc.tex

%files -n texlive-turabian-formatting
%{_texmfdistdir}/tex/latex/turabian-formatting/turabian-formatting.sty
%{_texmfdistdir}/tex/latex/turabian-formatting/turabian-researchpaper.cls
%{_texmfdistdir}/tex/latex/turabian-formatting/turabian-thesis.cls

%package -n texlive-turkmen
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2svn17748
Release:        0
License:        LPPL-1.0
Summary:        Babel support for Turkmen
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-turkmen-doc >= %{texlive_version}
Provides:       tex(turkmen.ldf)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source279:      turkmen.tar.xz
Source280:      turkmen.doc.tar.xz

%description -n texlive-turkmen
The package provides support for Turkmen in babel, but
integration with babel is not available.

%package -n texlive-turkmen-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2svn17748
Release:        0
Summary:        Documentation for texlive-turkmen
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-turkmen and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-turkmen-doc
%{_texmfdistdir}/doc/latex/turkmen/README
%{_texmfdistdir}/doc/latex/turkmen/turkmen.pdf

%files -n texlive-turkmen
%{_texmfdistdir}/tex/latex/turkmen/turkmen.ldf

%package -n texlive-turnstile
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn64967
Release:        0
License:        LPPL-1.0
Summary:        Typeset the (logic) turnstile notation
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-turnstile-doc >= %{texlive_version}
Provides:       tex(turnstile.sty)
Requires:       tex(ifthen.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source281:      turnstile.tar.xz
Source282:      turnstile.doc.tar.xz

%description -n texlive-turnstile
Among other uses, the turnstile sign is used by logicians for
denoting a consequence relation, related to a given logic,
between a collection of formulas and a derived formula.

%package -n texlive-turnstile-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn64967
Release:        0
Summary:        Documentation for texlive-turnstile
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-turnstile and texlive-alldocumentation)
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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-turnstile-doc
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
%{_texmfdistdir}/tex/latex/turnstile/turnstile.sty

%package -n texlive-turnthepage
Version:        %{texlive_version}.%{texlive_noarch}.1.3asvn29803
Release:        0
License:        LPPL-1.0
Summary:        Provide "turn page" instructions
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-turnthepage-doc >= %{texlive_version}
Provides:       tex(turnpageetex.sty)
Provides:       tex(turnpagewoetex.sty)
Provides:       tex(turnthepage.sty)
Requires:       tex(alphalph.sty)
Requires:       tex(atbegshi.sty)
Requires:       tex(pageslts.sty)
Requires:       tex(picture.sty)
Requires:       tex(zref-abspage.sty)
Requires:       tex(zref-lastpage.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source283:      turnthepage.tar.xz
Source284:      turnthepage.doc.tar.xz

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
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-turnthepage and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-turnthepage-doc
%{_texmfdistdir}/doc/latex/turnthepage/Makefile
%{_texmfdistdir}/doc/latex/turnthepage/README
%{_texmfdistdir}/doc/latex/turnthepage/perso.ist
%{_texmfdistdir}/doc/latex/turnthepage/turnthepage-bib.bib
%{_texmfdistdir}/doc/latex/turnthepage/turnthepage.pdf
%{_texmfdistdir}/doc/latex/turnthepage/turnthepage.tex

%files -n texlive-turnthepage
%{_texmfdistdir}/tex/latex/turnthepage/turnpageetex.sty
%{_texmfdistdir}/tex/latex/turnthepage/turnpagewoetex.sty
%{_texmfdistdir}/tex/latex/turnthepage/turnthepage.sty

%package -n texlive-tutodoc
Version:        %{texlive_version}.%{texlive_noarch}.1.1.0svn69343
Release:        0
License:        GPL-2.0-or-later
Summary:        Typeset tutorial-like documentations
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tutodoc-doc >= %{texlive_version}
Provides:       tex(tutodoc-locale-main-english.cfg.sty)
Provides:       tex(tutodoc-locale-main-french.cfg.sty)
Provides:       tex(tutodoc.sty)
Requires:       tex(amsthm.sty)
Requires:       tex(clrstrip.sty)
Requires:       tex(csquotes.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(marginnote.sty)
Requires:       tex(tcolorbox.sty)
Requires:       tex(titlesec.sty)
Requires:       tex(tocbasic.sty)
Requires:       tex(xcolor.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source285:      tutodoc.tar.xz
Source286:      tutodoc.doc.tar.xz

%description -n texlive-tutodoc
This package provides some macros to write documentation of
LaTeX packages in a tutorial style.

%package -n texlive-tutodoc-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1.0svn69343
Release:        0
Summary:        Documentation for texlive-tutodoc
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tutodoc and texlive-alldocumentation)
Provides:       locale(texlive-tutodoc-doc:en;fr)

%description -n texlive-tutodoc-doc
This package includes the documentation for texlive-tutodoc

%post -n texlive-tutodoc
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tutodoc
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tutodoc
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tutodoc-doc
%{_texmfdistdir}/doc/latex/tutodoc/MANIFEST.md
%{_texmfdistdir}/doc/latex/tutodoc/README.md
%{_texmfdistdir}/doc/latex/tutodoc/tutodoc-en.pdf
%{_texmfdistdir}/doc/latex/tutodoc/tutodoc-en.tex
%{_texmfdistdir}/doc/latex/tutodoc/tutodoc-fr.pdf
%{_texmfdistdir}/doc/latex/tutodoc/tutodoc-fr.tex

%files -n texlive-tutodoc
%{_texmfdistdir}/tex/latex/tutodoc/tutodoc-locale-main-english.cfg.sty
%{_texmfdistdir}/tex/latex/tutodoc/tutodoc-locale-main-french.cfg.sty
%{_texmfdistdir}/tex/latex/tutodoc/tutodoc.sty

%package -n texlive-twemoji-colr
Version:        %{texlive_version}.%{texlive_noarch}.0.0.7.0svn64854
Release:        0
License:        LPPL-1.0
Summary:        Twemoji font in COLR/CPAL layered format
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-twemoji-colr-doc >= %{texlive_version}
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source287:      twemoji-colr.tar.xz
Source288:      twemoji-colr.doc.tar.xz

%description -n texlive-twemoji-colr
This is a COLR/CPAL-based color OpenType font from the Twemoji
collection of emoji images.

%package -n texlive-twemoji-colr-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.7.0svn64854
Release:        0
Summary:        Documentation for texlive-twemoji-colr
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-twemoji-colr and texlive-alldocumentation)

%description -n texlive-twemoji-colr-doc
This package includes the documentation for texlive-twemoji-colr

%package -n texlive-twemoji-colr-fonts
Version:        %{texlive_version}.%{texlive_noarch}.0.0.7.0svn64854
Release:        0
Summary:        Severed fonts for texlive-twemoji-colr
License:        LPPL-1.0
URL:            https://www.tug.org/texlive/
Group:          Productivity/Publishing/TeX/Fonts
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Suggests:       xorg-x11-fonts-core

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-twemoji-colr-fonts

%files -n texlive-twemoji-colr-doc
%{_texmfdistdir}/doc/fonts/twemoji-colr/README.md

%files -n texlive-twemoji-colr
%verify(link) %{_texmfdistdir}/fonts/truetype/public/twemoji-colr/TwemojiMozilla.ttf

%files -n texlive-twemoji-colr-fonts
%dir %{_datadir}/fonts/texlive-twemoji-colr
%{_datadir}/fontconfig/conf.avail/58-texlive-twemoji-colr.conf
%verify(not md5 size mtime) %{_datadir}/fonts/texlive-twemoji-colr/encodings.dir
%verify(not md5 size mtime) %{_datadir}/fonts/texlive-twemoji-colr/fonts.dir
%verify(not md5 size mtime) %{_datadir}/fonts/texlive-twemoji-colr/fonts.scale
%{_datadir}/fonts/texlive-twemoji-colr/TwemojiMozilla.ttf

%package -n texlive-twemojis
Version:        %{texlive_version}.%{texlive_noarch}.1.3.1_twemoji_v14.0.1svn62930
Release:        0
License:        LPPL-1.0
Summary:        Use Twitter's open source emojis through LaTeX commands
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-twemojis-doc >= %{texlive_version}
Provides:       tex(twemojis.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(tikz.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source289:      twemojis.tar.xz
Source290:      twemojis.doc.tar.xz

%description -n texlive-twemojis
This package provides a simple wrapper which allows to use
Twitter's open source emojis through LaTeX commands. This
relies on images, so no fancy unicode-font stuff is needed and
it should work on every installation.

%package -n texlive-twemojis-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.3.1_twemoji_v14.0.1svn62930
Release:        0
Summary:        Documentation for texlive-twemojis
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-twemojis and texlive-alldocumentation)

%description -n texlive-twemojis-doc
This package includes the documentation for texlive-twemojis

%post -n texlive-twemojis
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-twemojis
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-twemojis
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-twemojis-doc
%{_texmfdistdir}/doc/latex/twemojis/README.md
%{_texmfdistdir}/doc/latex/twemojis/twemojis.pdf

%files -n texlive-twemojis
%{_texmfdistdir}/tex/latex/twemojis/all-twemojis.pdf
%{_texmfdistdir}/tex/latex/twemojis/twemojis.sty

%package -n texlive-twoinone
Version:        %{texlive_version}.%{texlive_noarch}.svn17024
Release:        0
License:        SUSE-Public-Domain
Summary:        Print two pages on a single page
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-twoinone-doc >= %{texlive_version}
Provides:       tex(2in1.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source291:      twoinone.tar.xz
Source292:      twoinone.doc.tar.xz

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
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-twoinone and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-twoinone-doc
%{_texmfdistdir}/doc/latex/twoinone/twoinone.pdf
%{_texmfdistdir}/doc/latex/twoinone/twoinone.tex

%files -n texlive-twoinone
%{_texmfdistdir}/tex/latex/twoinone/2in1.sty

%package -n texlive-twoup
Version:        %{texlive_version}.%{texlive_noarch}.1.3svn15878
Release:        0
License:        LPPL-1.0
Summary:        Print two virtual pages on each physical page
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-twoup-doc >= %{texlive_version}
Provides:       tex(twoup.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source293:      twoup.tar.xz
Source294:      twoup.doc.tar.xz

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
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-twoup and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-twoup-doc
%{_texmfdistdir}/doc/latex/twoup/README
%{_texmfdistdir}/doc/latex/twoup/twoup.pdf

%files -n texlive-twoup
%{_texmfdistdir}/tex/latex/twoup/twoup.sty

%package -n texlive-twoxtwogame
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2svn70423
Release:        0
License:        Apache-1.0
Summary:        Visualize 2x2 normal-form games
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-twoxtwogame-doc >= %{texlive_version}
Provides:       tex(twoxtwogame.sty)
Requires:       tex(amsfonts.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(amsthm.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(mathtools.sty)
Requires:       tex(pgfmath-xfp.sty)
Requires:       tex(pgfplots.sty)
Requires:       tex(tikz-3dplot.sty)
Requires:       tex(tikz.sty)
Requires:       tex(tikzscale.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source295:      twoxtwogame.tar.xz
Source296:      twoxtwogame.doc.tar.xz

%description -n texlive-twoxtwogame
This is a package for the visualization of 2x2 normal form
games. The package is based on PGF/TikZ and produces beautiful
vector graphics that are intended for use in scientific
publications. The commands include the creation of graphical
representations of 2x2 games, the visualization of equilibria
in 2x2 games and game embeddings for 2x2 games.

%package -n texlive-twoxtwogame-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2svn70423
Release:        0
Summary:        Documentation for texlive-twoxtwogame
License:        Apache-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-twoxtwogame and texlive-alldocumentation)

%description -n texlive-twoxtwogame-doc
This package includes the documentation for texlive-twoxtwogame

%post -n texlive-twoxtwogame
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-twoxtwogame
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-twoxtwogame
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-twoxtwogame-doc
%{_texmfdistdir}/doc/latex/twoxtwogame/LICENSE
%{_texmfdistdir}/doc/latex/twoxtwogame/README.md
%{_texmfdistdir}/doc/latex/twoxtwogame/twoxtwogame_bibtex.bib
%{_texmfdistdir}/doc/latex/twoxtwogame/twoxtwogame_doc.pdf
%{_texmfdistdir}/doc/latex/twoxtwogame/twoxtwogame_doc.tex

%files -n texlive-twoxtwogame
%{_texmfdistdir}/tex/latex/twoxtwogame/twoxtwogame.sty

%package -n texlive-txfonts
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
License:        GPL-2.0-or-later
Summary:        Times-like fonts in support of mathematics
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-txfonts-doc >= %{texlive_version}
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
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source297:      txfonts.tar.xz
Source298:      txfonts.doc.tar.xz

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
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-txfonts and texlive-alldocumentation)

%description -n texlive-txfonts-doc
This package includes the documentation for texlive-txfonts

%package -n texlive-txfonts-fonts
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Severed fonts for texlive-txfonts
License:        GPL-2.0-or-later
URL:            https://www.tug.org/texlive/
Group:          Productivity/Publishing/TeX/Fonts
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Suggests:       xorg-x11-fonts-core

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-txfonts-fonts

%files -n texlive-txfonts-doc
%{_texmfdistdir}/doc/fonts/txfonts/00bug_fix.txt
%{_texmfdistdir}/doc/fonts/txfonts/COPYRIGHT
%{_texmfdistdir}/doc/fonts/txfonts/README
%{_texmfdistdir}/doc/fonts/txfonts/txfontsdoc.pdf
%{_texmfdistdir}/doc/fonts/txfonts/txfontsdoc.tex
%{_texmfdistdir}/doc/fonts/txfonts/txfontsdocA4.pdf
%{_texmfdistdir}/doc/fonts/txfonts/txfontsdocA4.tex
%{_texmfdistdir}/doc/fonts/txfonts/txmi.vpl

%files -n texlive-txfonts
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
%dir %{_datadir}/fonts/texlive-txfonts
%{_datadir}/fontconfig/conf.avail/58-texlive-txfonts.conf
%verify(not md5 size mtime) %{_datadir}/fonts/texlive-txfonts/encodings.dir
%verify(not md5 size mtime) %{_datadir}/fonts/texlive-txfonts/fonts.dir
%verify(not md5 size mtime) %{_datadir}/fonts/texlive-txfonts/fonts.scale
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

%package -n texlive-txfontsb
Version:        %{texlive_version}.%{texlive_noarch}.1.1.1svn54512
Release:        0
License:        GPL-2.0-or-later
Summary:        Extensions to txfonts, using GNU Freefont
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-txfontsb-doc >= %{texlive_version}
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
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source299:      txfontsb.tar.xz
Source300:      txfontsb.doc.tar.xz

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
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-txfontsb and texlive-alldocumentation)

%description -n texlive-txfontsb-doc
This package includes the documentation for texlive-txfontsb

%package -n texlive-txfontsb-fonts
Version:        %{texlive_version}.%{texlive_noarch}.1.1.1svn54512
Release:        0
Summary:        Severed fonts for texlive-txfontsb
License:        GPL-2.0-or-later
URL:            https://www.tug.org/texlive/
Group:          Productivity/Publishing/TeX/Fonts
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Suggests:       xorg-x11-fonts-core

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-txfontsb-fonts

%files -n texlive-txfontsb-doc
%{_texmfdistdir}/doc/fonts/txfontsb/README
%{_texmfdistdir}/doc/fonts/txfontsb/txfontsb.pdf
%{_texmfdistdir}/doc/fonts/txfontsb/txfontsb.tex

%files -n texlive-txfontsb
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
%dir %{_datadir}/fonts/texlive-txfontsb
%{_datadir}/fontconfig/conf.avail/58-texlive-txfontsb.conf
%{_datadir}/fontconfig/conf.avail/55-texlive-txfontsb.conf
%config %{_sysconfdir}/fonts/conf.d/55-texlive-txfontsb.conf
%verify(not md5 size mtime) %{_datadir}/fonts/texlive-txfontsb/encodings.dir
%verify(not md5 size mtime) %{_datadir}/fonts/texlive-txfontsb/fonts.dir
%verify(not md5 size mtime) %{_datadir}/fonts/texlive-txfontsb/fonts.scale
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

%package -n texlive-txgreeks
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn21839
Release:        0
License:        LPPL-1.0
Summary:        Shape selection for TX fonts Greek letters
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-txgreeks-doc >= %{texlive_version}
Provides:       tex(txgreeks.sty)
Requires:       tex(txfonts.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source301:      txgreeks.tar.xz
Source302:      txgreeks.doc.tar.xz

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
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-txgreeks and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-txgreeks-doc
%{_texmfdistdir}/doc/latex/txgreeks/README
%{_texmfdistdir}/doc/latex/txgreeks/txgreeks.pdf

%files -n texlive-txgreeks
%{_texmfdistdir}/tex/latex/txgreeks/txgreeks.sty

%package -n texlive-txuprcal
Version:        %{texlive_version}.%{texlive_noarch}.1.00svn43327
Release:        0
License:        GPL-2.0-or-later
Summary:        Upright calligraphic font based on TX calligraphic
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-txuprcal-doc >= %{texlive_version}
Provides:       tex(TXUprCal.map)
Provides:       tex(txUprCal-Bold.tfm)
Provides:       tex(txUprCal-Regular.tfm)
Provides:       tex(txuprcal.sty)
Provides:       tex(utxuprcal.fd)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source303:      txuprcal.tar.xz
Source304:      txuprcal.doc.tar.xz

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
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-txuprcal and texlive-alldocumentation)

%description -n texlive-txuprcal-doc
This package includes the documentation for texlive-txuprcal

%package -n texlive-txuprcal-fonts
Version:        %{texlive_version}.%{texlive_noarch}.1.00svn43327
Release:        0
Summary:        Severed fonts for texlive-txuprcal
License:        GPL-2.0-or-later
URL:            https://www.tug.org/texlive/
Group:          Productivity/Publishing/TeX/Fonts
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Suggests:       xorg-x11-fonts-core

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-txuprcal-fonts

%files -n texlive-txuprcal-doc
%{_texmfdistdir}/doc/fonts/txuprcal/README
%{_texmfdistdir}/doc/fonts/txuprcal/txuprcal-doc.pdf
%{_texmfdistdir}/doc/fonts/txuprcal/txuprcal-doc.tex

%files -n texlive-txuprcal
%{_texmfdistdir}/fonts/map/dvips/txuprcal/TXUprCal.map
%{_texmfdistdir}/fonts/tfm/public/txuprcal/txUprCal-Bold.tfm
%{_texmfdistdir}/fonts/tfm/public/txuprcal/txUprCal-Regular.tfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/txuprcal/txuprcal-bold.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/txuprcal/txuprcal-reg.pfb
%{_texmfdistdir}/tex/latex/txuprcal/txuprcal.sty
%{_texmfdistdir}/tex/latex/txuprcal/utxuprcal.fd

%files -n texlive-txuprcal-fonts
%dir %{_datadir}/fonts/texlive-txuprcal
%{_datadir}/fontconfig/conf.avail/58-texlive-txuprcal.conf
%verify(not md5 size mtime) %{_datadir}/fonts/texlive-txuprcal/encodings.dir
%verify(not md5 size mtime) %{_datadir}/fonts/texlive-txuprcal/fonts.dir
%verify(not md5 size mtime) %{_datadir}/fonts/texlive-txuprcal/fonts.scale
%{_datadir}/fonts/texlive-txuprcal/txuprcal-bold.pfb
%{_datadir}/fonts/texlive-txuprcal/txuprcal-reg.pfb

%package -n texlive-type1cm
Version:        %{texlive_version}.%{texlive_noarch}.svn21820
Release:        0
License:        LPPL-1.0
Summary:        Arbitrary size font selection in LaTeX
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-type1cm-doc >= %{texlive_version}
Provides:       tex(type1cm.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source305:      type1cm.tar.xz
Source306:      type1cm.doc.tar.xz

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
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-type1cm and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-type1cm-doc
%{_texmfdistdir}/doc/latex/type1cm/type1cm-doc.pdf
%{_texmfdistdir}/doc/latex/type1cm/type1cm-doc.tex
%{_texmfdistdir}/doc/latex/type1cm/type1cm.txt

%files -n texlive-type1cm
%{_texmfdistdir}/tex/latex/type1cm/type1cm.sty

%package -n texlive-typed-checklist
Version:        %{texlive_version}.%{texlive_noarch}.2.1svn63445
Release:        0
License:        LPPL-1.0
Summary:        Typesetting tasks, goals, milestones, artifacts, and more in LaTeX
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-typed-checklist-doc >= %{texlive_version}
Provides:       tex(typed-checklist.sty)
Requires:       tex(array.sty)
Requires:       tex(asciilist.sty)
Requires:       tex(bbding.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(marginnote.sty)
Requires:       tex(tabularx.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xltabular.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source307:      typed-checklist.tar.xz
Source308:      typed-checklist.doc.tar.xz

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
Version:        %{texlive_version}.%{texlive_noarch}.2.1svn63445
Release:        0
Summary:        Documentation for texlive-typed-checklist
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-typed-checklist and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-typed-checklist-doc
%{_texmfdistdir}/doc/latex/typed-checklist/README.md
%{_texmfdistdir}/doc/latex/typed-checklist/typed-checklist.pdf

%files -n texlive-typed-checklist
%{_texmfdistdir}/tex/latex/typed-checklist/typed-checklist.sty

%package -n texlive-typeface
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn27046
Release:        0
License:        LPPL-1.0
Summary:        Select a balanced set of fonts
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-typeface-doc >= %{texlive_version}
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
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source309:      typeface.tar.xz
Source310:      typeface.doc.tar.xz

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
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-typeface and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-typeface-doc
%{_texmfdistdir}/doc/latex/typeface/README
%{_texmfdistdir}/doc/latex/typeface/typeface-all-rm.pdf
%{_texmfdistdir}/doc/latex/typeface/typeface-test.tex
%{_texmfdistdir}/doc/latex/typeface/typeface.pdf
%{_texmfdistdir}/doc/latex/typeface/typeface.tex

%files -n texlive-typeface
%{_texmfdistdir}/tex/latex/typeface/typeface.cfg
%{_texmfdistdir}/tex/latex/typeface/typeface.sty

%package -n texlive-typehtml
Version:        %{texlive_version}.%{texlive_noarch}.svn17134
Release:        0
License:        LPPL-1.0
Summary:        Typeset HTML directly from LaTeX
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-typehtml-doc >= %{texlive_version}
Provides:       tex(typehtml.sty)
Requires:       tex(exscale.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source311:      typehtml.tar.xz
Source312:      typehtml.doc.tar.xz

%description -n texlive-typehtml
Can handle almost all of HTML2, and most of the math fragment
of the draft HTML3.

%package -n texlive-typehtml-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn17134
Release:        0
Summary:        Documentation for texlive-typehtml
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-typehtml and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-typehtml-doc
%{_texmfdistdir}/doc/latex/typehtml/README
%{_texmfdistdir}/doc/latex/typehtml/typehtml.pdf

%files -n texlive-typehtml
%{_texmfdistdir}/tex/latex/typehtml/typehtml.sty

%package -n texlive-typeoutfileinfo
Version:        %{texlive_version}.%{texlive_noarch}.0.0.32svn67526
Release:        0
License:        LPPL-1.0
Summary:        Display class/package/file information
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires:       texlive-fileinfo >= %{texlive_version}
#!BuildIgnore: texlive-fileinfo
Requires(pre):  texlive-typeoutfileinfo-bin >= %{texlive_version}
#!BuildIgnore: texlive-typeoutfileinfo-bin
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-typeoutfileinfo-doc >= %{texlive_version}
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source313:      typeoutfileinfo.tar.xz
Source314:      typeoutfileinfo.doc.tar.xz

%description -n texlive-typeoutfileinfo
The package provides a minimalist shell script, for Unix
systems, that displays the information content in a
\ProvidesFile, \ProvidesPackage or \ProvidesClass command in a
LaTeX source file. The package requires that the readprov
package is available.

%package -n texlive-typeoutfileinfo-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.32svn67526
Release:        0
Summary:        Documentation for texlive-typeoutfileinfo
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-typeoutfileinfo and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-typeoutfileinfo-doc
%{_texmfdistdir}/doc/support/typeoutfileinfo/README

%files -n texlive-typeoutfileinfo
%{_texmfdistdir}/scripts/typeoutfileinfo/typeoutfileinfo.sh

%package -n texlive-typewriter
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn46641
Release:        0
License:        LPPL-1.0
Summary:        Typeset with a randomly variable monospace font
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-typewriter-doc >= %{texlive_version}
Provides:       tex(typewriter.sty)
Requires:       tex(luaotfload.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source315:      typewriter.tar.xz
Source316:      typewriter.doc.tar.xz

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
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-typewriter and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-typewriter-doc
%{_texmfdistdir}/doc/lualatex/typewriter/README.md
%{_texmfdistdir}/doc/lualatex/typewriter/typewriter-guide.pdf
%{_texmfdistdir}/doc/lualatex/typewriter/typewriter-guide.tex

%files -n texlive-typewriter
%{_texmfdistdir}/tex/lualatex/typewriter/typewriter.sty

%package -n texlive-typicons
Version:        %{texlive_version}.%{texlive_noarch}.2.0.7svn37623
Release:        0
License:        LPPL-1.0
Summary:        Font containing a set of web-related icons
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-typicons-doc >= %{texlive_version}
Provides:       tex(typicons.sty)
Requires:       tex(fontspec.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source317:      typicons.tar.xz
Source318:      typicons.doc.tar.xz

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
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-typicons and texlive-alldocumentation)

%description -n texlive-typicons-doc
This package includes the documentation for texlive-typicons

%package -n texlive-typicons-fonts
Version:        %{texlive_version}.%{texlive_noarch}.2.0.7svn37623
Release:        0
Summary:        Severed fonts for texlive-typicons
License:        LPPL-1.0
URL:            https://www.tug.org/texlive/
Group:          Productivity/Publishing/TeX/Fonts
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Suggests:       xorg-x11-fonts-core

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-typicons-fonts

%files -n texlive-typicons-doc
%{_texmfdistdir}/doc/fonts/typicons/README
%{_texmfdistdir}/doc/fonts/typicons/typicons.pdf
%{_texmfdistdir}/doc/fonts/typicons/typicons.tex

%files -n texlive-typicons
%verify(link) %{_texmfdistdir}/fonts/truetype/public/typicons/typicons.ttf
%{_texmfdistdir}/tex/latex/typicons/typicons.sty

%files -n texlive-typicons-fonts
%dir %{_datadir}/fonts/texlive-typicons
%{_datadir}/fontconfig/conf.avail/58-texlive-typicons.conf
%verify(not md5 size mtime) %{_datadir}/fonts/texlive-typicons/encodings.dir
%verify(not md5 size mtime) %{_datadir}/fonts/texlive-typicons/fonts.dir
%verify(not md5 size mtime) %{_datadir}/fonts/texlive-typicons/fonts.scale
%{_datadir}/fonts/texlive-typicons/typicons.ttf

%package -n texlive-typoaid
Version:        %{texlive_version}.%{texlive_noarch}.0.0.4.7svn44238
Release:        0
License:        LPPL-1.0
Summary:        Macros for font diagnostics
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-typoaid-doc >= %{texlive_version}
Provides:       tex(typoaid.sty)
Requires:       tex(array.sty)
Requires:       tex(booktabs.sty)
Requires:       tex(expl3.sty)
Requires:       tex(siunitx.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source319:      typoaid.tar.xz
Source320:      typoaid.doc.tar.xz

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
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-typoaid and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-typoaid-doc
%{_texmfdistdir}/doc/latex/typoaid/README.md
%{_texmfdistdir}/doc/latex/typoaid/typoaid.pdf
%{_texmfdistdir}/doc/latex/typoaid/typoaid.tex

%files -n texlive-typoaid
%{_texmfdistdir}/tex/latex/typoaid/typoaid.sty

%package -n texlive-typogrid
Version:        %{texlive_version}.%{texlive_noarch}.0.0.21svn24994
Release:        0
License:        LPPL-1.0
Summary:        Print a typographic grid
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-typogrid-doc >= %{texlive_version}
Provides:       tex(typogrid.sty)
Requires:       tex(calc.sty)
Requires:       tex(eso-pic.sty)
Requires:       tex(keyval.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source321:      typogrid.tar.xz
Source322:      typogrid.doc.tar.xz

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
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-typogrid and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-typogrid-doc
%{_texmfdistdir}/doc/latex/typogrid/ChangeLog
%{_texmfdistdir}/doc/latex/typogrid/Makefile
%{_texmfdistdir}/doc/latex/typogrid/README
%{_texmfdistdir}/doc/latex/typogrid/getversion.tex
%{_texmfdistdir}/doc/latex/typogrid/testtypogrid.tex
%{_texmfdistdir}/doc/latex/typogrid/typogrid.pdf

%files -n texlive-typogrid
%{_texmfdistdir}/tex/latex/typogrid/typogrid.sty

%package -n texlive-typstfun
Version:        %{texlive_version}.%{texlive_noarch}.2024asvn70018
Release:        0
License:        LPPL-1.0
Summary:        List of equivalent Typst function names of LaTeX commands
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source323:      typstfun.doc.tar.xz

%description -n texlive-typstfun
This documentation lists equivalent Typst function names of
LaTeX commands. Only math symbols provided by the LaTeX format
or the amsmath bundle are included.

%post -n texlive-typstfun
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-typstfun
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-typstfun
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-typstfun
%{_texmfdistdir}/doc/latex/typstfun/README.txt
%{_texmfdistdir}/doc/latex/typstfun/typstfun.pdf
%{_texmfdistdir}/doc/latex/typstfun/typstfun.sty
%{_texmfdistdir}/doc/latex/typstfun/typstfun.tex

%package -n texlive-tzplot
Version:        %{texlive_version}.%{texlive_noarch}.2.1svn64537
Release:        0
License:        LPPL-1.0
Summary:        Plot graphs with TikZ abbreviations
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-tzplot-doc >= %{texlive_version}
Provides:       tex(tzplot.sty)
Requires:       tex(expl3.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xparse.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source324:      tzplot.tar.xz
Source325:      tzplot.doc.tar.xz

%description -n texlive-tzplot
This is a LaTeX package that provides TikZ-based macros to make
it easy to draw graphs. The macros provided in this package are
just abbreviations for TikZ codes, which can be complicated;
but using the package will hopefully make drawing easier,
especially when drawing repeatedly. The macros were chosen and
developed with an emphasis on drawing graphs in economics. The
package depends on TikZ, xparse, and expl3.

%package -n texlive-tzplot-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.1svn64537
Release:        0
Summary:        Documentation for texlive-tzplot
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-tzplot and texlive-alldocumentation)

%description -n texlive-tzplot-doc
This package includes the documentation for texlive-tzplot

%post -n texlive-tzplot
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-tzplot
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-tzplot
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-tzplot-doc
%{_texmfdistdir}/doc/latex/tzplot/README.txt
%{_texmfdistdir}/doc/latex/tzplot/tzplot-doc-A-v2.1.tex
%{_texmfdistdir}/doc/latex/tzplot/tzplot-doc-B-v2.1.tex
%{_texmfdistdir}/doc/latex/tzplot/tzplot-doc-C-v2.1.tex
%{_texmfdistdir}/doc/latex/tzplot/tzplot-doc-C1-v2.1.tex
%{_texmfdistdir}/doc/latex/tzplot/tzplot-doc-C2-v2.1.tex
%{_texmfdistdir}/doc/latex/tzplot/tzplot-doc-D-v2.1.tex
%{_texmfdistdir}/doc/latex/tzplot/tzplot-doc-E-v2.1.tex
%{_texmfdistdir}/doc/latex/tzplot/tzplot-doc.pdf
%{_texmfdistdir}/doc/latex/tzplot/tzplot-doc.tex
%{_texmfdistdir}/doc/latex/tzplot/tzplot-oblivoirpartstyle.tex
%{_texmfdistdir}/doc/latex/tzplot/tzplot.ist

%files -n texlive-tzplot
%{_texmfdistdir}/tex/latex/tzplot/tzplot.sty

%package -n texlive-uaclasses
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
License:        SUSE-Public-Domain
Summary:        University of Arizona thesis and dissertation format
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-uaclasses-doc >= %{texlive_version}
Provides:       tex(my-thesis.cls)
Provides:       tex(my-title.sty)
Provides:       tex(ua-thesis.cls)
Provides:       tex(ua-title.sty)
Requires:       tex(amsbook.cls)
Requires:       tex(amsfonts.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(amsthm.sty)
Requires:       tex(report.cls)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source326:      uaclasses.tar.xz
Source327:      uaclasses.doc.tar.xz

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
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-uaclasses and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-uaclasses-doc
%{_texmfdistdir}/doc/latex/uaclasses/README
%{_texmfdistdir}/doc/latex/uaclasses/my-example.pdf
%{_texmfdistdir}/doc/latex/uaclasses/ua-example.pdf
%{_texmfdistdir}/doc/latex/uaclasses/ua-example.tex

%files -n texlive-uaclasses
%{_texmfdistdir}/tex/latex/uaclasses/my-thesis.cls
%{_texmfdistdir}/tex/latex/uaclasses/my-title.sty
%{_texmfdistdir}/tex/latex/uaclasses/ua-thesis.cls
%{_texmfdistdir}/tex/latex/uaclasses/ua-title.sty

%package -n texlive-uafthesis
Version:        %{texlive_version}.%{texlive_noarch}.12.12svn57349
Release:        0
License:        LPPL-1.0
Summary:        Document class for theses at University of Alaska Fairbanks
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-uafthesis-doc >= %{texlive_version}
Provides:       tex(uafthesis.cls)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source328:      uafthesis.tar.xz
Source329:      uafthesis.doc.tar.xz

%description -n texlive-uafthesis
This is an "unofficial" official class.

%package -n texlive-uafthesis-doc
Version:        %{texlive_version}.%{texlive_noarch}.12.12svn57349
Release:        0
Summary:        Documentation for texlive-uafthesis
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-uafthesis and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-uafthesis-doc
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
%{_texmfdistdir}/tex/latex/uafthesis/uafthesis.cls

%package -n texlive-uantwerpendocs
Version:        %{texlive_version}.%{texlive_noarch}.4.5svn66819
Release:        0
License:        LPPL-1.0
Summary:        Course texts, master theses, and exams in University of Antwerp style
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-uantwerpendocs-doc >= %{texlive_version}
Provides:       tex(beamercolorthemeuantwerpen.sty)
Provides:       tex(beamerfontthemeuantwerpen.sty)
Provides:       tex(beamerinnerthemeuantwerpen.sty)
Provides:       tex(beamerouterthemeuantwerpen.sty)
Provides:       tex(beamerthemeuantwerpen.sty)
Provides:       tex(uantwerpenbamathesis.cls)
Provides:       tex(uantwerpencolorlogoscheme.sty)
Provides:       tex(uantwerpencommonoptions.clo)
Provides:       tex(uantwerpencoursetext.cls)
Provides:       tex(uantwerpenexam.cls)
Provides:       tex(uantwerpenletter.cls)
Provides:       tex(uantwerpenphdthesis.cls)
Provides:       tex(uantwerpenreport.cls)
Requires:       tex(adjustbox.sty)
Requires:       tex(background.sty)
Requires:       tex(bm.sty)
Requires:       tex(cmbright.sty)
Requires:       tex(color.sty)
Requires:       tex(crop.sty)
Requires:       tex(ean13isbn.sty)
Requires:       tex(environ.sty)
Requires:       tex(eso-pic.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(expl3.sty)
Requires:       tex(fancyhdr.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(geometry.sty)
Requires:       tex(graphbox.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(iftex.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(sansmathaccent.sty)
Requires:       tex(shellesc.sty)
Requires:       tex(soul.sty)
Requires:       tex(tikz.sty)
Requires:       tex(ulem.sty)
Requires:       tex(xparse.sty)
Requires:       tex(xstring.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source330:      uantwerpendocs.tar.xz
Source331:      uantwerpendocs.doc.tar.xz

%description -n texlive-uantwerpendocs
These class files implement the house style of the University
of Antwerp. This package originated from the Faculty of Applied
Engineering. Using these class files will make it easy for you
to make and keep your documents compliant to this version and
future versions of the house style of the University of
Antwerp.

%package -n texlive-uantwerpendocs-doc
Version:        %{texlive_version}.%{texlive_noarch}.4.5svn66819
Release:        0
Summary:        Documentation for texlive-uantwerpendocs
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-uantwerpendocs and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-uantwerpendocs-doc
%{_texmfdistdir}/doc/latex/uantwerpendocs/LICENSE
%{_texmfdistdir}/doc/latex/uantwerpendocs/README
%{_texmfdistdir}/doc/latex/uantwerpendocs/beamerthemeuantwerpenuserguide.pdf
%{_texmfdistdir}/doc/latex/uantwerpendocs/beamerthemeuantwerpenuserguide.tex
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
%{_texmfdistdir}/doc/latex/uantwerpendocs/uantwerpenphdthesis-example1.pdf
%{_texmfdistdir}/doc/latex/uantwerpendocs/uantwerpenphdthesis-example1.tex
%{_texmfdistdir}/doc/latex/uantwerpendocs/uantwerpenphdthesis-example2.pdf
%{_texmfdistdir}/doc/latex/uantwerpendocs/uantwerpenphdthesis-example2.tex
%{_texmfdistdir}/doc/latex/uantwerpendocs/uantwerpenreport-example.pdf
%{_texmfdistdir}/doc/latex/uantwerpendocs/uantwerpenreport-example.tex

%files -n texlive-uantwerpendocs
%{_texmfdistdir}/tex/latex/uantwerpendocs/Images/uantwerpen-01.jpg
%{_texmfdistdir}/tex/latex/uantwerpendocs/Images/uantwerpen-02.jpg
%{_texmfdistdir}/tex/latex/uantwerpendocs/Images/uantwerpen-03.jpg
%{_texmfdistdir}/tex/latex/uantwerpendocs/Images/uantwerpen-04.jpg
%{_texmfdistdir}/tex/latex/uantwerpendocs/Images/uantwerpen-05.jpg
%{_texmfdistdir}/tex/latex/uantwerpendocs/Images/uantwerpen-06.jpg
%{_texmfdistdir}/tex/latex/uantwerpendocs/Images/uantwerpen-07.jpg
%{_texmfdistdir}/tex/latex/uantwerpendocs/Images/uantwerpen-08.jpg
%{_texmfdistdir}/tex/latex/uantwerpendocs/Images/uantwerpen-09.jpg
%{_texmfdistdir}/tex/latex/uantwerpendocs/Images/uantwerpen-10.jpg
%{_texmfdistdir}/tex/latex/uantwerpendocs/Images/uantwerpen-11.jpg
%{_texmfdistdir}/tex/latex/uantwerpendocs/Images/uantwerpen-keyboard.jpg
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/icon-uantwerpen-be-cmyk.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/icon-uantwerpen-be-cmyk.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/icon-uantwerpen-be-rgb.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/icon-uantwerpen-be-rgb.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/icon-uantwerpen-fbd-cmyk.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/icon-uantwerpen-fbd-cmyk.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/icon-uantwerpen-fbd-rgb.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/icon-uantwerpen-fbd-rgb.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/icon-uantwerpen-ggw-cmyk.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/icon-uantwerpen-ggw-cmyk.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/icon-uantwerpen-ggw-rgb.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/icon-uantwerpen-ggw-rgb.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/icon-uantwerpen-iob-cmyk.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/icon-uantwerpen-iob-cmyk.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/icon-uantwerpen-iob-rgb.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/icon-uantwerpen-iob-rgb.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/icon-uantwerpen-lw-cmyk.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/icon-uantwerpen-lw-cmyk.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/icon-uantwerpen-lw-rgb.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/icon-uantwerpen-lw-rgb.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/icon-uantwerpen-ow-cmyk.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/icon-uantwerpen-ow-cmyk.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/icon-uantwerpen-ow-rgb.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/icon-uantwerpen-ow-rgb.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/icon-uantwerpen-re-cmyk.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/icon-uantwerpen-re-cmyk.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/icon-uantwerpen-re-rgb.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/icon-uantwerpen-re-rgb.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/icon-uantwerpen-sw-cmyk.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/icon-uantwerpen-sw-cmyk.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/icon-uantwerpen-sw-rgb.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/icon-uantwerpen-sw-rgb.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/icon-uantwerpen-ti-cmyk.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/icon-uantwerpen-ti-cmyk.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/icon-uantwerpen-ti-rgb.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/icon-uantwerpen-ti-rgb.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/icon-uantwerpen-ua-cmyk.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/icon-uantwerpen-ua-cmyk.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/icon-uantwerpen-ua-rgb.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/icon-uantwerpen-ua-rgb.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/icon-uantwerpen-we-cmyk.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/icon-uantwerpen-we-cmyk.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/icon-uantwerpen-we-rgb.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/icon-uantwerpen-we-rgb.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-be-en-cmyk-mono-white.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-be-en-cmyk-mono-white.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-be-en-cmyk-neg.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-be-en-cmyk-neg.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-be-en-cmyk-pos.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-be-en-cmyk-pos.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-be-en-rgb-mono-white.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-be-en-rgb-mono-white.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-be-en-rgb-neg.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-be-en-rgb-neg.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-be-en-rgb-pos.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-be-en-rgb-pos.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-be-nl-cmyk-mono-white.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-be-nl-cmyk-mono-white.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-be-nl-cmyk-neg.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-be-nl-cmyk-neg.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-be-nl-cmyk-pos.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-be-nl-cmyk-pos.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-be-nl-rgb-mono-white.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-be-nl-rgb-mono-white.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-be-nl-rgb-neg.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-be-nl-rgb-neg.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-be-nl-rgb-pos.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-be-nl-rgb-pos.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-fbd-en-cmyk-mono-white.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-fbd-en-cmyk-mono-white.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-fbd-en-cmyk-neg.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-fbd-en-cmyk-neg.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-fbd-en-cmyk-pos.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-fbd-en-cmyk-pos.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-fbd-en-rgb-mono-white.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-fbd-en-rgb-mono-white.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-fbd-en-rgb-neg.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-fbd-en-rgb-neg.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-fbd-en-rgb-pos.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-fbd-en-rgb-pos.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-fbd-nl-cmyk-mono-white.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-fbd-nl-cmyk-mono-white.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-fbd-nl-cmyk-neg.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-fbd-nl-cmyk-neg.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-fbd-nl-cmyk-pos.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-fbd-nl-cmyk-pos.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-fbd-nl-rgb-mono-white.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-fbd-nl-rgb-mono-white.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-fbd-nl-rgb-neg.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-fbd-nl-rgb-neg.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-fbd-nl-rgb-pos.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-fbd-nl-rgb-pos.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ggw-en-cmyk-mono-white.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ggw-en-cmyk-mono-white.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ggw-en-cmyk-neg.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ggw-en-cmyk-neg.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ggw-en-cmyk-pos.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ggw-en-cmyk-pos.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ggw-en-rgb-mono-white.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ggw-en-rgb-mono-white.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ggw-en-rgb-neg.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ggw-en-rgb-neg.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ggw-en-rgb-pos.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ggw-en-rgb-pos.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ggw-nl-cmyk-mono-white.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ggw-nl-cmyk-mono-white.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ggw-nl-cmyk-neg.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ggw-nl-cmyk-neg.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ggw-nl-cmyk-pos.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ggw-nl-cmyk-pos.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ggw-nl-rgb-mono-white.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ggw-nl-rgb-mono-white.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ggw-nl-rgb-neg.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ggw-nl-rgb-neg.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ggw-nl-rgb-pos.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ggw-nl-rgb-pos.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-iob-en-cmyk-mono-white.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-iob-en-cmyk-mono-white.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-iob-en-cmyk-neg.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-iob-en-cmyk-neg.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-iob-en-cmyk-pos.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-iob-en-cmyk-pos.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-iob-en-rgb-mono-white.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-iob-en-rgb-mono-white.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-iob-en-rgb-neg.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-iob-en-rgb-neg.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-iob-en-rgb-pos.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-iob-en-rgb-pos.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-iob-nl-cmyk-mono-white.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-iob-nl-cmyk-mono-white.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-iob-nl-cmyk-neg.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-iob-nl-cmyk-neg.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-iob-nl-cmyk-pos.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-iob-nl-cmyk-pos.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-iob-nl-rgb-mono-white.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-iob-nl-rgb-mono-white.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-iob-nl-rgb-neg.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-iob-nl-rgb-neg.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-iob-nl-rgb-pos.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-iob-nl-rgb-pos.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-lw-en-cmyk-mono-white.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-lw-en-cmyk-mono-white.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-lw-en-cmyk-neg.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-lw-en-cmyk-neg.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-lw-en-cmyk-pos.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-lw-en-cmyk-pos.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-lw-en-rgb-mono-white.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-lw-en-rgb-mono-white.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-lw-en-rgb-neg.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-lw-en-rgb-neg.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-lw-en-rgb-pos.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-lw-en-rgb-pos.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-lw-nl-cmyk-mono-white.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-lw-nl-cmyk-mono-white.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-lw-nl-cmyk-neg.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-lw-nl-cmyk-neg.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-lw-nl-cmyk-pos.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-lw-nl-cmyk-pos.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-lw-nl-rgb-mono-white.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-lw-nl-rgb-mono-white.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-lw-nl-rgb-neg.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-lw-nl-rgb-neg.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-lw-nl-rgb-pos.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-lw-nl-rgb-pos.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ow-en-cmyk-mono-white.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ow-en-cmyk-mono-white.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ow-en-cmyk-neg.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ow-en-cmyk-neg.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ow-en-cmyk-pos.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ow-en-cmyk-pos.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ow-en-rgb-mono-white.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ow-en-rgb-mono-white.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ow-en-rgb-neg.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ow-en-rgb-neg.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ow-en-rgb-pos.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ow-en-rgb-pos.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ow-nl-cmyk-mono-white.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ow-nl-cmyk-mono-white.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ow-nl-cmyk-neg.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ow-nl-cmyk-neg.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ow-nl-cmyk-pos.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ow-nl-cmyk-pos.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ow-nl-rgb-mono-white.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ow-nl-rgb-mono-white.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ow-nl-rgb-neg.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ow-nl-rgb-neg.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ow-nl-rgb-pos.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ow-nl-rgb-pos.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-re-en-cmyk-mono-white.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-re-en-cmyk-mono-white.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-re-en-cmyk-neg.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-re-en-cmyk-neg.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-re-en-cmyk-pos.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-re-en-cmyk-pos.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-re-en-rgb-mono-white.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-re-en-rgb-mono-white.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-re-en-rgb-neg.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-re-en-rgb-neg.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-re-en-rgb-pos.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-re-en-rgb-pos.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-re-nl-cmyk-mono-white.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-re-nl-cmyk-mono-white.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-re-nl-cmyk-neg.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-re-nl-cmyk-neg.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-re-nl-cmyk-pos.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-re-nl-cmyk-pos.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-re-nl-rgb-mono-white.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-re-nl-rgb-mono-white.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-re-nl-rgb-neg.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-re-nl-rgb-neg.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-re-nl-rgb-pos.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-re-nl-rgb-pos.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-sw-en-cmyk-mono-white.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-sw-en-cmyk-mono-white.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-sw-en-cmyk-neg.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-sw-en-cmyk-neg.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-sw-en-cmyk-pos.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-sw-en-cmyk-pos.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-sw-en-rgb-mono-white.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-sw-en-rgb-mono-white.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-sw-en-rgb-neg.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-sw-en-rgb-neg.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-sw-en-rgb-pos.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-sw-en-rgb-pos.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-sw-nl-cmyk-mono-white.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-sw-nl-cmyk-mono-white.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-sw-nl-cmyk-neg.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-sw-nl-cmyk-neg.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-sw-nl-cmyk-pos.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-sw-nl-cmyk-pos.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-sw-nl-rgb-mono-white.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-sw-nl-rgb-mono-white.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-sw-nl-rgb-neg.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-sw-nl-rgb-neg.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-sw-nl-rgb-pos.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-sw-nl-rgb-pos.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ti-en-cmyk-mono-white.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ti-en-cmyk-mono-white.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ti-en-cmyk-neg.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ti-en-cmyk-neg.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ti-en-cmyk-pos.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ti-en-cmyk-pos.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ti-en-rgb-mono-white.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ti-en-rgb-mono-white.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ti-en-rgb-neg.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ti-en-rgb-neg.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ti-en-rgb-pos.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ti-en-rgb-pos.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ti-nl-cmyk-mono-white.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ti-nl-cmyk-mono-white.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ti-nl-cmyk-neg.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ti-nl-cmyk-neg.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ti-nl-cmyk-pos.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ti-nl-cmyk-pos.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ti-nl-rgb-mono-white.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ti-nl-rgb-mono-white.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ti-nl-rgb-neg.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ti-nl-rgb-neg.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ti-nl-rgb-pos.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ti-nl-rgb-pos.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ua-en-cmyk-mono-white.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ua-en-cmyk-mono-white.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ua-en-cmyk-neg.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ua-en-cmyk-neg.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ua-en-cmyk-pos.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ua-en-cmyk-pos.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ua-en-rgb-mono-white.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ua-en-rgb-mono-white.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ua-en-rgb-neg.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ua-en-rgb-neg.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ua-en-rgb-pos.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ua-en-rgb-pos.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ua-nl-cmyk-mono-white.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ua-nl-cmyk-mono-white.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ua-nl-cmyk-neg.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ua-nl-cmyk-neg.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ua-nl-cmyk-pos.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ua-nl-cmyk-pos.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ua-nl-cmyk.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ua-nl-cmyk.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ua-nl-rgb-mono-white.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ua-nl-rgb-mono-white.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ua-nl-rgb-neg.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ua-nl-rgb-neg.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ua-nl-rgb-pos.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-ua-nl-rgb-pos.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-we-en-cmyk-mono-white.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-we-en-cmyk-mono-white.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-we-en-cmyk-neg.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-we-en-cmyk-neg.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-we-en-cmyk-pos.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-we-en-cmyk-pos.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-we-en-rgb-mono-white.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-we-en-rgb-mono-white.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-we-en-rgb-neg.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-we-en-rgb-neg.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-we-en-rgb-pos.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-we-en-rgb-pos.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-we-nl-cmyk-mono-white.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-we-nl-cmyk-mono-white.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-we-nl-cmyk-neg.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-we-nl-cmyk-neg.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-we-nl-cmyk-pos.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-we-nl-cmyk-pos.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-we-nl-rgb-mono-white.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-we-nl-rgb-mono-white.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-we-nl-rgb-neg.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-we-nl-rgb-neg.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-we-nl-rgb-pos.eps
%{_texmfdistdir}/tex/latex/uantwerpendocs/Logos/logo-uantwerpen-we-nl-rgb-pos.pdf
%{_texmfdistdir}/tex/latex/uantwerpendocs/beamercolorthemeuantwerpen.sty
%{_texmfdistdir}/tex/latex/uantwerpendocs/beamerfontthemeuantwerpen.sty
%{_texmfdistdir}/tex/latex/uantwerpendocs/beamerinnerthemeuantwerpen.sty
%{_texmfdistdir}/tex/latex/uantwerpendocs/beamerouterthemeuantwerpen.sty
%{_texmfdistdir}/tex/latex/uantwerpendocs/beamerthemeuantwerpen.sty
%{_texmfdistdir}/tex/latex/uantwerpendocs/uantwerpenbamathesis.cls
%{_texmfdistdir}/tex/latex/uantwerpendocs/uantwerpencolorlogoscheme.sty
%{_texmfdistdir}/tex/latex/uantwerpendocs/uantwerpencommonoptions.clo
%{_texmfdistdir}/tex/latex/uantwerpendocs/uantwerpencoursetext.cls
%{_texmfdistdir}/tex/latex/uantwerpendocs/uantwerpendocs-degree.data
%{_texmfdistdir}/tex/latex/uantwerpendocs/uantwerpendocs-doctype.data
%{_texmfdistdir}/tex/latex/uantwerpendocs/uantwerpendocs-en.data
%{_texmfdistdir}/tex/latex/uantwerpendocs/uantwerpendocs-nl.data
%{_texmfdistdir}/tex/latex/uantwerpendocs/uantwerpenexam.cls
%{_texmfdistdir}/tex/latex/uantwerpendocs/uantwerpenletter.cls
%{_texmfdistdir}/tex/latex/uantwerpendocs/uantwerpenphdthesis.cls
%{_texmfdistdir}/tex/latex/uantwerpendocs/uantwerpenreport.cls

%package -n texlive-uassign
Version:        %{texlive_version}.%{texlive_noarch}.1.01svn38459
Release:        0
License:        LPPL-1.0
Summary:        Environments and options for typesetting university assignments
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-uassign-doc >= %{texlive_version}
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
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source332:      uassign.tar.xz
Source333:      uassign.doc.tar.xz

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
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-uassign and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-uassign-doc
%{_texmfdistdir}/doc/latex/uassign/README.md
%{_texmfdistdir}/doc/latex/uassign/uassign.pdf
%{_texmfdistdir}/doc/latex/uassign/uassign.tex

%files -n texlive-uassign
%{_texmfdistdir}/tex/latex/uassign/uassign.sty

%package -n texlive-ucalgmthesis
Version:        %{texlive_version}.%{texlive_noarch}.svn66602
Release:        0
License:        LPPL-1.0
Summary:        LaTeX thesis class for University of Calgary Faculty of Graduate Studies
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-ucalgmthesis-doc >= %{texlive_version}
Provides:       tex(ucalgmthesis.cls)
Requires:       tex(amsthm.sty)
Requires:       tex(erewhon.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(libertine.sty)
Requires:       tex(memoir.cls)
Requires:       tex(newpxmath.sty)
Requires:       tex(newpxtext.sty)
Requires:       tex(newtxmath.sty)
Requires:       tex(newtxtext.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source334:      ucalgmthesis.tar.xz
Source335:      ucalgmthesis.doc.tar.xz

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
Version:        %{texlive_version}.%{texlive_noarch}.svn66602
Release:        0
Summary:        Documentation for texlive-ucalgmthesis
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-ucalgmthesis and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-ucalgmthesis-doc
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
%{_texmfdistdir}/tex/latex/ucalgmthesis/ucalgmthesis.cls

%package -n texlive-ucbthesis
Version:        %{texlive_version}.%{texlive_noarch}.3.6svn51690
Release:        0
License:        LPPL-1.0
Summary:        Thesis and dissertation class supporting UCB requirements
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-ucbthesis-doc >= %{texlive_version}
Provides:       tex(ucbthesis.cls)
Requires:       tex(memoir.cls)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source336:      ucbthesis.tar.xz
Source337:      ucbthesis.doc.tar.xz

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
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-ucbthesis and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-ucbthesis-doc
%{_texmfdistdir}/doc/latex/ucbthesis/README
%{_texmfdistdir}/doc/latex/ucbthesis/example/abstract.tex
%{_texmfdistdir}/doc/latex/ucbthesis/example/chap1.tex
%{_texmfdistdir}/doc/latex/ucbthesis/example/chap2.tex
%{_texmfdistdir}/doc/latex/ucbthesis/example/references.bib
%{_texmfdistdir}/doc/latex/ucbthesis/example/thesis.tex
%{_texmfdistdir}/doc/latex/ucbthesis/ucbthesis.pdf
%{_texmfdistdir}/doc/latex/ucbthesis/ucbthesis.tex

%files -n texlive-ucbthesis
%{_texmfdistdir}/tex/latex/ucbthesis/ucbthesis.cls

%package -n texlive-ucdavisthesis
Version:        %{texlive_version}.%{texlive_noarch}.1.3svn40772
Release:        0
License:        LPPL-1.0
Summary:        A thesis/dissertation class for University of California at Davis
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-ucdavisthesis-doc >= %{texlive_version}
Provides:       tex(ucdavisthesis.cls)
Provides:       tex(ucdthesis10.clo)
Provides:       tex(ucdthesis11.clo)
Provides:       tex(ucdthesis12.clo)
Provides:       tex(ucdthesis13.clo)
Requires:       tex(ifthen.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source338:      ucdavisthesis.tar.xz
Source339:      ucdavisthesis.doc.tar.xz

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
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-ucdavisthesis and texlive-alldocumentation)

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
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-ucdavisthesis-doc
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
%{_texmfdistdir}/tex/latex/ucdavisthesis/ucdavisthesis.cls
%{_texmfdistdir}/tex/latex/ucdavisthesis/ucdthesis10.clo
%{_texmfdistdir}/tex/latex/ucdavisthesis/ucdthesis11.clo
%{_texmfdistdir}/tex/latex/ucdavisthesis/ucdthesis12.clo
%{_texmfdistdir}/tex/latex/ucdavisthesis/ucdthesis13.clo

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
    tar --use-compress-program=xz -xf %{S:1} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:2} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:3} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:4} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:5} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:6} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:7} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:8} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:9} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:10} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:11} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:12} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:13} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:14} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:15} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:16} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:17} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:18} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:19} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:20} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:21} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:22} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:23} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:24} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:25} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:26} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:27} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:28} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:29} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:30} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:31} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:32} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:33} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:34} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:35} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:36} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:37} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:38} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:39} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:40} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:41} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:42} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:43} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:44} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:45} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:46} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:47} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:48} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:49} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:50} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:51} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:52} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:53} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:54} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:55} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:56} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:57} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:58} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:59} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:60} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:61} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:62} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:63} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:64} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:65} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:66} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:67} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:68} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:69} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:70} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:71} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:72} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:73} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:74} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:75} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:76} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:77} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:78} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:79} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:80} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:81} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:82} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:83} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:84} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:85} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:86} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:87} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:88} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:89} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:90} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:91} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:92} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:93} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:94} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:95} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:96} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:97} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:98} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:99} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:100} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:101} -C %{buildroot}%{_datadir}/texlive
    tar --use-compress-program=xz -xf %{S:102} -C %{buildroot}%{_datadir}/texlive
    tar --use-compress-program=xz -xf %{S:103} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:104} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:105} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:106} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:107} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:108} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:109} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:110} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:111} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-times
    for font in %{buildroot}/%{_texmfdistdir}/fonts/type1/urw/times/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-times
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-times/${base} ${font}
    done
    /usr/bin/mkfontscale %{buildroot}%{_datadir}/fonts/texlive-times/
    /usr/bin/mkfontdir -e /usr/share/fonts/encodings/ %{buildroot}%{_datadir}/fonts/texlive-times/
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
    tar --use-compress-program=xz -xf %{S:112} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:113} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:114} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:115} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:116} -C %{buildroot}%{_datadir}/texlive/texmf-dist
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
    /usr/bin/mkfontscale %{buildroot}%{_datadir}/fonts/texlive-tinos/
    /usr/bin/mkfontdir -e /usr/share/fonts/encodings/ %{buildroot}%{_datadir}/fonts/texlive-tinos/
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
    tar --use-compress-program=xz -xf %{S:117} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:118} -C %{buildroot}%{_datadir}/texlive/texmf-dist
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
    /usr/bin/mkfontscale %{buildroot}%{_datadir}/fonts/texlive-tipa/
    /usr/bin/mkfontdir -e /usr/share/fonts/encodings/ %{buildroot}%{_datadir}/fonts/texlive-tipa/
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
    tar --use-compress-program=xz -xf %{S:119} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:120} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:121} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:122} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:123} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:124} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:125} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:126} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:127} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:128} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:129} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:130} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:131} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:132} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:133} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:134} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:135} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:136} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:137} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:138} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:139} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:140} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:141} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:142} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:143} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:144} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:145} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:146} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:147} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:148} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:149} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:150} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:151} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:152} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:153} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:154} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:155} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:156} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:157} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:158} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:159} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:160} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:161} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:162} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:163} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:164} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:165} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:166} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:167} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:168} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:169} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:170} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:171} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:172} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:173} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:174} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:175} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:176} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:177} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:178} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:179} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:180} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:181} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:182} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:183} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:184} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:185} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:186} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:187} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:188} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:189} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:190} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:191} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:192} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:193} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:194} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:195} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:196} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:197} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:198} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:199} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:200} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:201} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:202} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:203} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:204} -C %{buildroot}%{_datadir}/texlive
    tar --use-compress-program=xz -xf %{S:205} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:206} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:207} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:208} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:209} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:210} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:211} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:212} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-trajan
    for font in %{buildroot}/%{_texmfdistdir}/fonts/type1/public/trajan/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-trajan
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-trajan/${base} ${font}
    done
    /usr/bin/mkfontscale %{buildroot}%{_datadir}/fonts/texlive-trajan/
    /usr/bin/mkfontdir -e /usr/share/fonts/encodings/ %{buildroot}%{_datadir}/fonts/texlive-trajan/
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
    tar --use-compress-program=xz -xf %{S:213} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:214} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:215} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:216} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:217} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:218} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:219} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:220} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:221} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:222} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:223} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:224} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:225} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:226} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:227} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:228} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:229} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:230} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:231} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:232} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:233} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:234} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:235} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:236} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:237} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:238} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:239} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:240} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:241} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:242} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:243} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:244} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:245} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:246} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:247} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:248} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:249} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:250} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:251} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:252} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:253} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:254} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:255} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:256} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:257} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:258} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:259} -C %{buildroot}%{_datadir}/texlive
    tar --use-compress-program=xz -xf %{S:260} -C %{buildroot}%{_datadir}/texlive
    tar --use-compress-program=xz -xf %{S:261} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:262} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:263} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:264} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:265} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:266} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:267} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:268} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:269} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:270} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:271} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:272} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:273} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:274} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:275} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:276} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:277} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:278} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:279} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:280} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:281} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:282} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:283} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:284} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:285} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:286} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:287} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:288} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-twemoji-colr
    for font in %{buildroot}/%{_texmfdistdir}/fonts/truetype/public/twemoji-colr/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-twemoji-colr
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-twemoji-colr/${base} ${font}
    done
    /usr/bin/mkfontscale %{buildroot}%{_datadir}/fonts/texlive-twemoji-colr/
    /usr/bin/mkfontdir -e /usr/share/fonts/encodings/ %{buildroot}%{_datadir}/fonts/texlive-twemoji-colr/
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
    tar --use-compress-program=xz -xf %{S:289} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:290} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:291} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:292} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:293} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:294} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:295} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:296} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:297} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:298} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-txfonts
    for font in %{buildroot}/%{_texmfdistdir}/fonts/type1/public/txfonts/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-txfonts
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-txfonts/${base} ${font}
    done
    /usr/bin/mkfontscale %{buildroot}%{_datadir}/fonts/texlive-txfonts/
    /usr/bin/mkfontdir -e /usr/share/fonts/encodings/ %{buildroot}%{_datadir}/fonts/texlive-txfonts/
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
    tar --use-compress-program=xz -xf %{S:299} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:300} -C %{buildroot}%{_datadir}/texlive/texmf-dist
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
    /usr/bin/mkfontscale %{buildroot}%{_datadir}/fonts/texlive-txfontsb/
    /usr/bin/mkfontdir -e /usr/share/fonts/encodings/ %{buildroot}%{_datadir}/fonts/texlive-txfontsb/
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
    tar --use-compress-program=xz -xf %{S:301} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:302} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:303} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:304} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-txuprcal
    for font in %{buildroot}/%{_texmfdistdir}/fonts/type1/public/txuprcal/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-txuprcal
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-txuprcal/${base} ${font}
    done
    /usr/bin/mkfontscale %{buildroot}%{_datadir}/fonts/texlive-txuprcal/
    /usr/bin/mkfontdir -e /usr/share/fonts/encodings/ %{buildroot}%{_datadir}/fonts/texlive-txuprcal/
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
    tar --use-compress-program=xz -xf %{S:305} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:306} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:307} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:308} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:309} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:310} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:311} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:312} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:313} -C %{buildroot}%{_datadir}/texlive
    tar --use-compress-program=xz -xf %{S:314} -C %{buildroot}%{_datadir}/texlive
    tar --use-compress-program=xz -xf %{S:315} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:316} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:317} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:318} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-typicons
    for font in %{buildroot}/%{_texmfdistdir}/fonts/truetype/public/typicons/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-typicons
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-typicons/${base} ${font}
    done
    /usr/bin/mkfontscale %{buildroot}%{_datadir}/fonts/texlive-typicons/
    /usr/bin/mkfontdir -e /usr/share/fonts/encodings/ %{buildroot}%{_datadir}/fonts/texlive-typicons/
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
    tar --use-compress-program=xz -xf %{S:319} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:320} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:321} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:322} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:323} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:324} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:325} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:326} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:327} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:328} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:329} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:330} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:331} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:332} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:333} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:334} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:335} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:336} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:337} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:338} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:339} -C %{buildroot}%{_datadir}/texlive/texmf-dist
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
