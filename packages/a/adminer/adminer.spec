#
# spec file for package adminer
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2015 Jimmy Berry <jimmy@boombatower.com>
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


# pending package submissions to Factory
%bcond_with elasticsearch
%bcond_with mongodb
%bcond_with mssql
Name:           adminer
Version:        4.7.7
Release:        0
Summary:        Database management in a single PHP file
License:        GPL-2.0-only OR Apache-2.0
Group:          Productivity/Networking/Web/Frontends

URL:            https://www.adminer.org/
Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}-httpd.conf
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  apache-rpm-macros
BuildRequires:  apache2-devel
BuildRequires:  php-tokenizer
BuildRequires:  xz
Requires:       adminer-database-support = %{version}
Requires:       mod_php_any
Requires:       php-iconv
Requires:       php-mbstring
Requires:       php-session
Requires:       php-zlib
Suggests:       adminer-mysql

%description
Adminer (formerly phpMinAdmin) is a full-featured database management tool
written in PHP. Conversely to phpMyAdmin, it consists of a single file ready to
deploy to the target server. Adminer is available for MySQL, PostgreSQL, SQLite,
MS SQL, Oracle, Firebird, SimpleDB, Elasticsearch and MongoDB.


%package editor
Summary:        Data manipulation for end-users
Group:          Productivity/Networking/Web/Frontends
Requires:       adminer = %{version}

%description editor
Adminer Editor is both easy-to-use and user-friendly database data editing tool
written in PHP. It is suitable for common users, as it provides high-level data
manipulation.


%package designs
Summary:        Alternative designs
Group:          Productivity/Networking/Web/Frontends
Requires:       adminer = %{version}

%description designs
Alternative designs for Adminer. Update the symbolic link at
%{apache_datadir}/%{name}/adminer.css to target the desired theme found in
%{apache_datadir}/%{name}/designs/*/adminer.css.

# Define adminer-database-support packages
%package elasticsearch
Summary:        Dependencies required for Adminer ElasticSearch support
Group:          Productivity/Networking/Web/Frontends
Provides:       adminer-database-support = %{version}
Requires:       adminer = %{version}
Requires:       php-pear-horde_elasticsearch

%description elasticsearch
Virtual package that requires dependencies needed for Adminer ElasticSearch support


%package firebird
Summary:        Dependencies required for Adminer Firebird SQL support
Group:          Productivity/Networking/Web/Frontends
Provides:       adminer-database-support = %{version}
Requires:       adminer = %{version}
Requires:       php-firebird

%description firebird
Virtual package that requires dependencies needed for Adminer Firebird SQL support


%package mongodb
Summary:        Dependencies required for Adminer MongoDB support
Group:          Productivity/Networking/Web/Frontends
Provides:       adminer-database-support = %{version}
Requires:       adminer = %{version}
Requires:       php-pear-horde_mongo

%description mongodb
Virtual package that requires dependencies needed for Adminer MongoDB support


%package mssql
Summary:        Dependencies required for Adminer MS SQL support
Group:          Productivity/Networking/Web/Frontends
Provides:       adminer-database-support = %{version}
Requires:       adminer = %{version}
Requires:       php-mssql

%description mssql
Virtual package that requires dependencies needed for Adminer MS SQL support


%package mysql
Summary:        Dependencies required for Adminer MySQL support
Group:          Productivity/Networking/Web/Frontends
Provides:       adminer-database-support = %{version}
Requires:       adminer = %{version}
Requires:       php-mysql

%description mysql
Virtual package that requires dependencies needed for Adminer MySQL support


%package pgsql
Summary:        Dependencies required for Adminer PostgreSQL support
Group:          Productivity/Networking/Web/Frontends
Provides:       adminer-database-support = %{version}
Requires:       adminer = %{version}
Requires:       php-pgsql

%description pgsql
Virtual package that requires dependencies needed for Adminer PostgreSQL support


%package sqlite
Summary:        Dependencies required for Adminer SQLite support
Group:          Productivity/Networking/Web/Frontends
Provides:       adminer-database-support = %{version}
Requires:       adminer = %{version}
Requires:       php-sqlite

%description sqlite
Virtual package that requires dependencies needed for Adminer SQLite support


%prep
%setup -q

%build
# Creates: ./adminer-{version}.php.
./compile.php

# Creates: ./editor-{version}.php.
./compile.php editor

%install
# Remove version from file names.
mv adminer-%{version}.php adminer.php
mv editor-%{version}.php editor.php

# Install files in datadir.
install -d -m 0755 %{buildroot}%{apache_datadir}/%{name}
cp -R adminer.php editor.php designs/ \
  %{buildroot}%{apache_datadir}/%{name}

# Default to hever theme.
ln -s %{apache_datadir}/%{name}/designs/hever/adminer.css \
  %{buildroot}%{apache_datadir}/%{name}

install -D -m 0644 %{SOURCE1} %{buildroot}%{apache_sysconfdir}/conf.d/%{name}.conf
# Fix paths in httpd config.
sed -i -e "s,@apache_datadir@,%{apache_datadir},g" -e "s,@name@,%{name},g" \
  %{buildroot}%{apache_sysconfdir}/conf.d/%{name}.conf

# README for adminer-database-support packages
echo "Virtual package for Adminer database support" > README

%post
# Enable required apache modules.
if [ -x /usr/sbin/a2enmod ] ; then
  # Get installed php_version (5 or 7).
  php_version=$(php -v | grep '(cli)' | awk '{print $2}' | awk -F'.' '{print $1}')
  if [ -n "$php_version" ]; then
    a2enmod -q php${php_version} || a2enmod php${php_version}
    a2enmod -q version || a2enmod version
  fi
fi

%if 0%{?suse_version} < 1310
%restart_on_update apache2
#%%else
#systemctl try-restart apache2 >/dev/null
%endif

%postun
%if 0%{?suse_version} < 1310
%restart_on_update apache2
#%%else
#systemctl try-restart apache2 >/dev/null
%endif

%files
%defattr(-,root,root)
%doc changes.txt
%dir %{apache_datadir}/%{name}
%{apache_datadir}/%{name}/adminer.php
%{apache_datadir}/%{name}/designs/hever/
%config(noreplace) %{apache_datadir}/%{name}/adminer.css
%config(noreplace) %{apache_sysconfdir}/conf.d/%{name}.conf

%files editor
%defattr(-,root,root)
%{apache_datadir}/%{name}/editor.php

%files designs
%defattr(-,root,root)
%{apache_datadir}/%{name}/designs/
%exclude %{apache_datadir}/%{name}/designs/hever/

# Define adminer-database-support packages
%if %{with elasticsearch}
%files elasticsearch
%defattr(-,root,root)
%doc README
%endif

%files firebird
%defattr(-,root,root)
%doc README

%if %{with mongodb}
%files mongodb
%defattr(-,root,root)
%doc README
%endif

%if %{with mssql}
%files mssql
%defattr(-,root,root)
%doc README
%endif

%files mysql
%defattr(-,root,root)
%doc README

%files pgsql
%defattr(-,root,root)
%doc README

%files sqlite
%defattr(-,root,root)
%doc README

%changelog
