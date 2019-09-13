#
# spec file for package wordcut
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


Name:           wordcut
BuildRequires:  libtool
BuildRequires:  pkgconfig
Version:        0.5.1b2
Release:        0
Provides:       locale(th)
Url:            http://thaiwordseg.sourceforge.net/
Source0:        http://downloads.sourceforge.net/project/thaiwordseg/wordcut/wordcut-%{version}/wordcut-%{version}.tar.bz2
Patch0:         bugzilla-152315-locale-variable-used-before-set.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Summary:        Thai word segmentation utility.
License:        BSD-3-Clause
Group:          System/Libraries

%description
Thai word segmentation utility.

%package devel
Summary:        Include Files and Libraries mandatory for Development.
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version} glibc-devel

%description devel
This package contains all necessary include files and libraries needed
to develop applications that require these.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1

%build
autoreconf --force --install --verbose
export CFLAGS="$RPM_OPT_FLAGS" 
export CXXFLAGS="$RPM_OPT_FLAGS"
%configure --disable-static --with-pic
make %{_smp_mflags}

%install
make DESTDIR=${RPM_BUILD_ROOT} install

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-, root, root)
%doc AUTHORS COPYING NEWS README ChangeLog
%{_bindir}/*
%{_libdir}/libwordcut.so.*
%dir %{_datadir}/wordcut/
%{_datadir}/wordcut/*

%files devel
%defattr(-, root, root)
/usr/include/*
%{_libdir}/libwordcut.so
%{_libdir}/pkgconfig/*
%exclude %{_libdir}/*.la

%changelog
