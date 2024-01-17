#
# spec file for package libXau
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


%define lname	libXau6
Name:           libXau
Version:        1.0.11
Release:        0
Summary:        X11 authorization protocol library
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://xorg.freedesktop.org/
#Git-Clone:	git://anongit.freedesktop.org/xorg/lib/libXau
#Git-Web:       http://cgit.freedesktop.org/xorg/lib/libXau/
Source:         http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.xz
Source1:        baselibs.conf
#git#BuildRequires:	autoconf >= 2.60, automake
BuildRequires:  fdupes
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xproto)

%description
libXau provides mechanisms for individual access to an X Window
System display. It uses existing core protocol and library hooks for
specifying authorization data in the connection setup block to
restrict use of the display to only those clients that show that they
know a server-specific key called a "magic cookie".

%package -n %{lname}
Summary:        X11 authorization protocol library
# O/P added for 12.2
Group:          System/Libraries
Provides:       xorg-x11-libXau = 7.6_%{version}-%{release}
Obsoletes:      xorg-x11-libXau < 7.6_%{version}-%{release}

%description -n %{lname}
libXau provides mechanisms for individual access to an X Window
System display. It uses existing core protocol and library hooks for
specifying authorization data in the connection setup block to
restrict use of the display to only those clients that show that they
know a server-specific key called a "magic cookie".

%package devel
Summary:        Development files for the X11 authorization protocol library
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}
# O/P added for 12.2
Provides:       xorg-x11-libXau-devel = 7.6_%{version}-%{release}
Obsoletes:      xorg-x11-libXau-devel < 7.6_%{version}-%{release}

%description devel
libXau provides mechanisms for individual access to an X Window
System display. It uses existing core protocol and library hooks for
specifying authorization data in the connection setup block to
restrict use of the display to only those clients that show that they
know a server-specific key called a "magic cookie".

This package contains the development headers for the library found
in %{lname}.

%prep
%setup -q

%build
%configure --disable-static
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%fdupes %{buildroot}/%{_prefix}

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%license COPYING
%{_libdir}/libXau.so.6*

%files devel
%{_includedir}/X11/*
%{_libdir}/libXau.so
%{_libdir}/pkgconfig/xau.pc
%{_mandir}/man3/*

%changelog
