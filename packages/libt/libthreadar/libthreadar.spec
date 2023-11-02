#
# spec file for package libthreadar
#
# Copyright (c) 2023 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%define sover 1000
Name:           libthreadar
Version:        1.4.0
Release:        0
Summary:        C++ library proposing a set of high level classes for threads management
License:        LGPL-3.0-or-later
URL:            https://github.com/Edrusb/libthreadar
Source:         https://downloads.sourceforge.net/project/libthreadar/%{version}/%{name}-%{version}.tar.gz
Source2:        https://dar.edrusb.org/libthreadar/Releases/%{name}-%{version}.tar.gz.sig
# http://dar.linux.free.fr/doc/authentification.html
Source3:        http://dar.linux.free.fr/doc/dar_key.txt#/%{name}.keyring
BuildRequires:  c++_compiler
BuildRequires:  pkgconfig

%description
libthreadar provides C++ classes for manipulating threads and
propagating back exception from thread to parent thread when the
parent calls the join() method

%package -n %{name}%{sover}
Summary:        C++ library containing a set of high level classes for threads management

%description -n %{name}%{sover}
libthreadar is a C++ library containing a set of high level classes for threads management.

This package contains the shared library

%package devel
Summary:        Development files for libthreadar
Requires:       %{name}%{sover} = %{version}

%description devel
libthreadar is a C++ library containing a set of high level classes for threads management.

This package contains the files needed to build using libthreadar.

%prep
%autosetup

%build
%configure
%make_build

%install
%make_install
find %{buildroot}%{_libdir} -type f -name "*.a" -delete -print
find %{buildroot} -type f -name "*.la" -delete -print
rm %{buildroot}%{_datadir}/libthreadar/README

%ldconfig_scriptlets -n %{name}%{sover}

%files -n %{name}%{sover}
%license COPYING COPYING.LESSER
%{_libdir}/libthreadar.so.%{sover}
%{_libdir}/libthreadar.so.%{sover}.*

%files devel
%license COPYING COPYING.LESSER
%doc AUTHORS ChangeLog NEWS README
%{_includedir}/libthreadar
%{_libdir}/*.so
%{_libdir}/pkgconfig/libthreadar.pc

%changelog
