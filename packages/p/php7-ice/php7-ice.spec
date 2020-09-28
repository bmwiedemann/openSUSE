#
# spec file for package php7-ice
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


# See also http://en.opensuse.org/openSUSE:Shared_library_packaging_policy

%define _php    php7
%define _name   ice

Name:           %{_php}-%{_name}
Version:        1.7.0
Release:        0
Summary:        PHP framework delivered as C extension
License:        BSD-3-Clause
Group:          Development/Libraries/PHP
Url:            http://www.iceframework.org/
Source0:        https://github.com/ice/framework/archive/%{version}.tar.gz#/%{_name}-%{version}.tar.gz
Patch1:         ice-notime.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{_php}-ctype
BuildRequires:  %{_php}-devel
BuildRequires:  %{_php}-json
BuildRequires:  %{_php}-mbstring
BuildRequires:  %{_php}-mysql
BuildRequires:  %{_php}-openssl
BuildRequires:  %{_php}-pdo
BuildRequires:  %{_php}-tokenizer
BuildRequires:  gcc
BuildRequires:  re2c

%description
ICE is a PHP framework delivered as C extension. You don't need
learn or use the C language, since the functionality is exposed as
PHP classes.

%prep
%setup -qn framework-%version
%patch -P 1 -p1

%build
mv README.md README
mv CHANGELOG.md CHANGELOG
export CC="gcc"
export CFLAGS="%{optflags} -O2 -Wall -fvisibility=hidden -flto -DZEPHIR_RELEASE=1"

pushd build/%{_php}
phpize
%configure --enable-%{_name}
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_libdir}/%{_php}/extensions
mkdir -p %{buildroot}%{_sysconfdir}/%{_php}/conf.d
pushd build/%{_php}
make install INSTALL_ROOT=%{buildroot}

echo "; comment out next line to disable %{_name} extension in php" > %{buildroot}/%{_sysconfdir}/%{_php}/conf.d/%{_name}.ini
echo "extension=%{_name}.so" >> %{buildroot}/%{_sysconfdir}/%{_php}/conf.d/%{_name}.ini

%files
%defattr(-,root,root)
%doc LICENSE README CHANGELOG
%{_libdir}/%{_php}/extensions/%{_name}.so
%config(noreplace) %{_sysconfdir}/%{_php}/conf.d/%{_name}.ini

%changelog
