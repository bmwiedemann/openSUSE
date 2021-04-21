#
# spec file for package akka
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


%global namedreltag %{nil}
%global namedversion %{version}%{?namedreltag}
%global scala_short_version 2.10
Name:           akka
Version:        2.3.16
Release:        0
Summary:        Scalable real-time transaction processing
License:        Apache-2.0
URL:            http://akka.io/
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
Patch0:         akka-2.3.0-encoding.patch
Patch1:         akka-2.3.0-typesafe-config-1.3.0.patch
Patch2:         akka-2.3.16-typesafe-config-1.4.1.patch
BuildRequires:  ant
BuildRequires:  java-devel
BuildRequires:  javapackages-local
BuildRequires:  javapackages-tools
BuildRequires:  mvn(com.google.protobuf:protobuf-java)
# typesafe-config
BuildRequires:  mvn(com.typesafe:config)
BuildRequires:  mvn(io.netty:netty:3)
BuildRequires:  mvn(org.osgi:osgi.cmpn)
BuildRequires:  mvn(org.osgi:osgi.core)
BuildRequires:  mvn(org.scala-lang:scala-compiler)
BuildRequires:  mvn(org.scala-lang:scala-library)
BuildRequires:  mvn(org.scala-stm:scala-stm_2.10)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.uncommons.maths:uncommons-maths)
# requires for akka-remote
BuildRequires:  protobuf-devel
Requires:       java-headless
Requires:       mvn(com.google.protobuf:protobuf-java)
Requires:       mvn(com.typesafe:config)
Requires:       mvn(io.netty:netty:3)
Requires:       mvn(org.osgi:osgi.cmpn)
Requires:       mvn(org.osgi:osgi.core)
Requires:       mvn(org.scala-lang:scala-library)
Requires:       mvn(org.scala-stm:scala-stm_2.10)
Requires:       mvn(org.slf4j:slf4j-api)
Requires:       mvn(org.uncommons.maths:uncommons-maths)
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

%patch0 -p1
%if %{?pkg_vcmp:%pkg_vcmp typesafe-config >= 1.3}%{!?pkg_vcmp:0}
%patch1 -p1
%endif
%if %{?pkg_vcmp:%pkg_vcmp typesafe-config >= 1.4}%{!?pkg_vcmp:0}
%patch2 -p1
%endif

# handle compatibility netty jar
sed -i -e "s|netty[.]jar|$(basename %{_javadir}/netty3-*.jar)|" build.xml
cp -p %{SOURCE8} remote-pom.xml
%pom_xpath_set "pom:project/pom:dependencies/pom:dependency[pom:artifactId='netty']/pom:version" 3 remote-pom.xml

# use osgi 7.x apis
cp -p %{SOURCE7} osgi-pom.xml
%pom_change_dep :org.osgi.core :osgi.core osgi-pom.xml
%pom_change_dep :org.osgi.compendium :osgi.cmpn osgi-pom.xml

# spurious-executable-perm
chmod 644 LICENSE

%build

%{ant} dist doc

%install

mkdir -p %{buildroot}%{_javadir}/%{name}
cp -p target/%{name}-actor.jar %{buildroot}%{_javadir}/%{name}/
cp -p target/%{name}-agent.jar %{buildroot}%{_javadir}/%{name}/
cp -p target/%{name}-cluster.jar %{buildroot}%{_javadir}/%{name}/
cp -p target/%{name}-dataflow.jar %{buildroot}%{_javadir}/%{name}/
cp -p target/%{name}-kernel.jar %{buildroot}%{_javadir}/%{name}/
cp -p target/%{name}-osgi.jar %{buildroot}%{_javadir}/%{name}/
cp -p target/%{name}-remote.jar %{buildroot}%{_javadir}/%{name}/
cp -p target/%{name}-slf4j.jar %{buildroot}%{_javadir}/%{name}/
cp -p target/%{name}-transactor.jar %{buildroot}%{_javadir}/%{name}/

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 %{SOURCE2} %{buildroot}%{_mavenpomdir}/JPP.%{name}-%{name}-actor.pom
%add_maven_depmap JPP.%{name}-%{name}-actor.pom %{name}/%{name}-actor.jar

install -pm 644 %{SOURCE3} %{buildroot}%{_mavenpomdir}/JPP.%{name}-%{name}-agent.pom
%add_maven_depmap JPP.%{name}-%{name}-agent.pom %{name}/%{name}-agent.jar

install -pm 644 %{SOURCE4} %{buildroot}%{_mavenpomdir}/JPP.%{name}-%{name}-cluster.pom
%add_maven_depmap JPP.%{name}-%{name}-cluster.pom %{name}/%{name}-cluster.jar

install -pm 644 %{SOURCE5} %{buildroot}%{_mavenpomdir}/JPP.%{name}-%{name}-dataflow.pom
%add_maven_depmap JPP.%{name}-%{name}-dataflow.pom %{name}/%{name}-dataflow.jar

install -pm 644 %{SOURCE6} %{buildroot}%{_mavenpomdir}/JPP.%{name}-%{name}-kernel.pom
%add_maven_depmap JPP.%{name}-%{name}-kernel.pom %{name}/%{name}-kernel.jar

install -pm 644 osgi-pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-%{name}-osgi.pom
%add_maven_depmap JPP.%{name}-%{name}-osgi.pom %{name}/%{name}-osgi.jar

install -pm 644 remote-pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-%{name}-remote.pom
%add_maven_depmap JPP.%{name}-%{name}-remote.pom %{name}/%{name}-remote.jar

install -pm 644 %{SOURCE9} %{buildroot}%{_mavenpomdir}/JPP.%{name}-%{name}-slf4j.pom
%add_maven_depmap JPP.%{name}-%{name}-slf4j.pom %{name}/%{name}-slf4j.jar

install -pm 644 %{SOURCE10} %{buildroot}%{_mavenpomdir}/JPP.%{name}-%{name}-transactor.pom
%add_maven_depmap JPP.%{name}-%{name}-transactor.pom %{name}/%{name}-transactor.jar

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -rp target/apidocs/* %{buildroot}%{_javadocdir}/%{name}

%files -f .mfiles
%license LICENSE
%doc CONTRIBUTING.md README.textile

%files javadoc
%{_javadocdir}/%{name}
%license LICENSE

%changelog
