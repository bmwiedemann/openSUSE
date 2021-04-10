#
# spec file for package php-xdebug
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


%define pkg_name    xdebug

%define flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == ""
%define php_name php
ExclusiveArch:  do-not-build
%else
%define php_name %{flavor}
%endif
%if 0%{?suse_version} <= 1500
%define php_extdir  %(%{__php_config} --extension-dir)
%define php_cfgdir  %{_sysconfdir}/%{php_name}/conf.d
%endif

Name:           %{php_name}-%{pkg_name}
Version:        3.0.4
Release:        0
Summary:        Extended PHP debugger
License:        PHP-3.0
Group:          Productivity/Networking/Web/Servers
URL:            https://xdebug.org/
Source0:        https://xdebug.org/files/%{pkg_name}-%{version}.tgz
Source1:        php-%{pkg_name}-rpmlintrc
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
export CFLAGS="%{optflags} -fvisibility=hidden"
%{__phpize}
%configure --enable-xdebug
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}
mkdir -p %{buildroot}%{php_cfgdir}
cat > %{buildroot}%{php_cfgdir}/%{pkg_name}.ini <<EOF
; comment out next line to disable %{pkg_name} extension in php
extension = %{pkg_name}.so
EOF

%check
# check if the extension can be loaded
%{__php} --no-php-ini --define zend_extension=%{buildroot}%{php_extdir}/%{pkg_name}.so \
    --modules | grep Xdebug

%files
%license LICENSE
%doc CREDITS
%config(noreplace) %{php_cfgdir}/%{pkg_name}.ini
%{php_extdir}/%{pkg_name}.so

%changelog
