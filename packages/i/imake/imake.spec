#
# spec file for package imake
#
# Copyright (c) 2021 SUSE LLC
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


Name:           imake
Version:        1.0.8
Release:        0
Summary:        C preprocessor interface to the make utility
License:        MIT
Group:          Development/Tools/Building
URL:            https://xorg.freedesktop.org/
Source0:        https://xorg.freedesktop.org/releases/individual/util/%{name}-%{version}.tar.bz2
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xproto)
# For Imake.tmpl, Just in case packagers don't know it's in this package.
Requires:       xorg-cf-files
# This was part of the xorg-x11-util-devel package up to version 7.6
Conflicts:      xorg-x11-util-devel <= 7.6

%description
Imake is used to generate Makefiles from a template, a set of cpp macro
functions, and a per-directory input file called an Imakefile.

The X Window System used imake extensively up through the X11R6.9
release, for both full builds within the source tree and external
software. X has since moved to GNU autoconf and automake for its build
system in X11R7.0 and later releases, but still maintains imake for
building existing external software programs that have not yet
converted.

%prep
%setup -q

%build
%configure --with-config-dir=%{_datadir}/X11/config
%make_build

%install
%make_install

%files
%license COPYING
%doc ChangeLog README.md
%{_bindir}/ccmakedep
%{_bindir}/cleanlinks
%{_bindir}/imake
%{_bindir}/makeg
%{_bindir}/mergelib
%{_bindir}/mkdirhier
%{_bindir}/mkhtmlindex
%{_bindir}/revpath
%{_bindir}/xmkmf
%{_mandir}/man1/ccmakedep.1%{?ext_man}
%{_mandir}/man1/cleanlinks.1%{?ext_man}
%{_mandir}/man1/imake.1%{?ext_man}
%{_mandir}/man1/makeg.1%{?ext_man}
%{_mandir}/man1/mergelib.1%{?ext_man}
%{_mandir}/man1/mkdirhier.1%{?ext_man}
%{_mandir}/man1/mkhtmlindex.1%{?ext_man}
%{_mandir}/man1/revpath.1%{?ext_man}
%{_mandir}/man1/xmkmf.1%{?ext_man}

%changelog
