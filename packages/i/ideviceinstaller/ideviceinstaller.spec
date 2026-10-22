#
# spec file for package ideviceinstaller
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           ideviceinstaller
Version:        1.2.0
Release:        0
Summary:        Manage apps of iOS devices
License:        GPL-2.0-or-later
URL:            https://libimobiledevice.org/
Source:         https://github.com/libimobiledevice/ideviceinstaller/releases/download/%{version}/%{name}-%{version}.tar.bz2
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libimobiledevice-1.0) >= 1.3.0
BuildRequires:  pkgconfig(libplist-2.0) >= 2.3.0
BuildRequires:  pkgconfig(libzip) >= 0.10

%description
The ideviceinstaller application allows interacting with the app
installation service of an iOS device.

%prep
%autosetup -p1

%build
%configure --disable-static
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%files
%license COPYING
%doc AUTHORS NEWS README.md
%{_bindir}/ideviceinstaller
%{_mandir}/man1/ideviceinstaller.1%{?ext_man}

%changelog
