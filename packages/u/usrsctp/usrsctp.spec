#
# spec file for package usrsctp
#
# Copyright (c) 2021 SUSE LLC
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


%define sover 2
%define _lto_cflags %{nil}

Name:           usrsctp
Version:        0.9.5.0
Release:        0
Summary:        Userland SCTP implementation
License:        BSD-3-Clause
Group:          Productivity/Networking/Other
URL:            https://github.com/sctplab/usrsctp/
Source:         https://github.com/sctplab/usrsctp/archive/%{version}.tar.gz
# for run bootstrap
BuildRequires:  automake
BuildRequires:  libtool

%description
This is the reference implementation for userland SCTP.

%package -n lib%{name}%{sover}
Summary:        Usrsctp Library
Group:          System/Libraries

%description -n lib%{name}%{sover}
The libraries for usersctp.

%package devel
Summary:        Usersctp Development Kit 
Group:          Development/Libraries/C and C++
Requires:       lib%{name}%{sover} = %{version}

%description devel
The development files for usersctp.

%prep
%autosetup -p1

%build
./bootstrap
%configure --disable-debug --disable-warnings-as-errors --disable-static
%make_build

%install
%make_install
# remove .la files
rm -f %{buildroot}%{_libdir}/lib*.la

%post -n lib%{name}%{sover} -p /sbin/ldconfig

%postun -n lib%{name}%{sover} -p /sbin/ldconfig

%files -n lib%{name}%{sover}
%license LICENSE.md
%{_libdir}/*.so.*

%files devel
%{_includedir}/*.h
%{_libdir}/*.so

%changelog
