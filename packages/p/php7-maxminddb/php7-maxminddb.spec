#
# spec file for package php7-maxminddb
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


%define source_file MaxMind-DB-Reader-php
%define pkg_name    maxminddb
Name:           php7-%{pkg_name}
Version:        1.8.0
Release:        0
Summary:        PHP extension providing access to maxminddb databases
License:        Apache-2.0
Group:          Productivity/Networking/Web/Servers
URL:            https://pecl.php.net/package/maxminddb
Source0:        https://github.com/maxmind/%{source_file}/archive/v%{version}.tar.gz#/%{source_file}-%{version}.tar.gz
BuildRequires:  php7-devel >= 7.2.0
BuildRequires:  pkgconfig
BuildRequires:  re2c
BuildRequires:  pkgconfig(libmaxminddb)
Requires:       php(api) = %{php_core_api}
Requires:       php(zend-abi) = %{php_zend_api}
Provides:       php-%{pkg_name} = %{version}
Obsoletes:      php-%{pkg_name} < %{version}

%description
This extension provides access to maxminddb databases and is
a drop-in replacement for MaxMind\Db\Reader.

%prep
%setup -q -n %{source_file}-%{version}

%build
cd ext
export CFLAGS="%{optflags} -fvisibility=hidden"
%{_bindir}/phpize
%configure
%make_build

%check
cd ext
%make_build PHP_EXECUTABLE=%{__php} NO_INTERACTION=1 test

%install
cd ext
make DESTDIR=%{buildroot} install INSTALL_ROOT=%{buildroot}
mkdir -p %{buildroot}%{_sysconfdir}/php7/conf.d
echo '; comment out next line to disable the extension
extension = %{pkg_name}.so' > %{buildroot}%{_sysconfdir}/php7/conf.d/%{pkg_name}.ini

%files
%defattr(0644,root,root,-)
%license LICENSE
%doc README.md CHANGELOG.md
%config(noreplace) %{_sysconfdir}/php7/conf.d/%{pkg_name}.ini
%{_libdir}/php7/extensions/%{pkg_name}.so

%changelog
