#
# spec file for package php-cs-fixer
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


%define package_name  PHP-CS-Fixer
%global doc_version   2.14
Name:           php-cs-fixer
Version:        2.14.4
Release:        0
Summary:        PHP Coding Standards Fixer
License:        MIT
Group:          Development/Tools/Building
URL:            https://cs.symfony.com/
Source:         https://github.com/FriendsOfPHP/%{package_name}/releases/download/v%{version}/%{name}.phar
Source1:        https://github.com/FriendsOfPHP/%{package_name}/releases/download/v%{version}/%{name}.phar.asc
Source2:        %{name}.keyring
Source3:        https://raw.githubusercontent.com/FriendsOfPHP/PHP-CS-Fixer/v%{version}/README.rst
Source4:        https://raw.githubusercontent.com/FriendsOfPHP/PHP-CS-Fixer/v%{version}/LICENSE
BuildRequires:  php7 >= 7.0.0
Requires:       php7-iconv
Requires:       php7-json
Requires:       php7-phar
Requires:       php7-tokenizer
BuildArch:      noarch

%description
The PHP Coding Standards Fixer (PHP CS Fixer) tool fixes code to follow
standards; this can be the PHP coding standards as defined in the
PSR-1, PSR-2, etc., or other community driven ones like the Symfony one.
Custom styles can also be defined through configuration.

It can modernize code (like converting the pow function to the ** operator
on PHP 5.6) and (micro) optimize it.

%prep
%setup -q -c -T
cp %{SOURCE3} %{SOURCE4} .

%build
# empty section

%install
# Install compiled phar file
install -d -m 0750 %{buildroot}%{_bindir}
install -m 0755 %{SOURCE0} %{buildroot}%{_bindir}/php-cs-fixer

%files
%doc README.rst
%license LICENSE
%{_bindir}/*

%changelog
