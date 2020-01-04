#
# spec file for package php7-gmagick
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
# PATCH-FIX-UPSTREAM fix-segfault-on-shutdown.patch https://bugs.php.net/bug.php?id=78465
Patch0:         fix-segfault-on-shutdown.patch
BuildRequires:  %{php_name}-devel
BuildRequires:  GraphicsMagick-devel
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
%patch0

%build
export CFLAGS="%{optflags} -fvisibility=hidden %(GraphicsMagick-config --cflags)"
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
%config(noreplace) %{_sysconfdir}/%{php_name}/conf.d/%{pkg_name}.ini
%license LICENSE
%doc CONTRIBUTORS.md README.md
%{_libdir}/%{php_name}/extensions/%{pkg_name}.so

%changelog
