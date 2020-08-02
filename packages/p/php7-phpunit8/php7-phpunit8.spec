#
# spec file for package php7-phpunit8
#
# Copyright (c) 2019 SUSE LLC
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


Name:           php7-phpunit8
Version:        8.5.0
Release:        0
Summary:        Testing framework for PHP
License:        BSD-2-Clause
Group:          Development/Tools/Building
URL:            https://phpunit.de/
Source:         https://phar.phpunit.de/phpunit-%{version}.phar
Source1:        https://phar.phpunit.de/phpunit-%{version}.phar.asc
Source2:        %{name}.keyring
Source3:        https://raw.githubusercontent.com/sebastianbergmann/phpunit/%{version}/LICENSE
Source4:        https://raw.githubusercontent.com/sebastianbergmann/phpunit/%{version}/README.md
Source5:        macros.phpunit
Source6:        %{name}.rpmlintrc
BuildRequires:  php7 > 7.2.0
Requires:       php-dom
Requires:       php-phar
Requires:       php7 > 7.2.0
Obsoletes:      php7-phpunit6
Obsoletes:      php7-phpunit7_0
Provides:       php-phpunit = %{version}
Obsoletes:      php-phpunit < %{version}
BuildArch:      noarch

%description
PHPUnit is a programmer-oriented testing framework for PHP. It is an instance of the xUnit architecture for unit testing frameworks.

%prep
cp %{SOURCE3} %{SOURCE4} .

%build
# empty section

%install
# Install compiled phar file
install -d -m 0750 %{buildroot}%{_bindir}
install -m 0755 %{SOURCE0} %{buildroot}%{_bindir}/phpunit
# Install macros specific for this version of PHPUnit to be used by other applications
install -d -m 0750 %{buildroot}%{_libexecdir}/rpm/macros.d
install -m 0644 %{SOURCE5} %{buildroot}%{_libexecdir}/rpm/macros.d/macros.phpunit

%files
%license LICENSE
%doc README.md
%{_bindir}/phpunit
%{_libexecdir}/rpm/macros.d/macros.phpunit

%changelog
