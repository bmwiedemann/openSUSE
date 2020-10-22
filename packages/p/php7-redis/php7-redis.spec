#
# spec file for package php7-redis
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


%define php_name    php7
%define pkg_name    redis
Name:           %{php_name}-%{pkg_name}
Version:        5.3.2
Release:        0
Summary:        API for communicating with Redis servers
License:        PHP-3.01
URL:            https://pecl.php.net/package/%{pkg_name}
Source0:        https://pecl.php.net/get/%{pkg_name}-%{version}.tgz
Source1:        %{pkg_name}.ini
BuildRequires:  %{php_name}-devel
BuildRequires:  %{php_name}-json
BuildRequires:  re2c
Requires:       php(api) = %{php_core_api}
Requires:       php(zend-abi) = %{php_zend_api}
Provides:       php-%{pkg_name} = %{version}
Obsoletes:      php-%{pkg_name} < %{version}

%description
This extension provides an API for communicating with Redis servers

%prep
%setup -q -n %{pkg_name}-%{version}

%build
export CFLAGS="%{optflags} -fvisibility=hidden"
%{_bindir}/phpize
%configure
%make_build

%check
%make_build PHP_EXECUTABLE=%{__php} NO_INTERACTION=1 test

%install
%make_install INSTALL_ROOT=%{buildroot}
mkdir -p %{buildroot}%{_sysconfdir}/%{php_name}/conf.d
install -m644 %{SOURCE1} %{buildroot}%{_sysconfdir}/%{php_name}/conf.d/%{pkg_name}.ini

%files
%license COPYING
%doc CREDITS README.markdown
%config(noreplace) %{_sysconfdir}/%{php_name}/conf.d/%{pkg_name}.ini
%{_libdir}/%{php_name}/extensions/%{pkg_name}.so

%changelog
