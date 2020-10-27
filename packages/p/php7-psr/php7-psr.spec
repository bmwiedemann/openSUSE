#
# spec file for package php7-psr
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


%define _name           psr
%define _php            php7

Name:           %{_php}-psr
Version:        1.0.0
Release:        0
Summary:        PSR Extension Module
License:        BSD-2-Clause
Group:          Development/Libraries/PHP
URL:            http://www.php-fig.org/psr/
Source0:        https://pecl.php.net/get/%{_name}-%{version}.tgz
BuildRequires:  %{_php}-devel
BuildRequires:  gcc
Requires:       php(api) = %{php_core_api}
Requires:       php(zend-abi) = %{php_zend_api}

%description
This extension provides the accepted PSR interfaces, so they can be used in an extension.

%prep
%setup -q -n %{_name}-%{version}

%build
export CFLAGS="%{optflags} -fvisibility=hidden"
%{__phpize}
%configure --enable-%{_name}
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_libdir}/%{_php}/extensions
mkdir -p %{buildroot}%{_sysconfdir}/%{_php}/conf.d
make INSTALL_ROOT=%{buildroot} install-modules

cat > %{buildroot}/%{_sysconfdir}/%{_php}/conf.d/%{_name}.ini << EOF
; comment out next line to disable %{_name} extension in php"
extension=%{_name}.so
EOF

%files
%doc CHANGELOG.md README.md
%license LICENSE.md
%{_libdir}/%{_php}/extensions/%{_name}.so
%config(noreplace) %{_sysconfdir}/%{_php}/conf.d/%{_name}.ini

%changelog
