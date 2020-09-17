#
# spec file for package php7-xdebug
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


%define pkg_name    xdebug
%define pkg_version %{version}
Name:           php7-%{pkg_name}
Version:        2.9.7
Release:        0
Summary:        Extended PHP debugger
License:        PHP-3.0
Group:          Productivity/Networking/Web/Servers
URL:            https://xdebug.org/
Source:         https://xdebug.org/files/%{pkg_name}-%{pkg_version}.tgz
BuildRequires:  php7 < 8.0
BuildRequires:  php7 >= 7.1
BuildRequires:  php7-devel
BuildRequires:  php7-soap
Provides:       php-%{pkg_name} = %{version}
Obsoletes:      php-%{pkg_name} < %{version}
%if %{?php_zend_api}0
Requires:       php(api) = %{php_core_api}
Requires:       php(zend-abi) = %{php_zend_api}
%else
%requires_eq    php7
%endif

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
%setup -q -n %{pkg_name}-%{pkg_version}

%build
sed -i '1s|^|; comment out next line to disable xdebug extension in php\nzend_extension=xdebug.so\n\n|' xdebug.ini
export CFLAGS="%{optflags} -fvisibility=hidden"
%{__phpize}
%configure --enable-xdebug
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install INSTALL_ROOT=%{buildroot}
mkdir -p %{buildroot}%{_sysconfdir}/php7/conf.d
install -m 644 xdebug.ini %{buildroot}%{_sysconfdir}/php7/conf.d/xdebug.ini

%check
# check if the extension can be loaded
%{__php} --no-php-ini  --define zend_extension=%{buildroot}%{_libdir}/php7/extensions/xdebug.so \
    --modules | grep Xdebug

make %{?_smp_mflags} PHP_EXECUTABLE=%{__php} NO_INTERACTION=1 test

%files
%{_libdir}/php7/extensions/xdebug.so
%config(noreplace) %{_sysconfdir}/php7/conf.d/xdebug.ini
%license LICENSE
%doc CREDITS

%changelog
