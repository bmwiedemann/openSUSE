#
# spec file for package php7-memcached
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define pkg_name memcached
%define conf_dir %{_sysconfdir}/php7/conf.d
%define ext_dir  %(%{__php_config} --extension-dir)
Name:           php7-memcached
Version:        3.1.4
Release:        0
Summary:        PHP MemcacheD client Extension
License:        PHP-3.01
Group:          Productivity/Networking/Web/Servers
URL:            http://pecl.php.net/package/memcached
Source0:        http://pecl.php.net/get/%{pkg_name}-%{version}.tgz
BuildRequires:  libmemcached-devel >= 1.0.10
BuildRequires:  memcached
BuildRequires:  php7
BuildRequires:  php7-devel
BuildRequires:  php7-json
BuildRequires:  pkgconfig
BuildRequires:  sysvinit-tools
Requires:       php(api) = %{php_core_api}
Requires:       php(zend-abi) = %{php_zend_api}
Requires:       php7-json

%description
This extension uses libmemcached library to provide API for
communicating with memcached servers.

%prep
%setup -q -n %{pkg_name}-%{version}

%build
export CFLAGS="%{optflags} -fvisibility=hidden"
%{__phpize}
%configure \
%if 0%{?suse_version} < 1310
	--disable-memcached-sasl \
%endif
	--enable-memcached \
%if 0
	--enable-memcached-igbinary \
%endif
	--enable-memcached-json
make %{?_smp_mflags}

%check
%if 0
TEST_PHP_ARGS="-d extension=%{ext_dir}/igbinary.so"
%endif
TEST_PHP_ARGS="$TEST_PHP_ARGS -d extension=%{ext_dir}/json.so"
export TEST_PHP_ARGS
%{_sbindir}/memcached -vv -p 11211 -U 11211 -d
sleep 5
make %{?_smp_mflags} PHP_EXECUTABLE=%{__php} NO_INTERACTION=1 test
/sbin/killproc -v -TERM %{_sbindir}/memcached

%install
make INSTALL_ROOT=%{buildroot} install
install -d -m 0755 %{buildroot}%{conf_dir}/

cat > %{buildroot}%{conf_dir}/%{pkg_name}.ini <<EOF
; comment out next line to disable %{pkg_name} extension in php
extension = %{pkg_name}.so

EOF
cat %{pkg_name}.ini >> %{buildroot}%{conf_dir}/%{pkg_name}.ini

%files
%defattr(-,root,root)
%license LICENSE
%doc ChangeLog CREDITS memcached-api.php README.markdown
%{ext_dir}/%{pkg_name}.so
%config(noreplace) %{conf_dir}/%{pkg_name}.ini

%changelog
