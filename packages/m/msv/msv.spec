#
# spec file for package msv
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


Name:           msv
Version:        2013.6.1
Release:        0
Summary:        Multi-Schema Validator
License:        BSD-3-Clause AND Apache-1.1
Group:          Development/Libraries/Java
URL:            http://msv.java.net/
# To generate tarball from upstream source control:
# $ ./create-tarball
Source0:        %{name}-%{version}-clean.tar.gz
Source2:        http://www.apache.org/licenses/LICENSE-2.0.txt
Source3:        create-tarball.sh
# Use CatalogResolver from xml-commons-resolver package
Patch1:         %{name}-Use-CatalogResolver-class-from-xml-commons-resolver.patch
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(isorelax:isorelax)
BuildRequires:  mvn(net.java:jvnet-parent:pom:)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(relaxngDatatype:relaxngDatatype)
BuildRequires:  mvn(xerces:xercesImpl)
BuildRequires:  mvn(xml-resolver:xml-resolver)
Obsoletes:      %{name}-relames < %{version}-%{release}
BuildArch:      noarch

%description
The Sun Multi-Schema XML Validator (MSV) is a Java technology tool to validate
XML documents against several kinds of XML schemata. It supports RELAX NG,
RELAX Namespace, RELAX Core, TREX, XML DTDs, and a subset of XML Schema Part 1.
This latest (version 1.2) release includes several bug fixes and adds better
conformance to RELAX NG/W3C XML standards and JAXP masquerading.

%package msv
Summary:        Multi-Schema Validator Core
# src/com/sun/msv/reader/xmlschema/DOMLSInputImpl.java is under ASL 2.0
# msv/src/com/sun/msv/writer/ContentHandlerAdaptor.java is partially under Public Domain
# Explicit javapackages-tools requires since scripts use
# /usr/share/java-utils/java-functions
License:        BSD-3-Clause AND Apache-1.1 AND Apache-2.0 AND SUSE-Public-Domain
Group:          Development/Libraries/Java
Requires:       javapackages-tools

%description msv
%{summary}.

%package rngconv
Summary:        Multi-Schema Validator RNG Converter
# Explicit javapackages-tools requires since scripts use
# /usr/share/java-utils/java-functions
License:        BSD-3-Clause AND Apache-1.1
Group:          Development/Libraries/Java
Requires:       javapackages-tools

%description rngconv
%{summary}.

%package xmlgen
Summary:        Multi-Schema Validator Generator
# Explicit javapackages-tools requires since scripts use
# /usr/share/java-utils/java-functions
License:        BSD-3-Clause AND Apache-1.1
Group:          Development/Libraries/Java
Requires:       javapackages-tools

%description xmlgen
%{summary}.

%package xsdlib
Summary:        Multi-Schema Validator XML Schema Library
License:        BSD-3-Clause AND Apache-1.1
Group:          Development/Libraries/Java

%description xsdlib
%{summary}.

%package javadoc
Summary:        API documentation for Multi-Schema Validator
License:        BSD-3-Clause AND Apache-1.1 AND Apache-2.0 AND SUSE-Public-Domain
Group:          Documentation/HTML

%description javadoc
%{summary}.

%package manual
Summary:        Manual for Multi-Schema Validator
License:        BSD-3-Clause
Group:          Documentation/HTML

%description manual
%{summary}.

%package demo
Summary:        Samples for Multi-Schema Validator
License:        BSD-3-Clause
Group:          Development/Libraries/Java
Requires:       msv-msv
Requires:       msv-xsdlib

%description demo
%{summary}.

%prep
%setup -q

%pom_remove_plugin :buildnumber-maven-plugin

# Apply patches
%patch1 -p1
# Needed becuase of patch
%pom_add_dep xml-resolver:xml-resolver

# ASL 2.0 license text
cp %{SOURCE2} Apache-LICENSE-2.0.txt

# Delete anything pre-compiled
find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;
find -name '*.zip' -exec rm -f '{}' \;

# Test sources in default package break BND
rm -f testharness/src/*.java

# Delete class-path entries from manifests
for m in $(find . -name MANIFEST.MF) ; do
  sed --in-place -e '/^[Cc]lass-[Pp]ath:/d' $m
done

# Fix isorelax groupId
%pom_xpath_replace "pom:dependency[pom:groupId[text()='com.sun.xml.bind.jaxb']]/pom:groupId" "<groupId>isorelax</groupId>"
%pom_xpath_replace "pom:dependency[pom:groupId[text()='com.sun.xml.bind.jaxb']]/pom:groupId" "<groupId>isorelax</groupId>" msv

#
%pom_remove_plugin :maven-enforcer-plugin

# Change encoding of non utf-8 files
for m in $(find . -name copyright.txt) ; do
  iconv -f iso-8859-1 -t utf-8 < $m > $m.utf8
  mv $m.utf8 $m
done

%{mvn_file} ":%{name}-core" %{name}-core %{name}-%{name}
%{mvn_file} ":%{name}-rngconverter" %{name}-rngconverter %{name}-rngconv
%{mvn_file} ":%{name}-generator" %{name}-generator %{name}-xmlgen
%{mvn_file} ":xsdlib" xsdlib %{name}-xsdlib

%{mvn_alias} ":xsdlib" "com.sun.msv.datatype.xsd:xsdlib"

%{mvn_package} ":*::{tests,javadoc,sources}:" __noinstall
%{mvn_package} ":%{name}{,-testharness}::{}:" __noinstall
%{mvn_package} ":%{name}{,-core}::{}:" %{name}-msv

%build
%{mvn_build} -s -f \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
	-- -Dmaven.compiler.release=6
%endif

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

# Manuals
install -d -m 755 %{buildroot}%{_docdir}/%{name}/msv
install -m 644 msv/doc/*.html     %{buildroot}%{_docdir}/%{name}/msv
install -m 644 msv/doc/*.gif      %{buildroot}%{_docdir}/%{name}/msv
install -m 644 msv/doc/README.txt %{buildroot}%{_docdir}/%{name}/msv

install -d -m 755 %{buildroot}%{_docdir}/%{name}/rngconverter
install -m 644 rngconverter/README.txt %{buildroot}%{_docdir}/%{name}/rngconverter

install -d -m 755 %{buildroot}%{_docdir}/%{name}/generator
install -m 644 generator/*.html     %{buildroot}%{_docdir}/%{name}/generator
install -m 644 generator/README.txt %{buildroot}%{_docdir}/%{name}/generator

install -d -m 755 %{buildroot}%{_docdir}/%{name}/xsdlib
install -m 644 xsdlib/*.html     %{buildroot}%{_docdir}/%{name}/xsdlib
install -m 644 xsdlib/README.txt %{buildroot}%{_docdir}/%{name}/xsdlib
%fdupes -s %{buildroot}%{_docdir}

# Examples
install -d -m 755 %{buildroot}%{_datadir}/%{name}/msv
cp -pr msv/examples/* %{buildroot}%{_datadir}/%{name}/msv
install -d -m 755 %{buildroot}%{_datadir}/%{name}/xsdlib
cp -pr xsdlib/examples/* %{buildroot}%{_datadir}/%{name}/xsdlib

# Scripts
%jpackage_script com.sun.msv.driver.textui.Driver "" "" msv-msv:msv-xsdlib:relaxngDatatype:isorelax msv true
%jpackage_script com.sun.msv.generator.Driver "" "" msv-xmlgen:msv-msv:msv-xsdlib:relaxngDatatype:isorelax:xerces-j2 xmlgen true
%jpackage_script com.sun.msv.writer.relaxng.Driver "" "" msv-rngconv:msv-msv:msv-xsdlib:relaxngDatatype:isorelax:xerces-j2 rngconv true

%files msv -f .mfiles-msv-msv
%{_bindir}/msv
%license License.txt
%doc msv/doc/Apache-LICENSE-1.1.txt
%doc Apache-LICENSE-2.0.txt

%files rngconv -f .mfiles-msv-rngconverter
%{_bindir}/rngconv
%doc msv/doc/Apache-LICENSE-1.1.txt
%license License.txt

%files xmlgen -f .mfiles-msv-generator
%{_bindir}/xmlgen
%doc msv/doc/Apache-LICENSE-1.1.txt
%license License.txt

%files xsdlib -f .mfiles-xsdlib
%doc msv/doc/Apache-LICENSE-1.1.txt
%license License.txt

%files javadoc -f .mfiles-javadoc
%license License.txt
%doc msv/doc/Apache-LICENSE-1.1.txt
%doc Apache-LICENSE-2.0.txt

%files manual
%doc %{_docdir}/%{name}
%license License.txt

%files demo
%{_datadir}/%{name}

%changelog
