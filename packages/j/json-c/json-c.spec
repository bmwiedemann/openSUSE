#
# spec file for package json-c
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Name:           json-c
Version:        0.19
Release:        0
Summary:        JSON implementation in C
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://github.com/json-c/json-c
Source0:        https://github.com/json-c/json-c/archive/json-c-%{version}.tar.gz
Source1:        baselibs.conf
Patch1:         no-xxd.patch
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  libtool
BuildRequires:  pkg-config
#!BuildIgnore:  xxd

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

%package devel
Summary:        Development headers and libraries for json-c
Group:          Development/Libraries/C and C++
Requires:       %{libsoname} = %{version}
Provides:       libjson-devel = %{version}
Obsoletes:      libjson-devel < %{version}
Provides:       libjson-c-devel = %{version}
Obsoletes:      libjson-c-devel < %{version}

%description devel
JSON-C implements a reference counting object model that allows you to
easily construct JSON objects in C, output them as JSON formatted
strings and parse JSON formatted strings back into the C
representation of JSON objects.

This package includes header files and scripts needed for developers
using the json-c library

%package doc
Summary:        Documentation files
Group:          Documentation/Other
Provides:       libjson-doc = %{version}
Obsoletes:      libjson-doc < %{version}
Provides:       libjson-c-doc = %{version}
Obsoletes:      libjson-c-doc < %{version}
BuildArch:      noarch

%description doc
JSON-C implements a reference counting object model that allows you to
easily construct JSON objects in C, output them as JSON formatted
strings and parse JSON formatted strings back into the C
representation of JSON objects.

This package includes the json-c documentation.

%prep
%autosetup -p1 -n %{name}-json-c-%{version}

%build
%cmake \
    -DCMAKE_BUILD_TYPE=None \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} \
    -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
    -DENABLE_THREADING=ON \
    -DENABLE_RDRAND=ON
%cmake_build

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

%ldconfig_scriptlets -n %{libsoname}

%files -n %{libsoname}
%{_libdir}/%{libname}.so.*
%license COPYING

%files devel
%{_libdir}/%{libname}.so
%{_includedir}/json-c
%{_libdir}/pkgconfig/*.pc
%dir %{_libdir}/cmake/json-c
%{_libdir}/cmake/json-c/json-c-config.cmake
%{_libdir}/cmake/json-c/json-c-targets-none.cmake
%{_libdir}/cmake/json-c/json-c-targets.cmake

%files doc
%license COPYING
%doc AUTHORS ChangeLog README README.html
%doc %{_docdir}/%{name}-doc

%changelog
