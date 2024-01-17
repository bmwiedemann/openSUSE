#
# spec file for package x2x
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


Name:           x2x
Version:        1.30rc1+git.20180517
Release:        0
Summary:        X Window System Display Remote Control
License:        GPL-2.0+
Group:          System/X11/Utilities
Url:            https://github.com/dottedmag/x2x
Source:         %{name}-%{version}.tar.xz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xscrnsaver)
BuildRequires:  pkgconfig(xtst)

%description
x2x allows the keyboard and mouse on one ("from") X Window System
display to be used to control another ("to") X Window System display.

%prep
%setup -q

%build
autoreconf -i
%configure CPPFLAGS="-Wno-unprototyped-calls"
make %{?_smp_mflags}

%install
%make_install

%files
%{_bindir}/x2x
%{_datadir}/doc/x2x/
%{_mandir}/man1/x2x.1%{ext_man}

%changelog
