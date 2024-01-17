#
# spec file for package snakeyaml
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


%global vertag 7f5106920d77
%bcond_with tests
Name:           snakeyaml
Version:        1.33
Release:        0
Summary:        YAML parser and emitter for the Java programming language
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://bitbucket.org/%{name}/%{name}
Source0:        https://bitbucket.org/%{name}/%{name}/get/%{name}-%{version}.tar.bz2
Source1:        %{name}-build.xml
# Upstream has forked gdata-java and base64 and refuses [1] to
# consider replacing them by external dependencies.  Bundled libraries
# need to be removed and their use replaced by system libraries.
# See rhbz#875777 and http://code.google.com/p/snakeyaml/issues/detail?id=175
#
# Replace use of bundled Base64 implementation with java.util.Base64
Patch0:         0001-replace-bundled-base64coder-with-java.util.Base64.patch
# We don't have gdata-java, use commons-codec instead
Patch1:         0002-Replace-bundled-gdata-java-client-classes-with-commo.patch
Patch2:         0003-Fix-ReaderBomTest.patch
BuildRequires:  ant
BuildRequires:  apache-commons-codec
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local
Requires:       mvn(commons-codec:commons-codec)
BuildArch:      noarch
%if %{with tests}
BuildRequires:  ant-junit
BuildRequires:  apache-commons-collections
BuildRequires:  apache-commons-lang
BuildRequires:  hamcrest-core
BuildRequires:  joda-time
BuildRequires:  junit
BuildRequires:  oro
BuildRequires:  velocity
# Differently sorted collections make fail some tests that rely on a particular order
BuildConflicts: java >= 9
BuildConflicts: java-devel >= 9
BuildConflicts: java-headless >= 9
%endif

%description
SnakeYAML features:
    * a complete YAML 1.1 parser. In particular,
      SnakeYAML can parse all examples from the specification.
    * Unicode support including UTF-8/UTF-16 input/output.
    * high-level API for serializing and deserializing
      native Java objects.
    * support for all types from the YAML types repository.
    * relatively sensible error messages.

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains %{summary}.

%prep
%setup -q -n %{name}-%{name}-%{vertag}
cp %{SOURCE1} build.xml
%patch0 -p1
%patch1 -p1
%patch2 -p1

%pom_remove_plugin :cobertura-maven-plugin
%pom_remove_plugin :maven-changes-plugin
%pom_remove_plugin :maven-license-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-site-plugin

sed -i "/<artifactId>spring</s/spring/&-core/" pom.xml
rm -f src/test/java/examples/SpringTest.java

# Replacement for bundled gdata-java-client
%pom_add_dep commons-codec:commons-codec

# Unnecessary test-time only dependency
%pom_remove_dep joda-time:joda-time
rm -rf src/test/java/examples/jodatime
%pom_remove_dep org.projectlombok:lombok
%pom_remove_dep org.apache.velocity:velocity-engine-core

# fails in rpmbuild only due to different locale
rm src/test/java/org/yaml/snakeyaml/issues/issue67/NonAsciiCharsInClassNameTest.java
# fails after unbundling
rm src/test/java/org/yaml/snakeyaml/issues/issue318/ContextClassLoaderTest.java

# Tests using dependencies we don't have/have removed
rm src/test/java/org/yaml/snakeyaml/emitter/template/VelocityTest.java
rm src/test/java/org/yaml/snakeyaml/issues/issue387/YamlExecuteProcessContextTest.java
rm src/test/java/org/yaml/snakeyaml/env/ApplicationProperties.java
rm src/test/java/org/yaml/snakeyaml/env/EnvLombokTest.java
rm src/test/java/org/yaml/snakeyaml/issues/issue527/Fuzzy47047Test.java
rm src/test/java/org/yaml/snakeyaml/issues/issue530/Fuzzy47039Test.java
rm src/test/java/org/yaml/snakeyaml/issues/issue543/Fuzzer50355Test.java
rm src/test/java/org/yaml/snakeyaml/issues/issue525/FuzzyStackOverflowTest.java
rm src/test/java/org/yaml/snakeyaml/issues/issue529/Fuzzy47028Test.java
rm src/test/java/org/yaml/snakeyaml/issues/issue531/Fuzzy47081Test.java
rm src/test/java/org/yaml/snakeyaml/issues/issue526/Fuzzy47027Test.java

# Problematic test resources for maven-resources-plugin 3.2
rm src/test/resources/issues/issue99.jpeg
rm src/test/resources/reader/unicode-16be.txt
rm src/test/resources/reader/unicode-16le.txt
rm src/test/resources/pyyaml/spec-05-01-utf16be.data
rm src/test/resources/pyyaml/spec-05-01-utf16le.data
rm src/test/resources/pyyaml/spec-05-02-utf16le.data
rm src/test/resources/pyyaml/odd-utf16.stream-error
rm src/test/resources/pyyaml/invalid-character.loader-error
rm src/test/resources/pyyaml/invalid-character.stream-error
rm src/test/resources/pyyaml/invalid-utf8-byte.loader-error
rm src/test/resources/pyyaml/invalid-utf8-byte.stream-error
rm src/test/resources/pyyaml/empty-document-bug.data
rm src/test/resources/pyyaml/spec-05-02-utf16be.data
rm -rf src/test/resources/fuzzer/
# Test using the jpeg data removed above
rm src/test/java/org/yaml/snakeyaml/issues/issue99/YamlBase64Test.java

# convert CR+LF to LF
sed -i 's/\r//g' LICENSE.txt

%build
mkdir -p lib
build-jar-repository -s lib commons-codec
%if %{with tests}
build-jar-repository -s lib junit hamcrest/core velocity commons-collections commons-lang oro joda-time
%endif
%{ant} \
%if %{without tests}
  -Dtest.skip=true \
%endif
  clean package javadoc

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}
install -pm 0644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}
install -pm 0644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar
# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE.txt

%files javadoc
%license LICENSE.txt
%{_javadocdir}/%{name}

%changelog
