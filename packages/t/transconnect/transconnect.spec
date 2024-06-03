#
# spec file for package transconnect
#
# Copyright (c) 2024 SUSE LLC
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


Name:           transconnect
Version:        1.2
Release:        0
Summary:        Allows you to access the internet through a HTTP proxy
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Web/Proxy
URL:            http://transconnect.sourceforge.net/
Source0:        http://prdownloads.sourceforge.net/transconnect/%{name}-%{version}.tar.bz2
Source1:        README.SUSE
Patch0:         %{name}-%{version}.dif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
TransConnect is a program to allow you almost complete access to the
internet through a HTTP proxy like squid.

%prep
%autosetup -p0
cp %{SOURCE1} .

%build
make

%install
install -D -m 755 tconn.so %{buildroot}%{_libdir}/tconn.so

%files
%defattr(-,root,root)
%{_libdir}/tconn.so
%doc AUTHORS Changelog COPYING README README.SUSE tconn.conf

%changelog
