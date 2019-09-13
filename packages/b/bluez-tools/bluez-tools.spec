#
# spec file for package bluez-tools
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           bluez-tools
Version:        0.1.38+git20161212
Release:        0
Summary:        A set of tools to manage bluetooth devices
License:        GPL-2.0+
Group:          Hardware/Mobile
Url:            https://github.com/khvzak/bluez-tools
Source:         %{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
BuildRequires:  pkgconfig(gio-2.0) >= 2.26.0
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.26.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.36.0
Requires:       bluez

%description
bluez-tools is a project to implement the better command line tools
for BlueZ. The project is implemented in C and uses the D-Bus
interface of BlueZ.

%prep
%setup -q

%build
autoreconf -fi
%configure
make %{?_smp_mflags} V=1

%install
%make_install

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING README
%{_bindir}/bt-*
%{_mandir}/man1/bt-*.1%{?ext_man}

%changelog
