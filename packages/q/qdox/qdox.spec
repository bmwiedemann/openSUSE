#
# spec file for package qdox
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


Name:           qdox
Version:        2.0.1
Release:        0
Summary:        Tool to extract class/interface/method definitions from sources
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://github.com/paul-hammant/qdox
Source0:        https://repo1.maven.org/maven2/com/thoughtworks/qdox/qdox/%{version}/%{name}-%{version}-project.tar.bz2
Source1:        qdox-build.xml
Patch0:         Port-to-JFlex-1.7.0.patch
BuildRequires:  ant
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
%setup -q
cp %{SOURCE1} build.xml
%patch0 -p1
find -name *.jar -delete
find -name *.class -delete
rm -rf bootstrap
# We don't need these plugins
%pom_remove_plugin :animal-sniffer-maven-plugin
%pom_remove_plugin :maven-assembly-plugin
%pom_remove_plugin :maven-failsafe-plugin
%pom_remove_plugin :maven-invoker-plugin
%pom_remove_plugin :jflex-maven-plugin
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :exec-maven-plugin

%pom_remove_parent .

%build
# Generate scanners (upstream does this with maven-jflex-plugin)
jflex -d src/main/java/com/thoughtworks/qdox/parser/impl src/grammar/lexer.flex
jflex -d src/main/java/com/thoughtworks/qdox/parser/impl src/grammar/commentlexer.flex

# Generate parsers (upstream does this with exec-maven-plugin)
(cd ./src/main/java/com/thoughtworks/qdox/parser/impl
 byaccj -v -Jnorun -Jnoconstruct -Jclass=DefaultJavaCommentParser -Jpackage=com.thoughtworks.qdox.parser.impl ../../../../../../../grammar/commentparser.y
 byaccj -v -Jnorun -Jnoconstruct -Jclass=Parser -Jimplements=CommentHandler -Jsemantic=Value -Jpackage=com.thoughtworks.qdox.parser.impl -Jstack=500 ../../../../../../../grammar/parser.y
)

%ant jar javadoc

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}
install -pm 0644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}
install -pm 0644 pom.xml %{buildroot}%{_mavenpomdir}/%{name}.pom
%add_maven_depmap %{name}.pom %{name}.jar -a qdox:qdox
# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -aL target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE.txt
%doc README.md

%files javadoc
%{_javadocdir}/%{name}
%license LICENSE.txt

%changelog
