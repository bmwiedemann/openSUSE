#
# spec file for package omniORB
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2012-2017 Lars Vogdt
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


%define libname libomniORB4-3
%define libname_omnithread libomnithread4

Name:           omniORB
Summary:        A robust high performance CORBA ORB for C++ and Python
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/Libraries
Version:        4.3.2
Release:        0
URL:            https://omniorb.sourceforge.io
Source0:        https://downloads.sourceforge.net/project/omniorb/%{name}/%{name}-%{version}/%{name}-%{version}.tar.bz2
Source1:        omniORB-rpmlintrc
BuildRequires:  gcc-c++
BuildRequires:  openssl-devel
BuildRequires:  pkg-config
BuildRequires:  python-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  zlib-devel

%description
omniORB is a robust high performance CORBA ORB for C++ and Python.

It adheres to version 2.6 of the CORBA specification and is fully
interoperable with other CORBA ORBs.

%package devel
Group:          Development/Libraries/C and C++
Summary:        Development libraries, header files and utilities for omniORB
Requires:       %{libname_omnithread} = %{version}
Requires:       %{libname} = %{version}
Requires:       %{name} = %{version}

%description devel
omniORB-devel contains the omniORB development files. These
files are needed to develop applications based on omniORB.

%package -n %{libname}
Group:          System/Libraries
Summary:        omniORB libraries
Conflicts:      libomniORB4 <= 4.3.0

%description -n %{libname}
Shared libraries providing the omniORB CORBA implementation.

%package -n %{libname_omnithread}
Group:          System/Libraries
Summary:        omniORB thread library
Conflicts:      libomniORB4 <= 4.3.0

%description -n %{libname_omnithread}
Thread support library for omniORB.

%prep
%setup -q
find . -iname \*\.py -exec sed -ie '1 s@env python@python3@' '{}' \;

%build
%configure --disable-static \
           --with-omniNames-logdir=%{_var}/log/omninames

%make_build

%install
%make_install
mkdir -p %{buildroot}%{_var}/log/omninames
chmod +x %{buildroot}%{python3_sitelib}/omniidl/main.py
chmod +x %{buildroot}%{_libdir}/lib*.so.*

%post -n %{libname} -p /sbin/ldconfig
%post -n %{libname_omnithread} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig
%postun -n %{libname_omnithread} -p /sbin/ldconfig

%files -n %{libname}
%{_libdir}/lib*.so.*
%exclude %{_libdir}/libomnithread.so.*

%files -n %{libname_omnithread}
%{_libdir}/libomnithread.so.*

%files
%license COPYING*
%doc CREDITS README* ReleaseNotes* src/examples/ziop/README.txt
%doc doc/*
%dir %{_datadir}/idl
%dir %{_datadir}/idl/%{name}
%dir %{_datadir}/idl/%{name}/COS
%dir %{_var}/log/omninames
%dir %{python3_sitelib}/omniidl
%dir %{python3_sitelib}/omniidl_be
%{_bindir}/*
%{python3_sitearch}/_omniidl*
%{python3_sitelib}/omniidl/*
%{python3_sitelib}/omniidl_be/*
%{_datadir}/idl/%{name}/*.idl
%{_datadir}/idl/%{name}/COS/*.idl

%files devel
%license COPYING*
%doc CREDITS README* ReleaseNotes*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*

%changelog
