#
# spec file for package php-imagick
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


%define pkg_name    imagick

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
Version:        3.4.4
Release:        0
Summary:        Wrapper to the ImageMagick library
License:        PHP-3.01
Group:          Productivity/Networking/Web/Servers
URL:            https://pecl.php.net/package/imagick
Source0:        https://pecl.php.net/get/%{pkg_name}-%{version}.tgz
Source1:        %{pkg_name}.ini
Source2:        php-%{pkg_name}-rpmlintrc
Patch0:         imagick-reproducible.patch
BuildRequires:  ImageMagick-devel >= 6.5.3.10
BuildRequires:  ghostscript-fonts-std
BuildRequires:  %{php_name}-devel >= 7.0.1
BuildRequires:  re2c
Conflicts:      php7-gmagick
Provides:       php-%{pkg_name} = %{version}
Obsoletes:      php-%{pkg_name} < %{version}
Requires:       php(api) = %{php_core_api}
Requires:       php(zend-abi) = %{php_zend_api}

%description
PHP extension to create, modify and obtain meta information of images using
the ImageMagick API

%prep
%autosetup -n %{pkg_name}-%{version} -p1
# Ignore know failed test on OBS with timeout
rm tests/229_Tutorial_fxAnalyzeImage_case1.phpt

%build
export CFLAGS="%{optflags} -fvisibility=hidden"
%{__phpize}
%configure --with-%{pkg_name}=%{_usr}
%make_build

%check
%if 0%{?qemu_user_space_build}
export TEST_TIMEOUT=600
%endif
%make_build PHP_EXECUTABLE=%{__php} NO_INTERACTION=1 test \
	|| { for f in tests/*.out; do cat $f; echo '------'; done; exit 1; }

%install
make install-modules INSTALL_ROOT=%{buildroot}
mkdir -p %{buildroot}%{php_cfgdir}
install --mode=0644 %{SOURCE1} %{buildroot}%{php_cfgdir}/%{pkg_name}.ini

%files
%defattr(-,root,root,-)
%license LICENSE
%doc ChangeLog CREDITS
%config(noreplace) %{php_cfgdir}/%{pkg_name}.ini
%{php_extdir}/%{pkg_name}.so

%changelog
