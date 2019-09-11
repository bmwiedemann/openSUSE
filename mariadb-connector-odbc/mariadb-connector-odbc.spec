#
# spec file for package mariadb-connector-odbc
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


Name:           mariadb-connector-odbc
Version:        3.1.1
Release:        0
Summary:        MariaDB ODBC Connector
License:        LGPL-2.1-or-later
Group:          Productivity/Databases/Tools
Url:            https://downloads.mariadb.org/connector-odbc/
Source:         https://downloads.mariadb.org/interstitial/connector-odbc-%{version}/mariadb-connector-odbc-%{version}-ga-src.tar.gz
# signature is from copy/pasted stuff found on the download page, not actual file
Source1:        mariadb-connector-odbc-%{version}-ga-src.tar.gz.asc
Source2:        README
Source3:        sample_odbc.ini
Source4:        mariadb-connector-odbc-rpmlintrc
Patch1:         mysql_header_path.patch
Patch2:         install_correct_path.patch
Patch5:         package_name.patch
Patch6:         DSN_names.patch
Patch7:         missing_libs.patch
Patch8:         nosoname.patch
BuildRequires:  cmake > 3.5.0
BuildRequires:  gcc-c++
# This is actually MariaDB -devel package(s)
BuildRequires:  libmariadb-devel
BuildRequires:  libmariadbprivate
BuildRequires:  openssl-devel
BuildRequires:  unixODBC-devel
Obsoletes:      MyODBC-unixODBC <= 5.1.9

%description
This package contains the MariaDB ODBC Connector to be used with unixODBC.

%prep
%setup -q -n mariadb-connector-odbc-%{version}-ga-src
%patch1 -p1
%patch2 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1

%build
export CFLAGS="%{optflags} -std=gnu11"
%cmake \
  -DWITH_UNIXODBC=1 \
  -DWITH_OPENSSL=ON \
  -DMARIADB_LINK_DYNAMIC=1
%make_jobs

%install
%cmake_install
install -Dpm 0644 %{SOURCE2} %{SOURCE3} \
  %{buildroot}%{_docdir}/%{name}
rm %{buildroot}%{_docdir}/%{name}/COPYING

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%dir %{_docdir}/%{name}
%license COPYING
%{_libdir}/libmaodbc.so
%{_docdir}/%{name}/README
%{_docdir}/%{name}/sample_odbc.ini

%changelog
