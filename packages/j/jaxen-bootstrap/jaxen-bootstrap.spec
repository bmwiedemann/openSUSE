#
# spec file for package jaxen-bootstrap
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


%define real    jaxen
%define dom4jver   1.6.1
Name:           jaxen-bootstrap
Version:        1.1
Release:        0
Summary:        A convenience package for build of dom4j
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            http://jaxen.codehaus.org/
Source0:        http://dist.codehaus.org/jaxen/distributions/jaxen-1.1-src.tar.bz2
# Debian sources don't need a proprietary msv for build, so that's why I used them
# svn co svn://svn.debian.org/svn/pkg-java/trunk/dom4j
# rm dom4j/docs/xref/org/dom4j/tree/ConcurrentReaderHashMap.html
# rm dom4j/docs/clover/org/dom4j/tree/ConcurrentReaderHashMap.html
# bnc#501764
# rm dom4j/lib/tools/clover.license
# tar --exclude-vcs -cjf dom4j-1.6.1-debian.tar.bz2 dom4j/
Source1:        http://prdownloads.sourceforge.net/dom4j/dom4j-%{dom4jver}-debian.tar.bz2
Source2:        jaxen-1.1-b7-build.xml
BuildRequires:  ant >= 1.6
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-tools
BuildRequires:  unzip
BuildRequires:  xalan-j2
BuildRequires:  xerces-j2
BuildRequires:  xom
Requires:       xalan-j2
Requires:       xerces-j2
Requires:       xom
BuildArch:      noarch

%description
Dom4j depends on a jaxen build with dom4j support. This package must
only be installed in the rare event of having to rebuild dom4j.

%prep
%setup -q -n %{real}-%{version} -a1
cp %{SOURCE2} build.xml
find . -name "*.jar" -exec rm -f {} \;
rm -rf src/java/main/org/jaxen/jdom
rm -rf src/java/test/org/jaxen/jdom
rm -f src/java/test/org/jaxen/test/JaxenTests.java
rm -f src/java/test/org/jaxen/test/JDOMNavigatorTest.java
rm -f src/java/test/org/jaxen/test/JDOMPerformance.java
rm -f src/java/test/org/jaxen/test/JDOMTests.java
rm -f src/java/test/org/jaxen/test/JDOMXPathTest.java

%build
mkdir -p lib
build-jar-repository -s lib \
   xom \
   xalan-j2 \
   xerces-j2

mkdir -p dom4j/classes
javac \
	-source 8 -target 8 -d dom4j/classes \
	-sourcepath src/java/main:dom4j/src/java \
		dom4j/src/java/org/dom4j/Attribute.java \
		dom4j/src/java/org/dom4j/Branch.java \
		dom4j/src/java/org/dom4j/CDATA.java \
        dom4j/src/java/org/dom4j/Comment.java \
        dom4j/src/java/org/dom4j/Document.java \
        dom4j/src/java/org/dom4j/DocumentException.java \
        dom4j/src/java/org/dom4j/Element.java \
        dom4j/src/java/org/dom4j/Namespace.java \
        dom4j/src/java/org/dom4j/Node.java \
        dom4j/src/java/org/dom4j/ProcessingInstruction.java \
        dom4j/src/java/org/dom4j/Text.java \
        dom4j/src/java/org/dom4j/io/SAXReader.java

jar cf lib/dom4j.jar -C dom4j/classes .

%ant -Dant.build.javac.source=1.8 -Dant.build.javac.target=1.8

%install
# jars
install -d -m 755 %{buildroot}%{_javadir}
install -m 644 target/%{real}-%{version}-beta-7.jar %{buildroot}%{_javadir}/%{real}.jar

%files
%defattr(0644,root,root,0755)
%{_javadir}/*

%changelog
