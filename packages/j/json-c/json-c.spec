#
# spec file for package json-c
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


%define libname libjson-c
%define libsoname %{libname}5
%define oldlibname libjson
Name:           json-c
Version:        0.14
Release:        0
Summary:        JSON implementation in C
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://github.com/json-c/json-c/wiki
#Git-Clone	git://github.com/json-c/json-c
Source0:        https://s3.amazonaws.com/json-c_releases/releases/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  libtool
BuildRequires:  pkgconfig

%description
JSON-C implements a reference counting object model that allows you to
easily construct JSON objects in C, output them as JSON formatted
strings and parse JSON formatted strings back into the C
representation of JSON objects.

%package -n %{libsoname}
Summary:        JSON-C shared library
Group:          System/Libraries

%description -n %{libsoname}
JSON-C implements a reference counting object model that allows you to
easily construct JSON objects in C, output them as JSON formatted
strings and parse JSON formatted strings back into the C
representation of JSON objects.

This package includes the JSON library.

%package -n %{libname}-devel
Summary:        Development headers and libraries for json-c
Group:          Development/Libraries/C and C++
Requires:       %{libsoname} = %{version}
Provides:       %{oldlibname}-devel = %{version}
Obsoletes:      %{oldlibname}-devel < %{version}

%description -n %{libname}-devel
JSON-C implements a reference counting object model that allows you to
easily construct JSON objects in C, output them as JSON formatted
strings and parse JSON formatted strings back into the C
representation of JSON objects.

This package includes header files and scripts needed for developers
using the json-c library

%package -n %{libname}-doc
Summary:        Documentation files
Group:          Documentation/Other
Provides:       %{oldlibname}-doc = %{version}
Obsoletes:      %{oldlibname}-doc < %{version}
%if 0%{?suse_version} >= 1120
BuildArch:      noarch
%endif

%description -n %{libname}-doc
JSON-C implements a reference counting object model that allows you to
easily construct JSON objects in C, output them as JSON formatted
strings and parse JSON formatted strings back into the C
representation of JSON objects.

This package includes the json-c documentation.

%prep
%setup -q

%build
%if 0%{?suse_version} <= 1110
sed -i 's/-Werror //g' Makefile.am.inc
autoreconf -fiv
%endif
%cmake \
    -DCMAKE_BUILD_TYPE=None \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
    -DENABLE_THREADING=ON \
    -DENABLE_RDRAND=ON

%check
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
%ctest

%install
%cmake_install
find %{buildroot} -type f -name "*.la" -delete -print
# create a compatibilty pkg-config file for software needing it
(cd %{buildroot}%{_libdir}/pkgconfig && ln -s json-c.pc json.pc)
mkdir -p "%{buildroot}%{_docdir}/%{name}-doc"
cp -R doc/html "%{buildroot}%{_docdir}/%{name}-doc"
%fdupes %{buildroot}%{_docdir}

%post -n %{libsoname} -p /sbin/ldconfig
%postun -n %{libsoname} -p /sbin/ldconfig

%files -n %{libsoname}
%{_libdir}/%{libname}.so.*
%license COPYING

%files -n %{libname}-devel
%{_libdir}/%{libname}.so
%{_includedir}/json-c
%{_libdir}/pkgconfig/*.pc
%dir %{_libdir}/cmake/json-c
%{_libdir}/cmake/json-c/json-c-config.cmake
%{_libdir}/cmake/json-c/json-c-targets-none.cmake
%{_libdir}/cmake/json-c/json-c-targets.cmake

%files -n %{libname}-doc
%license COPYING
%doc AUTHORS ChangeLog README README.html
%doc %{_docdir}/%{name}-doc

%changelog
