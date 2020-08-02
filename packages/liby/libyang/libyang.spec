#
# spec file for package libyang
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2019, Martin Hauke <mardnh@gmx.de>
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


%define sover 1
Name:           libyang
Version:        1.0.167
Release:        0
Summary:        Parser toolkit for IETF YANG data modeling
License:        BSD-3-Clause
Group:          Development/Languages/C and C++
URL:            https://github.com/CESNET/libyang
Source:         https://github.com/CESNET/libyang/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  bison
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  pkgconfig
BuildRequires:  python3-devel
BuildRequires:  swig >= 3.0.12
BuildRequires:  pkgconfig(cmocka)
BuildRequires:  pkgconfig(libpcre)

%description
Libyang implements functions to process schemas expressed in the
YANG data modeling language defined by the IETF in RFCs 6020/7950.
Schemas expressed in this language primarily describe configuration
used by larger network equipment like routers and switches.

In addition to handling the schemas itself, the library also provides
functions to process data described by the schemas.

The library is implemented in C and provides an API for other software
to use in processing configurations.

%package -n libyang%{sover}
Summary:        IETF YANG data modeling parser toolkit runtime
Group:          System/Libraries
Recommends:     %{name}-extentions = %{version}

%description -n libyang%{sover}
Libyang implements functions to process schemas expressed in the
YANG data modeling language defined by the IETF in RFCs 6020/7950.
Schemas expressed in this language primarily describe configuration
used by larger network equipment like routers and switches.

In addition to handling the schemas itself, the library also provides
functions to process data described by the schemas.

The library is implemented in C and provides an API for other software
to use in processing configurations.

%package extentions
Summary:        IETF YANG data modeling parser toolkit runtime extentions
Group:          System/Libraries
Requires:       libyang%{sover} = %{version}

%description extentions
Libyang implements functions to process schemas expressed in the
YANG data modeling language defined by the IETF in RFCs 6020/7950.

This package contains extentions and user types used that enhance
behaviour of the libyang runtime library.

%package devel
Summary:        Development files for libyang
Group:          Development/Libraries/C and C++
Requires:       libyang%{sover} = %{version}

%description devel
Libyang implements functions to process schemas expressed in the
YANG data modeling language defined by the IETF in RFCs 6020/7950.
Schemas expressed in this language primarily describe configuration
used by larger network equipment like routers and switches.

In addition to handling the schemas itself, the library also provides
functions to process data described by the schemas.

This subpackage contains libraries and header files for developing
applications that want to make use of libyang.

%package -n yang-tools
Summary:        Executable tools from the IETF YANG data modeling parser toolkit
Group:          Productivity/Networking/Other

%description -n yang-tools
This package provides the "yanglint" and "yangre" tools which can be used
during the creation of IETF YANG schemas.  The tools are not generally
useful for normal operation where libyang primarily processes configuration
data, not schemas.

%package -n libyang-cpp%{sover}
Summary:        C++ runtime from the IETF YANG parser toolkit
Group:          System/Libraries

%description -n libyang-cpp%{sover}
Partially SWIG-generated bindings to use libyang with a C++ API.
The functionality is the same as in libyang, the C++ code links wraps
and uses libyang C code.

%package -n libyang-cpp-devel
Summary:        C++ development files for the IETF YANG parser toolkit
Group:          Development/Libraries/C and C++
Requires:       libyang-cpp%{sover} = %{version}

%description -n libyang-cpp-devel
Partially SWIG-generated bindings to use libyang with a C++ API.
The functionality is the same as in libyang, the C++ code links wraps
and uses libyang C code.

This is the accompanying development package, containing headers, a
pkgconfig file, and .so entry point for the libyang C++ bindings.

%package -n python3-yang
Summary:        Python3 bindings for the IETF YANG parser toolkit
Group:          Development/Languages/Python

%description -n python3-yang
This package allows using libyang functionality to load IETF YANG models
and data from Python3 code.

The bindings are partially generated by SWIG.

%package doc
Summary:        API documentation for libyang
Group:          Documentation/Other
BuildArch:      noarch

%description doc
This is the API documentation of libyang.

%prep
%setup -q

%build
%cmake \
    -DCMAKE_INSTALL_LIBDIR:PATH=%{_lib} \
    -DENABLE_LYD_PRIV=ON \
    -DGEN_LANGUAGE_BINDINGS=ON \
    -DENABLE_BUILD_TESTS=ON
make %{?_smp_mflags}
doxygen

%install
%cmake_install
mkdir -p %{buildroot}/%{_docdir}/%{name}
mv build/doc/html %{buildroot}%{_docdir}/%{name}/
%fdupes -s %{buildroot}/%{_docdir}/%{name}/html

%check
export LD_LIBRARY_PATH=%{buildroot}/%{_libdir}:$(pwd)/build/swig
%ctest

%post   -n libyang%{sover} -p /sbin/ldconfig
%postun -n libyang%{sover} -p /sbin/ldconfig
%post   -n libyang-cpp%{sover} -p /sbin/ldconfig
%postun -n libyang-cpp%{sover} -p /sbin/ldconfig

%files -n libyang%{sover}
%license LICENSE
%doc FAQ.md KNOWNISSUES.md README.md
%{_libdir}/libyang.so.*

%files extentions
%dir %{_libdir}/libyang
%dir %{_libdir}/libyang/extensions/
%{_libdir}/libyang/extensions/*.so
%dir %{_libdir}/libyang/user_types/
%{_libdir}/libyang/user_types/*.so

%files -n yang-tools
%{_bindir}/yanglint
%{_bindir}/yangre
%{_mandir}/man1/yanglint.1%{?ext_man}
%{_mandir}/man1/yangre.1%{?ext_man}

%files devel
%dir %{_includedir}/libyang/
%{_includedir}/libyang/*.h
%{_libdir}/libyang.so
%{_libdir}/pkgconfig/libyang.pc

%files -n libyang-cpp%{sover}
%{_libdir}/libyang-cpp.so.*

%files -n libyang-cpp-devel
%dir %{_includedir}/libyang/
%{_includedir}/libyang/*.hpp
%{_libdir}/libyang-cpp.so
%{_libdir}/pkgconfig/libyang-cpp.pc

%files -n python3-yang
%{python3_sitearch}/*

%files doc
%dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/html

%changelog
