#
# spec file for package scala-parser-combinators
#
# Copyright (c) 2023 SUSE LLC
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


%global scala_short_version 2.13
Name:           scala-parser-combinators
Version:        2.3.0
Release:        0
Summary:        Simple combinator-based parsing for Scala
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://github.com/scala/scala-parser-combinators
Source0:        %{name}-%{version}.tar.xz
Source1:        https://repo1.maven.org/maven2/org/scala-lang/modules/%{name}_%{scala_short_version}/%{version}/%{name}_%{scala_short_version}-%{version}.pom
BuildRequires:  fdupes
BuildRequires:  java-devel
BuildRequires:  javapackages-local
BuildRequires:  xmvn-install
BuildRequires:  xmvn-resolve
BuildRequires:  mvn(org.scala-lang:scala-compiler) >= %{scala_short_version}
BuildRequires:  mvn(org.scala-lang:scala-library) >= %{scala_short_version}
BuildArch:      noarch

%description
Simple combinator-based parsing for Scala. Formerly part of the Scala
standard library, now a separate community-maintained module

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Libraries/Java

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q

%{mvn_file} :{*} scala/@1

%build
rm -rf \
    shared/src/main/scala-2.13-

mkdir -p target/classes
scalac -d target/classes -release:8  $(find shared/src/main -name \*.scala && find jvm/src/main -name \*.scala | xargs)
jar -cf target/%{name}_%{scala_short_version}-%{version}.jar -C target/classes .
mkdir -p target/apidoc
scaladoc -d target/apidoc -release:8 $(find shared/src/main -name \*.scala && find jvm/src/main -name \*.scala | xargs)

%install
%{mvn_artifact} %{SOURCE1} target/%{name}_%{scala_short_version}-%{version}.jar
%mvn_install -J target/apidoc/
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%doc README.md
%license LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE

%changelog
