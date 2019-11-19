#
# spec file for package tesla-polyglot
#
# Copyright (c) 2019 SUSE LLC.
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "bootstrap"
%bcond_without bootstrap
%else
%bcond_with bootstrap
%endif
%global base_name tesla-polyglot
Version:        0.2.1
Release:        0
URL:            https://github.com/takari/maven-polyglot
Source0:        https://github.com/takari/polyglot-maven/archive/polyglot-%{version}.tar.gz
Patch0:         polyglot-snakeyaml-1.25.patch
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-model-builder)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.eclipse.sisu:org.eclipse.sisu.plexus)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildArch:      noarch
%if %{with bootstrap}
Name:           %{base_name}-common
Summary:        Polyglot Tesla :: Common
License:        EPL-1.0

%description
Polyglot Tesla :: Common.
%else
Name:           %{base_name}
Summary:        Modules to enable Maven usage in other JVM languages
License:        EPL-1.0
BuildRequires:  mvn(commons-logging:commons-logging)
# Built in the bootstrap phase
BuildRequires:  mvn(io.takari.polyglot:polyglot-common) = %{version}
# Maven plugins
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
# Yaml module
BuildRequires:  mvn(org.yaml:snakeyaml)
# Groovy module
BuildRequires:  mvn(org.codehaus.gmavenplus:gmavenplus-plugin)
BuildRequires:  mvn(org.codehaus.groovy:groovy)

%description
Polyglot for Maven is an experimental distribution of Maven
that allows the expression of a POM in something other than
XML. A couple of the dialects also have the capability to
write plugins inline: the Groovy, Ruby and Scala dialects
allow this.
%endif

%if %{without bootstrap}
%package atom
Summary:        Polyglot Tesla :: Atom

%description atom
Polyglot Tesla :: Atom.

%package groovy
Summary:        Polyglot Tesla :: Groovy

%description groovy
Polyglot Tesla :: Groovy.

%package yaml
Summary:        Polyglot Tesla :: YAML

%description yaml
Polyglot Tesla :: YAML.

%package maven-plugin
Summary:        Polyglot Tesla :: Maven Plugin

%description maven-plugin
This package contains Polyglot Tesla Maven Plugin.

%package translate-plugin
Summary:        Polyglot :: Translate Plugin

%description translate-plugin
This package contains Polyglot Translate Plugin.

%package xml
Summary:        Polyglot Tesla :: XML

%description xml
Polyglot Tesla :: XML.

%endif

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n polyglot-maven-polyglot-%{version}
%patch0 -p1

find -name "*.class" -delete
find -name "*.jar" -delete

# Unavailable build deps/tools
%pom_disable_module polyglot-clojure
%pom_disable_module polyglot-scala
%pom_remove_dep -r :polyglot-scala
%pom_disable_module polyglot-ruby
%pom_remove_dep -r :polyglot-ruby

%{pom_remove_parent}
perl -pi -e 's#takari-jar#jar#g' */pom.xml
perl -pi -e 's#takari-maven-plugin#maven-plugin#g' */pom.xml

%if %{with bootstrap}
%pom_disable_module polyglot-atom
%pom_disable_module polyglot-groovy
%pom_disable_module polyglot-maven-plugin
%pom_disable_module polyglot-translate-plugin
%pom_disable_module polyglot-xml
%pom_disable_module polyglot-yaml
%else
%pom_disable_module polyglot-common
%endif

%pom_remove_dep rubygems:maven-tools polyglot-ruby
rm -Rf polyglot-ruby/src/{test,it}
%pom_remove_plugin :maven-invoker-plugin polyglot-ruby

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
    <goal>testGenerateStubs</goal>
    <!--goal>compile</goal>
    <goal>testCompile</goal-->
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
for m in yaml groovy
do
%pom_add_plugin org.apache.maven.plugins:maven-compiler-plugin:3.0 polyglot-${m} '
<configuration>
 <source>1.7</source>
 <target>1.7</target>
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

%if %{with bootstrap}
%{mvn_package} :polyglot __noinstall
%endif

%build
%{mvn_build} \
%if %{without bootstrap}
	-s \
%endif
	-f -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%if %{with bootstrap}
%files -f .mfiles
%license LICENSE.txt license-header.txt

%else
%files -f .mfiles-polyglot
%doc poms README.md
%license LICENSE.txt license-header.txt

%files atom -f .mfiles-polyglot-atom

%files groovy -f .mfiles-polyglot-groovy

%files yaml -f .mfiles-polyglot-yaml

%files maven-plugin -f .mfiles-polyglot-maven-plugin

%files translate-plugin -f .mfiles-polyglot-translate-plugin

%files xml -f .mfiles-polyglot-xml
%doc polyglot-xml/README.md

%endif

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt license-header.txt

%changelog
