#
# spec file for package clxclient
#
# Copyright (c) 2020, Martin Hauke <mardnh@gmx.de>
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


%define sover   3
%define libname lib%{name}%{sover}
Name:           clxclient
Version:        3.9.2
Release:        0
Summary:        C++ wrapper library around the X Window System API
License:        LGPL-2.1-or-later
Group:          System/Libraries
URL:            https://kokkinizita.linuxaudio.org/linuxaudio/
Source:         https://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.bz2
Patch0:         fix-build.patch
BuildRequires:  clthreads-devel
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xproto)

%description
C++ wrapper library around the X Window System API.

%package -n %{libname}
Summary:        C++ wrapper library around the X Window System API
Group:          System/Libraries

%description -n %{libname}
C++ wrapper library around the X Window System API.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Requires:       clthreads-devel
Requires:       pkgconfig(freetype2)
Requires:       pkgconfig(x11)
Requires:       pkgconfig(xft)
Requires:       pkgconfig(xproto)

%description devel
Development files for %{name} including headers and libraries.

%prep
%setup -q
%patch0 -p1

%build
export CXXFLAGS="%{optflags}"
%make_build -C source

%install
make -C source DESTDIR=%{buildroot} PREFIX=%{_prefix} install

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license COPYING
%doc AUTHORS
%{_libdir}/libclxclient.so.%{sover}*

%files devel
%{_includedir}/clxclient.h
%{_libdir}/libclxclient.so

%changelog
