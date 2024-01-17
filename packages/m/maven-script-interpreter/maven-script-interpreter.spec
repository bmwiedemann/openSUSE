#
# spec file for package maven-script-interpreter
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


Name:           maven-script-interpreter
Version:        1.3
Release:        0
Summary:        Maven Script Interpreter
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://maven.apache.org/shared/maven-script-interpreter/
Source0:        https://dlcdn.apache.org/maven/shared/%{name}-%{version}-source-release.zip
Source1:        %{name}-build.xml
BuildRequires:  ant
BuildRequires:  apache-commons-io
BuildRequires:  bsh2
BuildRequires:  fdupes
BuildRequires:  javapackages-local
BuildRequires:  slf4j
BuildRequires:  unzip
Requires:       mvn(commons-io:commons-io)
Requires:       mvn(org.apache-extras.beanshell:bsh)
Requires:       mvn(org.slf4j:slf4j-api)
BuildArch:      noarch

%description
This component provides some utilities to interpret/execute some scripts for
various implementations: Groovy or BeanShell.

Groovy script is currently disabled.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
API documentation for %{name}.

%prep
%setup -q
cp %{SOURCE1} build.xml

%pom_remove_parent
%pom_xpath_inject pom:project "<groupId>org.apache.maven.shared</groupId>"

%pom_remove_dep :groovy
rm src/main/java/org/apache/maven/shared/scriptinterpreter/GroovyScriptInterpreter.java
rm src/test/java/org/apache/maven/shared/scriptinterpreter/GroovyScriptInterpreterTest.java
rm src/test/java/org/apache/maven/shared/scriptinterpreter/ScriptRunnerTest.java
sed -i /GroovyScriptInterpreter/d src/main/java/org/apache/maven/shared/scriptinterpreter/ScriptRunner.java

%build
mkdir -p lib
build-jar-repository -s lib \
	bsh2/bsh \
	commons-io \
    slf4j/api \
    slf4j/simple

%{ant} \
	jar javadoc

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}/%{name}
install -pm 0644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}/%{name}.jar

# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}
install -pm 0644 pom.xml %{buildroot}%{_mavenpomdir}/%{name}/%{name}.pom
%add_maven_depmap %{name}/%{name}.pom %{name}/%{name}.jar

# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE NOTICE
%doc DEPENDENCIES

%files javadoc
%{_javadocdir}/%{name}
%license LICENSE NOTICE

%changelog
