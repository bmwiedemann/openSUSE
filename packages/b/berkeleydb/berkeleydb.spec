#
# spec file for package berkeleydb
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           berkeleydb
Version:        5.0.58
Release:        0
Summary:        Berkeley DB Java Edition
License:        Sleepycat
Group:          Development/Libraries/Java
Url:            http://www.oracle.com/us/products/database/overview/index.html
Source0:        http://download.oracle.com/berkeley-db/je-%{version}.tar.gz
BuildRequires:  ant >= 1.7.0
BuildRequires:  ant-junit
BuildRequires:  fdupes
BuildRequires:  geronimo-j2ee-connector-1_5-api
BuildRequires:  java-devel >= 1.7
BuildRequires:  javapackages-tools
BuildRequires:  junit
BuildRequires:  mx4j
Requires:       j2ee-connector
Requires:       java
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Berkeley DB Java Edition is a high performance, transactional storage
engine written entirely in Java. Like the highly successful Berkeley DB
product, Berkeley DB Java Edition executes in the address space of the
application, without the overhead of client/server communication. It
stores data in the application's native format, so no runtime data
translation is required. Berkeley DB Java Edition supports full ACID
transactions and recovery. It provides an easy-to-use, programmatic
interface, allowing developers to store and retrieve information
quickly, simply and reliably.

%package        javadoc
Summary:        Berkeley DB Java Edition
Group:          Development/Libraries/Java

%description    javadoc
Berkeley DB Java Edition is a high performance, transactional storage
engine written entirely in Java. Like the highly successful Berkeley DB
product, Berkeley DB Java Edition executes in the address space of the
application, without the overhead of client/server communication. It
stores data in the application's native format, so no runtime data
translation is required. Berkeley DB Java Edition supports full ACID
transactions and recovery. It provides an easy-to-use, programmatic
interface, allowing developers to store and retrieve information
quickly, simply and reliably.

%package        manual
Summary:        Berkeley DB Java Edition
Group:          Development/Libraries/Java

%description    manual
Berkeley DB Java Edition is a high performance, transactional storage
engine written entirely in Java. Like the highly successful Berkeley DB
product, Berkeley DB Java Edition executes in the address space of the
application, without the overhead of client/server communication. It
stores data in the application's native format, so no runtime data
translation is required. Berkeley DB Java Edition supports full ACID
transactions and recovery. It provides an easy-to-use, programmatic
interface, allowing developers to store and retrieve information
quickly, simply and reliably.

%package        demo
Summary:        Berkeley DB Java Edition
Group:          Development/Libraries/Java

%description    demo
Berkeley DB Java Edition is a high performance, transactional storage
engine written entirely in Java. Like the highly successful Berkeley DB
product, Berkeley DB Java Edition executes in the address space of the
application, without the overhead of client/server communication. It
stores data in the application's native format, so no runtime data
translation is required. Berkeley DB Java Edition supports full ACID
transactions and recovery. It provides an easy-to-use, programmatic
interface, allowing developers to store and retrieve information
quickly, simply and reliably.

%prep
%setup -q -n je-%{version}

%build
export CLASSPATH=
export OPT_JAR_LIST="ant/ant-trax ant/ant-junit junit"
ant \
	-Djmx.jarfile=$(build-classpath mx4j/mx4j) \
	-Dj2ee.jarfile=$(build-classpath geronimo-j2ee-connector-1.5-api) \
	-Djdk.version=7 \
	jar javadoc-all

%install
install -dm 755 %{buildroot}%{_javadir}
install -pm 644 build/lib/je.jar \
  %{buildroot}%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar \
  %{buildroot}%{_javadir}/%{name}.jar
# javadoc
install -dm 755 %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr docs/java/* %{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}
# FIXME: (dwalluck): This breaks rpmbuild -bi --short-circuit
rm -rf docs/java
# Remove redundants documentations
%fdupes -s docs

# demo
install -dm 755 %{buildroot}%{_datadir}/%{name}
install -dm 755 %{buildroot}%{_datadir}/%{name}/examples
cp -pr examples/* %{buildroot}%{_datadir}/%{name}/examples

%files
%defattr(0644,root,root,0755)
%doc LICENSE README
%{_javadir}/*.jar

%files javadoc
%defattr(0644,root,root,0755)
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%files manual
%defattr(0644,root,root,0755)
%exclude %{_docdir}/%{name}/LICENSE
%exclude %{_docdir}/%{name}/README
%doc docs/*

%files demo
%defattr(-,root,root,0755)
%{_datadir}/%{name}/examples
%dir %{_datadir}/%{name}

%changelog
