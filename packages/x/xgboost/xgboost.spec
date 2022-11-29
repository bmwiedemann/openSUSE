#
# spec file for package xgboost
#
# Copyright (c) 2022 SUSE LLC
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


Name:           xgboost
Version:        0.90
Release:        0
Summary:        Gradient Boosting (GBDT, GBRT or GBM) Library
License:        Apache-2.0
URL:            https://github.com/dmlc/%{name}
Source0:        %{name}-%{version}.tar.xz
Patch0:         xgboost-fix-big-endian.patch
Patch1:         use-python3.patch
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  maven-local
BuildRequires:  python3
BuildRequires:  mvn(com.esotericsoftware.kryo:kryo)
BuildRequires:  mvn(com.typesafe.akka:akka-actor_2.10)
BuildRequires:  mvn(commons-logging:commons-logging)
BuildRequires:  mvn(net.alchim31.maven:scala-maven-plugin)
BuildRequires:  mvn(org.codehaus.mojo:exec-maven-plugin)
BuildRequires:  mvn(org.scala-lang:scala-compiler)
BuildRequires:  mvn(org.scala-lang:scala-library)
BuildRequires:  mvn(org.scala-lang:scala-reflect)
#!BuildRequires: sbt

%description
Scalable, Portable and Distributed Gradient Boosting (GBDT, GBRT or
GBM) Library, for Python, R, Java, Scala, C++ and more. Runs on
single machine, Hadoop, Spark, Flink and DataFlow

%package javadoc
Summary:        Javadoc for %{name}
BuildArch:      noarch

%description javadoc
%{summary}

%prep
%setup -q
%ifarch s390x ppc64
%patch0
%endif
%patch1 -p1
pushd jvm-packages
%pom_remove_plugin :scalatest-maven-plugin
%pom_remove_plugin :scalastyle-maven-plugin
%pom_remove_plugin :maven-checkstyle-plugin

%pom_disable_module xgboost4j-example
%pom_disable_module xgboost4j-spark
%pom_disable_module xgboost4j-flink

%pom_xpath_set pom:project/pom:properties/pom:scala.version 2.10.7
%pom_xpath_set pom:project/pom:properties/pom:scala.binary.version 2.10

%build
pushd jvm-packages
%{mvn_build} -f -- \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
	-DaddScalacArgs="-nobootcp" -Dmaven.compiler.release=7 \
%endif
    -Dsource=7
popd

%install
pushd jvm-packages
%mvn_install
rm -f %{buildroot}%{_javadocdir}/%{name}/javadoc.sh
%fdupes -s %{buildroot}%{_javadocdir}
popd

%files -f jvm-packages/.mfiles
%license LICENSE

%files javadoc -f jvm-packages/.mfiles-javadoc
%license LICENSE

%changelog
