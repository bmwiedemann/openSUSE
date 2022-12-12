#
# spec file for package php-maxminddb
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


%define pkg_name    maxminddb

%define flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "" || (0%{?suse_version} >= 1550 && "%{flavor}" == "php7")
%define php_name php
ExclusiveArch:  do-not-build
%else
%define php_name %{flavor}
%endif
%if 0%{?suse_version} <= 1500
%define php_extdir  %(%{__php_config} --extension-dir)
%define php_cfgdir  %{_sysconfdir}/%{php_name}/conf.d
%endif

Name:           %{php_name}-%{pkg_name}
Version:        1.11.0
Release:        0
Summary:        PHP extension providing access to maxminddb databases
License:        Apache-2.0
Group:          Productivity/Networking/Web/Servers
URL:            https://pecl.php.net/package/maxminddb
Source0:        https://pecl.php.net/get/maxminddb-%{version}.tgz
Source1:        php-%{pkg_name}-rpmlintrc
BuildRequires:  %{php_name}-devel >= 7.2.0
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
%setup -q -n %{pkg_name}-%{version}

%build
cd ext
export CFLAGS="%{optflags} -fvisibility=hidden"
%{__phpize}
%configure
%make_build

%check
cd ext
%make_build PHP_EXECUTABLE=%{__php} NO_INTERACTION=1 test

%install
cd ext
make DESTDIR=%{buildroot} install INSTALL_ROOT=%{buildroot}
mkdir -p %{buildroot}%{php_cfgdir}
cat > %{buildroot}%{php_cfgdir}/%{pkg_name}.ini <<EOF
; comment out next line to disable %{pkg_name} extension in php
extension = %{pkg_name}.so
EOF

%files
%defattr(0644,root,root,-)
%license LICENSE
%doc README.md CHANGELOG.md
%config(noreplace) %{php_cfgdir}/%{pkg_name}.ini
%{php_extdir}/%{pkg_name}.so

%changelog
