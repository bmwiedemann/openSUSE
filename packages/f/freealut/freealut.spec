#
# spec file for package freealut
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define sover   0
%define lname   libalut%{sover}
Name:           freealut
Version:        1.1.0
Release:        0
Summary:        freealut is a free implementation of OpenAL's ALUT standard
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Url:            http://connect.creativelabs.com/openal/default.aspx
Source:         %{name}-%{version}.tar.bz2
Source2:        baselibs.conf
BuildRequires:  cmake
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(openal)

%description
freealut is a free implementation of OpenAL's ALUT standard.

%package -n %{lname}
Summary:        freealut is a free implementation of OpenAL's ALUT standard
Group:          System/Libraries

%description -n %{lname}
freealut is a free implementation of OpenAL's ALUT standard.

%package devel
Summary:        Static libraries, header files and tests for openal library
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}
Requires:       glibc-devel

%description devel
OpenAL is an audio library designed in the spirit of OpenGL - machine
independent, cross platform, and data format neutral, with a clean,
simple C-based API.

%prep
%setup -q

%build
%cmake \
  -DBUILD_STATIC=OFF \
  -DWARNINGS=OFF \
  -DOPTIMIZATION=OFF \
  -Wno-dev
%make_jobs

%install
%cmake_install
# FIXME: should be fixed upstream
%if %__isa_bits == 64
mv %{buildroot}/usr/lib/ %{buildroot}/%{_libdir}
%endif

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%doc AUTHORS COPYING ChangeLog NEWS README
%{_libdir}/libalut.so.%{sover}*

%files devel
%{_bindir}/*-config
%{_includedir}/AL
%{_libdir}/libalut.so
%{_libdir}/pkgconfig/*.pc

%changelog
