#
# spec file for package scala-stm
#
# Copyright (c) 2021 SUSE LLC
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


%global scala_short_version 2.10
Name:           scala-stm
Version:        0.7
Release:        0
Summary:        Software Transactional Memory for Scala
License:        BSD-3-Clause
Group:          Development/Libraries/Java
URL:            https://nbronson.github.io/scala-stm/
Source0:        https://github.com/nbronson/scala-stm/archive/release-%{version}.tar.gz
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  java-devel
BuildRequires:  javapackages-local
BuildRequires:  sbt
BuildRequires:  xmvn-install
BuildRequires:  xmvn-resolve
BuildRequires:  mvn(org.scala-lang:scala-compiler)
BuildRequires:  mvn(org.scala-lang:scala-library)
BuildConflicts: java >= 9
BuildConflicts: java-devel >= 9
BuildConflicts: java-headless >= 9
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
%setup -q -n %{name}-release-%{version}
# Cleanup
find -name '*.class' -print -delete
find -name '*.jar' -print -delete
# sb7_java-v1.2.tgz http://lpd.epfl.ch/gramoli/doc/sw/sb7_java-v1.2.tgz
rm -r lib/*

# get rid of sbt plugins
rm project/plugins.sbt

# patch build.sbt
sed -i -e '/% "test"/d' build.sbt
sed -i -e '/credentials/d' build.sbt
sed -i -e 's/\(scalaVersion :=\).*$/scalaVersion := "2.10.7"/' build.sbt
sed -i -e 's/sbt[.]version=.*/sbt.version=0.13.18/g' project/build.properties

# delete tests due to missing deps
rm -rf src/test
rm -rf dep-tests

cp -rL %{_datadir}/sbt/ivy-local .
mkdir boot

%{mvn_file} org.%{name}:%{name}_%{scala_short_version} %{name}

%build

export SBT_BOOT_DIR=$PWD/boot
export SBT_IVY_DIR=$PWD/ivy-local
sbt -Dsbt.log.noformat=true package makePom deliverLocal doc

# No test deps available

%install
# target/scala-2.10/scala-stm_2.10-0.7.jar
%{mvn_artifact} target/scala-%{scala_short_version}/%{name}_%{scala_short_version}-%{version}.pom target/scala-%{scala_short_version}/%{name}_%{scala_short_version}-%{version}.jar
%mvn_install -J target/scala-%{scala_short_version}/api/
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%doc README RELEASE-NOTES.txt
%license LICENSE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
