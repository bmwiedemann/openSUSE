#
# spec file for package jdom
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


%define xom_version   1.2b1
%define xom_suffix    %{nil}
%define xom_dir       %{_builddir}/%{name}-%{jdom_version}/XOM
%define xom_included_jaxen_archive jaxen-1.1-src.zip
%define jdom_version      1.1.3
%define jdom_suffix     %{nil}
%define dom4j_version   1.6.1
%define dom4j_suffix    %{nil}
%define dom4j_dir       %{_builddir}/%{name}-%{jdom_version}/dom4j
%define saxpath_version   1.0
%define saxpath_suffix  -FCS
%define saxpath_dir     %{_builddir}/%{name}-%{jdom_version}/saxpath-%{saxpath_version}%{saxpath_suffix}
%define jaxen_version   1.1.1
%define jaxen_suffix    %{nil}
%define jaxen_dir       %{_builddir}/%{name}-%{jdom_version}/jaxen-%{jaxen_version}
%define jdom_dir        %{_builddir}/%{name}-%{jdom_version}/%{name}
%define stage1_build_dir %{_builddir}/build
Name:           jdom
Version:        1.1.3
Release:        0
Summary:        JDOM is a Java Representation of an XML Document
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            http://www.jdom.org
Source0:        http://jdom.org/dist/binary/archive/%{name}-%{version}.tar.gz
Source1:        saxpath-%{saxpath_version}.tar.bz2
Source2:        xom-%{xom_version}-src.tar.bz2
# svn co svn://svn.debian.org/svn/pkg-java/trunk/dom4j
# rm dom4j/docs/xref/org/dom4j/tree/ConcurrentReaderHashMap.html
# rm dom4j/docs/clover/org/dom4j/tree/ConcurrentReaderHashMap.html
# #bnc501764
# rm dom4j/lib/tools/clover.license
# tar --exclude-vcs -cjf dom4j-1.6.1-debian.tar.bz2 dom4j/
Source3:        dom4j-%{dom4j_version}-debian.tar.bz2
Source4:        jaxen-%{jaxen_version}-src.tar.bz2
Source10:       http://repo.maven.apache.org/maven2/org/%{name}/%{name}/%{jdom_version}%{jdom_suffix}/%{name}-%{jdom_version}%{jdom_suffix}.pom
Source11:       http://repo.maven.apache.org/maven2/saxpath/saxpath/%{saxpath_version}%{saxpath_suffix}/saxpath-%{saxpath_version}%{saxpath_suffix}.pom
Source12:       http://repo.maven.apache.org/maven2/xom/xom/1.2.5/xom-1.2.5.pom
Source13:       http://repo.maven.apache.org/maven2/jaxen/jaxen/%{jaxen_version}%{jaxen_suffix}/jaxen-%{jaxen_version}%{jaxen_suffix}.pom
Patch0:         jdom-1.1-build.xml.patch
Patch1:         jdom-1.1-OSGiManifest.patch
Patch2:         jdom-1.1-xom-get-jaxen.patch
BuildRequires:  ant
BuildRequires:  ant-junit
BuildRequires:  java-devel
BuildRequires:  javapackages-local
BuildRequires:  junit
BuildRequires:  relaxngDatatype
BuildRequires:  servletapi5
BuildRequires:  unzip
BuildRequires:  xalan-j2
BuildRequires:  xerces-j2
BuildRequires:  xpp2
BuildRequires:  xpp3
BuildArch:      noarch

%description
JDOM is, quite simply, a Java representation of an XML document. JDOM
provides a way to represent that document for easy and efficient
reading, manipulation, and writing. It has a straightforward API, is
lightweight and fast, and is optimized for the Java programmer. It is
an alternative to DOM and SAX, although it integrates well with both
DOM and SAX.

%package -n   saxpath
Version:        1.0_FCS
Release:        0
Summary:        SAXPath is an event-based API for XPath parsers
License:        Apache-2.0
Group:          Development/Libraries/Java

%description -n saxpath
SAXPath is an event-based API for XPath parsers, that is, for parsers
which parse XPath  expressions. SAXPath is intended to be for XPath
what SAX is for XML. Note that the SAXPath package only parses XPath
expressions; it does not evaluate them, or even provide an object
structure for representing them once they have been parsed.

%package -n   xom
Version:        1.2b1
Release:        0
Summary:        XOM is a new XML object model
License:        LGPL-2.1-or-later
Group:          Development/Languages/Java

%description -n xom
XOM is designed to be easy to learn and easy to use. It works very
straight-forwardly, and has a very shallow learning curve. Assuming
you're already familiar with XML, you should be able to get up and
running with XOM very quickly.

XOM is the only XML API that makes no compromises on correctness. XOM
only accepts namespace well-formed XML documents, and only allows you
to create namespace well-formed XML documents. (In fact, it's a little
stricter than that: it actually guarantees that all documents are
round-trippable and have well-defined XML infosets.) XOM manages your
XML so you don't have to. With XOM, you can focus on the unique value
of your application, and trust XOM to get the XML right.

XOM is fairly unique in that it is a dual streaming/tree-based API.
Individual nodes in the tree can be processed while the document is
still being built. The enables XOM programs to operate almost as fast
as the underlying parser can supply data. You don't need to wait for
the document to be completely parsed before you can start working with
it.

XOM is very memory efficient. If you read an entire document into
memory, XOM uses as little memory as possible. More importantly, XOM
allows you to filter documents as they're built so you don't have to
build the parts of the tree you aren't interested in. For instance, you
can skip building text nodes that only represent boundary white space,
if such white space is not significant in your application. You can
even process a document piece by piece and throw away each piece when
you're done with it. XOM has been used to process documents that are
gigabytes in size.

XOM includes built-in support for a number of XML technologies
including Namespaces in XML, XPath, XSLT, XInclude, xml:id, and
Canonical XML. XOM documents can be converted to and from SAX and DOM.

%package -n   jaxen
Version:        1.1.1
Release:        0
Summary:        The jaxen project is a Java XPath Engine
License:        Apache-2.0
Group:          Development/Libraries/Java
Provides:       jaxen-bootstrap = %{version}
Obsoletes:      jaxen-bootstrap < %{version}

%description -n jaxen
Jaxen is a universal object model walker, capable of evaluating XPath
expressions across multiple models. Currently supported are dom4j,
JDOM, and DOM.

%prep
%setup -q -c foo -a 1 -a 2 -a 3 -a 4
rm %{xom_dir}/%{xom_included_jaxen_archive}
mkdir %{stage1_build_dir}
# delete all inlcuded jar files:
find . -name "*.jar" -delete -name "*.class" -delete
%patch0
%patch1
%patch2
cp %{SOURCE10} %{name}-%{jdom_version}.pom
cp %{SOURCE11} saxpath-%{saxpath_version}.pom
cp %{SOURCE12} xom-%{xom_version}.pom
cp %{SOURCE13} jaxen-%{jaxen_version}.pom

%pom_xpath_set pom:project/pom:version "%{xom_version}%{xom_suffix}" xom-%{xom_version}.pom

%build
export JAVA_OPTS="-source 1.6 -target 1.6 -encoding UTF-8 -J-Xss4m"
export JAVAC="javac ${JAVA_OPTS} "
export ANT_OPTS="-Xss4m"
i=0
CLASSPATH="%{stage1_build_dir}:$(build-classpath xerces-j2 xalan-j2 xalan-j2-serializer junit relaxngDatatype servletapi5 xpp2 xpp3)"
SOURCE_DIRS="%{jaxen_dir}/src/java/main/ %{jdom_dir}/src/java/ %{saxpath_dir}/src/java/main/ %{xom_dir}/src/ %{dom4j_dir}/src/java"
SOURCE_PATH=$(echo ${SOURCE_DIRS} | sed 's#\ #:#g')
# Failing files
rm -f \
	XOM/src/nu/xom/tools/XHTMLJavaDoc.java \
	dom4j/src/java/org/dom4j/datatype/SchemaParser.java \
	dom4j/src/java/org/dom4j/datatype/DatatypeAttribute.java \
	dom4j/src/java/org/dom4j/datatype/DatatypeElement.java \
	dom4j/src/java/org/dom4j/datatype/NamedTypeResolver.java \
	dom4j/src/java/org/dom4j/datatype/DatatypeDocumentFactory.java \
	dom4j/src/java/org/dom4j/datatype/DatatypeElementFactory.java \
	dom4j/src/java/org/jaxen/dom4j/DocumentNavigator.java \
	dom4j/src/java/org/jaxen/dom4j/Dom4jXPath.java
${JAVAC} -classpath ${CLASSPATH} -sourcepath ${SOURCE_PATH} -d %{stage1_build_dir} $(find ${SOURCE_DIRS} -name "*.java" | xargs)
unset CLASSPATH SOURCE_DIRS SOURCE_PATH
jar cf %{jdom_dir}/jaxen.jar -C %{stage1_build_dir} .

pushd %{jdom_dir}
ant -Dparser.jar=$(build-classpath xerces-j2) \
    -Dxml-apis.jar=$(build-classpath xml-commons-apis) \
    -Djaxen.lib.dir=%{jdom_dir} \
    -Dcompile.source=1.6 -Dcompile.target=1.6 \
	-Dversion=%jdom_version \
    package
mv build/jdom-%{jdom_version}.jar %{_builddir}/jdom-%{jdom_version}.jar
rm jaxen.jar
popd
pushd %{jaxen_dir}/src/java/main
mkdir build
#mkdir %{_builddir}/jaxen-excluded
#mv org/jaxen/dom4j %{_builddir}/jaxen-excluded
${JAVAC} -classpath %{_builddir}/jdom-%{jdom_version}.jar:%{stage1_build_dir} -d build/ $(find . -name "*.java" | xargs)
jar -cf %{_builddir}/jaxen-%{jaxen_version}.jar -C build .
popd
pushd %{saxpath_dir}
mkdir src/conf
touch src/conf/MANIFEST.MF
CLASSPATH=%{_builddir}/jaxen-%{jaxen_version}.jar:%{_builddir}/jdom-%{jdom_version}.jar:%{stage1_build_dir} ant package
mv build/saxpath.jar %{_builddir}/saxpath-%{saxpath_version}.jar
popd
pushd %{xom_dir}
ant \
-Djaxen.dir=%{stage1_build_dir} \
-Dxml-apis.jar=$(build-classpath xml-commons-apis) \
-Dparser.jar=$(build-classpath xerces-j2) \
-Dxslt.jar=$(build-classpath xalan-j2) \
-Dserializer.jar=$(build-classpath xalan-j2-serializer) \
-Djunit.jar=$(build-classpath junit) \
-Dresolver.jar=$(build-classpath xml-commons-resolver) \
-Ddom4j.jar=%{stage1_build_dir} \
-Dant.build.javac.source=1.6 -Dant.build.javac.target=1.6 \
compile compile15 jar
mv build/xom-%{xom_version}.jar %{_builddir}
popd
#<<< build

%install
mkdir -p %{buildroot}/%{_javadir}
mv %{_builddir}/*.jar %{buildroot}/%{_javadir}
ln -sf %{_javadir}/jdom-%{jdom_version}.jar %{buildroot}/%{_javadir}/jdom.jar
ln -sf %{_javadir}/jaxen-%{jaxen_version}.jar %{buildroot}/%{_javadir}/jaxen.jar
ln -sf %{_javadir}/saxpath-%{saxpath_version}.jar %{buildroot}/%{_javadir}/saxpath.jar
ln -sf %{_javadir}/xom-%{xom_version}.jar %{buildroot}/%{_javadir}/xom.jar

mkdir -p %{buildroot}/%{_mavenpomdir}
cp *.pom %{buildroot}/%{_mavenpomdir}/
%add_maven_depmap jdom-%{jdom_version}.pom jdom-%{jdom_version}.jar -a jdom:jdom
%add_maven_depmap xom-%{xom_version}.pom xom-%{xom_version}.jar -f xom
%add_maven_depmap saxpath-%{saxpath_version}.pom saxpath-%{saxpath_version}.jar -f saxpath
%add_maven_depmap jaxen-%{jaxen_version}.pom jaxen-%{jaxen_version}.jar -f jaxen

%files
%{_javadir}/jdom*.jar
%{_mavenpomdir}/jdom*.pom
%if %{defined _maven_repository}
%{_mavendepmapfragdir}/%{name}
%else
%{_datadir}/maven-metadata/%{name}.xml*
%endif

%files -n xom
%{_javadir}/xom*.jar
%{_mavenpomdir}/xom*.pom
%if %{defined _maven_repository}
%{_mavendepmapfragdir}/%{name}-xom
%else
%{_datadir}/maven-metadata/%{name}-xom.xml*
%endif

%files -n saxpath
%{_javadir}/saxpath*.jar
%{_mavenpomdir}/saxpath*.pom
%if %{defined _maven_repository}
%{_mavendepmapfragdir}/%{name}-saxpath
%else
%{_datadir}/maven-metadata/%{name}-saxpath.xml*
%endif

%files -n jaxen
%{_javadir}/jaxen*.jar
%{_mavenpomdir}/jaxen*.pom
%if %{defined _maven_repository}
%{_mavendepmapfragdir}/%{name}-jaxen
%else
%{_datadir}/maven-metadata/%{name}-jaxen.xml*
%endif

%changelog
