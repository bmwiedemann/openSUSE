#
# spec file for package php-composer2
#
# Copyright (c) 2024 SUSE LLC
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
Version:        2.7.7
Release:        0
Summary:        Dependency Management for PHP
License:        MIT
Group:          Development/Libraries/Other
URL:            https://getcomposer.org/
Source0:        https://getcomposer.org/download/%{version}/composer.phar
Source1:        https://github.com/composer/composer/raw/%{version}/LICENSE
BuildRequires:  php-phar
Requires:       php >= 7.2.5
Requires:       php-curl
Requires:       php-json
Requires:       php-mbstring
Requires:       php-openssl
Requires:       php-phar
Requires:       php-zip
Requires:       php-zlib
Requires(post): update-alternatives
Requires(postun): update-alternatives
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
cp %{SOURCE1} .

%build

%install
# Install compiled phar file
install -d -m 0750 %{buildroot}%{_bindir}
install -m 0755 %{SOURCE0} %{buildroot}%{_bindir}/composer2
# Create a dummy target for /etc/alternatives/composer
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
ln -s -f %{_sysconfdir}/alternatives/composer %{buildroot}%{_bindir}/composer

%post
update-alternatives --install \
   %{_bindir}/composer composer %{_bindir}/composer2 2

%postun
if [ ! -f %{_bindir}/composer2 ] ; then
   update-alternatives --remove composer %{_bindir}/composer2
fi

%files
%license LICENSE
%defattr(-,root,root,0755)
%{_bindir}/composer
%{_bindir}/composer2
%ghost %{_sysconfdir}/alternatives/composer

%changelog
