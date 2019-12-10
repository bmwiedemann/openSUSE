#
# spec file for package sbt-launcher
#
# Copyright (c) 2019 SUSE LLC
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


%global short_name launcher
Name:           sbt-%{short_name}
Version:        1.1.2
Release:        0
Summary:        Launcher Implementation
License:        Apache-2.0 AND BSD-3-Clause
Group:          Development/Libraries/Java
URL:            https://github.com/sbt/%{short_name}
Source0:        %{short_name}-%{version}.tar.xz
Source1:        http://central.maven.org/maven2/org/scala-sbt/%{short_name}-interface/%{version}/%{short_name}-interface-%{version}.pom
# Generated offline by sbt make-pom and cleaned up
Source2:        %{short_name}-implementation.pom
BuildRequires:  apache-ivy
BuildRequires:  fdupes
BuildRequires:  javapackages-local
BuildRequires:  scala
BuildRequires:  xmvn-install
BuildRequires:  xmvn-resolve
BuildArch:      noarch

%description
Standalone launcher for maven/ivy deployed projects.

%package interface
Summary:        Launcher Interface
Group:          Development/Libraries/Java

%description interface
Interfaces for launching projects with the sbt launcher

%package javadoc
Summary:        API Documentation for %{name}
Group:          Documentation/HTML

%description javadoc
JavaDoc documentation for %{name}

%prep
%setup -q -n %{short_name}-%{version}

%build
pushd %{short_name}-interface
  cp %{SOURCE1} pom.xml
  # jar
  mkdir -p target/classes
  javac -d target/classes -source 6 -target 6 $(find src/main -name \*.java | xargs)
  jar -cf target/%{short_name}-interface-%{version}.jar -C target/classes .
  # javadoc
  mkdir -p target/site/apidocs
  javadoc -d target/site/apidocs -source 6 -notimestamp $(find src/main -name \*.java | xargs)
popd
%{mvn_artifact} %{short_name}-interface/pom.xml %{short_name}-interface/target/%{short_name}-interface-%{version}.jar
pushd %{short_name}-implementation
  cat %{SOURCE2} | sed 's#@VERSION@#%{version}#g' >pom.xml
  # Map sources
  mkdir -p target/generated-sources
  cat src/main/input_sources/CrossVersionUtil.scala | sed -e 's#\${{cross.package0}}#xsbt#g' -e 's#\${{cross.package1}}#boot#g' \
  > target/generated-sources/CrossVersionUtil.scala
  # jar
  mkdir -p target/classes
  scalac -d target/classes \
    -nobootcp \
    -classpath $(build-classpath apache-ivy scala):../%{short_name}-interface/target/%{short_name}-interface-%{version}.jar \
    $(find src/main/scala -name \*.scala  && find target/generated-sources -name \*.scala | xargs)
  jar -cf target/%{short_name}-implementation-%{version}.jar -C target/classes .
  # apidoc
  mkdir -p target/site/apidocs
  scaladoc -d target/site/apidocs \
    -nobootcp \
	-classpath $(build-classpath apache-ivy scala):../%{short_name}-interface/target/%{short_name}-interface-%{version}.jar \
    $(find src/main/scala -name \*.scala  && find target/generated-sources -name \*.scala | xargs)
popd
%{mvn_artifact} %{short_name}-implementation/pom.xml %{short_name}-implementation/target/%{short_name}-implementation-%{version}.jar

%{mvn_package} :*interface interface

mkdir -p target/site/apidocs/
mv %{short_name}-interface/target/site/apidocs target/site/apidocs/%{short_name}-interface
mv %{short_name}-implementation/target/site/apidocs target/site/apidocs/%{short_name}-implementation

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license licenses/LICENSE_Apache licenses/LICENSE_Scala NOTICE
%doc README.md

%files interface -f .mfiles-interface

%files javadoc -f .mfiles-javadoc 
%license licenses/LICENSE_Apache licenses/LICENSE_Scala NOTICE

%changelog
