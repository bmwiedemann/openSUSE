#
# spec file for package php7-pear-MDB2
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define pear_name  MDB2
Name:           php7-pear-MDB2
Version:        2.5.0b5
Release:        0
Summary:        Database abstraction layer
License:        BSD-3-Clause
Group:          Productivity/Networking/Web/Servers
Url:            http://pear.php.net/package/%{pear_name}
Source:         http://download.pear.php.net/package/%{pear_name}-%{version}.tgz
BuildRequires:  php7-devel
BuildRequires:  php7-pear >= 1.9.1
Requires:       php7
Requires:       php7-pear >= 1.9.1
Provides:       php-pear-%{pear_name} = %{version}
Provides:       php-pear(%{pear_name}) = %{version}
Obsoletes:      php5-pear-%{pear_name}
BuildArch:      noarch
%if 0%{?suse_version} < 1330
BuildRequires:  php7-macros
%endif

%description
PEAR MDB2 is a merge of the PEAR DB and Metabase php database abstraction layers.

It provides a common API for all supported RDBMS. The main difference to most
other DB abstraction packages is that MDB2 goes much further to ensure
portability. MDB2 provides most of its many features optionally that
can be used to construct portable SQL statements:
* Object-Oriented API
* A DSN (data source name) or array format for specifying database servers
* Datatype abstraction and on demand datatype conversion
* Various optional fetch modes to fix portability issues
* Portable error codes
* Sequential and non sequential row fetching as well as bulk fetching
* Ability to make buffered and unbuffered queries
* Ordered array and associative array for the fetched rows
* Prepare/execute (bind) named and unnamed placeholder emulation
* Sequence/autoincrement emulation
* Replace emulation
* Limited sub select emulation
* Row limit emulation
* Transactions/savepoint support
* Large Object support
* Index/Unique Key/Primary Key support
* Pattern matching abstraction
* Module framework to load advanced functionality on demand
* Ability to read the information schema
* RDBMS management methods (creating, dropping, altering)
* Reverse engineering schemas from an existing database
* SQL function call abstraction
* Full integration into the PEAR Framework
* PHPDoc API documentation

%prep
%setup -q -c

%build

%install
mv package*.xml %{pear_name}-%{version}
cd %{pear_name}-%{version}
%{__pear} -v \
	-d doc_dir=%{pear_docdir} \
	-d bin_dir=%{_bindir} \
	-d data_dir=%{php_peardir}/data \
	install --offline --nodeps -R %{buildroot} package.xml

install -D -m 0644 package.xml %{buildroot}%{php_pearxmldir}/%{pear_name}.xml

%check
# up-to date phpunit can not be run

%post
if [ "$1" = "1" ]; then
  %{__pear} install --nodeps --soft --force --register-only %{php_pearxmldir}/%{pear_name}.xml
fi
if [ "$1" = "2" ]; then
  %{__pear} upgrade --offline --register-only %{php_pearxmldir}/%{pear_name}.xml
fi

%postun
if [ "$1" = "0" ]; then
  %{__pear} uninstall --nodeps --ignore-errors --register-only pear.php.net/%{pear_name}
fi

%files
%{pear_phpdir}/*
%{php_pearxmldir}/*
%exclude %{pear_testdir}
%exclude %{pear_phpdir}/.*
%doc %{pear_docdir}

%changelog
