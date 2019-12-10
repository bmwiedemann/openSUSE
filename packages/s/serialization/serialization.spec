#
# spec file for package serialization
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
Name:           serialization
Version:        0.1.2
Release:        0
Summary:        Sbt wrapper around Scala pickling
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://github.com/sbt/serialization
Source0:        %{name}-%{version}.tar.xz
Source1:        https://repo1.maven.org/maven2/org/scala-sbt/%{name}_%{scala_version}/%{version}/%{name}_%{scala_version}-%{version}.pom
Patch0:         serialization-no-json4s-core.patch
Patch1:         serialization-jawn-json4s.patch
BuildRequires:  javapackages-local
BuildRequires:  jawn-json4s
BuildRequires:  jawn-parser
BuildRequires:  json4s-ast
BuildRequires:  quasiquotes
BuildRequires:  scala
BuildRequires:  scala-pickling
BuildRequires:  xmvn-install
BuildRequires:  xmvn-resolve
BuildArch:      noarch

%description
sbt serialization is a wrapper around Scala pickling focused
on sbt's usage. In particular it provides:
    * JSON format that's nice
    * static-only core picklers


%prep
%setup -q
cp %{SOURCE1} pom.xml
%patch0 -p1
%pom_change_dep :json4s-core_%{scala_version} :json4s-ast_%{scala_version}
%patch1 -p1
%pom_change_dep org.spire-math: org.typelevel::0.14.1
%pom_change_dep :json4s-support_%{scala_version} :jawn-json4s_%{scala_version}

%build
pushd %{name}
  mkdir -p target/classes
  scalac -d target/classes \
    -nobootcp \
	-classpath $(build-classpath \
        jawn/jawn-core_2.10 \
		jawn/jawn-json4s-2.10 \
		scala-pickling scala/scala-library \
		json4s/json4s-ast_2.10 \
		paradise/quasiquotes_2.10):target/classes \
	$(find src/main/scala -name \*.scala | xargs)
  jar cf %{name}-%{version}.jar -C target/classes .
popd

%mvn_artifact pom.xml %{name}/%{name}-%{version}.jar

%install
%mvn_install

%files -f .mfiles
%license LICENSE
%doc README.markdown

%changelog
