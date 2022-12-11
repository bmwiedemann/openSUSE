#
# spec file for package php-psr
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


%define pkg_name    psr

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
Version:        1.2.0
Release:        0
Summary:        PSR Extension Module
License:        BSD-2-Clause
Group:          Development/Libraries/PHP
URL:            https://pecl.php.net/package/psr
Source0:        https://pecl.php.net/get/%{pkg_name}-%{version}.tgz
Source1:        php-%{pkg_name}-rpmlintrc
BuildRequires:  %{php_name}-devel >= 7.3.0
BuildRequires:  gcc
Requires:       php(api) = %{php_core_api}
Requires:       php(zend-abi) = %{php_zend_api}

%description
This extension provides the accepted PSR interfaces, so they can be used in an extension.

%prep
%setup -q -n %{pkg_name}-%{version}

%build
export CFLAGS="%{optflags} -fvisibility=hidden"
%{__phpize}
%configure --enable-%{pkg_name}
%make_build

%check
%make_build PHP_EXECUTABLE=%{__php} NO_INTERACTION=1 test

%install
make INSTALL_ROOT=%{buildroot} install-modules
mkdir -p %{buildroot}%{php_cfgdir}
cat > %{buildroot}%{php_cfgdir}/%{pkg_name}.ini << EOF
; comment out next line to disable %{pkg_name} extension in php"
extension=%{pkg_name}.so
EOF

%files
%doc CHANGELOG.md README.md
%license LICENSE.md
%config(noreplace) %{php_cfgdir}/%{pkg_name}.ini
%{php_extdir}/%{pkg_name}.so

%changelog
