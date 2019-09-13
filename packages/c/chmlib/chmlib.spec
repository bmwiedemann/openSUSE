#
# spec file for package chmlib
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define lname	libchm0
Name:           chmlib
Version:        0.40
Release:        0
Summary:        A library for dealing with ITSS/CHM files
License:        LGPL-2.1+
Group:          System/Libraries
Url:            http://www.jedrea.com/chmlib/
Source0:        http://www.jedrea.com/chmlib/%{name}-%{version}.tar.bz2
Source2:        baselibs.conf
Patch0:         %{name}-0.39.diff
BuildRequires:  gcc-c++
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
CHMLIB is a library for dealing with Microsoft ITSS/CHM format files.

%package -n %{lname}
Summary:        A library for dealing with ITSS/CHM files
Group:          System/Libraries
Obsoletes:      chmlib < %{version}-%{release}
Provides:       chmlib = %{version}-%{release}

%description -n %{lname}
CHMLIB is a library for dealing with Microsoft ITSS/CHM format files.

%package      devel
Summary:        Documentation and Headers for chmlib
Group:          System/Libraries
Requires:       %{lname} = %{version}

%description	devel
This package contains the headers and documentation for the chmlib API
that programmers will need to develop applications which use chmlib,
the software library for dealing with Microsoft ITSS/CHM format files.

%package        examples
Summary:        Example applications for chmlib
Group:          System/Libraries
Requires:       %{lname} = %{version}

%description	examples
This package contains examples built on chmlib which may be useful
to convert chm files from command line.

%prep
%setup -q
%patch0

%build
export CFLAGS="%{optflags} -fstack-protector"
export CXXFLAGS="$CFLAGS"
export CXXCPP="g++ -E"
%configure \
	--disable-static \
	--with-pic \
	--disable-pread \
	--enable-examples
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{lname} -p /sbin/ldconfig

%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%defattr(-, root, root)
%doc AUTHORS COPYING NEWS README
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root)
%{_includedir}/chm_lib.h
%{_includedir}/lzx.h
%{_libdir}/*.so

%files examples
%defattr(-, root, root)
%{_bindir}/*

%changelog
