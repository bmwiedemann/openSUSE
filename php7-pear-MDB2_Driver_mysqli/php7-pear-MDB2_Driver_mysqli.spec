#
# spec file for package php7-pear-MDB2_Driver_mysqli
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
%define pear_name  MDB2_Driver_mysqli
Name:           php7-pear-MDB2_Driver_mysqli
Version:        1.5.0b4
Release:        0
Summary:        MySQLi MDB2 driver
License:        BSD-3-Clause
Group:          Productivity/Networking/Web/Servers
Url:            http://pear.php.net/package/%{pear_name}
Source:         http://pear.php.net/get/%{pear_name}-%{version}.tgz
BuildRequires:  %{php_name}-devel
BuildRequires:  %{php_name}-pear
Requires:       %{php_name}
Requires:       %{php_name}-mysql
Requires:       %{php_name}-pear
Requires:       php-pear(MDB2) >= 2.5.0b4
Provides:       php-pear-%{pear_name} = %{version}
Provides:       php-pear(%{pear_name}) = %{version}
Obsoletes:      php5-pear-%{pear_name}
BuildArch:      noarch
%if 0%{?suse_version} < 1330
BuildRequires:  %{php_name}-macros
%endif

%description
This is the MySQLi MDB2 driver.

%prep
%setup -q -c

%build

%install
mv package*.xml %{pear_name}-%{version}
cd %{pear_name}-%{version}
%{__pear} -v \
        -d doc_dir=/doc \
        -d bin_dir=%{_bindir} \
        -d data_dir=%{php_peardir}/data \
        install --offline --nodeps -R %{buildroot} package.xml

install -D -m 0644 package.xml %{buildroot}%{php_pearxmldir}/%{pear_name}.xml

rm -rf %{buildroot}/{tmp}
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
