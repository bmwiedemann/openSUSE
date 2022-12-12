#
# spec file
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


%define pkg_name   ice

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
%if "%{flavor}" == "php8"
Version:        1.9.0
%else
Version:        1.7.0
%endif
Release:        0
Summary:        PHP framework delivered as C extension
License:        BSD-3-Clause
Group:          Development/Libraries/PHP
URL:            http://www.iceframework.org/
Source0:        https://pecl.php.net/get/%{pkg_name}-1.7.0.tgz
Source1:        https://pecl.php.net/get/%{pkg_name}-1.9.0.tgz
Source2:        php-%{pkg_name}-rpmlintrc
BuildRequires:  %{php_name}-ctype
BuildRequires:  %{php_name}-devel
BuildRequires:  %{php_name}-mbstring
BuildRequires:  %{php_name}-mysql
BuildRequires:  %{php_name}-openssl
BuildRequires:  %{php_name}-pdo
BuildRequires:  %{php_name}-tokenizer
BuildRequires:  gcc
BuildRequires:  re2c
%if "%{flavor}" == "php8"
BuildRequires:  %{php_name} < 8.2
%else
BuildRequires:  %{php_name}-json
Requires:       %{php_name}-json
%endif

%description
ICE is a PHP framework delivered as C extension. You don't need
learn or use the C language, since the functionality is exposed as
PHP classes.

%prep
%if "%{flavor}" == "php8"
%setup -q -n %{pkg_name}-%{version} -T -b 1
%else
%setup -q -n %{pkg_name}-%{version}
%endif

%build
export CFLAGS="%{optflags} -fvisibility=hidden"
%{__phpize}
%configure --enable-%{pkg_name}
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}
mkdir -p %{buildroot}%{php_cfgdir}
cat > %{buildroot}%{php_cfgdir}/%{pkg_name}.ini <<EOF
; comment out next line to disable %{pkg_name} extension in php
extension = %{pkg_name}.so
EOF

%files
%defattr(0644,root,root,-)
%license LICENSE
%config(noreplace) %{php_cfgdir}/%{pkg_name}.ini
%{php_extdir}/%{pkg_name}.so

%changelog
