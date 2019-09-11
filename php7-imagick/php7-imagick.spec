#
# spec file for package php7-imagick
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


%define pkg_name    imagick
Name:           php7-%{pkg_name}
Version:        3.4.4
Release:        0
Summary:        Wrapper to the ImageMagick library
License:        PHP-3.01
Group:          Productivity/Networking/Web/Servers
URL:            https://pecl.php.net/package/imagick
Source0:        https://pecl.php.net/get/%{pkg_name}-%{version}.tgz
Source1:        %{pkg_name}.ini
Patch0:         imagick-reproducible.patch
BuildRequires:  ImageMagick-devel >= 6.5.3.10
BuildRequires:  ghostscript-fonts-std
BuildRequires:  php7-devel >= 7.0.1
BuildRequires:  re2c
Conflicts:      php7-gmagick
Provides:       php-%{pkg_name} = %{version}
Obsoletes:      php-%{pkg_name} < %{version}
%if %{?php_zend_api}0
Requires:       php(api) = %{php_core_api}
Requires:       php(zend-abi) = %{php_zend_api}
%else
%requires_eq    php7
%endif

%description
PHP extension to create, modify and obtain meta information of images using
the ImageMagick API

%prep
%setup -q -n %{pkg_name}-%{version}
%patch0 -p1
mkdir %{name}
# Ignore know failed test on OBS with timeout
rm tests/229_Tutorial_fxAnalyzeImage_case1.phpt

%build
%{_bindir}/phpize
export CFLAGS="%{optflags} -fvisibility=hidden"
%configure --with-%{pkg_name}=%{_usr}
make %{?_smp_mflags}

%check
%if 0%{?qemu_user_space_build}
export TEST_TIMEOUT=600
%endif
make %{?_smp_mflags} PHP_EXECUTABLE=%{__php} NO_INTERACTION=1 test \
	|| { for f in tests/*.out; do cat $f; echo '------'; done; exit 1; }

%install
make DESTDIR=%{buildroot} install INSTALL_ROOT=%{buildroot}
mkdir -p %{buildroot}%{_sysconfdir}/php7/conf.d
install --mode=0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/php7/conf.d/%{pkg_name}.ini

# remove not used header file(s)
rm -rf %{buildroot}/%{_includedir}/php7/ext/%{pkg_name}/

%files
%defattr(0644,root,root,-)
%{_libdir}/php7/extensions/%{pkg_name}.so
%config(noreplace) %{_sysconfdir}/php7/conf.d/%{pkg_name}.ini
%license LICENSE
%doc ChangeLog CREDITS

%changelog
