#
# spec file for package wsdl4j
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


Name:           wsdl4j
Version:        1.6.3
Release:        0
Summary:        Web Services Description Language Toolkit for Java
License:        IPL-1.0
Group:          Development/Libraries/Java
Url:            http://sourceforge.net/projects/wsdl4j
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-src-%{version}.zip
Source1:        %{name}-MANIFEST.MF
Source2:        http://repo1.maven.org/maven2/wsdl4j/wsdl4j/%{version}/wsdl4j-%{version}.pom
BuildRequires:  ant-junit
BuildRequires:  javapackages-local
BuildRequires:  javapackages-tools
BuildRequires:  unzip
BuildRequires:  xml-commons-apis
BuildRequires:  zip
Requires:       java
Requires:       jaxp_parser_impl
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
The Web Services Description Language for Java Toolkit (WSDL4J) allows
the creation, representation, and manipulation of WSDL documents
describing services.  This codebase will eventually serve as a
reference implementation of the standard created by JSR110.

%package javadoc
Summary:        Javadoc for wsdl4j
Group:          Development/Libraries/Java

%description javadoc
The Web Services Description Language for Java Toolkit (WSDL4J) allows
the creation, representation, and manipulation of WSDL documents
describing services.  This codebase will eventually serve as a
reference implementation of the standard created by JSR110.

This package contains the javadoc documentation for the Web Services
Description Language for Java.

%prep
%setup -q -n %{name}-1_6_3

%build
ant -Dant.build.javac.source=1.6 -Dant.build.javac.target=1.6 compile javadocs

%install
# inject OSGi manifests
mkdir -p META-INF
cp -p %{SOURCE1} META-INF/MANIFEST.MF
touch META-INF/MANIFEST.MF
zip -u build/lib/%{name}.jar META-INF/MANIFEST.MF

# jars
install -d -m 0755 %{buildroot}%{_javadir}
install -m 644 build/lib/%{name}.jar %{buildroot}%{_javadir}/%{name}.jar
install -m 644 build/lib/qname.jar %{buildroot}%{_javadir}/qname.jar

# POMs
install -d -m 0755 %{buildroot}%{_mavenpomdir}
install -p -m 0644 %{SOURCE2} %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr build/javadocs/* %{buildroot}%{_javadocdir}/%{name}

install -d -m 755 %{buildroot}%{_javadir}/javax.wsdl/
ln -sf ../%{name}.jar %{buildroot}%{_javadir}/javax.wsdl/
ln -sf ../qname.jar %{buildroot}%{_javadir}/javax.wsdl/

%files
%defattr(0644,root,root,0755)
%doc license.html
%{_mavenpomdir}/JPP-%{name}.pom
%{_datadir}/maven-metadata/%{name}.xml*
%{_javadir}/*

%files javadoc
%defattr(0644,root,root,0755)
%{_javadocdir}/%{name}

%changelog
