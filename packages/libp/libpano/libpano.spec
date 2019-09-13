#
# spec file for package libpano
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


%define _name libpano13

Name:           libpano
Version:        2.9.19
Release:        0
Summary:        Panorama Tools Back-End Library
License:        GPL-2.0+
Group:          Development/Libraries/C and C++
Url:            http://panotools.sourceforge.net/
Source:         %{_name}-%{version}.tar.bz2
# https://sourceforge.net/tracker/?func=detail&aid=2833227&group_id=96188&atid=613956
Patch0:         libpano-implicit-decl.patch
BuildRequires:  java-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  libtool
BuildRequires:  zlib-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Library and utilities for working with panoramas.

%package -n libpano13-3
Summary:        Panorama Tools Back-End Library
Group:          Development/Libraries/C and C++
Obsoletes:      %{name} < %{version}

%description -n libpano13-3
Library for working with panoramas.

%package utils
Summary:        Panorama Tools Utilities
Group:          Productivity/Graphics/Other
Obsoletes:      %{name} < %{version}
# Explicitly mentioned libpano (for <= 10.2) probably means libpano-utils:
Provides:       %{name} = %{version}

%description utils
Utilities for working with panoramas.

%package devel
Summary:        Panorama Tools Back-End Library - files mandatory for development
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libpano13-3 = %{version}

%description devel
Development files for library for working with panoramas.

%prep
%setup -q -n %{_name}-%{version}
%patch0

%build
autoreconf -f -i
%configure\
	--with-java=%{java_home}
make %{?_smp_mflags}

%install
%make_install
#Axe Libs.private from .pc files, which do not behave as expected
sed -i -e '/^Libs.private/d' %{buildroot}%{_libdir}/pkgconfig/libpano13.pc
find %{buildroot} -type f -name "*.la" -print -delete

%clean
rm -rf %{buildroot}

%post -n libpano13-3 -p /sbin/ldconfig

%postun -n libpano13-3 -p /sbin/ldconfig

%files -n libpano13-3
%defattr(-,root,root)
%doc README README.linux AUTHORS COPYING NEWS ChangeLog ChangeLog.hg doc/*.txt tools/README.PTmender
%{_libdir}/libpano13.so.*

%files utils
%defattr(-,root,root)
%{_bindir}/*
%doc %{_mandir}/man?/*.*

%files devel
%defattr(-,root,root)
%{_includedir}/pano13
%{_libdir}/libpano13.so
%{_libdir}/pkgconfig/libpano13.pc

%changelog
