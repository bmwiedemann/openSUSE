#
# spec file for package vsqlite++
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define lib_name libvsqlitepp
%define sover   3
Name:           vsqlite++
Version:        0.3.13
Release:        0
Summary:        Well designed C++ sqlite 3.x wrapper library
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
Url:            https://github.com/vinzenz/vsqlite--
Source0:        https://github.com/vinzenz/vsqlite--/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_headers-devel
%else
BuildRequires:  boost-devel
%endif
BuildRequires:  dos2unix
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  perl-base
BuildRequires:  sqlite-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
VSQLite++ is a C++ wrapper for sqlite3 using the C++ standard library and boost.
VSQLite++ is designed to be easy to use and focuses on simplicity.

%package -n %{lib_name}%{sover}
Summary:        Well designed C++ sqlite 3.x wrapper library
Group:          System/Libraries

%description -n  %{lib_name}%{sover}
VSQLite++ is a C++ wrapper for sqlite3 using the C++ standard library and boost.
VSQLite++ is designed to be easy to use and focuses on simplicity.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{lib_name}%{sover} = %{version}

%description devel
This package contains development files for %{name}.

%prep
%setup -q -n vsqlite---%{version}
find . -iname "*.[ch]pp" -exec dos2unix -k {} \;

%build
autoreconf -fiv
%configure
make %{?_smp_mflags}

%install
%make_install
# do not ship these
find %{buildroot} -type f \( -name '*.a' -o -name '*.la' \) -delete -print

%post -n %{lib_name}%{sover} -p /sbin/ldconfig
%postun -n %{lib_name}%{sover} -p /sbin/ldconfig

%files devel
%defattr(0644, root, root, 0755)
%doc ChangeLog README COPYING
%{_includedir}/sqlite
%{_libdir}/libvsqlitepp.so

%files -n %{lib_name}%{sover}
%defattr(0644, root, root, 0755)
%doc ChangeLog README COPYING
%{_libdir}/libvsqlitepp.so.%{sover}*

%changelog
