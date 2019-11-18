#
# spec file for package zinc
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


Name:           zinc
Version:        0.3.1
Release:        0
Summary:        Incremental scala compiler
License:        Apache-2.0
URL:            https://github.com/typesafehub/zinc
Source0:        https://github.com/typesafehub/zinc/archive/v%{version}.tar.gz
Source1:        http://repo1.maven.org/maven2/com/typesafe/zinc/zinc/%{version}/zinc-%{version}.pom
# ASL mandates that the licence file be included in redistributed source
Source2:        http://www.apache.org/licenses/LICENSE-2.0.txt
# Patch fixes compilation failure, which is probably caused by
# incompatible Scala version
Patch0:         0001-Fix-file-filtering.patch
BuildRequires:  javapackages-local
BuildRequires:  xmvn-install
BuildRequires:  xmvn-resolve
BuildRequires:  mvn(com.martiansoftware:nailgun-server)
BuildRequires:  mvn(org.scala-lang:scala-library)
BuildRequires:  mvn(org.scala-sbt:incremental-compiler)
BuildConflicts: java-devel >= 9
#!BuildRequires: sbt
BuildArch:      noarch

%description
Zinc is a stand-alone version of sbt's incremental compiler.

%prep
%setup -q
rm -rf src/scriptit dist nailgun project

%patch0 -p1

cp %{SOURCE1} pom.xml
cp %{SOURCE2} LICENSE.txt

%pom_xpath_remove "pom:dependency[pom:classifier='sources']"
%pom_change_dep :incremental-compiler org.scala-sbt:

%build
scalac -cp $(build-classpath sbt nailgun) src/main/scala/com/typesafe/zinc/*
jar cf zinc.jar com
%{mvn_artifact} pom.xml zinc.jar

%install
%mvn_install

%files -f .mfiles
%doc README.md
%license LICENSE.txt

%changelog
