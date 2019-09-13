#
# spec file for package php7-pear-Auth_SASL
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define php_name php7
%define pear_name  Auth_SASL
Name:           php7-pear-Auth_SASL
Version:        1.1.0
Release:        0
Summary:        Abstraction of various SASL mechanism responses
License:        BSD-3-Clause
Group:          Productivity/Networking/Web/Servers
Url:            http://pear.php.net/package/%{pear_name}
Source:         http://pear.php.net/get/%{pear_name}-%{version}.tgz
BuildRequires:  %{php_name}-devel
BuildRequires:  %{php_name}-pear >= 1.10.1
Requires:       %{php_name}-pear >= 1.10.1
Provides:       php-pear-%{pear_name} = %{version}
Provides:       php-pear(%{pear_name}) = %{version}
Obsoletes:      php5-pear-Auth_SASL
BuildArch:      noarch
%if 0%{?suse_version} <= 1330
BuildRequires:  %{php_name}-macros
%endif

%description
Provides code to generate responses to common SASL mechanisms, including:
  - Digest-MD5
  - CramMD5
  - Plain
  - Anonymous
  - Login (Pseudo mechanism)

%prep
%setup -q %setup -q -n %{pear_name}-%{version}
mv ../package.xml .

%build

%install
%{__pear} install --nodeps --offline --packagingroot %{buildroot} package.xml
install -D -m 0644 package.xml %{buildroot}%{pear_xmldir}/%{pear_name}.xml

rm -rf %{buildroot}/{doc,tmp}
rm -rf %{buildroot}/%{php_peardir}/.{filemap,lock,registry,channels,depdb,depdblock}

%php_pear_gen_filelist

%post
if [ "$1" = "1" ]; then
  # on "rpm -ivh"
  %{__pear} install --nodeps --soft --force --register-only %{pear_xmldir}/%{pear_name}.xml
fi
if [ "$1" = "2" ]; then
  # on "rpm -Uvh"
  %{__pear} upgrade --offline --register-only %{pear_xmldir}/%{pear_name}.xml
fi

%postun
if [ "$1" = "0" ]; then
  # on "rpm -e"
  %{__pear} uninstall --nodeps --ignore-errors --register-only pear.php.net/%{pear_name}
fi

%files -f %{name}.files

%changelog
