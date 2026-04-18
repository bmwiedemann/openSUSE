#
# spec file for package tn5250
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


Name:           tn5250
Version:        0.18.0
Release:        0
Summary:        5250 Emulator
License:        LGPL-2.1-or-later
Group:          Productivity/Networking/Other
URL:            https://tn5250.sourceforge.net/
Source:         https://sourceforge.net/projects/tn5250/files/tn5250/v%{version}/tn5250-%{version}.tar.gz
Source1:        README.SUSE
Patch0:         tn5250-0.16.2-terminfo.dif
Patch1:         tn5250-0.16.5-no-build-date.patch
BuildRequires:  gcc-c++
BuildRequires:  libopenssl-devel
BuildRequires:  libtool
BuildRequires:  ncurses-devel

%description
The 5250 is most commonly used for connecting to IBM's AS/400.	While
one can connect to an AS/400 with a VT100 emulator, it is not ideal.
The problem is that the 5250 is a screen at a time terminal, whereas
the VT100 is a character at a time device.  The emulator uses telnet's
binary mode to transfer the 5250 data stream.

%package -n lib5250-0
Summary:        Component library of the tn5250 emulator
Group:          System/Libraries

%description -n lib5250-0
Component library of the tn5250 emulator.

%package devel
Summary:        Header files for the 5250 Emulator
Group:          Productivity/Networking/Other
Requires:       lib5250-0 = %{version}
Provides:       tn5250:%{_includedir}/tn5250/tn5250d.h

%description devel
Header files for use with the tn5250 library.

%prep
%autosetup -p1
cp -p %{SOURCE1} .

%build
autoreconf -f -i
%configure --disable-static
%make_build

%install
mkdir -p "%{buildroot}/%{_bindir}"
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post   -n lib5250-0 -p /sbin/ldconfig
%postun -n lib5250-0 -p /sbin/ldconfig

%files
%license COPYING
%doc README.md ChangeLog XTerm README.SUSE
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_datadir}/tn5250

%files -n lib5250-0
%{_libdir}/lib5250.so.0
%{_libdir}/lib5250.so.0.0.0

%files devel
%{_includedir}/tn5250.h
%{_includedir}/tn5250
%{_libdir}/lib5250.so
%{_libdir}/pkgconfig/tn5250.pc

%changelog
