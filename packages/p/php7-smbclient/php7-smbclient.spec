#
# spec file for package php7-smbclient
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


%define pkg_name smbclient
Name:           php7-smbclient
Version:        1.0.0
Release:        0
Summary:        A PHP wrapper for libsmbclient
License:        PHP-3.01
Group:          Productivity/Networking/Web/Servers
URL:            http://pecl.php.net/package/smbclient
Source:         http://pecl.php.net/get/%{pkg_name}-%{version}.tgz
BuildRequires:  php7-devel >= 7.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(smbclient)
Patch0:         0001-fix-incorrect-deallocation-of-zend_string.patch
Requires:       php(api) = %{php_core_api}
Requires:       php(zend-abi) = %{php_zend_api}
Provides:       php-smbclient = %{version}
Obsoletes:      php-smbclient < %{version}

%description
smbclient is a PHP extension that uses Samba's libsmbclient library to provide
Samba related functions and 'smb' streams to PHP programs.

%prep
%setup -q -n %{pkg_name}-%{version}
%patch0 -p1
%build
export CFLAGS="%{optflags} -fvisibility=hidden"
%{_bindir}/phpize
%configure
make %{?_smp_mflags}

%check
make %{?_smp_mflags} test PHP_EXECUTABLE=%{_bindir}/php NO_INTERACTION=1

%install
make install INSTALL_ROOT=%{buildroot}
mkdir -p %{buildroot}%{_sysconfdir}/php7/conf.d
echo "; comment out next line to disable smbclient extension in php" > %{buildroot}%{_sysconfdir}/php7/conf.d/%{pkg_name}.ini
echo 'extension = smbclient.so' >> %{buildroot}%{_sysconfdir}/php7/conf.d/%{pkg_name}.ini

%files
%{_libdir}/php7/extensions/%{pkg_name}.so
%config(noreplace) %{_sysconfdir}/php7/conf.d/%{pkg_name}.ini

%changelog
