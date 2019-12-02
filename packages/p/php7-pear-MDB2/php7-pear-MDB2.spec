#
# spec file for package php7-pear-MDB2
#
# Copyright (c) 2019 SUSE LLC
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


%define pear_name  MDB2
Name:           php7-pear-MDB2
Version:        2.5.0b5
Release:        0
Summary:        Database abstraction layer
License:        BSD-3-Clause
Group:          Productivity/Networking/Web/Servers
URL:            https://pear.php.net/package/%{pear_name}
Source:         https://pear.php.net/get/%{pear_name}-%{version}.tgz
BuildRequires:  php7-devel
BuildRequires:  php7-pear
Requires:       php7-pear
Provides:       php-pear(%{pear_name}) = %{version}
BuildArch:      noarch

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
%setup -q -n %{pear_name}-%{version}
# move package.xml when needed
[ -f ../package.xml ] &&  mv ../package.xml .

%build

%install
%{__pear} install --nodeps --offline --packagingroot %{buildroot} package.xml
install -D -m 0644 package.xml %{buildroot}%{php_pearxmldir}/%{pear_name}.xml

%{php_pear_gen_filelist}

%post
if [ "$1" = "1" ]; then
  # on "rpm -ivh"
  %{__pear} install --nodeps --soft --force --register-only %{php_pearxmldir}/%{pear_name}.xml || :
fi
if [ "$1" = "2" ]; then
  # on "rpm -Uvh"
  %{__pear} upgrade --offline --register-only %{php_pearxmldir}/%{pear_name}.xml || :
fi

%postun
if [ "$1" = "0" ]; then
  # on "rpm -e"
  %{__pear} uninstall --nodeps --ignore-errors --register-only pear.php.net/%{pear_name} || :
fi

%files -f %{name}.files
%docdir  %{pear_docdir}
%exclude %{pear_metadir}/.??*
%exclude %{pear_testdir}

%changelog
