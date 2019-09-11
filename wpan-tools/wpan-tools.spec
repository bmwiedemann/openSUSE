#
# spec file for package wpan-tools
#
# Copyright (c) 2016 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           wpan-tools
Summary:        Utilities to manage the Linux 802.15.4 WPAN stack
Version:        0.8
Release:        0
License:        ISC
Group:          Hardware/Wifi
Url:            https://github.com/linux-wpan/wpan-tools
Source:         https://github.com/linux-wpan/wpan-tools/releases/download/%name-%version/%name-%version.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  help2man
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libnl-3.0) >= 3.1
BuildRequires:  pkgconfig(libnl-genl-3.0) >= 3.1

%description
This is a set of utils to manage the Linux WPAN stack,
compatible with IEEE 802.15.4-2003 (and to a lesser extent,
2006).

%prep
%setup -q

%build
%configure
make %{?_smp_mflags} V=1

%install
%make_install

%files
%defattr(-,root,root)
%_bindir/af*
%_bindir/iwpan
%_bindir/wpan-ping
%license COPYING

%changelog
