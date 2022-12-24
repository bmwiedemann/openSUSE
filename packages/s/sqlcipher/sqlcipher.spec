#
# spec file for package sqlcipher
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


%define         lib_version 3.39.4
%define         lib_name lib%{name}-3_39_4-0
Name:           sqlcipher
Version:        4.5.3
Release:        0
Summary:        SQLite database encryption
License:        BSD-3-Clause
Group:          Productivity/Databases/Clients
URL:            http://sqlcipher.net
Source:         https://github.com/sqlcipher/sqlcipher/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  ncurses-devel
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(tcl)

%description
SQLCipher is an SQLite extension that provides transparent 256-bit AES
encryption of database files. Pages are encrypted before being written to
disk and are decrypted when read back. Due to the small footprint and great
performance it’s ideal for protecting embedded application databases and is
well suited for mobile development.

%package -n %{lib_name}
Summary:        Shared library for SQLCipher
Group:          System/Libraries

%description -n %{lib_name}
SQLCipher is an SQLite extension that provides transparent 256-bit AES
encryption of database files. Pages are encrypted before being written to
disk and are decrypted when read back. Due to the small footprint and great
performance it’s ideal for protecting embedded application databases and is
well suited for mobile development/

This package contains shared library.

%package -n tcl-%{name}
Summary:        Tcl extension for sqlcipher
Group:          Development/Languages/Tcl
%requires_ge    tcl
Provides:       %{name}-tcl = %{version}-%{release}
Obsoletes:      %{name}-tcl < %{version}-%{release}

%description -n tcl-%{name}
SQLCipher is an SQLite extension that provides transparent 256-bit AES
encryption of database files. Pages are encrypted before being written to
disk and are decrypted when read back. Due to the small footprint and great
performance it’s ideal for protecting embedded application databases and is
well suited for mobile development/

This package provides tcl extension for SQLCipher.

%package devel
Summary:        Development files for SQLCipher
Group:          Development/Libraries/C and C++
Requires:       %{lib_name} = %{version}-%{release}
Requires:       %{name} = %{version}-%{release}
Requires:       tcl-%{name} = %{version}-%{release}

%description devel
SQLCipher is an SQLite extension that provides transparent 256-bit AES
encryption of database files. Pages are encrypted before being written to
disk and are decrypted when read back. Due to the small footprint and great
performance it’s ideal for protecting embedded application databases and is
well suited for mobile development.

This package contains development files for SQLCipher.

%prep
%autosetup

%build
export CFLAGS="%{optflags} -DSQLITE_HAS_CODEC -DSQLITE_TEMP_STORE=2"
export LDFLAGS="-lcrypto"
%configure \
  --enable-threadsafe \
  --enable-cross-thread-connections \
  --enable-releasemode \
  --disable-static \
  --with-crypto-lib \
  --with-tcl=%{_libdir} \
  --enable-tempstore=yes
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{lib_name} -p /sbin/ldconfig
%postun -n %{lib_name} -p /sbin/ldconfig

%files
%license LICENSE
%doc README.md
%{_bindir}/sqlcipher

%files -n %{lib_name}
%license LICENSE
%doc README.md
%{_libdir}/libsqlcipher-%{lib_version}.so.0
%{_libdir}/libsqlcipher-%{lib_version}.so.0.8.6

%files -n tcl-%{name}
%license LICENSE
%doc README.md
%dir %{_libdir}/tcl/tcl8.?/sqlite3
%{_libdir}/tcl/tcl8.?/sqlite3/libtclsqlite3.so
%{_libdir}/tcl/tcl8.?/sqlite3/pkgIndex.tcl

%files devel
%license LICENSE
%doc README.md
%{_libdir}/libsqlcipher.so
%{_libdir}/pkgconfig/sqlcipher.pc
%{_includedir}/sqlcipher/
%{_includedir}/sqlcipher/sqlite3.h
%{_includedir}/sqlcipher/sqlite3ext.h

%changelog
