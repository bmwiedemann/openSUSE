#
# spec file for package cppunit
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


%define libname libcppunit-1_15-1
Name:           cppunit
Version:        1.15.1
Release:        0
Summary:        C++ Port of the JUnit Testing Framework
License:        LGPL-2.1-or-later
URL:            https://www.freedesktop.org/wiki/Software/cppunit
Source:         http://dev-www.libreoffice.org/src/%{name}-%{version}.tar.gz
Source1:        cppunit-devel.desktop
Source99:       baselibs.conf
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files

%description
CppUnit is the C++ port of the famous JUnit framework for unit testing.
Test output is in XML for automatic testing and GUI based for
supervised tests.

%package -n %{libname}
Summary:        Cppunit library for writting C++ unittests

%description -n %{libname}
Cppunit library for writting C++ unittests in JUnit like fashion.

%package devel
Summary:        Include Files and Libraries for cppunit
Requires:       %{libname} = %{version}
Suggests:       devel-doc = %{version}
Provides:       libcppunit-devel = %{version}
Obsoletes:      libcppunit-devel < %{version}

%description devel
Cppunit library, headers, and all relevant additions for writting C++ unittests
in JUnit like fashion.

%package devel-doc
Summary:        Documentation for the cppunit API
Conflicts:      libcppunit-devel < 1.13.2
BuildArch:      noarch

%description devel-doc
This package contains documentation for the cppunit API.

%prep
%autosetup

%build
export CXXFLAGS="%{optflags}"
%configure \
    --docdir=%{_docdir}/%{name} \
    --disable-silent-rules \
    --disable-static \
    --enable-doxygen
%make_build

%install
%make_install
# remove la archive
find %{buildroot} -type f -name "*.la" -delete -print
# remove INSTALL* files from package docs
find %{buildroot}%{_docdir}/%{name}/ -type f -name "INSTALL*" -delete -print
# this got also installed to _defaultdocdir
rm -rf %{buildroot}%{_datadir}/cppunit/html/
find %{buildroot}%{_includedir} -type f | xargs chmod a-x
# install susehelp file
mkdir -p %{buildroot}%{_datadir}/susehelp/meta/Development/Libraries/
install %{SOURCE1} %{buildroot}%{_datadir}/susehelp/meta/Development/Libraries/
%suse_update_desktop_file %{buildroot}%{_datadir}/susehelp/meta/Development/Libraries/cppunit-devel.desktop

%check
%make_build check

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license COPYING
%doc AUTHORS
%{_libdir}/libcppunit*.so.*
%{_datadir}/cppunit

%files devel
%doc NEWS README THANKS ChangeLog
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/*
%{_bindir}/DllPlugInTester
%{_libdir}/libcppunit*.so
%{_libdir}/pkgconfig/cppunit.pc
%{_includedir}/*

%files devel-doc
%doc doc/html/*
%{_datadir}/susehelp

%changelog
