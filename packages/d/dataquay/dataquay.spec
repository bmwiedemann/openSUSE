#
# spec file for package dataquay
#
# Copyright (c) 2025 SUSE LLC and contributors
# Copyright (c) 2012 Pascal Bleser <pascal.bleser@opensuse.org>
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


%define soname  0
Name:           dataquay
Version:        0.9.5
Release:        0
Summary:        C++ API for RDF data stores
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://breakfastquay.com/dataquay/
Source:         https://breakfastquay.com/files/releases/%{name}-%{version}.tar.bz2
Patch1:         dataquay-lib64.patch
Patch2:         dataquay-redland.patch
Patch4:         dataquay-sharedlib.patch
# PATCH-FIX-OPENSUSE dataquay-includedir.patch aloisio@gmx.com -- add dataquay subdir to include path
Patch5:         dataquay-includedir.patch
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Test)
BuildRequires:  pkgconfig(raptor2)
BuildRequires:  pkgconfig(redland)

%description
Dataquay is a library that provides a C++ API for an
RDF data store using Qt6 classes and containers.

%package     -n lib%{name}%{soname}
Summary:        C++ API for RDF data stores
Group:          System/Libraries

%description -n lib%{name}%{soname}
Dataquay is a library that provides a C++ API for an
RDF data store using Qt6 classes and containers.

%package devel
Summary:        Development files for dataquay, an RDF data store library
Group:          Development/Libraries/C and C++
Requires:       libdataquay%{soname} = %{version}

%description devel
Dataquay is a library that provides a C++ API for an
RDF data store using Qt6 classes and containers.

This subpackage contains the header files for developing
applications that want to make use of dataquay.

%prep
%autosetup -p1

%build
%qmake6 PREFIX=%{_prefix} LIBDIR=%{_libdir} dataquay.pro
%qmake6_build

%install
%qmake6_install
install -D -m0644 deploy/%{name}.pc %{buildroot}%{_libdir}/pkgconfig/%{name}.pc

%post   -n lib%{name}%{soname} -p /sbin/ldconfig
%postun -n lib%{name}%{soname} -p /sbin/ldconfig

%files -n lib%{name}%{soname}
%defattr(-,root,root,-)
%license COPYING
%doc CHANGELOG README.txt
%{_libdir}/lib%{name}.so.%{soname}
%{_libdir}/lib%{name}.so.%{soname}.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
