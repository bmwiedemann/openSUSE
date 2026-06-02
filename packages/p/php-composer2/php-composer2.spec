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
Version:        2.10.0
Release:        0
Summary:        Dependency Management for PHP
License:        MIT
Group:          Development/Libraries/Other
URL:            https://getcomposer.org/
Source0:        https://github.com/composer/composer/releases/download/%{version}/composer.phar
Source1:        https://github.com/composer/composer/releases/download/%{version}/composer.phar.asc
Source2:        https://github.com/composer/composer/raw/%{version}/LICENSE
# 161DFBE342889F01DDAC4E61CBB3D576F2A0946F
Source3:        %{name}.keyring
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
%setup -q -c -T
cp %{SOURCE2} .

%build

%install
# Install compiled phar file
install -d -m 0750 %{buildroot}%{_bindir}
install -m 0755 %{SOURCE0} %{buildroot}%{_bindir}/composer2
ln -s ./composer2 %{buildroot}%{_bindir}/composer

%files
%license LICENSE
%defattr(-,root,root,0755)
%{_bindir}/composer
%{_bindir}/composer2

%changelog
