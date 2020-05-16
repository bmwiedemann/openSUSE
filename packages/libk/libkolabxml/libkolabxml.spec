#
# spec file for package libkolabxml
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


%global php_extdir %{_libdir}/php5/extensions
%global php_confdir %{_sysconfdir}/php5/conf.d
%define libname %{name}1
%bcond_with php
%bcond_without java
%bcond_with mono
%bcond_with tests
Name:           libkolabxml
Version:        1.1.6
Release:        0
Summary:        Kolab XML Format Schema Definitions Library
License:        LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://kolab.org/about/libkolabxml
Source:         http://mirror.kolabsys.com/pub/releases/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM
Patch0:         0001-Make-sure-boost-is-found-when-using-libkolabxml.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libcurl-devel
BuildRequires:  libxerces-c-devel >= 3.0
BuildRequires:  pkgconfig
BuildRequires:  swig >= 2.0
BuildRequires:  xsd >= 3.0
%if %{with php}
BuildRequires:  php-devel >= 5.3
%endif
BuildRequires:  libboost_system-devel
BuildRequires:  libboost_thread-devel
%if %{with java}
BuildRequires:  java-devel
%endif
%if %{with mono}
BuildRequires:  mono-devel
%endif
%if %{with tests}
BuildRequires:  extra-cmake-modules
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Test)
%endif

%description
Libkolabxml serves as a serialization/de-serialization library for the the Kolab XML Format

Features:
- Based on official standards:
- Todos/Events/Journals are fully xCal compliant
- Contacts/Distributionlists are fully xCard compliant
- Can model everything which is used in the Kolab XML Format 2.0, Kontact and Roundcube.
- Easily extensible
- Canonical storage format
- Supports Todos/Events/Journals/Contacts/Distribution Lists/Notes/Configurations

%package -n %{libname}
Summary:        Kolab XML Format Schema Definitions Library
Group:          System/Libraries

%description -n %{libname}
Libkolabxml serves as a serialization/de-serialization library for the the Kolab XML Format

Features:
- Based on official standards:
- Todos/Events/Journals are fully xCal compliant
- Contacts/Distributionlists are fully xCard compliant
- Can model everything which is used in the Kolab XML Format 2.0, Kontact and Roundcube.
- Easily extensible
- Canonical storage format
- Supports Todos/Events/Journals/Contacts/Distribution Lists/Notes/Configurations

%package devel
Summary:        Kolab XML Format Schema Definitions Library
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Requires:       libboost_chrono-devel
Requires:       libboost_date_time-devel
Requires:       libboost_system-devel
Requires:       libboost_thread-devel
Requires:       libcurl-devel
Requires:       libxerces-c-devel

%description devel
Libkolabxml serves as a serialization/de-serialization library for the the Kolab XML Format

Features:
- Based on official standards:
- Todos/Events/Journals are fully xCal compliant
- Contacts/Distributionlists are fully xCard compliant
- Can model everything which is used in the Kolab XML Format 2.0, Kontact and Roundcube.
- Easily extensible
- Canonical storage format
- Supports Todos/Events/Journals/Contacts/Distribution Lists/Notes/Configurations

%package -n java-%{libname}
Summary:        Java bindings for %{name}
Group:          Development/Languages/Java
Requires:       %{libname} = %{version}
Provides:       java-kolabformat = %{version}

%description -n java-%{libname}
Libkolabxml serves as a serialization/de-serialization library for the the Kolab XML Format

Features:
- Based on official standards:
- Todos/Events/Journals are fully xCal compliant
- Contacts/Distributionlists are fully xCard compliant
- Can model everything which is used in the Kolab XML Format 2.0, Kontact and Roundcube.
- Easily extensible
- Canonical storage format
- Supports Todos/Events/Journals/Contacts/Distribution Lists/Notes/Configurations

This package provides the java bindings for Libkolabxml

%package -n mono-%{libname}
Summary:        Mono (C#) bindings for %{name}
Group:          Development/Languages/Other
Requires:       %{libname} = %{version}
Provides:       csharp-kolabformat = %{version}

%description -n mono-%{libname}
Libkolabxml serves as a serialization/de-serialization library for the the Kolab XML Format

Features:
- Based on official standards:
- Todos/Events/Journals are fully xCal compliant
- Contacts/Distributionlists are fully xCard compliant
- Can model everything which is used in the Kolab XML Format 2.0, Kontact and Roundcube.
- Easily extensible
- Canonical storage format
- Supports Todos/Events/Journals/Contacts/Distribution Lists/Notes/Configurations

This package provides the mono (C#) bindings for Libkolabxml

%package -n php-%{libname}
Summary:        PHP bindings for %{name}
Group:          Development/Languages/Other
Requires:       %{libname} = %{version}
Provides:       php-kolabformat = %{version}

%description -n php-%{libname}
Libkolabxml serves as a serialization/de-serialization library for the the Kolab XML Format

Features:
- Based on official standards:
- Todos/Events/Journals are fully xCal compliant
- Contacts/Distributionlists are fully xCard compliant
- Can model everything which is used in the Kolab XML Format 2.0, Kontact and Roundcube.
- Easily extensible
- Canonical storage format
- Supports Todos/Events/Journals/Contacts/Distribution Lists/Notes/Configurations

This package provides the php bindings for Libkolabxml

%prep
%setup -q
%patch0 -p1

%build
# Tests require X server and net
# no-undefined does not work as the php bindings are "magic"
%cmake \
    -DCMAKE_EXE_LINKER_FLAGS=-Wl,--as-needed \
    -DCMAKE_MODULE_LINKER_FLAGS=-Wl,--as-needed \
    -DCMAKE_SHARED_LINKER_FLAGS=-Wl,--as-needed \
%if %{with java}
    -DJAVA_BINDINGS=TRUE -DJAVA_INSTALL_DIR=%{_jnidir} \
%endif
%if %{with php}
    -DPHP_BINDINGS=TRUE -DPHP_INSTALL_DIR=%{php_extdir}\
%endif
%if %{with mono}
    -DCSHARP_BINDINGS=TRUE -DCSHARP_INSTALL_DIR=%{_libexecdir}/mono/ \
%endif
%if %{with tests}
    -DBUILD_TESTS=TRUE \
    -DBUILD_QT5=TRUE \
%else
    -DBUILD_TESTS=FALSE
%endif

# parallel build is too unstable currently
make -j1

%install
%cmake_install

%if %{with php}
mkdir -p %{buildroot}/%{_datadir}/php5
mv %{buildroot}/%{php_extdir}/kolabformat.php %{buildroot}/%{_datadir}/php5/kolabformat.php

mkdir -p %{buildroot}/%{php_confdir}/
cat >%{buildroot}/%{php_confdir}/kolabformat.ini <<EOF
extension=kolabformat.so
EOF
%endif

%if %{with tests}
%check
export LD_LIBRARY_PATH=$(pwd)/build/src/
cd build/
ctest -V ||:
%endif

%post   -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license COPYING
%doc AUTHORS README
%{_libdir}/libkolabxml.so.*

%if %{with php}
%files -n php-%{libname}
%license COPYING
%config(noreplace) %{php_confdir}/kolabformat.ini
%{_datadir}/php5/kolabformat.php
%{php_extdir}/kolabformat.so
%endif

%if %{with java}
%files -n java-%{libname}
%license COPYING
%dir %{_libdir}/java/
%{_libdir}/java/*
%endif

%if %{with mono}
%files -n mono-%{libname}
%license COPYING
%{_libexecdir}/mono/*
%endif

%files devel
%doc DEVELOPMENT
%dir %{_libdir}/cmake/
%{_libdir}/cmake/Libkolabxml/
%{_libdir}/libkolabxml.so
%{_includedir}/kolabxml/

%changelog
