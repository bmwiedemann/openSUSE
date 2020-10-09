#
# spec file for package php7-APCu
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


%define pkg_name apcu
Name:           php7-APCu
Version:        5.1.19
Release:        0
Summary:        APCu - APC User Cache
License:        PHP-3.01
Group:          Productivity/Networking/Web/Servers
URL:            https://pecl.php.net/package/APCu
Source:         http://pecl.php.net/get/%{pkg_name}-%{version}.tgz
Source1:        apcu.ini
BuildRequires:  php7-devel >= 7.0
BuildRequires:  xz
Requires:       php(api) = %{php_core_api}
Requires:       php(zend-abi) = %{php_zend_api}
Provides:       php-APCu = %{version}
Obsoletes:      php-APCu < %{version}

%description
APCu is userland caching: APC stripped of opcode caching in preparation
for the deployment of Zend Optimizer+ as the primary solution to opcode
caching in future versions of PHP.

%prep
%setup -q -n %{pkg_name}-%{version}
if [ -z "$SOURCE_DATE_EPOCH" ]; then
FAKE_BUILDTIME=$(LC_ALL=C date -u -r php_apc.c '+%%H:%%M')
FAKE_BUILDDATE=$(LC_ALL=C date -u -r php_apc.c '+%%b %%e %%Y')
sed -e "s/__TIME__/\"$FAKE_BUILDTIME\"/g" -i php_apc.c
sed -e "s/__DATE__/\"$FAKE_BUILDDATE\"/g" -i php_apc.c
fi

%build
export CFLAGS="%{optflags} -fvisibility=hidden"
%{_bindir}/phpize
%configure --enable-apcu
%make_build

%check
%make_build test PHP_EXECUTABLE=%{_bindir}/php NO_INTERACTION=1

%install
make install INSTALL_ROOT=%{buildroot}
install -D -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/php7/conf.d/%{pkg_name}.ini

# remove not used header file(s)
rm -rf %{buildroot}/%{_includedir}/php7/ext/%{pkg_name}/

%files
%{_libdir}/php7/extensions/%{pkg_name}.so
%config(noreplace) %{_sysconfdir}/php7/conf.d/%{pkg_name}.ini
%doc NOTICE README.md TECHNOTES.txt apc.php
%license LICENSE

%changelog
