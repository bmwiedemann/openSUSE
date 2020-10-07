#
# spec file for package php7-uuid
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
%define pkg_name    uuid
#
Name:           php7-uuid
Version:        1.2.0
Release:        0
Summary:        PHP UUID support functions
License:        LGPL-2.1-only
Group:          Productivity/Networking/Web/Servers
URL:            https://pecl.php.net/uuid
Source:         https://pecl.php.net/get/%{pkg_name}-%{version}.tgz
BuildRequires:  libuuid-devel
BuildRequires:  php7-devel
Provides:       php-%{pkg_name} = %{version}
Obsoletes:      php-%{pkg_name} < %{version}
%if %{?php_zend_api}0
Requires:       php(api) = %{php_core_api}
Requires:       php(zend-abi) = %{php_zend_api}
%else
%requires_eq    php7
%endif

%description

This extension provides functions to generate and analyse
universally unique identifiers (UUIDs).

%prep
%setup -q -n %{pkg_name}-%{version}


mkdir %{name}

%build
%{_bindir}/phpize
pushd %{name}
CFLAGS="%{optflags}"
CXXFLAGS="%{optflags}"
export CFLAGS
export CXXFLAGS
../configure --with-%{pkg_name}=%{_usr} --with-libdir=%{_lib}
%make_build
popd

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags} -C %{name} INSTALL_ROOT=%{buildroot}
mkdir -p %{buildroot}%{_sysconfdir}/%{php_name}/conf.d
echo "; comment out next line to disable %{pkg_name} extension in php" > %{buildroot}%{_sysconfdir}/%{php_name}/conf.d/%{pkg_name}.ini
echo 'extension = %{pkg_name}.so' >> %{buildroot}%{_sysconfdir}/%{php_name}/conf.d/%{pkg_name}.ini

%check
# only check if the extension can be loaded
%{_bindir}/php \
    --no-php-ini \
    --define extension=%{buildroot}%{_libdir}/%{php_name}/extensions/%{pkg_name}.so \
    --modules | grep %{pkg_name}
if [ -x %{_bindir}/zts-php ] ; then
%{_bindir}/zts-php \
    --no-php-ini \
    --define extension=%{buildroot}%{_libdir}/%{php_name}/extensions/%{pkg_name}.so \
    --modules | grep %{pkg_name}
fi


%files
%{_libdir}/%{php_name}/extensions/%{pkg_name}.so
%config(noreplace) %{_sysconfdir}/%{php_name}/conf.d/%{pkg_name}.ini
%license LICENSE

%changelog
