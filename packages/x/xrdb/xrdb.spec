#
# spec file for package xrdb
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           xrdb
Version:        1.2.0
Release:        0
Summary:        X server resource database utility
License:        MIT
Group:          System/X11/Utilities
Url:            http://xorg.freedesktop.org/
Source0:        http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xmuu)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xproto) >= 7.0.17
Requires:       cpp
# This was part of the xorg-x11 package up to version 7.6
Conflicts:      xorg-x11 <= 7.6
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Xrdb is used to get or set the contents of the RESOURCE_MANAGER property
on the root window of screen 0, or the SCREEN_RESOURCES property on the
root window of any or all screens, or everything combined.

%prep
%setup -q

%build
# Run cpp with "-x assembler-with-cpp" in order to get rid of
# warnings when parsing valid comments (bsc#1120004)
%configure --with-cpp="%{_bindir}/cpp -x assembler-with-cpp, /lib/cpp"
make %{?_smp_mflags}

%install
%make_install

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING README.md
%{_bindir}/xrdb
%{_mandir}/man1/xrdb.1%{?ext_man}

%changelog
