#
# spec file for package jdom2
#
# Copyright (c) 2023 SUSE LLC
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


Name:           jdom2
Version:        2.0.6.1
Release:        0
Summary:        Java manipulation of XML
License:        Saxpath
Group:          Development/Libraries/Java
URL:            http://www.jdom.org/
Source0:        jdom-%{version}.tar.xz
Patch0:         0001-Adapt-build.patch
BuildRequires:  ant
BuildRequires:  ant-junit
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local
BuildArch:      noarch

%description
JDOM is a Java-oriented object model which models XML documents.
It provides a Java-centric means of generating and manipulating
XML documents. While JDOM inter-operates well with existing
standards such as the Simple API for XML (SAX) and the Document
Object Model (DOM), it is not an abstraction layer or
enhancement to those APIs. Rather, it provides a means of
reading and writing XML data.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n jdom-%{version}

%patch0 -p1

sed -i 's/\r//' LICENSE.txt

# Unable to run coverage: use log4j12 but switch to log4j 2.x
sed -i.coverage "s|coverage, jars|jars|" build.xml

# XPath functionality is not needed
rm -rf core/src/java/org/jdom2/xpath/
sed -i '/import org.jdom2.xpath.XPathFactory/d' core/src/java/org/jdom2/JDOMConstants.java

%build
mkdir -p lib
%{ant} -Dversion=%{version} -Dcompile.target=8 -Dcompile.source=8 -Dj2se.apidoc=%{_javadocdir}/java maven

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}/%{name}
install -pm 0644 build/package/jdom-%{version}.jar %{buildroot}%{_javadir}/%{name}/%{name}.jar
# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}
install -pm 0644 build/maven/core/%{name}-%{version}.pom %{buildroot}%{_mavenpomdir}/%{name}/%{name}.pom
%add_maven_depmap %{name}/%{name}.pom %{name}/%{name}.jar
# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr build/apidocs/* %{buildroot}%{_javadocdir}/%{name}/
%fdupes %{buildroot}%{_javadocdir}

%files -f .mfiles
%doc CHANGES.txt COMMITTERS.txt README.md TODO.txt
%license LICENSE.txt

%files javadoc
%{_javadocdir}/%{name}

%changelog
