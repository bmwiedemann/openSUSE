#
# spec file for package php-composer2
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           php-composer2
Version:        2.10.2
Release:        0
Summary:        Dependency Management for PHP
License:        MIT
Group:          Development/Libraries/Other
URL:            https://getcomposer.org/
Source0:        https://github.com/composer/composer/archive/refs/tags/%{version}/composer-%{version}.tar.gz
Source1:        https://github.com/composer/composer/releases/download/%{version}/composer.phar
Source2:        https://github.com/composer/composer/releases/download/%{version}/composer.phar.asc
# 161DFBE342889F01DDAC4E61CBB3D576F2A0946F
Source3:        %{name}.keyring
Patch0:         php-composer2-compiler-env.patch
BuildRequires:  php-cli
BuildRequires:  php-phar
Requires:       php >= 7.2.5
Requires:       php-curl
Requires:       php-json
Requires:       php-mbstring
Requires:       php-openssl
Requires:       php-phar
Requires:       php-zip
Requires:       php-zlib
Provides:       composer = %{version}
Provides:       php-composer = %{version}
Provides:       php7-composer = %{version}
Obsoletes:      php-composer < %{version}
BuildArch:      noarch

%description
Composer is a dependency manager tracking local dependencies of your projects
and libraries.

%prep
# 1. Unpack upstream source tarball
%setup -q -n composer-%{version}
# 2. Extract vendor directory from composer.phar (Source1)
mkdir PHAR_EXTRACT
cd PHAR_EXTRACT
cp %{SOURCE1} .
phar extract -f composer.phar
cd ..
mv PHAR_EXTRACT/vendor .
rm -rf PHAR_EXTRACT
# Create empty installed.json so that the Compiler class satisfies its checks
echo '{}' > vendor/composer/installed.json
# 3. Apply custom compiler env support patch
%autopatch -p1

%build
# Build the phar file using our environment-driven Compiler
export COMPOSER_VERSION="%{version}"
# Hardcode a fixed and reproducible release date for version 2.10.2
export COMPOSER_DATE="2026-07-15 12:00:00"
echo 'phar.readonly=Off' > php.ini
PHPRC=./php.ini php -d phar.readonly=Off -r 'require "src/bootstrap.php"; $c = new Composer\Compiler(); $c->compile();'

%install
# Install compiled phar file
install -d -m 0755 %{buildroot}%{_bindir}
install -m 0755 composer.phar %{buildroot}%{_bindir}/composer2
ln -s ./composer2 %{buildroot}%{_bindir}/composer

%files
%license LICENSE
%defattr(-,root,root,0755)
%{_bindir}/composer
%{_bindir}/composer2

%changelog
