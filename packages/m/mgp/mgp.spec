#
# spec file for package mgp
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           mgp
Version:        1.13a
Release:        0
Summary:        MagicPoint, an X Window System Presentation Tool
License:        BSD-3-Clause
Group:          Productivity/Publishing/Presentation
Url:            http://member.wide.ad.jp/wg/mgp/
Source:         magicpoint-%{version}.tar.bz2
Source1:        README.SUSE
Patch1:         magicpoint-ia64.diff
Patch2:         magicpoint-imlib2.patch
Patch3:         magicpoint-%{version}-tffonts.diff
Patch5:         magicpoint-%{version}-sample.diff
Patch6:         magicpoint-%{version}-nonvoid.diff
Patch7:         magicpoint-%{version}-cflags.diff
Patch8:         magicpoint-%{version}-compile-warning.diff
Patch9:         magicpoint-%{version}-null.diff
Patch10:        magicpoint-%{version}-xft-rendering-fix.diff
Patch11:        magicpoint-%{version}-lib64.diff
Patch13:        magicpoint-%{version}-warnings.patch
Patch14:        mgp-bilinear-zoom.diff
Patch15:        mgp-imlib2-segfault-fix.diff
Patch16:        mgp-alpha-channel.diff
Patch17:        mpg-netpbm-jpeg-fix.diff
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  emacs-nox
BuildRequires:  flex
BuildRequires:  imake
BuildRequires:  imlib2-devel
BuildRequires:  pkgconfig
BuildRequires:  sharutils
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xmu)
Requires:       perl
Requires:       sharutils
Recommends:     imlib2
Provides:       magicpoint

%description
MagicPoint is an X Window System presentation tool. It is designed to
make simple presentations easy while making complicated presentations
possible. Its presentation file (the suffix is typically .mgp) is plain
text so that you can create presentation files quickly with your
favorite editor (Emacs, for example). The package also includes the
tools mgp2html, mgp2ps, and mgp2latex, which convert mgp presentations
into other file formats.

%prep
%setup -q -n magicpoint-%{version}
#%patch
%patch1
%patch2  -p1
# %patch3
%patch5 -p1
%patch6
%patch7 -p1
%patch8
%patch9
#patch10
%patch11
%patch13
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
cp %{SOURCE1} .
rm -rf sample/CVS

%build
autoreconf -fiv
# FIXME: you should use the %%configure macro
%configure --disable-gif \
  --enable-imlib \
  --enable-locale \
  --disable-vflib \
  --disable-freetype
xmkmf -a
make Makefiles
make CCOPTIONS="%{optflags}"
emacs --batch --no-site -f batch-byte-compile contrib/mgp-mode20.el

%install
%make_install install.man
install -d %{buildroot}%{_bindir}
install -c contrib/mgp2html.pl %{buildroot}%{_bindir}/mgp2html
install -c contrib/mgp2latex.pl %{buildroot}%{_bindir}/mgp2latex
install -d %{buildroot}%{_datadir}/emacs/site-lisp
install -p -m644 contrib/mgp-mode20.el{,c} %{buildroot}%{_datadir}/emacs/site-lisp
cd sample
rm .cvsignore Imakefile* Makefile* README.jp

%files
%doc README README.fonts README.lang RELNOTES SYNTAX USAGE
%doc sample/README sample/
%doc README.SUSE
%{_bindir}/*
%if "%{_bindir}" != "%{_bindir}"
# mgp used to install both into /usr/bin and /usr/X11R6/bin
%{_bindir}/*
%endif
%{_prefix}/lib/X11/mgp/
%{_mandir}/man1/*
%{_datadir}/emacs/site-lisp/mgp-mode20.*

%changelog
