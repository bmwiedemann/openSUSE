#
# spec file for package SampleICC
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2011-2014 Kai-Uwe Behrmann
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


Name:           SampleICC
Version:        1.6.8
Release:        0
Summary:        Color Management System
License:        BSD-3-Clause
Group:          Development/Libraries/Other
URL:            https://sourceforge.net/projects/sampleicc/
Source:         %{name}-%{version}.tar.gz
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  graphviz
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  libxml2-devel
BuildRequires:  pkgconfig

%package -n lib%{name}1
Summary:        Colour Management System Libraries
Group:          Development/Libraries/Other

%package      -n lib%{name}-devel
Summary:        Headers, Configuration and static Libs + Documentation
Group:          Development/Libraries/Other
Requires:       lib%{name}1 = %{version}

%description
SampleICC is a C++ library for reading, writing, manipulating, and
applying ICC profiles along with applications that make use of this
library.

%description -n lib%{name}1
SampleICC is a C++ library for reading, writing, manipulating, and
applying ICC profiles along with applications that make use of this
library.

%description -n lib%{name}-devel
Header files, libraries and documentation for development of Color Management
applications.

%prep
%setup -q

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
%configure

%install
make  %{?_smp_mflags}
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n lib%{name}1 -p /sbin/ldconfig
%postun -n lib%{name}1 -p /sbin/ldconfig

%files
%license COPYING
%doc AUTHORS ChangeLog README
%{_bindir}/*

%files -n lib%{name}1
%license COPYING
%doc AUTHORS ChangeLog README
%{_libdir}/lib%{name}.so.*
%{_libdir}/libICC_utils.so.*

%files -n lib%{name}-devel
%license COPYING
%doc AUTHORS ChangeLog README
%{_libdir}/lib%{name}.so
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h
%{_libdir}/pkgconfig/*
%{_libdir}/lib%{name}.a
%{_libdir}/libICC_utils.a
%{_libdir}/libICC_utils.so

%changelog
