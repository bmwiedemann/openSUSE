#
# spec file for package php7-pear-Net_LDAP2
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
%define pear_name Net_LDAP2
Name:           php7-pear-Net_LDAP2
Version:        2.2.0
Release:        0
Summary:        Object oriented interface for searching and manipulating LDAP-entries
License:        LGPL-3.0
Group:          Development/Libraries/Other
Url:            http://pear.php.net/package/%{pear_name}
Source:         http://download.pear.php.net/package/%{pear_name}-%{version}.tgz
Source1:        LICENSE
BuildRequires:  %{php_name}-devel
BuildRequires:  %{php_name}-pear
Requires:       %{php_name}
Requires:       %{php_name}-pear
Requires:       php-ldap
Provides:       php-pear-%{pear_name} = %{version}
Provides:       php-pear(%{pear_name}) = %{version}
Obsoletes:      php5-pear-%{pear_name}
BuildArch:      noarch
%if 0%{?suse_version} < 1330
BuildRequires:  %{php_name}-macros
%endif

%description
Net_LDAP2 is the successor of Net_LDAP which is a clone of Perls Net::LDAPobject interface to directory servers.
It does contain most of Net::LDAP's features but has some own too.
With Net_LDAP2 you have:
 * A simple object-oriented interface to connections, searches entries and filters.
 * Support for tls and ldap v3.
 * Simple modification, deletion and creation of ldap entries.
 * Support for schema handling.

Net_LDAP2 layers itself on top of PHP's existing ldap extensions.

%prep
%setup -q -c
cp %{SOURCE1} .

%build

%install
mv package*.xml %{pear_name}-%{version}
cd %{pear_name}-%{version}

%{__pear} -v \
        -d bin_dir=%{_bindir} \
        -d doc_dir=%{php_peardir}/doc \
        -d data_dir=%{php_peardir}/data \
        -d test_dir=%{php_peardir}/tests \
        install --offline --nodeps -P %{buildroot} package.xml

install -D -m 0644 package.xml %{buildroot}%{php_pearxmldir}/%{pear_name}.xml

cd ..

# We don't pack tests, remove cruft, move docs into %%_docdir
mkdir -p doc/
mv %{buildroot}%{php_peardir}/doc/%{pear_name}/* doc/
rm -rf %{buildroot}%{php_peardir}/{doc,tests}
rm -rf %{buildroot}%{php_peardir}/.{filemap,lock,registry,channels,depdb,depdblock}

%{php_pear_gen_filelist}

%post
# install: $1 = 1
if [ "$1" = "1" ]; then
  %{__pear} install --nodeps --soft --force --register-only %{php_pearxmldir}/%{pear_name}.xml
fi
# upgrade: $1 = 1
if [ "$1" = "2" ]; then
  %{__pear} upgrade --offline --register-only %{php_pearxmldir}/%{pear_name}.xml
fi

%postun
# uninstall: $1 = 0
if [ "$1" = "0" ]; then
  %{__pear} uninstall --nodeps --ignore-errors --register-only pear.php.net/%{pear_name}
fi

%files -f %{name}.files
%doc LICENSE doc/*

%changelog
