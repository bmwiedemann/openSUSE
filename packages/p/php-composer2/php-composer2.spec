#
# spec file for package php-composer2
#
# Copyright (c) 2021 SUSE LLC
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
Version:        2.1.8
Release:        0
Summary:        Dependency Management for PHP
License:        MIT
Group:          Development/Libraries/Other
URL:            https://getcomposer.org/
Source0:        https://getcomposer.org/download/%{version}/composer.phar
Source1:        https://github.com/composer/composer/raw/%{version}/LICENSE
Requires:       php-curl
Requires:       php-json
Requires:       php-openssl
Requires:       php-phar
Requires:       php-zip
Requires:       php-zlib
Provides:       composer = %{version}
Provides:       php-composer = %{version}
Provides:       php5-composer = %{version}
Provides:       php7-composer = %{version}
BuildArch:      noarch
%if 0%{?sles_version} >= 10
BuildRequires:  php53 >= 5.3.2
Requires:       php53 >= 5.3.2
%else
BuildRequires:  php >= 5.3.2
Requires:       php >= 5.3.2
%endif

%description
Composer is a dependency manager tracking local dependencies of your projects
and libraries.

%prep
%setup -q -c -T
cp %{SOURCE1} .

%build

%install
# Install compiled phar file
install -d -m 0750 %{buildroot}%{_bindir}
install -m 0755 %{SOURCE0} %{buildroot}%{_bindir}/composer2

%files
%license LICENSE
%defattr(-,root,root,0755)
%{_bindir}/composer2

%changelog
