#
# spec file for package php-cs-fixer
#
# Copyright (c) 2022 SUSE LLC
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
%global doc_version   3.13
Name:           php-cs-fixer
Version:        3.13.0
Release:        0
Summary:        PHP Coding Standards Fixer
License:        MIT
Group:          Development/Tools/Building
URL:            https://cs.symfony.com/
Source:         https://github.com/FriendsOfPHP/%{package_name}/releases/download/v%{version}/%{name}.phar#/%{name}-%{version}.phar
Source1:        https://github.com/FriendsOfPHP/%{package_name}/releases/download/v%{version}/%{name}.phar.asc#/%{name}-%{version}.phar.asc
Source2:        %{name}.keyring
Source3:        https://raw.githubusercontent.com/FriendsOfPHP/PHP-CS-Fixer/v%{version}/README.md
Source4:        https://raw.githubusercontent.com/FriendsOfPHP/PHP-CS-Fixer/v%{version}/LICENSE
BuildRequires:  php8
Requires:       php8-iconv
Requires:       php8-phar
Requires:       php8-tokenizer
BuildArch:      noarch

%description
The PHP Coding Standards Fixer (PHP CS Fixer) tool fixes code to
follow standards; this can be the PHP coding standards as defined
in the PSR-1, PSR-2, etc., or other community driven ones like the
Symfony one. Custom styles can also be defined through
configuration.

%prep
%setup -q -c -T
cp -a %{SOURCE0} %{name}
cp -a %{SOURCE3} %{SOURCE4} .
# Any alteration breaks the phar.
# sed -i '1c\#!%%{_bindir}/php' php-cs-fixer

%build
# Nothing to build.

%install
install -Dpm 0755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
