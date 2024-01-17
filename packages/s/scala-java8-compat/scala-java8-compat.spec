#
# spec file for package scala-stm
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
Name:           scala-java8-compat
Version:        1.0.2
Release:        0
Summary:        Java 8 compatibility kit for Scala
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://github.com/scala/scala-java8-compat
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
A Java 8 compatibility kit for Scala 2.12 and 2.11.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Libraries/Java

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{version}

%{mvn_file} org.%{name}:%{name}_%{scala_short_version} %{name}

%build
rm -rf \
    src/main/scala-2.13- \
    src/main/scala-2.11 \
    src/main/java-2.13-

mkdir -p target/classes
scalac -d target/classes -release:8  $(find src/main -name \*.scala && find src/main -name \*.java | xargs)
jar -cf target/%{name}_%{scala_short_version}-%{version}.jar -C target/classes .
mkdir -p target/apidoc
scaladoc -d target/apidoc -release:8 $(find src/main -name \*.scala && find src/main -name \*.java | xargs)

%install
%{mvn_file} :%{name}{*} scala/%{name}@1
%{mvn_artifact} %{SOURCE1} target/%{name}_%{scala_short_version}-%{version}.jar
%mvn_install -J target/apidoc/
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%doc README.md
%license LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE

%changelog
