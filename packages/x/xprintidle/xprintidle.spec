#
# spec file for package xprintidle
#
# Copyright (c) 2023 SUSE LLC
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


Name:           xprintidle
Version:        0.2.5
Release:        0
Summary:        Utility to print user's idle time in X
License:        GPL-2.0-only
Group:          System/X11/Utilities
URL:            https://github.com/g0hl1n/xprintidle
Source:         http://httpredir.debian.org/debian/pool/main/x/%{name}/%{name}_%{version}.orig.tar.gz
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xscrnsaver)

%description
An utility that queries the X server for the user's idle time and
prints it to stdout (in milliseconds).

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
