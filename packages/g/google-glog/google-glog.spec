#
# spec file for package google-glog
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           google-glog
Version:        0.3.5
Release:        0
Summary:        Logging library for C++
License:        BSD-3-Clause
Group:          System/Libraries
Url:            https://github.com/google/glog
Source:         glog-%{version}.zip
BuildRequires:  gcc-c++
BuildRequires:  pkg-config
BuildRequires:  unzip
BuildRequires:  cmake
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

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
%configure
make %{?_smp_mflags}

%install
make %{?_smp_mflags} DESTDIR=%{buildroot} install
rm -rf %{buildroot}%{_libdir}/*.{a,la}
rm -rf %{buildroot}%{_datadir}/doc/glog-*

%post -n libglog0 -p /sbin/ldconfig
%postun -n libglog0 -p /sbin/ldconfig

%files -n libglog0
%defattr(-,root,root)
%doc COPYING
%{_libdir}/libglog.so.0
%{_libdir}/libglog.so.0.0.0

%files -n glog-devel
%defattr(-,root,root)
%doc COPYING AUTHORS ChangeLog README
%{_includedir}/glog/
%{_libdir}/libglog.so
%{_libdir}/pkgconfig/libglog.pc

%changelog
