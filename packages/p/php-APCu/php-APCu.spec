#
# spec file for package php-APCu
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


%define pkg_name  APCu
%define pkg_sname apcu

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
Version:        5.1.22
Release:        0
Summary:        APCu - APC User Cache
License:        PHP-3.01
Group:          Productivity/Networking/Web/Servers
URL:            https://pecl.php.net/package/%{pkg_name}
Source:         https://pecl.php.net/get/%{pkg_sname}-%{version}.tgz
Source1:        apcu.ini
Source2:        php-%{pkg_name}-rpmlintrc
BuildRequires:  %{php_name}-devel >= 7.0
Requires:       php(api) = %{php_core_api}
Requires:       php(zend-abi) = %{php_zend_api}
Provides:       php-%{pkg_name} = %{version}
Obsoletes:      php-%{pkg_name} < %{version}

%description
APCu is userland caching: APC stripped of opcode caching in preparation
for the deployment of Zend Optimizer+ as the primary solution to opcode
caching in future versions of PHP.

%prep
%setup -q -n %{pkg_sname}-%{version}

%build
export CFLAGS="%{optflags} -fvisibility=hidden"
%{__phpize}
%configure --enable-apcu
%make_build

%check
%make_build PHP_EXECUTABLE=%{__php} NO_INTERACTION=1 test

%install
make install-modules INSTALL_ROOT=%{buildroot}
install -D -m 0644 %{SOURCE1} %{buildroot}%{php_cfgdir}/%{pkg_sname}.ini

%files
%doc NOTICE README.md TECHNOTES.txt apc.php
%license LICENSE
%config(noreplace) %{php_cfgdir}/%{pkg_sname}.ini
%{php_extdir}/%{pkg_sname}.so

%changelog
