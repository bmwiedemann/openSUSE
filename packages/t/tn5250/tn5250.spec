#
# spec file for package tn5250
#
# Copyright (c) 2022 SUSE LLC
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
Version:        0.16.5
Release:        0
Summary:        5250 Emulator
License:        LGPL-2.1-or-later
Group:          Productivity/Networking/Other
URL:            http://tn5250.sourceforge.net/
Source:         https://sourceforge.net/projects/tn5250/files/tn5250/0.16.5/tn5250-0.16.5.tar.gz
Source1:        README.SUSE
Patch:          tn5250-0.16.2-terminfo.dif
Patch1:         tn5250-0.16.5-strings.patch
Patch2:         tn5250-0.16.5-no-build-date.patch
BuildRequires:  gcc-c++
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
Provides:       tn5250:/usr/include/tn5250/tn5250d.h
Requires:       lib5250-0 = %{version}

%description devel
Header files for use with the tn5250 library.

%prep
%setup
%patch -p1
%patch1
%patch2
cp -p %{SOURCE1} .

%build
DIR=$(find . -name configure -printf "%h\n")
%{?suse_update_config:%{suse_update_config -f $DIR }}
autoreconf -f -i
%configure --disable-static
%make_build

%install
mkdir -p "%{buildroot}/%{_bindir}"
%make_install
rm -f %{buildroot}%{_libdir}/*.la

%post   -n lib5250-0 -p /sbin/ldconfig
%postun -n lib5250-0 -p /sbin/ldconfig

%files
%doc BUGS COPYING README AUTHORS BUGS ChangeLog NEWS TODO XTerm README.SUSE
/usr/bin/*
%{_mandir}/man1/*
%{_mandir}/man5/*
/usr/share/tn5250

%files -n lib5250-0
%{_libdir}/lib5250.so.0
%{_libdir}/lib5250.so.0.0.0

%files devel
/usr/include/tn5250.h
/usr/include/tn5250
%{_libdir}/lib5250.so
/usr/share/aclocal/tn5250.m4

%changelog
