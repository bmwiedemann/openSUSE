#
# spec file for package tesla-polyglot-common
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


Name:           tesla-polyglot-common
Version:        0.4.5
Release:        0
Summary:        Polyglot Tesla :: Common
License:        EPL-1.0
URL:            https://github.com/takari/maven-polyglot
Source0:        https://github.com/takari/polyglot-maven/archive/polyglot-%{version}.tar.gz
Patch0:         polyglot-snakeyaml-1.25.patch
Patch1:         pomless-tycho.patch
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  maven-local
BuildRequires:  mvn(commons-beanutils:commons-beanutils)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-model-builder)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.eclipse.sisu:org.eclipse.sisu.plexus)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildArch:      noarch

%description
Polyglot Tesla :: Common.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n polyglot-maven-polyglot-%{version}
%patch0 -p1
%patch1 -p1

find -name "*.class" -delete
find -name "*.jar" -delete

# Unavailable build deps/tools
%pom_disable_module polyglot-clojure
%pom_disable_module polyglot-scala
%pom_remove_dep -r :polyglot-scala
%pom_disable_module polyglot-ruby
%pom_remove_dep -r :polyglot-ruby
%pom_disable_module polyglot-kotlin
%pom_remove_dep -r :polyglot-kotlin

%pom_remove_parent
perl -pi -e 's#takari-jar#jar#g' */pom.xml
perl -pi -e 's#takari-maven-plugin#maven-plugin#g' */pom.xml

%pom_disable_module polyglot-atom
%pom_disable_module polyglot-groovy
%pom_disable_module polyglot-java
%pom_disable_module polyglot-maven-plugin
%pom_disable_module polyglot-translate-plugin
%pom_disable_module polyglot-xml
%pom_disable_module polyglot-yaml

%pom_remove_dep rubygems:maven-tools polyglot-ruby
rm -Rf polyglot-ruby/src/{test,it}
%pom_remove_plugin :maven-invoker-plugin polyglot-ruby
%pom_remove_plugin -r :maven-enforcer-plugin

# Unavailable plugin
%pom_remove_plugin org.codehaus.groovy:groovy-eclipse-compiler polyglot-groovy
%pom_remove_dep org.codehaus.groovy:groovy-eclipse-batch polyglot-groovy
%pom_remove_dep org.codehaus.groovy:groovy-eclipse-compiler polyglot-groovy
%pom_remove_plugin :maven-compiler-plugin polyglot-groovy
# use gmavenplus
%pom_add_plugin org.codehaus.gmavenplus:gmavenplus-plugin:1.5 polyglot-groovy "
 <executions>
  <execution>
   <goals>
    <goal>generateStubs</goal>
   </goals>
  </execution>
 </executions>"

for p in maven-plugin translate-plugin; do
  %pom_add_plugin "org.apache.maven.plugins:maven-plugin-plugin:3.4" polyglot-${p} "
  <configuration>
    <skipErrorNoDescriptorsFound>true</skipErrorNoDescriptorsFound>
  </configuration>"
%pom_xpath_inject "pom:dependency[pom:groupId = 'org.apache.maven']" "<version>3.3.1</version>" polyglot-${p}
done

%pom_xpath_inject "pom:project/pom:dependencies/pom:dependency[pom:groupId = 'org.apache.maven']" '<version>${mavenVersion}</version>'

# atom common maven-plugin translate-plugin
# diamond operator
for m in common yaml groovy
do
%pom_add_plugin org.apache.maven.plugins:maven-compiler-plugin:3.0 polyglot-${m} '
<configuration>
 <source>1.8</source>
 <target>1.8</target>
 <encoding>UTF-8</encoding>
</configuration>'
done

# Use web access
sed -i '/pyyaml/d' polyglot-yaml/src/test/java/org/sonatype/maven/polyglot/yaml/CompactFormatTest.java

# test skipped for unavailable dependency org.easytesting:fest-assert:1.1
rm -rf polyglot-clojure/src/test/java/*

# com.cedarsoftware:java-util:1.19.3
sed -i '/DeepEquals/d' polyglot-xml/src/test/java/org/sonatype/maven/polyglot/xml/TestReaderComparedToDefault.java
%pom_remove_dep com.cedarsoftware:java-util polyglot-xml

# ComparisonFailure
rm polyglot-yaml/src/test/java/org/sonatype/maven/polyglot/yaml/SnakeYamlModelReaderTest.java

%{mvn_alias} ':polyglot-{*}' io.tesla.polyglot:tesla-polyglot-@1
%{mvn_alias} ':polyglot-{*}' org.sonatype.pmaven:pmaven-@1

%{mvn_file} :{*} %{base_name}/@1

%build
%{mvn_build} \
	-f -- \
	-Dproject.build.sourceEncoding=UTF-8 \
	-Dsource=8

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE.txt license-header.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt license-header.txt

%changelog
