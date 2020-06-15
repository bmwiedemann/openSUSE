#
# spec file for package php7-lzf
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


%define pkg_name    LZF
%define pkg_sname   lzf

Name:           php7-lzf
Version:        1.6.8
Release:        0
Summary:        LZF compression
License:        PHP-3.01
Group:          Productivity/Networking/Web/Servers
URL:            https://pecl.php.net/package/%{pkg_name}
Source:         https://pecl.php.net/get/%{pkg_name}-%{version}.tgz
BuildRequires:  php7-devel
Provides:       php-%{pkg_sname} = %{version}
Requires:       php(api) = %{php_core_api}
Requires:       php(zend-abi) = %{php_zend_api}

%description
This package handles LZF de/compression.

%prep
%setup -q -n %{pkg_name}-%{version}

%build
export CFLAGS="%{optflags} -fvisibility=hidden"
%{__phpize}
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} INSTALL_ROOT=%{buildroot}
mkdir -p %{buildroot}%{_sysconfdir}/php7/conf.d

cat > %{buildroot}%{_sysconfdir}/php7/conf.d/%{pkg_sname}.ini << EOF
; comment out next line to disable %{pkg_sname} extension in php
extension = %{pkg_sname}.so
EOF

%check
make %{?_smp_mflags} test PHP_EXECUTABLE=%{__php} NO_INTERACTION=1

%files
%doc lib/README
%license LICENSE
%{_libdir}/php7/extensions/%{pkg_sname}.so
%config(noreplace) %{_sysconfdir}/php7/conf.d/%{pkg_sname}.ini

%changelog
