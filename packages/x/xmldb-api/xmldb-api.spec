#
# spec file for package xmldb-api
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


%define bname   xmldb
%define cvs_version 20041010
Name:           xmldb-api
Version:        0.1
Release:        0
Summary:        XML:DB API for Java
License:        Apache-1.1
Group:          Development/Libraries/Java
Url:            http://xmldb-org.sourceforge.net
# cvs -d:pserver:anonymous@cvs.sourceforge.net:/cvsroot/xmldb-org login
# cvs -z3 -d:pserver:anonymous@cvs.sourceforge.net:/cvsroot/xmldb-org export -D 2004-10-10 xapi
Source0:        xmldb-xapi-%{cvs_version}-src.tar.bz2
Patch0:         xmldb-api-java5-enum.patch
BuildRequires:  ant >= 1.6
BuildRequires:  javapackages-tools
BuildRequires:  junit
BuildRequires:  xalan-j2
Requires:       xalan-j2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
The API interfaces are what driver developers must implement when
creating a new driver, and are the interfaces that applications are
developed against. Along with the interfaces, a concrete DriverManager
implementation is also provided.

%package sdk
Summary:        SDK for XML:DB API
Group:          Development/Libraries/Java
Requires:       %{name} = %{version}

%description sdk
The reference implementation provides a very simple file system based
implementation of the XML:DB API. This provides what is basically a
native XML database that uses directories to represent
collections, and just stores the XML in files.

The driver development kit provides a set of base classes that can be
extended to simplify and speed the development of XML:DB API drivers.
These classes are used to provide the basis for the reference
implementation, and therefore a simple example of how a driver can be
implemented. Using the SDK classes significantly reduces the amount of
code that must be written to create a new driver.

Along with the SDK base classes, the SDK also contains a set of jUnit
test cases that can be used to help validate the driver while it is
being developed. The test cases are still in development but there are
enough tests currently to be useful.

%package -n xmldb-common
Summary:        XML:DB API for Java
Group:          Development/Libraries/Java
Requires:       %{name} = %{version}

%description -n xmldb-common
The API interfaces are what driver developers must implement when
creating a new driver, and are the interfaces that applications are
developed against. Along with the interfaces, a concrete DriverManager
implementation is also provided.

%package javadoc
Summary:        Documentation for XML:DB API for Java
Group:          Documentation/HTML

%description javadoc
The API interfaces are what driver developers must implement when
creating a new driver, and are the interfaces that applications are
developed against. Along with the interfaces, a concrete DriverManager
implementation is also provided.

%prep
%setup -q -n xapi
%patch0 -p1
find . -name "*.jar" | xargs -t rm
# FIXME: (dwalluck): These use org.apache.xalan.xpath
rm src/common/org/xmldb/common/xml/queries/xalan/XPathQueryImpl.java
rm src/common/org/xmldb/common/xml/queries/xalan/XObjectImpl.java
rm src/common/org/xmldb/common/xml/queries/xalan/XPathQueryFactoryImpl.java
rm src/common/org/xmldb/common/xml/queries/xt/XPathQueryImpl.java
rm src/common/org/xmldb/common/xml/queries/xt/XPathQueryFactoryImpl.java

%build
export CLASSPATH=$(build-classpath junit xalan-j2)
export OPT_JAR_LIST=:
ant \
    -Dant.build.javac.source=1.6 -Dant.build.javac.target=1.6 \
    -Djarname=%{name} -Dsdk.jarname=%{name}-sdk \
    dist

%install
# jars
install -d -m 755 %{buildroot}%{_javadir}
install -m 644 dist/xmldb/%{name}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
install -m 644 dist/xmldb/%{name}-sdk.jar %{buildroot}%{_javadir}/%{name}-sdk-%{version}.jar
install -m 644 dist/xmldb/%{bname}-common.jar %{buildroot}%{_javadir}/%{bname}-common-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} ${jar/-%{version}/}; done)
# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr src/build/javadoc/full/* %{buildroot}%{_javadocdir}/%{name}

%files
%defattr(0644,root,root,0755)
%doc src/{AUTHORS,LICENSE,README,config.xml}
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar

%files sdk
%defattr(0644,root,root,0755)
%{_javadir}/%{name}-sdk-%{version}.jar
%{_javadir}/%{name}-sdk.jar

%files -n %{bname}-common
%defattr(0644,root,root,0755)
%{_javadir}/%{bname}-common-%{version}.jar
%{_javadir}/%{bname}-common.jar

%files javadoc
%defattr(0644,root,root,0755)
%{_javadocdir}/%{name}

%changelog
