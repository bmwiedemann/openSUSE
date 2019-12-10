#
# spec file for package json4s
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
Name:           json4s
Version:        3.6.7
Release:        0
Summary:        Common AST for Scala JSON parsers
License:        Apache-2.0
URL:            https://github.com/json4s/json4s
Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}-%{version}-build.tar.xz
Source100:      https://repo1.maven.org/maven2/org/%{name}/%{name}-ast_%{scala_version}/%{version}/%{name}-ast_%{scala_version}-%{version}.pom
Source101:      https://repo1.maven.org/maven2/org/%{name}/%{name}-core_%{scala_version}/%{version}/%{name}-core_%{scala_version}-%{version}.pom
Source102:      https://repo1.maven.org/maven2/org/%{name}/%{name}-ext_%{scala_version}/%{version}/%{name}-ext_%{scala_version}-%{version}.pom
Source103:      https://repo1.maven.org/maven2/org/%{name}/%{name}-jackson_%{scala_version}/%{version}/%{name}-jackson_%{scala_version}-%{version}.pom
Source104:      https://repo1.maven.org/maven2/org/%{name}/%{name}-native_%{scala_version}/%{version}/%{name}-native_%{scala_version}-%{version}.pom
Source105:      https://repo1.maven.org/maven2/org/%{name}/%{name}-scalap_%{scala_version}/%{version}/%{name}-scalap_%{scala_version}-%{version}.pom
Source106:      https://repo1.maven.org/maven2/org/%{name}/%{name}-xml_%{scala_version}/%{version}/%{name}-xml_%{scala_version}-%{version}.pom
BuildRequires:  ant-scala
BuildRequires:  jackson-annotations
BuildRequires:  jackson-core
BuildRequires:  jackson-databind
BuildRequires:  javapackages-local
BuildRequires:  joda-convert
BuildRequires:  joda-time
BuildRequires:  paranamer
BuildRequires:  scala
BuildRequires:  xmvn-install
BuildRequires:  xmvn-resolve
BuildArch:      noarch

%description
Json4s is a common AST for Scala JSON parsers.

%package ast
Summary:        The %{name} ast module

%description ast
Json4s is a common AST for Scala JSON parsers.

This package contains the ast module.

%package core
Summary:        The %{name} core module

%description core
Json4s is a common AST for Scala JSON parsers.

This package contains the core module.

%package ext
Summary:        The %{name} ext module

%description ext
Json4s is a common AST for Scala JSON parsers.

This package contains the ext module.

%package jackson
Summary:        The %{name} jackson module

%description jackson
Json4s is a common AST for Scala JSON parsers.

This package contains the jackson module.

%package native
Summary:        The %{name} native module

%description native
Json4s is a common AST for Scala JSON parsers.

This package contains the native module.

%package scalap
Summary:        The %{name} scalap module

%description scalap 
Json4s is a common AST for Scala JSON parsers.

This package contains the scalap module.

%package xml
Summary:        The %{name} xml module

%description xml
Json4s is a common AST for Scala JSON parsers.

This package contains the xml module.

%prep
%setup -q -a1

%{mvn_package} :json4s-{*}_%{scala_version} @1

%build
mkdir -p lib
build-jar-repository -s lib \
	jackson-annotations \
	jackson-core \
	jackson-databind \
	joda-convert \
	joda-time \
	paranamer/paranamer \

%{ant} \
	-Dscala.home=%{_datadir}/scala \
	package

%{mvn_artifact} %{SOURCE100} ast/target/%{name}-ast-%{version}.jar
%{mvn_artifact} %{SOURCE101} core/target/%{name}-core-%{version}.jar
%{mvn_artifact} %{SOURCE102} ext/target/%{name}-ext-%{version}.jar
%{mvn_artifact} %{SOURCE103} jackson/target/%{name}-jackson-%{version}.jar
%{mvn_artifact} %{SOURCE104} native/target/%{name}-native-%{version}.jar
%{mvn_artifact} %{SOURCE105} scalap/target/%{name}-scalap-%{version}.jar
%{mvn_artifact} %{SOURCE106} xml/target/%{name}-xml-%{version}.jar

%install
%mvn_install

%files ast -f .mfiles-ast
%doc README.md
%license LICENSE

%files core -f .mfiles-core

%files ext -f .mfiles-ext

%files jackson -f .mfiles-jackson

%files native -f .mfiles-native

%files scalap -f .mfiles-scalap

%files xml -f .mfiles-xml

%changelog
