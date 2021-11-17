#
# spec file for package xdo
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


Name:           xdo
Version:        0.5.7
Release:        0
Summary:        A tool to perform actions on windows
License:        BSD-2-Clause
Group:          System/X11/Utilities
URL:            https://github.com/baskerville/xdo
Source:         xdo-0.5.7.tar.gz
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-aux)
BuildRequires:  pkgconfig(xcb-ewmh)
BuildRequires:  pkgconfig(xcb-icccm)

%description
The tool lets you perform actions such as inspect, raise, lower, inject input on
X11 windows. Xdo is compatible with both Xorg and Xwayland.

%prep
%setup -q
%autopatch -p1

%build
CFLAGS="%{optflags}" %make_build

%install
%make_install PREFIX="%{_prefix}"

%files
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
