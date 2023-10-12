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
Name:           scala-stm
Version:        0.11.1
Release:        0
Summary:        Software Transactional Memory for Scala
License:        BSD-3-Clause
Group:          Development/Libraries/Java
URL:            https://github.com/scala-stm/scala-stm
Source0:        %{name}-%{version}.tar.xz
Source1:        https://repo1.maven.org/maven2/org/%{name}/%{name}_%{scala_short_version}/%{version}/%{name}_%{scala_short_version}-%{version}.pom
BuildRequires:  fdupes
BuildRequires:  java-devel
BuildRequires:  javapackages-local
BuildRequires:  scala >= %{scala_short_version}
BuildRequires:  xmvn-install
BuildRequires:  xmvn-resolve
BuildArch:      noarch

%description
ScalaSTM is a lightweight software transactional memory
for Scala, inspired by the STMs in Haskell and Clojure.

ScalaSTM provides a mutable cell called a Ref. If you
build a shared data structure using immutable objects and
Ref-s, then you can access it from multiple threads or
actors. No synchronized, no deadlocks or race conditions,
and good scalability. Included are concurrent sets and
maps, and we also have an easier and safer replacement
for wait and notifyAll.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Libraries/Java

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{version}

%{mvn_file} org.%{name}:%{name}_%{scala_short_version} %{name}

%build
mkdir -p target/classes
scalac -nobootcp -d target/classes -release:8  \
    $(find jvm/src/main/scala -name \*.scala && \
      find jvm/src/main/scala-2.13+ -name \*.scala && \
      find jvm/src/main/scala-2.14- -name \*.scala && \
      find shared/src/main/scala -name \*.scala && \
      find shared/src/main/scala-2.13+ -name \*.scala | xargs)
jar -cf target/%{name}_%{scala_short_version}-%{version}.jar -C target/classes .
mkdir -p target/apidoc
scaladoc -nobootcp -d target/apidoc -release:8 \
    $(find jvm/src/main/scala -name \*.scala && \
      find jvm/src/main/scala-2.13+ -name \*.scala && \
      find jvm/src/main/scala-2.14- -name \*.scala && \
      find shared/src/main/scala -name \*.scala && \
      find shared/src/main/scala-2.13+ -name \*.scala | xargs)

%install
# target/scala-2.10/scala-stm_2.10-0.7.jar
%{mvn_artifact} %{SOURCE1} target/%{name}_%{scala_short_version}-%{version}.jar
%mvn_install -J target/apidoc/
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%doc README.md RELEASE-NOTES.txt
%license LICENSE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
