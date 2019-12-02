#
# spec file for package php7-pear-Net_Socket
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
%define pear_name Net_Socket
Name:           php7-pear-Net_Socket
Version:        1.2.2
Release:        0
Summary:        Network Socket Interface
License:        BSD-2-Clause
Group:          Productivity/Networking/Web/Servers
URL:            https://pear.php.net/package/%{pear_name}
Source:         https://pear.php.net/get/%{pear_name}-%{version}.tgz
BuildRequires:  %{php_name}-devel
BuildRequires:  %{php_name}-pear
Requires:       %{php_name}-pear
Provides:       php-pear(%{pear_name}) = %{version}
BuildArch:      noarch

%description
Net_Socket is a class interface to TCP sockets. It provides blocking
and non-blocking operation, with different reading and writing modes
(byte-wise, block-wise, line-wise and special formats like network
byte-order ip addresses).

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
%docdir  %{pear_docdir}
%exclude %{pear_metadir}/.??*
%exclude %{pear_testdir}

%changelog
