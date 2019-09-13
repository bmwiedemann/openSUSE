#
# spec file for package php7-pear-Mail_Mime
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
%define pear_name Mail_Mime
Name:           php7-pear-Mail_Mime
Version:        1.10.1
Release:        0
Summary:        PHP classes to create MIME messages
License:        BSD-3-Clause
Group:          Development/Libraries/Other
URL:            http://pear.php.net/package/Mail_Mime
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
Mail_Mime provides classes to deal with the creation and manipulation
of MIME messages. It allows to create e-mail messages consisting of
text parts, HTML parts, inline HTML images, attachments and attached
(embedded) messages. It supports non-ASCII characters in filenames,
subjects, recipients, etc.

%prep
%setup -q -c
mv package.xml %{pear_name}-%{version}

%build

%install
pushd %{pear_name}-%{version}
%{__pear} -d doc_dir=%{pear_docdir} install --nodeps --offline --packagingroot %{buildroot} package.xml
install -D -m 0644 package.xml %{buildroot}%{php_pearxmldir}/%{pear_name}.xml
rm -rf %{buildroot}/%{pear_phpdir}/.{filemap,lock,registry,channels,depdb,depdblock}

%post
if [ "$1" = "1" ]; then
  %{__pear} install --nodeps --soft --force --register-only %{php_pearxmldir}/%{pear_name}.xml
fi
if [ "$1" = "2" ]; then
  %{__pear} upgrade --offline --register-only %{php_pearxmldir}/%{pear_name}.xml
fi

%postun
if [ "$1" = "0" ]; then
  %{__pear} uninstall --nodeps --ignore-errors --register-only pear.php.net/%{pear_name}
fi

%files
%{pear_phpdir}/*
%{php_pearxmldir}/*
%exclude %{pear_testdir}
%exclude %{pear_phpdir}/tmp
%doc %{pear_docdir}

%changelog
