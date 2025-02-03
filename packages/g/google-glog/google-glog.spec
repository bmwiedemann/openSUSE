#
# spec file for package google-glog
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2024 Andreas Stieger <Andreas.Stieger@gmx.de>
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
Name:           google-glog
Version:        0.7.1
Release:        0
Summary:        Logging library for C++
License:        BSD-3-Clause
Group:          System/Libraries
URL:            https://github.com/google/glog
Source:         https://github.com/google/glog/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  c++_compiler
BuildRequires:  cmake >= 3.22
BuildRequires:  pkgconfig

%description
The glog library implements application-level logging.
This library provides logging APIs based on C++-style
streams and various helper macros.

%package -n libglog%{sover}
Summary:        Logging library for C++
Group:          System/Libraries

%description -n libglog%{sover}
The glog library implements application-level logging.
This library provides logging APIs based on C++-style
streams and various helper macros.

%package -n glog-devel
Summary:        Header files for libglog%{sover}
Group:          Development/Libraries/C and C++
Requires:       libglog%{sover} = %{version}

%description -n glog-devel
The glog library implements application-level logging.
This library provides logging APIs based on C++-style
streams and various helper macros.

This package provides development files for libglog%{sover}.

%prep
%autosetup -p1 -n glog-%{version}

%build
%cmake \
	-DWITH_PKGCONFIG:BOOL=ON \
	-DWITH_GFLAGS:BOOL=OFF \
	-DWITH_GTEST:BOOL=OFF \
	%{nil}
%cmake_build

%install
%cmake_install
rm -rf %{buildroot}%{_datadir}/doc/glog-*

%ldconfig_scriptlets -n libglog%{sover}

%files -n libglog%{sover}
%license COPYING
%{_libdir}/libglog.so.%{sover}
%{_libdir}/libglog.so.%{version}

%files -n glog-devel
%license COPYING
%doc AUTHORS ChangeLog README.rst
%{_includedir}/glog/
%{_libdir}/libglog.so
%{_libdir}/pkgconfig/libglog.pc
%{_libdir}/cmake/glog

%changelog
