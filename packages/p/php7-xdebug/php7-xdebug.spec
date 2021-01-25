#
# spec file for package php7-xdebug
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


%define php_name    php7
%define pkg_name    xdebug
%define php_extdir  %(%{__php_config} --extension-dir)
%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150200
%define php_confdir %(%{__php_config} --ini-dir)
%else
%define php_confdir %{_sysconfdir}/%{php_name}/conf.d
%endif

Name:           %{php_name}-%{pkg_name}
Version:        3.0.2
Release:        0
Summary:        Extended PHP debugger
License:        PHP-3.0
Group:          Productivity/Networking/Web/Servers
URL:            https://xdebug.org/
Source:         https://xdebug.org/files/%{pkg_name}-%{version}.tgz
BuildRequires:  %{php_name}-devel >= 7.2
BuildRequires:  %{php_name}-soap
Provides:       php-%{pkg_name} = %{version}
Obsoletes:      php-%{pkg_name} < %{version}
Requires:       php(api) = %{php_core_api}
Requires:       php(zend-abi) = %{php_zend_api}

%description
The Xdebug extension helps debugging scripts by providing
debug information such as:

  * stack and function traces in error messages with:
    o full parameter display for user defined functions
    o function name, file name and line indications
    o support for member functions
  * memory allocation
  * protection for infinite recursions

Xdebug also provides:

  * profiling information for PHP scripts
  * code coverage analysis
  * capabilities to debug your scripts interactively with a debug client

%prep
%setup -q -n %{pkg_name}-%{version}

%build
sed -i '1s|^|; comment out next line to disable xdebug extension in php\nzend_extension=xdebug.so\n\n|' xdebug.ini
export CFLAGS="%{optflags} -fvisibility=hidden"
%{__phpize}
%configure --enable-xdebug
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}
mkdir -p %{buildroot}%{php_confdir}
install -m 644 xdebug.ini %{buildroot}%{php_confdir}/xdebug.ini

%check
# check if the extension can be loaded
%{__php} --no-php-ini  --define zend_extension=%{buildroot}%{php_extdir}/xdebug.so \
    --modules | grep Xdebug
%make_build PHP_EXECUTABLE=%{__php} NO_INTERACTION=1 test

%files
%license LICENSE
%doc CREDITS
%config(noreplace) %{php_confdir}/xdebug.ini
%{php_extdir}/xdebug.so

%changelog
