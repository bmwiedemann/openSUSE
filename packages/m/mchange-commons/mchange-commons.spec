#
# spec file for package mchange-commons
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


%global git_tag mchange-commons-java-%{version}
Name:           mchange-commons
Version:        0.2.11
Release:        0
Summary:        A collection of general purpose utilities for c3p0
License:        LGPL-2.0-only OR EPL-1.0
Group:          Development/Libraries/Java
URL:            https://github.com/swaldman/mchange-commons-java
Source0:        https://github.com/swaldman/mchange-commons-java/archive/%{git_tag}/mchange-commons-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  java-devel
BuildRequires:  javapackages-local
BuildRequires:  log4j12
BuildRequires:  slf4j
BuildRequires:  typesafe-config
BuildArch:      noarch

%description
Originally part of c3p0, mchange-commons is a set of general purpose
utilities.

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description javadoc
%{summary}.

%prep
%setup -q -n mchange-commons-java-%{git_tag}

find -name '*.class' -delete
find -name '*.jar' -delete

%build
mkdir -p target/classes
javac -d target/classes -source 7 -target 7 \
  -cp $(build-classpath log4j12/log4j-12 slf4j typesafe-config) \
  $(find src/main/java -name \*.java | xargs)
jar cf target/%{git_tag}.jar -C target/classes .
jar uf target/%{git_tag}.jar -C src/main/resources .
mkdir -p target/api
javadoc -d target/api -source 7 -notimestamp \
  -classpath $(build-classpath log4j12/log4j-12 slf4j typesafe-config) \
  $(find src/main/java -name \*.java | xargs)

sed "s/@mchange-commons-java.version.maven@/%{version}/g" \
  src/main/maven/pom.xml > target/%{git_tag}.pom
%{mvn_artifact} target/%{git_tag}.pom target/%{git_tag}.jar

%install
# jar
install -d -m 755 %{buildroot}%{_javadir}/%{name}
install -pm 644 target/%{git_tag}.jar %{buildroot}%{_javadir}/%{name}/mchange-commons-java.jar
# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}/%{name}
install -pm 644 target/%{git_tag}.pom %{buildroot}%{_mavenpomdir}/%{name}/mchange-commons-java.pom
%add_maven_depmap %{name}/mchange-commons-java.pom %{name}/mchange-commons-java.jar
# javadoc
mkdir -p %{buildroot}%{_javadocdir}
cp -a target/api %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE*

%files javadoc
%license LICENSE*
%{_javadocdir}/%{name}

%changelog
