#
# spec file for package jakarta-poi
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


%define base_name poi
Name:           jakarta-poi
Version:        2.5.1
Release:        0
Summary:        Java API To Access Microsoft Format Files
License:        Apache-2.0
Group:          Development/Languages/Java
Url:            http://jakarta.apache.org/poi/
Source0:        poi-src-2.5.1-final-20040804.tar.bz2
#cvs -d :pserver:anoncvs@cvs.apache.org:/home/cvspublic  login
#cvs -z3 -d :pserver:anoncvs@cvs.apache.org:/home/cvspublic export -r HEAD jakarta-poi/src/scratchpad
Source1:        poi-scratchpad-unreleased-src-20050824.tar.bz2
Patch0:         poi-build_xml.patch
Patch1:         poi-encoding.patch
Patch2:         %{name}-%{version}-junittest.patch
BuildRequires:  ant >= 1.6
BuildRequires:  ant-jdepend >= 1.6
BuildRequires:  ant-junit >= 1.6
BuildRequires:  fdupes
BuildRequires:  jakarta-commons-beanutils >= 1.6.1
BuildRequires:  jakarta-commons-collections >= 2.1
BuildRequires:  jakarta-commons-lang >= 2.0
BuildRequires:  jakarta-commons-logging >= 1.0.3
BuildRequires:  java-devel
BuildRequires:  javapackages-tools
BuildRequires:  jaxp_transform_impl
BuildRequires:  jdepend >= 2.6
BuildRequires:  junit >= 3.8.1
BuildRequires:  log4j12 >= 1.2.8
BuildRequires:  xalan-j2 >= 2.5.2
BuildRequires:  xerces-j2 >= 2.6.0
BuildRequires:  xml-commons-apis
Requires:       jakarta-commons-beanutils >= 1.6.1
Requires:       jakarta-commons-collections >= 2.1
Requires:       jakarta-commons-lang >= 2.0
Requires:       jakarta-commons-logging >= 1.0.3
Requires:       log4j12 >= 1.2.8
Requires:       xalan-j2 >= 2.5.2
Requires:       xerces-j2 >= 2.6.0
BuildArch:      noarch

%description
The POI project consists of APIs for manipulating various file formats
based upon Microsoft's OLE 2 Compound Document format using pure Java.
In short, you can read and write MS Excel files using Java. Soon,
you'll be able to read and write Word files using Java. POI is your
Java Excel solution as well as your Java Word solution. However, we
have a complete API for porting other OLE 2 Compound Document formats
and welcome others to participate. OLE 2 Compound Document Format based
files include most Microsoft Office files such as XLS and DOC as well
as MFC serialization API based file formats.

%package        javadoc
Summary:        Java API To Access Microsoft Format Files
Group:          Development/Languages/Java

%description    javadoc
The POI project consists of APIs for manipulating various file formats
based upon Microsoft's OLE 2 Compound Document format using pure Java.
In short, you can read and write MS Excel files using Java. Soon,
you'll be able to read and write Word files using Java. POI is your
Java Excel solution as well as your Java Word solution. However, we
have a complete API for porting other OLE 2 Compound Document formats
and welcome others to participate. OLE 2 Compound Document Format based
files include most Microsoft Office files such as XLS and DOC as well
as MFC serialization API based file formats.

%package        manual
Summary:        Java API To Access Microsoft Format Files
Group:          Development/Languages/Java

%description    manual
The POI project consists of APIs for manipulating various file formats
based upon Microsoft's OLE 2 Compound Document format using pure Java.
In short, you can read and write MS Excel files using Java. Soon,
you'll be able to read and write Word files using Java. POI is your
Java Excel solution as well as your Java Word solution. However, we
have a complete API for porting other OLE 2 Compound Document formats
and welcome others to participate. OLE 2 Compound Document Format based
files include most Microsoft Office files such as XLS and DOC as well
as MFC serialization API based file formats.

%prep
%setup -q -c -n %{base_name}
#find . -name "*.jar" -exec rm {} \;
find . -name "*.jar" -exec mv {} {}.no \;
bzip2 -dc %{SOURCE1} | tar xf -
rm -rf src/scratchpad/src/org/apache/poi/hslf/
rm -rf src/scratchpad/testcases/org/apache/poi/hslf/
# FIXME
rm src/testcases/org/apache/poi/hssf/usermodel/TestEscherGraphics*.java
rm src/testcases/org/apache/poi/hssf/HSSFTests.java
%patch0 -b .sav
%patch1 -b .sav1
%patch2 -b .sav2
# wrong end of line necoding
sed -i -e 's/.$//' \
        docs/jdepend/jdepend.xml \
        LICENSE \
        docs/skin/*.js \
        docs/skin/page.css \
        docs/changes.rss \
        docs/apidocs/package-list \
        docs/apidocs/stylesheet.css \
        docs/junit/stylesheet.css \
        docs/junit/TESTS-TestSuites.xml \
        docs/junit/org/apache/poi/hssf/usermodel/TestBugs*

%build
export OPT_JAR_LIST="ant/ant-junit junit ant/ant-jdepend jdepend jaxp_transform_impl ant/ant-trax"
export CLASSPATH=$(build-classpath \
commons-beanutils \
commons-collections \
commons-lang \
commons-logging \
log4j12/log4j-12 \
xalan-j2 \
xerces-j2 \
xml-commons-apis \
)
export ANT_OPTS="-Xmx256m -Djava.awt.headless=true -Dbuild.sysclasspath=first -Ddisconnected=true"
ant -Dant.build.javac.target=1.6 -Dant.build.javac.source=1.6 jar test

%install
install -dm 755 %{buildroot}%{_javadir}
cp -p build/dist/%{base_name}-%{version}-final-*.jar \
  %{buildroot}%{_javadir}/%{name}-%{version}.jar
cp -p build/dist/%{base_name}-contrib-%{version}-final-*.jar \
  %{buildroot}%{_javadir}/%{name}-contrib-%{version}.jar
cp -p build/dist/%{base_name}-scratchpad-%{version}-final-*.jar \
  %{buildroot}%{_javadir}/%{name}-scratchpad-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in %{name}*-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|jakarta-||g"`; done)
(cd %{buildroot}%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)
#javadoc
install -dm 755 %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr docs/apidocs/* %{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name} # ghost symlink
rm -rf docs/apidocs
#manual
install -dm 755 %{buildroot}%{_docdir}/%{name}-%{version}
cp -pr docs/* %{buildroot}%{_docdir}/%{name}-%{version}
cp -p LICENSE %{buildroot}%{_docdir}/%{name}-%{version}
ln -s %{_javadocdir}/%{name}-%{version} %{buildroot}%{_docdir}/%{name}-%{version}/apidocs # ghost symlink
%fdupes -s %{buildroot}

%files
%doc %{_docdir}/%{name}-%{version}/LICENSE
%{_javadir}/*.jar

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%ghost %doc %{_javadocdir}/%{name}

%files manual
%doc %{_docdir}/%{name}-%{version}
%exclude %{_docdir}/%{name}-%{version}/LICENSE

%changelog
