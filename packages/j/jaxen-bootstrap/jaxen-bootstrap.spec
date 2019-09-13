#
# spec file for package jaxen-bootstrap
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


%define with_maven 0
%define real    jaxen
%define dom4jver   1.6.1
%define section free

Name:           jaxen-bootstrap
Version:        1.1
Release:        0
Summary:        A convenience package for build of dom4j
License:        Apache-2.0
Group:          Development/Libraries/Java
Url:            http://jaxen.codehaus.org/
Source0:        http://dist.codehaus.org/jaxen/distributions/jaxen-1.1-src.tar.bz2
Source1:        pom-maven2jpp-depcat.xsl
Source2:        pom-maven2jpp-newdepmap.xsl
Source3:        pom-maven2jpp-mapdeps.xsl
Source4:        jaxen-1.1-b7-jpp-depmap.xml
# Debian sources don't need a proprietary msv for build, so that's why I used them
# svn co svn://svn.debian.org/svn/pkg-java/trunk/dom4j
# rm dom4j/docs/xref/org/dom4j/tree/ConcurrentReaderHashMap.html
# rm dom4j/docs/clover/org/dom4j/tree/ConcurrentReaderHashMap.html
# #bnc501764
# rm dom4j/lib/tools/clover.license
# tar --exclude-vcs -cjf dom4j-1.6.1-debian.tar.bz2 dom4j/
Source5:        http://prdownloads.sourceforge.net/dom4j/dom4j-%{dom4jver}-debian.tar.bz2
Source6:        jaxen-1.1-b7-build.xml
Patch0:         jaxen-bootstrap-project_xml.patch
Requires:       xalan-j2
Requires:       xerces-j2
Requires:       xom
BuildRequires:  ant >= 1.6
BuildRequires:  javapackages-tools
BuildRequires:  junit
%if %{with_maven}
BuildRequires:  maven >= 1.1
BuildRequires:  maven-plugin-license
BuildRequires:  maven-plugin-test
BuildRequires:  maven-plugins-base
BuildRequires:  saxon
BuildRequires:  saxon-scripts
%endif
BuildRequires:  java-devel
BuildRequires:  unzip
BuildRequires:  xalan-j2
BuildRequires:  xerces-j2
BuildRequires:  xom
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Dom4j depends on a jaxen build with dom4j support. This package must
only be installed in the rare event of having to rebuild dom4j.



%prep
%setup -q -n %{real}-%{version}
tar -xf %{SOURCE5}
#/bin/gzip -dc %{SOURCE5} | tar -xf -
cp %{SOURCE6} build.xml
find . -name "*.jar" -exec rm -f {} \;
%patch0 -b .sav
%if %{with_maven}
export DEPCAT=$(pwd)/jaxen-1.1-b7-depcat.new.xml
echo '<?xml version="1.0" standalone="yes"?>' > $DEPCAT
echo '<depset>' >> $DEPCAT
for p in $(find . -name project.xml); do
    pushd $(dirname $p)
    /usr/bin/saxon project.xml %{SOURCE1} >> $DEPCAT
    popd
done
echo >> $DEPCAT
echo '</depset>' >> $DEPCAT
/usr/bin/saxon $DEPCAT %{SOURCE2} > jaxen-1.1-b7-depmap.new.xml
%endif
rm -rf src/java/main/org/jaxen/jdom
rm -rf src/java/test/org/jaxen/jdom
rm -f src/java/test/org/jaxen/test/JaxenTests.java
rm -f src/java/test/org/jaxen/test/JDOMNavigatorTest.java
rm -f src/java/test/org/jaxen/test/JDOMPerformance.java
rm -f src/java/test/org/jaxen/test/JDOMTests.java
rm -f src/java/test/org/jaxen/test/JDOMXPathTest.java

%build
export CLASSPATH=$(build-classpath \
xom \
jdom \
xalan-j2 \
xerces-j2 \
)
pushd dom4j/src/java
javac -sourcepath ../../../src/java/main:. \
        org/dom4j/Attribute.java \
        org/dom4j/Branch.java \
        org/dom4j/CDATA.java \
        org/dom4j/Comment.java \
        org/dom4j/Document.java \
        org/dom4j/DocumentException.java \
        org/dom4j/Element.java \
        org/dom4j/Namespace.java \
        org/dom4j/Node.java \
        org/dom4j/ProcessingInstruction.java \
        org/dom4j/Text.java \
        org/dom4j/io/SAXReader.java 
jar cf ../../dom4j.jar $(find . -name "*.class")
popd
mkdir -p .maven/repository/JPP/jars
cp dom4j/dom4j.jar .maven/repository/JPP/jars/dom4j.jar
%if %{with_maven}
for p in $(find . -name project.xml); do
    pushd $(dirname $p)
    cp project.xml project.xml.orig
    /usr/bin/saxon -o project.xml project.xml.orig %{SOURCE3} map=%{SOURCE4}
    popd
done
maven \
        -Dmaven.test.skip=true \
        -Dmaven.repo.remote=file:/usr/share/maven/repository \
        -Dmaven.home.local=$(pwd)/.maven \
        jar
%else
export CLASSPATH=$CLASSPATH:dom4j/dom4j.jar
ant -Dant.build.javac.source=1.6 -Dant.build.javac.target=1.6 \
    -Dbuild.sysclasspath=first
%endif

%install
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 target/%{real}-%{version}-beta-7.jar \
$RPM_BUILD_ROOT%{_javadir}/%{real}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do \
ln -sf ${jar} ${jar/-%{version}/}; done)

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(0644,root,root,0755)
%{_javadir}/*

%changelog
