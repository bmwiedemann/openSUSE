#
# spec file for package xbean
#
# Copyright (c) 2020 SUSE LLC
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
Version:        4.5
Release:        0
Summary:        Java plugin based web server
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://geronimo.apache.org/xbean/
Source0:        http://repo2.maven.org/maven2/org/apache/%{name}/%{name}/%{version}/%{name}-%{version}-source-release.zip
# Fix dependency on xbean-asm4-shaded to original objectweb-asm
Patch0:         0001-Unshade-ASM.patch
Patch2:         0003-Port-to-QDox-2.0.patch
BuildRequires:  apache-commons-logging
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local
BuildRequires:  log4j12
BuildRequires:  objectweb-asm >= 5
BuildRequires:  slf4j
BuildRequires:  unzip
# The code uses sun.misc.URLClassloader
BuildConflicts: java-devel >= 9
BuildConflicts: java-headless >= 9
# Avoid build cycles
BuildConflicts: java-devel-openj9
BuildConflicts: java-headless-openj9
Requires:       objectweb-asm >= 5
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
%setup -q
# build failing on this due to doxia-sitetools problems
rm src/site/site.xml

%patch0 -p1
%patch2 -p1

%pom_remove_parent
%pom_remove_dep mx4j:mx4j

%pom_remove_dep -r :xbean-asm5-shaded
%pom_remove_dep -r :xbean-finder-shaded
%pom_disable_module xbean-asm5-shaded
%pom_disable_module xbean-finder-shaded

%pom_xpath_remove pom:scope xbean-asm-util
%pom_xpath_remove pom:optional xbean-asm-util

# Prevent modules depending on springframework from building.
%pom_remove_dep org.springframework:
%pom_disable_module xbean-classloader
%pom_disable_module xbean-spring
%pom_disable_module maven-xbean-plugin
rm -rf maven-xbean-plugin
# blueprint FTBFS, disable for now
%pom_disable_module xbean-blueprint

%pom_remove_dep :xbean-bundleutils xbean-finder
rm -r xbean-finder/src/main/java/org/apache/xbean/finder{,/archive}/Bundle*
%pom_disable_module xbean-bundleutils

%pom_disable_module xbean-telnet

# maven-xbean-plugin invocation makes no sense as there are no namespaces
%pom_remove_plugin :maven-xbean-plugin xbean-classloader

# As auditing tool RAT is useful for upstream only.
%pom_remove_plugin :apache-rat-plugin

# disable copy of internal aries-blueprint
sed -i "s|<Private-Package>|<!--Private-Package>|" xbean-blueprint/pom.xml
sed -i "s|</Private-Package>|</Private-Package-->|" xbean-blueprint/pom.xml

%pom_change_dep -r -f ::::: :::::

%build
for i in xbean-asm-util xbean-classpath xbean-finder xbean-naming xbean-reflect; do
  pushd $i
    mkdir -p build/classes
    javac -d build/classes  -encoding utf-8 -source 6 -target 6 \
      -cp $(build-classpath log4j12/log4j-12 commons-logging-api slf4j/api objectweb-asm/asm objectweb-asm/asm-commons):../xbean-asm-util/xbean-asm-util.jar \
      $(find src/main/java -name *.java)
    jar cf $i.jar -C build/classes .
  popd
done
mkdir -p build/apidoc
javadoc -d build/apidoc -source 6 -encoding utf-8 \
  -classpath $(build-classpath log4j12/log4j-12 commons-logging-api slf4j/api objectweb-asm/asm objectweb-asm/asm-commons) \
  $(for i in xbean-asm-util xbean-classpath xbean-finder xbean-naming xbean-reflect; do find $i/src/main/java -name *.java; done | xargs)

%install
# jars && poms
install -dm 755 %{buildroot}%{_javadir}/%{name}
install -dm 755 %{buildroot}%{_mavenpomdir}/%{name}
for i in xbean-asm-util xbean-classpath xbean-finder xbean-naming xbean-reflect; do
  install -m 0644 $i/$i.jar %{buildroot}%{_javadir}/%{name}
  %pom_remove_parent ${i}
  %pom_xpath_inject pom:project "<groupId>org.apache.xbean</groupId><version>%{version}</version>" ${i}
  install -m 0644 $i/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/$i.pom
  %add_maven_depmap %{name}/$i.pom %{name}/$i.jar
done

# javadoc
install -dm 755 %{buildroot}/%{_javadocdir}/%{name}
cp -aL build/apidoc/* %{buildroot}/%{_javadocdir}/%{name}
%fdupes -s %{buildroot}/%{_javadocdir}/%{name}

%files -f .mfiles
%license LICENSE
%doc NOTICE

%files javadoc
%{_javadocdir}/%{name}

%changelog
