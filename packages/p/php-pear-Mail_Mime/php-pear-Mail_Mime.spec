#
# spec file for package php-pear-Mail_Mime
#
# Copyright (c) 2020 SUSE LLC
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


%define pear_name  Mail_Mime

Name:           php-pear-Mail_Mime
Version:        1.10.8
Release:        0
Summary:        PHP classes to create MIME messages
License:        BSD-3-Clause
Group:          Development/Libraries/Other
URL:            https://pear.php.net/package/%{pear_name}
Source:         https://pear.php.net/get/%{pear_name}-%{version}.tgz
BuildRequires:  php-devel
BuildRequires:  php-pear
Requires:       php-pear
Provides:       php-pear(%{pear_name}) = %{version}
# PHP5 last used in openSUSE:Leap_42.3
Provides:       php5-pear-%{pear_name} = %{version}
Obsoletes:      php5-pear-%{pear_name} < %{version}
Provides:       php7-pear-%{pear_name} = %{version}
Obsoletes:      php7-pear-%{pear_name} < %{version}
BuildArch:      noarch

%description
Mail_Mime provides classes to deal with the creation and manipulation
of MIME messages. It allows to create e-mail messages consisting of
text parts, HTML parts, inline HTML images, attachments and attached
(embedded) messages. It supports non-ASCII characters in filenames,
subjects, recipients, etc.

%prep
%setup -q -n %{pear_name}-%{version}
# move package.xml when needed
[ -f ../package.xml ] &&  mv ../package.xml . || :

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
