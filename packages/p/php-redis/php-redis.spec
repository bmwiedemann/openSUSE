#
# spec file for package php-redis
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


%define pkg_name    redis

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
Version:        5.3.7
Release:        0
Summary:        API for communicating with Redis servers
License:        PHP-3.01
URL:            https://pecl.php.net/package/%{pkg_name}
Source0:        https://pecl.php.net/get/%{pkg_name}-%{version}.tgz
Source1:        %{pkg_name}.ini
Source2:        php-%{pkg_name}-rpmlintrc
BuildRequires:  %{php_name}-devel
BuildRequires:  re2c
Requires:       php(api) = %{php_core_api}
Requires:       php(zend-abi) = %{php_zend_api}
Provides:       php-%{pkg_name} = %{version}
Obsoletes:      php-%{pkg_name} < %{version}

%description
This extension provides an API for communicating with Redis servers

%prep
%setup -q -n %{pkg_name}-%{version}
sed -i 's|CONFIG_FILE=`tempfile`|CONFIG_FILE=`mktemp`|' tests/mkring.sh

%build
export CFLAGS="%{optflags} -fvisibility=hidden"
%{__phpize}
%configure
%make_build

%check
%make_build PHP_EXECUTABLE=%{__php} NO_INTERACTION=1 test

%install
%make_install INSTALL_ROOT=%{buildroot}
mkdir -p %{buildroot}%{php_cfgdir}
install -pm0644 %{SOURCE1} %{buildroot}%{php_cfgdir}/%{pkg_name}.ini

%files
%license COPYING
%doc CREDITS README.markdown
%config(noreplace) %{php_cfgdir}/%{pkg_name}.ini
%{php_extdir}/%{pkg_name}.so

%changelog
