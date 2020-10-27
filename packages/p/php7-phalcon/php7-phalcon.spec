#
# spec file for package php7-phalcon
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


%define _name           phalcon
%define _cname          cphalcon
%define _php            php7
%define _architecture   %([[ %{_arch} == "i586" ]] && echo "32bits" || echo "64bits")

Name:           %{_php}-phalcon
Version:        4.0.6
Release:        0
Summary:        PHP7 Extension Module
License:        BSD-3-Clause
Group:          Development/Libraries/PHP
URL:            http://phalconphp.com/
Source0:        https://github.com/%{_name}/%{_cname}/archive/v%{version}.tar.gz#/%{_cname}-%{version}.tar.gz
BuildRequires:  %{_php} >= 7.2
BuildRequires:  %{_php}-ctype
BuildRequires:  %{_php}-devel
BuildRequires:  %{_php}-json
BuildRequires:  %{_php}-pdo
BuildRequires:  %{_php}-psr >= 0.7.0
BuildRequires:  gcc
Requires:       %{_php}-mysql

%description
Phalcon is an open source, full stack framework for PHP 5
written as a C-extension, optimized for high performance.
You don't need learn or use the C language, since the functionality
is exposed as PHP classes ready for you to use. Zephir is a high level
language, something between C and PHP. It’s both dynamic and static
typed and it supports just the features we need to create and maintain
a project like Phalcon.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q -n %{_cname}-%{version}

%build
cd build/%{_php}/%{_architecture}
phpize
%configure --enable-%{_name}
make VERBOSE=1 %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_libdir}/%{_php}/extensions
mkdir -p %{buildroot}%{_sysconfdir}/%{_php}/conf.d
cd build/%{_php}/%{_architecture}
make INSTALL_ROOT=%{buildroot} install-modules

echo "; comment out next line to disable %{_name} extension in php" > %{buildroot}/%{_sysconfdir}/%{_php}/conf.d/%{_name}.ini
echo "extension=%{_name}.so" >> %{buildroot}/%{_sysconfdir}/%{_php}/conf.d/%{_name}.ini

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md CONTRIBUTING.md README.md
%{_libdir}/%{_php}/extensions/%{_name}.so
%config(noreplace) %{_sysconfdir}/%{_php}/conf.d/%{_name}.ini

%changelog
