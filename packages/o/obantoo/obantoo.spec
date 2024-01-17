#
# spec file for package obantoo
#
# Copyright (c) 2022 SUSE LLC
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


Name:           obantoo
Version:        2.1.12
Release:        0
Summary:        German Online Banking Library
License:        LGPL-3.0-only
Group:          Development/Languages/Java
URL:            http://obantoo.sourceforge.net/
Source0:        %{name}-%{version}.tar.gz
Patch0:         %{name}-classpath.patch
Patch1:         %{name}-no-hard-source-target.patch
BuildRequires:  ant
BuildRequires:  dos2unix
BuildRequires:  glassfish-jaxb-api
BuildRequires:  itextpdf
BuildRequires:  java-devel >= 1.8
BuildRequires:  junit
BuildArch:      noarch

%description
A library of tools for German online banking implementing SEPA, IBAN/BIC, DETAUS and QIF.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
find . -name \*.jar -print -delete
build-jar-repository -s lib itextpdf junit glassfish-jaxb-api

dos2unix *.txt

%build
%{ant} -Dant.build.javac.source=1.8 -Dant.build.javac.target=1.8

%install
mkdir -p %{buildroot}%{_javadir}
install build/%{name}-bin-%{version}.jar %{buildroot}%{_javadir}

%files
%doc LGPL.txt
%{_javadir}/%{name}-bin-%{version}.jar

%changelog
