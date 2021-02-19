#
# spec file for package php-memcached
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


%define flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == ""
%define php_name php
ExclusiveArch:  do-not-build
%else
%define php_name %{flavor}
%endif

%define php_extdir  %(%{__php_config} --extension-dir)
%define php_cfgdir  %{_sysconfdir}/%{php_name}/conf.d
%define pkg_name    memcached

Name:           %{php_name}-%{pkg_name}
Version:        3.1.5
Release:        0
Summary:        PHP MemcacheD client Extension
License:        PHP-3.01
Group:          Productivity/Networking/Web/Servers
URL:            https://pecl.php.net/package/memcached
Source0:        https://pecl.php.net/get/%{pkg_name}-%{version}.tgz
# PATCH-FIX-UPSTREAM: https://github.com/php-memcached-dev/php-memcached/pull/475
Patch1:         fixup-unit-tests.patch
Patch2:         fixup-unit-tests-broken-in-php8.patch
BuildRequires:  %{php_name}-devel
%if 0%{?suse_version} > 1500
BuildRequires:  fastlzlib-devel
%endif
BuildRequires:  libmemcached-devel >= 1.0.10
BuildRequires:  memcached
BuildRequires:  zlib-devel
Requires:       php(api) = %{php_core_api}
Requires:       php(zend-abi) = %{php_zend_api}
%if "%{php_name}" == "php7"
BuildRequires:  %{php_name}-json
Requires:       %{php_name}-json
%endif

%description
This extension uses libmemcached library to provide API for
communicating with memcached servers.

%prep
%setup -q -n %{pkg_name}-%{version}
%patch1
%if "%{php_name}" == "php8"
%patch2
%endif

%build
export CFLAGS="%{optflags} -fvisibility=hidden"
%{__phpize}
%configure \
	--enable-memcached \
%if 0%{?suse_version} > 1500
	--with-system-fastlz \
%endif
	--enable-memcached-json
%make_build

%check
%if "%{php_name}" == "php7"
export TEST_PHP_ARGS="$TEST_PHP_ARGS -d extension=%{php_extdir}/json.so"
%endif
%{_sbindir}/memcached -P /tmp/memcached.pid -p 11211 -U 11211 -d
%make_build PHP_EXECUTABLE=%{__php} NO_INTERACTION=1 test
kill -TERM $(cat /tmp/memcached.pid)

%install
%make_install INSTALL_ROOT=%{buildroot}
mkdir -p %{buildroot}%{php_cfgdir}
cat > %{buildroot}%{php_cfgdir}/%{pkg_name}.ini <<EOF
; comment out next line to disable %{pkg_name} extension in php
extension = %{pkg_name}.so

EOF
cat %{pkg_name}.ini >> %{buildroot}%{php_cfgdir}/%{pkg_name}.ini

%files
%defattr(-,root,root)
%license LICENSE
%doc ChangeLog CREDITS memcached-api.php README.markdown
%config(noreplace) %{php_cfgdir}/%{pkg_name}.ini
%{php_extdir}/%{pkg_name}.so

%changelog
