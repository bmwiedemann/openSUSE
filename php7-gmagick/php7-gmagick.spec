#
# spec file for package php7-gmagick
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


%define php_name    php7
%define pkg_name    gmagick
Name:           %{php_name}-%{pkg_name}
Version:        2.0.5RC1
Release:        0
Summary:        Wrapper to the GraphicsMagick library
License:        PHP-3.01
Group:          Productivity/Networking/Web/Servers
URL:            https://pecl.php.net/package/gmagick
Source0:        https://pecl.php.net/get/%{pkg_name}-%{version}.tgz
Source1:        %{pkg_name}.ini
BuildRequires:  %{php_name}-devel >= 7.0.1
BuildRequires:  GraphicsMagick-devel >= 1.3.17
BuildRequires:  ghostscript-fonts-std
BuildRequires:  re2c
Conflicts:      php7-imagick
Provides:       php-%{pkg_name} = %{version}
Obsoletes:      php-%{pkg_name} < %{version}
%if %{?php_zend_api}0
Requires:       php(api) = %{php_core_api}
Requires:       php(zend-abi) = %{php_zend_api}
%else
%requires_eq    %{php_name}
%endif

%description
PHP extension to create, modify and obtain meta information of images using
the GraphicsMagick API

%prep
%setup -q -n %{pkg_name}-%{version}
mkdir %{name}

%build
%{_bindir}/phpize
export CFLAGS="%{optflags} -fvisibility=hidden"
%configure --with-%{pkg_name}=%{_usr}
make %{?_smp_mflags}

%check
make %{?_smp_mflags} PHP_EXECUTABLE=%{__php} NO_INTERACTION=1 test

%install
make DESTDIR=%{buildroot} install INSTALL_ROOT=%{buildroot}
mkdir -p %{buildroot}%{_sysconfdir}/%{php_name}/conf.d
install --mode=0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/%{php_name}/conf.d/%{pkg_name}.ini

%files
%{_libdir}/%{php_name}/extensions/%{pkg_name}.so
%config(noreplace) %{_sysconfdir}/%{php_name}/conf.d/%{pkg_name}.ini
%license LICENSE
%doc CONTRIBUTORS.md README.md

%changelog
