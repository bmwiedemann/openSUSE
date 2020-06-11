#
# spec file for package texlive
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


%define texlive_version  2020
%define texlive_previous 2019
%define texlive_release  20200327
%define texlive_noarch   176
%define texlive_source   texlive-20200327-source

%define __perl_requires		%{nil}
%define __os_install_post	/usr/lib/rpm/brp-compress \\\
  %(ls /usr/lib/rpm/brp-suse.d/* 2> /dev/null | grep -vE 'symlink|desktop') %{nil}

%if ! %{defined perl_version}
%global perl_version %(rpm -q --qf '%%{VERSION}' perl)
%endif
%global perl_versnum %(rpm -q --qf '%%{VERSION}' perl | sed 's/\\.//g')

%bcond_with     zypper_posttrans

#
# LuaJIT -- does not build nor support all architectures
#	    Current status is available at https://github.com/LuaJIT/LuaJIT
#                                          https://github.com/LuaJIT/LuaJIT/issues/42
#	    Compare with libs/luajit/LuaJIT-<version>/src/lj_arch.h
#
%ifarch %ix86 x86_64 %arml aarch64 mips
%global         with_LuaJIT 1
%endif
%bcond_with	LuaJIT

#
# poppler -- use system wide libpoppler
#
%global         with_poppler 1
%bcond_with	poppler

# psutils -- is also available as the package psutils and therefore
#           not necessary required, enabling the resulting psutils
#           cause dependency on package collection-fontutils
%bcond_with	psutils

#
# buildbiber -- we build our own biber executable as with this all
#	    architectures can be supported (in theory) and the final
#	    perl dump binary is smaller
#
%bcond_without	buildbiber

#
# lcdf-typetools -- is also available as the package lcdf-typetools
#	    and therefore we may only require this external package
%bcond_without	lcdf_typetools

Name:           texlive
Version:        %{texlive_version}.%{texlive_release}
Release:        0
Summary:        The TeXLive Formatting System
License:        GPL-2.0-or-later AND GPL-2.0-only AND GPL-3.0-only AND LPPL-1.3c AND LPPL-1.0 AND Artistic-1.0 AND Apache-2.0 AND MIT AND BSD-3-Clause AND SUSE-TeX AND SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
PreReq:         /usr/bin/perl
PreReq:         /usr/bin/clear
PreReq:         /usr/bin/dialog
PreReq:         coreutils
PreReq:         ed
PreReq:         findutils
PreReq:         grep
PreReq:         sed
PreReq:         %{name}-filesystem >= %{texlive_version}
PreReq:         %{name}-kpathsea-bin >= %{texlive_version}
PreReq:         %{name}-kpathsea >= %{texlive_version}
PreReq:         %{name}-scripts >= %{texlive_version}
#!BuildIgnore:  %{name}-kpathsea-bin
#!BuildIgnore:  %{name}-kpathsea
#!BuildIgnore:  %{name}-scripts-bin
#!BuildIgnore:  %{name}-scripts
Requires(post): coreutils
Requires(postun): coreutils
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): %{name}-filesystem >= %{texlive_version}
Requires(posttrans): %{name}-kpathsea-bin >= %{texlive_version}
Requires(posttrans): %{name}-kpathsea >= %{texlive_version}
Requires(posttrans): %{name}-scripts-bin >= %{texlive_version}
Requires(posttrans): %{name}-scripts >= %{texlive_version}
Recommends:     %{name}-scheme-medium
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  cairo
BuildRequires:  cairo-devel
BuildRequires:  dejavu
BuildRequires:  dialog
BuildRequires:  ed
BuildRequires:  expat
BuildRequires:  fdupes
BuildRequires:  fftw3-devel
BuildRequires:  flex
BuildRequires:  freeglut-devel
BuildRequires:  freetype2-devel
BuildRequires:  gc-devel
BuildRequires:  gcc-c++
BuildRequires:  gd-devel
BuildConflicts: ghostscript-mini
BuildRequires:  %{name}-filesystem
BuildRequires:  Mesa-libglapi-devel
BuildRequires:  ghostscript-devel
BuildRequires:  ghostscript-library
BuildRequires:  glibc-devel
BuildRequires:  graphite2-devel
BuildRequires:  gsl-devel
%if 0%{?suse_version} >= 1550
BuildRequires:  harfbuzz-devel >= 2.6
%else
%if 0%{?sle_version} >= 150200
BuildRequires:  harfbuzz-devel >= 2.6
%endif
%endif
BuildRequires:  jpeg
BuildRequires:  libOSMesa-devel
BuildRequires:  libicu-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libopenssl-devel
BuildRequires:  libpaper-devel
BuildRequires:  libpng-devel
BuildRequires:  libpoppler-devel
BuildRequires:  libsigsegv-devel
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  libxslt-devel
BuildRequires:  mpfr-devel
BuildRequires:  ncurses-devel
BuildRequires:  netpbm
BuildRequires:  pango-devel
BuildRequires:  pango-tools
BuildRequires:  potrace-devel
BuildRequires:  pwdutils
BuildRequires:  readline-devel
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glew)
#BuildRequires:  pkgconfig(glm)
BuildRequires:  glm-devel
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(gsl)
BuildConflicts: texinfo
BuildRequires:  unzip
BuildRequires:  xaw3d-devel
BuildRequires:  xz
BuildRequires:  zip
BuildRequires:  zlib-devel
BuildRequires:  zziplib-devel
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(xt)
%if %{with buildbiber}
BuildRequires:  perl-base >= 5.26.1
BuildRequires:  perl(autovivification)
#BuildRequires: perl(Business::ISBN)
BuildRequires:  perl-Business-ISBN >= 3.005
BuildRequires:  perl-Business-ISBN-Data >= 20191107
BuildRequires:  perl(Business::ISMN)
BuildRequires:  perl(Business::ISSN)
BuildRequires:  perl(Class::Accessor)
BuildRequires:  perl(Class::Factory::Util)
BuildRequires:  perl(Config::AutoConf) >= 0.15
BuildRequires:  perl(Data::Compare)
BuildRequires:  perl(Data::Dump)
BuildRequires:  perl(Data::Uniqid)
BuildRequires:  perl(Date::Simple)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::Calendar::Julian)
BuildRequires:  perl(DateTime::Format::Builder)
BuildRequires:  perl(DateTime::Format::Strptime)
BuildRequires:  perl(Encode::EUCJPASCII)
BuildRequires:  perl(Encode::HanExtra)
BuildRequires:  perl(Encode::JIS2K)
BuildRequires:  perl(ExtUtils::LibBuilder) >= 0.02
BuildRequires:  perl(File::Slurp::Unicode)
BuildRequires:  perl(File::Slurper)
BuildRequires:  perl(File::Which)
BuildRequires:  perl(IO::String)
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(IPC::Run3)
BuildRequires:  perl(LWP::Protocol::https)
BuildRequires:  perl(LWP::Simple)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Lingua::Translit)
BuildRequires:  perl(List::AllUtils)
BuildRequires:  perl(List::MoreUtils) >= 0.407
BuildRequires:  perl(List::MoreUtils::XS)
BuildRequires:  perl(Log::Log4perl)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Package::DeprecationManager)
BuildRequires:  perl(Params::Util)
BuildRequires:  perl(Parse::RecDescent)
BuildRequires:  perl(PerlIO::utf8_strict)
BuildRequires:  perl(Readonly::XS)
BuildRequires:  perl(Regexp::Common)
BuildRequires:  perl(Sort::Key)
BuildRequires:  perl(Sub::Install)
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod) >= 1.22
BuildRequires:  perl(Test::Pod::Coverage) >= 1.08
BuildRequires:  perl(Text::BibTeX) >= 0.85
BuildRequires:  perl(Text::CSV)
BuildRequires:  perl(Text::CSV_XS)
BuildRequires:  perl(Text::Roman)
BuildRequires:  perl(Unicode::Collate) >= 1.25
BuildRequires:  perl(Unicode::GCString)
BuildRequires:  perl(Unicode::LineBreak)
BuildRequires:  perl(Unicode::Normalize) >= 1.23
BuildRequires:  perl(XML::LibXML::Simple)
BuildRequires:  perl(XML::LibXSLT)
BuildRequires:  perl(XML::Writer::String)
%endif
# Download at ftp://tug.org/texlive/historic/%{texlive_version}/
Source0:        %{texlive_source}.tar.xz
Source3:        biber-2.14.tar.xz
Source4:        cnf-to-paths.awk
Source30:       texlive-rpmlintrc
Source50:       public.c
Source51:       public.8
Patch0:         source.dif
Patch1:         source-configure.dif
Patch2:         source-xdvizilla.dif
Patch3:         source-arraysubs.dif
Patch5:         source-texdoc.dif
Patch6:         source-dviutils.dif
Patch8:         source-psutils.dif
Patch10:        source-poppler.dif
Patch11:        source-lacheck.dif
Patch12:        source-warns.dif
Patch13:        source-x11r7.dif
Patch15:        source-overflow.dif
Patch17:        source-64.dif
Patch18:        source-a2ping.dif
Patch19:        source-dvipng.dif
Patch20:        source-missed-scripts.dif
Patch21:        source-ppc64.dif
# PATCH-FIX-SUSE Make biber work with our perl
Patch42:        biblatex-encoding.dif
# PATCH-FIX-SUSE Old problem back: we do not use internal Certs!
Patch44:        biber-certs.dif
# PATCH-FIX-SUSE Make biber work with perl 5.18.2
Patch47:        biber-perl-5.18.2.dif
# PATCH-FIX-SUSE Support older poppler version as well
Patch53:        source-poppler0.59.0.patch
# PATCH-FIX-TEXLIVE
Patch54:        source-fix-const-poppler0.66.0.patch
# PATCH-FIX-TEXLIVE
Patch55:        source-fix-bool-poppler.patch
# PATCH-FIX-TEXLIVE
Patch56:        source-poppler-use-std_string.patch
# PATCH-FIX-SUSE Fix leaking string copy
Patch57:        source-poppler-fix-dict-memleak.patch
# PATCH-FIX-TEXLIVE
Patch58:        source-poppler0.79.0.patch
# PATCH-FIX-TEXLIVE
Patch61:        source-poppler0.83.0.patch
# PATCH-FIX-SUSE Let it build even without ls-R files around
Patch62:        source-psutils-kpathsea.dif
# PATCH-FIX-UPSTREAM source-poppler0.86.0.patch
Patch64:        source-poppler0.86.0.patch
# PATCH-FIX-SUSE Support luajit on ppc64/ppc64le
Patch104:       0004-Add-ppc64-support-based-on-koriakin-GitHub-patchset.patch
# PATCH-FIX-SUSE Support luajit fix for arm64
Patch106:       0006-Fix-register-allocation-bug-in-arm64.patch
Prefix:         %{_bindir}
Provides:       pdfjam = %{version}
Obsoletes:      pdfjam < %{version}

%define add_optflags(a:f:t:p:w:W:d:g:O:A:C:D:E:H:i:M:n:P:U:u:l:s:X:B:I:L:b:V:m:x:c:S:E:o:v:) \
%global optflags %{optflags} %{**}

%{expand: %%global options %(mktemp /tmp/texlive-opts.XXXXXXXX)}
%global _varlib		%{_localstatedir}/lib
%global _libexecdir	%{_prefix}/lib

%define _texmfdistdir	%{_datadir}/texmf
%if 0%{texlive_version} >= 2013
%define _texmfmaindir	%{_texmfdistdir}
%define _texmfdirs	%{_texmfdistdir}
%else
%define _texmfmaindir	%{_libexecdir}/texmf
%define _texmfdirs	\{%{_texmfdistdir},%{_texmfmaindir}\}
%endif

%define _texmfconfdir	%{_sysconfdir}/texmf
%define _texmfvardir	%{_varlib}/texmf
%define _texmfcache	%{_localstatedir}/cache/texmf
%define _fontcache	%{_texmfcache}/fonts
#
%define _x11bin		%{_prefix}/bin
%define _x11lib		%{_libdir}
%define _x11data	%{_datadir}/X11
%define _x11inc		%{_includedir}
%define _appdefdir	%{_x11data}/app-defaults
#
%define texgrp		mktex
%define texusr		mktex
#%define texgid		505
#%define texuid		505
#
%description
After installing texlive and the package texlive-latex, find a large
selection of documentation for TeX, LaTeX, and various layout styles in
/usr/share/texmf/doc.

TeX (pronounced tech) is an interpreter for text formatting and was
developed by Donald E. Knuth.  It works with control and macro commands
on a text file. Working with TeX is similar to typesetting methods.
LaTeX is a complex macro package that removes the cryptical TeX
interface and does most of the work for the user.

TeX uses special fonts produced by the MetaFont program. Various
printer drivers and an X11 viewer are also included in this package.
The teTeX package is based on the standard TeX package of Karl Berry,
which makes configuration much easier. It is also possible to use
PostScript fonts. A real PostScript printer is required, however. If
the ghostscript (gs) package is installed, all drivers for printing and
viewing can use these fonts. Note, however, that the fonts included in
the ghostscript package are not identical to Adobe's PostScript fonts.
The copyright prohibids us to include them on the CD.

Besides these features, the programs MakeIndex (for producing indexes)
and BibTeX (for literature data processing) exist.

The texlive package includes a full texmf tree, many programs like tex,
dvips, etc., shell script configuration, and a big collection of
documentations. This package is easily configured by the script
texconfig and has multilanguage options.


%package a2ping-bin
Version:        %{texlive_version}.%{texlive_release}.svn27321
Release:        0
Summary:        Binary files of a2ping
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-a2ping >= %{texlive_version}
#!BuildIgnore:  texlive-a2ping
Prefix:         %{_bindir}

%description a2ping-bin
Binary files of a2ping

%package accfonts-bin
Version:        %{texlive_version}.%{texlive_release}.svn12688
Release:        0
Summary:        Binary files of accfonts
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-accfonts >= %{texlive_version}
#!BuildIgnore:  texlive-accfonts
Prefix:         %{_bindir}

%description accfonts-bin
Binary files of accfonts

%package adhocfilelist-bin
Version:        %{texlive_version}.%{texlive_release}.svn28038
Release:        0
Summary:        Binary files of adhocfilelist
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-adhocfilelist >= %{texlive_version}
#!BuildIgnore:  texlive-adhocfilelist
Prefix:         %{_bindir}

%description adhocfilelist-bin
Binary files of adhocfilelist

%package afm2pl-bin
Version:        %{texlive_version}.%{texlive_release}.svn53999
Release:        0
Summary:        Binary files of afm2pl
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-afm2pl >= %{texlive_version}
#!BuildIgnore:  texlive-afm2pl
Prefix:         %{_bindir}

%description afm2pl-bin
Binary files of afm2pl

%package aleph-bin
Version:        %{texlive_version}.%{texlive_release}.svn53999
Release:        0
Summary:        Binary files of aleph
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-aleph >= %{texlive_version}
#!BuildIgnore:  texlive-aleph
Prefix:         %{_bindir}

%description aleph-bin
Binary files of aleph

%package amstex-bin
Version:        %{texlive_version}.%{texlive_release}.svn3006
Release:        0
Summary:        Binary files of amstex
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-amstex >= %{texlive_version}
#!BuildIgnore:  texlive-amstex
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Recommends:     texlive-collection-basic >= %{texlive_version}
Prefix:         %{_bindir}

%description amstex-bin
Binary files of amstex

%package arara-bin
Version:        %{texlive_version}.%{texlive_release}.svn29036
Release:        0
Summary:        Binary files of arara
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-arara >= %{texlive_version}
#!BuildIgnore:  texlive-arara
Prefix:         %{_bindir}

%description arara-bin
Binary files of arara

%package asymptote-bin
Version:        %{texlive_version}.%{texlive_release}.svn54575
Release:        0
Summary:        Binary files of asymptote
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-asymptote >= %{texlive_version}
#!BuildIgnore:  texlive-asymptote
Prefix:         %{_bindir}

%description asymptote-bin
Binary files of asymptote

%package attachfile2-bin
Version:        %{texlive_version}.%{texlive_release}.svn52909
Release:        0
Summary:        Binary files of attachfile2
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-attachfile2 >= %{texlive_version}
#!BuildIgnore:  texlive-attachfile2
Prefix:         %{_bindir}

%description attachfile2-bin
Binary files of attachfile2

%package authorindex-bin
Version:        %{texlive_version}.%{texlive_release}.svn18790
Release:        0
Summary:        Binary files of authorindex
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-authorindex >= %{texlive_version}
#!BuildIgnore:  texlive-authorindex
Prefix:         %{_bindir}

%description authorindex-bin
Binary files of authorindex

%package autosp-bin
Version:        %{texlive_version}.%{texlive_release}.svn54358
Release:        0
Summary:        Binary files of autosp
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-autosp >= %{texlive_version}
#!BuildIgnore:  texlive-autosp
Prefix:         %{_bindir}

%description autosp-bin
Binary files of autosp

%package axodraw2-bin
Version:        %{texlive_version}.%{texlive_release}.svn53999
Release:        0
Summary:        Binary files of axodraw2
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-axodraw2 >= %{texlive_version}
#!BuildIgnore:  texlive-axodraw2
Prefix:         %{_bindir}

%description axodraw2-bin
Binary files of axodraw2

%package bib2gls-bin
Version:        %{texlive_version}.%{texlive_release}.svn45266
Release:        0
Summary:        Binary files of bib2gls
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-bib2gls >= %{texlive_version}
#!BuildIgnore:  texlive-bib2gls
Prefix:         %{_bindir}

%description bib2gls-bin
Binary files of bib2gls

%package biber-bin
Version:        %{texlive_version}.%{texlive_release}.svn53064
Release:        0
Summary:        Binary files of biber
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
%if %{with buildbiber}
Requires:       perl = %{perl_version}
Recommends:     ca-certificates
Recommends:     ca-certificates-mozilla
%if 0%{?suse_version} > 1230
Requires:       perl(Biber) >= %{texlive_version}.%{texlive_release}
%endif
Requires:       perl(LWP::UserAgent)
Requires:       perl(Text::BibTeX)
Requires:       perl(Text::Roman)
%endif
BuildArch:      noarch
Requires(pre):  texlive-biber >= %{texlive_version}
#!BuildIgnore:  texlive-biber
Prefix:         %{_bindir}

%description biber-bin
Binary files of biber

%package bibexport-bin
Version:        %{texlive_version}.%{texlive_release}.svn16219
Release:        0
Summary:        Binary files of bibexport
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-bibexport >= %{texlive_version}
#!BuildIgnore:  texlive-bibexport
Prefix:         %{_bindir}

%description bibexport-bin
Binary files of bibexport

%package bibtex-bin
Version:        %{texlive_version}.%{texlive_release}.svn53999
Release:        0
Summary:        Binary files of bibtex
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-bibtex >= %{texlive_version}
#!BuildIgnore:  texlive-bibtex
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Recommends:     texlive-collection-basic >= %{texlive_version}
Prefix:         %{_bindir}

%description bibtex-bin
Binary files of bibtex

%package bibtex8-bin
Version:        %{texlive_version}.%{texlive_release}.svn53999
Release:        0
Summary:        Binary files of bibtex8
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-bibtex8 >= %{texlive_version}
#!BuildIgnore:  texlive-bibtex8
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Recommends:     texlive-collection-basic >= %{texlive_version}
Prefix:         %{_bindir}

%description bibtex8-bin
Binary files of bibtex8

%package bibtexu-bin
Version:        %{texlive_version}.%{texlive_release}.svn53999
Release:        0
Summary:        Binary files of bibtexu
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-bibtexu >= %{texlive_version}
#!BuildIgnore:  texlive-bibtexu
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Recommends:     texlive-collection-basic >= %{texlive_version}
Prefix:         %{_bindir}

%description bibtexu-bin
Binary files of bibtexu

%package bundledoc-bin
Version:        %{texlive_version}.%{texlive_release}.svn17794
Release:        0
Summary:        Binary files of bundledoc
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-bundledoc >= %{texlive_version}
#!BuildIgnore:  texlive-bundledoc
Prefix:         %{_bindir}

%description bundledoc-bin
Binary files of bundledoc

%package cachepic-bin
Version:        %{texlive_version}.%{texlive_release}.svn15543
Release:        0
Summary:        Binary files of cachepic
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-cachepic >= %{texlive_version}
#!BuildIgnore:  texlive-cachepic
Prefix:         %{_bindir}

%description cachepic-bin
Binary files of cachepic

%package checkcites-bin
Version:        %{texlive_version}.%{texlive_release}.svn25623
Release:        0
Summary:        Binary files of checkcites
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-checkcites >= %{texlive_version}
#!BuildIgnore:  texlive-checkcites
Prefix:         %{_bindir}

%description checkcites-bin
Binary files of checkcites

%package checklistings-bin
Version:        %{texlive_version}.%{texlive_release}.svn38300
Release:        0
Summary:        Binary files of checklistings
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-checklistings >= %{texlive_version}
#!BuildIgnore:  texlive-checklistings
Prefix:         %{_bindir}

%description checklistings-bin
Binary files of checklistings

%package chklref-bin
Version:        %{texlive_version}.%{texlive_release}.svn52631
Release:        0
Summary:        Binary files of chklref
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-chklref >= %{texlive_version}
#!BuildIgnore:  texlive-chklref
Prefix:         %{_bindir}

%description chklref-bin
Binary files of chklref

%package chktex-bin
Version:        %{texlive_version}.%{texlive_release}.svn53999
Release:        0
Summary:        Binary files of chktex
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-chktex >= %{texlive_version}
#!BuildIgnore:  texlive-chktex
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Recommends:     texlive-collection-basic >= %{texlive_version}
Prefix:         %{_bindir}

%description chktex-bin
Binary files of chktex

%package cjk-gs-integrate-bin
Version:        %{texlive_version}.%{texlive_release}.svn37223
Release:        0
Summary:        Binary files of cjk-gs-integrate
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-cjk-gs-integrate >= %{texlive_version}
#!BuildIgnore:  texlive-cjk-gs-integrate
Prefix:         %{_bindir}

%description cjk-gs-integrate-bin
Binary files of cjk-gs-integrate

%package cjkutils-bin
Version:        %{texlive_version}.%{texlive_release}.svn53999
Release:        0
Summary:        Binary files of cjkutils
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Obsoletes:      texlive-bin-cjk <= %{texlive_previous}
Requires(pre):  texlive-cjkutils >= %{texlive_version}
#!BuildIgnore:  texlive-cjkutils
Prefix:         %{_bindir}

%description cjkutils-bin
Binary files of cjkutils

%package clojure-pamphlet-bin
Version:        %{texlive_version}.%{texlive_release}.svn51944
Release:        0
Summary:        Binary files of clojure-pamphlet
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-clojure-pamphlet >= %{texlive_version}
#!BuildIgnore:  texlive-clojure-pamphlet
Prefix:         %{_bindir}

%description clojure-pamphlet-bin
Binary files of clojure-pamphlet

%package cluttex-bin
Version:        %{texlive_version}.%{texlive_release}.svn48871
Release:        0
Summary:        Binary files of cluttex
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-cluttex >= %{texlive_version}
#!BuildIgnore:  texlive-cluttex
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Recommends:     texlive-collection-basic >= %{texlive_version}
Prefix:         %{_bindir}

%description cluttex-bin
Binary files of cluttex

%package context-bin
Version:        %{texlive_version}.%{texlive_release}.svn34112
Release:        0
Summary:        Binary files of context
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-context >= %{texlive_version}
#!BuildIgnore:  texlive-context
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Recommends:     texlive-collection-context >= %{texlive_version}
Prefix:         %{_bindir}

%description context-bin
Binary files of context

%package convbkmk-bin
Version:        %{texlive_version}.%{texlive_release}.svn30408
Release:        0
Summary:        Binary files of convbkmk
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-convbkmk >= %{texlive_version}
#!BuildIgnore:  texlive-convbkmk
Prefix:         %{_bindir}

%description convbkmk-bin
Binary files of convbkmk

%package crossrefware-bin
Version:        %{texlive_version}.%{texlive_release}.svn45927
Release:        0
Summary:        Binary files of crossrefware
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-crossrefware >= %{texlive_version}
#!BuildIgnore:  texlive-crossrefware
Prefix:         %{_bindir}

%description crossrefware-bin
Binary files of crossrefware

%package cslatex-bin
Version:        %{texlive_version}.%{texlive_release}.svn3006
Release:        0
Summary:        Binary files of cslatex
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-cslatex >= %{texlive_version}
#!BuildIgnore:  texlive-cslatex
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Recommends:     texlive-collection-latexrecommended >= %{texlive_version}
Prefix:         %{_bindir}

%description cslatex-bin
Binary files of cslatex

%package csplain-bin
Version:        %{texlive_version}.%{texlive_release}.svn50528
Release:        0
Summary:        Binary files of csplain
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-csplain >= %{texlive_version}
#!BuildIgnore:  texlive-csplain
Prefix:         %{_bindir}

%description csplain-bin
Binary files of csplain

%package ctan-o-mat-bin
Version:        %{texlive_version}.%{texlive_release}.svn46996
Release:        0
Summary:        Binary files of ctan-o-mat
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-ctan-o-mat >= %{texlive_version}
#!BuildIgnore:  texlive-ctan-o-mat
Prefix:         %{_bindir}

%description ctan-o-mat-bin
Binary files of ctan-o-mat

%package ctanbib-bin
Version:        %{texlive_version}.%{texlive_release}.svn48478
Release:        0
Summary:        Binary files of ctanbib
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-ctanbib >= %{texlive_version}
#!BuildIgnore:  texlive-ctanbib
Prefix:         %{_bindir}

%description ctanbib-bin
Binary files of ctanbib

%package ctanify-bin
Version:        %{texlive_version}.%{texlive_release}.svn24061
Release:        0
Summary:        Binary files of ctanify
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-ctanify >= %{texlive_version}
#!BuildIgnore:  texlive-ctanify
Prefix:         %{_bindir}

%description ctanify-bin
Binary files of ctanify

%package ctanupload-bin
Version:        %{texlive_version}.%{texlive_release}.svn23866
Release:        0
Summary:        Binary files of ctanupload
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-ctanupload >= %{texlive_version}
#!BuildIgnore:  texlive-ctanupload
Prefix:         %{_bindir}

%description ctanupload-bin
Binary files of ctanupload

%package ctie-bin
Version:        %{texlive_version}.%{texlive_release}.svn53999
Release:        0
Summary:        Binary files of ctie
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-ctie >= %{texlive_version}
#!BuildIgnore:  texlive-ctie
Prefix:         %{_bindir}

%description ctie-bin
Binary files of ctie

%package cweb-bin
Version:        %{texlive_version}.%{texlive_release}.svn53999
Release:        0
Summary:        Binary files of cweb
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-cweb >= %{texlive_version}
#!BuildIgnore:  texlive-cweb
Prefix:         %{_bindir}

%description cweb-bin
Binary files of cweb

%package cyrillic-bin-bin
Version:        %{texlive_version}.%{texlive_release}.svn53554
Release:        0
Summary:        Binary files of cyrillic-bin
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-cyrillic-bin >= %{texlive_version}
#!BuildIgnore:  texlive-cyrillic-bin
Prefix:         %{_bindir}

%description cyrillic-bin-bin
Binary files of cyrillic-bin

%package de-macro-bin
Version:        %{texlive_version}.%{texlive_release}.svn17399
Release:        0
Summary:        Binary files of de-macro
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-de-macro >= %{texlive_version}
#!BuildIgnore:  texlive-de-macro
Prefix:         %{_bindir}

%description de-macro-bin
Binary files of de-macro

%package detex-bin
Version:        %{texlive_version}.%{texlive_release}.svn53999
Release:        0
Summary:        Binary files of detex
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-detex >= %{texlive_version}
#!BuildIgnore:  texlive-detex
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Recommends:     texlive-collection-basic >= %{texlive_version}
Prefix:         %{_bindir}

%description detex-bin
Binary files of detex

%package diadia-bin
Version:        %{texlive_version}.%{texlive_release}.svn37645
Release:        0
Summary:        Binary files of diadia
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
BuildArch:      noarch
Requires(pre):  texlive-diadia >= %{texlive_version}
#!BuildIgnore:  texlive-diadia
Prefix:         %{_bindir}

%description diadia-bin
Binary files of diadia

%package dosepsbin-bin
Version:        %{texlive_version}.%{texlive_release}.svn24759
Release:        0
Summary:        Binary files of dosepsbin
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-dosepsbin >= %{texlive_version}
#!BuildIgnore:  texlive-dosepsbin
Prefix:         %{_bindir}

%description dosepsbin-bin
Binary files of dosepsbin

%package dtl-bin
Version:        %{texlive_version}.%{texlive_release}.svn53999
Release:        0
Summary:        Binary files of dtl
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-dtl >= %{texlive_version}
#!BuildIgnore:  texlive-dtl
Prefix:         %{_bindir}

%description dtl-bin
Binary files of dtl

%package dtxgen-bin
Version:        %{texlive_version}.%{texlive_release}.svn29031
Release:        0
Summary:        Binary files of dtxgen
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-dtxgen >= %{texlive_version}
#!BuildIgnore:  texlive-dtxgen
Prefix:         %{_bindir}

%description dtxgen-bin
Binary files of dtxgen

%package dviasm-bin
Version:        %{texlive_version}.%{texlive_release}.svn8329
Release:        0
Summary:        Binary files of dviasm
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-dviasm >= %{texlive_version}
#!BuildIgnore:  texlive-dviasm
Prefix:         %{_bindir}

%description dviasm-bin
Binary files of dviasm

%package dvicopy-bin
Version:        %{texlive_version}.%{texlive_release}.svn53999
Release:        0
Summary:        Binary files of dvicopy
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-dvicopy >= %{texlive_version}
#!BuildIgnore:  texlive-dvicopy
Prefix:         %{_bindir}

%description dvicopy-bin
Binary files of dvicopy

%package dvidvi-bin
Version:        %{texlive_version}.%{texlive_release}.svn50281
Release:        0
Summary:        Binary files of dvidvi
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-dvidvi >= %{texlive_version}
#!BuildIgnore:  texlive-dvidvi
Prefix:         %{_bindir}

%description dvidvi-bin
Binary files of dvidvi

%package dviinfox-bin
Version:        %{texlive_version}.%{texlive_release}.svn44515
Release:        0
Summary:        Binary files of dviinfox
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-dviinfox >= %{texlive_version}
#!BuildIgnore:  texlive-dviinfox
Prefix:         %{_bindir}

%description dviinfox-bin
Binary files of dviinfox

%package dviljk-bin
Version:        %{texlive_version}.%{texlive_release}.svn53999
Release:        0
Summary:        Binary files of dviljk
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Obsoletes:      texlive-bin-dvilj <= %{texlive_previous}
Provides:       texlive-bin-dvilj   = %{texlive_version}
Requires(pre):  texlive-dviljk >= %{texlive_version}
#!BuildIgnore:  texlive-dviljk
Prefix:         %{_bindir}

%description dviljk-bin
Binary files of dviljk

%package dviout-util-bin
Version:        %{texlive_version}.%{texlive_release}.svn53999
Release:        0
Summary:        Binary files of dviout-util
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-dviout-util >= %{texlive_version}
#!BuildIgnore:  texlive-dviout-util
Prefix:         %{_bindir}

%description dviout-util-bin
Binary files of dviout-util

%package dvipdfmx-bin
Version:        %{texlive_version}.%{texlive_release}.svn54346
Release:        0
Summary:        Binary files of dvipdfmx
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Obsoletes:      texlive-dvipdfm-bin <= 2012
Provides:       texlive-dvipdfm-bin = %{texlive_version}
Requires:       texlive-scripts >= %{texlive_version}
Requires:       texlive-xetex-bin >= %{texlive_version}
Requires(pre):  texlive-dvipdfmx >= %{texlive_version}
#!BuildIgnore:  texlive-dvipdfmx
Prefix:         %{_bindir}

%description dvipdfmx-bin
Binary files of dvipdfmx

%package dvipng-bin
Version:        %{texlive_version}.%{texlive_release}.svn53999
Release:        0
Summary:        Binary files of dvipng
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-dvipng >= %{texlive_version}
#!BuildIgnore:  texlive-dvipng
Prefix:         %{_bindir}

%description dvipng-bin
Binary files of dvipng

%package dvipos-bin
Version:        %{texlive_version}.%{texlive_release}.svn53999
Release:        0
Summary:        Binary files of dvipos
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-dvipos >= %{texlive_version}
#!BuildIgnore:  texlive-dvipos
Prefix:         %{_bindir}

%description dvipos-bin
Binary files of dvipos

%package dvips-bin
Version:        %{texlive_version}.%{texlive_release}.svn53999
Release:        0
Summary:        Binary files of dvips
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-dvips >= %{texlive_version}
#!BuildIgnore:  texlive-dvips
Prefix:         %{_bindir}

%description dvips-bin
Binary files of dvips

%package dvisvgm-bin
Version:        %{texlive_version}.%{texlive_release}.svn54460
Release:        0
Summary:        Binary files of dvisvgm
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-dvisvgm >= %{texlive_version}
#!BuildIgnore:  texlive-dvisvgm
Prefix:         %{_bindir}

%description dvisvgm-bin
Binary files of dvisvgm

%package ebong-bin
Version:        %{texlive_version}.%{texlive_release}.svn21000
Release:        0
Summary:        Binary files of ebong
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-ebong >= %{texlive_version}
#!BuildIgnore:  texlive-ebong
Prefix:         %{_bindir}

%description ebong-bin
Binary files of ebong

%package eplain-bin
Version:        %{texlive_version}.%{texlive_release}.svn3006
Release:        0
Summary:        Binary files of eplain
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-eplain >= %{texlive_version}
#!BuildIgnore:  texlive-eplain
Prefix:         %{_bindir}

%description eplain-bin
Binary files of eplain

%package epspdf-bin
Version:        %{texlive_version}.%{texlive_release}.svn29050
Release:        0
Summary:        Binary files of epspdf
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-epspdf >= %{texlive_version}
#!BuildIgnore:  texlive-epspdf
Prefix:         %{_bindir}

%description epspdf-bin
Binary files of epspdf

%package epstopdf-bin
Version:        %{texlive_version}.%{texlive_release}.svn18336
Release:        0
Summary:        Binary files of epstopdf
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-epstopdf >= %{texlive_version}
#!BuildIgnore:  texlive-epstopdf
Prefix:         %{_bindir}

%description epstopdf-bin
Binary files of epstopdf

%package exceltex-bin
Version:        %{texlive_version}.%{texlive_release}.svn25860
Release:        0
Summary:        Binary files of exceltex
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-exceltex >= %{texlive_version}
#!BuildIgnore:  texlive-exceltex
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Recommends:     texlive-collection-basic >= %{texlive_version}
Prefix:         %{_bindir}

%description exceltex-bin
Binary files of exceltex

%package fig4latex-bin
Version:        %{texlive_version}.%{texlive_release}.svn14752
Release:        0
Summary:        Binary files of fig4latex
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-fig4latex >= %{texlive_version}
#!BuildIgnore:  texlive-fig4latex
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Recommends:     texlive-collection-latexrecommended >= %{texlive_version}
Prefix:         %{_bindir}

%description fig4latex-bin
Binary files of fig4latex

%package findhyph-bin
Version:        %{texlive_version}.%{texlive_release}.svn14758
Release:        0
Summary:        Binary files of findhyph
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-findhyph >= %{texlive_version}
#!BuildIgnore:  texlive-findhyph
Prefix:         %{_bindir}

%description findhyph-bin
Binary files of findhyph

%package fontinst-bin
Version:        %{texlive_version}.%{texlive_release}.svn53554
Release:        0
Summary:        Binary files of fontinst
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-fontinst >= %{texlive_version}
#!BuildIgnore:  texlive-fontinst
Prefix:         %{_bindir}

%description fontinst-bin
Binary files of fontinst

%package fontools-bin
Version:        %{texlive_version}.%{texlive_release}.svn25997
Release:        0
Summary:        Binary files of fontools
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-fontools >= %{texlive_version}
#!BuildIgnore:  texlive-fontools
Prefix:         %{_bindir}

%description fontools-bin
Binary files of fontools

%package fontware-bin
Version:        %{texlive_version}.%{texlive_release}.svn53999
Release:        0
Summary:        Binary files of fontware
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-fontware >= %{texlive_version}
#!BuildIgnore:  texlive-fontware
Prefix:         %{_bindir}

%description fontware-bin
Binary files of fontware

%package fragmaster-bin
Version:        %{texlive_version}.%{texlive_release}.svn13663
Release:        0
Summary:        Binary files of fragmaster
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-fragmaster >= %{texlive_version}
#!BuildIgnore:  texlive-fragmaster
Prefix:         %{_bindir}

%description fragmaster-bin
Binary files of fragmaster

%package getmap-bin
Version:        %{texlive_version}.%{texlive_release}.svn34971
Release:        0
Summary:        Binary files of getmap
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-getmap >= %{texlive_version}
#!BuildIgnore:  texlive-getmap
Prefix:         %{_bindir}

%description getmap-bin
Binary files of getmap

%package git-latexdiff-bin
Version:        %{texlive_version}.%{texlive_release}.svn54732
Release:        0
Summary:        Binary files of git-latexdiff
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-git-latexdiff >= %{texlive_version}
#!BuildIgnore:  texlive-git-latexdiff
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Recommends:     texlive-collection-latexrecommended >= %{texlive_version}
Prefix:         %{_bindir}

%description git-latexdiff-bin
Binary files of git-latexdiff

%package glossaries-bin
Version:        %{texlive_version}.%{texlive_release}.svn37813
Release:        0
Summary:        Binary files of glossaries
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-glossaries >= %{texlive_version}
#!BuildIgnore:  texlive-glossaries
Prefix:         %{_bindir}

%description glossaries-bin
Binary files of glossaries

%package gregoriotex-bin
Version:        %{texlive_version}.%{texlive_release}.svn53999
Release:        0
Summary:        Binary files of gregoriotex
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-gregoriotex >= %{texlive_version}
#!BuildIgnore:  texlive-gregoriotex
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Recommends:     texlive-collection-basic >= %{texlive_version}
Prefix:         %{_bindir}

%description gregoriotex-bin
Binary files of gregoriotex

%package gsftopk-bin
Version:        %{texlive_version}.%{texlive_release}.svn53999
Release:        0
Summary:        Binary files of gsftopk
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-gsftopk >= %{texlive_version}
#!BuildIgnore:  texlive-gsftopk
Prefix:         %{_bindir}

%description gsftopk-bin
Binary files of gsftopk

%package jadetex-bin
Version:        %{texlive_version}.%{texlive_release}.svn3006
Release:        0
Summary:        Binary files of jadetex
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Obsoletes:      texlive-bin-jadetex <= %{texlive_previous}
Requires(pre):  texlive-jadetex >= %{texlive_version}
#!BuildIgnore:  texlive-jadetex
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Recommends:     texlive-collection-basic >= %{texlive_version}
Prefix:         %{_bindir}

%description jadetex-bin
Binary files of jadetex

%package jfmutil-bin
Version:        %{texlive_version}.%{texlive_release}.svn44835
Release:        0
Summary:        Binary files of jfmutil
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-jfmutil >= %{texlive_version}
#!BuildIgnore:  texlive-jfmutil
Prefix:         %{_bindir}

%description jfmutil-bin
Binary files of jfmutil

%package ketcindy-bin
Version:        %{texlive_version}.%{texlive_release}.svn49033
Release:        0
Summary:        Binary files of ketcindy
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-ketcindy >= %{texlive_version}
#!BuildIgnore:  texlive-ketcindy
Prefix:         %{_bindir}

%description ketcindy-bin
Binary files of ketcindy

%package kotex-utils-bin
Version:        %{texlive_version}.%{texlive_release}.svn32101
Release:        0
Summary:        Binary files of kotex-utils
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-kotex-utils >= %{texlive_version}
#!BuildIgnore:  texlive-kotex-utils
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Recommends:     texlive-collection-basic >= %{texlive_version}
Prefix:         %{_bindir}

%description kotex-utils-bin
Binary files of kotex-utils

%package kpathsea-bin
Version:        %{texlive_version}.%{texlive_release}.svn53999
Release:        0
Summary:        Binary files of kpathsea
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):    %{name}-filesystem >= %{texlive_version}
Requires(pre):    /usr/bin/getent
Requires(pre):    /usr/sbin/groupadd
Requires(post):   %{name}-filesystem
Requires(post):   permissions
Requires:       %{name}-gsftopk-bin
Requires(pre):    %{name}-scripts-bin
Requires(verify): %{name}-filesystem
Requires(verify): permissions
Requires(pre):  texlive-kpathsea >= %{texlive_version}
#!BuildIgnore:  texlive-kpathsea
Prefix:         %{_bindir}

%description kpathsea-bin
Binary files of kpathsea

%package l3build-bin
Version:        %{texlive_version}.%{texlive_release}.svn46894
Release:        0
Summary:        Binary files of l3build
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-l3build >= %{texlive_version}
#!BuildIgnore:  texlive-l3build
Prefix:         %{_bindir}

%description l3build-bin
Binary files of l3build

%package lacheck-bin
Version:        %{texlive_version}.%{texlive_release}.svn53999
Release:        0
Summary:        Binary files of lacheck
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-lacheck >= %{texlive_version}
#!BuildIgnore:  texlive-lacheck
Prefix:         %{_bindir}

%description lacheck-bin
Binary files of lacheck

%package latex-bin-dev-bin
Version:        %{texlive_version}.%{texlive_release}.svn53999
Release:        0
Summary:        Binary files of latex-bin-dev
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-latex-bin-dev >= %{texlive_version}
#!BuildIgnore:  texlive-latex-bin-dev
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Recommends:     texlive-collection-latexrecommended >= %{texlive_version}
Prefix:         %{_bindir}

%description latex-bin-dev-bin
Binary files of latex-bin-dev

%package latex-bin-bin
Version:        %{texlive_version}.%{texlive_release}.svn54358
Release:        0
Summary:        Binary files of latex-bin
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-latex-bin >= %{texlive_version}
#!BuildIgnore:  texlive-latex-bin
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Recommends:     texlive-collection-latexrecommended >= %{texlive_version}
Prefix:         %{_bindir}

%description latex-bin-bin
Binary files of latex-bin

%package latex-git-log-bin
Version:        %{texlive_version}.%{texlive_release}.svn30983
Release:        0
Summary:        Binary files of latex-git-log
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-latex-git-log >= %{texlive_version}
#!BuildIgnore:  texlive-latex-git-log
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Recommends:     texlive-collection-latexrecommended >= %{texlive_version}
Prefix:         %{_bindir}

%description latex-git-log-bin
Binary files of latex-git-log

%package latex-papersize-bin
Version:        %{texlive_version}.%{texlive_release}.svn42296
Release:        0
Summary:        Binary files of latex-papersize
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-latex-papersize >= %{texlive_version}
#!BuildIgnore:  texlive-latex-papersize
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Recommends:     texlive-collection-latexrecommended >= %{texlive_version}
Prefix:         %{_bindir}

%description latex-papersize-bin
Binary files of latex-papersize

%package latex2man-bin
Version:        %{texlive_version}.%{texlive_release}.svn13663
Release:        0
Summary:        Binary files of latex2man
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-latex2man >= %{texlive_version}
#!BuildIgnore:  texlive-latex2man
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Recommends:     texlive-collection-latexrecommended >= %{texlive_version}
Prefix:         %{_bindir}

%description latex2man-bin
Binary files of latex2man

%package latex2nemeth-bin
Version:        %{texlive_version}.%{texlive_release}.svn42300
Release:        0
Summary:        Binary files of latex2nemeth
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-latex2nemeth >= %{texlive_version}
#!BuildIgnore:  texlive-latex2nemeth
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Recommends:     texlive-collection-latexrecommended >= %{texlive_version}
Prefix:         %{_bindir}

%description latex2nemeth-bin
Binary files of latex2nemeth

%package latexdiff-bin
Version:        %{texlive_version}.%{texlive_release}.svn16420
Release:        0
Summary:        Binary files of latexdiff
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-latexdiff >= %{texlive_version}
#!BuildIgnore:  texlive-latexdiff
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Recommends:     texlive-collection-latexrecommended >= %{texlive_version}
Prefix:         %{_bindir}

%description latexdiff-bin
Binary files of latexdiff

%package latexfileversion-bin
Version:        %{texlive_version}.%{texlive_release}.svn25012
Release:        0
Summary:        Binary files of latexfileversion
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-latexfileversion >= %{texlive_version}
#!BuildIgnore:  texlive-latexfileversion
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Recommends:     texlive-collection-latexrecommended >= %{texlive_version}
Prefix:         %{_bindir}

%description latexfileversion-bin
Binary files of latexfileversion

%package latexindent-bin
Version:        %{texlive_version}.%{texlive_release}.svn32150
Release:        0
Summary:        Binary files of latexindent
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-latexindent >= %{texlive_version}
#!BuildIgnore:  texlive-latexindent
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Recommends:     texlive-collection-latexrecommended >= %{texlive_version}
Prefix:         %{_bindir}

%description latexindent-bin
Binary files of latexindent

%package latexmk-bin
Version:        %{texlive_version}.%{texlive_release}.svn10937
Release:        0
Summary:        Binary files of latexmk
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-latexmk >= %{texlive_version}
#!BuildIgnore:  texlive-latexmk
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Recommends:     texlive-collection-latexrecommended >= %{texlive_version}
Prefix:         %{_bindir}

%description latexmk-bin
Binary files of latexmk

%package latexpand-bin
Version:        %{texlive_version}.%{texlive_release}.svn27025
Release:        0
Summary:        Binary files of latexpand
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-latexpand >= %{texlive_version}
#!BuildIgnore:  texlive-latexpand
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Recommends:     texlive-collection-latexrecommended >= %{texlive_version}
Prefix:         %{_bindir}

%description latexpand-bin
Binary files of latexpand

%package lcdftypetools-bin
Version:        %{texlive_version}.%{texlive_release}.svn53999
Release:        0
Summary:        Binary files of lcdftypetools
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
%if %{with lcdf_typetools}
Conflicts:      lcdf-typetools
%else
Requires:       lcdf-typetools
%endif
Requires(pre):  texlive-lcdftypetools >= %{texlive_version}
#!BuildIgnore:  texlive-lcdftypetools
Prefix:         %{_bindir}

%description lcdftypetools-bin
Binary files of lcdftypetools

%package lilyglyphs-bin
Version:        %{texlive_version}.%{texlive_release}.svn31696
Release:        0
Summary:        Binary files of lilyglyphs
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-lilyglyphs >= %{texlive_version}
#!BuildIgnore:  texlive-lilyglyphs
Prefix:         %{_bindir}

%description lilyglyphs-bin
Binary files of lilyglyphs

%package listbib-bin
Version:        %{texlive_version}.%{texlive_release}.svn26126
Release:        0
Summary:        Binary files of listbib
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-listbib >= %{texlive_version}
#!BuildIgnore:  texlive-listbib
Prefix:         %{_bindir}

%description listbib-bin
Binary files of listbib

%package listings-ext-bin
Version:        %{texlive_version}.%{texlive_release}.svn15093
Release:        0
Summary:        Binary files of listings-ext
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-listings-ext >= %{texlive_version}
#!BuildIgnore:  texlive-listings-ext
Prefix:         %{_bindir}

%description listings-ext-bin
Binary files of listings-ext

%package lollipop-bin
Version:        %{texlive_version}.%{texlive_release}.svn41465
Release:        0
Summary:        Binary files of lollipop
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-lollipop >= %{texlive_version}
#!BuildIgnore:  texlive-lollipop
Prefix:         %{_bindir}

%description lollipop-bin
Binary files of lollipop

%package ltxfileinfo-bin
Version:        %{texlive_version}.%{texlive_release}.svn29005
Release:        0
Summary:        Binary files of ltxfileinfo
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-ltxfileinfo >= %{texlive_version}
#!BuildIgnore:  texlive-ltxfileinfo
Prefix:         %{_bindir}

%description ltxfileinfo-bin
Binary files of ltxfileinfo

%package ltximg-bin
Version:        %{texlive_version}.%{texlive_release}.svn32346
Release:        0
Summary:        Binary files of ltximg
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-ltximg >= %{texlive_version}
#!BuildIgnore:  texlive-ltximg
Prefix:         %{_bindir}

%description ltximg-bin
Binary files of ltximg

%package luahbtex-bin
Version:        %{texlive_version}.%{texlive_release}.svn54358
Release:        0
Summary:        Binary files of luahbtex
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-luahbtex >= %{texlive_version}
#!BuildIgnore:  texlive-luahbtex
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Recommends:     texlive-collection-basic >= %{texlive_version}
Prefix:         %{_bindir}

%description luahbtex-bin
Binary files of luahbtex

%package luajittex-bin
Version:        %{texlive_version}.%{texlive_release}.svn54358
Release:        0
Summary:        Binary files of luajittex
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-luajittex >= %{texlive_version}
#!BuildIgnore:  texlive-luajittex
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Recommends:     texlive-collection-basic >= %{texlive_version}
Prefix:         %{_bindir}

%description luajittex-bin
Binary files of luajittex

%package luaotfload-bin
Version:        %{texlive_version}.%{texlive_release}.svn34647
Release:        0
Summary:        Binary files of luaotfload
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-luaotfload >= %{texlive_version}
#!BuildIgnore:  texlive-luaotfload
Prefix:         %{_bindir}

%description luaotfload-bin
Binary files of luaotfload

%package luatex-bin
Version:        %{texlive_version}.%{texlive_release}.svn54358
Release:        0
Summary:        Binary files of luatex
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-luatex >= %{texlive_version}
#!BuildIgnore:  texlive-luatex
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Recommends:     texlive-collection-luatex >= %{texlive_version}
Prefix:         %{_bindir}

%description luatex-bin
Binary files of luatex

%package lwarp-bin
Version:        %{texlive_version}.%{texlive_release}.svn43292
Release:        0
Summary:        Binary files of lwarp
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-lwarp >= %{texlive_version}
#!BuildIgnore:  texlive-lwarp
Prefix:         %{_bindir}

%description lwarp-bin
Binary files of lwarp

%package m-tx-bin
Version:        %{texlive_version}.%{texlive_release}.svn50281
Release:        0
Summary:        Binary files of m-tx
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-m-tx >= %{texlive_version}
#!BuildIgnore:  texlive-m-tx
Prefix:         %{_bindir}

%description m-tx-bin
Binary files of m-tx

%package make4ht-bin
Version:        %{texlive_version}.%{texlive_release}.svn37750
Release:        0
Summary:        Binary files of make4ht
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-make4ht >= %{texlive_version}
#!BuildIgnore:  texlive-make4ht
Prefix:         %{_bindir}

%description make4ht-bin
Binary files of make4ht

%package makedtx-bin
Version:        %{texlive_version}.%{texlive_release}.svn38769
Release:        0
Summary:        Binary files of makedtx
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-makedtx >= %{texlive_version}
#!BuildIgnore:  texlive-makedtx
Prefix:         %{_bindir}

%description makedtx-bin
Binary files of makedtx

%package makeindex-bin
Version:        %{texlive_version}.%{texlive_release}.svn53999
Release:        0
Summary:        Binary files of makeindex
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-makeindex >= %{texlive_version}
#!BuildIgnore:  texlive-makeindex
Prefix:         %{_bindir}

%description makeindex-bin
Binary files of makeindex

%package match_parens-bin
Version:        %{texlive_version}.%{texlive_release}.svn23500
Release:        0
Summary:        Binary files of match_parens
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-match_parens >= %{texlive_version}
#!BuildIgnore:  texlive-match_parens
Prefix:         %{_bindir}

%description match_parens-bin
Binary files of match_parens

%package mathspic-bin
Version:        %{texlive_version}.%{texlive_release}.svn23661
Release:        0
Summary:        Binary files of mathspic
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-mathspic >= %{texlive_version}
#!BuildIgnore:  texlive-mathspic
Prefix:         %{_bindir}

%description mathspic-bin
Binary files of mathspic

%package metafont-bin
Version:        %{texlive_version}.%{texlive_release}.svn53999
Release:        0
Summary:        Binary files of metafont
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-metafont >= %{texlive_version}
#!BuildIgnore:  texlive-metafont
Prefix:         %{_bindir}

%description metafont-bin
Binary files of metafont

%package metapost-bin
Version:        %{texlive_version}.%{texlive_release}.svn54358
Release:        0
Summary:        Binary files of metapost
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Obsoletes:      texlive-bin-metapost <= %{texlive_previous}
Requires(pre):  texlive-metapost >= %{texlive_version}
#!BuildIgnore:  texlive-metapost
Prefix:         %{_bindir}

%description metapost-bin
Binary files of metapost

%package mex-bin
Version:        %{texlive_version}.%{texlive_release}.svn3006
Release:        0
Summary:        Binary files of mex
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-mex >= %{texlive_version}
#!BuildIgnore:  texlive-mex
Prefix:         %{_bindir}

%description mex-bin
Binary files of mex

%package mf2pt1-bin
Version:        %{texlive_version}.%{texlive_release}.svn23406
Release:        0
Summary:        Binary files of mf2pt1
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-mf2pt1 >= %{texlive_version}
#!BuildIgnore:  texlive-mf2pt1
Prefix:         %{_bindir}

%description mf2pt1-bin
Binary files of mf2pt1

%package mflua-bin
Version:        %{texlive_version}.%{texlive_release}.svn53999
Release:        0
Summary:        Binary files of mflua
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-mflua >= %{texlive_version}
#!BuildIgnore:  texlive-mflua
Prefix:         %{_bindir}

%description mflua-bin
Binary files of mflua

%package mfware-bin
Version:        %{texlive_version}.%{texlive_release}.svn53999
Release:        0
Summary:        Binary files of mfware
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-mfware >= %{texlive_version}
#!BuildIgnore:  texlive-mfware
Prefix:         %{_bindir}

%description mfware-bin
Binary files of mfware

%package mkgrkindex-bin
Version:        %{texlive_version}.%{texlive_release}.svn14428
Release:        0
Summary:        Binary files of mkgrkindex
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-mkgrkindex >= %{texlive_version}
#!BuildIgnore:  texlive-mkgrkindex
Prefix:         %{_bindir}

%description mkgrkindex-bin
Binary files of mkgrkindex

%package mkjobtexmf-bin
Version:        %{texlive_version}.%{texlive_release}.svn8457
Release:        0
Summary:        Binary files of mkjobtexmf
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-mkjobtexmf >= %{texlive_version}
#!BuildIgnore:  texlive-mkjobtexmf
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Recommends:     texlive-collection-basic >= %{texlive_version}
Prefix:         %{_bindir}

%description mkjobtexmf-bin
Binary files of mkjobtexmf

%package mkpic-bin
Version:        %{texlive_version}.%{texlive_release}.svn33688
Release:        0
Summary:        Binary files of mkpic
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-mkpic >= %{texlive_version}
#!BuildIgnore:  texlive-mkpic
Prefix:         %{_bindir}

%description mkpic-bin
Binary files of mkpic

%package mltex-bin
Version:        %{texlive_version}.%{texlive_release}.svn3006
Release:        0
Summary:        Binary files of mltex
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-mltex >= %{texlive_version}
#!BuildIgnore:  texlive-mltex
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Recommends:     texlive-collection-basic >= %{texlive_version}
Prefix:         %{_bindir}

%description mltex-bin
Binary files of mltex

%package mptopdf-bin
Version:        %{texlive_version}.%{texlive_release}.svn18674
Release:        0
Summary:        Binary files of mptopdf
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-mptopdf >= %{texlive_version}
#!BuildIgnore:  texlive-mptopdf
Prefix:         %{_bindir}

%description mptopdf-bin
Binary files of mptopdf

%package multibibliography-bin
Version:        %{texlive_version}.%{texlive_release}.svn30534
Release:        0
Summary:        Binary files of multibibliography
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-multibibliography >= %{texlive_version}
#!BuildIgnore:  texlive-multibibliography
Prefix:         %{_bindir}

%description multibibliography-bin
Binary files of multibibliography

%package musixtex-bin
Version:        %{texlive_version}.%{texlive_release}.svn37026
Release:        0
Summary:        Binary files of musixtex
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Obsoletes:      texlive-bin-musictex <= %{texlive_previous}
Requires:       texlive-m-tx-bin >= %{texlive_version}
Requires:       texlive-pmx-bin >= %{texlive_version}
Requires(pre):  texlive-musixtex >= %{texlive_version}
#!BuildIgnore:  texlive-musixtex
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Recommends:     texlive-collection-basic >= %{texlive_version}
Prefix:         %{_bindir}

%description musixtex-bin
Binary files of musixtex

%package musixtnt-bin
Version:        %{texlive_version}.%{texlive_release}.svn50281
Release:        0
Summary:        Binary files of musixtnt
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-musixtnt >= %{texlive_version}
#!BuildIgnore:  texlive-musixtnt
Prefix:         %{_bindir}

%description musixtnt-bin
Binary files of musixtnt

%package omegaware-bin
Version:        %{texlive_version}.%{texlive_release}.svn53999
Release:        0
Summary:        Binary files of omegaware
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Obsoletes:      texlive-bin-omega <= %{texlive_previous}
Requires:       texlive-uptex-bin >= %{texlive_version}
Requires(pre):  texlive-omegaware >= %{texlive_version}
#!BuildIgnore:  texlive-omegaware
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Recommends:     texlive-collection-omega >= %{texlive_version}
Prefix:         %{_bindir}

%description omegaware-bin
Binary files of omegaware

%package optex-bin
Version:        %{texlive_version}.%{texlive_release}.svn53804
Release:        0
Summary:        Binary files of optex
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-optex >= %{texlive_version}
#!BuildIgnore:  texlive-optex
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Recommends:     texlive-collection-basic >= %{texlive_version}
Prefix:         %{_bindir}

%description optex-bin
Binary files of optex

%package patgen-bin
Version:        %{texlive_version}.%{texlive_release}.svn53999
Release:        0
Summary:        Binary files of patgen
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-patgen >= %{texlive_version}
#!BuildIgnore:  texlive-patgen
Prefix:         %{_bindir}

%description patgen-bin
Binary files of patgen

%package pax-bin
Version:        %{texlive_version}.%{texlive_release}.svn10843
Release:        0
Summary:        Binary files of pax
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-pax >= %{texlive_version}
#!BuildIgnore:  texlive-pax
Prefix:         %{_bindir}

%description pax-bin
Binary files of pax

%package pdfbook2-bin
Version:        %{texlive_version}.%{texlive_release}.svn37537
Release:        0
Summary:        Binary files of pdfbook2
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-pdfbook2 >= %{texlive_version}
#!BuildIgnore:  texlive-pdfbook2
Prefix:         %{_bindir}

%description pdfbook2-bin
Binary files of pdfbook2

%package pdfcrop-bin
Version:        %{texlive_version}.%{texlive_release}.svn14387
Release:        0
Summary:        Binary files of pdfcrop
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-pdfcrop >= %{texlive_version}
#!BuildIgnore:  texlive-pdfcrop
Prefix:         %{_bindir}

%description pdfcrop-bin
Binary files of pdfcrop

%package pdfjam-bin
Version:        %{texlive_version}.%{texlive_release}.svn52858
Release:        0
Summary:        Binary files of pdfjam
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-pdfjam >= %{texlive_version}
#!BuildIgnore:  texlive-pdfjam
Prefix:         %{_bindir}

%description pdfjam-bin
Binary files of pdfjam

%package pdflatexpicscale-bin
Version:        %{texlive_version}.%{texlive_release}.svn41779
Release:        0
Summary:        Binary files of pdflatexpicscale
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-pdflatexpicscale >= %{texlive_version}
#!BuildIgnore:  texlive-pdflatexpicscale
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Recommends:     texlive-collection-latexrecommended >= %{texlive_version}
Prefix:         %{_bindir}

%description pdflatexpicscale-bin
Binary files of pdflatexpicscale

%package pdftex-quiet-bin
Version:        %{texlive_version}.%{texlive_release}.svn49140
Release:        0
Summary:        Binary files of pdftex-quiet
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-pdftex-quiet >= %{texlive_version}
#!BuildIgnore:  texlive-pdftex-quiet
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Recommends:     texlive-collection-basic >= %{texlive_version}
Prefix:         %{_bindir}

%description pdftex-quiet-bin
Binary files of pdftex-quiet

%package pdftex-bin
Version:        %{texlive_version}.%{texlive_release}.svn53999
Release:        0
Summary:        Binary files of pdftex
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-pdftex >= %{texlive_version}
#!BuildIgnore:  texlive-pdftex
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Recommends:     texlive-collection-basic >= %{texlive_version}
Prefix:         %{_bindir}

%description pdftex-bin
Binary files of pdftex

%package pdftosrc-bin
Version:        %{texlive_version}.%{texlive_release}.svn53999
Release:        0
Summary:        Binary files of pdftosrc
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-pdftosrc >= %{texlive_version}
#!BuildIgnore:  texlive-pdftosrc
Prefix:         %{_bindir}

%description pdftosrc-bin
Binary files of pdftosrc

%package pdfxup-bin
Version:        %{texlive_version}.%{texlive_release}.svn40690
Release:        0
Summary:        Binary files of pdfxup
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-pdfxup >= %{texlive_version}
#!BuildIgnore:  texlive-pdfxup
Prefix:         %{_bindir}

%description pdfxup-bin
Binary files of pdfxup

%package pedigree-perl-bin
Version:        %{texlive_version}.%{texlive_release}.svn25962
Release:        0
Summary:        Binary files of pedigree-perl
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-pedigree-perl >= %{texlive_version}
#!BuildIgnore:  texlive-pedigree-perl
Prefix:         %{_bindir}

%description pedigree-perl-bin
Binary files of pedigree-perl

%package perltex-bin
Version:        %{texlive_version}.%{texlive_release}.svn16181
Release:        0
Summary:        Binary files of perltex
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-perltex >= %{texlive_version}
#!BuildIgnore:  texlive-perltex
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Recommends:     texlive-collection-basic >= %{texlive_version}
Prefix:         %{_bindir}

%description perltex-bin
Binary files of perltex

%package petri-nets-bin
Version:        %{texlive_version}.%{texlive_release}.svn39165
Release:        0
Summary:        Binary files of petri-nets
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-petri-nets >= %{texlive_version}
#!BuildIgnore:  texlive-petri-nets
Prefix:         %{_bindir}

%description petri-nets-bin
Binary files of petri-nets

%package pfarrei-bin
Version:        %{texlive_version}.%{texlive_release}.svn29348
Release:        0
Summary:        Binary files of pfarrei
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-pfarrei >= %{texlive_version}
#!BuildIgnore:  texlive-pfarrei
Prefix:         %{_bindir}

%description pfarrei-bin
Binary files of pfarrei

%package pkfix-helper-bin
Version:        %{texlive_version}.%{texlive_release}.svn13663
Release:        0
Summary:        Binary files of pkfix-helper
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-pkfix-helper >= %{texlive_version}
#!BuildIgnore:  texlive-pkfix-helper
Prefix:         %{_bindir}

%description pkfix-helper-bin
Binary files of pkfix-helper

%package pkfix-bin
Version:        %{texlive_version}.%{texlive_release}.svn13364
Release:        0
Summary:        Binary files of pkfix
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-pkfix >= %{texlive_version}
#!BuildIgnore:  texlive-pkfix
Prefix:         %{_bindir}

%description pkfix-bin
Binary files of pkfix

%package platex-bin
Version:        %{texlive_version}.%{texlive_release}.svn52800
Release:        0
Summary:        Binary files of platex
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-platex >= %{texlive_version}
#!BuildIgnore:  texlive-platex
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Recommends:     texlive-collection-latexrecommended >= %{texlive_version}
Prefix:         %{_bindir}

%description platex-bin
Binary files of platex

%package pmx-bin
Version:        %{texlive_version}.%{texlive_release}.svn54410
Release:        0
Summary:        Binary files of pmx
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-pmx >= %{texlive_version}
#!BuildIgnore:  texlive-pmx
Prefix:         %{_bindir}

%description pmx-bin
Binary files of pmx

%package pmxchords-bin
Version:        %{texlive_version}.%{texlive_release}.svn32405
Release:        0
Summary:        Binary files of pmxchords
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-pmxchords >= %{texlive_version}
#!BuildIgnore:  texlive-pmxchords
Prefix:         %{_bindir}

%description pmxchords-bin
Binary files of pmxchords

%package ps2eps-bin
Version:        %{texlive_version}.%{texlive_release}.svn50281
Release:        0
Summary:        Binary files of ps2eps
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-ps2eps >= %{texlive_version}
#!BuildIgnore:  texlive-ps2eps
Prefix:         %{_bindir}

%description ps2eps-bin
Binary files of ps2eps

%package ps2pk-bin
Version:        %{texlive_version}.%{texlive_release}.svn53999
Release:        0
Summary:        Binary files of ps2pk
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Obsoletes:      texlive-ps2pkm-bin <= 2014
Requires(pre):  texlive-ps2pk >= %{texlive_version}
#!BuildIgnore:  texlive-ps2pk
Prefix:         %{_bindir}

%description ps2pk-bin
Binary files of ps2pk

%package pst-pdf-bin
Version:        %{texlive_version}.%{texlive_release}.svn7838
Release:        0
Summary:        Binary files of pst-pdf
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-pst-pdf >= %{texlive_version}
#!BuildIgnore:  texlive-pst-pdf
Prefix:         %{_bindir}

%description pst-pdf-bin
Binary files of pst-pdf

%package pst2pdf-bin
Version:        %{texlive_version}.%{texlive_release}.svn29333
Release:        0
Summary:        Binary files of pst2pdf
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-pst2pdf >= %{texlive_version}
#!BuildIgnore:  texlive-pst2pdf
Prefix:         %{_bindir}

%description pst2pdf-bin
Binary files of pst2pdf

%package ptex-fontmaps-bin
Version:        %{texlive_version}.%{texlive_release}.svn44206
Release:        0
Summary:        Binary files of ptex-fontmaps
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-ptex-fontmaps >= %{texlive_version}
#!BuildIgnore:  texlive-ptex-fontmaps
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Recommends:     texlive-collection-basic >= %{texlive_version}
Prefix:         %{_bindir}

%description ptex-fontmaps-bin
Binary files of ptex-fontmaps

%package ptex-bin
Version:        %{texlive_version}.%{texlive_release}.svn54358
Release:        0
Summary:        Binary files of ptex
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-ptex >= %{texlive_version}
#!BuildIgnore:  texlive-ptex
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Recommends:     texlive-collection-basic >= %{texlive_version}
Prefix:         %{_bindir}

%description ptex-bin
Binary files of ptex

%package ptex2pdf-bin
Version:        %{texlive_version}.%{texlive_release}.svn29335
Release:        0
Summary:        Binary files of ptex2pdf
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-ptex2pdf >= %{texlive_version}
#!BuildIgnore:  texlive-ptex2pdf
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Recommends:     texlive-collection-basic >= %{texlive_version}
Prefix:         %{_bindir}

%description ptex2pdf-bin
Binary files of ptex2pdf

%package purifyeps-bin
Version:        %{texlive_version}.%{texlive_release}.svn13663
Release:        0
Summary:        Binary files of purifyeps
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-purifyeps >= %{texlive_version}
#!BuildIgnore:  texlive-purifyeps
Prefix:         %{_bindir}

%description purifyeps-bin
Binary files of purifyeps

%package pygmentex-bin
Version:        %{texlive_version}.%{texlive_release}.svn34996
Release:        0
Summary:        Binary files of pygmentex
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-pygmentex >= %{texlive_version}
#!BuildIgnore:  texlive-pygmentex
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Recommends:     texlive-collection-basic >= %{texlive_version}
Prefix:         %{_bindir}

%description pygmentex-bin
Binary files of pygmentex

%package pythontex-bin
Version:        %{texlive_version}.%{texlive_release}.svn31638
Release:        0
Summary:        Binary files of pythontex
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-pythontex >= %{texlive_version}
#!BuildIgnore:  texlive-pythontex
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Recommends:     texlive-collection-basic >= %{texlive_version}
Prefix:         %{_bindir}

%description pythontex-bin
Binary files of pythontex

%package rubik-bin
Version:        %{texlive_version}.%{texlive_release}.svn32919
Release:        0
Summary:        Binary files of rubik
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-rubik >= %{texlive_version}
#!BuildIgnore:  texlive-rubik
Prefix:         %{_bindir}

%description rubik-bin
Binary files of rubik

%package seetexk-bin
Version:        %{texlive_version}.%{texlive_release}.svn53999
Release:        0
Summary:        Binary files of seetexk
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-seetexk >= %{texlive_version}
#!BuildIgnore:  texlive-seetexk
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Recommends:     texlive-collection-basic >= %{texlive_version}
Prefix:         %{_bindir}

%description seetexk-bin
Binary files of seetexk

%package splitindex-bin
Version:        %{texlive_version}.%{texlive_release}.svn29688
Release:        0
Summary:        Binary files of splitindex
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-splitindex >= %{texlive_version}
#!BuildIgnore:  texlive-splitindex
Prefix:         %{_bindir}

%description splitindex-bin
Binary files of splitindex

%package srcredact-bin
Version:        %{texlive_version}.%{texlive_release}.svn38710
Release:        0
Summary:        Binary files of srcredact
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-srcredact >= %{texlive_version}
#!BuildIgnore:  texlive-srcredact
Prefix:         %{_bindir}

%description srcredact-bin
Binary files of srcredact

%package sty2dtx-bin
Version:        %{texlive_version}.%{texlive_release}.svn21215
Release:        0
Summary:        Binary files of sty2dtx
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-sty2dtx >= %{texlive_version}
#!BuildIgnore:  texlive-sty2dtx
Prefix:         %{_bindir}

%description sty2dtx-bin
Binary files of sty2dtx

%package svn-multi-bin
Version:        %{texlive_version}.%{texlive_release}.svn13663
Release:        0
Summary:        Binary files of svn-multi
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-svn-multi >= %{texlive_version}
#!BuildIgnore:  texlive-svn-multi
Prefix:         %{_bindir}

%description svn-multi-bin
Binary files of svn-multi

%package synctex-bin
Version:        %{texlive_version}.%{texlive_release}.svn50281
Release:        0
Summary:        Binary files of synctex
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-synctex >= %{texlive_version}
#!BuildIgnore:  texlive-synctex
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Recommends:     texlive-collection-basic >= %{texlive_version}
Prefix:         %{_bindir}

%description synctex-bin
Binary files of synctex

%package tex-bin
Version:        %{texlive_version}.%{texlive_release}.svn53999
Release:        0
Summary:        Binary files of tex
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-tex >= %{texlive_version}
#!BuildIgnore:  texlive-tex
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Recommends:     texlive-collection-basic >= %{texlive_version}
Prefix:         %{_bindir}

%description tex-bin
Binary files of tex

%package tex4ebook-bin
Version:        %{texlive_version}.%{texlive_release}.svn37771
Release:        0
Summary:        Binary files of tex4ebook
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-tex4ebook >= %{texlive_version}
#!BuildIgnore:  texlive-tex4ebook
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Recommends:     texlive-collection-basic >= %{texlive_version}
Prefix:         %{_bindir}

%description tex4ebook-bin
Binary files of tex4ebook

%package tex4ht-bin
Version:        %{texlive_version}.%{texlive_release}.svn53999
Release:        0
Summary:        Binary files of tex4ht
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Obsoletes:      texlive-bin-tex4ht <= %{texlive_previous}
Conflicts:      ht
Requires(pre):  texlive-tex4ht >= %{texlive_version}
#!BuildIgnore:  texlive-tex4ht
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Recommends:     texlive-collection-basic >= %{texlive_version}
Prefix:         %{_bindir}

%description tex4ht-bin
Binary files of tex4ht

%package texcount-bin
Version:        %{texlive_version}.%{texlive_release}.svn13013
Release:        0
Summary:        Binary files of texcount
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-texcount >= %{texlive_version}
#!BuildIgnore:  texlive-texcount
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Recommends:     texlive-collection-basic >= %{texlive_version}
Prefix:         %{_bindir}

%description texcount-bin
Binary files of texcount

%package texdef-bin
Version:        %{texlive_version}.%{texlive_release}.svn45011
Release:        0
Summary:        Binary files of texdef
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-texdef >= %{texlive_version}
#!BuildIgnore:  texlive-texdef
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Recommends:     texlive-collection-basic >= %{texlive_version}
Prefix:         %{_bindir}

%description texdef-bin
Binary files of texdef

%package texdiff-bin
Version:        %{texlive_version}.%{texlive_release}.svn15506
Release:        0
Summary:        Binary files of texdiff
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-texdiff >= %{texlive_version}
#!BuildIgnore:  texlive-texdiff
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Recommends:     texlive-collection-basic >= %{texlive_version}
Prefix:         %{_bindir}

%description texdiff-bin
Binary files of texdiff

%package texdirflatten-bin
Version:        %{texlive_version}.%{texlive_release}.svn12782
Release:        0
Summary:        Binary files of texdirflatten
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-texdirflatten >= %{texlive_version}
#!BuildIgnore:  texlive-texdirflatten
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Recommends:     texlive-collection-basic >= %{texlive_version}
Prefix:         %{_bindir}

%description texdirflatten-bin
Binary files of texdirflatten

%package texdoc-bin
Version:        %{texlive_version}.%{texlive_release}.svn47948
Release:        0
Summary:        Binary files of texdoc
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-texdoc >= %{texlive_version}
#!BuildIgnore:  texlive-texdoc
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Recommends:     texlive-collection-basic >= %{texlive_version}
Prefix:         %{_bindir}

%description texdoc-bin
Binary files of texdoc

%package texdoctk-bin
Version:        %{texlive_version}.%{texlive_release}.svn29741
Release:        0
Summary:        Binary files of texdoctk
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-texdoctk >= %{texlive_version}
#!BuildIgnore:  texlive-texdoctk
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Recommends:     texlive-collection-basic >= %{texlive_version}
Prefix:         %{_bindir}

%description texdoctk-bin
Binary files of texdoctk

%package texfot-bin
Version:        %{texlive_version}.%{texlive_release}.svn33155
Release:        0
Summary:        Binary files of texfot
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-texfot >= %{texlive_version}
#!BuildIgnore:  texlive-texfot
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Recommends:     texlive-collection-basic >= %{texlive_version}
Prefix:         %{_bindir}

%description texfot-bin
Binary files of texfot

%package -n texlive-scripts-extra-bin
Version:        %{texlive_version}.%{texlive_release}.svn53577
Release:        0
Summary:        Binary files of texlive-scripts-extra
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Obsoletes:      texlive-pdftools-bin <= %{texlive_previous}
Obsoletes:      texlive-pstools-bin <= %{texlive_previous}
Requires(pre):  texlive-scripts-extra >= %{texlive_version}
#!BuildIgnore:  texlive-scripts-extra
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Recommends:     texlive-collection-basic >= %{texlive_version}
Prefix:         %{_bindir}

%description -n texlive-scripts-extra-bin
Binary files of texlive-scripts-extra

%package -n texlive-scripts-bin
Version:        %{texlive_version}.%{texlive_release}.svn54807
Release:        0
Summary:        Binary files of texlive-scripts
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Obsoletes:      texlive-tetex-bin <= %{texlive_previous}
Obsoletes:      tlshell-bin <= %{texlive_previous}
Requires(pre):  texlive-scripts >= %{texlive_version}
#!BuildIgnore:  texlive-scripts
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Recommends:     texlive-collection-basic >= %{texlive_version}
Prefix:         %{_bindir}

%description -n texlive-scripts-bin
Binary files of texlive-scripts

%package texliveonfly-bin
Version:        %{texlive_version}.%{texlive_release}.svn24062
Release:        0
Summary:        Binary files of texliveonfly
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-texliveonfly >= %{texlive_version}
#!BuildIgnore:  texlive-texliveonfly
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Recommends:     texlive-collection-basic >= %{texlive_version}
Prefix:         %{_bindir}

%description texliveonfly-bin
Binary files of texliveonfly

%package texloganalyser-bin
Version:        %{texlive_version}.%{texlive_release}.svn13663
Release:        0
Summary:        Binary files of texloganalyser
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-texloganalyser >= %{texlive_version}
#!BuildIgnore:  texlive-texloganalyser
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Recommends:     texlive-collection-basic >= %{texlive_version}
Prefix:         %{_bindir}

%description texloganalyser-bin
Binary files of texloganalyser

%package texosquery-bin
Version:        %{texlive_version}.%{texlive_release}.svn43596
Release:        0
Summary:        Binary files of texosquery
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-texosquery >= %{texlive_version}
#!BuildIgnore:  texlive-texosquery
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Recommends:     texlive-collection-basic >= %{texlive_version}
Prefix:         %{_bindir}

%description texosquery-bin
Binary files of texosquery

%package texplate-bin
Version:        %{texlive_version}.%{texlive_release}.svn53444
Release:        0
Summary:        Binary files of texplate
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-texplate >= %{texlive_version}
#!BuildIgnore:  texlive-texplate
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Recommends:     texlive-collection-basic >= %{texlive_version}
Prefix:         %{_bindir}

%description texplate-bin
Binary files of texplate

%package texsis-bin
Version:        %{texlive_version}.%{texlive_release}.svn3006
Release:        0
Summary:        Binary files of texsis
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-texsis >= %{texlive_version}
#!BuildIgnore:  texlive-texsis
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Recommends:     texlive-collection-basic >= %{texlive_version}
Prefix:         %{_bindir}

%description texsis-bin
Binary files of texsis

%package texware-bin
Version:        %{texlive_version}.%{texlive_release}.svn53999
Release:        0
Summary:        Binary files of texware
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-texware >= %{texlive_version}
#!BuildIgnore:  texlive-texware
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Recommends:     texlive-collection-basic >= %{texlive_version}
Prefix:         %{_bindir}

%description texware-bin
Binary files of texware

%package thumbpdf-bin
Version:        %{texlive_version}.%{texlive_release}.svn6898
Release:        0
Summary:        Binary files of thumbpdf
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-thumbpdf >= %{texlive_version}
#!BuildIgnore:  texlive-thumbpdf
Prefix:         %{_bindir}

%description thumbpdf-bin
Binary files of thumbpdf

%package tie-bin
Version:        %{texlive_version}.%{texlive_release}.svn53999
Release:        0
Summary:        Binary files of tie
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-tie >= %{texlive_version}
#!BuildIgnore:  texlive-tie
Prefix:         %{_bindir}

%description tie-bin
Binary files of tie

%package tpic2pdftex-bin
Version:        %{texlive_version}.%{texlive_release}.svn50281
Release:        0
Summary:        Binary files of tpic2pdftex
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-tpic2pdftex >= %{texlive_version}
#!BuildIgnore:  texlive-tpic2pdftex
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Recommends:     texlive-collection-basic >= %{texlive_version}
Prefix:         %{_bindir}

%description tpic2pdftex-bin
Binary files of tpic2pdftex

%package ttfutils-bin
Version:        %{texlive_version}.%{texlive_release}.svn53999
Release:        0
Summary:        Binary files of ttfutils
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-ttfutils >= %{texlive_version}
#!BuildIgnore:  texlive-ttfutils
Prefix:         %{_bindir}

%description ttfutils-bin
Binary files of ttfutils

%package typeoutfileinfo-bin
Version:        %{texlive_version}.%{texlive_release}.svn25648
Release:        0
Summary:        Binary files of typeoutfileinfo
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-typeoutfileinfo >= %{texlive_version}
#!BuildIgnore:  texlive-typeoutfileinfo
Prefix:         %{_bindir}

%description typeoutfileinfo-bin
Binary files of typeoutfileinfo

%package ulqda-bin
Version:        %{texlive_version}.%{texlive_release}.svn13663
Release:        0
Summary:        Binary files of ulqda
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-ulqda >= %{texlive_version}
#!BuildIgnore:  texlive-ulqda
Prefix:         %{_bindir}

%description ulqda-bin
Binary files of ulqda

%package uplatex-bin
Version:        %{texlive_version}.%{texlive_release}.svn52800
Release:        0
Summary:        Binary files of uplatex
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-uplatex >= %{texlive_version}
#!BuildIgnore:  texlive-uplatex
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Recommends:     texlive-collection-latexrecommended >= %{texlive_version}
Prefix:         %{_bindir}

%description uplatex-bin
Binary files of uplatex

%package uptex-bin
Version:        %{texlive_version}.%{texlive_release}.svn54358
Release:        0
Summary:        Binary files of uptex
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-uptex >= %{texlive_version}
#!BuildIgnore:  texlive-uptex
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Recommends:     texlive-collection-basic >= %{texlive_version}
Prefix:         %{_bindir}

%description uptex-bin
Binary files of uptex

%package urlbst-bin
Version:        %{texlive_version}.%{texlive_release}.svn23262
Release:        0
Summary:        Binary files of urlbst
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-urlbst >= %{texlive_version}
#!BuildIgnore:  texlive-urlbst
Prefix:         %{_bindir}

%description urlbst-bin
Binary files of urlbst

%package velthuis-bin
Version:        %{texlive_version}.%{texlive_release}.svn50281
Release:        0
Summary:        Binary files of velthuis
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-velthuis >= %{texlive_version}
#!BuildIgnore:  texlive-velthuis
Prefix:         %{_bindir}

%description velthuis-bin
Binary files of velthuis

%package vlna-bin
Version:        %{texlive_version}.%{texlive_release}.svn50281
Release:        0
Summary:        Binary files of vlna
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-vlna >= %{texlive_version}
#!BuildIgnore:  texlive-vlna
Prefix:         %{_bindir}

%description vlna-bin
Binary files of vlna

%package vpe-bin
Version:        %{texlive_version}.%{texlive_release}.svn6897
Release:        0
Summary:        Binary files of vpe
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-vpe >= %{texlive_version}
#!BuildIgnore:  texlive-vpe
Prefix:         %{_bindir}

%description vpe-bin
Binary files of vpe

%package web-bin
Version:        %{texlive_version}.%{texlive_release}.svn53999
Release:        0
Summary:        Binary files of web
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-web >= %{texlive_version}
#!BuildIgnore:  texlive-web
Prefix:         %{_bindir}

%description web-bin
Binary files of web

%package webquiz-bin
Version:        %{texlive_version}.%{texlive_release}.svn50419
Release:        0
Summary:        Binary files of webquiz
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-webquiz >= %{texlive_version}
#!BuildIgnore:  texlive-webquiz
Prefix:         %{_bindir}

%description webquiz-bin
Binary files of webquiz

%package wordcount-bin
Version:        %{texlive_version}.%{texlive_release}.svn46165
Release:        0
Summary:        Binary files of wordcount
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-wordcount >= %{texlive_version}
#!BuildIgnore:  texlive-wordcount
Prefix:         %{_bindir}

%description wordcount-bin
Binary files of wordcount

%package xdvi-bin
Version:        %{texlive_version}.%{texlive_release}.svn54358
Release:        0
Summary:        Binary files of xdvi
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-xdvi >= %{texlive_version}
#!BuildIgnore:  texlive-xdvi
Prefix:         %{_bindir}

%description xdvi-bin
Binary files of xdvi

%package xelatex-dev-bin
Version:        %{texlive_version}.%{texlive_release}.svn53999
Release:        0
Summary:        Binary files of xelatex-dev
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-xelatex-dev >= %{texlive_version}
#!BuildIgnore:  texlive-xelatex-dev
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Recommends:     texlive-collection-latexrecommended >= %{texlive_version}
Prefix:         %{_bindir}

%description xelatex-dev-bin
Binary files of xelatex-dev

%package xetex-bin
Version:        %{texlive_version}.%{texlive_release}.svn53999
Release:        0
Summary:        Binary files of xetex
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Obsoletes:      texlive-bin-xetex <= %{texlive_previous}
Requires(pre):  texlive-xetex >= %{texlive_version}
#!BuildIgnore:  texlive-xetex
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Recommends:     texlive-collection-xetex >= %{texlive_version}
Prefix:         %{_bindir}

%description xetex-bin
Binary files of xetex

%package xindex-bin
Version:        %{texlive_version}.%{texlive_release}.svn49312
Release:        0
Summary:        Binary files of xindex
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-xindex >= %{texlive_version}
#!BuildIgnore:  texlive-xindex
Prefix:         %{_bindir}

%description xindex-bin
Binary files of xindex

%package xmltex-bin
Version:        %{texlive_version}.%{texlive_release}.svn3006
Release:        0
Summary:        Binary files of xmltex
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Obsoletes:      texlive-bin-xmltex <= %{texlive_previous}
Requires(pre):  texlive-xmltex >= %{texlive_version}
#!BuildIgnore:  texlive-xmltex
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Recommends:     texlive-collection-htmlxml >= %{texlive_version}
Prefix:         %{_bindir}

%description xmltex-bin
Binary files of xmltex

%package xpdfopen-bin
Version:        %{texlive_version}.%{texlive_release}.svn52917
Release:        0
Summary:        Binary files of xpdfopen
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Obsoletes:      texlive-pdftools-bin <= 2019
Requires(pre):  texlive-xpdfopen >= %{texlive_version}
#!BuildIgnore:  texlive-xpdfopen
Prefix:         %{_bindir}

%description xpdfopen-bin
Binary files of xpdfopen

%package yplan-bin
Version:        %{texlive_version}.%{texlive_release}.svn34398
Release:        0
Summary:        Binary files of yplan
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-yplan >= %{texlive_version}
#!BuildIgnore:  texlive-yplan
Prefix:         %{_bindir}

%description yplan-bin
Binary files of yplan

%package -n libkpathsea6
Version:        6.3.2
Release:        0
Summary:        Path searching library for TeX-related files
License:        LGPL-2.1-or-later
Group:          System/Libraries
URL:            http://www.tug.org/texlive/
Prefix:         %{_libdir}

%description -n libkpathsea6
Kpathsea is a library and utility programs which provide path
searching facilities for TeX file types, including the self-
locating feature required for movable installations, layered on
top of a general search mechanism. It is not distributed
separately, but rather is released and maintained as part of
the TeX-live sources.

%package -n %{name}-kpathsea-devel
Version:        6.3.2
Release:        0
Summary:        Path searching library for TeX-related files
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            http://www.tug.org/texlive/
Requires:       libkpathsea6 = 6.3.2

%description -n %{name}-kpathsea-devel
Kpathsea is a library and utility programs which provide path
searching facilities for TeX file types, including the self-
locating feature required for movable installations, layered on
top of a general search mechanism. It is not distributed
separately, but rather is released and maintained as part of
the TeX-live sources.

%package -n libptexenc1
Version:        1.3.8
Release:        0
Summary:        Libraries of Kanji code convert library for pTeX
License:        BSD-3-Clause
Group:          System/Libraries
URL:            http://www.tug.org/texlive/
Prefix:         %{_libdir}

%description -n libptexenc1
The ptexenc is a useful library for Japanese pTeX
(which stands for publishing TeX, and is an extension of
TeX by ASCII Co.) and its surrounding tools.

%package -n %{name}-ptexenc-devel
Version:        1.3.8
Release:        0
Summary:        Libraries of Kanji code convert library for pTeX
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            http://www.tug.org/texlive/
Requires:       libptexenc1 = 1.3.8

%description -n %{name}-ptexenc-devel
This package includes the ptexenc development files.
The ptexenc is a useful library for Japanese pTeX
(which stands for publishing TeX, and is an extension of
TeX by ASCII Co.) and its surrounding tools.

%package -n libsynctex2
Version:        1.21
Release:        0
Summary:        Libraries of The Synchronization TeXnology
License:        MIT
Group:          System/Libraries
URL:            http://www.tug.org/texlive/
Prefix:         %{_libdir}

%description -n libsynctex2
The Synchronization TeXnology by Jérôme Laurens is a new feature
of recent TeX engines.  It allows to synchronize between input
and output, which means to navigate from the source document to
the typeset material and vice versa.

%package -n %{name}-synctex-devel
Version:        1.21
Release:        0
Summary:        Libraries of The Synchronization TeXnology
License:        MIT
Group:          Development/Libraries/C and C++
URL:            http://www.tug.org/texlive/
Requires:       libsynctex2 = 1.21

%description -n %{name}-synctex-devel
This package includes the synctex development files.
The Synchronization TeXnology by Jérôme Laurens is a new feature
of recent TeX engines.  It allows to synchronize between input
and output, which means to navigate from the source document to
the typeset material and vice versa.

%package -n libtexlua53-5
Version:        5.3.5
Release:        0
Summary:        Libraries of an extended version of pdfTeX using Lua
License:        MIT
Group:          System/Libraries
URL:            http://www.tug.org/texlive/
Prefix:         %{_libdir}

%description -n libtexlua53-5
LuaTeX is an extended version of pdfTeX using Lua as an
embedded scripting language

%package -n %{name}-texlua-devel
Version:        5.3.5
Release:        0
Summary:        Libraries of an extended version of pdfTeX using Lua
License:        MIT
Group:          Development/Libraries/C and C++
URL:            http://www.tug.org/texlive/
Requires:       libtexlua53-5 = 5.3.5

%description -n %{name}-texlua-devel
This package includes the luatex development files.
LuaTeX is an extended version of pdfTeX using Lua as an
embedded scripting language

%if %{with LuaJIT}
%package -n libtexluajit2
Version:        2.1.0beta3
Release:        0
Summary:        Libraries of Just-In-Time compiler for Lua
License:        MIT
Group:          System/Libraries
URL:            http://www.tug.org/texlive/
Prefix:         %{_libdir}

%description -n libtexluajit2
LuaJIT is a Just-In-Time (JIT) compiler for the Lua programming language

%package -n %{name}-texluajit-devel
Version:        2.1.0beta3
Release:        0
Summary:        Libraries of Just-In-Time compiler for Lua
License:        MIT
Group:          Development/Libraries/C and C++
URL:            http://www.tug.org/texlive/
Requires:       libtexlua53-5 = 5.3.5

%description -n %{name}-texluajit-devel
This package includes the LuaJIT development files.
LuaJIT is a Just-In-Time (JIT) compiler for the Lua programming language
%endif

%package -n %{name}-bin-devel
Version:        %{texlive_version}.%{texlive_release}
Release:        0
Summary:        Basic development packages for TeXLive
License:        LGPL-2.1-or-later AND BSD-3-Clause AND SUSE-TeX
Group:          Development/Languages/Other
URL:            http://www.tug.org/texlive/
Requires:       libkpathsea6 = 6.3.2
Requires:       libptexenc1 = 1.3.8
Requires:       libsynctex2 = 1.21
Requires:       libtexlua53-5 = 5.3.5
%if %{with LuaJIT}
Requires:       libtexluajit2 = 2.1.0beta3
%endif
Requires:       texlive-cweb-bin >= %{texlive_version}
Requires:       texlive-web-bin >= %{texlive_version}

%description -n %{name}-bin-devel
This package will cause the installation of several
development packages for TeXLive.

%if %{with buildbiber}
%package -n perl-biber
Version:        %{texlive_version}.%{texlive_release}.svn30357
Release:        0
Summary:        Library files of Biber a BibTeX replacement
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://biblatex-biber.sourceforge.net/
Recommends:     perl(Readonly::XS)
Requires:       perl-base >= 5.26.1
Requires:       perl(Business::ISBN) >= 3.005
Requires:       perl(Business::ISMN)
Requires:       perl(Business::ISSN)
Requires:       perl(Class::Accessor)
Requires:       perl(Data::Compare)
Requires:       perl(Data::Dump)
Requires:       perl(Data::Uniqid)
Requires:       perl(Date::Simple)
Requires:       perl(DateTime)
Requires:       perl(DateTime::Calendar::Julian)
Requires:       perl(DateTime::Format::Builder)
Requires:       perl(DateTime::TimeZone)
Requires:       perl(Encode::EUCJPASCII)
Requires:       perl(Encode::HanExtra)
Requires:       perl(Encode::JIS2K)
Requires:       perl(File::Slurp)
Requires:       perl(File::Slurp::Unicode)
Requires:       perl(File::Slurper)
Requires:       perl(IPC::Cmd)
Requires:       perl(IPC::Run3)
Requires:       perl(LWP::Protocol::https)
Requires:       perl(LWP::Simple)
Requires:       perl(List::AllUtils)
Requires:       perl(List::MoreUtils)
Requires:       perl(Log::Log4perl)
Requires:       perl(Regexp::Common)
Requires:       perl(Sort::Key)
Requires:       perl(Text::BibTeX)
Requires:       perl(Text::CSV)
Requires:       perl(Text::Roman)
Requires:       perl(URI)
Requires:       perl(Unicode::Collate)
Requires:       perl(Unicode::GCString)
Requires:       perl(XML::LibXML::Simple)
Requires:       perl(XML::LibXSLT)
Requires:       perl(XML::Writer)
Requires:       perl(autovivification)
Prefix:         %{_bindir}
BuildArch:      noarch

%description -n perl-biber
Perl library files of Biber a BibTeX replacement for users of BibLaTeX.
This package is required by the package texlive-biber-bin.
%endif

%prep
%define _lto_cflags %{nil}
    OS=%{_target_os}
    CPU=%{_target_cpu}
%ifarch ia64
    RPM_OPT_FLAGS=$(echo "${RPM_OPT_FLAGS}"|sed -r 's/-O[0-9]?/-O1/g')
%endif
%ifarch %arm
    RPM_OPT_FLAGS=${RPM_OPT_FLAGS/-mthumb/-mthumb-interwork -marm}
%endif
    CC=gcc
    CXX=g++
    XCFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE"
    XCXXFLAGS="$XCFLAGS"
    cflags ()
    {
	local flag=$1; shift || return
	local cvar=$1; shift || return
	local xvar=$1; shift || true
	if test -z "${flag}" ; then
	    return
	fi
	case "$flag" in
	-Wl,*)
	    if test -z "${cvar}" ; then
		return
	    fi
	    case "${!cvar}" in
	    *${flag}*) return
	    esac
	    if echo 'int main () { return 0; }' | ${CC:-gcc} -Werror $flag -o /dev/null -xc - ; then
		eval $cvar=\${$cvar:+\$$cvar\ }$flag
	    fi
	    ;;
	*)
	    if test -z "${cvar}" ; then
		return
	    fi
	    case "${!cvar}" in
	    *${flag}*) ;;
	    *)	if ${CC:-gcc} -Werror $flag -S -o /dev/null -xc /dev/null ; then
		    eval $cvar=\${$cvar:+\$$cvar\ }$flag
		fi
	    esac
	    if test -z "${xvar}" ; then
		return
	    fi
	    case "${!xvar}" in
	    *${flag}*) ;;
	    *)	if ${CXX:-g++} -Werror $flag -S -o /dev/null -xc++ /dev/null ; then
		    eval $xvar=\${$xvar:+\$$xvar\ }$flag
		fi
	    esac
	esac > /dev/null 2>&1
    }
    cflags -std=gnu99			XCFLAGS
    cflags -fno-const-strings		XCFLAGS XCXXFLAGS
    cflags -fno-strict-aliasing		XCFLAGS XCXXFLAGS
    cflags -fPIC			XCFLAGS XCXXFLAGS
    cflags -Wno-write-strings		XCFLAGS XCXXFLAGS
    cflags -Wno-char-subscripts		XCFLAGS XCXXFLAGS
    cflags -Wno-unused			XCFLAGS XCXXFLAGS
    cflags -Wno-uninitialized		XCFLAGS XCXXFLAGS
    cflags -Wno-return-type		XCFLAGS XCXXFLAGS
    cflags -Wno-parentheses		XCFLAGS XCXXFLAGS
    cflags -Wno-sign-compare		XCFLAGS XCXXFLAGS
    cflags -Wno-unprototyped-calls	XCFLAGS
    cflags -pipe			XCFLAGS XCXXFLAGS
    cflags -Wl,-O2			XLDFLAGS
    cflags -Wl,--as-needed		XLDFLAGS
    cflags -Wl,--hash-size=8599		XLDFLAGS
    cflags -Wl,-warn-common		XLDFLAGS
    cflags -Wl,-Bsymbolic-functions	XLDFLAGS
    XCXXFLAGS="${XCXXFLAGS/-Wno-unprototyped-calls/}"
    HOST=%{_target_cpu}-suse-%{_host_os}
    BUILD=%{_target_cpu}-suse-%{_build_os}
    BINARY=${CPU}-${OS}
    VENDOR="%{vendor}"
    VENDOR="${VENDOR%%%%,*}"

    # Generate the Options file
    exec 6>&1
    exec 1>|%{options}

    # On error clear
    trap 'rm -vf %{options}' ERR

    # Disable MALLOC_PERTURB_
    # echo unset MALLOC_PERTURB_

    # System wide configuration
    echo CPU=\"$CPU\"
    echo BINARY=\"${BINARY%%-gnu*}\"
    echo XCFLAGS=\"$XCFLAGS\"
    echo XCXXFLAGS=\"$XCXXFLAGS\"
    echo XLDFLAGS=\"$XLDFLAGS\"
    echo HOST=\"${HOST%%-gnu*}\"
    echo BUILD=\"${BUILD%%-gnu*}\"

    echo export XCFLAGS XCXXFLAGS XLDFLAGS HOST BUILD BINARY

    # Do not include e.g. from manual build
    echo unset TEXINPUTS TEXMF HOME

    # Use a well defined multi byte locale
    echo unset ${!LC_*}
    echo LANG=POSIX
    echo LC_CTYPE=en_US.UTF-8
    echo export LANG LC_CTYPE

    # Environment for configuration
    echo CONFIG_SHELL=/bin/bash
    echo CC=\"$CC\"
    echo CXX=\"$CXX\"
    echo CFLAGS=\"$XCFLAGS\"
    echo CXXFLAGS=\"$XCXXFLAGS\"
    echo LDFLAGS=\"-Wl,-warn-common $XLDFLAGS\"
    echo VENDOR=\"${VENDOR}\"
    echo ARCH_LIB=%{_lib}
    echo export CC CXX CFLAGS CXXFLAGS LDFLAGS VENDOR PATH CONFIG_SHELL ARCH_LIB LANG

    # Do not run TeX engine in fmtutil with batchmode
    echo batchmode=no
    echo export batchmode
%ifnarch hppa
    echo ulimit -s unlimited
%else
    # This is the maximum on hppa
    echo ulimit -s 81920
%endif
    exec 1>&6-

%setup -c -q -n texlive -T

    tar --use-compress-program=xz --strip-components=1 -xf %{S:0}
%if %{with buildbiber}
    pushd ../
	tar --use-compress-program=xz -xf %{S:3}
    popd
%endif

%patch1  -p0 -b .configure
%patch2  -p0 -b .xdvizilla
%patch3  -p0 -b .arraysubs
%patch5  -p0 -b .texdoc
%patch6  -p0 -b .dviutils
%patch8  -p0 -b .psutils
%patch10 -p0 -b .poppler
%patch11 -p0 -b .lacheck
%patch12 -p0 -b .warns
%patch13 -p0 -b .x11r7
%patch15 -p0 -b .overflow
%patch17 -p0 -b .64
%patch18 -p0 -b .a2p
%patch19 -p0 -b .dvipng
%patch20 -p0 -b .missed
%patch21 -p0 -b .ppcelf
pushd libs/luajit/LuaJIT-src/
%patch104 -p1 -b .ppc64
%patch106 -p1 -b .arm64
popd
%patch0  -p0 -b .p0
%if %{with buildbiber}
pushd ../*biber-*/
/usr/bin/chmod -Rf a+rX,u+w,g-w,o-w .
%patch42 -p0 -b .en
%patch44 -p0 -b .noica
%if 0%{perl_versnum} < 5200
%patch47 -p0 -b .518
%endif
rm -vf bin/biber.noica
rm -vf t/*.fastsort
popd
%endif

%patch53 -p0 -b .poppler0590
%if %{?pkg_vcmp:%{pkg_vcmp libpoppler-devel >= 0.59.0}}%{!?pkg_vcmp:0}
%patch54 -p0 -b .poppler
%patch55 -p1 -b .popplerbool
%endif
%if %{?pkg_vcmp:%{pkg_vcmp libpoppler-devel >= 0.72.0}}%{!?pkg_vcmp:0}
%patch56 -p1 -b .popplerstring
%endif
%if %{?pkg_vcmp:%{pkg_vcmp libpoppler-devel >= 0.69.0}}%{!?pkg_vcmp:0}
%patch57 -p1 -b .popplerdict
%endif
%if %{?pkg_vcmp:%{pkg_vcmp libpoppler-devel >= 0.73.0}}%{!?pkg_vcmp:0}
%patch58 -p1 -b .poppler75
%endif
%if %{?pkg_vcmp:%{pkg_vcmp libpoppler-devel >= 0.83.0}}%{!?pkg_vcmp:0}
%patch61 -p1 -b .poppler79
%endif
%if %{?pkg_vcmp:%{pkg_vcmp libpoppler-devel >= 0.86.0}}%{!?pkg_vcmp:0}
%patch64 -p1 -b .poppler86
%endif
pver=$(pkg-config --modversion poppler)
%if %{?pkg_vcmp:%{pkg_vcmp libpoppler-devel >= 0.79.0}}%{!?pkg_vcmp:0}
cp ./texk/web2c/pdftexdir/pdftoepdf-poppler0.75.0.cc ./texk/web2c/pdftexdir/pdftoepdf-poppler${pver}.cc
%endif
%patch62 -p0 -b .kpserr

if pkg-config --atleast-version=0.59 poppler
then
    for cc in $(find -name '*-newpoppler.cc')
    do
	test -e "$cc" || continue
	old=${cc/-newpoppler/}
	test -e "$old" && mv -fv $old $old.oldpoppler || :
	mv -fv $cc $old
    done
    for cc in $(find -name '*-poppler0.59.0.cc')
    do
	test -e "$cc" || continue
	old=${cc/-poppler0.59.0/}
	test -e "$old" && mv -fv $old $old.oldpoppler || :
	mv -fv $cc $old
    done
    for cc in $(find -name "*-poppler${pver}.cc")
    do
	test -e "$cc" || continue
	old=${cc/-poppler${pver}/}
	test -e "$old" && mv -fv $old $old.oldpoppler || :
	mv -fv $cc $old
    done
fi

    # Correct FHS paths
    paths=$(find -name cnf-to-paths.awk)
    test -n "$paths" || exit 1
    cp -vf %{S:4} $paths

%build
    # Extend the options file
    echo "world=${PWD}/world" >> %{options}
    echo "prefix=${PWD}/prefix" >> %{options}
    echo "texmfcnf=${PWD}/texk/kpathsea" >> %{options}

    # Read the options file
    . %{options}

    # Sanity check for system icu libraries and headers
    # Remark: official libicu is _not_ compatible with libicu of XeTeX
    if test -s /usr/include/layout/GlyphPositioningTables.h -a \
	-s /usr/include/layout/Features.h -a \
	-s /usr/include/common/cmemory.h \
	&& false
    then
	icu[0]='--with-system-icu'
	icu[1]='--with-icu-include=/usr/include/unicode -I/usr/include/layout -I/usr/include/common'
    else
	icu[0]=""
    fi
    # Wrong version string
    sed -ri '/m4_define.*tex_live_version/{s@[0-9]+/dev@%{texlive_version}@}' version.ac
    for rp in $(find -name configure) ; do
	sed -ri '/(Web2C|STRING|VERSION)/{s@[0-9]+/dev@%{texlive_version}@}' $rp
    done

    # Avoid -rpath as libtool is not configurable at this point
    for rp in $(find -name libtool.m4 -or -name configure) ; do
	sed -ri 's/(-rpath)/\1-link/g' $rp
    done
    LD_LIBRARY_PATH=${prefix}/lib:${world}/texk/kpathsea/.libs:${world}/texk/ptexenc/.libs
    export LD_LIBRARY_PATH

    # We have an other autoconf/automake version and some patch changing ac files
    ./reautoconf . libs/gd libs/icu/dummy texk/dvipdfm-x texk/dvipng texk/dvisvgm \
	texk/ttf2pk2 texk/web2c texk/web2c/web2c texk/xdvik

    if [[ $VENDOR =~ opensuse ]] ; then
	banner='for opensuse.org'
    else
	banner='for SUSE Linux'
    fi
    #
    # Avoid win32 Makefile
    #
    find -name configure | xargs sed -ri '/(CONFIG_FILES|ac_config_files)=/ { s@[[:blank:]]+(otps/|)win32/Makefile@@p; }'
    find -name config.status | xargs -r rm -vf

    # Run configure now ... no reautoconf here as TeX Live uses modified m4 macros
    # longinteger and off_t declarations are still inconsistent, do not enable
    # largefile unless you are testing.
    # Default to building ICU without thread support, since xetex does not need it.
    cache=$PWD/config.cache
    mkdir -p ${world}
    pushd ${world}/
	STRIP=/bin/true				\
	STRIPPROG=/bin/true			\
	../configure				\
	    --host=${HOST}			\
	    --build=${BUILD}			\
	    --enable-fast-install=no		\
	    --disable-native-texlive-build	\
	    --disable-cxx-runtime-hack		\
	    --cache-file=$cache			\
	    --disable-multiplatform		\
	    --prefix=$prefix			\
	    --datadir=$prefix			\
	    --datarootdir=$prefix		\
	    --exec-prefix=$prefix		\
	    --bindir=$prefix/bin		\
	    --libdir=$prefix/lib		\
	    --infodir=$prefix/share/info	\
	    --mandir=$prefix/share/man		\
	    --sysconfdir=$prefix/etc		\
	    --localstatedir=$prefix/var/lib	\
	    --sharedstatedir=$prefix/var/lib	\
	    --includedir=$prefix/include	\
	    --x-libraries=%{_x11lib}		\
	    --x-includes=%{_x11inc}		\
	    --disable-cxx-runtime-hack		\
	    --disable-texinfo			\
	    --disable-texi2html			\
	    --disable-dialog			\
	    --disable-t1utils			\
	    --disable-dvi2tty			\
	    --disable-xindy			\
	    --disable-xindy-docs		\
	    --disable-xindy-rules		\
	    --disable-xz			\
	    --disable-largefile			\
	    --disable-threads			\
	    --%{!?with_psutils:disable}%{?with_psutils:enable}-psutils \
	    --%{!?with_lcdf_typetools:disable}%{?with_lcdf_typetools:enable}-lcdf-typetools \
	    --enable-freetype			\
	    --enable-musixflx			\
	    --enable-lacheck			\
	    --enable-detex			\
	    --enable-seetexk			\
	    --enable-tex4htk			\
	    --enable-shared			\
%if %{with LuaJIT}
	    --enable-luajittex			\
	    --enable-luajithbtex		\
	    --enable-mfluajit			\
%else
	    --disable-luajittex			\
	    --disable-luajithbtex		\
	    --disable-mfluajit			\
%endif
	    --with-gnu-ld			\
	    --with-gnu-libc			\
	    --with-system-xz			\
	    --with-system-dialog		\
	    --with-system-t1utils		\
	    --with-system-ncurses		\
	    --with-system-zlib			\
	    --with-system-expat			\
	    --with-system-unzip			\
%if %{with poppler}
	    --with-system-poppler		\
%endif
	    --with-system-xpdf			\
	    --with-system-libpng		\
	    --with-system-pnglib		\
	    --with-system-gd			\
	    --with-system-zziplib		\
	    --with-system-libgs			\
	    --with-system-freetype2		\
	    --with-freetype2-includes=/usr/include/freetype2 \
	    --with-system-cairo			\
	    --with-system-includes=/usr/include/cairo \
	    --with-system-mpfr			\
%if 0%{?suse_version} >= 1550
	    --with-system-harfbuzz		\
%else
%if 0%{?sle_version} >= 150200
	    --with-system-harfbuzz		\
%endif
%endif
	    --with-system-icu			\
	    --with-system-graphite2		\
	    --with-system-potrace		\
	    --with-system-libpaper		\
	    --with-banner-add="/TeX Live $banner" \
	    ${icu[0]:+"${icu[@]}"}		\
	    --enable-epsfwin			\
	    --enable-mftalkwin			\
	    --enable-regiswin			\
	    --enable-tektronixwin		\
	    --enable-unitermwin			\
	    --with-ps=gs			\
	    --with-x				\
	    --with-mf-x-toolkit			\
	    --with-xdvi-x-toolkit=xaw3d		\
	    --with-editor='vi +%%d %%s'

	PATH=$prefix/bin:$PATH			\
	TEXMFLOCAL=%{_texmfmaindir}		\
	TEXMFCNF=$texmfcnf			\
	make %{?_smp_mflags} world STRIP=/bin/true STRIPPROG=/bin/true
    popd

    pushd utils/asymptote
	autoreconf
	(cat>libOSMesa.so)<<-'EOF'
		/* GNU ld script */
		INPUT(%{_libdir}/libOSMesa.so AS_NEEDED(-lglapi))
	EOF
%if 0%{?suse_version} <= 1350
	sed -ri '/^namespace camp \{/{ s/$/ using glm::value_ptr;/; }'  glrender.cc
%endif
	PATH=$prefix/bin:$PATH			\
	TEXMFLOCAL=%{_texmfmaindir}		\
	TEXMFCNF=$texmfcnf			\
	STRIP=/bin/true				\
	STRIPPROG=/bin/true			\
	LDFLAGS="$LDFLAGS -L$PWD"		\
	CFLAGS="${CFLAGS/-Wno-unprototyped-calls/}"	\
	CXXFLAGS="${CXXFLAGS/-Wno-unprototyped-calls/}"	\
%if 0%{?suse_version} <= 1350
	CFLAGS="${CFLAGS/-std=gnu99/-std=gnu++11} -DGLM_FORCE_RADIANS"		\
	CXXFLAGS="${CXXFLAGS/-std=gnu99/-std=gnu++11} -DGLM_FORCE_RADIANS"	\
%else
	CFLAGS="${CFLAGS/-std=gnu99/}"		\
	CXXFLAGS="${CXXFLAGS/-std=gnu99/}"	\
%endif
	./configure				\
	    --host=${HOST}			\
	    --build=${BUILD}			\
	    --prefix=%{_prefix}			\
	    --bindir=%{_bindir}			\
	    --libdir=%{_libdir}			\
	    --datadir=%{_texmfmaindir}		\
	    --disable-texlive-build		\
	    --enable-offscreen			\
	    --enable-readline			\
	    --enable-gsl			\
	    --enable-fftw			\
	    --enable-gc=system			\
	    --enable-gl
	make clean
	make asy
	mkdir -p ${prefix}/bin
	mkdir -p ${prefix}/texmf/asymptote/GUI
	install -m 0755 asy		${prefix}/bin/
	install -m 0755 GUI/xasy.py	${prefix}/texmf/asymptote/GUI
	ln -sf ../texmf/asymptote/GUI/xasy.py ${prefix}/bin/xasy
    popd

    # compile public
    mkdir -p ${prefix}/lib/mktex
    $CC ${RPM_OPT_FLAGS} -DTEXGRP='"%{texgrp}"' -DTEXUSR='"%{texusr}"' -DMKTEX='"%{_libexecdir}/mktex"' -fPIE -pie -o ${prefix}/lib/mktex/public %{S:50}

    # install our own scripts
    mkdir -p ${prefix}/bin
    install -m 0755 texk/seetexk/a4toa5 ${prefix}/bin/
    install -m 0755 texk/seetexk/mydvichk ${prefix}/bin/
    install -m 0755 texk/seetexk/odd2even ${prefix}/bin/

%if %{with LuaJIT}
    echo "Luaji is supported on this platform"
%else
    for broken in luajittex texluajit texluajitc luajithbtex luajittex texluajit texluajitc
    do
	test ! -x ${prefix}/bin/$broken || continue
	(cat>${prefix}/bin/$broken)<<-'EOF'
	#!/bin/sh
	echo "${0}: is not supported on $(uname -m)" 1>&2
	echo "${0}: Report at https://github.com/LuaJIT/LuaJIT/issues/42" 1>&2
	exit 1
	EOF
	chmod 0755 ${prefix}/bin/$broken
	unset broken
    done
%endif

    # install perl modules
    mkdir -p ${prefix}/share/texmf/tlpkg/TeXLive
    install -m 0644 texk/tests/TeXLive/TLConfig.pm ${prefix}/share/texmf/tlpkg/TeXLive/
    install -m 0644 texk/tests/TeXLive/TLUtils.pm  ${prefix}/share/texmf/tlpkg/TeXLive/

%if %{with buildbiber}
    # dump a biber executable
    pushd ../*biber-*/
	find -name '*.ca' | xargs -r rm -vf

	if test "$(getconf LONG_BIT)" -lt 64 ; then
	    sed -ri '/eq_or_diff.*(17000002|era[1234]|range[12])/{s@.*@eq_or_diff("dummy", "dummy", "skipped on 32bit");@}' t/dateformats.t
	fi

	LANG=en_US.UTF-8 %{__perl} ./Build.PL installdirs=vendor optimize="$RPM_OPT_FLAGS"
	LANG=en_US.UTF-8 ./Build build flags=%{?_smp_mflags}

	# There is no network here
	rm t/remote-files.t

	LANG=en_US.UTF-8 \
	BIBER_DEV_TESTS=1 \
	./Build test
    popd
%endif

%install

    # Read the options file
    . %{options}

    mkdir -p %{buildroot}%{_bindir}
    mkdir -p %{buildroot}%{_libdir}/pkgconfig
    mkdir -p %{buildroot}%{_includedir}
    mkdir -p %{buildroot}%{_infodir}
    mkdir -p %{buildroot}%{_libexecdir}/mktex
    mkdir -p %{buildroot}%{_mandir}
    mkdir -p %{buildroot}%{_mandir}/man1
    mkdir -p %{buildroot}%{_mandir}/man5
    mkdir -p %{buildroot}%{_mandir}/man8
    mkdir -p %{buildroot}%{_texmfmaindir}
    mkdir -p %{buildroot}%{_texmfdistdir}
    mkdir -p %{buildroot}%{_texmfconfdir}/dvipdfm/config
    mkdir -p %{buildroot}%{_texmfconfdir}/dvipdfmx
    mkdir -p %{buildroot}%{_texmfconfdir}/dvips/config
    mkdir -p %{buildroot}%{_texmfconfdir}/scripts/urlbst
    mkdir -p %{buildroot}%{_texmfconfdir}/scripts/match_parens
    mkdir -p %{buildroot}%{_texmfconfdir}/scripts/mf2pt1
    mkdir -p %{buildroot}%{_texmfconfdir}/tex/amstex/base
    mkdir -p %{buildroot}%{_texmfconfdir}/tex/generic/config
    mkdir -p %{buildroot}%{_texmfconfdir}/tex/lambda/config
    mkdir -p %{buildroot}%{_texmfconfdir}/tex/mex/base
    mkdir -p %{buildroot}%{_texmfconfdir}/tex/plain/cyrplain
    mkdir -p %{buildroot}%{_texmfconfdir}/web2c
    mkdir -p %{buildroot}%{_texmfconfdir}/xdvi
    mkdir -p %{buildroot}%{_texmfvardir}
    mkdir -p %{buildroot}%{_texmfvardir}/dist
    mkdir -p %{buildroot}%{_texmfvardir}/fonts
    mkdir -p %{buildroot}%{_texmfvardir}/fonts/dvipdfm
    mkdir -p %{buildroot}%{_texmfvardir}/fonts/dvips
    mkdir -p %{buildroot}%{_texmfvardir}/fonts/pdftex
    mkdir -p %{buildroot}%{_texmfvardir}/main
    mkdir -p %{buildroot}%{_texmfvardir}/md5
    mkdir -p %{buildroot}%{_texmfvardir}/web2c
    mkdir -p %{buildroot}%{_texmfvardir}/web2c/aleph
    mkdir -p %{buildroot}%{_texmfvardir}/web2c/eptex
    mkdir -p %{buildroot}%{_texmfvardir}/web2c/luatex
    mkdir -p %{buildroot}%{_texmfvardir}/web2c/metafont
    mkdir -p %{buildroot}%{_texmfvardir}/web2c/pdftex
    mkdir -p %{buildroot}%{_texmfvardir}/web2c/ptex
    mkdir -p %{buildroot}%{_texmfvardir}/web2c/tex
    mkdir -p %{buildroot}%{_texmfvardir}/web2c/xetex
    mkdir -p %{buildroot}%{_texmfcache}
    mkdir -p %{buildroot}%{_fontcache}
    mkdir -p %{buildroot}%{_fontcache}/pk
    mkdir -p %{buildroot}%{_fontcache}/source
    mkdir -p %{buildroot}%{_fontcache}/tfm
    mkdir -p %{buildroot}%{_appdefdir}
    mkdir -p %{buildroot}/var/adm/update-scripts

    pushd ${prefix}/bin/
	tar -cpSf - . | tar -xvspSf - -C %{buildroot}%{_bindir}/
	rm -vf %{buildroot}%{_bindir}/tlmgr
	rm -vf %{buildroot}%{_bindir}/tlshell
	rm -vf %{buildroot}%{_bindir}/installfont-tl
	rm -vf %{buildroot}%{_bindir}/tlcockpit
    popd
    pushd ${prefix}/lib/
	tar -cpSf - *.so* | tar -xvspSf - -C %{buildroot}%{_libdir}/
	tar -cpSf - mktex | tar -xvspSf - -C %{buildroot}%{_libexecdir}/
    popd
    pushd ${prefix}/share/texmf
	tar -cpSf - tlpkg | tar -xvspSf - -C %{buildroot}%{_texmfdistdir}/
    popd
    pushd ${prefix}/include/
	tar -cpSf - . | tar -xvspSf - -C %{buildroot}%{_includedir}/
    popd
    pushd ${prefix}/share/man/
    popd
    #
    # Biber support
    #
%if %{with buildbiber}
    pushd ../*biber-*/
	./Build install destdir=%{buildroot}
	sed -rn '\@^#![[:space:]]*/usr/bin/env[[:space:]]+perl@{s@(/usr/bin/)env[[:space:]]+(perl)@\1\2@p}' \
		      %{buildroot}%{_bindir}/biber
	chmod    0755 %{buildroot}%{_bindir}/biber
	rm -vf        %{buildroot}%{_mandir}/man1/biber.1*
	chmod    0644 %{buildroot}%{perl_vendorlib}/Biber.pm
	chmod -R u+rw %{buildroot}%{perl_vendorlib}/Biber
	if test -d %{buildroot}%{perl_vendorlib}/Unicode/Collate
	then
	    chmod -R u+rw %{buildroot}%{perl_vendorlib}/Unicode/Collate/*
	fi
	rm -vrf %{buildroot}%{perl_vendorarch}/auto
	rm -vrf %{buildroot}%{_mandir}/man3
	%perl_process_packlist
	%perl_gen_filelist
	pushd blib
	    install -m 0644 bindoc/biber.1 %{buildroot}%{_mandir}/man1/
	popd
	sed -ri '\@/usr/(share|bin)/.*@d' texlive.files
    popd
    mv ../*biber-*/texlive.files perl-biber.files
%else
    (cat > %{buildroot}%{_bindir}/biber)<<-'EOF'
	#!/bin/sh
	echo No biber available due to old perl installation >&2
	exit 1
	EOF
    chmod	0755 %{buildroot}%{_bindir}/biber
%endif

    #
    # Those lines with exclamation mark have to done in the
    # specific spec files
    #
#!  pushd ${prefix}/share/info/
#!	tar -cpSf - *.info | tar -xvspSf - -C %{buildroot}%{_infodir}/
#!  popd
#!  pushd ${prefix}/share/man/
#!	tar -cpSf - . | tar -xvspSf - -C %{buildroot}%{_mandir}/
#!	rm -vf %{buildroot}%{_mandir}/man*/tlmgr*
#!	rm -vf %{buildroot}%{_mandir}/man*/installfont-tl*
#!  popd
    pushd ${prefix}/texmf/
	tar -cpSf - . | tar -xvspSf - -C %{buildroot}%{_texmfmaindir}/
	rm -vrf %{buildroot}%{_texmfmaindir}/texconfig/g
	rm -vrf %{buildroot}%{_texmfmaindir}/texconfig/v
	rm -vrf %{buildroot}%{_texmfmaindir}/texconfig/x
	rm -vrf %{buildroot}%{_texmfmaindir}/tlpkg/tlpobj
	rm -vf  %{buildroot}%{_texmfmaindir}/texconfig/generic
	rm -vf  %{buildroot}%{_texmfmaindir}/texconfig/README
#!	mv -vf  %{buildroot}%{_texmfmaindir}/dvipdfmx/dvipdfmx.cfg \
#!		%{buildroot}%{_texmfconfdir}/dvipdfmx/
#!	ln -sf		    %{_texmfconfdir}/dvipdfmx/dvipdfmx.cfg \
#!		%{buildroot}%{_texmfmaindir}/dvipdfmx/
	for cnf in %{buildroot}%{_texmfmaindir}/web2c/*.cnf ; do
	    test -e "$cnf" || break
	    mv -vf $cnf %{buildroot}%{_texmfconfdir}/web2c/
	    ln -sf %{_texmfconfdir}/web2c/${cnf##*/} $cnf
	done
#!	mv -vf  %{buildroot}%{_texmfmaindir}/xdvi/xdvi.cfg \
#!		%{buildroot}%{_texmfconfdir}/xdvi/
#!	ln -sf		    %{_texmfconfdir}/xdvi/xdvi.cfg \
#!		%{buildroot}%{_texmfmaindir}/xdvi/
#!	mv -vf  %{buildroot}%{_texmfmaindir}/xdvi/XDvi \
#!		%{buildroot}%{_texmfconfdir}/xdvi/
#!	ln -sf		    %{_texmfconfdir}/xdvi/XDvi \
#!		%{buildroot}%{_appdefdir}/
    popd
    pushd ${prefix}/texmf-dist/
	tar -cpSf - . | tar -xvspSf - -C %{buildroot}%{_texmfdistdir}/
	rm -vrf %{buildroot}%{_texmfdistdir}/texconfig/g
	rm -vrf %{buildroot}%{_texmfdistdir}/texconfig/v
	rm -vrf %{buildroot}%{_texmfdistdir}/texconfig/x
	rm -vrf %{buildroot}%{_texmfdistdir}/tlpkg/tlpobj
	rm -vf  %{buildroot}%{_texmfdistdir}/texconfig/generic
	rm -vf  %{buildroot}%{_texmfdistdir}/texconfig/README
	for cnf in %{buildroot}%{_texmfdistdir}/web2c/*.cnf ; do
	    test -e "$cnf" || break
	    mv -vf $cnf %{buildroot}%{_texmfconfdir}/web2c/
	    ln -sf %{_texmfconfdir}/web2c/${cnf##*/} $cnf
	done
    popd
    pushd %{buildroot}%{_bindir}/
	# ppower4 (currently) not part of TEX Live
	rm -f pdfthumb
	rm -f ppower4
	# repair/relocate the script links
	find -type l -printf '%f\a%l\n' | \
	    while IFS=$'\a' read dst src; do
		case "$src" in
%if 0%{texlive_version} >= 2013
		*/texmf/*)	ln -vsf ../share/texmf/${src#../texmf/}	    $dst ;;
%else
		*/texmf/*)	ln -vsf ../lib/texmf/${src#../texmf/}	    $dst ;;
%endif
		*/texmf-dist/*)	ln -vsf ../share/texmf/${src#../texmf-dist/} $dst ;;
		esac
	    done
	# set xasy script link
%if 0%{texlive_version} >= 2013
	ln -vsf ../share/texmf/asymptote/GUI/xasy.py xasy
%else
	ln -vsf ../lib/texmf/asymptote/GUI/xasy.py xasy
%endif
	# some scripts not included in main source tar ball
	test -e match_parens || ln -vsf ../share/texmf/scripts/match_parens/match_parens match_parens
	test -e mf2pt1       || ln -vsf ../share/texmf/scripts/mf2pt1/mf2pt1.pl mf2pt1
	test -e urlbst       || ln -vsf ../share/texmf/scripts/urlbst/urlbst urlbst
	# set some may missed symbolic links
	test -e mfplain  || ln -vsf mpost    mfplain
	test -e texlua   || ln -vsf luatex   texlua
	test -e texluac  || ln -vsf luatex   texluac
	test -e texhash  || ln -vsf mktexlsr texhash
	test -e rpdfcrop || ln -vsf pdfcrop  rpdfcrop
	test -e latexdef || ln -vsf texdef   latexdef
	# stolen from texlink script, also added musixtex case
	sed -r '\@^[[:blank:]]*(#|$)@d;s@\*@@' < $prefix/texmf-dist/web2c/fmtutil.cnf | \
	awk '{print $1, $2 }' | while read fmt engine ; do
	    test -f "$engine" || continue
	    case "$fmt" in
	    mf) test "$engine" = mf-nowin -a -f mfw && engine=mfw
	    esac
	    case "$fmt" in
	    cont-??|mptopdf|*musixtex) continue ;;
	    *)  test "$fmt" = "$(ls -ld "$fmt" 2> /dev/null | awk '{print $NF}')" || rm -rf "$fmt"
		test ! -f "$fmt" || continue
		ln -vsf "$engine" "$fmt"
	    esac
	done
	# our pdfmusixtex extension of the musixtex lua script
	test -e pdfmusixtex  || ln -sf musixtex pdfmusixtex
	if test ! -e rlxtools ; then
	    printf '#!/bin/sh\nmtxrun --script rlxtools "$@"\n' > rlxtools
	    chmod 755 rlxtools
	fi
%if 0%{texlive_version} >= 2017
	# new dviinfox perl script
	ln -vsf ../share/texmf/scripts/dviinfox/dviinfox.pl dviinfox
%endif
%if 0%{texlive_version} >= 2018
	# new ketcindy wrapper script
	ln -vsf ../share/texmf/scripts/ketcindy/ketcindy.sh ketcindy
%endif
%if 0%{texlive_version} >= 2020
	# new git-latexdiff wrapper script
	ln -vsf ../share/texmf/scripts/git-latexdiff/git-latexdiff git-latexdiff
	# ... and add rungs texlua script as dvipdfmx/dvipdfm require this
	ln -vsf ../share/texmf/scripts/texlive/rungs.tlu rungs
	rm -vf %{buildroot}%{_texmfdistdir}/scripts/texlive/rungs.tlu
%endif
    popd

    # clear out all file below texmf tree as this will delivered by texlive tar balls
    find %{buildroot}%{_texmfdirs} -type f | xargs -r rm -vf

    # but work around missing MusixTeX files ...
%if 0%{texlive_version} < 2013
    pushd ${prefix}/texmf-dist/
	install -m 0755 scripts/m-tx/m-tx.lua %{buildroot}%{_texmfdistdir}/scripts/m-tx/
	install -m 0755 scripts/pmx/pmx2pdf.lua %{buildroot}%{_texmfdistdir}/scripts/pmx/
    popd
%endif
    # install manual page of public
    install -m 0644 %{S:51} %{buildroot}%{_mandir}/man8/public.8

    # is part of texlive-kpathsea
    rm -vf %{buildroot}%{_texmfconfdir}/web2c/fmtutil.cnf
    rm -vf %{buildroot}%{_texmfconfdir}/web2c/texmf.cnf
    rm -vf %{buildroot}%{_texmfmaindir}/web2c/fmtutil.cnf
    rm -vf %{buildroot}%{_texmfmaindir}/web2c/texmf.cnf
    rm -vf %{buildroot}%{_texmfdistdir}/web2c/fmtutil.cnf
    rm -vf %{buildroot}%{_texmfdistdir}/web2c/texmf.cnf

    # relink texlive helpers to public binary
    for mktex in texhash mktexlsr mktexmf mktexpk mktextfm
    do
        # mktexlsr and co are now perl/shell script out of package texlive-scripts
	rm -f %{buildroot}%{_bindir}/$mktex
	case "$mktex" in
	mktexlsr*)
	   ln -sf ../../share/texmf/scripts/texlive/${mktex}.pl %{buildroot}%{_libexecdir}/mktex/$mktex
	   ;;
	*)
	   ln -sf ../../share/texmf/scripts/texlive/${mktex}    %{buildroot}%{_libexecdir}/mktex/$mktex
	   ;;
	esac
	ln -sf %{_libexecdir}/mktex/public %{buildroot}%{_bindir}/$mktex
    done
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
	%{buildroot}/var/adm/update-scripts/%{name}-%{version}-%{release}-zypper
%endif

    pushd ${prefix}/lib/pkgconfig/
    for pc in kpathsea ptexenc texlua texlua53 texluajit synctex
    do
	test -e "$pc.pc" || continue
	sed -ri "s@([^=]+=)${prefix}@\1/usr@" $pc.pc
	install -m 0644 $pc.pc %{buildroot}%{_libdir}/pkgconfig/
    done
    popd

    pushd ${world}/texk/kpathsea/
	install -m 0644 c-auto.h %{buildroot}%{_includedir}/kpathsea/
    popd

%if %{with buildbiber}
    for scr in %{_bindir}/biber \
%else
    for scr in \
%endif
	%{_texmfdistdir}/scripts/texlive/rungs.tlu
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

%if %{defined verify_permissions}
%verifyscript kpathsea-bin
%verify_permissions -e %{_libexecdir}/mktex/public
%endif

%pre kpathsea-bin
%{_bindir}/getent group  %{texgrp} > /dev/null 2>&1 || %{_sbindir}/groupadd -r %{?texgid:-g %texgid} %{texgrp}
%{_bindir}/getent passwd %{texusr} > /dev/null 2>&1 || %{_sbindir}/useradd  -r %{?texuid:-u %texuid} -g %{texgrp} -d %{_fontcache} -s /bin/false %{texusr}

%post kpathsea-bin
%if %{defined set_permissions}
%set_permissions %{_libexecdir}/mktex/public
%endif

%pre
%{_bindir}/getent group  %{texgrp} > /dev/null 2>&1 || %{_sbindir}/groupadd -r %{?texgid:-g %texgid} %{texgrp}
%{_bindir}/getent passwd %{texusr} > /dev/null 2>&1 || %{_sbindir}/useradd  -r %{?texuid:-u %texuid} -g %{texgrp} -d %{_fontcache} -s /bin/false %{texusr}

%post
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun
if test $1 = 1; then
    mkdir -p /var/run/texlive
    > /var/run/texlive/run-mktexlsr
    > /var/run/texlive/run-update
fi

%posttrans
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%post   -n libkpathsea6 -p /sbin/ldconfig
%postun -n libkpathsea6 -p /sbin/ldconfig

%post   -n libptexenc1 -p /sbin/ldconfig
%postun -n libptexenc1 -p /sbin/ldconfig

%post   -n libsynctex2 -p /sbin/ldconfig
%postun -n libsynctex2 -p /sbin/ldconfig

%post   -n libtexlua53-5 -p /sbin/ldconfig
%postun -n libtexlua53-5 -p /sbin/ldconfig

%if %{with LuaJIT}
%post   -n libtexluajit2 -p /sbin/ldconfig
%postun -n libtexluajit2 -p /sbin/ldconfig
%endif

%files
%defattr(-,root,root,755)
# is part of texlive-texlive.infra
#%{_texmfdistdir}/tlpkg/TeXLive/TLConfig.pm
#%{_texmfdistdir}/tlpkg/TeXLive/TLUtils.pm
# is part of texlive-kpathsea
#%config(noreplace) %verify(not md5 size mtime) %{_texmfconfdir}/web2c/fmtutil.cnf
#%config(noreplace) %verify(not md5 size mtime) %{_texmfconfdir}/web2c/texmf.cnf
#%verify(link) %{_texmfmaindir}/web2c/fmtutil.cnf
#%verify(link) %{_texmfmaindir}/web2c/texmf.cnf
# is part of texlive-luatex
#%config(noreplace) %verify(not md5 size mtime) %{_texmfconfdir}/web2c/texmfcnf.lua
#%verify(link) %{_texmfmaindir}/web2c/texmfcnf.lua
%{_mandir}/man8/public.*
%if %{with zypper_posttrans}
%verify(link) /var/adm/update-scripts/%{name}-%{version}-%{release}-zypper
%endif

%files a2ping-bin
%defattr(-,root,root,755)
%{_bindir}/a2ping

%files accfonts-bin
%defattr(-,root,root,755)
%{_bindir}/mkt1font
%{_bindir}/vpl2ovp
%{_bindir}/vpl2vpl

%files adhocfilelist-bin
%defattr(-,root,root,755)
%{_bindir}/adhocfilelist

%files afm2pl-bin
%defattr(-,root,root,755)
%{_bindir}/afm2pl

%files aleph-bin
%defattr(-,root,root,755)
%{_bindir}/aleph
%{_bindir}/lamed

%files amstex-bin
%defattr(-,root,root,755)
%{_bindir}/amstex

%files arara-bin
%defattr(-,root,root,755)
%{_bindir}/arara

%files asymptote-bin
%defattr(-,root,root,755)
%{_bindir}/asy
%{_bindir}/xasy

%files attachfile2-bin
%defattr(-,root,root,755)
%{_bindir}/pdfatfi

%files authorindex-bin
%defattr(-,root,root,755)
%{_bindir}/authorindex

%files autosp-bin
%defattr(-,root,root,755)
%{_bindir}/autosp
%{_bindir}/tex2aspc

%files axodraw2-bin
%defattr(-,root,root,755)
%{_bindir}/axohelp

%files bib2gls-bin
%defattr(-,root,root,755)
%{_bindir}/bib2gls
%{_bindir}/convertgls2bib

%files biber-bin
%defattr(-,root,root,755)
%{_bindir}/biber
%if %{with buildbiber}
%{_mandir}/man1/biber.1*
%endif

%files bibexport-bin
%defattr(-,root,root,755)
%{_bindir}/bibexport

%files bibtex-bin
%defattr(-,root,root,755)
%{_bindir}/bibtex

%files bibtex8-bin
%defattr(-,root,root,755)
%{_bindir}/bibtex8

%files bibtexu-bin
%defattr(-,root,root,755)
%{_bindir}/bibtexu

%files bundledoc-bin
%defattr(-,root,root,755)
%{_bindir}/arlatex
%{_bindir}/bundledoc

%files cachepic-bin
%defattr(-,root,root,755)
%{_bindir}/cachepic

%files checkcites-bin
%defattr(-,root,root,755)
%{_bindir}/checkcites

%files checklistings-bin
%defattr(-,root,root,755)
%{_bindir}/checklistings

%files chklref-bin
%defattr(-,root,root,755)
%{_bindir}/chklref

%files chktex-bin
%defattr(-,root,root,755)
%{_bindir}/chktex
%{_bindir}/chkweb
%{_bindir}/deweb

%files cjk-gs-integrate-bin
%defattr(-,root,root,755)
%{_bindir}/cjk-gs-integrate

%files cjkutils-bin
%defattr(-,root,root,755)
%{_bindir}/bg5+latex
%{_bindir}/bg5+pdflatex
%{_bindir}/bg5conv
%{_bindir}/bg5latex
%{_bindir}/bg5pdflatex
%{_bindir}/cef5conv
%{_bindir}/cef5latex
%{_bindir}/cef5pdflatex
%{_bindir}/cefconv
%{_bindir}/ceflatex
%{_bindir}/cefpdflatex
%{_bindir}/cefsconv
%{_bindir}/cefslatex
%{_bindir}/cefspdflatex
%{_bindir}/extconv
%{_bindir}/gbklatex
%{_bindir}/gbkpdflatex
%{_bindir}/hbf2gf
%{_bindir}/sjisconv
%{_bindir}/sjislatex
%{_bindir}/sjispdflatex

%files clojure-pamphlet-bin
%defattr(-,root,root,755)
%{_bindir}/pamphletangler

%files cluttex-bin
%defattr(-,root,root,755)
%{_bindir}/cllualatex
%{_bindir}/cluttex
%{_bindir}/clxelatex

%files context-bin
%defattr(-,root,root,755)
%{_bindir}/context
%{_bindir}/contextjit
%{_bindir}/luatools
%{_bindir}/mtxrun
%{_bindir}/rlxtools
%{_bindir}/mtxrunjit
%{_bindir}/texexec
%{_bindir}/texmfstart

%files convbkmk-bin
%defattr(-,root,root,755)
%{_bindir}/convbkmk

%files crossrefware-bin
%defattr(-,root,root,755)
%{_bindir}/bbl2bib
%{_bindir}/bibdoiadd
%{_bindir}/bibmradd
%{_bindir}/biburl2doi
%{_bindir}/bibzbladd
%{_bindir}/ltx2crossrefxml

%files cslatex-bin
%defattr(-,root,root,755)
%{_bindir}/cslatex
%{_bindir}/pdfcslatex

%files csplain-bin
%defattr(-,root,root,755)
%{_bindir}/csplain
%{_bindir}/luacsplain
%{_bindir}/pdfcsplain

%files ctan-o-mat-bin
%defattr(-,root,root,755)
%{_bindir}/ctan-o-mat

%files ctanbib-bin
%defattr(-,root,root,755)
%{_bindir}/ctanbib

%files ctanify-bin
%defattr(-,root,root,755)
%{_bindir}/ctanify

%files ctanupload-bin
%defattr(-,root,root,755)
%{_bindir}/ctanupload

%files ctie-bin
%defattr(-,root,root,755)
%{_bindir}/ctie

%files cweb-bin
%defattr(-,root,root,755)
%{_bindir}/ctangle
%{_bindir}/ctwill
%{_bindir}/ctwill-refsort
%{_bindir}/ctwill-twinx
%{_bindir}/cweave

%files cyrillic-bin-bin
%defattr(-,root,root,755)
%{_bindir}/rubibtex
%{_bindir}/rumakeindex

%files de-macro-bin
%defattr(-,root,root,755)
%{_bindir}/de-macro

%files detex-bin
%defattr(-,root,root,755)
%{_bindir}/detex

%files diadia-bin
%defattr(-,root,root,755)
%{_bindir}/diadia

%files dosepsbin-bin
%defattr(-,root,root,755)
%{_bindir}/dosepsbin

%files dtl-bin
%defattr(-,root,root,755)
%{_bindir}/dt2dv
%{_bindir}/dv2dt

%files dtxgen-bin
%defattr(-,root,root,755)
%{_bindir}/dtxgen

%files dviasm-bin
%defattr(-,root,root,755)
%{_bindir}/dviasm

%files dvicopy-bin
%defattr(-,root,root,755)
%{_bindir}/dvicopy

%files dvidvi-bin
%defattr(-,root,root,755)
%{_bindir}/dvidvi

%files dviinfox-bin
%defattr(-,root,root,755)
%{_bindir}/dviinfox

%files dviljk-bin
%defattr(-,root,root,755)
%{_bindir}/dvihp
%{_bindir}/dvilj
%{_bindir}/dvilj2p
%{_bindir}/dvilj4
%{_bindir}/dvilj4l
%{_bindir}/dvilj6

%files dviout-util-bin
%defattr(-,root,root,755)
%{_bindir}/chkdvifont
%{_bindir}/dvispc

%files dvipdfmx-bin
%defattr(-,root,root,755)
%{_bindir}/dvipdfm
%{_bindir}/dvipdfmx
%{_bindir}/rungs
%{_bindir}/dvipdft
%{_bindir}/ebb
%{_bindir}/extractbb
%{_bindir}/xdvipdfmx

%files dvipng-bin
%defattr(-,root,root,755)
%{_bindir}/dvigif
%{_bindir}/dvipng

%files dvipos-bin
%defattr(-,root,root,755)
%{_bindir}/dvipos

%files dvips-bin
%defattr(-,root,root,755)
%{_bindir}/afm2tfm
%{_bindir}/dvips

%files dvisvgm-bin
%defattr(-,root,root,755)
%{_bindir}/dvisvgm

%files ebong-bin
%defattr(-,root,root,755)
%{_bindir}/ebong

%files eplain-bin
%defattr(-,root,root,755)
%{_bindir}/eplain

%files epspdf-bin
%defattr(-,root,root,755)
%{_bindir}/epspdf
%{_bindir}/epspdftk

%files epstopdf-bin
%defattr(-,root,root,755)
%{_bindir}/epstopdf
%{_bindir}/repstopdf

%files exceltex-bin
%defattr(-,root,root,755)
%{_bindir}/exceltex

%files fig4latex-bin
%defattr(-,root,root,755)
%{_bindir}/fig4latex

%files findhyph-bin
%defattr(-,root,root,755)
%{_bindir}/findhyph

%files fontinst-bin
%defattr(-,root,root,755)
%{_bindir}/fontinst

%files fontools-bin
%defattr(-,root,root,755)
%{_bindir}/afm2afm
%{_bindir}/autoinst
%{_bindir}/ot2kpx

%files fontware-bin
%defattr(-,root,root,755)
%{_bindir}/pltotf
%{_bindir}/tftopl
%{_bindir}/vftovp
%{_bindir}/vptovf

%files fragmaster-bin
%defattr(-,root,root,755)
%{_bindir}/fragmaster

%files getmap-bin
%defattr(-,root,root,755)
%{_bindir}/getmapdl

%files git-latexdiff-bin
%defattr(-,root,root,755)
%{_bindir}/git-latexdiff

%files glossaries-bin
%defattr(-,root,root,755)
%{_bindir}/makeglossaries
%{_bindir}/makeglossaries-lite

%files gregoriotex-bin
%defattr(-,root,root,755)
%{_bindir}/gregorio

%files gsftopk-bin
%defattr(-,root,root,755)
%{_bindir}/gsftopk

%files jadetex-bin
%defattr(-,root,root,755)
%{_bindir}/jadetex
%{_bindir}/pdfjadetex

%files jfmutil-bin
%defattr(-,root,root,755)
%{_bindir}/jfmutil

%files ketcindy-bin
%defattr(-,root,root,755)
%{_bindir}/ketcindy

%files kotex-utils-bin
%defattr(-,root,root,755)
%{_bindir}/jamo-normalize
%{_bindir}/komkindex
%{_bindir}/ttf2kotexfont

%files kpathsea-bin
%defattr(-,root,root,755)
%{_bindir}/kpseaccess
%{_bindir}/kpsereadlink
%{_bindir}/kpsestat
%{_bindir}/kpsewhich
%{_bindir}/mktexlsr
%attr(2755,root,%{texgrp}) %{_libexecdir}/mktex/public
%{_libexecdir}/mktex/*tex*

%files l3build-bin
%defattr(-,root,root,755)
%{_bindir}/l3build

%files lacheck-bin
%defattr(-,root,root,755)
%{_bindir}/lacheck

%files latex-bin-dev-bin
%defattr(-,root,root,755)
%{_bindir}/dvilualatex-dev
%{_bindir}/latex-dev
%{_bindir}/lualatex-dev
%{_bindir}/pdflatex-dev

%files latex-bin-bin
%defattr(-,root,root,755)
%{_bindir}/dvilualatex
%{_bindir}/latex
%{_bindir}/lualatex
%{_bindir}/pdflatex

%files latex-git-log-bin
%defattr(-,root,root,755)
%{_bindir}/latex-git-log

%files latex-papersize-bin
%defattr(-,root,root,755)
%{_bindir}/latex-papersize

%files latex2man-bin
%defattr(-,root,root,755)
%{_bindir}/latex2man

%files latex2nemeth-bin
%defattr(-,root,root,755)
%{_bindir}/latex2nemeth

%files latexdiff-bin
%defattr(-,root,root,755)
%{_bindir}/latexdiff
%{_bindir}/latexdiff-vc
%{_bindir}/latexrevise

%files latexfileversion-bin
%defattr(-,root,root,755)
%{_bindir}/latexfileversion

%files latexindent-bin
%defattr(-,root,root,755)
%{_bindir}/latexindent

%files latexmk-bin
%defattr(-,root,root,755)
%{_bindir}/latexmk

%files latexpand-bin
%defattr(-,root,root,755)
%{_bindir}/latexpand

%files lcdftypetools-bin
%defattr(-,root,root,755)
%if %{with lcdf_typetools}
%{_bindir}/cfftot1
%{_bindir}/mmafm
%{_bindir}/mmpfb
%{_bindir}/otfinfo
%{_bindir}/otftotfm
%{_bindir}/t1dotlessj
%{_bindir}/t1lint
%{_bindir}/t1rawafm
%{_bindir}/t1reencode
%{_bindir}/t1testpage
%{_bindir}/ttftotype42
%endif

%files lilyglyphs-bin
%defattr(-,root,root,755)
%{_bindir}/lily-glyph-commands
%{_bindir}/lily-image-commands
%{_bindir}/lily-rebuild-pdfs

%files listbib-bin
%defattr(-,root,root,755)
%{_bindir}/listbib

%files listings-ext-bin
%defattr(-,root,root,755)
%{_bindir}/listings-ext.sh

%files lollipop-bin
%defattr(-,root,root,755)
%{_bindir}/lollipop

%files ltxfileinfo-bin
%defattr(-,root,root,755)
%{_bindir}/ltxfileinfo

%files ltximg-bin
%defattr(-,root,root,755)
%{_bindir}/ltximg

%files luahbtex-bin
%defattr(-,root,root,755)
%{_bindir}/luahbtex

%files luajittex-bin
%defattr(-,root,root,755)
%{_bindir}/luajithbtex
%{_bindir}/luajittex
%{_bindir}/texluajit
%{_bindir}/texluajitc

%files luaotfload-bin
%defattr(-,root,root,755)
%{_bindir}/luaotfload-tool

%files luatex-bin
%defattr(-,root,root,755)
%{_bindir}/dviluatex
%{_bindir}/luatex
%{_bindir}/texlua
%{_bindir}/texluac

%files lwarp-bin
%defattr(-,root,root,755)
%{_bindir}/lwarpmk

%files m-tx-bin
%defattr(-,root,root,755)
%{_bindir}/m-tx
%{_bindir}/prepmx

%files make4ht-bin
%defattr(-,root,root,755)
%{_bindir}/make4ht

%files makedtx-bin
%defattr(-,root,root,755)
%{_bindir}/makedtx

%files makeindex-bin
%defattr(-,root,root,755)
%{_bindir}/makeindex
%{_bindir}/mkindex

%files match_parens-bin
%defattr(-,root,root,755)
%{_bindir}/match_parens

%files mathspic-bin
%defattr(-,root,root,755)
%{_bindir}/mathspic

%files metafont-bin
%defattr(-,root,root,755)
%{_bindir}/inimf
%{_bindir}/mf
%{_bindir}/mf-nowin

%files metapost-bin
%defattr(-,root,root,755)
%{_bindir}/dvitomp
%{_bindir}/mfplain
%{_bindir}/mpost
%{_bindir}/r-mpost

%files mex-bin
%defattr(-,root,root,755)
%{_bindir}/mex
%{_bindir}/pdfmex
%{_bindir}/utf8mex

%files mf2pt1-bin
%defattr(-,root,root,755)
%{_bindir}/mf2pt1

%files mflua-bin
%defattr(-,root,root,755)
%{_bindir}/mflua
%{_bindir}/mflua-nowin
%if %{with LuaJIT}
%{_bindir}/mfluajit
%endif
%if %{with LuaJIT}
%{_bindir}/mfluajit-nowin
%endif

%files mfware-bin
%defattr(-,root,root,755)
%{_bindir}/gftodvi
%{_bindir}/gftopk
%{_bindir}/gftype
%{_bindir}/mft
%{_bindir}/pktogf
%{_bindir}/pktype

%files mkgrkindex-bin
%defattr(-,root,root,755)
%{_bindir}/mkgrkindex

%files mkjobtexmf-bin
%defattr(-,root,root,755)
%{_bindir}/mkjobtexmf

%files mkpic-bin
%defattr(-,root,root,755)
%{_bindir}/mkpic

%files mltex-bin
%defattr(-,root,root,755)
%{_bindir}/mllatex
%{_bindir}/mltex

%files mptopdf-bin
%defattr(-,root,root,755)
%{_bindir}/mptopdf

%files multibibliography-bin
%defattr(-,root,root,755)
%{_bindir}/multibibliography

%files musixtex-bin
%defattr(-,root,root,755)
%{_bindir}/musixflx
%{_bindir}/musixtex
%{_bindir}/pdfmusixtex

%files musixtnt-bin
%defattr(-,root,root,755)
%{_bindir}/msxlint

%files omegaware-bin
%defattr(-,root,root,755)
%{_bindir}/odvicopy
%{_bindir}/odvitype
%{_bindir}/ofm2opl
%{_bindir}/omfonts
%{_bindir}/opl2ofm
%{_bindir}/otangle
%{_bindir}/otp2ocp
%{_bindir}/outocp
%{_bindir}/ovf2ovp
%{_bindir}/ovp2ovf
%{_bindir}/wofm2opl
%{_bindir}/wopl2ofm
%{_bindir}/wovf2ovp

%files optex-bin
%defattr(-,root,root,755)
%{_bindir}/optex

%files patgen-bin
%defattr(-,root,root,755)
%{_bindir}/patgen

%files pax-bin
%defattr(-,root,root,755)
%{_bindir}/pdfannotextractor

%files pdfbook2-bin
%defattr(-,root,root,755)
%{_bindir}/pdfbook2

%files pdfcrop-bin
%defattr(-,root,root,755)
%{_bindir}/pdfcrop
%{_bindir}/rpdfcrop

%files pdfjam-bin
%defattr(-,root,root,755)
%{_bindir}/pdfjam

%files pdflatexpicscale-bin
%defattr(-,root,root,755)
%{_bindir}/pdflatexpicscale

%files pdftex-quiet-bin
%defattr(-,root,root,755)
%{_bindir}/pdftex-quiet

%files pdftex-bin
%defattr(-,root,root,755)
%{_bindir}/etex
%{_bindir}/pdfetex
%{_bindir}/pdftex
%{_bindir}/simpdftex

%files pdftosrc-bin
%defattr(-,root,root,755)
%{_bindir}/pdftosrc

%files pdfxup-bin
%defattr(-,root,root,755)
%{_bindir}/pdfxup

%files pedigree-perl-bin
%defattr(-,root,root,755)
%{_bindir}/pedigree

%files perltex-bin
%defattr(-,root,root,755)
%{_bindir}/perltex

%files petri-nets-bin
%defattr(-,root,root,755)
%{_bindir}/pn2pdf

%files pfarrei-bin
%defattr(-,root,root,755)
%{_bindir}/a5toa4
%{_bindir}/pfarrei

%files pkfix-helper-bin
%defattr(-,root,root,755)
%{_bindir}/pkfix-helper

%files pkfix-bin
%defattr(-,root,root,755)
%{_bindir}/pkfix

%files platex-bin
%defattr(-,root,root,755)
%{_bindir}/platex
%{_bindir}/platex-dev

%files pmx-bin
%defattr(-,root,root,755)
%{_bindir}/pmxab
%{_bindir}/scor2prt

%files pmxchords-bin
%defattr(-,root,root,755)
%{_bindir}/pmxchords

%files ps2eps-bin
%defattr(-,root,root,755)
%{_bindir}/bbox
%{_bindir}/ps2eps

%files ps2pk-bin
%defattr(-,root,root,755)
%{_bindir}/mag
%{_bindir}/pfb2pfa
%{_bindir}/pk2bm
%{_bindir}/ps2pk

%files pst-pdf-bin
%defattr(-,root,root,755)
%{_bindir}/ps4pdf

%files pst2pdf-bin
%defattr(-,root,root,755)
%{_bindir}/pst2pdf

%files ptex-fontmaps-bin
%defattr(-,root,root,755)
%{_bindir}/kanji-config-updmap
%{_bindir}/kanji-config-updmap-sys
%{_bindir}/kanji-config-updmap-user
%{_bindir}/kanji-fontmap-creator

%files ptex-bin
%defattr(-,root,root,755)
%{_bindir}/eptex
%{_bindir}/makejvf
%{_bindir}/mendex
%{_bindir}/pbibtex
%{_bindir}/pdvitomp
%{_bindir}/pdvitype
%{_bindir}/pmpost
%{_bindir}/ppltotf
%{_bindir}/ptex
%{_bindir}/ptftopl
%{_bindir}/r-pmpost

%files ptex2pdf-bin
%defattr(-,root,root,755)
%{_bindir}/ptex2pdf

%files purifyeps-bin
%defattr(-,root,root,755)
%{_bindir}/purifyeps

%files pygmentex-bin
%defattr(-,root,root,755)
%{_bindir}/pygmentex

%files pythontex-bin
%defattr(-,root,root,755)
%{_bindir}/depythontex
%{_bindir}/pythontex

%files rubik-bin
%defattr(-,root,root,755)
%{_bindir}/rubikrotation

%files seetexk-bin
%defattr(-,root,root,755)
%{_bindir}/dvibook
%{_bindir}/dviconcat
%{_bindir}/dviselect
%{_bindir}/dvitodvi
%{_bindir}/a4toa5
%{_bindir}/mydvichk
%{_bindir}/odd2even

%files splitindex-bin
%defattr(-,root,root,755)
%{_bindir}/splitindex

%files srcredact-bin
%defattr(-,root,root,755)
%{_bindir}/srcredact

%files sty2dtx-bin
%defattr(-,root,root,755)
%{_bindir}/sty2dtx

%files svn-multi-bin
%defattr(-,root,root,755)
%{_bindir}/svn-multi

%files synctex-bin
%defattr(-,root,root,755)
%{_bindir}/synctex

%files tex-bin
%defattr(-,root,root,755)
%{_bindir}/initex
%{_bindir}/tex

%files tex4ebook-bin
%defattr(-,root,root,755)
%{_bindir}/tex4ebook

%files tex4ht-bin
%defattr(-,root,root,755)
%{_bindir}/ht
%{_bindir}/htcontext
%{_bindir}/htlatex
%{_bindir}/htmex
%{_bindir}/httex
%{_bindir}/httexi
%{_bindir}/htxelatex
%{_bindir}/htxetex
%{_bindir}/mk4ht
%{_bindir}/t4ht
%{_bindir}/tex4ht
%{_bindir}/xhlatex

%files texcount-bin
%defattr(-,root,root,755)
%{_bindir}/texcount

%files texdef-bin
%defattr(-,root,root,755)
%{_bindir}/latexdef
%{_bindir}/texdef

%files texdiff-bin
%defattr(-,root,root,755)
%{_bindir}/texdiff

%files texdirflatten-bin
%defattr(-,root,root,755)
%{_bindir}/texdirflatten

%files texdoc-bin
%defattr(-,root,root,755)
%{_bindir}/texdoc

%files texdoctk-bin
%defattr(-,root,root,755)
%{_bindir}/texdoctk

%files texfot-bin
%defattr(-,root,root,755)
%{_bindir}/texfot

%files -n texlive-scripts-extra-bin
%defattr(-,root,root,755)
%{_bindir}/allcm
%{_bindir}/allec
%{_bindir}/allneeded
%{_bindir}/dvi2fax
%{_bindir}/dvired
%{_bindir}/e2pall
%{_bindir}/kpsepath
%{_bindir}/kpsetool
%{_bindir}/kpsewhere
%{_bindir}/kpsexpand
%{_bindir}/mkocp
%{_bindir}/mkofm
%{_bindir}/ps2frag
%{_bindir}/pslatex
%{_bindir}/texconfig
%{_bindir}/texconfig-dialog
%{_bindir}/texconfig-sys
%{_bindir}/texlinks

%files -n texlive-scripts-bin
%defattr(-,root,root,755)
%{_bindir}/fmtutil
%{_bindir}/fmtutil-sys
%{_bindir}/fmtutil-user
%{_bindir}/mktexfmt
%{_bindir}/mktexmf
%{_bindir}/mktexpk
%{_bindir}/mktextfm
%{_bindir}/rungs
%{_bindir}/texhash
%{_bindir}/updmap
%{_bindir}/updmap-sys
%{_bindir}/updmap-user

%files texliveonfly-bin
%defattr(-,root,root,755)
%{_bindir}/texliveonfly

%files texloganalyser-bin
%defattr(-,root,root,755)
%{_bindir}/texloganalyser

%files texosquery-bin
%defattr(-,root,root,755)
%{_bindir}/texosquery
%{_bindir}/texosquery-jre5
%{_bindir}/texosquery-jre8

%files texplate-bin
%defattr(-,root,root,755)
%{_bindir}/texplate

%files texsis-bin
%defattr(-,root,root,755)
%{_bindir}/texsis

%files texware-bin
%defattr(-,root,root,755)
%{_bindir}/dvitype
%{_bindir}/pooltype

%files thumbpdf-bin
%defattr(-,root,root,755)
%{_bindir}/thumbpdf

%files tie-bin
%defattr(-,root,root,755)
%{_bindir}/tie

%files tpic2pdftex-bin
%defattr(-,root,root,755)
%{_bindir}/tpic2pdftex

%files ttfutils-bin
%defattr(-,root,root,755)
%{_bindir}/ttf2afm
%{_bindir}/ttf2pk
%{_bindir}/ttf2tfm
%{_bindir}/ttfdump

%files typeoutfileinfo-bin
%defattr(-,root,root,755)
%{_bindir}/typeoutfileinfo

%files ulqda-bin
%defattr(-,root,root,755)
%{_bindir}/ulqda

%files uplatex-bin
%defattr(-,root,root,755)
%{_bindir}/uplatex
%{_bindir}/uplatex-dev

%files uptex-bin
%defattr(-,root,root,755)
%{_bindir}/euptex
%{_bindir}/r-upmpost
%{_bindir}/upbibtex
%{_bindir}/updvitomp
%{_bindir}/updvitype
%{_bindir}/upmendex
%{_bindir}/upmpost
%{_bindir}/uppltotf
%{_bindir}/uptex
%{_bindir}/uptftopl
%{_bindir}/wovp2ovf

%files urlbst-bin
%defattr(-,root,root,755)
%{_bindir}/urlbst

%files velthuis-bin
%defattr(-,root,root,755)
%{_bindir}/devnag

%files vlna-bin
%defattr(-,root,root,755)
%{_bindir}/vlna

%files vpe-bin
%defattr(-,root,root,755)
%{_bindir}/vpe

%files web-bin
%defattr(-,root,root,755)
%{_bindir}/tangle
%{_bindir}/weave

%files webquiz-bin
%defattr(-,root,root,755)
%{_bindir}/webquiz

%files wordcount-bin
%defattr(-,root,root,755)
%{_bindir}/wordcount

%files xdvi-bin
%defattr(-,root,root,755)
%{_bindir}/xdvi
%{_bindir}/xdvi-xaw3d

%files xelatex-dev-bin
%defattr(-,root,root,755)
%{_bindir}/xelatex-dev

%files xetex-bin
%defattr(-,root,root,755)
%{_bindir}/teckit_compile
%{_bindir}/xelatex
%{_bindir}/xetex

%files xindex-bin
%defattr(-,root,root,755)
%{_bindir}/xindex

%files xmltex-bin
%defattr(-,root,root,755)
%{_bindir}/pdfxmltex
%{_bindir}/xmltex

%files xpdfopen-bin
%defattr(-,root,root,755)
%{_bindir}/pdfclose
%{_bindir}/pdfopen

%files yplan-bin
%defattr(-,root,root,755)
%{_bindir}/yplan

%files -n libkpathsea6
%defattr(-,root,root,755)
%{_libdir}/libkpathsea*.so.*

%files -n %{name}-kpathsea-devel
%defattr(-,root,root)
%dir %{_includedir}/kpathsea
%{_includedir}/kpathsea/*
%{_libdir}/libkpathsea.so
%{_libdir}/pkgconfig/kpathsea.pc

%files -n libptexenc1
%defattr(-,root,root,755)
%{_libdir}/libptexenc*.so.*

%files -n %{name}-ptexenc-devel
%defattr(-,root,root)
%dir %{_includedir}/ptexenc
%{_includedir}/ptexenc/*
%{_libdir}/libptexenc.so
%{_libdir}/pkgconfig/ptexenc.pc

%files -n libsynctex2
%defattr(-,root,root,755)
%{_libdir}/libsynctex.so.*

%files -n %{name}-synctex-devel
%defattr(-,root,root)
%dir %{_includedir}/synctex/
%{_includedir}/synctex/*.h
%{_libdir}/libsynctex.so
%{_libdir}/pkgconfig/synctex.pc

%files -n libtexlua53-5
%defattr(-,root,root,755)
%{_libdir}/libtexlua53*so.*

%files -n %{name}-texlua-devel
%defattr(-,root,root)
%dir %{_includedir}/texlua[0-9]*/
%{_includedir}/texlua[0-9]*/*.h*
%{_libdir}/libtexlua[0-9]*so
%{_libdir}/pkgconfig/texlua[0-9]*.pc

%if %{with LuaJIT}
%files -n libtexluajit2
%defattr(-,root,root,755)
%{_libdir}/libtexluajit.so.*

%files -n %{name}-texluajit-devel
%defattr(-,root,root)
%dir %{_includedir}/texluajit/
%{_includedir}/texluajit/*.h*
%{_libdir}/libtexluajit.so
%{_libdir}/pkgconfig/texluajit.pc
%endif

%files -n %{name}-bin-devel
%defattr(-,root,root,755)

%if %{with buildbiber}
%files -n perl-biber -f perl-biber.files
%defattr(-,root,root,755)
%endif

%changelog
