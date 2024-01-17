#
# spec file for package google-glog
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


%{!?make_build:%global make_build make %{?_smp_mflags}}
Name:           google-glog
Version:        0.5.0
Release:        0
Summary:        Logging library for C++
License:        BSD-3-Clause
Group:          System/Libraries
URL:            https://github.com/google/glog
Source:         https://github.com/google/glog/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig

%description
The glog library implements application-level logging.
This library provides logging APIs based on C++-style
streams and various helper macros.

%package -n libglog0
Summary:        Logging library for C++
Group:          System/Libraries

%description -n libglog0
The glog library implements application-level logging.
This library provides logging APIs based on C++-style
streams and various helper macros.

%package -n glog-devel
Summary:        Header files for libglog0
Group:          Development/Libraries/C and C++
Requires:       libglog0 = %{version}

%description -n glog-devel
The glog library implements application-level logging.
This library provides logging APIs based on C++-style
streams and various helper macros.

This package provides development files for libglog0.

%prep
%setup -q -n glog-%{version}

%build
%cmake -DCMAKE_INSTALL_LIBDIR:PATH=%{_lib}
%make_build

%install
%cmake_install
rm -rf %{buildroot}%{_libdir}/*.{a,la}
rm -rf %{buildroot}%{_datadir}/doc/glog-*

%post -n libglog0 -p /sbin/ldconfig
%postun -n libglog0 -p /sbin/ldconfig

%files -n libglog0
%license COPYING
%{_libdir}/libglog.so.0
%{_libdir}/libglog.so.0.5.0

%files -n glog-devel
%license COPYING
%doc AUTHORS ChangeLog README.rst
%{_includedir}/glog/
%{_libdir}/libglog.so
%{_libdir}/pkgconfig/libglog.pc
%{_libdir}/cmake/glog

%changelog
