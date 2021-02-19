#
# spec file for package php-phalcon
#
# Copyright (c) 2021 SUSE LLC
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


%define pkg_name    phalcon
%define pkg_cname   cphalcon

%define flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == ""
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
Version:        4.1.0
Release:        0
Summary:        PHP7 Extension Module
License:        BSD-3-Clause
Group:          Development/Libraries/PHP
URL:            http://phalconphp.com/
Source0:        https://github.com/%{pkg_name}/%{pkg_cname}/archive/v%{version}.tar.gz#/%{pkg_cname}-%{version}.tar.gz
Source1:        php-%{pkg_name}-rpmlintrc
BuildRequires:  %{php_name}-ctype
BuildRequires:  %{php_name}-devel
BuildRequires:  %{php_name}-pdo
BuildRequires:  %{php_name}-psr >= 0.7.0
BuildRequires:  gcc
%if "%{php_name}" == "php7"
BuildRequires:  %{php_name}-json
%endif
Requires:       %{php_name}-mysql

%description
Phalcon is a framework for PHP 5 written as a C extension.
Zephir is a high-level language, something between C and PHP. It is
both dynamic and static typed and it supports the features we need to
create and maintain a project like Phalcon.

%prep
%setup -q -n %{pkg_cname}-%{version}

%build
cd build/%{php_name}/safe
%{__phpize}
%configure --enable-%{pkg_name}
%make_build

%install
cd build/%{php_name}/safe
make INSTALL_ROOT=%{buildroot} install-modules
mkdir -p %{buildroot}%{php_cfgdir}
cat >> %{buildroot}%{php_cfgdir}/%{pkg_name}.ini << EOF
; comment out next line to disable %{pkg_name} extension in php
extension=%{pkg_name}.so"
EOF

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md CONTRIBUTING.md README.md
%config(noreplace) %{php_cfgdir}/%{pkg_name}.ini
%{php_extdir}/%{pkg_name}.so

%changelog
