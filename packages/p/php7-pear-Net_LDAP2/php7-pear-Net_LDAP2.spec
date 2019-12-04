#
# spec file for package php7-pear-Net_LDAP2
#
# Copyright (c) 2019 SUSE LLC
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
%define pear_name Net_LDAP2
Name:           php7-pear-Net_LDAP2
Version:        2.2.0
Release:        0
Summary:        Object oriented interface for searching and manipulating LDAP-entries
License:        LGPL-3.0-only
Group:          Development/Libraries/Other
URL:            https://pear.php.net/package/%{pear_name}
Source:         https://pear.php.net/get/%{pear_name}-%{version}.tgz
BuildRequires:  %{php_name}-devel
BuildRequires:  %{php_name}-pear
Requires:       %{php_name}-pear
Requires:       php-ldap
Provides:       php-pear(%{pear_name}) = %{version}
Obsoletes:      php5-pear-%{pear_name}
BuildArch:      noarch

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
%setup -q -n %{pear_name}-%{version}
# move package.xml when needed
[ -f ../package.xml ] &&  mv ../package.xml .

%build

%install
%{__pear} install --nodeps --offline --packagingroot %{buildroot} package.xml
install -D -m 0644 package.xml %{buildroot}%{php_pearxmldir}/%{pear_name}.xml

%{php_pear_gen_filelist}

%post
if [ "$1" = "1" ]; then
  # on "rpm -ivh"
  %{__pear} install --nodeps --soft --force --register-only %{php_pearxmldir}/%{pear_name}.xml || :
fi
if [ "$1" = "2" ]; then
  # on "rpm -Uvh"
  %{__pear} upgrade --offline --register-only %{php_pearxmldir}/%{pear_name}.xml || :
fi

%postun
if [ "$1" = "0" ]; then
  # on "rpm -e"
  %{__pear} uninstall --nodeps --ignore-errors --register-only pear.php.net/%{pear_name} || :
fi

%files -f %{name}.files
%docdir %{pear_docdir}
%exclude %{pear_metadir}/.??*
%exclude %{pear_testdir}

%changelog
