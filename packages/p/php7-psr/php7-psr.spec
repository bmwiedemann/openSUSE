#
# spec file for package php7-psr
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


%define php_name    php7
%define pkg_name    psr
%define php_extdir  %(%{__php_config} --extension-dir)
%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150200
%define php_confdir %(%{__php_config} --ini-dir)
%else
%define php_confdir %{_sysconfdir}/%{php_name}/conf.d
%endif

Name:           %{php_name}-%{pkg_name}
Version:        1.0.1
Release:        0
Summary:        PSR Extension Module
License:        BSD-2-Clause
Group:          Development/Libraries/PHP
URL:            http://www.php-fig.org/psr/
Source0:        https://pecl.php.net/get/%{pkg_name}-%{version}.tgz
BuildRequires:  %{php_name}-devel
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

%install
make INSTALL_ROOT=%{buildroot} install-modules

mkdir -p %{buildroot}%{php_confdir}
cat > %{buildroot}%{php_confdir}/%{pkg_name}.ini << EOF
; comment out next line to disable %{pkg_name} extension in php"
extension=%{pkg_name}.so
EOF

%files
%doc CHANGELOG.md README.md
%license LICENSE.md
%config(noreplace) %{php_confdir}/%{pkg_name}.ini
%{php_extdir}/%{pkg_name}.so

%changelog
