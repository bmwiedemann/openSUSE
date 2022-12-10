#
# spec file for package php-memcache
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


%define pkg_name    memcache

%define flavor @BUILD_FLAVOR@%nil
%if "%{flavor}" == "" || (0%{?suse_version} >= 1550 && "%{flavor}" == "php7")
%define php_name php
ExclusiveArch:  do-not-build
%else
%define php_name %flavor
%endif
%if 0%{?suse_version} <= 1500
%define php_extdir  %(%{__php_config} --extension-dir)
%define php_cfgdir  %{_sysconfdir}/%{php_name}/conf.d
%endif

Name:           %{php_name}-%{pkg_name}
%if "%{php_name}" == "php8"
Version:        8.0
Release:        0
%else
Version:        4.0.5.2
Release:        0
%endif
Summary:        PHP Memcache client Extension
License:        PHP-3.0
Group:          Productivity/Networking/Web/Servers
URL:            https://pecl.php.net/package/memcache
Source0:        https://pecl.php.net/get/%{pkg_name}-4.0.5.2.tgz
Source1:        https://pecl.php.net/get/%{pkg_name}-8.0.tgz
Source10:       php-memcache-rpmlintrc
Patch1:         fixup-unit-tests.patch
Patch2:         fixup-unit-test-040.patch
# PATCH-FIX-UPSTREAM: https://github.com/websupport-sk/pecl-memcache/pull/88
Patch3:         fix-deprecated-memcache_connect.patch
%if 0%{?suse_version} > 1500
BuildRequires:  %{php_name}-cli
%endif
BuildRequires:  %{php_name}-devel
BuildRequires:  memcached
BuildRequires:  zlib-devel
Requires:       php(api) = %{php_core_api}
Requires:       php(zend-abi) = %{php_zend_api}

%description
Memcached is a caching daemon designed especially for
dynamic web applications to decrease database load by
storing objects in memory.
This extension allows you to work with memcached through
handy OO and procedural interfaces.
The extension allows use to store sessions in memcached
via memcache.

%prep
%if "%{flavor}" == "php8"
%setup -q -n %{pkg_name}-%{version} -T -b 1
%patch3 -p1
%else
%setup -q -n %{pkg_name}-%{version}
%patch2
%endif
%patch1

%build
export CFLAGS="%{optflags} -fvisibility=hidden"
%{__phpize}
%configure
%make_build

%check
if [ -x %{_sbindir}/memcached ]; then
  export MEMCACHED_BIN=%{_sbindir}/memcached
elif [ -x %{_bindir}/memcached ]; then
  export MEMCACHED_BIN=%{_bindir}/memcached
else
  echo "Failed to start memcached - tests can't pass"
  exit 1
fi

$MEMCACHED_BIN -P /tmp/memcached1.pid -p 11211 -U 11211 -d
$MEMCACHED_BIN -P /tmp/memcached2.pid -p 11212 -U 11212 -d
$MEMCACHED_BIN -P /tmp/memcached3.pid -s /tmp/memcached.sock -d
%make_build PHP_EXECUTABLE=%{__php} NO_INTERACTION=1 test
kill $(cat /tmp/memcached*.pid)

%install
%make_install INSTALL_ROOT=%{buildroot}
mkdir -p %{buildroot}%{php_cfgdir}
cat > %{buildroot}%{php_cfgdir}/%{pkg_name}.ini <<EOF
; comment out next line to disable %{pkg_name} extension in php
extension = %{pkg_name}.so
EOF

%files
%license LICENSE
%doc README
%config(noreplace) %{php_cfgdir}/%{pkg_name}.ini
%{php_extdir}/%{pkg_name}.so

%changelog
