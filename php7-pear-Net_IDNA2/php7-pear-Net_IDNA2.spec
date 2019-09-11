#
# spec file for package php7-pear-Net_IDNA2
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


%define php_name  php7
%define pear_name Net_IDNA2
Name:           php7-pear-Net_IDNA2
Version:        0.2.0
Release:        0
Summary:        PHP library for Punycode encoding and decoding
License:        LGPL-2.0+
Group:          Development/Libraries/PHP
Url:            http://pear.php.net/package/%{pear_name}/
Source:         http://download.pear.php.net/package/%{pear_name}-%{version}.tgz
BuildRequires:  %{php_name}-devel
BuildRequires:  %{php_name}-pear
Requires:       %{php_name}
Requires:       %{php_name}-pear
Provides:       php-pear-%{pear_name} = %{version}
Provides:       php-pear(%{pear_name}) = %{version}
Obsoletes:      php5-pear-%{pear_name}
BuildArch:      noarch
%if 0%{?suse_version} < 1330
BuildRequires:  %{php_name}-macros
%endif

%description
The package provides a class which allows one to convert from and to
internationalized domain names (RFC 3490). They can be used with
various registries worldwide to be translated between their original
(localized) form and their encoded form as it will be used in the DNS
(Domain Name System).

%prep
%setup -q -c

%build

%install
mv package.xml %{pear_name}-%{version}
cd %{pear_name}-%{version}
%{__pear} -v \
        -d doc_dir=/doc \
        -d bin_dir=%{_bindir} \
        -d data_dir=%{php_peardir}/data \
        install --offline --nodeps -R %{buildroot} package.xml

install -D -m 0644 package.xml %{buildroot}%{php_pearxmldir}/%{pear_name}.xml

rm -rf %{buildroot}/{doc,tmp}
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
