#
# spec file for package akka
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


%global namedreltag %{nil}
%global namedversion %{version}%{?namedreltag}
%global scala_short_version 2.10
Name:           akka
Version:        2.3.16
Release:        0
Summary:        Scalable real-time transaction processing
License:        Apache-2.0
URL:            https://akka.io/
Source0:        %{name}-%{version}.tar.xz
# Default use sbt
Source1:        akka-build.xml
# Build only these sub-modules, cause: unavailable build deps
# TODO  akka-camel akka-contrib akka-durable-mailboxes akka-persistence akka-samples akka-zeromq
Source2:        https://repo1.maven.org/maven2/com/typesafe/akka/akka-actor_%{scala_short_version}/%{namedversion}/akka-actor_%{scala_short_version}-%{namedversion}.pom
Source3:        https://repo1.maven.org/maven2/com/typesafe/akka/akka-agent_%{scala_short_version}/%{namedversion}/akka-agent_%{scala_short_version}-%{namedversion}.pom
Source4:        https://repo1.maven.org/maven2/com/typesafe/akka/akka-cluster_%{scala_short_version}/%{namedversion}/akka-cluster_%{scala_short_version}-%{namedversion}.pom
Source5:        https://repo1.maven.org/maven2/com/typesafe/akka/akka-dataflow_%{scala_short_version}/%{namedversion}/akka-dataflow_%{scala_short_version}-%{namedversion}.pom
Source6:        https://repo1.maven.org/maven2/com/typesafe/akka/akka-kernel_%{scala_short_version}/%{namedversion}/akka-kernel_%{scala_short_version}-%{namedversion}.pom
Source7:        https://repo1.maven.org/maven2/com/typesafe/akka/akka-osgi_%{scala_short_version}/%{namedversion}/akka-osgi_%{scala_short_version}-%{namedversion}.pom
Source8:        https://repo1.maven.org/maven2/com/typesafe/akka/akka-remote_%{scala_short_version}/%{namedversion}/akka-remote_%{scala_short_version}-%{namedversion}.pom
Source9:        https://repo1.maven.org/maven2/com/typesafe/akka/akka-slf4j_%{scala_short_version}/%{namedversion}/akka-slf4j_%{scala_short_version}-%{namedversion}.pom
Source10:       https://repo1.maven.org/maven2/com/typesafe/akka/akka-transactor_%{scala_short_version}/%{namedversion}/akka-transactor_%{scala_short_version}-%{namedversion}.pom
Patch1:         akka-2.3.0-typesafe-config-1.3.0.patch
Patch2:         akka-2.3.16-typesafe-config-1.4.1.patch
BuildRequires:  ant
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local
BuildRequires:  javapackages-tools
BuildRequires:  mvn(com.google.protobuf:protobuf-java)
# typesafe-config
BuildRequires:  mvn(com.typesafe:config)
BuildRequires:  mvn(io.netty:netty)
BuildRequires:  mvn(org.osgi:osgi.cmpn)
BuildRequires:  mvn(org.osgi:osgi.core)
BuildRequires:  mvn(org.scala-lang:scala-compiler)
BuildRequires:  mvn(org.scala-lang:scala-library)
BuildRequires:  mvn(org.scala-stm:scala-stm_2.10)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.uncommons.maths:uncommons-maths)
# requires for akka-remote
BuildRequires:  protobuf-devel
BuildRequires:  xmvn-install
BuildRequires:  xmvn-resolve
Requires:       java-headless >= 1.8
BuildArch:      noarch

%description
Akka is a toolkit and run-time for building highly concurrent,
distributed, and fault tolerant event-driven applications on
the JVM.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q

cp -p %{SOURCE1} build.xml
sed -i "s|@VERSION@|%{namedversion}|" build.xml

%if %{?pkg_vcmp:%pkg_vcmp typesafe-config >= 1.3}%{!?pkg_vcmp:0}
%patch1 -p1
%endif
%if %{?pkg_vcmp:%pkg_vcmp typesafe-config >= 1.4}%{!?pkg_vcmp:0}
%patch2 -p1
%endif

# handle compatibility netty jar
sed -i -e "s|netty[.]jar|$(basename %{_javadir}/netty3.jar)|" build.xml

# use osgi 7.x apis
cp -p %{SOURCE7} osgi-pom.xml
%pom_change_dep :org.osgi.core :osgi.core osgi-pom.xml
%pom_change_dep :org.osgi.compendium :osgi.cmpn osgi-pom.xml

# spurious-executable-perm
chmod 644 LICENSE

%build

%{ant} dist doc

%{mvn_artifact} %{SOURCE2} target/%{name}-actor.jar
%{mvn_artifact} %{SOURCE3} target/%{name}-agent.jar
%{mvn_artifact} %{SOURCE4} target/%{name}-cluster.jar
%{mvn_artifact} %{SOURCE5} target/%{name}-dataflow.jar
%{mvn_artifact} %{SOURCE6} target/%{name}-kernel.jar
%{mvn_artifact} osgi-pom.xml target/%{name}-osgi.jar
%{mvn_artifact} %{SOURCE8} target/%{name}-remote.jar
%{mvn_artifact} %{SOURCE9} target/%{name}-slf4j.jar
%{mvn_artifact} %{SOURCE10} target/%{name}-transactor.jar

%install
%mvn_install -J target/apidocs/
cp -rp target/apidocs/* %{buildroot}%{_javadocdir}/%{name}

%files -f .mfiles
%license LICENSE
%doc CONTRIBUTING.md README.textile

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
