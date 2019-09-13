#
# spec file for package php7-pear-XML_Parser
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


%define pear_name XML_Parser
Name:           php7-pear-XML_Parser
Version:        1.3.7
Release:        0
Summary:        XML parsing class based on PHP's bundled expat
License:        BSD-2-Clause
Group:          Development/Libraries/Other
Url:            http://pear.php.net/package/XML_Parser
Source0:        http://download.pear.php.net/package/XML_Parser-%{version}.tgz
Source1:        LICENSE
BuildRequires:  php7-devel
BuildRequires:  php7-pear
Requires:       php7
Requires:       php7-pear
Provides:       php-pear-%{pear_name} = %{version}
Provides:       php-pear(%{pear_name}) = %{version}
Obsoletes:      php5-pear-%{pear_name}
BuildArch:      noarch
%if 0%{?suse_version} < 1330
BuildRequires:  php7-macros
%endif

%description
This is an XML parser based on PHPs built-in xml extension.

It supports two basic modes of operation: "func" and "event". In "func" mode,
it will look for a function named after each element (xmltag_ELEMENT for start
tags and xmltag_ELEMENT_ for end tags), and in "event" mode it uses a set of
generic callbacks.

Since version 1.2.0 there's a new XML_Parser_Simple class that makes parsing of
most XML documents easier, by automatically providing a stack for the elements.
Furthermore its now possible to split the parser from the handler object, so
you do not have to extend XML_Parser anymore in order to parse a document with
it.

%prep
%setup -q -c
mv package.xml %{pear_name}-%{version}
cp %{SOURCE1} .

%build

%install
pushd %{pear_name}-%{version}
%{__pear} install --nodeps --offline --packagingroot %{buildroot} package.xml
install -D -m 0644 package.xml %{buildroot}%{php_pearxmldir}/%{pear_name}.xml
rm -rf %{buildroot}/%{php_peardir}/{doc,tmp}
rm -rf %{buildroot}/%{php_peardir}/.{filemap,lock,registry,channels,depdb,depdblock}
popd

%{php_pear_gen_filelist}

%post
if [ "$1" = "1" ]; then
  # install (rpm -i)
  %{__pear} install --nodeps --soft --force --register-only %{php_pearxmldir}/%{pear_name}.xml ||:
fi
if [ "$1" = "2" ]; then
  # update (rpm -U)
  %{__pear} upgrade --offline --register-only %{php_pearxmldir}/%{pear_name}.xml ||:
fi

%postun
if [ "$1" -eq "0" ] ; then
# uninstall (rpm -e)
%{__pear} uninstall --nodeps --ignore-errors --register-only %{pear_name} >/dev/null ||:
fi

%files -f %{name}.files
%doc LICENSE

%changelog
