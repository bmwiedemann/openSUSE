#
# spec file for package fmt
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


%define sover   7
Name:           fmt
Version:        7.1.0
Release:        0
Summary:        A formatting library for C++
License:        MIT
URL:            http://fmtlib.net/
Source0:        https://github.com/fmtlib/fmt/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
# PATCH-FIX-UPSTREAM fmt-7.1.0-LTO.patch
Patch0:         fmt-7.1.0-LTO.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig

%description
Fmt is a formatting library for C++. It can be used as an
alternative to (s)printf and IOStreams.

%package -n libfmt%{sover}
Summary:        A formatting library for C++

%description -n libfmt%{sover}
Shared library for fmt, a formatting library for C++.

%package devel
Summary:        Development files for fmt, a formatting library
Requires:       libfmt%{sover} = %{version}

%description devel
Development files for fmt, a formatting library for C++.

%prep
%autosetup -p1

%build
%cmake -DCMAKE_INSTALL_INCLUDEDIR:PATH=%{_includedir}
%make_jobs

%install
%cmake_install

%check
# path needs to be exported otherwise unit tests will fail
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:%{buildroot}%{_libdir}
%ctest

%post -n libfmt%{sover} -p /sbin/ldconfig
%postun -n libfmt%{sover} -p /sbin/ldconfig

%files -n libfmt%{sover}
%license LICENSE.rst
%{_libdir}/libfmt.so.%{sover}*

%files devel
%doc ChangeLog.rst README.rst
%{_includedir}/%{name}
%{_libdir}/cmake/%{name}
%{_libdir}/libfmt.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
