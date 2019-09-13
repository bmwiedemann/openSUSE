#
# spec file for package libbitmask
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Url:            http://oss.sgi.com/projects/cpusets/

Name:           libbitmask
Summary:        Multi-word bitmask abstract data type (used by cpusets)
License:        LGPL-2.1+
Group:          Development/Languages/C and C++
Version:        2.0
Release:        0
Source:         libbitmask-%{version}.tar.bz2
BuildRequires:  libtool
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The Cpuset System is a processor and memory placement mechanism that
The libbitmask package provides an abstract data type for arbitrary
length bit masks, with a variety of operators.	The cpuset package
depends on libbitmask.

%package -n libbitmask1
Summary:        Multi-word bitmask abstract data type (used by cpusets)
Group:          Development/Languages/C and C++

%description -n libbitmask1
The Cpuset System is a processor and memory placement mechanism that
The libbitmask package provides an abstract data type for arbitrary
length bit masks, with a variety of operators.	The cpuset package
depends on libbitmask.

%package -n libbitmask-devel
Summary:        Multi-word bitmask abstract data type (used by cpusets)
Group:          Development/Languages/C and C++
Requires:       libbitmask1 = %{version}

%description -n libbitmask-devel
The Cpuset System is a processor and memory placement mechanism that
The libbitmask package provides an abstract data type for arbitrary
length bit masks, with a variety of operators.	The cpuset package
depends on libbitmask.

%prep
%setup -q -n %{name}

%build
autoreconf -i
%configure --disable-static --with-pic
make %{?_smp_mflags}

%install
%makeinstall
rm -f $RPM_BUILD_ROOT/%{_libdir}/*.la

%post -n libbitmask1 -p /sbin/ldconfig

%postun -n libbitmask1 -p /sbin/ldconfig

%files -n libbitmask1
%defattr(-,root,root)
%{_libdir}/lib*so.*

%files -n libbitmask-devel
%defattr(-,root,root)
%doc %{_mandir}/man3/*
%{_includedir}/*
%{_libdir}/lib*so
%{_docdir}/libbitmask/libbitmask.*
%dir %{_docdir}/libbitmask

%changelog
