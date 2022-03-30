#
# spec file for package xml-security
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


%global oname xmlsec
%global _version 2_1_7
Name:           xml-security
Version:        2.1.7
Release:        0
Summary:        Apache XML Security for Java
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://santuario.apache.org/
Source0:        https://archive.apache.org/dist/santuario/java-library/%{_version}/%{oname}-%{version}-source-release.zip
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  unzip
BuildRequires:  mvn(com.fasterxml.woodstox:woodstox-core)
BuildRequires:  mvn(commons-codec:commons-codec)
BuildRequires:  mvn(javax.xml.bind:jaxb-api)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache:apache:pom:)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(xalan:xalan)
BuildRequires:  mvn(xerces:xercesImpl)
BuildRequires:  mvn(xml-apis:xml-apis)
BuildArch:      noarch

%description
Apache XML Security for Java supports XML-Signature Syntax and Processing,
W3C Recommendation 12 February 2002, and XML Encryption Syntax and
Processing, W3C Recommendation 10 December 2002. As of version 1.4,
the library supports the standard Java API JSR-105: XML Digital Signature APIs.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{oname}-%{version}

%pom_remove_plugin :maven-pmd-plugin
%pom_remove_plugin :maven-source-plugin

%pom_xpath_remove pom:plugin/pom:configuration/pom:compilerArgs
%pom_xpath_remove pom:plugin/pom:configuration/pom:annotationProcessorPaths

%pom_xpath_remove pom:profiles

%pom_add_dep javax.xml.bind:jaxb-api::provided

%{mvn_file} :%{oname} %{name} %{oname}

%build
%{mvn_build} -f -- -Dsource=8

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE

%changelog
