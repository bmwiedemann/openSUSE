#
# spec file for package sqliteodbc
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


Name:           sqliteodbc
Version:        0.9998
Release:        0
Summary:        ODBC driver for SQLite
License:        BSD-2-Clause
Group:          Development/Libraries/C and C++
URL:            http://www.ch-werner.de/sqliteodbc
Source0:        http://www.ch-werner.de/sqliteodbc/%{name}-%{version}.tar.gz
# This is not typical shared library but plugin for unixODBC
Source1:        %{name}-rpmlintrc
BuildRequires:  dos2unix
BuildRequires:  doxygen
BuildRequires:  graphviz
BuildRequires:  libxml2-devel
BuildRequires:  sqlite3-devel
BuildRequires:  unixODBC-devel
BuildRequires:  zlib-devel
Requires:       unixODBC
Requires(post): unixODBC
Requires(preun): unixODBC

%description
ODBC driver for SQLite interfacing SQLite 3.x using the
unixODBC or iODBC driver managers. For more information refer to
http://www.sqlite.org    -  SQLite engine
http://www.unixodbc.org  -  unixODBC Driver Manager
http://www.iodbc.org     -  iODBC Driver Manager

%package doc
Summary:        Documentation for %{name}
Group:          Documentation/HTML

%description doc
ODBC driver for SQLite interfacing SQLite 3.x using the
unixODBC or iODBC driver managers. This package contains generated
documentation.

%prep
%setup -q
# Fix bug https://bugzilla.novell.com/show_bug.cgi?id=969496
# No more changing time stamp for every time this builds
echo "HTML_TIMESTAMP         = NO" >> doxygen.conf

%build
%configure \
	--enable-static=no
%make_build all doxy
dos2unix README

%install
mkdir -p %{buildroot}%{_libdir}
%make_install
find %{buildroot} -type f \( -name '*.a' -o -name '*.la' \) -delete -print

%post
/sbin/ldconfig
if [ -x %{_bindir}/odbcinst ] ; then
	INST=$(%{_bindir}/mktemp)

	if [ -r %{_libdir}/libsqliteodbc.so ] ; then
		%{_bindir}/cat > $INST <<- 'EOD'
			[SQLITE]
			Description=SQLite ODBC 2.X
			Driver=%{_libdir}/libsqliteodbc.so
			Setup=%{_libdir}/libsqliteodbc.so
			Threading=2
			FileUsage=1
		EOD

		%{_bindir}/odbcinst -q -d -n SQLITE | %{_bindir}/grep '^\[SQLITE\]' >/dev/null || {
			%{_bindir}/odbcinst -i -d -n SQLITE -f $INST || true
		}

		%{_bindir}/cat > $INST <<- 'EOD'
			[SQLite Datasource]
			Driver=SQLITE
		EOD

		%{_bindir}/odbcinst -q -s -n "SQLite Datasource" | \
		%{_bindir}/grep '^\[SQLite Datasource\]' >/dev/null || {
			%{_bindir}/odbcinst -i -l -s -n "SQLite Datasource" -f $INST || true
		}
	fi

	if [ -r %{_libdir}/libsqlite3odbc.so ] ; then
		%{_bindir}/cat > $INST <<- 'EOD'
			[SQLITE3]
			Description=SQLite ODBC 3.X
			Driver=%{_libdir}/libsqlite3odbc.so
			Setup=%{_libdir}/libsqlite3odbc.so
			Threading=2
			FileUsage=1
		EOD

		%{_bindir}/odbcinst -q -d -n SQLITE3 | %{_bindir}/grep '^\[SQLITE3\]' >/dev/null || {
			%{_bindir}/odbcinst -i -d -n SQLITE3 -f $INST || true
		}

		%{_bindir}/cat > $INST <<- 'EOD'
			[SQLite3 Datasource]
			Driver=SQLITE3
		EOD

		%{_bindir}/odbcinst -q -s -n "SQLite3 Datasource" | \
		%{_bindir}/grep '^\[SQLite3 Datasource\]' >/dev/null || {
			%{_bindir}/odbcinst -i -l -s -n "SQLite3 Datasource" -f $INST || true
		}
	fi

	%{_bindir}/rm -f $INST || true
fi

%preun
if [ "$1" = "0" ] ; then
	test -x %{_bindir}/odbcinst && {
		%{_bindir}/odbcinst -u -d -n SQLITE || true
		%{_bindir}/odbcinst -u -l -s -n "SQLite Datasource" || true
		%{_bindir}/odbcinst -u -d -n SQLITE3 || true
		%{_bindir}/odbcinst -u -l -s -n "SQLite3 Datasource" || true
	}

	true
fi

%postun -p /sbin/ldconfig

%files
%license license.terms
%doc README ChangeLog
%{_libdir}/libsqlite3_mod_blobtoxy-%{version}.so
%{_libdir}/libsqlite3_mod_blobtoxy.so
%{_libdir}/libsqlite3_mod_csvtable-%{version}.so
%{_libdir}/libsqlite3_mod_csvtable.so
%{_libdir}/libsqlite3_mod_impexp-%{version}.so
%{_libdir}/libsqlite3_mod_impexp.so
%{_libdir}/libsqlite3_mod_xpath-%{version}.so
%{_libdir}/libsqlite3_mod_xpath.so
%{_libdir}/libsqlite3_mod_zipfile-%{version}.so
%{_libdir}/libsqlite3_mod_zipfile.so
%{_libdir}/libsqlite3odbc-%{version}.so
%{_libdir}/libsqlite3odbc.so

%files doc
%license license.terms
%doc README ChangeLog
%doc html

%changelog
