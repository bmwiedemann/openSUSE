#
# spec file for package jcifs
#
# Copyright (c) 2024 SUSE LLC
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


%define section free
Name:           jcifs
Version:        1.3.19
Release:        0
Summary:        Common Internet File System Client in 100% Java
License:        LGPL-2.1-or-later
Group:          Development/Libraries/Java
URL:            https://jcifs.samba.org/
Source0:        http://jcifs.samba.org/src/%{name}-%{version}.tgz
Source1:        https://repo1.maven.org/maven2/jcifs/jcifs/1.3.17/jcifs-1.3.17.pom
Patch0:         jcifs-1.3.19-build.patch
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  glassfish-servlet-api
BuildRequires:  java-devel
BuildRequires:  javapackages-local
Requires:       mvn(javax.servlet:javax.servlet-api)
BuildArch:      noarch

%description
The jCIFS SMB client library enables any Java application to remotely
access shared files and directories on SMB file servers(i.e. a
Microsoft Windows "share") in addition to domain, workgroup, and server
enumeration of NetBIOS over TCP/IP networks. It is an advanced
implementation of the CIFS protocol supporting Unicode, batching,
multiplexing of threaded callers, encrypted authentication,
transactions, the Remote Access Protocol (RAP), and much more. It is
licensed under LGPL which means commercial organizations can
legitimately use it with their proprietary code(you just can't sell or
give away a modified binary only version of the library itself without
reciprocation).

%package javadoc
Summary:        Common Internet File System Client in 100% Java
Group:          Documentation/HTML

%description javadoc
The jCIFS SMB client library enables any Java application to remotely
access shared files and directories on SMB file servers(i.e. a
Microsoft Windows "share") in addition to domain, workgroup, and server
enumeration of NetBIOS over TCP/IP networks. It is an advanced
implementation of the CIFS protocol supporting Unicode, batching,
multiplexing of threaded callers, encrypted authentication,
transactions, the Remote Access Protocol (RAP), and much more. It is
licensed under LGPL which means commercial organizations can
legitimately use it with their proprietary code(you just can't sell or
give away a modified binary only version of the library itself without
reciprocation).

%package demo
Summary:        Common Internet File System Client in 100% Java
Group:          Development/Libraries/Java
Requires:       %{name} = %{version}

%description demo
The jCIFS SMB client library enables any Java application to remotely
access shared files and directories on SMB file servers(i.e. a
Microsoft Windows "share") in addition to domain, workgroup, and server
enumeration of NetBIOS over TCP/IP networks. It is an advanced
implementation of the CIFS protocol supporting Unicode, batching,
multiplexing of threaded callers, encrypted authentication,
transactions, the Remote Access Protocol (RAP), and much more. It is
licensed under LGPL which means commercial organizations can
legitimately use it with their proprietary code(you just can't sell or
give away a modified binary only version of the library itself without
reciprocation).

%prep
%setup -q -n %{name}_%{version}
find -name '*.class' -delete
find -name '*.jar' -delete
# failed to build
rm examples/GetLocalGroupsMap.java
rm examples/SmbShell.java
%patch -P 0 -p1
sed -i "s|1.5|1.8|" build.xml
cp -p %{SOURCE1} pom.xml
sed -i "s|<version>1.3.17|<version>%{version}|" pom.xml

%pom_change_dep javax.servlet: :javax.servlet-api:3.1.0

%build
export CLASSPATH=$(build-classpath glassfish-servlet-api)
export OPT_JAR_LIST=:
%{ant} -Dant.build.javac.source=1.8 -Dant.build.javac.target=1.8 jar javadoc
export CLASSPATH=$(build-classpath glassfish-servlet-api):$(pwd)/%{name}-%{version}.jar
(cd examples && %javac -target 1.8 -source 1.8 *.java)

%install
# jar
mkdir -p %{buildroot}%{_javadir}
install -p -m 644 %{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} ${jar/-%{version}/}; done)
# pom
mkdir -p %{buildroot}%{_mavenpomdir}
%{mvn_install_pom} pom.xml %{buildroot}%{_mavenpomdir}/%{name}-%{version}.pom
%add_maven_depmap %{name}-%{version}.pom %{name}-%{version}.jar -a "org.samba.jcifs:jcifs"

# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr docs/api/* %{buildroot}%{_javadocdir}/%{name}-%{version}
%fdupes -s %{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}
# data
mkdir -p %{buildroot}%{_datadir}/%{name}/examples
cp -pr examples/*{.class,.java} %{buildroot}%{_datadir}/%{name}/examples
%fdupes -s %{buildroot}%{_datadir}/%{name}/examples

%files -f .mfiles
%doc README.txt docs/*.{html,txt,gif}
%{_javadir}/%{name}.jar

%files javadoc
%{_javadocdir}/%{name}
%{_javadocdir}/%{name}-%{version}

%files demo
%{_datadir}/%{name}

%changelog
