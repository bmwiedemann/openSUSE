#
# spec file for package dom4j
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           dom4j
Version:        1.6.1
Release:        0
Summary:        JarJar of dom4j for JBoss
License:        Apache-1.1
Group:          Development/Libraries/Java
Url:            http://www.dom4j.org/
#Source0:        dom4j-1.6.1.tar.gz
# Debian sources don't need a proprietary msv for build, so that's why I used them
# svn co svn://svn.debian.org/svn/pkg-java/trunk/dom4j
# rm dom4j/docs/xref/org/dom4j/tree/ConcurrentReaderHashMap.html
# rm dom4j/docs/clover/org/dom4j/tree/ConcurrentReaderHashMap.html
# #bnc501764
# rm dom4j/lib/tools/clover.license
# tar --exclude-vcs -cjf dom4j-1.6.1-debian.tar.bz2 dom4j/
Source0:        dom4j-1.6.1-debian.tar.bz2
Source1:        dom4j_rundemo.sh
Source2:        http://repo1.maven.org/maven2/dom4j/dom4j/1.6.1/dom4j-1.6.1.pom
Patch0:         dom4j-1.6.1-bug1618750.patch
Patch1:         dom4j-sourcetarget.patch
Patch2:         dom4j-javadoc.patch
# PATCH-FIX-UPSTREAM bsc#1105443 CVE-2018-1000632
Patch3:         dom4j-CVE-2018-1000632.patch
# PATCH-FIX-OPENSUSE bsc#1123158 Don't disable STAX and datatypes
Patch4:         dom4j-enable-stax-datatypes.patch
BuildRequires:  ant >= 1.6.5
BuildRequires:  ant-apache-resolver
BuildRequires:  ant-junit
BuildRequires:  bea-stax
BuildRequires:  fdupes
BuildRequires:  isorelax
BuildRequires:  java-devel >= 1.6
# Needed for maven conversions
BuildRequires:  javapackages-local
BuildRequires:  javapackages-tools
BuildRequires:  jaxen-bootstrap >= 1.1
BuildRequires:  jtidy
BuildRequires:  junit
BuildRequires:  junitperf
BuildRequires:  relaxngDatatype
BuildRequires:  stax_1_0_api
BuildRequires:  ws-jaxme
BuildRequires:  xalan-j2 >= 2.7
BuildRequires:  xerces-j2
BuildRequires:  xpp2
BuildRequires:  xpp3
Requires:       bea-stax
Requires:       isorelax
Requires:       java >= 1.6.0
Requires:       jaxen >= 1.1
Requires:       relaxngDatatype
Requires:       stax_1_0_api
Requires:       ws-jaxme
Requires:       xalan-j2
Requires:       xerces-j2
Requires:       xpp2
Requires:       xpp3
#Requires:       jaxp = 1.2
Requires(post): javapackages-tools
Requires(postun): javapackages-tools
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
dom4j is an easy to use Open Source XML, XPath and XSLT framework for
Java using the Java Collections Framework. dom4j allows you to read,
write, navigate, create and modify XML documents. dom4j integrates with
DOM, SAX and JAXP and is seamlessly integrated with full XPath support.

%package demo
Summary:        XML, XPath and XSLT library for Java
Group:          Development/Libraries/Java
Requires:       %{name} = %{version}

%description demo
dom4j is an easy to use Open Source XML, XPath and XSLT framework for
Java using the Java Collections Framework. dom4j allows you to read,
write, navigate, create and modify XML documents. dom4j integrates with
DOM, SAX and JAXP and is seamlessly integrated with full XPath support.

%package manual
Summary:        JarJar of dom4j for JBoss
Group:          Development/Libraries/Java

%description manual
dom4j is an easy to use Open Source XML, XPath and XSLT framework for
Java using the Java Collections Framework. dom4j allows you to read,
write, navigate, create and modify XML documents. dom4j integrates with
DOM, SAX and JAXP and is seamlessly integrated with full XPath support.

%package javadoc
Summary:        XML, XPath and XSLT library for Java
Group:          Development/Libraries/Java

%description javadoc
dom4j is an easy to use Open Source XML, XPath and XSLT framework for
Java using the Java Collections Framework. dom4j allows you to read,
write, navigate, create and modify XML documents. dom4j integrates with
DOM, SAX and JAXP and is seamlessly integrated with full XPath support.

%prep
%setup -q -n %{name}
# replace run.sh
cp %{SOURCE1} run.sh
rm -f src/test/org/dom4j/xpath/MatrixConcatTest.java
# won't succeed in headless environment
rm src/test/org/dom4j/bean/BeansTest.java
# FIXME Bug in Xalan 2.6 -- reactivate with Xalan 2.7
#rm src/test/org/dom4j/XPathExamplesTest.java
# fix for deleted jars
sed -i -e '/unjar/d' -e 's|,cookbook/\*\*,|,|' build.xml
# FIXME: (yyang): failed in JDK6
rm -f src/test/org/dom4j/ThreadingTest.java
# FIXME: (yyang): failed in JDK6, maybe failed to load russArticle.xml because it's russian encoding
rm -f src/test/org/dom4j/io/StaxTest.java
%patch0 -p1 -b .bug1618750
%patch1 -p1 -b .sourcetarget
%patch2 -p1 -b .javadoc
%patch3 -p1
%patch4 -p1
perl -pi -e 's/\r//g' LICENSE.txt docs/clover/*.css docs/style/*.css docs/xref/*.css docs/xref-test/*.css src/doc/style/*.css docs/benchmarks/xpath/*.java

pushd lib
ln -sf $(build-classpath xpp2)
ln -sf $(build-classpath relaxngDatatype)
ln -sf $(build-classpath jaxme/jaxmeapi)
#ln -sf $(build-classpath msv-xsdlib)
#ln -sf $(build-classpath msv-msv)
ln -sf $(build-classpath jaxen)
ln -sf $(build-classpath bea-stax-api)
pushd test
ln -sf $(build-classpath bea-stax-ri)
ln -sf $(build-classpath junitperf)
ln -sf $(build-classpath junit)
popd
ln -sf $(build-classpath xpp3)
pushd tools
ln -sf $(build-classpath jaxme/jaxmexs)
ln -sf $(build-classpath xalan-j2)
ln -sf $(build-classpath xalan-j2-serializer)
ln -sf $(build-classpath jaxme/jaxmejs)
ln -sf $(build-classpath jtidy)
ln -sf $(build-classpath isorelax)
ln -sf $(build-classpath jaxme/jaxme2)
ln -sf $(build-classpath xerces-j2)
popd
popd

%build
export CLASSPATH=$(build-classpath jaxen relaxngDatatype xpp3 xpp2)
export OPT_JAR_LIST="junit ant/ant-junit"
rm -rf src/java/org/dom4j/datatype
ant package release-javadoc

%install
# jars
install -d -m 755 %{buildroot}%{_javadir}
install -d -m 755 %{buildroot}%{_datadir}/maven2/poms
cp -p build/%{name}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

mkdir -p %{buildroot}/%{_mavenpomdir}
install -m 644 %{SOURCE2} %{buildroot}/%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap

# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr build/doc/javadoc/* %{buildroot}%{_javadocdir}/%{name}
# manual
mkdir -p %{buildroot}%{_docdir}/%{name}-%{version}
rm -rf docs/apidocs
cp -pr docs/* %{buildroot}%{_docdir}/%{name}-%{version}
# demo
mkdir -p %{buildroot}%{_datadir}/%{name}/classes/org/dom4j
cp -pr xml %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_datadir}/%{name}/src
cp -pr src/samples %{buildroot}%{_datadir}/%{name}/src
#cp -pr build/classes/org/dom4j/samples $RPM_BUILD_ROOT%%{_datadir}/%%{name}/classes/org/dom4j
install -m 0755 run.sh %{buildroot}%{_datadir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_docdir}/%{name}-%{version}
%fdupes -s %{buildroot}%{_datadir}/%{name}

%files
%defattr(0644,root,root,0755)
%doc LICENSE.txt
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-%{version}.jar
%{_mavenpomdir}/*
%{_datadir}/maven-metadata/%{name}.xml*

%files javadoc
%defattr(0644,root,root,0755)
%{_javadocdir}/%{name}

%files manual
%defattr(0644,root,root,0755)
%{_docdir}/%{name}-%{version}

%files demo
%defattr(-,root,root,0755)
%{_datadir}/%{name}

%changelog
