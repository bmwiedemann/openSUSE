#
# spec file for package xbean
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


Name:           xbean
Version:        4.20
Release:        0
Summary:        Java plugin based web server
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://geronimo.apache.org/xbean/
Source0:        https://repo1.maven.org/maven2/org/apache/%{name}/%{name}/%{version}/%{name}-%{version}-source-release.zip
Source1:        %{name}-build.tar.xz
Patch2:         0002-Unbundle-ASM.patch
Patch3:         0003-Remove-dependency-on-log4j-and-commons-logging.patch
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.7
BuildRequires:  javapackages-local
BuildRequires:  objectweb-asm >= 9
BuildRequires:  slf4j
BuildRequires:  unzip
Requires:       objectweb-asm >= 9
Requires:       slf4j
BuildArch:      noarch

%description
XBean is a plugin-based server analogous to Eclipse being a
plugin-based IDE. XBean is able to discover, download and install
server plugins from an Internet-based repository. Support for
multiple IoC systems, support for running with no IoC system, JMX
without JMX code, lifecycle and class loader management, and a Spring
integration is included.

%package        javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description    javadoc
This package provides API documentation for xbean.

%prep
%setup -q -a1
%patch2 -p1
%patch3 -p1

cp xbean-asm-util/src/main/java/org/apache/xbean/asm9/original/commons/AsmConstants.java xbean-reflect/src/main/java/org/apache/xbean/recipe/

# Parent POM is not packaged
%pom_remove_parent

for i in xbean-asm-util xbean-finder xbean-reflect; do
  %pom_remove_parent ${i}
  %pom_xpath_inject pom:project "<groupId>org.apache.xbean</groupId><version>%{version}</version>" ${i}
done

%pom_disable_module xbean-classloader
%pom_disable_module xbean-classpath
%pom_disable_module xbean-bundleutils
%pom_disable_module xbean-asm9-shaded
%pom_disable_module xbean-finder-shaded
%pom_disable_module xbean-naming
%pom_disable_module xbean-blueprint
%pom_disable_module xbean-spring
%pom_disable_module xbean-telnet
%pom_disable_module maven-xbean-plugin

%pom_remove_dep :commons-logging-api xbean-reflect
%pom_remove_dep :log4j xbean-reflect
%pom_remove_dep :xbean-asm9-shaded xbean-reflect
find -name CommonsLoggingConverter.java -delete
find -name Log4jConverter.java -delete

# Plugins useful for upstream only
%pom_remove_plugin :apache-rat-plugin
%pom_remove_plugin :maven-source-plugin

%pom_remove_dep :xbean-bundleutils xbean-finder
%pom_remove_dep org.osgi:org.osgi.core xbean-finder
rm -r xbean-finder/src/main/java/org/apache/xbean/finder{,/archive}/Bundle*

%pom_change_dep -r -f ::::: :::::

%build
mkdir -p lib
build-jar-repository -s lib objectweb-asm slf4j
%{ant} package javadoc

%install
# jars
install -dm 755 %{buildroot}%{_javadir}/%{name}
for i in xbean-asm-util xbean-finder xbean-reflect; do
  install -m 0644 ${i}/target/${i}-%{version}.jar %{buildroot}%{_javadir}/%{name}/${i}.jar
done

# poms
install -dm 755 %{buildroot}%{_mavenpomdir}/%{name}
for i in xbean-asm-util xbean-finder xbean-reflect; do
  install -m 0644 ${i}/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/${i}.pom
  %add_maven_depmap %{name}/${i}.pom %{name}/${i}.jar
done

# javadoc
install -dm 755 %{buildroot}/%{_javadocdir}/%{name}
for i in xbean-asm-util xbean-finder xbean-reflect; do
  cp -r ${i}/target/site/apidocs %{buildroot}/%{_javadocdir}/%{name}/${i}
done
%fdupes -s %{buildroot}/%{_javadocdir}/%{name}

%files -f .mfiles
%license LICENSE
%doc NOTICE

%files javadoc
%{_javadocdir}/%{name}

%changelog
