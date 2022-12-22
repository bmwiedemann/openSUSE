#
# spec file for package wt
#
# Copyright (c) 2022 SUSE LLC
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


%define WTSRVDIR /srv/wt
%define WTRUNDIR %{WTSRVDIR}/run
%define so_version 4_8_1
Name:           wt
Version:        4.8.1
Release:        0
Summary:        Web Toolkit
License:        GPL-2.0-only
Group:          Development/Libraries/C and C++
URL:            https://www.webtoolkit.eu/wt/
Source0:        https://github.com/emweb/wt/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  FastCGI-devel
BuildRequires:  Mesa-devel
BuildRequires:  apache-rpm-macros
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  glew-devel
BuildRequires:  glu-devel
BuildRequires:  graphviz
BuildRequires:  libharu-devel
BuildRequires:  libpng-devel
BuildRequires:  mysql-devel
BuildRequires:  pango-devel
BuildRequires:  pkgconfig
BuildRequires:  postgresql-devel
BuildRequires:  zlib-devel
BuildRequires:  cmake(Qt5Core)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(sqlite3)
Requires:       FastCGI
Requires:       openssl
Recommends:     %{name}-dbo = %{version}
Suggests:       %{name}-dbo-mysql = %{version}
Suggests:       %{name}-dbo-postgres = %{version}
%if 0%{?suse_version} > 1315
BuildRequires:  libboost_atomic-devel
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_program_options-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libboost_thread-devel
%else
BuildRequires:  boost-devel >= 1.50.0
%endif

%description
Wt is a C++ library and application server for developing and
deploying web applications. The widget-centric API is inspired by
existing C++ GUI APIs. It offers complete abstraction of any
web-specific implementation details.  Most importantly, the entire
application is written in only one compiled language (C++), from which
the library generates the necessary HTML, Javascript, CGI, and AJAX
code.

%package        -n libwtdbo%{so_version}
Summary:        Wt::Dbo ORM library and Sqlite3 back-end
Group:          Development/Libraries/C and C++
Provides:       %{name}-dbo = %{version}

%description    -n libwtdbo%{so_version}
This package contains the Wt::Dbo Object-Relational Mapping library
and Sqlite3 back-end of it.

%package -n libwtdbomysql%{so_version}
Summary:        MySQL back-end for the Wt::Dbo ORM library
Group:          Development/Libraries/C and C++
Provides:       %{name}-dbo-mysql = %{version}

%description -n libwtdbomysql%{so_version}
This package contains the MySQL back-end for the Wt::Dbo ORM library.

%package -n libwtdbopostgres%{so_version}
Summary:        PostgreSQL back-end for the Wt::Dbo ORM library
Group:          Development/Libraries/C and C++
Provides:       %{name}-dbo-postgres = %{version}

%description -n libwtdbopostgres%{so_version}
This package contains the PostgresSQL back-end for the Wt::Dbo ORM library.

%package        devel
Summary:        Web Toolkit - Development Files
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       %{name}-dbo = %{version}
Requires:       %{name}-dbo-mysql = %{version}
Requires:       %{name}-dbo-postgres = %{version}
Requires:       FastCGI-devel
Requires:       Xerces-c-devel
Requires:       boost-devel >= 1.34.1
Requires:       cmake
Requires:       mxml-devel >= 2.3
Requires:       pkgconfig(openssl)

%description devel
Development files for the Wt library.

Wt is a C++ library and application server for developping and
deploying web applications. The widget-centric API is inspired by
existing C++ GUI APIs. It offers complete abstraction of any
web-specific implementation details.  Most imporantly, the entire
application is written in only one compiled language (C++), from which
the library generates the necessary HTML, Javascript, CGI, and AJAX
code.

%prep
%autosetup -p1

%build
%cmake \
    -DENABLE_FIREBIRD=OFF \
    -DENABLE_QT4=OFF \
    -DSHARED_LIBS=ON \
    -DMULTI_THREADED=ON \
    -DUSE_SYSTEM_SQLITE3=ON \
    -DUSE_SYSTEM_GLEW=ON \
    -DCONNECTOR_HTTP=ON \
    -DCONNECTOR_FCGI=ON \
    -DENABLE_EXT=ON \
    -DWEBGROUP="%{apache_group}" -DWEBUSER="%{apache_user}" \
    -DRUNDIR="%{WTRUNDIR}" \
    -DBUILD_EXAMPLES=ON \
    -DENABLE_POSTGRES=ON \
    -DWT_WITH_SSL=ON \
    -DHTTP_WITH_ZLIB=ON
%cmake_build

%install
%cmake_install

mkdir -p %{buildroot}%{_docdir}/%{name}
mkdir -p %{buildroot}%{WTSRVDIR}
mkdir -p %{buildroot}%{WTRUNDIR}
mkdir %{buildroot}%{_docdir}/%{name}-devel/
cp -rv doc/* %{buildroot}%{_docdir}/%{name}-devel/
mv -v %{buildroot}%{_datadir}/Wt %{buildroot}%{_datadir}/wt

# Remove shell scripts used for generating some images.
rm %{buildroot}%{_datadir}/wt/resources/themes/*/*/generate.sh

%fdupes %{buildroot}/%{_docdir}
%fdupes %{buildroot}/%{_datadir}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%post -n libwtdbo%{so_version} -p /sbin/ldconfig
%postun -n libwtdbo%{so_version} -p /sbin/ldconfig
%post -n libwtdbomysql%{so_version} -p /sbin/ldconfig
%postun -n libwtdbomysql%{so_version} -p /sbin/ldconfig
%post -n libwtdbopostgres%{so_version} -p /sbin/ldconfig
%postun -n libwtdbopostgres%{so_version} -p /sbin/ldconfig

%files
%license LICENSE
%doc Changelog ReleaseNotes.html
%dir %{WTSRVDIR}
%attr(-,%{apache_user},%{apache_group}) %{WTRUNDIR}
%dir %{_sysconfdir}/wt
%config(noreplace) %{_sysconfdir}/wt/wt_config.xml
%{_datadir}/wt
%{_libdir}/libwt.so.*
%{_libdir}/libwtfcgi.so.*
%{_libdir}/libwthttp.so.*
%{_libdir}/libwttest.so.*

%files -n libwtdbo%{so_version}
%{_libdir}/libwtdbo.so.*
%{_libdir}/libwtdbosqlite3.so.*

%files -n libwtdbomysql%{so_version}
%{_libdir}/libwtdbomysql.so.*

%files -n libwtdbopostgres%{so_version}
%{_libdir}/libwtdbopostgres.so.*

%files devel
%{_includedir}/Wt
%{_libdir}/*.so
%{_libdir}/cmake/wt
%doc %{_docdir}/%{name}-devel

%changelog
