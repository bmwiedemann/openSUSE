#
# spec file for package php7-pear-Net_Sieve
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define php_name  php7
%define pear_name Net_Sieve
Name:           php7-pear-Net_Sieve
Version:        1.4.4
Release:        0
Summary:        PHP module for talking to a sieve server
License:        BSD-2-Clause
Group:          Development/Libraries/Other
Url:            http://pear.php.net/package/%{pear_name}
Source:         http://download.pear.php.net/package/%{pear_name}-%{version}.tgz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{php_name}-devel >= 5.0
BuildRequires:  %{php_name}-pear
%if 0%{?suse_version} < 1330
BuildRequires:  %{php_name}-macros
%endif
BuildArch:      noarch

Requires:       %{php_name} >= 5.0
Requires:       %{php_name}-pear
Requires:       php-pear(Net_Socket) >= 1.0

Suggests:       php-pear(Auth_SASL) >= 1.0

Provides:       php-pear-%{pear_name} = %{version}
Provides:       php-pear(%{pear_name}) = %{version}
Obsoletes:      php5-pear-%{pear_name}

%description
This package provides an API to talk to servers implementing the managesieve protocol. It can be used to install and remove sieve scripts, mark them active etc.

%prep
%setup -q -c

%build

%install
mv package.xml %{pear_name}-%{version}
cd %{pear_name}-%{version}
%{__pear} install --nodeps --offline --packagingroot %{buildroot} package.xml
install -D -m 0644 package.xml %{buildroot}%{php_pearxmldir}/%{pear_name}.xml

rm -rf %{buildroot}%{php_peardir}/{doc,tmp}
rm -rf %{buildroot}%{php_peardir}/.{filemap,lock,registry,channels,depdb,depdblock}

cd ..

%{php_pear_gen_filelist}

%post
# on `rpm -ivh` PARAM is 1
# on `rpm -Uvh` PARAM is 2
if [ "$1" = "1" ]; then
  %{__pear} install --nodeps --soft --force --register-only %{php_pearxmldir}/%{pear_name}.xml
fi
if [ "$1" = "2" ]; then
  %{__pear} upgrade --offline --register-only %{php_pearxmldir}/%{pear_name}.xml
fi

%postun
# on `rpm -e` PARAM is 0
if [ "$1" = "0" ]; then
  %{__pear} uninstall --nodeps --ignore-errors --register-only pear.php.net/%{pear_name}
fi

%files -f %{name}.files

%changelog
