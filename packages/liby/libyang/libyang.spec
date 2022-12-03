#
# spec file for package libyang
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2019-2022, Martin Hauke <mardnh@gmx.de>
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


%global sover 2
Name:           libyang
Version:        2.1.4
Release:        0
Summary:        Parser toolkit for IETF YANG data modeling
License:        BSD-3-Clause
Group:          System/Libraries
URL:            https://github.com/CESNET/libyang
Source0:        https://github.com/CESNET/libyang/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  graphviz
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cmocka)
BuildRequires:  pkgconfig(libpcre2-8) >= 10.30

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

%package doc
Summary:        API documentation for libyang
Group:          Documentation/Other
BuildArch:      noarch

%description doc
This is the API documentation of libyang.

%prep
%autosetup -p1

%build
%cmake \
    -DPLUGINS_DIR=%{_libdir}/libyang%{sover} \
    -DCMAKE_INSTALL_LIBDIR:PATH=%{_lib} \
    -DENABLE_LYD_PRIV=ON \
    -DGEN_LANGUAGE_BINDINGS=ON \
    -DENABLE_BUILD_TESTS=ON
%make_build
doxygen

%install
%cmake_install
cp tools/re/yangre.1 %{buildroot}/%{_mandir}/man1/yangre.1
mkdir -p %{buildroot}/%{_docdir}/libyang%{sover}
mkdir -p %{buildroot}/%{_libdir}/libyang%{sover}/extensions
mkdir -p %{buildroot}/%{_libdir}/libyang%{sover}/types
mkdir -p %{buildroot}%{_docdir}/%{name}/
cp README.md %{buildroot}%{_docdir}/%{name}/
cp -r build/doc/html %{buildroot}%{_docdir}/%{name}/
%fdupes -s %{buildroot}%{_docdir}/%{name}

%check
export LD_LIBRARY_PATH=%{buildroot}/%{_libdir}
%ctest

%post   -n libyang%{sover} -p /sbin/ldconfig
%postun -n libyang%{sover} -p /sbin/ldconfig

%files -n libyang%{sover}
%license LICENSE
%{_libdir}/libyang.so.*
%dir %{_libdir}/libyang%{sover}
%dir %{_libdir}/libyang%{sover}/extensions/
%dir %{_libdir}/libyang%{sover}/types/

%files -n yang-tools
%{_bindir}/yanglint
%{_bindir}/yangre
%{_mandir}/man1/yanglint.1%{?ext_man}
%{_mandir}/man1/yangre.1%{?ext_man}
%{_datadir}/yang/

%files devel
%dir %{_includedir}/libyang/
%{_includedir}/libyang/*.h
%{_libdir}/libyang.so
%{_libdir}/pkgconfig/libyang.pc

%files doc
%doc %{_docdir}/%{name}

%changelog
