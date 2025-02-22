#
# spec file for package texlive
#
# Copyright (c) 2025 SUSE LLC
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


%define texlive_version  2024
%define texlive_previous 2022
%define texlive_release  20240311
%define texlive_noarch   217
%define texlive_source   texlive-20240311-source
%define biber_version    2.19

%define __perl_requires		%{nil}
%define __os_install_post	/usr/lib/rpm/brp-compress \\\
  %(ls /usr/lib/rpm/brp-suse.d/* 2> /dev/null | grep -vE 'symlink|desktop') %{nil}

%if ! %{defined perl_version}
%global perl_version %(rpm -q --qf '%%{VERSION}' perl)
%endif
%global perl_versnum %(rpm -q --qf '%%{VERSION}' perl | sed 's/\\.//g')

#
# LuaJIT -- does not build nor support all architectures
#	    Current status is available at https://github.com/LuaJIT/LuaJIT
#                                          https://github.com/LuaJIT/LuaJIT/issues/42
#	    Compare with libs/luajit/LuaJIT-<version>/src/lj_arch.h
#
%ifnarch ppc %power64 s390 s390x riscv64
%global         with_LuaJIT 1
%endif
%bcond_with	LuaJIT

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

#
#
#
%bcond_without	luametatex

Name:           texlive
Version:        %{texlive_version}.%{texlive_release}
Release:        0
Summary:        The TeXLive Formatting System
License:        Apache-2.0 AND Artistic-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LPPL-1.3c AND LPPL-1.0 AND MIT AND BSD-3-Clause AND SUSE-TeX AND SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
PreReq:         %{name}-filesystem >= %{texlive_version}
PreReq:         %{name}-kpathsea >= %{texlive_version}
PreReq:         %{name}-kpathsea-bin >= %{texlive_version}
PreReq:         %{name}-scripts >= %{texlive_version}
PreReq:         /usr/bin/clear
PreReq:         /usr/bin/dialog
PreReq:         /usr/bin/perl
PreReq:         coreutils
PreReq:         ed
PreReq:         findutils
PreReq:         grep
PreReq:         sed
#!BuildIgnore:  %{name}-kpathsea-bin
#!BuildIgnore:  %{name}-kpathsea
#!BuildIgnore:  %{name}-scripts-bin
#!BuildIgnore:  %{name}-scripts
Requires(pre):  user(mktex)
Requires(pre):  group(mktex)
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
BuildRequires:  ghostscript-devel
BuildRequires:  ghostscript-library
BuildRequires:  glibc-devel
BuildRequires:  graphite2-devel
BuildRequires:  gsl-devel
%if 0%{?suse_version} > 1550
BuildRequires:  harfbuzz-devel >= 7.1
%endif
BuildRequires:  jpeg
%if 0%{?suse_version} > 1550
BuildRequires:  libicu-devel >= 72.1
%endif
BuildRequires:  Mesa-dri-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libopenssl-devel
BuildRequires:  libpaper-devel
BuildRequires:  libpng-devel
BuildRequires:  libsigsegv-devel
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  libxslt-devel
BuildRequires:  makeinfo
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
%if 0%{?suse_version} > 1550 && 0%{is_opensuse}
BuildRequires:  zlib-ng-compat-devel
%else
BuildRequires:  zlib-devel
%endif
BuildRequires:  zziplib-devel
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(xt)
%if %{with buildbiber}
#BuildRequires:  perl-base >= 5.32.0
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
BuildRequires:  perl(Lingua::Translit) >= 0.28
BuildRequires:  perl(List::AllUtils)
BuildRequires:  perl(List::MoreUtils) >= 0.407
BuildRequires:  perl(List::MoreUtils::XS)
BuildRequires:  perl(Log::Log4perl)
BuildRequires:  perl(Module::Build) >= 0.38
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
BuildRequires:  perl(Text::BibTeX) >= 0.88
BuildRequires:  perl(Text::CSV)
BuildRequires:  perl(Text::CSV_XS)
BuildRequires:  perl(Text::Roman)
BuildRequires:  perl(Unicode::Collate) >= 1.29
BuildRequires:  perl(Unicode::GCString)
BuildRequires:  perl(Unicode::LineBreak) >= 2019.001
BuildRequires:  perl(Unicode::Normalize) >= 1.26
BuildRequires:  perl(XML::LibXML) >= 1.70
BuildRequires:  perl(XML::LibXML::Simple)
BuildRequires:  perl(XML::LibXSLT)
BuildRequires:  perl(XML::Writer::String)
%endif
# Download at ftp://tug.org/texlive/historic/%{texlive_version}/
Source0:        %{texlive_source}.tar.xz
Source1:        https://github.com/plk/biber/archive/refs/tags/v%{biber_version}.tar.gz#/biber-%{biber_version}.tar.gz
Source2:        biblatex-biber-ms.tar.gz
%if %{with luametatex}
Source3:        luametatex-230310.tar.xz
%endif
Source4:        cnf-to-paths.awk
Source30:       texlive-rpmlintrc
Source50:       public.c
Source51:       public.8
Patch0:         source.dif
Patch1:         source-configure.dif
Patch2:         source-xdvizilla.dif
Patch3:         source-arraysubs.dif
Patch4:         source-decNumber.dif
Patch5:         source-texdoc.dif
Patch6:         source-dviutils.dif
Patch7:         source-mesa24.dif
Patch8:         source-psutils.dif
Patch9:         source-luacore.dif
Patch11:        source-lacheck.dif
Patch12:        source-warns.dif
Patch13:        source-x11r7.dif
Patch17:        source-64.dif
Patch18:        source-a2ping.dif
Patch19:        source-dvipng.dif
Patch21:        source-ppc64.dif
# PATCH-FIX-UPSTREAM
Patch22:        source-dvipdfm-x.dif
# PATCH-FIX-UPSTREAM
Patch23:        source-pdftex-gcc14.patch
# PATCH-FIX-SUSE Make biber work with our perl
Patch42:        biblatex-encoding.dif
Patch43:        biblatex-ms-encoding.dif
# PATCH-FIX-SUSE Old problem back: we do not use internal Certs!
Patch44:        biber-certs.dif
Patch45:        biblatex-ms-missing.dif
# PATCH-FIX-SUSE Make biber work with perl 5.18.2
Patch47:        biber-perl-5.18.2.dif
#
Patch50:        luametatex.dif
# PATCH-FIX-SUSE Let it build even without ls-R files around
Patch62:        source-psutils-kpathsea.dif
# Missed luajit fix for ppc/ppc64/ppc64le and riscv64
# PATCH-FIX-SUSE Support luajit fix for arm64
Patch106:       0006-Fix-register-allocation-bug-in-arm64.patch
Prefix:         %{_bindir}

%define add_optflags(a:f:t:p:w:W:d:g:O:A:C:D:E:H:i:M:n:P:U:u:l:s:X:B:I:L:b:V:m:x:c:S:E:o:v:) \
%global optflags %{optflags} %{**}

%{expand: %%global options %(mktemp /tmp/texlive-opts.XXXXXXXX)}
%global _varlib		%{_localstatedir}/lib

%define libexec %(rpm --eval '%%{_libexecdir}' | sed 's-/usr--g')
%define libexecdir	${prefix}%{libexec}

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

#define texgid		505
#define texuid		505
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
License:        LPPL-1.0
Summary:        Binary files of a2ping
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-a2ping >= %{texlive_version}
#!BuildIgnore:  texlive-a2ping
Prefix:         %{_bindir}

%description a2ping-bin
Binary files of a2ping

%package accfonts-bin
Version:        %{texlive_version}.%{texlive_release}.svn12688
Release:        0
License:        LPPL-1.0
Summary:        Binary files of accfonts
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-accfonts >= %{texlive_version}
#!BuildIgnore:  texlive-accfonts
Prefix:         %{_bindir}

%description accfonts-bin
Binary files of accfonts

%package adhocfilelist-bin
Version:        %{texlive_version}.%{texlive_release}.svn28038
Release:        0
License:        LPPL-1.0
Summary:        Binary files of adhocfilelist
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-adhocfilelist >= %{texlive_version}
#!BuildIgnore:  texlive-adhocfilelist
Prefix:         %{_bindir}

%description adhocfilelist-bin
Binary files of adhocfilelist

%package afm2pl-bin
Version:        %{texlive_version}.%{texlive_release}.svn70276
Release:        0
License:        LPPL-1.0
Summary:        Binary files of afm2pl
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-afm2pl >= %{texlive_version}
#!BuildIgnore:  texlive-afm2pl
Prefix:         %{_bindir}

%description afm2pl-bin
Binary files of afm2pl

%package albatross-bin
Version:        %{texlive_version}.%{texlive_release}.svn57089
Release:        0
License:        LPPL-1.0
Summary:        Binary files of albatross
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-albatross >= %{texlive_version}
#!BuildIgnore:  texlive-albatross
Prefix:         %{_bindir}

%description albatross-bin
Binary files of albatross

%package aleph-bin
Version:        %{texlive_version}.%{texlive_release}.svn70276
Release:        0
License:        LPPL-1.0
Summary:        Binary files of aleph
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-aleph >= %{texlive_version}
#!BuildIgnore:  texlive-aleph
Prefix:         %{_bindir}

%description aleph-bin
Binary files of aleph

%package amstex-bin
Version:        %{texlive_version}.%{texlive_release}.svn3006
Release:        0
License:        LPPL-1.0
Summary:        Binary files of amstex
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-amstex >= %{texlive_version}
#!BuildIgnore:  texlive-amstex
Recommends:     texlive-collection-basic >= %{texlive_version}
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Prefix:         %{_bindir}

%description amstex-bin
Binary files of amstex

%package arara-bin
Version:        %{texlive_version}.%{texlive_release}.svn29036
Release:        0
License:        LPPL-1.0
Summary:        Binary files of arara
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-arara >= %{texlive_version}
#!BuildIgnore:  texlive-arara
Prefix:         %{_bindir}

%description arara-bin
Binary files of arara

%package asymptote-bin
Version:        %{texlive_version}.%{texlive_release}.svn70569
Release:        0
License:        LPPL-1.0
Summary:        Binary files of asymptote
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-asymptote >= %{texlive_version}
#!BuildIgnore:  texlive-asymptote
Prefix:         %{_bindir}

%description asymptote-bin
Binary files of asymptote

%package attachfile2-bin
Version:        %{texlive_version}.%{texlive_release}.svn52909
Release:        0
License:        LPPL-1.0
Summary:        Binary files of attachfile2
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-attachfile2 >= %{texlive_version}
#!BuildIgnore:  texlive-attachfile2
Conflicts:      texlive-pdftools-bin
Provides:       texlive-pdftools-bin:%{_bindir}/pdfatfi
Prefix:         %{_bindir}

%description attachfile2-bin
Binary files of attachfile2

%package authorindex-bin
Version:        %{texlive_version}.%{texlive_release}.svn18790
Release:        0
License:        LPPL-1.0
Summary:        Binary files of authorindex
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-authorindex >= %{texlive_version}
#!BuildIgnore:  texlive-authorindex
Prefix:         %{_bindir}

%description authorindex-bin
Binary files of authorindex

%package autosp-bin
Version:        %{texlive_version}.%{texlive_release}.svn69782
Release:        0
License:        LPPL-1.0
Summary:        Binary files of autosp
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-autosp >= %{texlive_version}
#!BuildIgnore:  texlive-autosp
Prefix:         %{_bindir}

%description autosp-bin
Binary files of autosp

%package axodraw2-bin
Version:        %{texlive_version}.%{texlive_release}.svn69782
Release:        0
License:        LPPL-1.0
Summary:        Binary files of axodraw2
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-axodraw2 >= %{texlive_version}
#!BuildIgnore:  texlive-axodraw2
Prefix:         %{_bindir}

%description axodraw2-bin
Binary files of axodraw2

%package bib2gls-bin
Version:        %{texlive_version}.%{texlive_release}.svn45266
Release:        0
License:        LPPL-1.0
Summary:        Binary files of bib2gls
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-bib2gls >= %{texlive_version}
#!BuildIgnore:  texlive-bib2gls
Prefix:         %{_bindir}

%description bib2gls-bin
Binary files of bib2gls

%package bibcop-bin
Version:        %{texlive_version}.%{texlive_release}.svn65257
Release:        0
License:        LPPL-1.0
Summary:        Binary files of bibcop
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-bibcop >= %{texlive_version}
#!BuildIgnore:  texlive-bibcop
Prefix:         %{_bindir}

%description bibcop-bin
Binary files of bibcop

%package biber-ms-bin
Version:        %{texlive_version}.%{texlive_release}.svn66478
Release:        0
License:        LPPL-1.0
Summary:        Binary files of biber-ms
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
%if %{with buildbiber}
Requires:       perl = %{perl_version}
Recommends:     ca-certificates
Recommends:     ca-certificates-mozilla
Requires:       perl(Biber) == %{biber_version}
Requires:       perl(LWP::UserAgent)
Requires:       perl(Text::BibTeX)
Requires:       perl(Text::Roman)
%endif
BuildArch:      noarch
Requires(pre):  texlive-biber-ms >= %{texlive_version}
#!BuildIgnore:  texlive-biber-ms
Prefix:         %{_bindir}

%description biber-ms-bin
Binary files of biber-ms

%package biber-bin
Version:        %{texlive_version}.%{texlive_release}.svn66402
Release:        0
License:        LPPL-1.0
Summary:        Binary files of biber
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
%if %{with buildbiber}
Requires:       perl = %{perl_version}
Recommends:     ca-certificates
Recommends:     ca-certificates-mozilla
Requires:       perl(Biber) == %{biber_version}
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
License:        LPPL-1.0
Summary:        Binary files of bibexport
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-bibexport >= %{texlive_version}
#!BuildIgnore:  texlive-bibexport
Prefix:         %{_bindir}

%description bibexport-bin
Binary files of bibexport

%package bibtex-bin
Version:        %{texlive_version}.%{texlive_release}.svn70276
Release:        0
License:        LPPL-1.0
Summary:        Binary files of bibtex
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-bibtex >= %{texlive_version}
#!BuildIgnore:  texlive-bibtex
Recommends:     texlive-collection-basic >= %{texlive_version}
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Prefix:         %{_bindir}

%description bibtex-bin
Binary files of bibtex

%package bibtex8-bin
Version:        %{texlive_version}.%{texlive_release}.svn70276
Release:        0
License:        LPPL-1.0
Summary:        Binary files of bibtex8
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-bibtex8 >= %{texlive_version}
#!BuildIgnore:  texlive-bibtex8
Recommends:     texlive-collection-basic >= %{texlive_version}
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Prefix:         %{_bindir}

%description bibtex8-bin
Binary files of bibtex8

%package bibtexperllibs-bin
Version:        %{texlive_version}.%{texlive_release}.svn68869
Release:        0
License:        LPPL-1.0
Summary:        Binary files of bibtexperllibs
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-bibtexperllibs >= %{texlive_version}
#!BuildIgnore:  texlive-bibtexperllibs
Recommends:     texlive-collection-basic >= %{texlive_version}
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Prefix:         %{_bindir}

%description bibtexperllibs-bin
Binary files of bibtexperllibs

%package bibtexu-bin
Version:        %{texlive_version}.%{texlive_release}.svn70276
Release:        0
License:        LPPL-1.0
Summary:        Binary files of bibtexu
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-bibtexu >= %{texlive_version}
#!BuildIgnore:  texlive-bibtexu
Recommends:     texlive-collection-basic >= %{texlive_version}
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Prefix:         %{_bindir}

%description bibtexu-bin
Binary files of bibtexu

%package bundledoc-bin
Version:        %{texlive_version}.%{texlive_release}.svn17794
Release:        0
License:        LPPL-1.0
Summary:        Binary files of bundledoc
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-bundledoc >= %{texlive_version}
#!BuildIgnore:  texlive-bundledoc
Prefix:         %{_bindir}

%description bundledoc-bin
Binary files of bundledoc

%package cachepic-bin
Version:        %{texlive_version}.%{texlive_release}.svn15543
Release:        0
License:        LPPL-1.0
Summary:        Binary files of cachepic
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-cachepic >= %{texlive_version}
#!BuildIgnore:  texlive-cachepic
Prefix:         %{_bindir}

%description cachepic-bin
Binary files of cachepic

%package checkcites-bin
Version:        %{texlive_version}.%{texlive_release}.svn25623
Release:        0
License:        LPPL-1.0
Summary:        Binary files of checkcites
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-checkcites >= %{texlive_version}
#!BuildIgnore:  texlive-checkcites
Prefix:         %{_bindir}

%description checkcites-bin
Binary files of checkcites

%package checklistings-bin
Version:        %{texlive_version}.%{texlive_release}.svn38300
Release:        0
License:        LPPL-1.0
Summary:        Binary files of checklistings
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-checklistings >= %{texlive_version}
#!BuildIgnore:  texlive-checklistings
Prefix:         %{_bindir}

%description checklistings-bin
Binary files of checklistings

%package chklref-bin
Version:        %{texlive_version}.%{texlive_release}.svn52631
Release:        0
License:        LPPL-1.0
Summary:        Binary files of chklref
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-chklref >= %{texlive_version}
#!BuildIgnore:  texlive-chklref
Prefix:         %{_bindir}

%description chklref-bin
Binary files of chklref

%package chktex-bin
Version:        %{texlive_version}.%{texlive_release}.svn70276
Release:        0
License:        LPPL-1.0
Summary:        Binary files of chktex
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-chktex >= %{texlive_version}
#!BuildIgnore:  texlive-chktex
Recommends:     texlive-collection-basic >= %{texlive_version}
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Prefix:         %{_bindir}

%description chktex-bin
Binary files of chktex

%package citation-style-language-bin
Version:        %{texlive_version}.%{texlive_release}.svn64151
Release:        0
License:        LPPL-1.0
Summary:        Binary files of citation-style-language
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-citation-style-language >= %{texlive_version}
#!BuildIgnore:  texlive-citation-style-language
Prefix:         %{_bindir}

%description citation-style-language-bin
Binary files of citation-style-language

%package cjk-gs-integrate-bin
Version:        %{texlive_version}.%{texlive_release}.svn37223
Release:        0
License:        LPPL-1.0
Summary:        Binary files of cjk-gs-integrate
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-cjk-gs-integrate >= %{texlive_version}
#!BuildIgnore:  texlive-cjk-gs-integrate
Prefix:         %{_bindir}

%description cjk-gs-integrate-bin
Binary files of cjk-gs-integrate

%package cjkutils-bin
Version:        %{texlive_version}.%{texlive_release}.svn70276
Release:        0
License:        LPPL-1.0
Summary:        Binary files of cjkutils
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Obsoletes:      texlive-bin-cjk <= %{texlive_previous}
Requires(pre):  texlive-cjkutils >= %{texlive_version}
#!BuildIgnore:  texlive-cjkutils
Prefix:         %{_bindir}

%description cjkutils-bin
Binary files of cjkutils

%package clojure-pamphlet-bin
Version:        %{texlive_version}.%{texlive_release}.svn51944
Release:        0
License:        LPPL-1.0
Summary:        Binary files of clojure-pamphlet
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-clojure-pamphlet >= %{texlive_version}
#!BuildIgnore:  texlive-clojure-pamphlet
Prefix:         %{_bindir}

%description clojure-pamphlet-bin
Binary files of clojure-pamphlet

%package cluttex-bin
Version:        %{texlive_version}.%{texlive_release}.svn48871
Release:        0
License:        LPPL-1.0
Summary:        Binary files of cluttex
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-cluttex >= %{texlive_version}
#!BuildIgnore:  texlive-cluttex
Recommends:     texlive-collection-basic >= %{texlive_version}
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Prefix:         %{_bindir}

%description cluttex-bin
Binary files of cluttex

%package context-legacy-bin
Version:        %{texlive_version}.%{texlive_release}.svn70338
Release:        0
License:        LPPL-1.0
Summary:        Binary files of context-legacy
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-context-legacy >= %{texlive_version}
#!BuildIgnore:  texlive-context-legacy
Recommends:     texlive-collection-context >= %{texlive_version}
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Prefix:         %{_bindir}

%description context-legacy-bin
Binary files of context-legacy

%package context-texlive-bin
Version:        %{texlive_version}.%{texlive_release}.svn70338
Release:        0
License:        LPPL-1.0
Summary:        Binary files of context-texlive
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-context-texlive >= %{texlive_version}
#!BuildIgnore:  texlive-context-texlive
Recommends:     texlive-collection-context >= %{texlive_version}
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Prefix:         %{_bindir}

%description context-texlive-bin
Binary files of context-texlive

%package context-bin
Version:        %{texlive_version}.%{texlive_release}.svn70189
Release:        0
License:        LPPL-1.0
Summary:        Binary files of context
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-context >= %{texlive_version}
#!BuildIgnore:  texlive-context
Recommends:     texlive-collection-context >= %{texlive_version}
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Prefix:         %{_bindir}

%description context-bin
Binary files of context

%package convbkmk-bin
Version:        %{texlive_version}.%{texlive_release}.svn30408
Release:        0
License:        LPPL-1.0
Summary:        Binary files of convbkmk
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-convbkmk >= %{texlive_version}
#!BuildIgnore:  texlive-convbkmk
Prefix:         %{_bindir}

%description convbkmk-bin
Binary files of convbkmk

%package crossrefware-bin
Version:        %{texlive_version}.%{texlive_release}.svn45927
Release:        0
License:        LPPL-1.0
Summary:        Binary files of crossrefware
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-crossrefware >= %{texlive_version}
#!BuildIgnore:  texlive-crossrefware
Prefix:         %{_bindir}

%description crossrefware-bin
Binary files of crossrefware

%package csplain-bin
Version:        %{texlive_version}.%{texlive_release}.svn50528
Release:        0
License:        LPPL-1.0
Summary:        Binary files of csplain
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-csplain >= %{texlive_version}
#!BuildIgnore:  texlive-csplain
Prefix:         %{_bindir}

%description csplain-bin
Binary files of csplain

%package ctan-o-mat-bin
Version:        %{texlive_version}.%{texlive_release}.svn46996
Release:        0
License:        LPPL-1.0
Summary:        Binary files of ctan-o-mat
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-ctan-o-mat >= %{texlive_version}
#!BuildIgnore:  texlive-ctan-o-mat
Prefix:         %{_bindir}

%description ctan-o-mat-bin
Binary files of ctan-o-mat

%package ctanbib-bin
Version:        %{texlive_version}.%{texlive_release}.svn48478
Release:        0
License:        LPPL-1.0
Summary:        Binary files of ctanbib
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-ctanbib >= %{texlive_version}
#!BuildIgnore:  texlive-ctanbib
Prefix:         %{_bindir}

%description ctanbib-bin
Binary files of ctanbib

%package ctanify-bin
Version:        %{texlive_version}.%{texlive_release}.svn24061
Release:        0
License:        LPPL-1.0
Summary:        Binary files of ctanify
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-ctanify >= %{texlive_version}
#!BuildIgnore:  texlive-ctanify
Prefix:         %{_bindir}

%description ctanify-bin
Binary files of ctanify

%package ctanupload-bin
Version:        %{texlive_version}.%{texlive_release}.svn23866
Release:        0
License:        LPPL-1.0
Summary:        Binary files of ctanupload
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-ctanupload >= %{texlive_version}
#!BuildIgnore:  texlive-ctanupload
Prefix:         %{_bindir}

%description ctanupload-bin
Binary files of ctanupload

%package ctie-bin
Version:        %{texlive_version}.%{texlive_release}.svn70276
Release:        0
License:        LPPL-1.0
Summary:        Binary files of ctie
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-ctie >= %{texlive_version}
#!BuildIgnore:  texlive-ctie
Prefix:         %{_bindir}

%description ctie-bin
Binary files of ctie

%package cweb-bin
Version:        %{texlive_version}.%{texlive_release}.svn70571
Release:        0
License:        LPPL-1.0
Summary:        Binary files of cweb
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-cweb >= %{texlive_version}
#!BuildIgnore:  texlive-cweb
Prefix:         %{_bindir}

%description cweb-bin
Binary files of cweb

%package cyrillic-bin-bin
Version:        %{texlive_version}.%{texlive_release}.svn53554
Release:        0
License:        LPPL-1.0
Summary:        Binary files of cyrillic-bin
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-cyrillic-bin >= %{texlive_version}
#!BuildIgnore:  texlive-cyrillic-bin
Prefix:         %{_bindir}

%description cyrillic-bin-bin
Binary files of cyrillic-bin

%package de-macro-bin
Version:        %{texlive_version}.%{texlive_release}.svn17399
Release:        0
License:        LPPL-1.0
Summary:        Binary files of de-macro
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-de-macro >= %{texlive_version}
#!BuildIgnore:  texlive-de-macro
Prefix:         %{_bindir}

%description de-macro-bin
Binary files of de-macro

%package detex-bin
Version:        %{texlive_version}.%{texlive_release}.svn70276
Release:        0
License:        LPPL-1.0
Summary:        Binary files of detex
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-detex >= %{texlive_version}
#!BuildIgnore:  texlive-detex
Recommends:     texlive-collection-basic >= %{texlive_version}
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Prefix:         %{_bindir}

%description detex-bin
Binary files of detex

%package diadia-bin
Version:        %{texlive_version}.%{texlive_release}.svn37645
Release:        0
License:        LPPL-1.0
Summary:        Binary files of diadia
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
BuildArch:      noarch
Requires(pre):  texlive-diadia >= %{texlive_version}
#!BuildIgnore:  texlive-diadia
Prefix:         %{_bindir}

%description diadia-bin
Binary files of diadia

%package digestif-bin
Version:        %{texlive_version}.%{texlive_release}.svn65210
Release:        0
License:        LPPL-1.0
Summary:        Binary files of digestif
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-digestif >= %{texlive_version}
#!BuildIgnore:  texlive-digestif
Prefix:         %{_bindir}

%description digestif-bin
Binary files of digestif

%package dosepsbin-bin
Version:        %{texlive_version}.%{texlive_release}.svn24759
Release:        0
License:        LPPL-1.0
Summary:        Binary files of dosepsbin
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-dosepsbin >= %{texlive_version}
#!BuildIgnore:  texlive-dosepsbin
Prefix:         %{_bindir}

%description dosepsbin-bin
Binary files of dosepsbin

%package dtl-bin
Version:        %{texlive_version}.%{texlive_release}.svn69782
Release:        0
License:        LPPL-1.0
Summary:        Binary files of dtl
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-dtl >= %{texlive_version}
#!BuildIgnore:  texlive-dtl
Prefix:         %{_bindir}

%description dtl-bin
Binary files of dtl

%package dtxgen-bin
Version:        %{texlive_version}.%{texlive_release}.svn29031
Release:        0
License:        LPPL-1.0
Summary:        Binary files of dtxgen
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-dtxgen >= %{texlive_version}
#!BuildIgnore:  texlive-dtxgen
Prefix:         %{_bindir}

%description dtxgen-bin
Binary files of dtxgen

%package dviasm-bin
Version:        %{texlive_version}.%{texlive_release}.svn8329
Release:        0
License:        LPPL-1.0
Summary:        Binary files of dviasm
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-dviasm >= %{texlive_version}
#!BuildIgnore:  texlive-dviasm
Prefix:         %{_bindir}

%description dviasm-bin
Binary files of dviasm

%package dvicopy-bin
Version:        %{texlive_version}.%{texlive_release}.svn70571
Release:        0
License:        LPPL-1.0
Summary:        Binary files of dvicopy
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-dvicopy >= %{texlive_version}
#!BuildIgnore:  texlive-dvicopy
Prefix:         %{_bindir}

%description dvicopy-bin
Binary files of dvicopy

%package dvidvi-bin
Version:        %{texlive_version}.%{texlive_release}.svn69782
Release:        0
License:        LPPL-1.0
Summary:        Binary files of dvidvi
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-dvidvi >= %{texlive_version}
#!BuildIgnore:  texlive-dvidvi
Prefix:         %{_bindir}

%description dvidvi-bin
Binary files of dvidvi

%package dviinfox-bin
Version:        %{texlive_version}.%{texlive_release}.svn44515
Release:        0
License:        LPPL-1.0
Summary:        Binary files of dviinfox
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-dviinfox >= %{texlive_version}
#!BuildIgnore:  texlive-dviinfox
Prefix:         %{_bindir}

%description dviinfox-bin
Binary files of dviinfox

%package dviljk-bin
Version:        %{texlive_version}.%{texlive_release}.svn70276
Release:        0
License:        LPPL-1.0
Summary:        Binary files of dviljk
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Obsoletes:      texlive-bin-dvilj <= %{texlive_previous}
Provides:       texlive-bin-dvilj   = %{texlive_version}
Requires(pre):  texlive-dviljk >= %{texlive_version}
#!BuildIgnore:  texlive-dviljk
Prefix:         %{_bindir}

%description dviljk-bin
Binary files of dviljk

%package dviout-util-bin
Version:        %{texlive_version}.%{texlive_release}.svn70276
Release:        0
License:        LPPL-1.0
Summary:        Binary files of dviout-util
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-dviout-util >= %{texlive_version}
#!BuildIgnore:  texlive-dviout-util
Prefix:         %{_bindir}

%description dviout-util-bin
Binary files of dviout-util

%package dvipdfmx-bin
Version:        %{texlive_version}.%{texlive_release}.svn70489
Release:        0
License:        LPPL-1.0
Summary:        Binary files of dvipdfmx
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Obsoletes:      texlive-dvipdfm-bin < 2013
Provides:       texlive-dvipdfm-bin = %{texlive_version}
Requires:       texlive-scripts >= %{texlive_version}
Requires:       texlive-xetex-bin >= %{texlive_version}
Requires(pre):  texlive-dvipdfmx >= %{texlive_version}
#!BuildIgnore:  texlive-dvipdfmx
Prefix:         %{_bindir}

%description dvipdfmx-bin
Binary files of dvipdfmx

%package dvipng-bin
Version:        %{texlive_version}.%{texlive_release}.svn70276
Release:        0
License:        LPPL-1.0
Summary:        Binary files of dvipng
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-dvipng >= %{texlive_version}
#!BuildIgnore:  texlive-dvipng
Prefix:         %{_bindir}

%description dvipng-bin
Binary files of dvipng

%package dvipos-bin
Version:        %{texlive_version}.%{texlive_release}.svn70276
Release:        0
License:        LPPL-1.0
Summary:        Binary files of dvipos
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-dvipos >= %{texlive_version}
#!BuildIgnore:  texlive-dvipos
Prefix:         %{_bindir}

%description dvipos-bin
Binary files of dvipos

%package dvips-bin
Version:        %{texlive_version}.%{texlive_release}.svn70276
Release:        0
License:        LPPL-1.0
Summary:        Binary files of dvips
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-dvips >= %{texlive_version}
#!BuildIgnore:  texlive-dvips
Prefix:         %{_bindir}

%description dvips-bin
Binary files of dvips

%package dvisvgm-bin
Version:        %{texlive_version}.%{texlive_release}.svn70489
Release:        0
License:        LPPL-1.0
Summary:        Binary files of dvisvgm
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-dvisvgm >= %{texlive_version}
#!BuildIgnore:  texlive-dvisvgm
Prefix:         %{_bindir}

%description dvisvgm-bin
Binary files of dvisvgm

%package easydtx-bin
Version:        %{texlive_version}.%{texlive_release}.svn68514
Release:        0
License:        LPPL-1.0
Summary:        Binary files of easydtx
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-easydtx >= %{texlive_version}
#!BuildIgnore:  texlive-easydtx
Prefix:         %{_bindir}

%description easydtx-bin
Binary files of easydtx

%package eolang-bin
Version:        %{texlive_version}.%{texlive_release}.svn69391
Release:        0
License:        LPPL-1.0
Summary:        Binary files of eolang
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-eolang >= %{texlive_version}
#!BuildIgnore:  texlive-eolang
Prefix:         %{_bindir}

%description eolang-bin
Binary files of eolang

%package eplain-bin
Version:        %{texlive_version}.%{texlive_release}.svn3006
Release:        0
License:        LPPL-1.0
Summary:        Binary files of eplain
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-eplain >= %{texlive_version}
#!BuildIgnore:  texlive-eplain
Prefix:         %{_bindir}

%description eplain-bin
Binary files of eplain

%package epspdf-bin
Version:        %{texlive_version}.%{texlive_release}.svn29050
Release:        0
License:        LPPL-1.0
Summary:        Binary files of epspdf
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-epspdf >= %{texlive_version}
#!BuildIgnore:  texlive-epspdf
Prefix:         %{_bindir}

%description epspdf-bin
Binary files of epspdf

%package epstopdf-bin
Version:        %{texlive_version}.%{texlive_release}.svn18336
Release:        0
License:        LPPL-1.0
Summary:        Binary files of epstopdf
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-epstopdf >= %{texlive_version}
#!BuildIgnore:  texlive-epstopdf
Prefix:         %{_bindir}

%description epstopdf-bin
Binary files of epstopdf

%package exceltex-bin
Version:        %{texlive_version}.%{texlive_release}.svn25860
Release:        0
License:        LPPL-1.0
Summary:        Binary files of exceltex
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-exceltex >= %{texlive_version}
#!BuildIgnore:  texlive-exceltex
Recommends:     texlive-collection-basic >= %{texlive_version}
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Prefix:         %{_bindir}

%description exceltex-bin
Binary files of exceltex

%package fig4latex-bin
Version:        %{texlive_version}.%{texlive_release}.svn14752
Release:        0
License:        LPPL-1.0
Summary:        Binary files of fig4latex
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
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
License:        LPPL-1.0
Summary:        Binary files of findhyph
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-findhyph >= %{texlive_version}
#!BuildIgnore:  texlive-findhyph
Prefix:         %{_bindir}

%description findhyph-bin
Binary files of findhyph

%package fontinst-bin
Version:        %{texlive_version}.%{texlive_release}.svn53554
Release:        0
License:        LPPL-1.0
Summary:        Binary files of fontinst
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-fontinst >= %{texlive_version}
#!BuildIgnore:  texlive-fontinst
Prefix:         %{_bindir}

%description fontinst-bin
Binary files of fontinst

%package fontools-bin
Version:        %{texlive_version}.%{texlive_release}.svn25997
Release:        0
License:        LPPL-1.0
Summary:        Binary files of fontools
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-fontools >= %{texlive_version}
#!BuildIgnore:  texlive-fontools
Prefix:         %{_bindir}

%description fontools-bin
Binary files of fontools

%package fontware-bin
Version:        %{texlive_version}.%{texlive_release}.svn70571
Release:        0
License:        LPPL-1.0
Summary:        Binary files of fontware
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-fontware >= %{texlive_version}
#!BuildIgnore:  texlive-fontware
Prefix:         %{_bindir}

%description fontware-bin
Binary files of fontware

%package fragmaster-bin
Version:        %{texlive_version}.%{texlive_release}.svn13663
Release:        0
License:        LPPL-1.0
Summary:        Binary files of fragmaster
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-fragmaster >= %{texlive_version}
#!BuildIgnore:  texlive-fragmaster
Prefix:         %{_bindir}

%description fragmaster-bin
Binary files of fragmaster

%package getmap-bin
Version:        %{texlive_version}.%{texlive_release}.svn34971
Release:        0
License:        LPPL-1.0
Summary:        Binary files of getmap
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-getmap >= %{texlive_version}
#!BuildIgnore:  texlive-getmap
Prefix:         %{_bindir}

%description getmap-bin
Binary files of getmap

%package git-latexdiff-bin
Version:        %{texlive_version}.%{texlive_release}.svn54732
Release:        0
License:        LPPL-1.0
Summary:        Binary files of git-latexdiff
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
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
License:        LPPL-1.0
Summary:        Binary files of glossaries
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-glossaries >= %{texlive_version}
#!BuildIgnore:  texlive-glossaries
Prefix:         %{_bindir}

%description glossaries-bin
Binary files of glossaries

%package gregoriotex-bin
Version:        %{texlive_version}.%{texlive_release}.svn70276
Release:        0
License:        LPPL-1.0
Summary:        Binary files of gregoriotex
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-gregoriotex >= %{texlive_version}
#!BuildIgnore:  texlive-gregoriotex
Recommends:     texlive-collection-basic >= %{texlive_version}
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Prefix:         %{_bindir}

%description gregoriotex-bin
Binary files of gregoriotex

%package gsftopk-bin
Version:        %{texlive_version}.%{texlive_release}.svn70276
Release:        0
License:        LPPL-1.0
Summary:        Binary files of gsftopk
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-gsftopk >= %{texlive_version}
#!BuildIgnore:  texlive-gsftopk
Prefix:         %{_bindir}

%description gsftopk-bin
Binary files of gsftopk

%package hitex-bin
Version:        %{texlive_version}.%{texlive_release}.svn70276
Release:        0
License:        LPPL-1.0
Summary:        Binary files of hitex
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-hitex >= %{texlive_version}
#!BuildIgnore:  texlive-hitex
Recommends:     texlive-collection-basic >= %{texlive_version}
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Prefix:         %{_bindir}

%description hitex-bin
Binary files of hitex

%package hyperxmp-bin
Version:        %{texlive_version}.%{texlive_release}.svn56984
Release:        0
License:        LPPL-1.0
Summary:        Binary files of hyperxmp
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-hyperxmp >= %{texlive_version}
#!BuildIgnore:  texlive-hyperxmp
Prefix:         %{_bindir}

%description hyperxmp-bin
Binary files of hyperxmp

%package jadetex-bin
Version:        %{texlive_version}.%{texlive_release}.svn3006
Release:        0
License:        LPPL-1.0
Summary:        Binary files of jadetex
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Obsoletes:      texlive-bin-jadetex <= %{texlive_previous}
Requires(pre):  texlive-jadetex >= %{texlive_version}
#!BuildIgnore:  texlive-jadetex
Recommends:     texlive-collection-basic >= %{texlive_version}
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Prefix:         %{_bindir}

%description jadetex-bin
Binary files of jadetex

%package jfmutil-bin
Version:        %{texlive_version}.%{texlive_release}.svn44835
Release:        0
License:        LPPL-1.0
Summary:        Binary files of jfmutil
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-jfmutil >= %{texlive_version}
#!BuildIgnore:  texlive-jfmutil
Prefix:         %{_bindir}

%description jfmutil-bin
Binary files of jfmutil

%package ketcindy-bin
Version:        %{texlive_version}.%{texlive_release}.svn49033
Release:        0
License:        LPPL-1.0
Summary:        Binary files of ketcindy
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-ketcindy >= %{texlive_version}
#!BuildIgnore:  texlive-ketcindy
Prefix:         %{_bindir}

%description ketcindy-bin
Binary files of ketcindy

%package kotex-utils-bin
Version:        %{texlive_version}.%{texlive_release}.svn32101
Release:        0
License:        LPPL-1.0
Summary:        Binary files of kotex-utils
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-kotex-utils >= %{texlive_version}
#!BuildIgnore:  texlive-kotex-utils
Recommends:     texlive-collection-basic >= %{texlive_version}
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Prefix:         %{_bindir}

%description kotex-utils-bin
Binary files of kotex-utils

%package kpathsea-bin
Version:        %{texlive_version}.%{texlive_release}.svn70276
Release:        0
License:        LPPL-1.0
Summary:        Binary files of kpathsea
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  %{name}-filesystem >= %{texlive_version}
Requires(pre):  user(mktex)
Requires(pre):  group(mktex)
Requires(post): %{name}-filesystem
Requires(post): permissions
Requires:       %{name}-gsftopk-bin
Requires(pre):  %{name}-scripts-bin
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
License:        LPPL-1.0
Summary:        Binary files of l3build
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-l3build >= %{texlive_version}
#!BuildIgnore:  texlive-l3build
Prefix:         %{_bindir}

%description l3build-bin
Binary files of l3build

%package lacheck-bin
Version:        %{texlive_version}.%{texlive_release}.svn69782
Release:        0
License:        LPPL-1.0
Summary:        Binary files of lacheck
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-lacheck >= %{texlive_version}
#!BuildIgnore:  texlive-lacheck
Prefix:         %{_bindir}

%description lacheck-bin
Binary files of lacheck

%package latex-bin-dev-bin
Version:        %{texlive_version}.%{texlive_release}.svn53999
Release:        0
License:        LPPL-1.0
Summary:        Binary files of latex-bin-dev
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
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
License:        LPPL-1.0
Summary:        Binary files of latex-bin
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
# Needs to have the same version of zlib on system that it is compiled against
%requires_eq    libz1
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
License:        LPPL-1.0
Summary:        Binary files of latex-git-log
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
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
License:        LPPL-1.0
Summary:        Binary files of latex-papersize
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
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
License:        LPPL-1.0
Summary:        Binary files of latex2man
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
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
License:        LPPL-1.0
Summary:        Binary files of latex2nemeth
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
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
License:        LPPL-1.0
Summary:        Binary files of latexdiff
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
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
License:        LPPL-1.0
Summary:        Binary files of latexfileversion
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
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
License:        LPPL-1.0
Summary:        Binary files of latexindent
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
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
License:        LPPL-1.0
Summary:        Binary files of latexmk
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
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
License:        LPPL-1.0
Summary:        Binary files of latexpand
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-latexpand >= %{texlive_version}
#!BuildIgnore:  texlive-latexpand
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Recommends:     texlive-collection-latexrecommended >= %{texlive_version}
Prefix:         %{_bindir}

%description latexpand-bin
Binary files of latexpand

%package lcdftypetools-bin
Version:        %{texlive_version}.%{texlive_release}.svn70276
Release:        0
License:        LPPL-1.0
Summary:        Binary files of lcdftypetools
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
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

%package light-latex-make-bin
Version:        %{texlive_version}.%{texlive_release}.svn56352
Release:        0
License:        LPPL-1.0
Summary:        Binary files of light-latex-make
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-light-latex-make >= %{texlive_version}
#!BuildIgnore:  texlive-light-latex-make
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Recommends:     texlive-collection-latexrecommended >= %{texlive_version}
Prefix:         %{_bindir}

%description light-latex-make-bin
Binary files of light-latex-make

%package lilyglyphs-bin
Version:        %{texlive_version}.%{texlive_release}.svn31696
Release:        0
License:        LPPL-1.0
Summary:        Binary files of lilyglyphs
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-lilyglyphs >= %{texlive_version}
#!BuildIgnore:  texlive-lilyglyphs
Prefix:         %{_bindir}

%description lilyglyphs-bin
Binary files of lilyglyphs

%package listbib-bin
Version:        %{texlive_version}.%{texlive_release}.svn26126
Release:        0
License:        LPPL-1.0
Summary:        Binary files of listbib
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-listbib >= %{texlive_version}
#!BuildIgnore:  texlive-listbib
Prefix:         %{_bindir}

%description listbib-bin
Binary files of listbib

%package listings-ext-bin
Version:        %{texlive_version}.%{texlive_release}.svn15093
Release:        0
License:        LPPL-1.0
Summary:        Binary files of listings-ext
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-listings-ext >= %{texlive_version}
#!BuildIgnore:  texlive-listings-ext
Prefix:         %{_bindir}

%description listings-ext-bin
Binary files of listings-ext

%package lollipop-bin
Version:        %{texlive_version}.%{texlive_release}.svn41465
Release:        0
License:        LPPL-1.0
Summary:        Binary files of lollipop
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-lollipop >= %{texlive_version}
#!BuildIgnore:  texlive-lollipop
Prefix:         %{_bindir}

%description lollipop-bin
Binary files of lollipop

%package ltxfileinfo-bin
Version:        %{texlive_version}.%{texlive_release}.svn29005
Release:        0
License:        LPPL-1.0
Summary:        Binary files of ltxfileinfo
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-ltxfileinfo >= %{texlive_version}
#!BuildIgnore:  texlive-ltxfileinfo
Prefix:         %{_bindir}

%description ltxfileinfo-bin
Binary files of ltxfileinfo

%package ltximg-bin
Version:        %{texlive_version}.%{texlive_release}.svn32346
Release:        0
License:        LPPL-1.0
Summary:        Binary files of ltximg
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-ltximg >= %{texlive_version}
#!BuildIgnore:  texlive-ltximg
Prefix:         %{_bindir}

%description ltximg-bin
Binary files of ltximg

%package luafindfont-bin
Version:        %{texlive_version}.%{texlive_release}.svn61207
Release:        0
License:        LPPL-1.0
Summary:        Binary files of luafindfont
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-luafindfont >= %{texlive_version}
#!BuildIgnore:  texlive-luafindfont
Prefix:         %{_bindir}

%description luafindfont-bin
Binary files of luafindfont

%package luahbtex-bin
Version:        %{texlive_version}.%{texlive_release}.svn70276
Release:        0
License:        LPPL-1.0
Summary:        Binary files of luahbtex
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
# Needs to have the same version of zlib on system that it is compiled against
%requires_eq    libz1
Requires(pre):  texlive-luahbtex >= %{texlive_version}
#!BuildIgnore:  texlive-luahbtex
Recommends:     texlive-collection-basic >= %{texlive_version}
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Prefix:         %{_bindir}

%description luahbtex-bin
Binary files of luahbtex

%package luajittex-bin
Version:        %{texlive_version}.%{texlive_release}.svn70276
Release:        0
License:        LPPL-1.0
Summary:        Binary files of luajittex
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
# Needs to have the same version of zlib on system that it is compiled against
%requires_eq    libz1
Requires(pre):  texlive-luajittex >= %{texlive_version}
#!BuildIgnore:  texlive-luajittex
Recommends:     texlive-collection-basic >= %{texlive_version}
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Prefix:         %{_bindir}

%description luajittex-bin
Binary files of luajittex

%package luaotfload-bin
Version:        %{texlive_version}.%{texlive_release}.svn34647
Release:        0
License:        LPPL-1.0
Summary:        Binary files of luaotfload
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-luaotfload >= %{texlive_version}
#!BuildIgnore:  texlive-luaotfload
Prefix:         %{_bindir}

%description luaotfload-bin
Binary files of luaotfload

%package luatex-bin
Version:        %{texlive_version}.%{texlive_release}.svn70276
Release:        0
License:        LPPL-1.0
Summary:        Binary files of luatex
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
# Needs to have the same version of zlib on system that it is compiled against
%requires_eq    libz1
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
License:        LPPL-1.0
Summary:        Binary files of lwarp
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-lwarp >= %{texlive_version}
#!BuildIgnore:  texlive-lwarp
Prefix:         %{_bindir}

%description lwarp-bin
Binary files of lwarp

%package m-tx-bin
Version:        %{texlive_version}.%{texlive_release}.svn69782
Release:        0
License:        LPPL-1.0
Summary:        Binary files of m-tx
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-m-tx >= %{texlive_version}
#!BuildIgnore:  texlive-m-tx
Prefix:         %{_bindir}

%description m-tx-bin
Binary files of m-tx

%package make4ht-bin
Version:        %{texlive_version}.%{texlive_release}.svn37750
Release:        0
License:        LPPL-1.0
Summary:        Binary files of make4ht
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-make4ht >= %{texlive_version}
#!BuildIgnore:  texlive-make4ht
Prefix:         %{_bindir}

%description make4ht-bin
Binary files of make4ht

%package makedtx-bin
Version:        %{texlive_version}.%{texlive_release}.svn38769
Release:        0
License:        LPPL-1.0
Summary:        Binary files of makedtx
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-makedtx >= %{texlive_version}
#!BuildIgnore:  texlive-makedtx
Prefix:         %{_bindir}

%description makedtx-bin
Binary files of makedtx

%package makeindex-bin
Version:        %{texlive_version}.%{texlive_release}.svn70276
Release:        0
License:        LPPL-1.0
Summary:        Binary files of makeindex
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-makeindex >= %{texlive_version}
#!BuildIgnore:  texlive-makeindex
Prefix:         %{_bindir}

%description makeindex-bin
Binary files of makeindex

%package match_parens-bin
Version:        %{texlive_version}.%{texlive_release}.svn23500
Release:        0
License:        LPPL-1.0
Summary:        Binary files of match_parens
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-match_parens >= %{texlive_version}
#!BuildIgnore:  texlive-match_parens
Prefix:         %{_bindir}

%description match_parens-bin
Binary files of match_parens

%package mathspic-bin
Version:        %{texlive_version}.%{texlive_release}.svn23661
Release:        0
License:        LPPL-1.0
Summary:        Binary files of mathspic
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-mathspic >= %{texlive_version}
#!BuildIgnore:  texlive-mathspic
Prefix:         %{_bindir}

%description mathspic-bin
Binary files of mathspic

%package memoize-bin
Version:        %{texlive_version}.%{texlive_release}.svn68515
Release:        0
License:        LPPL-1.0
Summary:        Binary files of memoize
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-memoize >= %{texlive_version}
#!BuildIgnore:  texlive-memoize
Prefix:         %{_bindir}

%description memoize-bin
Binary files of memoize

%package metafont-bin
Version:        %{texlive_version}.%{texlive_release}.svn70276
Release:        0
License:        LPPL-1.0
Summary:        Binary files of metafont
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-metafont >= %{texlive_version}
#!BuildIgnore:  texlive-metafont
Prefix:         %{_bindir}

%description metafont-bin
Binary files of metafont

%package metapost-bin
Version:        %{texlive_version}.%{texlive_release}.svn70276
Release:        0
License:        LPPL-1.0
Summary:        Binary files of metapost
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Obsoletes:      texlive-bin-metapost <= %{texlive_previous}
Requires(pre):  texlive-metapost >= %{texlive_version}
#!BuildIgnore:  texlive-metapost
Prefix:         %{_bindir}

%description metapost-bin
Binary files of metapost

%package mex-bin
Version:        %{texlive_version}.%{texlive_release}.svn3006
Release:        0
License:        LPPL-1.0
Summary:        Binary files of mex
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-mex >= %{texlive_version}
#!BuildIgnore:  texlive-mex
Prefix:         %{_bindir}

%description mex-bin
Binary files of mex

%package mf2pt1-bin
Version:        %{texlive_version}.%{texlive_release}.svn23406
Release:        0
License:        LPPL-1.0
Summary:        Binary files of mf2pt1
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-mf2pt1 >= %{texlive_version}
#!BuildIgnore:  texlive-mf2pt1
Prefix:         %{_bindir}

%description mf2pt1-bin
Binary files of mf2pt1

%package mflua-bin
Version:        %{texlive_version}.%{texlive_release}.svn70276
Release:        0
License:        LPPL-1.0
Summary:        Binary files of mflua
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-mflua >= %{texlive_version}
#!BuildIgnore:  texlive-mflua
Prefix:         %{_bindir}

%description mflua-bin
Binary files of mflua

%package mfware-bin
Version:        %{texlive_version}.%{texlive_release}.svn70571
Release:        0
License:        LPPL-1.0
Summary:        Binary files of mfware
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-mfware >= %{texlive_version}
#!BuildIgnore:  texlive-mfware
Prefix:         %{_bindir}

%description mfware-bin
Binary files of mfware

%package mkgrkindex-bin
Version:        %{texlive_version}.%{texlive_release}.svn14428
Release:        0
License:        LPPL-1.0
Summary:        Binary files of mkgrkindex
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-mkgrkindex >= %{texlive_version}
#!BuildIgnore:  texlive-mkgrkindex
Prefix:         %{_bindir}

%description mkgrkindex-bin
Binary files of mkgrkindex

%package mkjobtexmf-bin
Version:        %{texlive_version}.%{texlive_release}.svn8457
Release:        0
License:        LPPL-1.0
Summary:        Binary files of mkjobtexmf
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-mkjobtexmf >= %{texlive_version}
#!BuildIgnore:  texlive-mkjobtexmf
Recommends:     texlive-collection-basic >= %{texlive_version}
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Prefix:         %{_bindir}

%description mkjobtexmf-bin
Binary files of mkjobtexmf

%package mkpic-bin
Version:        %{texlive_version}.%{texlive_release}.svn33688
Release:        0
License:        LPPL-1.0
Summary:        Binary files of mkpic
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-mkpic >= %{texlive_version}
#!BuildIgnore:  texlive-mkpic
Prefix:         %{_bindir}

%description mkpic-bin
Binary files of mkpic

%package mltex-bin
Version:        %{texlive_version}.%{texlive_release}.svn3006
Release:        0
License:        LPPL-1.0
Summary:        Binary files of mltex
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-mltex >= %{texlive_version}
#!BuildIgnore:  texlive-mltex
Recommends:     texlive-collection-basic >= %{texlive_version}
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Prefix:         %{_bindir}

%description mltex-bin
Binary files of mltex

%package mptopdf-bin
Version:        %{texlive_version}.%{texlive_release}.svn18674
Release:        0
License:        LPPL-1.0
Summary:        Binary files of mptopdf
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-mptopdf >= %{texlive_version}
#!BuildIgnore:  texlive-mptopdf
Prefix:         %{_bindir}

%description mptopdf-bin
Binary files of mptopdf

%package multibibliography-bin
Version:        %{texlive_version}.%{texlive_release}.svn30534
Release:        0
License:        LPPL-1.0
Summary:        Binary files of multibibliography
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-multibibliography >= %{texlive_version}
#!BuildIgnore:  texlive-multibibliography
Prefix:         %{_bindir}

%description multibibliography-bin
Binary files of multibibliography

%package musixtex-bin
Version:        %{texlive_version}.%{texlive_release}.svn37026
Release:        0
License:        LPPL-1.0
Summary:        Binary files of musixtex
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Obsoletes:      texlive-bin-musictex <= %{texlive_previous}
Requires:       texlive-m-tx-bin >= %{texlive_version}
Requires:       texlive-pmx-bin >= %{texlive_version}
Requires(pre):  texlive-musixtex >= %{texlive_version}
#!BuildIgnore:  texlive-musixtex
Recommends:     texlive-collection-basic >= %{texlive_version}
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Prefix:         %{_bindir}

%description musixtex-bin
Binary files of musixtex

%package musixtnt-bin
Version:        %{texlive_version}.%{texlive_release}.svn69782
Release:        0
License:        LPPL-1.0
Summary:        Binary files of musixtnt
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-musixtnt >= %{texlive_version}
#!BuildIgnore:  texlive-musixtnt
Prefix:         %{_bindir}

%description musixtnt-bin
Binary files of musixtnt

%package omegaware-bin
Version:        %{texlive_version}.%{texlive_release}.svn70571
Release:        0
License:        LPPL-1.0
Summary:        Binary files of omegaware
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
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
License:        LPPL-1.0
Summary:        Binary files of optex
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-optex >= %{texlive_version}
#!BuildIgnore:  texlive-optex
Recommends:     texlive-collection-basic >= %{texlive_version}
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Prefix:         %{_bindir}

%description optex-bin
Binary files of optex

%package optexcount-bin
Version:        %{texlive_version}.%{texlive_release}.svn59817
Release:        0
License:        LPPL-1.0
Summary:        Binary files of optexcount
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-optexcount >= %{texlive_version}
#!BuildIgnore:  texlive-optexcount
Recommends:     texlive-collection-basic >= %{texlive_version}
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Prefix:         %{_bindir}

%description optexcount-bin
Binary files of optexcount

%package pagelayout-bin
Version:        %{texlive_version}.%{texlive_release}.svn65625
Release:        0
License:        LPPL-1.0
Summary:        Binary files of pagelayout
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-pagelayout >= %{texlive_version}
#!BuildIgnore:  texlive-pagelayout
Prefix:         %{_bindir}

%description pagelayout-bin
Binary files of pagelayout

%package patgen-bin
Version:        %{texlive_version}.%{texlive_release}.svn70571
Release:        0
License:        LPPL-1.0
Summary:        Binary files of patgen
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-patgen >= %{texlive_version}
#!BuildIgnore:  texlive-patgen
Prefix:         %{_bindir}

%description patgen-bin
Binary files of patgen

%package pax-bin
Version:        %{texlive_version}.%{texlive_release}.svn10843
Release:        0
License:        LPPL-1.0
Summary:        Binary files of pax
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-pax >= %{texlive_version}
#!BuildIgnore:  texlive-pax
Prefix:         %{_bindir}

%description pax-bin
Binary files of pax

%package pdfbook2-bin
Version:        %{texlive_version}.%{texlive_release}.svn37537
Release:        0
License:        LPPL-1.0
Summary:        Binary files of pdfbook2
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-pdfbook2 >= %{texlive_version}
#!BuildIgnore:  texlive-pdfbook2
Prefix:         %{_bindir}

%description pdfbook2-bin
Binary files of pdfbook2

%package pdfcrop-bin
Version:        %{texlive_version}.%{texlive_release}.svn14387
Release:        0
License:        LPPL-1.0
Summary:        Binary files of pdfcrop
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-pdfcrop >= %{texlive_version}
#!BuildIgnore:  texlive-pdfcrop
Prefix:         %{_bindir}

%description pdfcrop-bin
Binary files of pdfcrop

%package pdfjam-bin
Version:        %{texlive_version}.%{texlive_release}.svn52858
Release:        0
License:        LPPL-1.0
Summary:        Binary files of pdfjam
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Provides:       pdfjam = %{texlive_version}
Obsoletes:      pdfjam < %{texlive_version}
Requires:       /usr/bin/pdflatex
Requires(pre):  texlive-pdfjam >= %{texlive_version}
#!BuildIgnore:  texlive-pdfjam
Prefix:         %{_bindir}

%description pdfjam-bin
Binary files of pdfjam

%package pdflatexpicscale-bin
Version:        %{texlive_version}.%{texlive_release}.svn41779
Release:        0
License:        LPPL-1.0
Summary:        Binary files of pdflatexpicscale
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
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
License:        LPPL-1.0
Summary:        Binary files of pdftex-quiet
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-pdftex-quiet >= %{texlive_version}
#!BuildIgnore:  texlive-pdftex-quiet
Recommends:     texlive-collection-basic >= %{texlive_version}
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Prefix:         %{_bindir}

%description pdftex-quiet-bin
Binary files of pdftex-quiet

%package pdftex-bin
Version:        %{texlive_version}.%{texlive_release}.svn70276
Release:        0
License:        LPPL-1.0
Summary:        Binary files of pdftex
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-pdftex >= %{texlive_version}
#!BuildIgnore:  texlive-pdftex
Recommends:     texlive-collection-basic >= %{texlive_version}
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Prefix:         %{_bindir}

%description pdftex-bin
Binary files of pdftex

%package pdftosrc-bin
Version:        %{texlive_version}.%{texlive_release}.svn69782
Release:        0
License:        LPPL-1.0
Summary:        Binary files of pdftosrc
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-pdftosrc >= %{texlive_version}
#!BuildIgnore:  texlive-pdftosrc
Conflicts:      texlive-pdftools-bin
Provides:       texlive-pdftools-bin:%{_bindir}/pdftosrc
Prefix:         %{_bindir}

%description pdftosrc-bin
Binary files of pdftosrc

%package pdfxup-bin
Version:        %{texlive_version}.%{texlive_release}.svn40690
Release:        0
License:        LPPL-1.0
Summary:        Binary files of pdfxup
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-pdfxup >= %{texlive_version}
#!BuildIgnore:  texlive-pdfxup
Prefix:         %{_bindir}

%description pdfxup-bin
Binary files of pdfxup

%package pedigree-perl-bin
Version:        %{texlive_version}.%{texlive_release}.svn25962
Release:        0
License:        LPPL-1.0
Summary:        Binary files of pedigree-perl
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-pedigree-perl >= %{texlive_version}
#!BuildIgnore:  texlive-pedigree-perl
Prefix:         %{_bindir}

%description pedigree-perl-bin
Binary files of pedigree-perl

%package perltex-bin
Version:        %{texlive_version}.%{texlive_release}.svn16181
Release:        0
License:        LPPL-1.0
Summary:        Binary files of perltex
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-perltex >= %{texlive_version}
#!BuildIgnore:  texlive-perltex
Recommends:     texlive-collection-basic >= %{texlive_version}
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Prefix:         %{_bindir}

%description perltex-bin
Binary files of perltex

%package petri-nets-bin
Version:        %{texlive_version}.%{texlive_release}.svn39165
Release:        0
License:        LPPL-1.0
Summary:        Binary files of petri-nets
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-petri-nets >= %{texlive_version}
#!BuildIgnore:  texlive-petri-nets
Prefix:         %{_bindir}

%description petri-nets-bin
Binary files of petri-nets

%package pfarrei-bin
Version:        %{texlive_version}.%{texlive_release}.svn29348
Release:        0
License:        LPPL-1.0
Summary:        Binary files of pfarrei
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-pfarrei >= %{texlive_version}
#!BuildIgnore:  texlive-pfarrei
Prefix:         %{_bindir}

%description pfarrei-bin
Binary files of pfarrei

%package pkfix-helper-bin
Version:        %{texlive_version}.%{texlive_release}.svn13663
Release:        0
License:        LPPL-1.0
Summary:        Binary files of pkfix-helper
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-pkfix-helper >= %{texlive_version}
#!BuildIgnore:  texlive-pkfix-helper
Prefix:         %{_bindir}

%description pkfix-helper-bin
Binary files of pkfix-helper

%package pkfix-bin
Version:        %{texlive_version}.%{texlive_release}.svn13364
Release:        0
License:        LPPL-1.0
Summary:        Binary files of pkfix
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-pkfix >= %{texlive_version}
#!BuildIgnore:  texlive-pkfix
Prefix:         %{_bindir}

%description pkfix-bin
Binary files of pkfix

%package platex-bin
Version:        %{texlive_version}.%{texlive_release}.svn67315
Release:        0
License:        LPPL-1.0
Summary:        Binary files of platex
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-platex >= %{texlive_version}
#!BuildIgnore:  texlive-platex
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Recommends:     texlive-collection-latexrecommended >= %{texlive_version}
Prefix:         %{_bindir}

%description platex-bin
Binary files of platex

%package pmx-bin
Version:        %{texlive_version}.%{texlive_release}.svn69782
Release:        0
License:        LPPL-1.0
Summary:        Binary files of pmx
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-pmx >= %{texlive_version}
#!BuildIgnore:  texlive-pmx
Prefix:         %{_bindir}

%description pmx-bin
Binary files of pmx

%package pmxchords-bin
Version:        %{texlive_version}.%{texlive_release}.svn32405
Release:        0
License:        LPPL-1.0
Summary:        Binary files of pmxchords
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-pmxchords >= %{texlive_version}
#!BuildIgnore:  texlive-pmxchords
Prefix:         %{_bindir}

%description pmxchords-bin
Binary files of pmxchords

%package ps2eps-bin
Version:        %{texlive_version}.%{texlive_release}.svn69782
Release:        0
License:        LPPL-1.0
Summary:        Binary files of ps2eps
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-ps2eps >= %{texlive_version}
#!BuildIgnore:  texlive-ps2eps
Conflicts:      texlive-pstools-bin
Provides:       texlive-pstools-bin:%{_bindir}/bbox
Provides:       texlive-pstools-bin:%{_bindir}/ps2eps
Prefix:         %{_bindir}

%description ps2eps-bin
Binary files of ps2eps

%package ps2pk-bin
Version:        %{texlive_version}.%{texlive_release}.svn70276
Release:        0
License:        LPPL-1.0
Summary:        Binary files of ps2pk
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Obsoletes:      texlive-ps2pkm-bin < 2015
Requires(pre):  texlive-ps2pk >= %{texlive_version}
#!BuildIgnore:  texlive-ps2pk
Prefix:         %{_bindir}

%description ps2pk-bin
Binary files of ps2pk

%package pst-pdf-bin
Version:        %{texlive_version}.%{texlive_release}.svn7838
Release:        0
License:        LPPL-1.0
Summary:        Binary files of pst-pdf
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-pst-pdf >= %{texlive_version}
#!BuildIgnore:  texlive-pst-pdf
Prefix:         %{_bindir}

%description pst-pdf-bin
Binary files of pst-pdf

%package pst2pdf-bin
Version:        %{texlive_version}.%{texlive_release}.svn29333
Release:        0
License:        LPPL-1.0
Summary:        Binary files of pst2pdf
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-pst2pdf >= %{texlive_version}
#!BuildIgnore:  texlive-pst2pdf
Prefix:         %{_bindir}

%description pst2pdf-bin
Binary files of pst2pdf

%package ptex-fontmaps-bin
Version:        %{texlive_version}.%{texlive_release}.svn44206
Release:        0
License:        LPPL-1.0
Summary:        Binary files of ptex-fontmaps
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-ptex-fontmaps >= %{texlive_version}
#!BuildIgnore:  texlive-ptex-fontmaps
Recommends:     texlive-collection-basic >= %{texlive_version}
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Prefix:         %{_bindir}

%description ptex-fontmaps-bin
Binary files of ptex-fontmaps

%package ptex-bin
Version:        %{texlive_version}.%{texlive_release}.svn70276
Release:        0
License:        LPPL-1.0
Summary:        Binary files of ptex
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-ptex >= %{texlive_version}
#!BuildIgnore:  texlive-ptex
Recommends:     texlive-collection-basic >= %{texlive_version}
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Prefix:         %{_bindir}

%description ptex-bin
Binary files of ptex

%package ptex2pdf-bin
Version:        %{texlive_version}.%{texlive_release}.svn29335
Release:        0
License:        LPPL-1.0
Summary:        Binary files of ptex2pdf
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-ptex2pdf >= %{texlive_version}
#!BuildIgnore:  texlive-ptex2pdf
Recommends:     texlive-collection-basic >= %{texlive_version}
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Prefix:         %{_bindir}

%description ptex2pdf-bin
Binary files of ptex2pdf

%package purifyeps-bin
Version:        %{texlive_version}.%{texlive_release}.svn13663
Release:        0
License:        LPPL-1.0
Summary:        Binary files of purifyeps
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-purifyeps >= %{texlive_version}
#!BuildIgnore:  texlive-purifyeps
Prefix:         %{_bindir}

%description purifyeps-bin
Binary files of purifyeps

%package pygmentex-bin
Version:        %{texlive_version}.%{texlive_release}.svn34996
Release:        0
License:        LPPL-1.0
Summary:        Binary files of pygmentex
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-pygmentex >= %{texlive_version}
#!BuildIgnore:  texlive-pygmentex
Recommends:     texlive-collection-basic >= %{texlive_version}
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Prefix:         %{_bindir}

%description pygmentex-bin
Binary files of pygmentex

%package pythontex-bin
Version:        %{texlive_version}.%{texlive_release}.svn31638
Release:        0
License:        LPPL-1.0
Summary:        Binary files of pythontex
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-pythontex >= %{texlive_version}
#!BuildIgnore:  texlive-pythontex
Recommends:     texlive-collection-basic >= %{texlive_version}
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Prefix:         %{_bindir}

%description pythontex-bin
Binary files of pythontex

%package rubik-bin
Version:        %{texlive_version}.%{texlive_release}.svn32919
Release:        0
License:        LPPL-1.0
Summary:        Binary files of rubik
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-rubik >= %{texlive_version}
#!BuildIgnore:  texlive-rubik
Prefix:         %{_bindir}

%description rubik-bin
Binary files of rubik

%package runtexshebang-bin
Version:        %{texlive_version}.%{texlive_release}.svn68232
Release:        0
License:        LPPL-1.0
Summary:        Binary files of runtexshebang
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-runtexshebang >= %{texlive_version}
#!BuildIgnore:  texlive-runtexshebang
Recommends:     texlive-collection-basic >= %{texlive_version}
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Prefix:         %{_bindir}

%description runtexshebang-bin
Binary files of runtexshebang

%package seetexk-bin
Version:        %{texlive_version}.%{texlive_release}.svn69782
Release:        0
License:        LPPL-1.0
Summary:        Binary files of seetexk
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-seetexk >= %{texlive_version}
#!BuildIgnore:  texlive-seetexk
Recommends:     texlive-collection-basic >= %{texlive_version}
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Prefix:         %{_bindir}

%description seetexk-bin
Binary files of seetexk

%package spix-bin
Version:        %{texlive_version}.%{texlive_release}.svn55933
Release:        0
License:        LPPL-1.0
Summary:        Binary files of spix
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-spix >= %{texlive_version}
#!BuildIgnore:  texlive-spix
Prefix:         %{_bindir}

%description spix-bin
Binary files of spix

%package splitindex-bin
Version:        %{texlive_version}.%{texlive_release}.svn29688
Release:        0
License:        LPPL-1.0
Summary:        Binary files of splitindex
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-splitindex >= %{texlive_version}
#!BuildIgnore:  texlive-splitindex
Prefix:         %{_bindir}

%description splitindex-bin
Binary files of splitindex

%package srcredact-bin
Version:        %{texlive_version}.%{texlive_release}.svn38710
Release:        0
License:        LPPL-1.0
Summary:        Binary files of srcredact
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-srcredact >= %{texlive_version}
#!BuildIgnore:  texlive-srcredact
Prefix:         %{_bindir}

%description srcredact-bin
Binary files of srcredact

%package sty2dtx-bin
Version:        %{texlive_version}.%{texlive_release}.svn21215
Release:        0
License:        LPPL-1.0
Summary:        Binary files of sty2dtx
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-sty2dtx >= %{texlive_version}
#!BuildIgnore:  texlive-sty2dtx
Prefix:         %{_bindir}

%description sty2dtx-bin
Binary files of sty2dtx

%package svn-multi-bin
Version:        %{texlive_version}.%{texlive_release}.svn13663
Release:        0
License:        LPPL-1.0
Summary:        Binary files of svn-multi
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-svn-multi >= %{texlive_version}
#!BuildIgnore:  texlive-svn-multi
Prefix:         %{_bindir}

%description svn-multi-bin
Binary files of svn-multi

%package synctex-bin
Version:        %{texlive_version}.%{texlive_release}.svn69782
Release:        0
License:        LPPL-1.0
Summary:        Binary files of synctex
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-synctex >= %{texlive_version}
#!BuildIgnore:  texlive-synctex
Recommends:     texlive-collection-basic >= %{texlive_version}
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Prefix:         %{_bindir}

%description synctex-bin
Binary files of synctex

%package tex-bin
Version:        %{texlive_version}.%{texlive_release}.svn70276
Release:        0
License:        LPPL-1.0
Summary:        Binary files of tex
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-tex >= %{texlive_version}
#!BuildIgnore:  texlive-tex
Recommends:     texlive-collection-basic >= %{texlive_version}
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Prefix:         %{_bindir}

%description tex-bin
Binary files of tex

%package tex4ebook-bin
Version:        %{texlive_version}.%{texlive_release}.svn37771
Release:        0
License:        LPPL-1.0
Summary:        Binary files of tex4ebook
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-tex4ebook >= %{texlive_version}
#!BuildIgnore:  texlive-tex4ebook
Recommends:     texlive-collection-basic >= %{texlive_version}
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Prefix:         %{_bindir}

%description tex4ebook-bin
Binary files of tex4ebook

%package tex4ht-bin
Version:        %{texlive_version}.%{texlive_release}.svn70276
Release:        0
License:        LPPL-1.0
Summary:        Binary files of tex4ht
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Obsoletes:      texlive-bin-tex4ht <= %{texlive_previous}
Conflicts:      ht
Requires(pre):  texlive-tex4ht >= %{texlive_version}
#!BuildIgnore:  texlive-tex4ht
Recommends:     texlive-collection-basic >= %{texlive_version}
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Prefix:         %{_bindir}

%description tex4ht-bin
Binary files of tex4ht

%package texaccents-bin
Version:        %{texlive_version}.%{texlive_release}.svn64447
Release:        0
License:        LPPL-1.0
Summary:        Binary files of texaccents
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-texaccents >= %{texlive_version}
#!BuildIgnore:  texlive-texaccents
Recommends:     texlive-collection-basic >= %{texlive_version}
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Prefix:         %{_bindir}

%description texaccents-bin
Binary files of texaccents

%package texblend-bin
Version:        %{texlive_version}.%{texlive_release}.svn68961
Release:        0
License:        LPPL-1.0
Summary:        Binary files of texblend
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-texblend >= %{texlive_version}
#!BuildIgnore:  texlive-texblend
Recommends:     texlive-collection-basic >= %{texlive_version}
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Prefix:         %{_bindir}

%description texblend-bin
Binary files of texblend

%package texcount-bin
Version:        %{texlive_version}.%{texlive_release}.svn13013
Release:        0
License:        LPPL-1.0
Summary:        Binary files of texcount
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-texcount >= %{texlive_version}
#!BuildIgnore:  texlive-texcount
Recommends:     texlive-collection-basic >= %{texlive_version}
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Prefix:         %{_bindir}

%description texcount-bin
Binary files of texcount

%package texdef-bin
Version:        %{texlive_version}.%{texlive_release}.svn45011
Release:        0
License:        LPPL-1.0
Summary:        Binary files of texdef
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-texdef >= %{texlive_version}
#!BuildIgnore:  texlive-texdef
Recommends:     texlive-collection-basic >= %{texlive_version}
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Prefix:         %{_bindir}

%description texdef-bin
Binary files of texdef

%package texdiff-bin
Version:        %{texlive_version}.%{texlive_release}.svn15506
Release:        0
License:        LPPL-1.0
Summary:        Binary files of texdiff
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-texdiff >= %{texlive_version}
#!BuildIgnore:  texlive-texdiff
Recommends:     texlive-collection-basic >= %{texlive_version}
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Prefix:         %{_bindir}

%description texdiff-bin
Binary files of texdiff

%package texdirflatten-bin
Version:        %{texlive_version}.%{texlive_release}.svn12782
Release:        0
License:        LPPL-1.0
Summary:        Binary files of texdirflatten
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-texdirflatten >= %{texlive_version}
#!BuildIgnore:  texlive-texdirflatten
Recommends:     texlive-collection-basic >= %{texlive_version}
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Prefix:         %{_bindir}

%description texdirflatten-bin
Binary files of texdirflatten

%package texdoc-bin
Version:        %{texlive_version}.%{texlive_release}.svn47948
Release:        0
License:        LPPL-1.0
Summary:        Binary files of texdoc
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-texdoc >= %{texlive_version}
#!BuildIgnore:  texlive-texdoc
Recommends:     texlive-collection-basic >= %{texlive_version}
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Prefix:         %{_bindir}

%description texdoc-bin
Binary files of texdoc

%package texdoctk-bin
Version:        %{texlive_version}.%{texlive_release}.svn29741
Release:        0
License:        LPPL-1.0
Summary:        Binary files of texdoctk
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-texdoctk >= %{texlive_version}
#!BuildIgnore:  texlive-texdoctk
Recommends:     texlive-collection-basic >= %{texlive_version}
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Prefix:         %{_bindir}

%description texdoctk-bin
Binary files of texdoctk

%package texfindpkg-bin
Version:        %{texlive_version}.%{texlive_release}.svn66777
Release:        0
License:        LPPL-1.0
Summary:        Binary files of texfindpkg
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-texfindpkg >= %{texlive_version}
#!BuildIgnore:  texlive-texfindpkg
Recommends:     texlive-collection-basic >= %{texlive_version}
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Prefix:         %{_bindir}

%description texfindpkg-bin
Binary files of texfindpkg

%package texfot-bin
Version:        %{texlive_version}.%{texlive_release}.svn33155
Release:        0
License:        LPPL-1.0
Summary:        Binary files of texfot
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-texfot >= %{texlive_version}
#!BuildIgnore:  texlive-texfot
Recommends:     texlive-collection-basic >= %{texlive_version}
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Prefix:         %{_bindir}

%description texfot-bin
Binary files of texfot

%package -n texlive-scripts-extra-bin
Version:        %{texlive_version}.%{texlive_release}.svn53577
Release:        0
License:        LPPL-1.0
Summary:        Binary files of texlive-scripts-extra
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-scripts-extra >= %{texlive_version}
#!BuildIgnore:  texlive-scripts-extra
Recommends:     texlive-collection-basic >= %{texlive_version}
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Obsoletes:      texlive-pdftools-bin < 2020
Obsoletes:      texlive-pstools-bin < 2020
Obsoletes:      texlive-tetex-bin < 2020
Obsoletes:      texlive-texconfig-bin < 2018
Provides:       texlive-pdftools-bin:%{_bindir}/e2pall
Provides:       texlive-tetex-bin:%{_bindir}/allcm
Provides:       texlive-tetex-bin:%{_bindir}/allneeded
Provides:       texlive-tetex-bin:%{_bindir}/dvi2fax
Provides:       texlive-tetex-bin:%{_bindir}/dvired
Provides:       texlive-tetex-bin:%{_bindir}/kpsetool
Provides:       texlive-tetex-bin:%{_bindir}/kpsewhere
Provides:       texlive-tetex-bin:%{_bindir}/texconfig-dialog
Provides:       texlive-tetex-bin:%{_bindir}/texconfig-sys
Provides:       texlive-tetex-bin:%{_bindir}/texlinks
Provides:       texlive-texconfig-bin:%{_bindir}/texconfig
Prefix:         %{_bindir}

%description -n texlive-scripts-extra-bin
Binary files of texlive-scripts-extra

%package -n texlive-scripts-bin
Version:        %{texlive_version}.%{texlive_release}.svn64356
Release:        0
License:        LPPL-1.0
Summary:        Binary files of texlive-scripts
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Obsoletes:      texlive-tetex-bin <= %{texlive_previous}
Obsoletes:      tlshell-bin <= %{texlive_previous}
Requires(pre):  texlive-scripts >= %{texlive_version}
#!BuildIgnore:  texlive-scripts
Recommends:     texlive-collection-basic >= %{texlive_version}
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Prefix:         %{_bindir}

%description -n texlive-scripts-bin
Binary files of texlive-scripts

%package texliveonfly-bin
Version:        %{texlive_version}.%{texlive_release}.svn24062
Release:        0
License:        LPPL-1.0
Summary:        Binary files of texliveonfly
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-texliveonfly >= %{texlive_version}
#!BuildIgnore:  texlive-texliveonfly
Recommends:     texlive-collection-basic >= %{texlive_version}
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Prefix:         %{_bindir}

%description texliveonfly-bin
Binary files of texliveonfly

%package texloganalyser-bin
Version:        %{texlive_version}.%{texlive_release}.svn13663
Release:        0
License:        LPPL-1.0
Summary:        Binary files of texloganalyser
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-texloganalyser >= %{texlive_version}
#!BuildIgnore:  texlive-texloganalyser
Recommends:     texlive-collection-basic >= %{texlive_version}
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Prefix:         %{_bindir}

%description texloganalyser-bin
Binary files of texloganalyser

%package texlogfilter-bin
Version:        %{texlive_version}.%{texlive_release}.svn61780
Release:        0
License:        LPPL-1.0
Summary:        Binary files of texlogfilter
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-texlogfilter >= %{texlive_version}
#!BuildIgnore:  texlive-texlogfilter
Recommends:     texlive-collection-basic >= %{texlive_version}
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Prefix:         %{_bindir}

%description texlogfilter-bin
Binary files of texlogfilter

%package texlogsieve-bin
Version:        %{texlive_version}.%{texlive_release}.svn61328
Release:        0
License:        LPPL-1.0
Summary:        Binary files of texlogsieve
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-texlogsieve >= %{texlive_version}
#!BuildIgnore:  texlive-texlogsieve
Recommends:     texlive-collection-basic >= %{texlive_version}
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Prefix:         %{_bindir}

%description texlogsieve-bin
Binary files of texlogsieve

%package texosquery-bin
Version:        %{texlive_version}.%{texlive_release}.svn43596
Release:        0
License:        LPPL-1.0
Summary:        Binary files of texosquery
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-texosquery >= %{texlive_version}
#!BuildIgnore:  texlive-texosquery
Recommends:     texlive-collection-basic >= %{texlive_version}
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Prefix:         %{_bindir}

%description texosquery-bin
Binary files of texosquery

%package texplate-bin
Version:        %{texlive_version}.%{texlive_release}.svn53444
Release:        0
License:        LPPL-1.0
Summary:        Binary files of texplate
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-texplate >= %{texlive_version}
#!BuildIgnore:  texlive-texplate
Recommends:     texlive-collection-basic >= %{texlive_version}
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Prefix:         %{_bindir}

%description texplate-bin
Binary files of texplate

%package texsis-bin
Version:        %{texlive_version}.%{texlive_release}.svn3006
Release:        0
License:        LPPL-1.0
Summary:        Binary files of texsis
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-texsis >= %{texlive_version}
#!BuildIgnore:  texlive-texsis
Recommends:     texlive-collection-basic >= %{texlive_version}
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Prefix:         %{_bindir}

%description texsis-bin
Binary files of texsis

%package texware-bin
Version:        %{texlive_version}.%{texlive_release}.svn70571
Release:        0
License:        LPPL-1.0
Summary:        Binary files of texware
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-texware >= %{texlive_version}
#!BuildIgnore:  texlive-texware
Recommends:     texlive-collection-basic >= %{texlive_version}
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Prefix:         %{_bindir}

%description texware-bin
Binary files of texware

%package thumbpdf-bin
Version:        %{texlive_version}.%{texlive_release}.svn6898
Release:        0
License:        LPPL-1.0
Summary:        Binary files of thumbpdf
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-thumbpdf >= %{texlive_version}
#!BuildIgnore:  texlive-thumbpdf
Prefix:         %{_bindir}

%description thumbpdf-bin
Binary files of thumbpdf

%package tie-bin
Version:        %{texlive_version}.%{texlive_release}.svn70276
Release:        0
License:        LPPL-1.0
Summary:        Binary files of tie
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-tie >= %{texlive_version}
#!BuildIgnore:  texlive-tie
Prefix:         %{_bindir}

%description tie-bin
Binary files of tie

%package tikztosvg-bin
Version:        %{texlive_version}.%{texlive_release}.svn55132
Release:        0
License:        LPPL-1.0
Summary:        Binary files of tikztosvg
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-tikztosvg >= %{texlive_version}
#!BuildIgnore:  texlive-tikztosvg
Prefix:         %{_bindir}

%description tikztosvg-bin
Binary files of tikztosvg

%package tpic2pdftex-bin
Version:        %{texlive_version}.%{texlive_release}.svn50281
Release:        0
License:        LPPL-1.0
Summary:        Binary files of tpic2pdftex
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-tpic2pdftex >= %{texlive_version}
#!BuildIgnore:  texlive-tpic2pdftex
Recommends:     texlive-collection-basic >= %{texlive_version}
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Prefix:         %{_bindir}

%description tpic2pdftex-bin
Binary files of tpic2pdftex

%package ttfutils-bin
Version:        %{texlive_version}.%{texlive_release}.svn70276
Release:        0
License:        LPPL-1.0
Summary:        Binary files of ttfutils
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-ttfutils >= %{texlive_version}
#!BuildIgnore:  texlive-ttfutils
Prefix:         %{_bindir}

%description ttfutils-bin
Binary files of ttfutils

%package typeoutfileinfo-bin
Version:        %{texlive_version}.%{texlive_release}.svn25648
Release:        0
License:        LPPL-1.0
Summary:        Binary files of typeoutfileinfo
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-typeoutfileinfo >= %{texlive_version}
#!BuildIgnore:  texlive-typeoutfileinfo
Prefix:         %{_bindir}

%description typeoutfileinfo-bin
Binary files of typeoutfileinfo

%package ulqda-bin
Version:        %{texlive_version}.%{texlive_release}.svn13663
Release:        0
License:        LPPL-1.0
Summary:        Binary files of ulqda
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-ulqda >= %{texlive_version}
#!BuildIgnore:  texlive-ulqda
Prefix:         %{_bindir}

%description ulqda-bin
Binary files of ulqda

%package uplatex-bin
Version:        %{texlive_version}.%{texlive_release}.svn52800
Release:        0
License:        LPPL-1.0
Summary:        Binary files of uplatex
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-uplatex >= %{texlive_version}
#!BuildIgnore:  texlive-uplatex
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Recommends:     texlive-collection-latexrecommended >= %{texlive_version}
Prefix:         %{_bindir}

%description uplatex-bin
Binary files of uplatex

%package upmendex-bin
Version:        %{texlive_version}.%{texlive_release}.svn70276
Release:        0
License:        LPPL-1.0
Summary:        Binary files of upmendex
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-upmendex >= %{texlive_version}
#!BuildIgnore:  texlive-upmendex
Prefix:         %{_bindir}

%description upmendex-bin
Binary files of upmendex

%package uptex-bin
Version:        %{texlive_version}.%{texlive_release}.svn70571
Release:        0
License:        LPPL-1.0
Summary:        Binary files of uptex
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-uptex >= %{texlive_version}
#!BuildIgnore:  texlive-uptex
Recommends:     texlive-collection-basic >= %{texlive_version}
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Prefix:         %{_bindir}

%description uptex-bin
Binary files of uptex

%package urlbst-bin
Version:        %{texlive_version}.%{texlive_release}.svn23262
Release:        0
License:        LPPL-1.0
Summary:        Binary files of urlbst
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-urlbst >= %{texlive_version}
#!BuildIgnore:  texlive-urlbst
Prefix:         %{_bindir}

%description urlbst-bin
Binary files of urlbst

%package velthuis-bin
Version:        %{texlive_version}.%{texlive_release}.svn69782
Release:        0
License:        LPPL-1.0
Summary:        Binary files of velthuis
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-velthuis >= %{texlive_version}
#!BuildIgnore:  texlive-velthuis
Prefix:         %{_bindir}

%description velthuis-bin
Binary files of velthuis

%package vlna-bin
Version:        %{texlive_version}.%{texlive_release}.svn69782
Release:        0
License:        LPPL-1.0
Summary:        Binary files of vlna
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-vlna >= %{texlive_version}
#!BuildIgnore:  texlive-vlna
Prefix:         %{_bindir}

%description vlna-bin
Binary files of vlna

%package vpe-bin
Version:        %{texlive_version}.%{texlive_release}.svn6897
Release:        0
License:        LPPL-1.0
Summary:        Binary files of vpe
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-vpe >= %{texlive_version}
#!BuildIgnore:  texlive-vpe
Prefix:         %{_bindir}

%description vpe-bin
Binary files of vpe

%package web-bin
Version:        %{texlive_version}.%{texlive_release}.svn70571
Release:        0
License:        LPPL-1.0
Summary:        Binary files of web
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-web >= %{texlive_version}
#!BuildIgnore:  texlive-web
Prefix:         %{_bindir}

%description web-bin
Binary files of web

%package webquiz-bin
Version:        %{texlive_version}.%{texlive_release}.svn50419
Release:        0
License:        LPPL-1.0
Summary:        Binary files of webquiz
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-webquiz >= %{texlive_version}
#!BuildIgnore:  texlive-webquiz
Prefix:         %{_bindir}

%description webquiz-bin
Binary files of webquiz

%package wordcount-bin
Version:        %{texlive_version}.%{texlive_release}.svn46165
Release:        0
License:        LPPL-1.0
Summary:        Binary files of wordcount
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-wordcount >= %{texlive_version}
#!BuildIgnore:  texlive-wordcount
Prefix:         %{_bindir}

%description wordcount-bin
Binary files of wordcount

%package xdvi-bin
Version:        %{texlive_version}.%{texlive_release}.svn70276
Release:        0
License:        LPPL-1.0
Summary:        Binary files of xdvi
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-xdvi >= %{texlive_version}
#!BuildIgnore:  texlive-xdvi
Prefix:         %{_bindir}

%description xdvi-bin
Binary files of xdvi

%package xelatex-dev-bin
Version:        %{texlive_version}.%{texlive_release}.svn53999
Release:        0
License:        LPPL-1.0
Summary:        Binary files of xelatex-dev
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-xelatex-dev >= %{texlive_version}
#!BuildIgnore:  texlive-xelatex-dev
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Recommends:     texlive-collection-latexrecommended >= %{texlive_version}
Prefix:         %{_bindir}

%description xelatex-dev-bin
Binary files of xelatex-dev

%package xetex-bin
Version:        %{texlive_version}.%{texlive_release}.svn70276
Release:        0
License:        LPPL-1.0
Summary:        Binary files of xetex
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
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
License:        LPPL-1.0
Summary:        Binary files of xindex
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-xindex >= %{texlive_version}
#!BuildIgnore:  texlive-xindex
Prefix:         %{_bindir}

%description xindex-bin
Binary files of xindex

%package xml2pmx-bin
Version:        %{texlive_version}.%{texlive_release}.svn69782
Release:        0
License:        LPPL-1.0
Summary:        Binary files of xml2pmx
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-xml2pmx >= %{texlive_version}
#!BuildIgnore:  texlive-xml2pmx
Prefix:         %{_bindir}

%description xml2pmx-bin
Binary files of xml2pmx

%package xmltex-bin
Version:        %{texlive_version}.%{texlive_release}.svn3006
Release:        0
License:        LPPL-1.0
Summary:        Binary files of xmltex
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
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
Version:        %{texlive_version}.%{texlive_release}.svn69782
Release:        0
License:        LPPL-1.0
Summary:        Binary files of xpdfopen
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Obsoletes:      texlive-pdftools-bin < 2020
Requires(pre):  texlive-xpdfopen >= %{texlive_version}
#!BuildIgnore:  texlive-xpdfopen
Prefix:         %{_bindir}

%description xpdfopen-bin
Binary files of xpdfopen

%package yplan-bin
Version:        %{texlive_version}.%{texlive_release}.svn34398
Release:        0
License:        LPPL-1.0
Summary:        Binary files of yplan
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-yplan >= %{texlive_version}
#!BuildIgnore:  texlive-yplan
Prefix:         %{_bindir}

%description yplan-bin
Binary files of yplan

%package -n libkpathsea6
Version:        6.4.0
Release:        0
Summary:        Path searching library for TeX-related files
License:        LGPL-2.1-or-later
Group:          System/Libraries
URL:            https://www.tug.org/texlive/
Prefix:         %{_libdir}

%description -n libkpathsea6
Kpathsea is a library and utility programs which provide path
searching facilities for TeX file types, including the self-
locating feature required for movable installations, layered on
top of a general search mechanism. It is not distributed
separately, but rather is released and maintained as part of
the TeX-live sources.

%package -n %{name}-kpathsea-devel
Version:        6.4.0
Release:        0
Summary:        Path searching library for TeX-related files
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://www.tug.org/texlive/
Requires:       libkpathsea6 = 6.4.0

%description -n %{name}-kpathsea-devel
Kpathsea is a library and utility programs which provide path
searching facilities for TeX file types, including the self-
locating feature required for movable installations, layered on
top of a general search mechanism. It is not distributed
separately, but rather is released and maintained as part of
the TeX-live sources.

%package -n libptexenc1
Version:        1.4.6
Release:        0
Summary:        Libraries of Kanji code convert library for pTeX
License:        BSD-3-Clause
Group:          System/Libraries
URL:            https://www.tug.org/texlive/
Prefix:         %{_libdir}

%description -n libptexenc1
The ptexenc is a useful library for Japanese pTeX
(which stands for publishing TeX, and is an extension of
TeX by ASCII Co.) and its surrounding tools.

%package -n %{name}-ptexenc-devel
Version:        1.4.6
Release:        0
Summary:        Libraries of Kanji code convert library for pTeX
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            https://www.tug.org/texlive/
Requires:       libptexenc1 = 1.4.6

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
URL:            https://www.tug.org/texlive/
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
URL:            https://www.tug.org/texlive/
Requires:       libsynctex2 = 1.21

%description -n %{name}-synctex-devel
This package includes the synctex development files.
The Synchronization TeXnology by Jérôme Laurens is a new feature
of recent TeX engines.  It allows to synchronize between input
and output, which means to navigate from the source document to
the typeset material and vice versa.

%package -n libtexlua53-5
Version:        5.3.6
Release:        0
Summary:        Libraries of an extended version of pdfTeX using Lua
License:        MIT
Group:          System/Libraries
URL:            https://www.tug.org/texlive/
Prefix:         %{_libdir}

%description -n libtexlua53-5
LuaTeX is an extended version of pdfTeX using Lua as an
embedded scripting language

%package -n %{name}-texlua-devel
Version:        5.3.6
Release:        0
Summary:        Libraries of an extended version of pdfTeX using Lua
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://www.tug.org/texlive/
Requires:       libtexlua53-5 = 5.3.6

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
URL:            https://www.tug.org/texlive/
Prefix:         %{_libdir}

%description -n libtexluajit2
LuaJIT is a Just-In-Time (JIT) compiler for the Lua programming language

%package -n %{name}-texluajit-devel
Version:        2.1.0beta3
Release:        0
Summary:        Libraries of Just-In-Time compiler for Lua
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://www.tug.org/texlive/
Requires:       libtexlua53-5 = 5.3.6
Requires:       libtexluajit2 = 2.1.0beta3

%description -n %{name}-texluajit-devel
This package includes the LuaJIT development files.
LuaJIT is a Just-In-Time (JIT) compiler for the Lua programming language
%endif

%package -n %{name}-bin-devel
Version:        %{texlive_version}.%{texlive_release}
Release:        0
Summary:        Basic development packages for TeXLive
License:        BSD-3-Clause AND LGPL-2.1-or-later AND SUSE-TeX
Group:          Development/Languages/Other
URL:            https://www.tug.org/texlive/
Requires:       libkpathsea6 = 6.4.0
Requires:       libptexenc1 = 1.4.6
Requires:       libsynctex2 = 1.21
Requires:       libtexlua53-5 = 5.3.6
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
Version:        %{biber_version}
Release:        0
Summary:        Library files of Biber a BibTeX replacement
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://biblatex-biber.sourceforge.net/
Recommends:     perl(Readonly::XS)
Requires:       perl-base = %{perl_version}
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
Requires:       perl(Text::BibTeX) >= 0.88
Requires:       perl(Text::CSV)
Requires:       perl(Text::Roman)
Requires:       perl(URI)
Requires:       perl(Unicode::Collate) >= 1.29
Requires:       perl(Unicode::GCString)
Requires:       perl(XML::LibXML) >= 1.70
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
    XCXXFLAGS="$XCFLAGS -include cstdint"
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
    # Unicode
    cflags -DDECDPUN=1			XCFLAGS
    cflags -DDECNUMDIGITS=3		XCFLAGS
    #
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
    echo unset TEXINPUTS TEXMF
    echo export HOME=${PWD}/world

    # Use a well defined multi byte locale
    echo unset ${!LC_*}
    if test -d /usr/lib/locale/C.utf8
    then
        echo LANG=C.UTF-8
        echo LC_CTYPE=C.UTF-8
    else
        echo LANG=POSIX
        echo LC_CTYPE=en_US.UTF-8
    fi
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
    echo export CC CXX CFLAGS CXXFLAGS LDFLAGS VENDOR PATH CONFIG_SHELL ARCH_LIB

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

    tar --strip-components=1 -xf %{SOURCE0}
%if %{with buildbiber}
    pushd ../
	tar xf %{SOURCE1}
    popd
    pushd ../
	tar xf %{SOURCE2}
    popd
%endif
%if %{with luametatex}
    pushd ../
       tar -xf %{SOURCE3}
    popd
%endif

%patch -P1  -p0 -b .configure
%patch -P2  -p0 -b .xdvizilla
%patch -P3  -p0 -b .arraysubs
%patch -P4  -p0 -b .unicode
%patch -P5  -p0 -b .texdoc
%patch -P6  -p0 -b .dviutils
%patch -P7  -p0 -b .mesa24
%patch -P8  -p0 -b .psutils
%patch -P9  -p0 -b .perms
%patch -P11 -p0 -b .lacheck
%patch -P12 -p0 -b .warns
%patch -P13 -p0 -b .x11r7
%patch -P17 -p0 -b .64
%patch -P18 -p0 -b .a2p
%patch -P19 -p0 -b .dvipng
%patch -P21 -p0 -b .ppcelf
%patch -P22 -p0 -b .sameimg
%patch -P23 -p0 -b .gcc14
pushd libs/luajit/LuaJIT-src/
#Missed patch ppc and risc
%patch -P106 -p1 -b .arm64
popd
%patch -P0  -p0 -b .p0
%if %{with luametatex}
pushd ../luametatex*
%patch -P50 -p0 -b .unicode
popd
%endif
%if %{with buildbiber}
pushd ../biber-*/
/usr/bin/chmod -Rf a+rX,u+w,g-w,o-w .
%patch -P42 -p0 -b .en
%patch -P44 -p0 -b .noica
%if 0%{perl_versnum} < 5200
%patch -P47 -p0 -b .518
%endif
rm -vf bin/biber.noica
rm -vf t/*.fastsort
popd
pushd ../biblatex-biber-*/
/usr/bin/chmod -Rf a+rX,u+w,g-w,o-w .
%patch -P43 -p0 -b .en
%patch -P44 -p0 -b .noica
%patch -P45 -p0 -b .missing
%if 0%{perl_versnum} < 5200
%patch -P47 -p0 -b .518
%endif
rm -vf bin/biber.noica
rm -vf t/*.fastsort
popd
%endif

%patch -P62 -p0 -b .kpserr

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

    if test -d /usr/include/unicode -a -d /usr/include/harfbuzz && \
        grep -qrs UBLOCK_LATIN_EXTENDED_F /usr/include/unicode
    then
	icu[0]='--with-system-icu'
	icu[1]='--with-system-harfbuzz'
    else
	icu[0]='--without-system-icu'
	icu[1]='--without-system-harfbuzz'
    fi
    # Wrong version string
    sed -ri '/m4_define.*tex_live_version/{s@[0-9]+/dev@%{texlive_version}@}' version.ac
    for rp in $(find -name configure) ; do
	sed -ri '/(Web2C|STRING|VERSION)/{s@[0-9]+/dev@%{texlive_version}@}' $rp
    done
    for rp in $(find -name configure.ac) ; do
	sed -ri 's/KPSE_WIN32_CALL/KPSE_COND_WIN32/' $rp
    done

    # Avoid -rpath as libtool is not configurable at this point
    for rp in $(find -name libtool.m4 -or -name configure) ; do
	sed -ri 's/(-rpath)/\1-link/g' $rp
    done
    LD_LIBRARY_PATH=${prefix}/%{_lib}:${world}/texk/kpathsea/.libs:${world}/texk/ptexenc/.libs
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

    #
    # The (up)mendex unsigned character sort does not work on non-Intel boxes
    #
    sed -ri '/^CFLAGS/{ s/$/ -fsigned-char/ }' texk/mendexk/Makefile.in
    sed -ri '/^CFLAGS/{ s/$/ -fsigned-char/ }' texk/upmendex/Makefile.in

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
	    --libdir=$prefix/%{_lib}		\
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
	    --with-system-libpng		\
	    --with-system-pnglib		\
	    --with-system-gd			\
	    --with-system-zziplib		\
	    --with-system-libgs			\
	    --with-system-freetype2		\
	    --with-freetype2-includes=%{_includedir}/freetype2 \
	    --with-system-cairo			\
	    --with-system-includes=%{_includedir}/cairo \
	    --with-system-mpfr			\
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

	testsuite () {
	    test -s ${world}/texk/bibtex-x/test-suite.log || return
	    cat ${world}/texk/bibtex-x/test-suite.log
	    for log in ${world}/texk/bibtex-x/tests/*.log
	    do
		echo $log
		cat $log
	    done
	    rm -vf %{options}
	}
	trap "testsuite" ERR

	PATH=$prefix/bin:$PATH			\
	TEXMFLOCAL=%{_texmfmaindir}		\
	TEXMFCNF=$texmfcnf			\
	make %{?_smp_mflags} world STRIP=/bin/true STRIPPROG=/bin/true

	trap 'rm -vf %{options}' ERR

    popd

    pushd utils/asymptote
	autoreconf
	if pkg-config --atleast-version 25 dri
	then
	    (cat>libOSMesa.so)<<-'EOF'
		/* GNU ld script */
		INPUT(%{_libdir}/libOSMesa.so AS_NEEDED(-lgallium))
		EOF
	else
	    (cat>libOSMesa.so)<<-'EOF'
		/* GNU ld script */
		INPUT(%{_libdir}/libOSMesa.so AS_NEEDED(-lglapi))
		EOF
	fi
	PATH=$prefix/bin:$PATH			\
	TEXMFLOCAL=%{_texmfmaindir}		\
	TEXMFCNF=$texmfcnf			\
	STRIP=/bin/true				\
	STRIPPROG=/bin/true			\
	LDFLAGS="$LDFLAGS -L$PWD"		\
	CFLAGS="${CFLAGS/-Wno-unprototyped-calls/}"	\
	CXXFLAGS="${CXXFLAGS/-Wno-unprototyped-calls/}"	\
	CFLAGS="${CFLAGS/-std=gnu99/}"		\
	CXXFLAGS="${CXXFLAGS/-std=gnu99/}"	\
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
	make asy
	mkdir -p ${prefix}/bin
	mkdir -p ${prefix}/texmf/asymptote/GUI
	install -m 0755 asy		${prefix}/bin/
	install -m 0755 GUI/xasy.py	${prefix}/texmf/asymptote/GUI
	ln -sf ../texmf/asymptote/GUI/xasy.py ${prefix}/bin/xasy
    popd

    # compile public
    mkdir -p %{libexecdir}/mktex
    $CC ${RPM_OPT_FLAGS} -D_GNU_SOURCE -DTEXGRP='"%{texgrp}"' -DTEXUSR='"%{texusr}"' -DMKTEX='"%{_libexecdir}/mktex"' -fPIE -pie -o %{libexecdir}/mktex/public %{S:50}

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

%if %{with luametatex}
    pushd ../luametatex*
        %cmake \
        -DVERBOSE=ON \
        -DCMAKE_C_COMPILER=gcc \
        -DCMAKE_STRIP:FILEPATH=/bin/true \
        -DCMAKE_CXX_COMPILER=g++
        cmake --build . --parallel %{?_smp_mflags}
    popd
%endif
%if %{with buildbiber}
    # dump a biber executable
    pushd ../biber-*/
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
    pushd ../biblatex-biber-*/
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
    pushd ${prefix}/%{_lib}/
	tar -cpSf - *.so* | tar -xvspSf - -C %{buildroot}%{_libdir}/
    popd
    pushd %{libexecdir}/
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
%if %{with luametatex}
    pushd ../luametatex*
        %cmake_install
        for exe in context mtxrun
        do
            ln -sf luametatex %{buildroot}%{_bindir}/${exe}
            ln -sf %{_texmfdistdir}/scripts/context/lua/${exe}.lua %{buildroot}%{_bindir}/${exe}.lua
        done
        ln -sf %{_texmfdistdir}/scripts/context/lua/mtx-context.lua %{buildroot}%{_bindir}/mtx-context.lua
        for exe in texexec texmfstart
        do
            ln -sf %{_texmfdistdir}/scripts/context/ruby/${exe}.rb %{buildroot}%{_bindir}/${exe}
        done
        for exe in contextjit luatools mtxrunjit
        do
            ln -sf %{_texmfdistdir}/scripts/context-texlive/stubs-mkiv/unix/${exe} %{buildroot}%{_bindir}/${exe}
        done
    popd
%endif
    #
    # Biber support
    #
%if %{with buildbiber}
    pushd ../biblatex-biber-*/
	./Build install destdir=%{buildroot}
	chmod    0755 %{buildroot}%{_bindir}/biber
	rm -vf        %{buildroot}%{_mandir}/man1/biber.1*
	chmod    0644 %{buildroot}%{perl_vendorlib}/Biber.pm
	chmod -R u+rw %{buildroot}%{perl_vendorlib}/Biber
	mkdir %{buildroot}%{perl_vendorlib}/biber-ms
	mv %{buildroot}%{perl_vendorlib}/Biber.pm %{buildroot}%{perl_vendorlib}/biber-ms/Biber.pm
	mv %{buildroot}%{perl_vendorlib}/Biber    %{buildroot}%{perl_vendorlib}/biber-ms/Biber
	mv %{buildroot}%{_bindir}/biber           %{buildroot}%{_bindir}/biber-ms
	if test -d %{buildroot}%{perl_vendorlib}/Unicode/Collate
	then
	    chmod -R u+rw %{buildroot}%{perl_vendorlib}/Unicode/Collate/*
	fi
	rm -vrf %{buildroot}%{perl_vendorarch}/auto
	rm -vrf %{buildroot}%{_mandir}/man3
	%perl_process_packlist
	%perl_gen_filelist
	pushd blib
	    install -m 0644 bindoc/biber.1 %{buildroot}%{_mandir}/man1/biber-ms.1
	    gzip -n9 %{buildroot}%{_mandir}/man1/biber-ms.1
	popd
	sed -ri "/^use warnings;/a\use lib %{perl_vendorlib}/biber-ms;" %{buildroot}%{_bindir}/biber-ms
	sed -ri '\@/usr/(share|bin)/.*@d' texlive.files
    popd
    mv ../biblatex-biber-*/texlive.files perl-biber-ms.files
    pushd ../biber-*/
	./Build install destdir=%{buildroot}
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
	    gzip -n9 %{buildroot}%{_mandir}/man1/biber.1
	popd
	sed -ri '\@/usr/(share|bin)/.*@d' texlive.files
    popd
    mv ../biber-*/texlive.files perl-biber.files
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
                /*)             ;;
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
		test "$fmt" = "pdfcsplain" && engine=pdftex
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
%if 0%{texlive_version} >= 2023
	ln -vsf ../share/texmf/scripts/texlive/rungs.lua rungs
	rm -vf %{buildroot}%{_texmfdistdir}/scripts/texlive/rungs.lua
%else
	ln -vsf ../share/texmf/scripts/texlive/rungs.tlu rungs
	rm -vf %{buildroot}%{_texmfdistdir}/scripts/texlive/rungs.tlu
%endif
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
    gzip -n9 %{buildroot}%{_mandir}/man8/public.8

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
	texhash*)
	   ln -sf ../../share/texmf/scripts/texlive/mktexlsr.pl %{buildroot}%{_libexecdir}/mktex/$mktex
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

    pushd ${prefix}/%{_lib}/pkgconfig/
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
	%{_bindir}/biber-ms \
%else
    for scr in \
%endif
	%{_texmfdistdir}/scripts/texlive/rungs.tlu \
	%{_texmfdistdir}/scripts/texlive/rungs.lua
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
# Currently disabled due python2 requirement
rm -vf %{buildroot}%{_bindir}/ebong

%if %{defined verify_permissions}
%verifyscript kpathsea-bin
%verify_permissions -e %{_libexecdir}/mktex/public
%endif

%post kpathsea-bin
%if %{defined set_permissions}
%set_permissions %{_libexecdir}/mktex/public
%endif

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

%if %{with luametatex}
%post context-bin
mkdir -p /var/run/texlive
> /var/run/texlive/run-fmtutil.context

%postun context-bin
if test $1 = 1; then
    mkdir -p /var/run/texlive
    > /var/run/texlive/run-fmtutil.context
fi
%endif

%files
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
%{_mandir}/man8/public.8%{?ext_man}
%if %{with zypper_posttrans}
%verify(link) /var/adm/update-scripts/%{name}-%{version}-%{release}-zypper
%endif

%files a2ping-bin
%{_bindir}/a2ping

%files accfonts-bin
%{_bindir}/mkt1font
%{_bindir}/vpl2ovp
%{_bindir}/vpl2vpl

%files adhocfilelist-bin
%{_bindir}/adhocfilelist

%files afm2pl-bin
%{_bindir}/afm2pl

%files albatross-bin
%{_bindir}/albatross

%files aleph-bin
%{_bindir}/aleph

%files amstex-bin
%{_bindir}/amstex

%files arara-bin
%{_bindir}/arara

%files asymptote-bin
%{_bindir}/asy
%{_bindir}/xasy

%files attachfile2-bin
%{_bindir}/pdfatfi

%files authorindex-bin
%{_bindir}/authorindex

%files autosp-bin
%{_bindir}/autosp
%{_bindir}/tex2aspc

%files axodraw2-bin
%{_bindir}/axohelp

%files bib2gls-bin
%{_bindir}/bib2gls
%{_bindir}/convertgls2bib

%files bibcop-bin
%{_bindir}/bibcop

%files biber-ms-bin
%{_bindir}/biber-ms
%if %{with buildbiber}
%{_mandir}/man1/biber-ms.1%{ext_man}
%endif

%files biber-bin
%{_bindir}/biber
%if %{with buildbiber}
%{_mandir}/man1/biber.1%{ext_man}
%endif

%files bibexport-bin
%{_bindir}/bibexport

%files bibtex-bin
%{_bindir}/bibtex

%files bibtex8-bin
%{_bindir}/bibtex8

%files bibtexperllibs-bin
%{_bindir}/ltx2unitxt

%files bibtexu-bin
%{_bindir}/bibtexu

%files bundledoc-bin
%{_bindir}/arlatex
%{_bindir}/bundledoc

%files cachepic-bin
%{_bindir}/cachepic

%files checkcites-bin
%{_bindir}/checkcites

%files checklistings-bin
%{_bindir}/checklistings

%files chklref-bin
%{_bindir}/chklref

%files chktex-bin
%{_bindir}/chktex
%{_bindir}/chkweb
%{_bindir}/deweb

%files citation-style-language-bin
%{_bindir}/citeproc-lua

%files cjk-gs-integrate-bin
%{_bindir}/cjk-gs-integrate

%files cjkutils-bin
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
%{_bindir}/pamphletangler

%files cluttex-bin
%{_bindir}/cllualatex
%{_bindir}/cluttex
%{_bindir}/clxelatex

%files context-legacy-bin
%{_bindir}/texexec
%{_bindir}/texmfstart

%files context-texlive-bin
%{_bindir}/contextjit
%{_bindir}/luatools
%{_bindir}/mtxrunjit

%files context-bin
%{_bindir}/context
%{_bindir}/context.lua
%{_bindir}/luametatex
%{_bindir}/mtxrun
%{_bindir}/rlxtools
%{_bindir}/mtxrun.lua
%{_bindir}/mtx-context.lua

%files convbkmk-bin
%{_bindir}/convbkmk

%files crossrefware-bin
%{_bindir}/bbl2bib
%{_bindir}/bibdoiadd
%{_bindir}/bibmradd
%{_bindir}/biburl2doi
%{_bindir}/bibzbladd
%{_bindir}/ltx2crossrefxml

%files csplain-bin
%{_bindir}/csplain
%{_bindir}/luacsplain
%{_bindir}/pdfcsplain

%files ctan-o-mat-bin
%{_bindir}/ctan-o-mat

%files ctanbib-bin
%{_bindir}/ctanbib

%files ctanify-bin
%{_bindir}/ctanify

%files ctanupload-bin
%{_bindir}/ctanupload

%files ctie-bin
%{_bindir}/ctie

%files cweb-bin
%{_bindir}/ctangle
%{_bindir}/ctwill
%{_bindir}/ctwill-proofsort
%{_bindir}/ctwill-refsort
%{_bindir}/ctwill-twinx
%{_bindir}/cweave
%{_bindir}/twill
%{_bindir}/twill-refsort

%files cyrillic-bin-bin
%{_bindir}/rubibtex
%{_bindir}/rumakeindex

%files de-macro-bin
%{_bindir}/de-macro

%files detex-bin
%{_bindir}/detex

%files diadia-bin
%{_bindir}/diadia

%files digestif-bin
%{_bindir}/digestif

%files dosepsbin-bin
%{_bindir}/dosepsbin

%files dtl-bin
%{_bindir}/dt2dv
%{_bindir}/dv2dt

%files dtxgen-bin
%{_bindir}/dtxgen

%files dviasm-bin
%{_bindir}/dviasm

%files dvicopy-bin
%{_bindir}/dvicopy

%files dvidvi-bin
%{_bindir}/dvidvi

%files dviinfox-bin
%{_bindir}/dviinfox

%files dviljk-bin
%{_bindir}/dvihp
%{_bindir}/dvilj
%{_bindir}/dvilj2p
%{_bindir}/dvilj4
%{_bindir}/dvilj4l
%{_bindir}/dvilj6

%files dviout-util-bin
%{_bindir}/chkdvifont
%{_bindir}/dvispc

%files dvipdfmx-bin
%{_bindir}/dvipdfm
%{_bindir}/dvipdfmx
%{_bindir}/dvipdft
%{_bindir}/ebb
%{_bindir}/extractbb
%{_bindir}/xdvipdfmx

%files dvipng-bin
%{_bindir}/dvigif
%{_bindir}/dvipng

%files dvipos-bin
%{_bindir}/dvipos

%files dvips-bin
%{_bindir}/afm2tfm
%{_bindir}/dvips

%files dvisvgm-bin
%{_bindir}/dvisvgm

%files easydtx-bin
%{_bindir}/edtx2dtx

%files eolang-bin
%{_bindir}/eolang

%files eplain-bin
%{_bindir}/eplain

%files epspdf-bin
%{_bindir}/epspdf
%{_bindir}/epspdftk

%files epstopdf-bin
%{_bindir}/epstopdf
%{_bindir}/repstopdf

%files exceltex-bin
%{_bindir}/exceltex

%files fig4latex-bin
%{_bindir}/fig4latex

%files findhyph-bin
%{_bindir}/findhyph

%files fontinst-bin
%{_bindir}/fontinst

%files fontools-bin
%{_bindir}/afm2afm
%{_bindir}/autoinst
%{_bindir}/ot2kpx

%files fontware-bin
%{_bindir}/pltotf
%{_bindir}/tftopl
%{_bindir}/vftovp
%{_bindir}/vptovf

%files fragmaster-bin
%{_bindir}/fragmaster

%files getmap-bin
%{_bindir}/getmapdl

%files git-latexdiff-bin
%{_bindir}/git-latexdiff

%files glossaries-bin
%{_bindir}/makeglossaries
%{_bindir}/makeglossaries-lite

%files gregoriotex-bin
%{_bindir}/gregorio

%files gsftopk-bin
%{_bindir}/gsftopk

%files hitex-bin
%{_bindir}/hilatex
%{_bindir}/hishrink
%{_bindir}/histretch
%{_bindir}/hitex

%files hyperxmp-bin
%{_bindir}/hyperxmp-add-bytecount

%files jadetex-bin
%{_bindir}/jadetex
%{_bindir}/pdfjadetex

%files jfmutil-bin
%{_bindir}/jfmutil

%files ketcindy-bin
%{_bindir}/ketcindy

%files kotex-utils-bin
%{_bindir}/jamo-normalize
%{_bindir}/komkindex
%{_bindir}/ttf2kotexfont

%files kpathsea-bin
%{_bindir}/kpseaccess
%{_bindir}/kpsereadlink
%{_bindir}/kpsestat
%{_bindir}/kpsewhich
%{_bindir}/mktexlsr
%attr(2755,root,%{texgrp}) %{_libexecdir}/mktex/public
%{_libexecdir}/mktex/*tex*

%files l3build-bin
%{_bindir}/l3build

%files lacheck-bin
%{_bindir}/lacheck

%files latex-bin-dev-bin
%{_bindir}/dvilualatex-dev
%{_bindir}/latex-dev
%{_bindir}/lualatex-dev
%{_bindir}/pdflatex-dev

%files latex-bin-bin
%{_bindir}/dvilualatex
%{_bindir}/latex
%{_bindir}/lualatex
%{_bindir}/pdflatex

%files latex-git-log-bin
%{_bindir}/latex-git-log

%files latex-papersize-bin
%{_bindir}/latex-papersize

%files latex2man-bin
%{_bindir}/latex2man

%files latex2nemeth-bin
%{_bindir}/latex2nemeth

%files latexdiff-bin
%{_bindir}/latexdiff
%{_bindir}/latexdiff-vc
%{_bindir}/latexrevise

%files latexfileversion-bin
%{_bindir}/latexfileversion

%files latexindent-bin
%{_bindir}/latexindent

%files latexmk-bin
%{_bindir}/latexmk

%files latexpand-bin
%{_bindir}/latexpand

%files lcdftypetools-bin
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

%files light-latex-make-bin
%{_bindir}/llmk

%files lilyglyphs-bin
%{_bindir}/lily-glyph-commands
%{_bindir}/lily-image-commands
%{_bindir}/lily-rebuild-pdfs

%files listbib-bin
%{_bindir}/listbib

%files listings-ext-bin
%{_bindir}/listings-ext.sh

%files lollipop-bin
%{_bindir}/lollipop

%files ltxfileinfo-bin
%{_bindir}/ltxfileinfo

%files ltximg-bin
%{_bindir}/ltximg

%files luafindfont-bin
%{_bindir}/luafindfont

%files luahbtex-bin
%{_bindir}/luahbtex

%files luajittex-bin
%{_bindir}/luajithbtex
%{_bindir}/luajittex
%{_bindir}/texluajit
%{_bindir}/texluajitc

%files luaotfload-bin
%{_bindir}/luaotfload-tool

%files luatex-bin
%{_bindir}/dviluatex
%{_bindir}/luatex
%{_bindir}/texlua
%{_bindir}/texluac

%files lwarp-bin
%{_bindir}/lwarpmk

%files m-tx-bin
%{_bindir}/m-tx
%{_bindir}/prepmx

%files make4ht-bin
%{_bindir}/make4ht

%files makedtx-bin
%{_bindir}/makedtx

%files makeindex-bin
%{_bindir}/makeindex
%{_bindir}/mkindex

%files match_parens-bin
%{_bindir}/match_parens

%files mathspic-bin
%{_bindir}/mathspic

%files memoize-bin
%{_bindir}/memoize-clean
%{_bindir}/memoize-extract

%files metafont-bin
%{_bindir}/inimf
%{_bindir}/mf
%{_bindir}/mf-nowin

%files metapost-bin
%{_bindir}/dvitomp
%{_bindir}/mfplain
%{_bindir}/mpost
%{_bindir}/r-mpost

%files mex-bin
%{_bindir}/mex
%{_bindir}/pdfmex
%{_bindir}/utf8mex

%files mf2pt1-bin
%{_bindir}/mf2pt1

%files mflua-bin
%{_bindir}/mflua
%{_bindir}/mflua-nowin
%if %{with LuaJIT}
%{_bindir}/mfluajit
%endif
%if %{with LuaJIT}
%{_bindir}/mfluajit-nowin
%endif

%files mfware-bin
%{_bindir}/gftodvi
%{_bindir}/gftopk
%{_bindir}/gftype
%{_bindir}/mft
%{_bindir}/pktogf
%{_bindir}/pktype

%files mkgrkindex-bin
%{_bindir}/mkgrkindex

%files mkjobtexmf-bin
%{_bindir}/mkjobtexmf

%files mkpic-bin
%{_bindir}/mkpic

%files mltex-bin
%{_bindir}/mllatex
%{_bindir}/mltex

%files mptopdf-bin
%{_bindir}/mptopdf

%files multibibliography-bin
%{_bindir}/multibibliography

%files musixtex-bin
%{_bindir}/musixflx
%{_bindir}/musixtex
%{_bindir}/pdfmusixtex

%files musixtnt-bin
%{_bindir}/msxlint

%files omegaware-bin
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
%{_bindir}/optex

%files optexcount-bin
%{_bindir}/optexcount

%files pagelayout-bin
%{_bindir}/pagelayoutapi
%{_bindir}/textestvis

%files patgen-bin
%{_bindir}/patgen

%files pax-bin
%{_bindir}/pdfannotextractor

%files pdfbook2-bin
%{_bindir}/pdfbook2

%files pdfcrop-bin
%{_bindir}/pdfcrop
%{_bindir}/rpdfcrop

%files pdfjam-bin
%{_bindir}/pdfjam

%files pdflatexpicscale-bin
%{_bindir}/pdflatexpicscale

%files pdftex-quiet-bin
%{_bindir}/pdftex-quiet

%files pdftex-bin
%{_bindir}/etex
%{_bindir}/pdfetex
%{_bindir}/pdftex
%{_bindir}/simpdftex

%files pdftosrc-bin
%{_bindir}/pdftosrc

%files pdfxup-bin
%{_bindir}/pdfxup

%files pedigree-perl-bin
%{_bindir}/pedigree

%files perltex-bin
%{_bindir}/perltex

%files petri-nets-bin
%{_bindir}/pn2pdf

%files pfarrei-bin
%{_bindir}/a5toa4
%{_bindir}/pfarrei

%files pkfix-helper-bin
%{_bindir}/pkfix-helper

%files pkfix-bin
%{_bindir}/pkfix

%files platex-bin
%{_bindir}/platex
%{_bindir}/platex-dev

%files pmx-bin
%{_bindir}/pmxab
%{_bindir}/scor2prt

%files pmxchords-bin
%{_bindir}/pmxchords

%files ps2eps-bin
%{_bindir}/bbox
%{_bindir}/ps2eps

%files ps2pk-bin
%{_bindir}/mag
%{_bindir}/pfb2pfa
%{_bindir}/pk2bm
%{_bindir}/ps2pk

%files pst-pdf-bin
%{_bindir}/ps4pdf

%files pst2pdf-bin
%{_bindir}/pst2pdf

%files ptex-fontmaps-bin
%{_bindir}/kanji-config-updmap
%{_bindir}/kanji-config-updmap-sys
%{_bindir}/kanji-config-updmap-user
%{_bindir}/kanji-fontmap-creator

%files ptex-bin
%{_bindir}/eptex
%{_bindir}/makejvf
%{_bindir}/mendex
%{_bindir}/pbibtex
%{_bindir}/pdvitomp
%{_bindir}/pdvitype
%{_bindir}/pmpost
%{_bindir}/ppltotf
%{_bindir}/ptekf
%{_bindir}/ptex
%{_bindir}/ptftopl
%{_bindir}/r-pmpost

%files ptex2pdf-bin
%{_bindir}/ptex2pdf

%files purifyeps-bin
%{_bindir}/purifyeps

%files pygmentex-bin
%{_bindir}/pygmentex

%files pythontex-bin
%{_bindir}/depythontex
%{_bindir}/pythontex

%files rubik-bin
%{_bindir}/rubikrotation

%files runtexshebang-bin
%{_bindir}/runtexshebang

%files seetexk-bin
%{_bindir}/dvibook
%{_bindir}/dviconcat
%{_bindir}/dviselect
%{_bindir}/dvitodvi
%{_bindir}/a4toa5
%{_bindir}/mydvichk
%{_bindir}/odd2even

%files spix-bin
%{_bindir}/spix

%files splitindex-bin
%{_bindir}/splitindex

%files srcredact-bin
%{_bindir}/srcredact

%files sty2dtx-bin
%{_bindir}/sty2dtx

%files svn-multi-bin
%{_bindir}/svn-multi

%files synctex-bin
%{_bindir}/synctex

%files tex-bin
%{_bindir}/initex
%{_bindir}/tex

%files tex4ebook-bin
%{_bindir}/tex4ebook

%files tex4ht-bin
%{_bindir}/ht
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

%files texaccents-bin
%{_bindir}/texaccents

%files texblend-bin
%{_bindir}/texblend

%files texcount-bin
%{_bindir}/texcount

%files texdef-bin
%{_bindir}/latexdef
%{_bindir}/texdef

%files texdiff-bin
%{_bindir}/texdiff

%files texdirflatten-bin
%{_bindir}/texdirflatten

%files texdoc-bin
%{_bindir}/texdoc

%files texdoctk-bin
%{_bindir}/texdoctk

%files texfindpkg-bin
%{_bindir}/texfindpkg

%files texfot-bin
%{_bindir}/texfot

%files -n texlive-scripts-extra-bin
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
%{_bindir}/texliveonfly

%files texloganalyser-bin
%{_bindir}/texloganalyser

%files texlogfilter-bin
%{_bindir}/texlogfilter

%files texlogsieve-bin
%{_bindir}/texlogsieve

%files texosquery-bin
%{_bindir}/texosquery
%{_bindir}/texosquery-jre5
%{_bindir}/texosquery-jre8

%files texplate-bin
%{_bindir}/texplate

%files texsis-bin
%{_bindir}/texsis

%files texware-bin
%{_bindir}/dvitype
%{_bindir}/pooltype

%files thumbpdf-bin
%{_bindir}/thumbpdf

%files tie-bin
%{_bindir}/tie

%files tikztosvg-bin
%{_bindir}/tikztosvg

%files tpic2pdftex-bin
%{_bindir}/tpic2pdftex

%files ttfutils-bin
%{_bindir}/ttf2afm
%{_bindir}/ttf2pk
%{_bindir}/ttf2tfm
%{_bindir}/ttfdump

%files typeoutfileinfo-bin
%{_bindir}/typeoutfileinfo

%files ulqda-bin
%{_bindir}/ulqda

%files uplatex-bin
%{_bindir}/uplatex
%{_bindir}/uplatex-dev

%files upmendex-bin
%{_bindir}/upmendex

%files uptex-bin
%{_bindir}/euptex
%{_bindir}/r-upmpost
%{_bindir}/upbibtex
%{_bindir}/updvitomp
%{_bindir}/updvitype
%{_bindir}/upmpost
%{_bindir}/uppltotf
%{_bindir}/uptex
%{_bindir}/uptftopl
%{_bindir}/wovp2ovf

%files urlbst-bin
%{_bindir}/urlbst

%files velthuis-bin
%{_bindir}/devnag

%files vlna-bin
%{_bindir}/vlna

%files vpe-bin
%{_bindir}/vpe

%files web-bin
%{_bindir}/tangle
%{_bindir}/weave

%files webquiz-bin
%{_bindir}/webquiz

%files wordcount-bin
%{_bindir}/wordcount

%files xdvi-bin
%{_bindir}/xdvi
%{_bindir}/xdvi-xaw3d

%files xelatex-dev-bin
%{_bindir}/xelatex-dev

%files xetex-bin
%{_bindir}/teckit_compile
%{_bindir}/xelatex
%{_bindir}/xelatex-unsafe
%{_bindir}/xetex
%{_bindir}/xetex-unsafe

%files xindex-bin
%{_bindir}/xindex

%files xml2pmx-bin
%{_bindir}/xml2pmx

%files xmltex-bin
%{_bindir}/pdfxmltex
%{_bindir}/xmltex

%files xpdfopen-bin
%{_bindir}/pdfclose
%{_bindir}/pdfopen

%files yplan-bin
%{_bindir}/yplan

%files -n libkpathsea6
%{_libdir}/libkpathsea*.so.*

%files -n %{name}-kpathsea-devel
%dir %{_includedir}/kpathsea
%{_includedir}/kpathsea/*
%{_libdir}/libkpathsea.so
%{_libdir}/pkgconfig/kpathsea.pc

%files -n libptexenc1
%{_libdir}/libptexenc*.so.*

%files -n %{name}-ptexenc-devel
%dir %{_includedir}/ptexenc
%{_includedir}/ptexenc/*
%{_libdir}/libptexenc.so
%{_libdir}/pkgconfig/ptexenc.pc

%files -n libsynctex2
%{_libdir}/libsynctex.so.*

%files -n %{name}-synctex-devel
%dir %{_includedir}/synctex/
%{_includedir}/synctex/*.h
%{_libdir}/libsynctex.so
%{_libdir}/pkgconfig/synctex.pc

%files -n libtexlua53-5
%{_libdir}/libtexlua53*so.*

%files -n %{name}-texlua-devel
%dir %{_includedir}/texlua[0-9]*/
%{_includedir}/texlua[0-9]*/*.h*
%{_libdir}/libtexlua[0-9]*so
%{_libdir}/pkgconfig/texlua[0-9]*.pc

%if %{with LuaJIT}
%files -n libtexluajit2
%{_libdir}/libtexluajit.so.*

%files -n %{name}-texluajit-devel
%dir %{_includedir}/texluajit/
%{_includedir}/texluajit/*.h*
%{_libdir}/libtexluajit.so
%{_libdir}/pkgconfig/texluajit.pc
%endif

%files -n %{name}-bin-devel

%if %{with buildbiber}
%files -n perl-biber -f perl-biber.files
%endif

%changelog
