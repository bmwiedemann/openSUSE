#
# spec file for package cppunit
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define libname libcppunit-1_14-0
Name:           cppunit
Version:        1.14.0
Release:        0
Summary:        C++ Port of the JUnit Testing Framework
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Url:            http://www.freedesktop.org/wiki/Software/cppunit
Source:         http://dev-www.libreoffice.org/src/%{name}-%{version}.tar.gz
Source1:        cppunit-devel.desktop
Source99:       baselibs.conf
Patch0:         gcc9-Wdeprecated-copy-1.patch
Patch1:         gcc9-Wdeprecated-copy-2.patch
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
CppUnit is the C++ port of the famous JUnit framework for unit testing.
Test output is in XML for automatic testing and GUI based for
supervised tests.

%package -n %{libname}
Summary:        Cppunit library for writting C++ unittests
Group:          System/Libraries

%description -n %{libname}
Cppunit library for writting C++ unittests in JUnit like fashion.

%package devel
Summary:        Include Files and Libraries for cppunit
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Suggests:       devel-doc = %{version}
Provides:       libcppunit-devel = %{version}
Obsoletes:      libcppunit-devel < %{version}

%description devel
Cppunit library, headers, and all relevant additions for writting C++ unittests
in JUnit like fashion.

%package devel-doc
Summary:        Documentation for the cppunit API
Group:          Documentation/HTML
Conflicts:      libcppunit-devel < 1.13.2
BuildArch:      noarch

%description devel-doc
This package contains documentation for the cppunit API.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
export CXXFLAGS="%{optflags}"
%configure \
    --docdir=%{_docdir}/%{name} \
    --disable-silent-rules \
    --disable-static \
    --enable-doxygen
make %{?_smp_mflags}

%install
%make_install
# remove la archive
find %{buildroot} -type f -name "*.la" -delete -print
# this got also installed to _defaultdocdir
rm -rf %{buildroot}%{_datadir}/cppunit/html/
find %{buildroot}%{_includedir} -type f | xargs chmod a-x
# install susehelp file
mkdir -p %{buildroot}%{_datadir}/susehelp/meta/Development/Libraries/
install %{SOURCE1} %{buildroot}%{_datadir}/susehelp/meta/Development/Libraries/
%suse_update_desktop_file %{buildroot}%{_datadir}/susehelp/meta/Development/Libraries/cppunit-devel.desktop

%check
make check %{?_smp_mflags}

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS COPYING
%{_libdir}/libcppunit*.so.*
%{_datadir}/cppunit

%files devel
%defattr(-,root,root)
%doc NEWS README THANKS ChangeLog
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/*
%{_bindir}/DllPlugInTester
%{_libdir}/libcppunit*.so
%{_libdir}/pkgconfig/cppunit.pc
%{_includedir}/*

%files devel-doc
%defattr(-,root,root)
%doc doc/html/*
%{_datadir}/susehelp

%changelog
