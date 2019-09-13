#
# spec file for package obantoo
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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

Name:           obantoo
License:        LGPL-3.0
Group:          Development/Languages/Java
Summary:        German Online Banking Library
Version:        2.1.12
Release:        0
Url:            http://obantoo.sourceforge.net/
Source:         %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  dos2unix
BuildRequires:  ant
BuildArch:      noarch

%description
A library of tools for German online banking implementing SEPA, IBAN/BIC, DETAUS and QIF.

%prep
%setup -q
dos2unix *.txt

%build
%ant

%install
mkdir -p %{buildroot}%{_javadir}
install build/%{name}-bin-%{version}.jar %{buildroot}%{_javadir}

%files
%defattr(-,root,root)
%doc LGPL.txt
%{_javadir}/%{name}-bin-%{version}.jar

%changelog
