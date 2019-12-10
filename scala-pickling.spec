#
# spec file for package scala-pickling
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


%global scala_version 2.10
Name:           scala-pickling
Version:        0.10.1
Release:        0
Summary:        Scala Pickling
License:        BSD-3-Clause
URL:            https://github.com/scala/pickling
Source0:        %{name}-%{version}.tar.xz
Source1:        http://central.maven.org/maven2/org/scala-lang/modules/%{name}_%{scala_version}/%{version}/%{name}_%{scala_version}-%{version}.pom
BuildRequires:  javapackages-local
BuildRequires:  paradise
BuildRequires:  xmvn-install
BuildRequires:  xmvn-resolve
BuildRequires:  mvn(org.scalamacros:quasiquotes_2.10)

%description
Scala Pickling is an automatic serialization framework made for Scala.
It's fast, boilerplate-free, and allows users to easily swap in/out
different serialization formats (such as binary, or JSON), or even to
provide their own custom serialization format.

%prep
%setup -q

%build
pushd core
  mkdir -p target/classes
  javac -d target/classes -source 6 -target 6 \
    -cp $(build-classpath scala) \
    $(find src/main/java -name \*.java | xargs)
  scalac -d target/classes -Xplugin:%{_javadir}/paradise/paradise_%{scala_version}.jar \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
    -nobootcp \
%endif
    -classpath $(build-classpath scala paradise):target/classes \
    $(find src/main/scala -name \*.scala | xargs)
  jar cf ../%{name}.jar -C target/classes .
popd

%mvn_artifact %{SOURCE1} %{name}.jar

%install
%mvn_install

%files -f .mfiles
%license LICENSE
%doc README.md

%changelog
