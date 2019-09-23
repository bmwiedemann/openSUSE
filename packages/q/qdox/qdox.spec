#
# spec file for package qdox
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


%global vertag  M9
%global verbase 2.0
Name:           qdox
Version:        %{verbase}.%{vertag}
Release:        0
Summary:        Tool to extract class/interface/method definitions from sources
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://github.com/paul-hammant/qdox
Source0:        http://repo2.maven.org/maven2/com/thoughtworks/qdox/qdox/%{verbase}-%{vertag}/%{name}-%{verbase}-%{vertag}-project.tar.gz
Source1:        qdox-MANIFEST.MF
BuildRequires:  byaccj
BuildRequires:  fdupes
BuildRequires:  java-cup-bootstrap
BuildRequires:  java-devel
BuildRequires:  javapackages-local
BuildRequires:  jflex-bootstrap
BuildArch:      noarch

%description
QDox is a parser for extracting class/interface/method definitions
from source files complete with JavaDoc @tags. It is designed to be
used by active code generators or documentation tools.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Libraries/Java

%description javadoc
API docs for %{name}.

%prep
%setup -q -n %{name}-%{verbase}-%{vertag}
find -name *.jar -delete
find -name *.class -delete
rm -rf bootstrap

# We don't need these plugins
%pom_remove_plugin :animal-sniffer-maven-plugin
%pom_remove_plugin :maven-failsafe-plugin
%pom_remove_plugin :maven-jflex-plugin
%pom_remove_plugin :maven-enforcer-plugin

%pom_xpath_set pom:workingDirectory '${basedir}/src/main/java/com/thoughtworks/qdox/parser/impl'

%pom_remove_parent .

%build
# Generate scanners (upstream does this with maven-jflex-plugin)
# Add the --inputstreamctor option if jflex is upgraded to a version 1.6 or higher
CLASSPATH=$(build-classpath java-cup) \
  jflex -d src/main/java/com/thoughtworks/qdox/parser/impl src/grammar/lexer.flex
CLASSPATH=$(build-classpath java-cup) \
  jflex -d src/main/java/com/thoughtworks/qdox/parser/impl src/grammar/commentlexer.flex

# Generate the parsers using the command-line that the exec-maven-plugin uses
GRAMMAR_PATH=$(pwd)/src/grammar/commentparser.y && \
  (cd src/main/java/com/thoughtworks/qdox/parser/impl && \
  byaccj -v -Jnorun -Jnoconstruct -Jclass=DefaultJavaCommentParser \
    -Jpackage=com.thoughtworks.qdox.parser.impl ${GRAMMAR_PATH})
GRAMMAR_PATH=$(pwd)/src/grammar/parser.y && \
  (cd src/main/java/com/thoughtworks/qdox/parser/impl && \
  byaccj -v -Jnorun -Jnoconstruct -Jclass=Parser \
    -Jimplements=CommentHandler -Jsemantic=Value \
	-Jpackage=com.thoughtworks.qdox.parser.impl \
	-Jstack=500 ${GRAMMAR_PATH})

# Build artifact
mkdir -p build/classes
javac -d build/classes -source 6 -target 6 \
  $(find src/main/java -name \*.java)
jar cf build/%{name}-%{verbase}-%{vertag}.jar -C build/classes .

# Inject OSGi manifests
jar ufm build/%{name}-%{verbase}-%{vertag}.jar %{SOURCE1}

mkdir -p build/apidoc
javadoc -d build/apidoc -source 6 -notimestamp $(find src/main/java -name \*.java)

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}
install -pm 0644 build/%{name}-%{verbase}-%{vertag}.jar %{buildroot}%{_javadir}/%{name}.jar
# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}
install -pm 0644 pom.xml %{buildroot}%{_mavenpomdir}/%{name}.pom
%add_maven_depmap %{name}.pom %{name}.jar -a qdox:qdox
# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -aL build/apidoc/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE.txt
%doc README.md

%files javadoc
%{_javadocdir}/%{name}
%license LICENSE.txt

%changelog
