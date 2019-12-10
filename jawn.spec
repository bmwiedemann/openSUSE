#
# spec file for package jawn
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
Name:           jawn
Version:        0.14.1
Release:        0
Summary:        A JSON parser
License:        MIT
Group:          Development/Libraries/Java
URL:            https://github.com/typelevel/jawn
Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}-%{version}-build.tar.xz
Source100:      https://repo1.maven.org/maven2/org/typelevel/%{name}-ast_%{scala_version}/%{version}/%{name}-ast_%{scala_version}-%{version}.pom
Source101:      https://repo1.maven.org/maven2/org/typelevel/%{name}-parser_%{scala_version}/%{version}/%{name}-parser_%{scala_version}-%{version}.pom
Source102:      https://repo1.maven.org/maven2/org/typelevel/%{name}-util_%{scala_version}/%{version}/%{name}-util_%{scala_version}-%{version}.pom
Source103:      https://repo1.maven.org/maven2/org/typelevel/%{name}-json4s_%{scala_version}/%{version}/%{name}-json4s_%{scala_version}-%{version}.pom
BuildRequires:  ant-scala
BuildRequires:  javapackages-local
BuildRequires:  json4s-jackson
BuildRequires:  scala
BuildRequires:  xmvn-install
BuildRequires:  xmvn-resolve
BuildArch:      noarch

%description
Jawn is a JSON parser that was designed to parse
JSON into an AST as quickly as possible.

%package ast
Summary:        A small AST
Group:          Development/Libraries/Java

%description ast
Jawn is a JSON parser that was designed to parse
JSON into an AST as quickly as possible.

This package contains a amall AST.

%package parser
Summary:        A generic JSON parser
Group:          Development/Libraries/Java

%description parser
Jawn is a JSON parser that was designed to parse
JSON into an AST as quickly as possible.

This package contains a generic JSON parser.

%package util
Summary:        A few helpful utilities
Group:          Development/Libraries/Java

%description util
Jawn is a JSON parser that was designed to parse
JSON into an AST as quickly as possible.

This package contains a few helpful utilities.

%package json4s
Summary:        Support to parse to json4s AST
Group:          Development/Libraries/Java

%description json4s
Jawn is a JSON parser that was designed to parse
JSON into an AST as quickly as possible.

This package contains support to parse to json4s AST.

%prep
%setup -q -a1

%{mvn_package} :%{name}-{*}_%{scala_version} @1

# Different versions were distributed with different
# groupIds and artifactIds
%{mvn_alias} org.typelevel: org.spire-math:
%{mvn_alias} org.typelevel:jawn-json4s{*} org.spire-math:json4s-support@1

%build
mkdir -p lib
build-jar-repository -s lib json4s

%{ant} \
	-Dscala.home=%{_datadir}/scala \
	package

%{mvn_artifact} %{SOURCE100} ast/target/%{name}-ast-%{version}.jar
%{mvn_artifact} %{SOURCE101} parser/target/%{name}-parser-%{version}.jar
%{mvn_artifact} %{SOURCE102} util/target/%{name}-util-%{version}.jar
%{mvn_artifact} %{SOURCE103} support/json4s/target/%{name}-json4s-%{version}.jar

%install
%mvn_install

%files ast -f .mfiles-ast
%doc README.md

%files parser -f .mfiles-parser

%files util -f .mfiles-util

%files json4s -f .mfiles-json4s

%changelog
