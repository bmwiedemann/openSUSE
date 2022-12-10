#
# spec file for package php-gmagick
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


%define pkg_name    gmagick

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
Version:        2.0.6RC1
Release:        0
Summary:        Wrapper to the GraphicsMagick library
License:        PHP-3.01
Group:          Productivity/Networking/Web/Servers
URL:            https://pecl.php.net/package/gmagick
Source0:        https://pecl.php.net/get/%{pkg_name}-%{version}.tgz
Source1:        php-%{pkg_name}-rpmlintrc
Patch1:         ignore-test-GraphicsMagick-1.3.36.patch
# PATCH-FIX-UPSTREAM: https://github.com/vitoc/gmagick/pull/54
Patch2:         fix-param-order-in-test.patch
BuildRequires:  %{php_name}-devel
BuildRequires:  GraphicsMagick-devel
BuildRequires:  ghostscript-fonts-std
BuildRequires:  re2c
Requires:       php(api) = %{php_core_api}
Requires:       php(zend-abi) = %{php_zend_api}
Conflicts:      %{php_name}-imagick
Provides:       php-%{pkg_name} = %{version}
Obsoletes:      php-%{pkg_name} < %{version}

%description
PHP extension to create, modify and obtain meta information of images using
the GraphicsMagick API

%prep
%setup -q -n %{pkg_name}-%{version}
%if 0%{?suse_version} > 1500
%patch1
%endif
%patch2 -p1

%build
export CFLAGS="%{optflags} -fvisibility=hidden %(GraphicsMagick-config --cflags)"
%{__phpize}
%configure
%make_build

%check
%make_build PHP_EXECUTABLE=%{__php} NO_INTERACTION=1 test

%install
%make_install INSTALL_ROOT=%{buildroot}
mkdir -p %{buildroot}%{php_cfgdir}
cat > %{buildroot}%{php_cfgdir}/%{pkg_name}.ini <<EOF
; comment out next line to disable %{pkg_name} extension in php
extension = %{pkg_name}.so
EOF

%files
%license LICENSE
%doc CONTRIBUTORS.md README.md
%config(noreplace) %{php_cfgdir}/%{pkg_name}.ini
%{php_extdir}/%{pkg_name}.so

%changelog
