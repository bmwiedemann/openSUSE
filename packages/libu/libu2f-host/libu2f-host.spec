#
# spec file for package libu2f-host
#
# Copyright (c) 2020 SUSE LLC
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


%define sover  0
Name:           libu2f-host
Version:        1.1.10
Release:        0
Summary:        Yubico Universal 2nd Factor (U2F) Host C Library
License:        LGPL-2.1-or-later
Group:          Productivity/Networking/Security
URL:            https://developers.yubico.com/
Source0:        https://developers.yubico.com/libu2f-host/Releases/%{name}-%{version}.tar.xz
Source1:        https://developers.yubico.com/libu2f-host/Releases/%{name}-%{version}.tar.xz.sig
Patch0:         json-c-update.patch
BuildRequires:  libhidapi-devel
BuildRequires:  libtool
BuildRequires:  libzip
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(json-c) >= 0.10
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(udev)

%description
libu2f-host provide a command-line tool that implements
the host-side of the U2F protocol. There are APIs to talk to a U2F
device and perform the U2F Register and U2F Authenticate operations.

%package     -n %{name}%{sover}
Summary:        Library for Universal 2nd Factor (U2F)
Group:          Productivity/Networking/Security

%description -n %{name}%{sover}
Libu2f-host provide a C library that implements
the host-side of the U2F protocol.  There are APIs to talk to a U2F
device and perform the U2F Register and U2F Authenticate operations.

%package     -n %{name}-devel
Summary:        Development files for Universal 2nd Factor (U2F)
Group:          Development/Libraries/C and C++
Requires:       %{name}%{sover} = %{version}

%description -n %{name}-devel
This package contains the header file needed to develop applications that
use Universal 2nd Factor (U2F).

%package     -n u2f-host
Summary:        Tool to support Yubico's Universal 2nd Factor (U2F)
Group:          Productivity/Networking/Security
Requires:       %{name}%{sover} = %{version}

%description -n u2f-host
Command line tool that implements the host side of the Universal 2nd Factor (U2F) protocol.

%package        doc
Summary:        Documentation for the U2F protocol
Group:          Productivity/Networking/Security

%description    doc
Documentation files for the host side of the U2F protocol.

%prep
%autosetup -p1

%build
%configure --disable-static --with-openssl --with-udevrulesdir=%{_udevrulesdir}
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} INSTALL="install -p"
find %{buildroot} -type f -name "*.la" -delete -print

%post
%{?udev_rules_update:%udev_rules_update}

%post   -n %{name}%{sover} -p /sbin/ldconfig
%postun -n %{name}%{sover} -p /sbin/ldconfig

%files -n u2f-host
%doc AUTHORS NEWS ChangeLog README
%license COPYING
%{_bindir}/u2f-host
%{_mandir}/man1/u2f-host.1%{?ext_man}
%dir %{_prefix}/lib/udev
%dir %{_udevrulesdir}
%{_udevrulesdir}/*-u2f.rules

%files doc
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/u2f-host/

%files -n %{name}%{sover}
%{_libdir}/%{name}.so.%{sover}
%{_libdir}/%{name}.so.%{sover}.1.10

%files -n %{name}-devel
%{_includedir}/u2f-host/
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/*

%changelog
