#
# spec file for package sqlcipher
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


%define         sover 0
Name:           sqlcipher
Version:        4.17.0
Release:        0
Summary:        SQLite database encryption
License:        BSD-3-Clause
URL:            http://sqlcipher.net
Source:         https://github.com/sqlcipher/sqlcipher/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source99:       baselibs.conf
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(zlib)
# The Tcl extension subpackage is gone: upstream's new build system no longer
# produces a standalone sqlcipher Tcl binding.
Obsoletes:      sqlcipher-tcl < %{version}
Obsoletes:      tcl-sqlcipher < %{version}
%{?suse_build_hwcaps_libs}

%description
SQLCipher is an SQLite extension that provides transparent 256-bit AES
encryption of database files. Pages are encrypted before being written to
disk and are decrypted when read back. Due to the small footprint and great
performance it’s ideal for protecting embedded application databases and is
well suited for mobile development.

%package -n libsqlcipher%{sover}
Summary:        Shared library for SQLCipher

%description -n libsqlcipher%{sover}
SQLCipher is an SQLite extension that provides transparent 256-bit AES
encryption of database files. Pages are encrypted before being written to
disk and are decrypted when read back. Due to the small footprint and great
performance it’s ideal for protecting embedded application databases and is
well suited for mobile development.

This package contains the shared library.

%package devel
Summary:        Development files for SQLCipher
Requires:       %{name} = %{version}-%{release}
Requires:       libsqlcipher%{sover} = %{version}-%{release}

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
# Disable LTO: sqlcipher 4.17.0 (SQLite 3.53.3) adds a thread-local xoshiro PRNG
# state; under -flto the x86_64 sqlite3 shell link fails with "relocation
# truncated to fit: R_X86_64_TPOFF32 against symbol xoshiro_s.lto_priv.0". The
# overflow is x86_64-specific (local-exec TLS) and only appears with LTO.
%define _lto_cflags %{nil}
# sqlcipher 4.16.0 switched to SQLite's autosetup configure and now builds the
# upstream sqlite3/libsqlite3 names by default.  Following Debian and Arch:
#  * $CC is exported so the compiler is not derived from %%configure's --host
#    prefix (x86_64-suse-linux-gcc),
#  * the OpenSSL crypto provider is selected via CFLAGS defines + -lcrypto
#    (the old --with-crypto-lib option was removed upstream),
#  * --dll-basename together with an explicit -soname builds the shared library
#    as libsqlcipher.so.0 so it does not collide with system sqlite3.
export CC=gcc
export CFLAGS="%{optflags} -DSQLITE_HAS_CODEC -DSQLITE_EXTRA_INIT=sqlcipher_extra_init -DSQLITE_EXTRA_SHUTDOWN=sqlcipher_extra_shutdown"
export LDFLAGS="-lcrypto -Wl,-soname,libsqlcipher.so.%{sover}"
%configure \
  --disable-static \
  --disable-tcl \
  --with-tempstore=yes \
  --dll-basename=libsqlcipher
%make_build

%install
%make_install
# Rename the upstream sqlite3 artifacts to sqlcipher so the package does not
# collide with the system sqlite3 package (matches Debian/Arch packaging).
mv %{buildroot}%{_bindir}/sqlite3 %{buildroot}%{_bindir}/sqlcipher
mv %{buildroot}%{_mandir}/man1/sqlite3.1 %{buildroot}%{_mandir}/man1/sqlcipher.1
mv %{buildroot}%{_libdir}/pkgconfig/sqlite3.pc %{buildroot}%{_libdir}/pkgconfig/sqlcipher.pc
mkdir -p %{buildroot}%{_includedir}/sqlcipher
mv %{buildroot}%{_includedir}/sqlite3.h %{buildroot}%{_includedir}/sqlcipher/
mv %{buildroot}%{_includedir}/sqlite3ext.h %{buildroot}%{_includedir}/sqlcipher/
# Point the .pc at the renamed library and the relocated headers
sed -i \
  -e 's/-lsqlite3/-lsqlcipher/g' \
  -e 's|^includedir=.*|includedir=%{_includedir}/sqlcipher|' \
  %{buildroot}%{_libdir}/pkgconfig/sqlcipher.pc
find %{buildroot} -type f -name "*.la" -delete -print

%ldconfig_scriptlets -n libsqlcipher%{sover}

%files
%license LICENSE.md
%doc README.md
%{_bindir}/sqlcipher
%{_mandir}/man1/sqlcipher.1%{?ext_man}

%files -n libsqlcipher%{sover}
%license LICENSE.md
%{_libdir}/libsqlcipher.so.*

%files devel
%license LICENSE.md
%doc README.md
%{_libdir}/libsqlcipher.so
%{_libdir}/pkgconfig/sqlcipher.pc
%dir %{_includedir}/sqlcipher
%{_includedir}/sqlcipher/sqlite3.h
%{_includedir}/sqlcipher/sqlite3ext.h

%changelog
