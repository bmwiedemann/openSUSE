#
# spec file for package php7-geoip
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define pkg_name    geoip
%define php_name    php7
#
Name:           php7-geoip
Version:        1.1.1
Release:        0
Summary:        PHP module for MaxMind GeoIP libraries
License:        PHP-3.01
Group:          Productivity/Networking/Web/Servers
Url:            https://pecl.php.net/geoip
Source:         https://pecl.php.net/get/%{pkg_name}-%{version}.tgz
Patch0:         geoip-module-deps.patch
BuildRequires:  %{php_name}-devel
BuildRequires:  GeoIP-devel
Provides:       php-%{pkg_name} = %{version}
Obsoletes:      php-%{pkg_name} < %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if %{?php_zend_api}0
Requires:       php(api) = %{php_core_api}
Requires:       php(zend-abi) = %{php_zend_api}
%else
%requires_eq    %{php_name}
%endif

%description
This PHP extension allows you to find the location of an IP address - City, State,
Country, Longitude, Latitude, and other information as all, such as ISP and connection type.
For more info, please visit Maxmind's website.

%prep
%setup -q -n %{pkg_name}-%{version}
%patch0

%build
export CFLAGS="%{optflags} -fvisibility=hidden"
%{_bindir}/phpize
%configure --with-geoip=%{_usr}
make %{?_smp_mflags}

%check
# only check if the extension can be loaded
%{_bindir}/php \
    --no-php-ini \
    --define extension=%{buildroot}%{_libdir}/%{php_name}/extensions/geoip.so \
    --modules | grep geoip

%install
make DESTDIR=%{buildroot} install INSTALL_ROOT=%{buildroot}
mkdir -p %{buildroot}%{_sysconfdir}/%{php_name}/conf.d
echo "; comment out next line to disable geoip extension in php" > %{buildroot}%{_sysconfdir}/%{php_name}/conf.d/geoip.ini
echo 'extension = geoip.so' >> %{buildroot}%{_sysconfdir}/%{php_name}/conf.d/geoip.ini
echo 'geoip.database_standard = /var/lib/GeoIP/GeoIP.dat' >> %{buildroot}%{_sysconfdir}/%{php_name}/conf.d/geoip.ini

%files
%defattr(-,root,root,-)
%{_libdir}/%{php_name}/extensions/geoip.so
%config(noreplace) %{_sysconfdir}/%{php_name}/conf.d/geoip.ini
%doc README ChangeLog
%license LICENSE

%changelog
