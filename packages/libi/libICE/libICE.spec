#
# spec file for package libICE
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


%define lname	libICE6
Name:           libICE
Version:        1.1.2
Release:        0
Summary:        X11 Inter-Client Exchange Library
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://xorg.freedesktop.org/
#Git-Clone:	git://anongit.freedesktop.org/xorg/lib/libICE
#Git-Web:	http://cgit.freedesktop.org/xorg/lib/libICE/
Source:         https://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.xz
Source1:        baselibs.conf
#git#BuildRequires:	autoconf >= 2.60, automake, libtool
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(xorg-macros) >= 1.12
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(xtrans)

%description
There are numerous possible inter-client protocols, with many
similarities and common needs - authentication, version negotiation,
byte order negotiation, and so on.
The Inter-Client Exchange (ICE) protocol is intended to provide a
framework for building such protocols, allowing them to make use of
common negotiation mechanisms and to be multiplexed over a single
transport connection.

%package -n %{lname}
Summary:        X11 Inter-Client Exchange Library
# O/P added for 12.2
Group:          System/Libraries
Provides:       xorg-x11-libICE = 7.6_%{version}-%{release}
Obsoletes:      xorg-x11-libICE < 7.6_%{version}-%{release}

%description -n %{lname}
The Inter-Client Exchange (ICE) protocol is intended to provide a
framework for building such protocols, allowing them to make use of
common negotiation mechanisms and to be multiplexed over a single
transport connection.

%package devel
Summary:        Development files for the X11 Inter-Client Exchange Library
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}
# O/P added for 12.2
Provides:       xorg-x11-libICE-devel = 7.6_%{version}-%{release}
Obsoletes:      xorg-x11-libICE-devel < 7.6_%{version}-%{release}

%description devel
The Inter-Client Exchange (ICE) protocol is intended to provide a
framework for building such protocols, allowing them to make use of
common negotiation mechanisms and to be multiplexed over a single
transport connection.

This package contains the development headers for the library found
in %{lname}.

%prep
%setup -q

%build
autoreconf -fi
%configure --docdir=%{_docdir}/%{name} --disable-static
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%license COPYING
%{_libdir}/libICE.so.6*

%files devel
%{_includedir}/X11/*
%{_libdir}/libICE.so
%{_libdir}/pkgconfig/ice.pc
%{_docdir}/%{name}

%changelog
