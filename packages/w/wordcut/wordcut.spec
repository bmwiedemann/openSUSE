#
# spec file for package wordcut
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


%define lname   libwordcut0
Name:           wordcut
Version:        0.5.1b2
Release:        0
Summary:        Thai word segmentation utility
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            http://thaiwordseg.sourceforge.net/
Source0:        http://downloads.sourceforge.net/project/thaiwordseg/wordcut/wordcut-%{version}/wordcut-%{version}.tar.bz2
Patch0:         bugzilla-152315-locale-variable-used-before-set.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  libtool
BuildRequires:  pkgconfig
Provides:       locale(th)

%description
Thai word segmentation utility.

%package -n %{lname}
Summary:        Thai word segmentation utility
Group:          System/Libraries

%description -n %{lname}
Thai word segmentation utility.

%package devel
Summary:        Header files for wordcut, a Thai word segmentation utility
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}
Requires:       glibc-devel

%description devel
This package contains files necessary to build against libwordcut.

%prep
%autosetup -p1

%build
autoreconf --force --install --verbose
%configure --disable-static
%make_build

%install
%make_install

%post   -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files
%license COPYING
%{_bindir}/*
%dir %{_datadir}/wordcut/
%{_datadir}/wordcut/*

%files -n %{lname}
%{_libdir}/libwordcut.so.*

%files devel
%{_includedir}/*
%{_libdir}/libwordcut.so
%{_libdir}/pkgconfig/*
%exclude %{_libdir}/*.la

%changelog
