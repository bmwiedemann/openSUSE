#
# spec file for package clthreads
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


%define sover   2
%define libname lib%{name}%{sover}
Name:           clthreads
Version:        2.4.2
Release:        0
Summary:        C++ wrapper library around the POSIX threads API
License:        LGPL-2.1-or-later
Group:          System/Libraries
URL:            https://kokkinizita.linuxaudio.org/linuxaudio/
Source:         https://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.bz2
Patch0:         fix-build.patch
BuildRequires:  gcc-c++

%description
C++ wrapper library around the POSIX threads API.

%package -n %{libname}
Summary:        C++ wrapper library around the POSIX threads API
Group:          System/Libraries

%description -n %{libname}
C++ wrapper library around the POSIX threads API.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
Development files for %{name} including headers and libraries.

%prep
%setup -q
%patch0 -p1

%build
export CXXFLAGS="%{optflags}"
%make_build -C source

%install
make -C source DESTDIR=%{buildroot} PREFIX=%{_prefix} LIBDIR=%{_libdir} install

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license COPYING
%doc AUTHORS
%{_libdir}/libclthreads.so.%{sover}*

%files devel
%{_includedir}/clthreads.h
%{_libdir}/libclthreads.so

%changelog
